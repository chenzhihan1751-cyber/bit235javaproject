package au.edu.mp.testwikiapp;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

/**
 * MVC controller for the wiki pages.
 *
 * The controller is the C in MVC: it receives the request, asks the model for
 * data and returns the name of the Thymeleaf view that should be rendered.
 * Templates live in src/main/resources/templates.
 */
@Controller
public class WikiController {

    /** One wiki topic. A record keeps the model small and immutable. */
    public record Topic(String slug, String title, String summary, String body) {
    }

    private static final List<Topic> TOPICS = List.of(
            new Topic("spring-boot-basics", "Spring Boot basics",
                    "What Spring Boot adds on top of plain Java and Maven.",
                    "Spring Boot starts an embedded Tomcat server, creates the Spring "
                            + "application context and wires the beans for you. A single "
                            + "@SpringBootApplication class is the entry point, and the "
                            + "starter dependencies pull in everything the app needs."),
            new Topic("mvc-in-spring-boot", "MVC in Spring Boot",
                    "How a request travels from the browser to a template.",
                    "A request hits DispatcherServlet, which looks for a method on a "
                            + "@Controller that matches the URL. The method fills the Model "
                            + "and returns a view name; Thymeleaf renders that view back to "
                            + "the browser as HTML."),
            new Topic("thymeleaf-templates", "Thymeleaf templates",
                    "Writing HTML that the server can fill with data.",
                    "Templates are plain HTML files with th: attributes, for example "
                            + "th:each to loop over a list or th:text to print a value. They "
                            + "stay valid HTML, so a designer can open them in a browser "
                            + "without running the Java application."),
            new Topic("run-the-app", "Running the application",
                    "Starting the app from VS Code or from the command line.",
                    "Run TestwikiappApplication from VS Code, or build the jar with "
                            + "mvn package and start it with java -jar. When the log says "
                            + "\"Tomcat started on port 8080\", open http://127.0.0.1:8080.")
    );

    @GetMapping("/topics")
    public String topics(Model model) {
        model.addAttribute("topics", TOPICS);
        model.addAttribute("pageTitle", "Wiki topics");
        return "topics";
    }

    @GetMapping("/topics/{slug}")
    public String topic(@PathVariable String slug, Model model) {
        Topic topic = TOPICS.stream()
                .filter(t -> t.slug().equals(slug))
                .findFirst()
                .orElse(null);
        if (topic == null) {
            return "redirect:/topics";
        }
        model.addAttribute("topic", topic);
        model.addAttribute("pageTitle", topic.title());
        return "topic";
    }

    // "/" is not mapped on purpose: Spring Boot serves src/main/resources/static/index.html
    // for the context root, which keeps the URL as http://127.0.0.1:8080
}
