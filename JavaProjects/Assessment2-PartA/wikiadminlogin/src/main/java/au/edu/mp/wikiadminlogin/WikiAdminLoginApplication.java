/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: WikiAdminLoginApplication.java
 *
 * This is the entry point of the Spring Boot application.
 */
package au.edu.mp.wikiadminlogin;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Starts the embedded Tomcat server and the Spring application context.
 *
 * <p>@SpringBootApplication is three annotations in one: it marks this class as
 * a configuration class, switches on auto-configuration (which is what wires up
 * Tomcat and Thymeleaf without any XML), and tells Spring to scan the
 * au.edu.mp.wikiadminlogin package and its sub-packages for beans. That scan is
 * how the controller, the service and the repository find each other.</p>
 */
@SpringBootApplication
public class WikiAdminLoginApplication {

    /**
     * main() is the ordinary Java entry point. SpringApplication.run() creates
     * the application context, starts Tomcat on the configured port and then
     * blocks until the process is stopped.
     */
    public static void main(String[] args) {
        SpringApplication.run(WikiAdminLoginApplication.class, args);
    }
}
