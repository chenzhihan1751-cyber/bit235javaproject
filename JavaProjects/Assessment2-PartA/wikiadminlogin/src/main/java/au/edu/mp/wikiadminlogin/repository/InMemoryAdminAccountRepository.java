/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: InMemoryAdminAccountRepository.java
 */
package au.edu.mp.wikiadminlogin.repository;

import au.edu.mp.wikiadminlogin.model.AdminAccount;
import org.springframework.stereotype.Repository;

import java.util.Optional;

/**
 * The only implementation of AdminAccountRepository for Part A: the account
 * lives in a constant instead of a table.
 *
 * <p>The brief asks for one hard-coded username and password, and they are my
 * first name in lower case and 123. The @Repository annotation marks the class
 * as a bean, so Spring creates one instance and injects it into AuthService.</p>
 */
@Repository
public class InMemoryAdminAccountRepository implements AdminAccountRepository {

    /**
     * The user name is lower case on purpose: the service lower-cases whatever
     * the visitor types, so "Zhihan" and "zhihan" reach the same account.
     */
    private static final String HARD_CODED_USERNAME = "zhihan";

    /** The password required by the brief. */
    private static final String HARD_CODED_PASSWORD = "123";

    /** What the welcome message calls me. */
    private static final String DISPLAY_NAME = "Zhihan";

    /**
     * @return the one account, always present in this stage
     */
    @Override
    public Optional<AdminAccount> findAdminAccount() {
        return Optional.of(new AdminAccount(HARD_CODED_USERNAME, HARD_CODED_PASSWORD, DISPLAY_NAME));
    }
}
