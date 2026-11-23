/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: AuthServiceTests.java
 */
package au.edu.mp.wikiadminlogin;

import au.edu.mp.wikiadminlogin.model.AdminAccount;
import au.edu.mp.wikiadminlogin.model.LoginResult;
import au.edu.mp.wikiadminlogin.repository.AdminAccountRepository;
import au.edu.mp.wikiadminlogin.repository.InMemoryAdminAccountRepository;
import au.edu.mp.wikiadminlogin.service.AuthService;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Unit tests for the credential check.
 *
 * <p>No Spring context is started here. The service only needs a repository, so
 * the real one is passed in directly; that keeps the test fast and proves the
 * service really is independent of the web layer.</p>
 */
class AuthServiceTests {

    /** The service under test, built with the in-memory account. */
    private final AuthService authService = new AuthService(new InMemoryAdminAccountRepository());

    /** @return the result of checking this pair of values */
    private LoginResult check(String username, String password) {
        return authService.authenticate(username, password);
    }

    /** The account from the brief: zhihan / 123 is accepted. */
    @Test
    void acceptsTheStoredCredentials() {
        LoginResult result = check("zhihan", "123");
        assertTrue(result.authenticated());
        assertEquals("Zhihan", result.account().displayName());
    }

    /** Usernames are not case sensitive, so ZHIHAN must also work. */
    @Test
    void ignoresTheCaseOfTheUsername() {
        assertTrue(check("ZHIHAN", "123").authenticated());
    }

    /** Spaces around the username are trimmed before the comparison. */
    @Test
    void trimsSpacesAroundTheUsername() {
        assertTrue(check("  zhihan  ", "123").authenticated());
    }

    /** A wrong password fails and carries no account. */
    @Test
    void rejectsAWrongPassword() {
        LoginResult result = check("zhihan", "124");
        assertFalse(result.authenticated());
        assertNull(result.account());
    }

    /** Passwords are case sensitive, so 123 cannot be typed as 123a. */
    @Test
    void rejectsAPasswordWithExtraCharacters() {
        assertFalse(check("zhihan", "1234").authenticated());
    }

    /** An unknown username fails. */
    @Test
    void rejectsAnUnknownUsername() {
        assertFalse(check("admin", "123").authenticated());
    }

    /** Two empty fields are rejected with the message that asks for input. */
    @Test
    void rejectsEmptyInput() {
        LoginResult result = check("", "");
        assertFalse(result.authenticated());
        assertTrue(result.message().startsWith("Enter both"));
    }

    /** A null value must not throw a NullPointerException. */
    @Test
    void handlesNullWithoutCrashing() {
        assertFalse(check(null, null).authenticated());
        assertFalse(check("zhihan", null).authenticated());
    }

    /** An empty repository is treated as a failed login, not an exception. */
    @Test
    void failsWhenNoAccountIsStored() {
        AdminAccountRepository emptyStore = () -> Optional.empty();
        AuthService service = new AuthService(emptyStore);
        LoginResult result = service.authenticate("zhihan", "123");
        assertFalse(result.authenticated());
    }

    /** The success result also builds the greeting the welcome page shows. */
    @Test
    void successMessageUsesTheDisplayName() {
        AdminAccount account = new AdminAccount("zhihan", "123", "Zhihan");
        LoginResult result = LoginResult.success(account);
        assertEquals("Welcome, Zhihan.", result.message());
    }
}
