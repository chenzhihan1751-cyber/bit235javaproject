/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: LoginForm.java
 */
package au.edu.mp.wikiadminlogin.model;

/**
 * Holds the two fields that the browser posts from the login page.
 *
 * <p>Spring needs a bean with a no-argument constructor and setter methods here,
 * because it creates the object first and then fills it in from the request
 * parameters ("username" and "password"), one setter call per field. A record
 * would not work for that: records have no setters.</p>
 */
public class LoginForm {

    private String username = "";
    private String password = "";

    /** @return the raw text typed into the username box, may be empty or null */
    public String getUsername() {
        return username;
    }

    /** Called by Spring while binding the submitted form values. */
    public void setUsername(String username) {
        this.username = username;
    }

    /** @return the raw text typed into the password box, may be empty or null */
    public String getPassword() {
        return password;
    }

    /** Called by Spring while binding the submitted form values. */
    public void setPassword(String password) {
        this.password = password;
    }
}
