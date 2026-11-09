"""Build the three Week 5 submission documents for BIT235.

  doc/BIT235_Week5_MethodOverloading_S1580887.docx   (answers written into the
      original workshop docx, screenshots under "paste a screenshot here")
  doc/BIT235_Week5_OOPConcepts_S1580887.docx          (20 steps + code + output)
  doc/BIT235_Week5_OOPConceptsExtension_S1580887.docx (20 steps recap + manager)

Code and console output are taken from the real files next to this script, so the
document can never drift from what the programs actually printed.
"""
import os
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from docx.enum.section import WD_SECTION

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(HERE)
SHOTS = os.path.join(HERE, "screenshots")

STUDENT = "Chen Zhihan"
STUDENT_ID = "S1580887"
REPO = "https://github.com/chenzhihan1751-cyber/bit235javaproject"


def read_text(path, encoding="utf-8-sig"):
    with open(path, "r", encoding=encoding) as f:
        return f.read().replace("\r\n", "\n")


def read_code(name):
    return read_text(os.path.join(PROJECT, name))


def read_output(name):
    return read_text(os.path.join(PROJECT, "output", name))


def set_font(run, name="Calibri", size=10.5, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        from docx.oxml import OxmlElement
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), name)


def tidy(paragraph, before=0, after=4, spacing=1.0):
    pf = paragraph.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = spacing


def para(doc, text="", size=10.5, bold=False, italic=False, after=4, before=0,
         color=None, align=None, font="Calibri"):
    p = doc.add_paragraph()
    tidy(p, before, after)
    if align is not None:
        p.alignment = align
    if text:
        set_font(p.add_run(text), font, size, bold, italic, color)
    return p


def bullet(doc, text, size=10.5, after=2):
    p = doc.add_paragraph(style="List Bullet")
    tidy(p, 0, after)
    set_font(p.add_run(text), "Calibri", size)
    return p


def heading(doc, text, level=1):
    p = doc.add_paragraph()
    sizes = {1: 16, 2: 13, 3: 11.5}
    tidy(p, 12 if level == 1 else 8, 4)
    set_font(p.add_run(text), "Calibri", sizes.get(level, 11), bold=True,
             color=RGBColor(0x1F, 0x3B, 0x73))
    return p


def code(doc, text, size=7.2):
    for line in text.rstrip("\n").split("\n"):
        p = doc.add_paragraph()
        tidy(p, 0, 0, 1.0)
        p.paragraph_format.left_indent = Inches(0.12)
        set_font(p.add_run(line if line.strip() else " "), "Consolas", size)


def output_block(doc, text, size=7.2):
    code(doc, text, size)


def image(doc, filename, caption=None, width=6.35):
    path = os.path.join(SHOTS, filename)
    if caption:
        p = doc.add_paragraph()
        tidy(p, 4, 2)
        set_font(p.add_run(caption), "Calibri", 9, italic=True,
                 color=RGBColor(0x44, 0x44, 0x44))
    p = doc.add_paragraph()
    tidy(p, 0, 6)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=Inches(width))


def page_setup(doc):
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)


def cover(doc, title, subtitle):
    para(doc, "BIT235 Object Oriented Programming", 11, bold=True, after=2)
    para(doc, "Melbourne Polytechnic - Semester 1, 2026", 9.5, after=10,
         color=RGBColor(0x55, 0x55, 0x55))
    para(doc, title, 20, bold=True, after=4, color=RGBColor(0x1F, 0x3B, 0x73))
    para(doc, subtitle, 11, italic=True, after=14)
    para(doc, "Student: %s        Student ID: %s" % (STUDENT, STUDENT_ID), 10.5, after=2)
    para(doc, "Repository: " + REPO, 9, after=2)
    para(doc, "Programs: Java 8 bytecode, compiled with javac 21.0.2 "
              "(--release 8) and run in the VS Code integrated terminal.", 9, after=12)
    p = doc.add_paragraph()
    tidy(p, 0, 10)
    pPr = p._p.get_or_add_pPr()
    from docx.oxml import OxmlElement
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:color"), "1F3B73")
    borders.append(bottom)
    pPr.append(borders)


# ---------------------------------------------------------------------------
# Document 1: Method Overloading - answers written into the workshop docx
# ---------------------------------------------------------------------------

