# testwikiapp - BIT235 Week 7 (Spring Boot, MVC)

A small Spring Boot web application built for the Week 7 homework:
*Web App Development Preparation*.

Student: Chen Zhihan (S1580887), Melbourne Polytechnic BIT235.

## Stack

| Item | Value |
|---|---|
| Spring Boot | 4.1.2 |
| Java | 21 (JDK 21) |
| Build | Maven (`mvnw` wrapper included) |
| Dependencies | Spring Web (MVC + embedded Tomcat), Thymeleaf, Spring Boot DevTools |
| Generated with | Spring Initializr (VS Code extension / start.spring.io) |
| Group ID / Artifact | `au.edu.mp` / `testwikiapp` |
| Packaging | jar |

## What is in the project

```
src/main/java/au/edu/mp/testwikiapp/
    TestwikiappApplication.java   entry point, @SpringBootApplication
    WikiController.java           the C in MVC: /topics and /topics/{slug}
src/main/resources/
    static/index.html             home page, CSS embedded in the head
    static/about.html             about page
    static/css/wiki.css           shared stylesheet
    templates/topics.html         Thymeleaf view: list of topics
    templates/topic.html          Thymeleaf view: one topic
    application.properties        port 8080, Thymeleaf cache off
```

## Run it

From VS Code: open `TestwikiappApplication.java` and press **Run**, or use the
integrated terminal:

```powershell
$env:JAVA_HOME="C:\ComPackageSet\openjdk-21.0.2_windows-x64_bin\jdk-21.0.2"
mvn spring-boot:run
```

Then open <http://127.0.0.1:8080>.

## Pages

| URL | Rendered by |
|---|---|
| `/` | `static/index.html` (static welcome page) |
| `/topics` | `WikiController.topics()` + `topics.html` |
| `/topics/{slug}` | `WikiController.topic()` + `topic.html` |
| `/about.html` | static file |

## Screenshots

`doc/screenshots/` holds the screenshots used in the submitted document:

| File | Shows |
|---|---|
| `01_extension_pack.png` | Extensions view filtered by "spring boot" - Spring Boot Extension Pack installed |
| `02_spring_initializr.png` | Spring Initializr Java Support installed |
| `03_spring_boot_run.png` | `mvn spring-boot:run` output, Tomcat on port 8080 |
| `04_home_page.png` | home page |
| `05_topics_page.png` | topics list from the controller |
| `06_topic_page.png` | a single topic page |
