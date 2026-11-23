/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: AuthService.java
 */
package au.edu.mp.wikiadminlogin.service;

import au.edu.mp.wikiadminlogin.model.AdminAccount;
import au.edu.mp.wikiadminlogin.model.LoginResult;
import au.edu.mp.wikiadminlogin.repository.AdminAccountRepository;
import org.springframework.stereotype.Service;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.util.Optional;

/**
 * The business rule of this application: does the submitted username and
 * password belong to the administrator account?
 *
 * <p>The check lives here and not in the controller, because the controller's
 * job is to move data between the browser and the view. Keeping the rule in one
 * place also means the same rule can be unit tested without starting a web
 * server, which is what AuthServiceTests does.</p>
 */
@Service
public class AuthService {

    /** The message for an empty field or a completely wrong pair. */
    private static final String FAILURE_MESSAGE = "The username or password is incorrect.";

    /** The account store, injected by constructor. */
    private final AdminAccountRepository accountRepository;

    /**
     * Constructor injection: Spring passes in the repository bean when it
     * builds this service. A final field plus a constructor is the preferred
     * form because the service can never be created half-filled.
     *
     * @param accountRepository the repository that holds the admin account
     */
    public AuthService(AdminAccountRepository accountRepository) {
        this.accountRepository = accountRepository;
    }

    /**
     * Checks the submitted credentials against the stored account.
     *
     * <p>The order of the checks matters. Empty input is rejected first, so the
     * user gets a message that tells them what to fix instead of a generic
     * rejection. Only after that are the two values compared.</p>
     *
     * @param username the text typed into the username box, may be null
     * @param password the text typed into the password box, may be null
     * @return a LoginResult that the controller puts into the model
     */
    public LoginResult authenticate(String username, String password) {
        // Blank input never reaches the comparison. isBlank() also catches a
        // field that holds only spaces, which trim() alone would not reject
        // once the value has been normalised.
        if (username == null || username.isBlank() || password == null || password.isBlank()) {
            return LoginResult.failure("Enter both a username and a password, then press Sign in.");
        }

        Optional<AdminAccount> found = accountRepository.findAdminAccount();

        // No account in the store means the application is misconfigured rather
        // than the visitor being wrong, but the visitor still sees a plain
        // refusal and the detail stays out of the page.
        if (found.isEmpty()) {
            return LoginResult.failure(FAILURE_MESSAGE);
        }

        AdminAccount account = found.get();

        // Usernames are not case sensitive in this wiki, so both sides are
        // trimmed and lowered before they are compared. The password is only
        // trimmed for stray spaces and is never lower-cased: passwords are case
        // sensitive.
        String submittedUser = username.trim().toLowerCase(java.util.Locale.ROOT);
        String submittedPassword = password.trim();

        boolean userMatches = equalsIgnoringTiming(submittedUser, account.username());
        boolean passwordMatches = equalsIgnoringTiming(submittedPassword, account.password());

        // Both halves have to match, so the two booleans are joined with &&.
        if (userMatches && passwordMatches) {
            return LoginResult.success(account);
        }

        // The same sentence is returned whether the username or the password
        // was wrong. A page that said "wrong password" would confirm to a
        // visitor that the username exists.
        return LoginResult.failure(FAILURE_MESSAGE);
    }

    /**
     * Compares two strings byte by byte without stopping at the first
     * difference.
     *
     * <p>String.equals() returns as soon as two characters differ, so the time
     * it takes depends slightly on how much of the value was correct. That
     * timing is not worth attacking in a first-year project, but
     * MessageDigest.isEqual() is the standard library call for this job and it
     * costs one line, so there is no reason to use the weaker comparison.</p>
     *
     * @param submitted the value typed by the visitor
     * @param stored the value held by the repository
     * @return true when both strings are identical
     */
    private boolean equalsIgnoringTiming(String submitted, String stored) {
        // getBytes() needs a charset; UTF-8 is named explicitly so the result
        // does not depend on the machine's default encoding.
        byte[] left = submitted.getBytes(StandardCharsets.UTF_8);
        byte[] right = stored.getBytes(StandardCharsets.UTF_8);
        return MessageDigest.isEqual(left, right);
    }
}