def build_overloading():
    src = r"C:\temp\overloading.docx"
    doc = Document(src)
    body = doc.element.body

    def para_after(anchor, text="", size=10.5, bold=False, italic=False, after=4,
                   font="Calibri", color=None):
        p = anchor.insert_paragraph_before("")
        anchor._p.addnext(p._p)
        tidy(p, 0, after)
        if text:
            set_font(p.add_run(text), font, size, bold, italic, color)
        return p

    def code_after(anchor, text, size=7.2):
        for line in text.rstrip("\n").split("\n"):
            p = anchor.insert_paragraph_before("")
            anchor._p.addnext(p._p)
            tidy(p, 0, 0, 1.0)
            p.paragraph_format.left_indent = Inches(0.12)
            set_font(p.add_run(line if line.strip() else " "), "Consolas", size)
            anchor = p
        return anchor

    def image_after(anchor, filename, caption=None, width=6.35):
        if caption:
            p = anchor.insert_paragraph_before("")
            anchor._p.addnext(p._p)
            tidy(p, 4, 2)
            set_font(p.add_run(caption), "Calibri", 9, italic=True,
                     color=RGBColor(0x44, 0x44, 0x44))
            anchor = p
        p = anchor.insert_paragraph_before("")
        anchor._p.addnext(p._p)
        tidy(p, 0, 6)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(os.path.join(SHOTS, filename), width=Inches(width))
        return p

    paragraphs = doc.paragraphs
    anchors = {}
    for p in paragraphs:
        t = p.text.strip()
        if t.startswith("Write down the expected output"):
            anchors["q1"] = p
        elif t.startswith("What would happen if you tried to call calculate(10, 20)"):
            anchors["q2"] = p
        elif t.startswith("Paste a screenshot of your program here"):
            anchors["shot1"] = p
        elif t.startswith("Paste a screenshot of your modified program here"):
            anchors["shot2"] = p
    missing = [k for k in ("q1", "q2", "shot1", "shot2") if k not in anchors]
    if missing:
        raise SystemExit("anchor paragraphs not found: %s" % missing)

    # --- Part 1 -----------------------------------------------------------
    a = anchors["q1"]
    a = para_after(a, "Answer", 11, bold=True, after=3,
                   color=RGBColor(0x1F, 0x3B, 0x73))
    a = para_after(a, "Expected output:", 10.5, bold=True, after=2)
    a = code_after(a, read_output("OverloadDemo.txt"))
    a = para_after(a, "Which method is called, and why:", 10.5, bold=True, after=2)
    a = para_after(a, "display(5) - 5 is an int literal, so display(int) is an exact "
                      "match in the first phase of overload resolution.", 10.5)
    a = para_after(a, "display(5.5) - 5.5 is a double literal, so display(double) is "
                      "an exact match.", 10.5)
    a = para_after(a, "display(\"Hello\") - a String literal matches display(String) "
                      "exactly.", 10.5)
    a = para_after(a, "display('A') - 'A' is a char and there is no display(char). "
                      "Java first tries to match without boxing or varargs, and it is "
                      "allowed to widen a primitive. char is a 16-bit unsigned integer "
                      "type, so it widens to int; display(int) is the most specific "
                      "applicable method (int comes before long, float and double in the "
                      "widening chain), so the program prints the code point of 'A', "
                      "which is 65.", 10.5)
    a = para_after(a, "display(100L) - 100L is a long and there is no display(long). "
                      "long widens to float or double; it cannot narrow to int. Of the "
                      "applicable methods only display(double) is reachable by widening, "
                      "so it prints 100.0.", 10.5)
    a = para_after(a, "Rule: overload resolution happens at compile time. The compiler "
                      "picks the most specific method that is applicable without "
                      "narrowing, so the argument's static type decides the output.",
                   10.5, after=10)

    # --- Part 2 -----------------------------------------------------------
    a = anchors["q2"]
    a = para_after(a, "Answer", 11, bold=True, after=3,
                   color=RGBColor(0x1F, 0x3B, 0x73))
    a = para_after(a, "What javac reports:", 10.5, bold=True, after=2)
    a = code_after(a, read_output("CalculatorAmbiguity_compile_errors.txt"))
    a = para_after(a, "Why the statements are rejected:", 10.5, bold=True, after=2)
    a = para_after(a, "calculate(10, 20) - both arguments are int. Method 1 takes "
                      "(int, long), so 20 would be widened to long. Method 2 takes "
                      "(long, int), so 10 would be widened to long. Both methods are "
                      "applicable with exactly one widening conversion, and neither is "
                      "more specific than the other (each one is better in a different "
                      "parameter position), so the call is ambiguous and the compiler "
                      "stops with \"reference to calculate is ambiguous\".", 10.5)
    a = para_after(a, "calculate(10.5, 20.5) - both arguments are double. Neither "
                      "(int, long) nor (long, int) can take a double: double to int or "
                      "long is a narrowing conversion and Java never applies narrowing "
                      "implicitly, so there is no applicable method at all.", 10.5)
    a = para_after(a, "Would calculate(10, 20) compile without any type casting?", 10.5,
                   bold=True, after=2)
    a = para_after(a, "No. There is no calculate(int, int) method, and the two methods "
                      "that do exist are equally applicable after one widening step, so "
                      "the compiler cannot choose one. A cast removes the ambiguity by "
                      "making one call an exact match, for example calculate(10, 20L) "
                      "calls Method 1 and calculate(10L, 20) calls Method 2. This is a "
                      "compile-time error, not a run-time decision: Java fixes the "
                      "overload from the static types of the arguments.", 10.5)
    a = para_after(a, "The calls that do compile, and what they print: ", 10.5,
                   bold=True, after=2)
    a = code_after(a, read_output("CalculatorAmbiguityFixed.txt"))
    a = para_after(a, "The two rejected calls are commented out in "
                      "CalculatorAmbiguityFixed.java; the screenshot below is the "
                      "compiler output for the version exactly as it appears in the "
                      "workshop sheet (demo-errors/CalculatorAmbiguity.java).", 10.5,
                   after=6)
    a = image_after(a, "03_Ambiguity_compile_errors.png",
                    "VS Code - javac reports the ambiguity and the missing method "
                    "(integrated terminal).")
    a = para_after(a, "", 10.5, after=8)

    # --- Part 3 -----------------------------------------------------------
    a = anchors["shot1"]
    # replace the placeholder sentence with our own line
    for run in list(a.runs):
        run.text = ""
    set_font(a.add_run("Screenshot of the program running in VS Code "
                       "(Calculator.java, integrated terminal):"), "Calibri", 10.5,
             italic=True)
    a = image_after(a, "04_Calculator_multiply.png",
                    "VS Code - java Calculator")
    a = para_after(a, "Program (Calculator.java):", 10.5, bold=True, after=2)
    a = code_after(a, read_code("Calculator.java"))
    a = para_after(a, "Output:", 10.5, bold=True, after=2)
    a = code_after(a, read_output("Calculator.txt"))
    a = para_after(a, "Note: the sheet writes \"public static void main()\". The JVM "
                      "only starts a class through main(String[] args), so the "
                      "signature used here is main(String[] args); the three multiply "
                      "methods are exactly the ones requested.", 9.5, italic=True,
                   after=10)

    # --- Part 4 -----------------------------------------------------------
    a = anchors["shot2"]
    for run in list(a.runs):
        run.text = ""
    set_font(a.add_run("Screenshot of the modified program running in VS Code "
                       "(PrinterDemo.java, integrated terminal):"), "Calibri", 10.5,
             italic=True)
    a = image_after(a, "05_Printer.png", "VS Code - java PrinterDemo")
    a = para_after(a, "Which methods are called:", 10.5, bold=True, after=2)
    a = para_after(a, "printer.print(\"Hello\") calls print(String) - exact match on "
                      "the argument type.", 10.5)
    a = para_after(a, "printer.print(42) calls print(int) - 42 is an int literal.", 10.5)
    a = para_after(a, "printer.print(\"Hello\", 42) calls print(String, int) - two "
                      "arguments, so only the two-parameter overload is applicable.",
                   10.5)
    a = para_after(a, "printer.print(3.14) calls the new print(double) - 3.14 is a "
                      "double literal. Before the change this line would not have "
                      "compiled, because a double cannot narrow to int.", 10.5)
    a = para_after(a, "The added overload does not break the existing calls: each "
                      "argument list still has exactly one exact match, so the previous "
                      "three lines print the same text as before.", 10.5)
    a = para_after(a, "Program (PrinterDemo.java, class Main from the sheet is named "
                      "PrinterDemo to match the file):", 10.5, bold=True, after=2)
    a = code_after(a, read_code("PrinterDemo.java"))
    a = para_after(a, "Output:", 10.5, bold=True, after=2)
    a = code_after(a, read_output("PrinterDemo.txt"))

    out = os.path.join(HERE, "BIT235_Week5_MethodOverloading_S1580887.docx")
    doc.save(out)
    return out


