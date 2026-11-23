/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: AdminAccountRepository.java
 */
package au.edu.mp.wikiadminlogin.repository;

import au.edu.mp.wikiadminlogin.model.AdminAccount;

import java.util.Optional;

/**
 * The data access boundary for administrator accounts.
 *
 * <p>Part A has no database, but putting an interface here keeps the layering
 * honest: the service asks for an account and does not care where it came from.
 * In Part B the implementation can be swapped for one that talks to MySQL or
 * JPA, and neither the service nor the controller needs to change.</p>
 */
public interface AdminAccountRepository {

    /**
     * Looks up the one administrator account this stage of the wiki supports.
     *
     * @return the account wrapped in an Optional, or an empty Optional when no
     *         account has been configured
     */
    Optional<AdminAccount> findAdminAccount();
}
