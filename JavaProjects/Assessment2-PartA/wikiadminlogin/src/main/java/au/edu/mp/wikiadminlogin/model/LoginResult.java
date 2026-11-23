/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: LoginResult.java
 */
package au.edu.mp.wikiadminlogin.model;

/**
 * The answer the service gives back after checking a username and password.
 *
 * <p>Returning an object instead of a bare boolean keeps two facts together:
 * whether the login worked, and the sentence the view should show. The account
 * is only present when the login succeeded, so the success factory is the one
 * place that sets it.</p>
 *
 * @param authenticated true when both fields matched the stored account
 * @param message the text shown to the user, either way
 * @param account the account that was matched, or null on failure
 */
public record LoginResult(boolean authenticated, String message, AdminAccount account) {

    /**
     * Builds a successful result.
     *
     * @param account the account whose credentials were matched
     * @return a result with authenticated set to true
     */
    public static LoginResult success(AdminAccount account) {
        return new LoginResult(true, "Welcome, " + account.displayName() + ".", account);
    }

    /**
     * Builds a failed result. The account is left as null because no account
     * was matched.
     *
     * @param message the reason shown on the error page
     * @return a result with authenticated set to false
     */
    public static LoginResult failure(String message) {
        return new LoginResult(false, message, null);
    }
}