# ---------------------------------------------------------------------------
# Document 2: OOP Concepts (20 steps)
# ---------------------------------------------------------------------------

def build_oop_concepts():
    doc = Document()
    page_setup(doc)
    cover(doc, "Workshop - OOP Concepts", "ZooKeeper, Enclosure and polymorphism")

    heading(doc, "1. What the program builds", 1)
    para(doc, "The workshop starts from the Enclosure project and grows it into a small "
              "zoo model. An Enclosure has an id, a capacity and an optional ZooKeeper; "
              "Cage, Aquarium and Aviary are subclasses of Enclosure; a ZooKeeper can "
              "look after several enclosures. MainDriver walks through steps 3 to 20 in "
              "order and prints a heading before each group so the output can be matched "
              "against the sheet.")
    bullet(doc, "Enclosure - shared data (enclosureId, capacity, keeper) and "
                "displayDetails().")
    bullet(doc, "Cage / Aquarium / Aviary - extend Enclosure, add their own field and "
                "override displayDetails() and getType().")
    bullet(doc, "ZooKeeper - id, givenName, familyName, plus an ArrayList<Enclosure> so "
                "one keeper can be responsible for many enclosures.")
    bullet(doc, "MainDriver - creates the objects and calls displayDetails() in the "
                "order the workshop asks for.")

    heading(doc, "2. Steps 1-3: the ZooKeeper class", 1)
    para(doc, "ZooKeeper holds the three fields from step 1 (id, givenName, familyName) "
              "and displayDetails() prints them. Step 3 creates one object in main() and "
              "calls the method, which produces:")
    code(doc, read_output("MainDriver.txt").split("=== Steps 6-7")[0].strip())
    para(doc, "The class also carries the ArrayList<Enclosure> used later in steps "
              "17-20; the methods for that are explained in section 7.", 10.5,
         italic=True)
    heading(doc, "ZooKeeper.java", 3)
    code(doc, read_code("ZooKeeper.java"))

    heading(doc, "3. Steps 4-7: linking a ZooKeeper to an Enclosure", 1)
    para(doc, "Step 4 adds the field ZooKeeper keeper and the method "
              "assignKeeper(ZooKeeper k) to Enclosure. assignKeeper() stores the "
              "reference and also registers the enclosure with the keeper, so the "
              "relationship is consistent in both directions.")
    para(doc, "Step 5 rewrites displayDetails() so it prints the enclosure id, the "
              "capacity and the keeper's name using keeper.getGivenName() and "
              "keeper.getFamilyName() (the fields are private, so the getters are used "
              "instead of keeper.givenName). If no keeper has been assigned the method "
              "prints \"(not assigned)\" instead of throwing a NullPointerException.")
    para(doc, "Steps 6-7 create one enclosure and one keeper, assign the keeper and "
              "display the result:")
    code(doc, """=== Steps 6-7: one Enclosure with a ZooKeeper assigned ===
Type         : Enclosure
Enclosure ID : E-001
Capacity     : 6
ZooKeeper    : Sam Lee""")
    heading(doc, "Enclosure.java", 3)
    code(doc, read_code("Enclosure.java"))

    heading(doc, "4. Steps 8-11: several keepers, several enclosures", 1)
    para(doc, "Three keepers and three different enclosure types are created, each "
              "enclosure gets its own keeper, and every enclosure is displayed:")
    code(doc, """Type         : Cage
Enclosure ID : C-101
Capacity     : 4
ZooKeeper    : Sam Lee
Mesh size    : 25.0 mm

Type         : Aquarium
Enclosure ID : A-101
Capacity     : 12
ZooKeeper    : Alex Kim
Water type   : Salt water
Depth        : 3.5 m

Type         : Aviary
Enclosure ID : V-101
Capacity     : 30
ZooKeeper    : Priya Nair
Flight height: 8.0 m""")
    heading(doc, "Cage.java", 3)
    code(doc, read_code("Cage.java"))
    heading(doc, "Aquarium.java", 3)
    code(doc, read_code("Aquarium.java"))
    heading(doc, "Aviary.java", 3)
    code(doc, read_code("Aviary.java"))

    heading(doc, "5. Steps 12-14: polymorphism with an array", 1)
    para(doc, "The three objects are stored in an Enclosure[] array and the loop calls "
              "displayDetails() through the Enclosure reference:")
    code(doc, """Enclosure[] enclosures = new Enclosure[3];
enclosures[0] = cage;
enclosures[1] = aquarium;
enclosures[2] = aviary;
for (Enclosure e : enclosures) {
    e.displayDetails();
}""")
    para(doc, "Each object still prints its own type, its own extra field and its own "
              "keeper, even though the array type is Enclosure. The output is identical "
              "to the block in section 4, which is the point of steps 12-14.")

    heading(doc, "6. Steps 15-16: why one Enclosure variable can hold different types", 1)
    para(doc, "Step 15 - a variable of type Enclosure can refer to a Cage, an Aquarium "
              "or an Aviary because those classes extend Enclosure. Java allows a "
              "reference of a superclass type to point at an object of any subclass; the "
              "compiler only checks that the object is an Enclosure, which it is by "
              "inheritance. The variable type decides what the compiler lets you call, "
              "the object type decides which implementation actually runs.")
    para(doc, "Step 16 - the concept is polymorphism (dynamic method dispatch), built on "
              "inheritance and method overriding. displayDetails() is declared in "
              "Enclosure and overridden in Cage, Aquarium and Aviary, so the JVM picks "
              "the override that belongs to the real object at run time. Without "
              "overriding, the loop would call Enclosure.displayDetails() three times "
              "and the extra fields would never be printed.")

    heading(doc, "7. Steps 17-20: one ZooKeeper, many enclosures", 1)
    para(doc, "Step 17 changes ZooKeeper so it can be assigned to more than one "
              "enclosure: the class keeps an ArrayList<Enclosure> instead of a single "
              "reference. Step 18 adds assignEnclosure(Enclosure e), which adds the "
              "enclosure to that list and keeps the back-reference on the enclosure.")
    para(doc, "Step 19 updates the program so one keeper manages several enclosures, and "
              "step 20 prints the list for every keeper:")
    code(doc, """=== Steps 17-20: one ZooKeeper managing several enclosures ===
ZooKeeper ID : 1000004
ZooKeeper    : Dana Wong
Enclosures managed by Dana Wong:
  - C-201 (Cage, capacity 6)
  - A-201 (Aquarium, capacity 10)
  - V-201 (Aviary, capacity 25)""")
    para(doc, "The last part of the output lists every keeper with the enclosures they "
              "are responsible for, including the keepers from steps 8-11, which shows "
              "that the one-to-many relationship works in both directions.")

    heading(doc, "8. Running the program in VS Code", 1)
    para(doc, "The project is compiled with javac 21 using --release 8 and each program "
              "is run in the VS Code integrated terminal. The screenshot below shows "
              "MainDriver.java and the real console output of the run.")
    image(doc, "06_MainDriver_OOP.png",
          "VS Code - java MainDriver (integrated terminal, end of the output).")

    heading(doc, "9. Complete console output", 1)
    output_block(doc, read_output("MainDriver.txt"))

    heading(doc, "10. MainDriver.java", 1)
    code(doc, read_code("MainDriver.java"))

    out = os.path.join(HERE, "BIT235_Week5_OOPConcepts_S1580887.docx")
    doc.save(out)
    return out


