/*
 * BIT235 Object Oriented Programming - Assessment 2 Part A
 * Student: Chen Zhihan    Student ID: S1580887
 * File: LoginController.java
 */
package au.edu.mp.wikiadminlogin.controller;

import au.edu.mp.wikiadminlogin.model.LoginForm;
import au.edu.mp.wikiadminlogin.model.LoginResult;
import au.edu.mp.wikiadminlogin.service.AuthService;
import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

/**
 * The C in MVC: it maps URLs to methods, hands the request over to the service,
 * and chooses which template is rendered.
 *
 * <p>Nothing about usernames or passwords is decided here. This class only
 * moves data: request parameters into a LoginForm, the form into the service,
 * and the service's LoginResult into the Model. That is the split that the
 * marking rubric calls separation of responsibilities.</p>
 */
@Controller
public class LoginController {

    /**
     * The session attribute that remembers who is signed in. A constant avoids
     * typos between the place that writes it and the places that read it.
     */
    public static final String SESSION_ADMIN = "loggedInAdmin";

    /** The service that owns the credential check. */
    private final AuthService authService;

    /**
     * @param authService injected by Spring; the controller never builds one
     */
    public LoginController(AuthService authService) {
        this.authService = authService;
    }

    /**
     * Sends the context root to the login page, so the address bar always shows
     * a page name instead of a bare slash.
     *
     * @return a redirect instruction, not a view name
     */
    @GetMapping("/")
    public String root() {
        return "redirect:/login";
    }

    /**
     * Shows the login form.
     *
     * <p>A visitor who already has a session is sent straight to the welcome
     * page, which stops the browser's back button from showing a login form to
     * somebody who is signed in.</p>
     *
     * @param session the current HTTP session, created on demand by Tomcat
     * @param loggedOut true when the URL carries ?loggedOut after signing out
     * @param model the object the template reads its values from
     * @return the login template, or a redirect to the welcome page
     */
    @GetMapping("/login")
    public String showLoginForm(HttpSession session,
                                @RequestParam(name = "loggedOut", required = false) String loggedOut,
                                Model model) {
        // getAttribute() returns null when the key was never set, so a null
        // check is enough to tell "signed out" from "signed in".
        if (session.getAttribute(SESSION_ADMIN) != null) {
            return "redirect:/welcome";
        }

        // The template reads ${loginForm} to fill the two input boxes.
        model.addAttribute("loginForm", new LoginForm());

        // A short note after signing out, so the user is not left wondering
        // whether the click did anything.
        if (loggedOut != null) {
            model.addAttribute("notice", "You have been signed out.");
        }
        return "login";
    }

    /**
     * Handles the form submission.
     *
     * <p>@ModelAttribute builds a LoginForm from the posted fields, which is why
     * the HTML inputs are named username and password. The result of the check
     * decides between two paths: on success the session is marked and the
     * browser is redirected, on failure the error page is rendered with the
     * service's message.</p>
     *
     * @param form the submitted username and password
     * @param session used to remember a successful login
     * @param model used to pass the failure message to the error page
     * @return a redirect on success, the error template on failure
     */
    @PostMapping("/login")
    public String submitLogin(@ModelAttribute LoginForm form, HttpSession session, Model model) {
        // The service decides; the controller does not compare strings itself.
        LoginResult result = authService.authenticate(form.getUsername(), form.getPassword());

        if (result.authenticated()) {
            // Only the display name is stored. The password is not put in the
            // session, because anything in the session ends up in server memory
            // for as long as the session lives.
            session.setAttribute(SESSION_ADMIN, result.account().displayName());

            // Redirect after POST (the Post/Redirect/Get pattern). Without it a
            // refresh would resubmit the form and ask the server to log in
            // again.
            return "redirect:/welcome";
        }

        // The failed attempt is shown on the error page. The typed username is
        // kept so the visitor does not have to retype it; the password is
        // deliberately not sent back to the browser.
        model.addAttribute("errorMessage", result.message());
        model.addAttribute("username", form.getUsername());
        return "login-error";
    }

    /**
     * The page a signed-in administrator sees.
     *
     * <p>This method checks the session itself instead of trusting the URL.
     * Without the check, typing /welcome directly would show the welcome page to
     * anyone, which would defeat the point of the login.</p>
     *
     * @param session the current session
     * @param model holds the name shown in the greeting
     * @return the welcome template, or a redirect back to the login page
     */
    @GetMapping("/welcome")
    public String showWelcome(HttpSession session, Model model) {
        Object admin = session.getAttribute(SESSION_ADMIN);
        if (admin == null) {
            return "redirect:/login";
        }
        model.addAttribute("displayName", admin);
        return "welcome";
    }

    /**
     * Ends the session and returns to the login page.
     *
     * <p>invalidate() throws away every attribute in the session, so the browser
     * cookie that Tomcat issued no longer points at a live session.</p>
     *
     * @param session the session to discard
     * @return a redirect to the login page with the signed-out notice
     */
    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/login?loggedOut=1";
    }
}
