/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: AdminAccount.java
 */
package au.edu.mp.wikiadminlogin.model;

/**
 * One administrator account, as the rest of the application sees it.
 *
 * <p>It is a record, so the compiler generates the constructor, the three
 * accessor methods, equals(), hashCode() and toString(). Nothing can change a
 * record after it is built, which suits an account that is loaded from storage
 * and only read afterwards.</p>
 *
 * @param username the login name, stored in lower case
 * @param password the plain password for this part of the assessment
 * @param displayName the name shown in the welcome message
 */
public record AdminAccount(String username, String password, String displayName) {
}