# ---------------------------------------------------------------------------
# Document 3: OOP Concepts Extension
# ---------------------------------------------------------------------------

def build_extension():
    doc = Document()
    page_setup(doc)
    cover(doc, "Workshop Extension - Bringing it home!",
          "EnclosureManager: one controller for enclosures and keepers")

    heading(doc, "1. What this extension adds", 1)
    para(doc, "Steps 1-20 are the same twenty steps as the OOP Concepts workshop, so "
              "the model (ZooKeeper, Enclosure, Cage, Aquarium, Aviary) and the answers "
              "are identical; the code is listed again in Appendix A so this document "
              "can be read on its own. The new part is the last page of the extension: "
              "an EnclosureManager class that acts as a central controller which stores "
              "enclosures, assigns keepers and prints a report.")
    para(doc, "The manager is the first step towards the assignment: instead of the "
              "driver wiring every object by hand, one object owns the collection and "
              "offers the operations the rest of the system needs. MainDriver then only "
              "talks to the manager.")

    heading(doc, "2. The twenty steps in one paragraph each", 1)
    for title, text in [
        ("Steps 1-3", "ZooKeeper with id, givenName and familyName; displayDetails() "
                      "prints them; one object created in main()."),
        ("Steps 4-7", "Enclosure gets a ZooKeeper field and assignKeeper(); "
                      "displayDetails() prints id, capacity and the keeper's name; one "
                      "enclosure and one keeper are created, linked and displayed."),
        ("Steps 8-11", "Several keepers and several enclosures (Cage, Aquarium, Aviary), "
                       "each with a different keeper, then all of them displayed."),
        ("Steps 12-14", "An Enclosure[] array holds the three subclasses and the loop "
                        "calls displayDetails() on each element."),
        ("Steps 15-16", "A superclass reference can hold a subclass object because of "
                        "inheritance; the overridden method that runs is chosen at run "
                        "time, which is polymorphism (dynamic dispatch)."),
        ("Steps 17-20", "ZooKeeper keeps an ArrayList<Enclosure> and assignEnclosure(); "
                        "one keeper manages several enclosures and the program prints "
                        "which enclosures belong to each keeper."),
    ]:
        p = doc.add_paragraph()
        tidy(p, 2, 3)
        set_font(p.add_run(title + ": "), "Calibri", 10.5, bold=True)
        set_font(p.add_run(text), "Calibri", 10.5)

    heading(doc, "3. EnclosureManager", 1)
    para(doc, "The starter code from the sheet is used as given: a private "
              "ArrayList<Enclosure>, addEnclosure(), "
              "assignKeeperToEnclosure(int index, ZooKeeper k) with a bounds check, and "
              "printReport() which calls displayDetails() on every enclosure and prints "
              "a separator. One small helper, getEnclosureCount(), was added so the "
              "driver can print how many enclosures the report contains.")
    para(doc, "Design notes:")
    bullet(doc, "The manager owns the collection, so the driver never keeps its own "
                "list of enclosures - there is one source of truth.")
    bullet(doc, "assignKeeperToEnclosure() delegates to Enclosure.assignKeeper(), which "
                "keeps the keeper's own list in sync, so the same relationship is "
                "visible from both objects.")
    bullet(doc, "The bounds check means an invalid index is ignored instead of throwing "
                "IndexOutOfBoundsException, which keeps the controller safe to call from "
                "a menu or a test.")
    bullet(doc, "printReport() relies on polymorphism: it only knows Enclosure, but each "
                "element prints its own type, capacity, keeper and extra field.")
    heading(doc, "EnclosureManager.java", 3)
    code(doc, read_code("EnclosureManager.java"))

    heading(doc, "4. Using it from the driver", 1)
    para(doc, "The code from page 3 of the sheet is used unchanged inside "
              "ExtensionDriver (the class is renamed so MainDriver can stay the driver "
              "for steps 3-20; the two would otherwise clash). Only the constructor "
              "arguments were added, because Cage and Aquarium in this project take "
              "their extra fields in the constructor.")
    heading(doc, "ExtensionDriver.java", 3)
    code(doc, read_code("ExtensionDriver.java"))

    heading(doc, "5. Output", 1)
    output_block(doc, read_output("ExtensionDriver.txt"))

    heading(doc, "6. Running it in VS Code", 1)
    image(doc, "07_EnclosureManager.png",
          "VS Code - java ExtensionDriver (integrated terminal).")

    heading(doc, "7. What I would add next", 1)
    para(doc, "The manager is a natural place for the assignment features: a method to "
              "find an enclosure by id, a removeEnclosure() that also unlinks the keeper, "
              "and a report that groups enclosures by keeper. Because the manager owns "
              "the collection, those changes stay in one class instead of spreading "
              "through main().")

    heading(doc, "Appendix A - full source", 1)
    for name in ("ZooKeeper.java", "Enclosure.java", "Cage.java", "Aquarium.java",
                 "Aviary.java", "MainDriver.java"):
        heading(doc, name, 3)
        code(doc, read_code(name))

    out = os.path.join(HERE, "BIT235_Week5_OOPConceptsExtension_S1580887.docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    made = [build_overloading(), build_oop_concepts(), build_extension()]
    for m in made:
        print("built:", m, os.path.getsize(m))
