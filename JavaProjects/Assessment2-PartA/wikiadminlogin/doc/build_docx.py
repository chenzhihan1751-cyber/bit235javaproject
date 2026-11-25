"""
BIT235 Assessment 2 Part A - build the submission document.

Student: Chen Zhihan  ID: S1580887

Reads the Java sources and the screenshots from this project, so the code
listing in the document always matches the files that were built and run.

Run from the project folder:
    python doc/build_docx.py
"""

import os
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
DOC_DIR = ROOT / "doc"
SHOTS = DOC_DIR / "screenshots"
SRC = ROOT / "src"

INK = RGBColor(0x17, 0x15, 0x26)
BRAND = RGBColor(0x3B, 0x2A, 0x72)
MUTED = RGBColor(0x5B, 0x5A, 0x72)
GOLD = RGBColor(0x8A, 0x66, 0x1C)

STUDENT = "Chen Zhihan"
STUDENT_ID = "S1580887"
REPO = "https://github.com/chenzhihan1751-cyber/bit235javaproject"


# ---------------------------------------------------------------- helpers

def set_cell_shading(cell, hex_fill):
    """Paint a table cell background. python-docx has no direct API for this."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    tc_pr.append(shd)


def set_table_borders(table, color="D9D4EA", size="4"):
    """Thin grey borders on every side of every cell."""
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), size)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tbl_pr.append(borders)


def add_page_number(paragraph):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = "PAGE"
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(begin)
    run._r.append(instr)
    run._r.append(end)


def body(doc, text, size=10.5, space_after=7, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.color.rgb = INK
    run.italic = italic
    return p


def bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.12
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.color.rgb = INK
    return p


def numbered(doc, text):
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.12
    run = p.add_run(text)
    run.font.size = Pt(10.5)
    run.font.color.rgb = INK
    return p


def heading(doc, text, level=1):
    h = doc.add_heading(level=level)
    run = h.add_run(text)
    run.font.name = "Calibri"
    if level == 1:
        run.font.size = Pt(14)
        run.font.color.rgb = BRAND
        h.paragraph_format.space_before = Pt(16)
    elif level == 2:
        run.font.size = Pt(11.5)
        run.font.color.rgb = INK
        h.paragraph_format.space_before = Pt(10)
    else:
        run.font.size = Pt(10.5)
        run.font.color.rgb = MUTED
        h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(4)
    return h


def code_block(doc, text, size=8):
    """One-cell table with a tinted background; keeps long lines inside the page."""
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_shading(cell, "F6F4FC")
    set_table_borders(table, "E2DDF2", "4")
    cell.width = Cm(16.2)

    para = cell.paragraphs[0]
    para.paragraph_format.space_before = Pt(4)
    para.paragraph_format.space_after = Pt(4)
    para.paragraph_format.line_spacing = 1.0
    run = para.add_run(text.rstrip("\n"))
    run.font.name = "Consolas"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Consolas")
    run.font.size = Pt(size)
    run.font.color.rgb = INK
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table


def landscape_section(doc):
    """A landscape page, so a full desktop screenshot can be printed large."""
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.LANDSCAPE
    s.page_width = Cm(29.7)
    s.page_height = Cm(21.0)
    s.left_margin = Cm(1.6)
    s.right_margin = Cm(1.6)
    s.top_margin = Cm(1.5)
    s.bottom_margin = Cm(1.3)
    return s


def portrait_section(doc):
    """Back to A4 portrait for the rest of the document."""
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.PORTRAIT
    s.page_width = Cm(21.0)
    s.page_height = Cm(29.7)
    s.left_margin = Cm(2.4)
    s.right_margin = Cm(2.4)
    s.top_margin = Cm(2.0)
    s.bottom_margin = Cm(2.0)
    return s


def figure(doc, filename, caption, width_cm=15.6):
    path = SHOTS / filename
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(str(path), width=Cm(width_cm))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(10)
    run = cap.add_run(caption)
    run.font.size = Pt(8.5)
    run.italic = True
    run.font.color.rgb = MUTED


def data_table(doc, headers, rows, widths=None, size=9):
    table = doc.add_table(rows=1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)
    hdr = table.rows[0]
    for i, text in enumerate(headers):
        cell = hdr.cells[i]
        if text:
            set_cell_shading(cell, "EFEBF9")
        para = cell.paragraphs[0]
        para.paragraph_format.space_after = Pt(2)
        run = para.add_run(text)
        run.bold = True
        run.font.size = Pt(size)
        run.font.color.rgb = BRAND
    for row in rows:
        cells = table.add_row().cells
        for i, text in enumerate(row):
            para = cells[i].paragraphs[0]
            para.paragraph_format.space_after = Pt(2)
            run = para.add_run(text)
            run.font.size = Pt(size)
            run.font.color.rgb = INK
    if widths:
        for row in table.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table


def read_source(rel_path):
    return (ROOT / rel_path).read_text(encoding="utf-8")


# ---------------------------------------------------------------- document

doc = Document()

# Base styles
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
normal.font.size = Pt(10.5)
normal.paragraph_format.space_after = Pt(7)

section = doc.sections[0]
section.page_width = Cm(21.0)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.0)
section.bottom_margin = Cm(2.0)
section.left_margin = Cm(2.4)
section.right_margin = Cm(2.4)

# Footer: name and ID on the left, page number on the right
footer_p = section.footer.paragraphs[0]
footer_p.text = ""
run = footer_p.add_run(f"BIT235 Assessment 2 Part A  |  {STUDENT} ({STUDENT_ID})  |  Page ")
run.font.size = Pt(8)
run.font.color.rgb = MUTED
add_page_number(footer_p)

# ---------------------------------------------------------------- cover

for _ in range(3):
    doc.add_paragraph()

p = doc.add_paragraph()
run = p.add_run("BIT235 Object Oriented Programming")
run.font.size = Pt(12)
run.font.color.rgb = GOLD
run.bold = True
p.paragraph_format.space_after = Pt(4)

p = doc.add_paragraph()
run = p.add_run("Assessment 2, Part A")
run.font.size = Pt(26)
run.font.color.rgb = BRAND
run.bold = True
p.paragraph_format.space_after = Pt(2)

p = doc.add_paragraph()
run = p.add_run("Wiki administrator login with Spring Boot")
run.font.size = Pt(14)
run.font.color.rgb = INK
p.paragraph_format.space_after = Pt(26)

data_table(
    doc,
    ["", ""],
    [
        ["Student", STUDENT],
        ["Student ID", STUDENT_ID],
        ["Course", "BIT235 Object Oriented Programming (FMP), 2026 Semester 5"],
        ["Assessment", "Assessment 2, Part A: Wiki Administrator Login (20%)"],
        ["Submitted", "23 November 2026"],
        ["GitHub repository", REPO],
        ["Project folder in the repository", "JavaProjects/Assessment2-PartA/wikiadminlogin"],
        ["Repository access", "public"],
    ],
    widths=[5.2, 11.0],
    size=9.5,
)

body(doc, "The repository is public, so the code and the commit history can be opened "
          "without an invitation. The same commit is inside the zip that accompanies this "
          "document, together with the screenshots and the logs referenced in the sections "
          "below.", space_after=4)

doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

# ---------------------------------------------------------------- 1

heading(doc, "1. What this submission is")
body(doc, "The submission is one Spring Boot project called wikiadminlogin. It serves a "
          "login page, checks the username and password against a single hard-coded "
          "administrator account, and then shows either a welcome message or a rejection. "
          "Part A has no database, so the account is kept in a repository class. Part B "
          "replaces that class and leaves the controller and the service alone.")
body(doc, "The account is zhihan with the password 123, which is my first name in lower "
          "case plus 123 as the brief asks. The login page prints the account on screen so "
          "a marker can try it without hunting through the code. That hint has to disappear "
          "in Part B.")
body(doc, "Everything runs from the Maven build. There is no database to create, no SQL "
          "script to run and no server to install, because Spring Boot starts its own "
          "Tomcat inside the Java process.")

# ---------------------------------------------------------------- 2

heading(doc, "2. Running the project")
body(doc, "The lab image already has JDK 21 and Maven 3.9. From the project folder the "
          "first line below is all that is needed. The last two lines are the address to open "
          "once the log says the server has started.")
code_block(doc, "cd wikiadminlogin\nmvn spring-boot:run\n\n# then open\nhttp://127.0.0.1:8081")
body(doc, "The console ends with these four lines. They are copied from doc/run-console.log, "
          "which was written during the run that produced the screenshots in this document.")
code_block(doc,
           "Tomcat initialized with port 8081 (http)\n"
           "Starting service [Tomcat]\n"
           "Tomcat started on port 8081 (http) with context path '/'\n"
           "Started WikiAdminLoginApplication in 2.024 seconds (process running for 2.63)", size=8)
body(doc, "The port is 8081 instead of the usual 8080 because the Week 7 wiki project was "
          "still running on 8080 on this machine and I did not want the two applications "
          "fighting for the same port while I compared them. It is one line in "
          "application.properties (server.port=8081) and can be changed back without "
          "touching any Java code.")
body(doc, "Two other ways in: run WikiAdminLoginApplication from VS Code, or run "
          "mvn package and then java -jar target/wikiadminlogin-0.0.1-SNAPSHOT.jar. All "
          "three start the same embedded Tomcat on the same port.")

# ---------------------------------------------------------------- 3

heading(doc, "3. How the code is organised")
body(doc, "The packages follow the three layers the rubric asks for, plus a model package "
          "for the objects that travel between them.")
data_table(
    doc,
    ["File", "Responsibility"],
    [
        ["controller/LoginController.java", "Maps the four URLs, moves data between the request, the service and the views"],
        ["service/AuthService.java", "Decides whether the submitted pair matches the stored account, and owns the messages"],
        ["repository/AdminAccountRepository.java", "Interface the service depends on; hides where accounts live"],
        ["repository/InMemoryAdminAccountRepository.java", "The hard-coded account behind that interface"],
        ["model/AdminAccount.java", "Record for one administrator: username, password, display name"],
        ["model/LoginForm.java", "Bean that receives the two posted fields"],
        ["model/LoginResult.java", "What the service returns: matched or not, the message, the account"],
        ["templates/*.html", "Four Thymeleaf views: login, login-error, welcome, error"],
        ["static/css/wiki.css", "One stylesheet shared by all four pages"],
        ["src/test/.../AuthServiceTests.java", "Ten JUnit tests for the credential rule"],
    ],
    widths=[6.3, 9.9],
)
body(doc, "The split is not decoration. The controller deals in HTTP and knows nothing about "
          "passwords; the service deals in passwords and knows nothing about requests; the "
          "repository is the only place that knows the account is a constant rather than a "
          "table row. When Part B adds MySQL, the InMemory class is replaced by a JPA "
          "repository and AuthService does not change, because it only ever asked for "
          "Optional<AdminAccount>.")
body(doc, "The service takes its repository through the constructor rather than creating "
          "one with new. That is what makes AuthServiceTests possible: the test hands the "
          "service a one-line lambda that returns an empty Optional, and the \"no account "
          "stored\" branch is covered without a database or a Spring context.")

heading(doc, "3.1 The project in VS Code", level=2)
body(doc, "Figures 1 and 2 on the two landscape pages that follow are whole VS Code windows, "
          "not cropped pictures of one panel, and they are printed sideways so the text in "
          "them stays readable. Figure 1 shows the explorer on the left with the four "
          "packages under src/main/java, the static/css and templates folders under "
          "resources, and the single test class under src/test. In the middle "
          "AuthService.java is open at the javadoc comment for authenticate(), and at the "
          "bottom the integrated terminal still holds the start-up log from "
          "mvn spring-boot:run.")
body(doc, "Figure 2 was taken in the same window after the run was stopped. The terminal now "
          "holds the output of mvn test: the one test class, the ten test methods, and "
          "BUILD SUCCESS. The prompt at the bottom is the project folder, so the screenshot "
          "also shows where the command was typed. The console code page is set to UTF-8 "
          "(chcp 65001) before Maven runs, which is why the Chinese characters in the "
          "project path print correctly instead of turning into boxes.")

landscape_section(doc)
figure(doc, "06-vscode-project-and-run.png",
       "Figure 1: the project in VS Code with the app started from the integrated terminal "
       "(Tomcat on port 8081)", width_cm=26.0)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
figure(doc, "07-vscode-tests.png",
       "Figure 2: mvn test in the integrated terminal, 10 tests, 0 failures",
       width_cm=26.0)
portrait_section(doc)

# ---------------------------------------------------------------- 4

heading(doc, "4. One request from click to page")
body(doc, "The sequence below is what I would walk through in the demonstration. Class and "
          "method names are the ones in the code.")
numbered(doc, "The browser asks for /login. DispatcherServlet matches the URL against "
              "LoginController.showLoginForm, which is annotated @GetMapping(\"/login\").")
numbered(doc, "The method puts a new LoginForm in the Model and returns the string "
              "\"login\". The Thymeleaf view resolver turns that name into "
              "templates/login.html; Thymeleaf evaluates the th:* attributes on the server "
              "and the browser receives plain HTML.")
numbered(doc, "The form posts to the same /login address. The HTTP method is different, so "
              "Spring routes it to submitLogin, annotated @PostMapping(\"/login\").")
numbered(doc, "@ModelAttribute builds the LoginForm from the two request parameters, "
              "calling setUsername and setPassword because the inputs are named username "
              "and password.")
numbered(doc, "The controller calls authService.authenticate(username, password). The "
              "service asks the repository for the account, normalises the input and "
              "compares both halves.")
numbered(doc, "On a match the controller writes the display name into the HttpSession and "
              "returns \"redirect:/welcome\". The browser receives a 302 and fetches the "
              "welcome page; a refresh therefore cannot resubmit the form.")
numbered(doc, "On that GET, showWelcome reads the session attribute. Present: the name "
              "goes into the Model and welcome.html is rendered. Absent: the visitor is "
              "redirected to /login, so typing /welcome by hand shows nothing.")
numbered(doc, "On a mismatch submitLogin puts the service message and the typed username in "
              "the Model and returns \"login-error\", which renders the error page with a "
              "link back to the form.")

# ---------------------------------------------------------------- 5

heading(doc, "5. Task (a): the login page and the error pages")
body(doc, "Figure 3 is the login page. The two fields are ordinary HTML inputs inside a form "
          "with method=\"post\" and action=\"/login\". Posting means the password travels in "
          "the request body, so it never appears in the address bar or in the browser "
          "history. Both inputs carry required, which lets the browser stop an empty "
          "submission before a request is made; the server checks for empty values as well, "
          "because the attribute can be removed in the developer tools.")
figure(doc, "01-login-page.png", "Figure 3: GET http://127.0.0.1:8081/login, the page a visitor sees first")

body(doc, "The page is a Thymeleaf template, not a static file. The stylesheet link uses "
          "th:href=\"@{/css/wiki.css}\", which rewrites the address if the application is "
          "ever deployed under a context path, and the username box uses "
          "th:value=\"${loginForm.username}\" so a rejected name survives a round trip.")
body(doc, "There are two error templates, and the reason is practical. login-error.html is "
          "returned by the controller when the credentials are wrong: it needs the message "
          "and the attempted username, both of which the controller puts in the Model. "
          "error.html is Spring Boot's error view for anything else, such as an address that "
          "does not exist; Boot fills that page with status and error instead. Sharing one "
          "file between the two paths would mean one of them always has model attributes "
          "missing.")
figure(doc, "02-error-page.png", "Figure 4: the error page after posting zhihan with the wrong password")

body(doc, "Figure 4 shows the rejection. The message is the same one a wrong username "
          "produces, which is deliberate: a page that said \"wrong password\" would confirm "
          "to a stranger that the username exists. The typed username is echoed back so it "
          "can be corrected rather than retyped, and the password is not echoed at all.")
figure(doc, "05-not-found.png", "Figure 5: the same error.html template serving a 404 for an address that does not exist")

# ---------------------------------------------------------------- 6

heading(doc, "6. Task (b): checking the submitted credentials")
body(doc, "The comparison lives in AuthService.authenticate. The controller never compares "
          "strings; it only passes the two values on and looks at the result.")
code_block(doc,
           'public LoginResult authenticate(String username, String password) {\n'
           '    if (username == null || username.isBlank()\n'
           '            || password == null || password.isBlank()) {\n'
           '        return LoginResult.failure(\n'
           '                "Enter both a username and a password, then press Sign in.");\n'
           '    }\n'
           '\n'
           '    Optional<AdminAccount> found = accountRepository.findAdminAccount();\n'
           '    if (found.isEmpty()) {\n'
           '        return LoginResult.failure(FAILURE_MESSAGE);\n'
           '    }\n'
           '\n'
           '    AdminAccount account = found.get();\n'
           '    String submittedUser     = username.trim().toLowerCase(Locale.ROOT);\n'
           '    String submittedPassword = password.trim();\n'
           '\n'
           '    boolean userMatches     = equalsIgnoringTiming(submittedUser, account.username());\n'
           '    boolean passwordMatches = equalsIgnoringTiming(submittedPassword, account.password());\n'
           '\n'
           '    if (userMatches && passwordMatches) {\n'
           '        return LoginResult.success(account);\n'
           '    }\n'
           '    return LoginResult.failure(FAILURE_MESSAGE);\n'
           '}', size=8)

body(doc, "Four decisions are worth explaining, because each one is a choice rather than "
          "the only way to write it.")
body(doc, "Empty input is rejected before the account is even fetched. That gives the user a "
          "sentence they can act on instead of a generic rejection, and it means a blank "
          "submission never reaches the comparison at all.")
body(doc, "The username is trimmed and lower-cased on both sides, so Zhihan, zhihan and "
          "zhihan with a trailing space all reach the same account. Usernames are labels "
          "people type differently; passwords are not, so the password is only trimmed of "
          "stray spaces and its case is preserved. Trimming a password is already generous, "
          "and a real system would probably not trim either field.")
body(doc, "The comparison uses MessageDigest.isEqual rather than String.equals. equals stops "
          "at the first character that differs, so the time it takes leaks how much of the "
          "value was correct. That is not a realistic attack on a first-year assignment, but "
          "the constant-time call is one line in the standard library and removes the "
          "question.")
body(doc, "Both halves must match before LoginResult.success is built, so there is no path "
          "that returns a success with a mismatched password. The failure message is "
          "identical for a wrong username and a wrong password.")

# ---------------------------------------------------------------- 7

heading(doc, "7. Task (c): the welcome message and the rejection")
body(doc, "A correct pair ends on the welcome page in Figure 6. The greeting comes from the "
          "session, not from the URL: after a successful login the controller stores the "
          "display name under the key \"loggedInAdmin\", and showWelcome reads it back. Only "
          "the display name is stored. The password is not put in the session, because "
          "session attributes sit in server memory for as long as the session lives.")
figure(doc, "03-welcome-page.png", "Figure 6: the welcome page after signing in as zhihan")

body(doc, "The redirect matters more than it looks. If the POST rendered the welcome page "
          "directly, the browser would reload that page with a form resubmission, and the "
          "credentials would be posted again on every refresh. Returning "
          "\"redirect:/welcome\" turns the response into a 302, so the last request the "
          "browser makes is a GET.")
body(doc, "Signing out calls session.invalidate(), which discards every attribute and makes "
          "the cookie that Tomcat issued point at a session that no longer exists. The "
          "visitor lands back on the login page with a short notice, shown in Figure 7, so "
          "the page does not look like it simply reloaded.")
figure(doc, "04-signed-out.png", "Figure 7: GET /login?loggedOut=1 after signing out")

# ---------------------------------------------------------------- 8

heading(doc, "8. Testing")
heading(doc, "8.1 Unit tests", level=2)
body(doc, "AuthServiceTests covers the rule without starting a web server. Ten tests, all "
          "passing, and Figure 2 shows them going through in the VS Code terminal:")
code_block(doc,
           "Tests run: 10, Failures: 0, Errors: 0, Skipped: 0, "
           "Time elapsed: 0.112 s -- in au.edu.mp.wikiadminlogin.AuthServiceTests", size=8)
body(doc, "The cases that matter are the ones that are easy to get wrong: upper case in the "
          "username, spaces around the username, a password one character too long, a null "
          "password, and a repository that returns nothing. The last one is why the service "
          "was written against an interface: the test supplies an empty store with a lambda "
          "and checks that the result is a plain failure instead of an exception.")

heading(doc, "8.2 Checks against the running application", level=2)
body(doc, "The unit tests cannot prove the pages and the mappings work, so I also drove the "
          "running application with a small script (doc/http-checks.ps1) that keeps its own "
          "cookie jar and turns off automatic redirects, so the 302s are visible instead of "
          "being followed silently. Output, shortened to the columns that matter:")
code_block(doc,
           "GET  /login                    -> 200   username input=True   password input=True\n"
           "GET  /                         -> 302   Location=http://127.0.0.1:8081/login\n"
           "POST /login zhihan / 123       -> 302   Location=.../welcome;jsessionid=38C6058F...\n"
           "GET  /welcome (same session)   -> 200   <h2>Welcome, Zhihan!</h2>\n"
           "POST /login zhihan / 999       -> 200   rejected=True\n"
           "POST /login admin / 123        -> 200   rejected=True\n"
           "POST /login ZHIHAN / 123       -> 302   upper case accepted=True\n"
           "POST /login empty / empty      -> 200   asks for input=True\n"
           "POST /login zhihan / empty     -> 200   asks for input=True\n"
           "GET  /welcome (no session)     -> 302   Location=.../login\n"
           "GET  /logout                   -> 302   Location=.../login?loggedOut=1\n"
           "GET  /welcome (after logout)   -> 302   session no longer valid=True\n"
           "GET  /topics                   -> 404   custom error page=True", size=7.5)

body(doc, "Two of those lines are worth pulling out. The third line returns 302 rather than "
          "200, which is the redirect-after-post behaviour described in section 7. The ninth "
          "line posts an empty username with an empty password directly, skipping the "
          "browser's required check, and still gets the \"enter both\" message, which shows "
          "the server-side check is doing real work rather than trusting the form.")

heading(doc, "8.3 One bug that the testing caught", level=2)
body(doc, "The first version of the error page was a single template used for both a "
          "rejected login and an HTTP error. It carried the condition "
          "${errorMessage and username}, and Thymeleaf tried to read the message string as a "
          "boolean. A wrong password produced HTTP 500 with the message "
          "\"Invalid boolean value 'The username or password is incorrect.'\" in the log, "
          "while the page looked fine in the source. The fix was to stop sharing the file: "
          "login-error.html is returned by the controller and only ever sees errorMessage and "
          "username, and error.html is Boot's error view and only ever sees status and error. "
          "The lesson I took from it is that a template is a contract about model attributes, "
          "and two different callers rarely offer the same ones.")

# ---------------------------------------------------------------- 9

heading(doc, "9. Limitations, and what Part B changes")
body(doc, "The password sits in the source as plain text, which is what the brief asks for "
          "at this stage. Part B needs a stored hash instead, and the comparison has to "
          "change with it. There is also no CSRF token on the form, no limit on how many "
          "times somebody can try, and the session id is not regenerated on login, so a "
          "production version would add all three. These are recorded here rather than "
          "hidden, because Part B builds on this code and the gaps are the next tasks.")
body(doc, "The account is loaded from a repository each time rather than cached in the "
          "service. That is slower and pointless while the repository is a constant, but it "
          "keeps the call shape that the JPA version will need.")

# ---------------------------------------------------------------- 10

heading(doc, "10. References")
refs = [
    "Spring Boot Reference Documentation, version 4.1.x. https://docs.spring.io/spring-boot/ "
    "(project structure, embedded Tomcat, error handling).",
    "Thymeleaf 3.1 documentation, standard expressions and attribute processors. "
    "https://www.thymeleaf.org/documentation.html",
    "Jakarta Servlet 6.1 specification, HttpSession and session invalidation. "
    "https://jakarta.ee/specifications/servlet/",
    "Java SE 21 API, java.security.MessageDigest and java.util.Optional. "
    "https://docs.oracle.com/en/java/javase/21/docs/api/",
    "BIT235 lecture and lab material, Week 7: Spring Boot and MVC, Melbourne Polytechnic, 2026.",
    "My own Week 7 wiki project, used for the page layout and the stylesheet palette "
    f"(same repository, JavaProjects/Week07-SpringBoot). {REPO}",
]
for ref in refs:
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(ref)
    run.font.size = Pt(9.5)

doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

# ---------------------------------------------------------------- appendix

heading(doc, "Appendix: full source code")
body(doc, "The files below are copied straight out of the project by the build script that "
          "produced this document, so what is printed here is what was compiled and run. "
          "Each file starts with my name and student ID. The two Thymeleaf templates that "
          "carry the shared layout, and the stylesheet, are in the zip.")

java_files = [
    ("WikiAdminLoginApplication.java", "src/main/java/au/edu/mp/wikiadminlogin/WikiAdminLoginApplication.java"),
    ("controller/LoginController.java", "src/main/java/au/edu/mp/wikiadminlogin/controller/LoginController.java"),
    ("service/AuthService.java", "src/main/java/au/edu/mp/wikiadminlogin/service/AuthService.java"),
    ("repository/AdminAccountRepository.java", "src/main/java/au/edu/mp/wikiadminlogin/repository/AdminAccountRepository.java"),
    ("repository/InMemoryAdminAccountRepository.java", "src/main/java/au/edu/mp/wikiadminlogin/repository/InMemoryAdminAccountRepository.java"),
    ("model/AdminAccount.java", "src/main/java/au/edu/mp/wikiadminlogin/model/AdminAccount.java"),
    ("model/LoginForm.java", "src/main/java/au/edu/mp/wikiadminlogin/model/LoginForm.java"),
    ("model/LoginResult.java", "src/main/java/au/edu/mp/wikiadminlogin/model/LoginResult.java"),
    ("AuthServiceTests.java", "src/test/java/au/edu/mp/wikiadminlogin/AuthServiceTests.java"),
]

for title, rel in java_files:
    heading(doc, title, level=2)
    code_block(doc, read_source(rel), size=7.2)

heading(doc, "templates/login.html", level=2)
code_block(doc, read_source("src/main/resources/templates/login.html"), size=7.2)

heading(doc, "templates/login-error.html", level=2)
code_block(doc, read_source("src/main/resources/templates/login-error.html"), size=7.2)

heading(doc, "templates/welcome.html", level=2)
code_block(doc, read_source("src/main/resources/templates/welcome.html"), size=7.2)

heading(doc, "templates/error.html", level=2)
code_block(doc, read_source("src/main/resources/templates/error.html"), size=7.2)

out = DOC_DIR / f"BIT235_Assessment2_PartA_{STUDENT_ID}.docx"
doc.save(out)
print(f"saved {out}  ({os.path.getsize(out) / 1024:.0f} KB)")
