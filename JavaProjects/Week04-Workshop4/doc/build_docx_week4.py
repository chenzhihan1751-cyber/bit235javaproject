"""Build the three Week 4 Word documents (methods / arrays workshop / objects workshop).

Every answer block is: caption + VS Code screenshot (real run) + program source +
real console output. Source and output are read from disk so the document can
never drift from what was actually compiled and executed.
"""
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

BASE = r"D:\VSCode代码\01-学校作业\BIT235-Java\JavaProjects\Week04-Workshop4"
SHOTS = os.path.join(BASE, "doc", "screenshots")
OUT = os.path.join(BASE, "output")
DOCDIR = os.path.join(BASE, "doc")

STUDENT = "Chen Zhihan (S1580887)"


def set_font(run, name, size, bold=False, italic=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), name)


def para(doc, text, size=10.5, bold=False, italic=False, space_after=4, space_before=0, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    if align:
        p.alignment = align
    run = p.add_run(text)
    set_font(run, "Calibri", size, bold=bold, italic=italic)
    return p


def heading(doc, text, level=1):
    h = doc.add_heading(level=level)
    h.paragraph_format.space_before = Pt(12 if level == 1 else 10)
    h.paragraph_format.space_after = Pt(6)
    run = h.add_run(text)
    set_font(run, "Calibri", 15 if level == 1 else 12.5, bold=True,
             color=RGBColor(0x1F, 0x3B, 0x73))
    return h


def code_block(doc, text, size=7.2):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(text.rstrip("\n"))
    set_font(run, "Consolas", size)
    return p


def label(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    set_font(run, "Calibri", 9.5, bold=True, color=RGBColor(0x33, 0x33, 0x33))
    return p


def shot(doc, image_name, caption):
    path = os.path.join(SHOTS, image_name)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Inches(6.35))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(6)
    run = cap.add_run(caption)
    set_font(run, "Calibri", 8.5, italic=True, color=RGBColor(0x55, 0x55, 0x55))


def read(path):
    with open(path, "r", encoding="utf-8-sig") as fh:
        return fh.read()


def cover(doc, title, subtitle, intro_lines):
    t = doc.add_paragraph()
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.paragraph_format.space_before = Pt(24)
    run = t.add_run(title)
    set_font(run, "Calibri", 20, bold=True, color=RGBColor(0x1F, 0x3B, 0x73))

    s = doc.add_paragraph()
    s.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = s.add_run(subtitle)
    set_font(run, "Calibri", 12.5, color=RGBColor(0x44, 0x44, 0x44))

    i = doc.add_paragraph()
    i.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = i.add_run(STUDENT)
    set_font(run, "Calibri", 11.5, bold=True)

    para(doc, "", size=6)
    for line in intro_lines:
        para(doc, line, size=10)


def answer(doc, image_name, code_files, output_file, caption):
    label(doc, "Answer:")
    shot(doc, image_name, caption)
    for name, path in code_files:
        label(doc, "Program: " + name)
        code_block(doc, read(path))
    label(doc, "Output:")
    code_block(doc, read(os.path.join(OUT, output_file)), size=7.5)


# --------------------------------------------------------------------------- #
# 1. Methods exercises
# --------------------------------------------------------------------------- #
def build_methods():
    doc = Document()
    cover(doc, "BIT235 Object Oriented Programming",
          "Week 4 - Methods Exercises",
          ["The four method types are covered in order: void with no parameters, void with "
           "parameters, returning with no parameters, and returning with parameters.",
           "Every program was compiled with javac (release 8) and run in the VS Code "
           "integrated terminal; the screenshots below are the real runs."])

    heading(doc, "Question 1 - Void method (no parameters)", 1)
    para(doc, "Write a method called displayWelcome(). It must not return a value and must not "
              "accept any parameters. It must print the message: Welcome to Java programming")
    answer(doc, "01_Methods_Q1_DisplayWelcome.png",
           [("DisplayWelcome.java", os.path.join(BASE, "DisplayWelcome.java"))],
           "Q1_DisplayWelcome.txt",
           "VS Code - java DisplayWelcome")

    heading(doc, "Question 2 - Void method (with parameter)", 1)
    para(doc, "Write a method called displayNumber(). It must not return a value and must accept "
              "one int parameter. It must print \"The number is: x\".")
    answer(doc, "02_Methods_Q2_DisplayNumber.png",
           [("DisplayNumber.java", os.path.join(BASE, "DisplayNumber.java"))],
           "Q2_DisplayNumber.txt",
           "VS Code - java DisplayNumber")

    heading(doc, "Question 3 - Returning method (no parameters)", 1)
    para(doc, "Write a method called diceRoll(). It must return an int, must not accept any "
              "parameters, and must return a random number between 1 and 6. Call it twice, add "
              "the two values, print the rolls, then print \"7 is a winner!!\" when the total is 7 "
              "and \"Try again.\" otherwise.")
    answer(doc, "03_Methods_Q3_DiceRoll.png",
           [("DiceRoll.java", os.path.join(BASE, "DiceRoll.java"))],
           "Q3_DiceRoll.txt",
           "VS Code - java DiceRoll (the roll is random, so the result changes on every run)")

    heading(doc, "Question 4 - Returning method (with multiple parameters)", 1)
    para(doc, "Write a method called randomNumber(). It must return an int, must accept two int "
              "parameters, and must return a random number between the first and the second "
              "parameter inclusive. The returned number must be displayed.")
    answer(doc, "04_Methods_Q4_RandomNumber.png",
           [("RandomNumber.java", os.path.join(BASE, "RandomNumber.java"))],
           "Q4_RandomNumber.txt",
           "VS Code - java RandomNumber")

    out = os.path.join(DOCDIR, "BIT235_Week4_Methods_S1580887.docx")
    doc.save(out)
    return out


# --------------------------------------------------------------------------- #
# 2. Arrays workshop (basic 8 questions + extended 3 exercises)
# --------------------------------------------------------------------------- #
def build_arrays():
    doc = Document()
    cover(doc, "BIT235 Object Oriented Programming",
          "Week 4 Workshop - Arrays",
          ["Part A answers questions 1 to 8 of the Arrays exercise sheet.",
           "Part B answers the three extended array exercises: passing an array to a method, "
           "bubble sort, and binary versus linear search.",
           "Every program was compiled with javac (release 8) and run in the VS Code integrated "
           "terminal; the screenshots below are the real runs."])

    heading(doc, "Part A - Arrays exercise", 1)

    heading(doc, "Q1. Creating an array (shorthand)", 2)
    para(doc, "Create an int array called numbers using the shorthand method, containing the "
              "values 3, 6, 9, 12, 15.")
    answer(doc, "05_Arrays_Q1_Shorthand.png",
           [("ShorthandArray.java", os.path.join(BASE, "ShorthandArray.java"))],
           "A1_ShorthandArray.txt", "VS Code - java ShorthandArray")

    heading(doc, "Q2. Creating an array (standard method)", 2)
    para(doc, "Create an int array called values with new int[], five elements, and assign the "
              "values 12, 4, 1, 8, 7.")
    answer(doc, "06_Arrays_Q2_Standard.png",
           [("StandardArray.java", os.path.join(BASE, "StandardArray.java"))],
           "A2_StandardArray.txt", "VS Code - java StandardArray")

    heading(doc, "Q3. Traversing an array using .length", 2)
    para(doc, "Using the numbers array from Q1, write a for loop that prints each value, using "
              "numbers.length in the loop.")
    answer(doc, "07_Arrays_Q3_ForLoop.png",
           [("ForLoopTraversal.java", os.path.join(BASE, "ForLoopTraversal.java"))],
           "A3_ForLoopTraversal.txt", "VS Code - java ForLoopTraversal")

    heading(doc, "Q4. Traversing an array using foreach", 2)
    para(doc, "Using the values array from Q2, write a foreach loop that prints each value.")
    answer(doc, "08_Arrays_Q4_ForEach.png",
           [("ForEachTraversal.java", os.path.join(BASE, "ForEachTraversal.java"))],
           "A4_ForEachTraversal.txt", "VS Code - java ForEachTraversal")

    heading(doc, "Q5. Searching for a value (if statement)", 2)
    para(doc, "Using the numbers array, write code with a loop and an if statement that checks "
              "whether the value 9 exists, printing \"Value found\" or \"Value not found\".")
    answer(doc, "09_Arrays_Q5_Search.png",
           [("SearchValue.java", os.path.join(BASE, "SearchValue.java"))],
           "A5_SearchValue.txt", "VS Code - java SearchValue")

    heading(doc, "Q6. Traversing an array in reverse", 2)
    para(doc, "Using the values array from Q2, print the values in reverse order.")
    para(doc, "Note: the sample output on the exercise sheet (15 12 9 6 3) is the numbers array "
              "reversed, while the instruction names the values array. The program follows the "
              "instruction, so the values array is printed backwards: 7 8 1 4 12.", size=9.5,
         italic=True)
    answer(doc, "10_Arrays_Q6_Reverse.png",
           [("ReverseTraversal.java", os.path.join(BASE, "ReverseTraversal.java"))],
           "A6_ReverseTraversal.txt", "VS Code - java ReverseTraversal")

    heading(doc, "Q7. Filling an array at runtime", 2)
    para(doc, "Create an array called people of size 5. Fill it from user input with Scanner and "
              "break out when the user enters nothing. Then display the elements as a comma "
              "separated list.")
    para(doc, "Note: a foreach loop cannot fill an array, because it copies each element into a "
              "local variable and writing to that variable never reaches the array. The program "
              "reads the input with an indexed for loop and prints the result with the same "
              "comma separated pattern.", size=9.5, italic=True)
    answer(doc, "11_Arrays_Q7_FillRuntime.png",
           [("FillArrayAtRuntime.java", os.path.join(BASE, "FillArrayAtRuntime.java"))],
           "A7_FillArrayAtRuntime.txt",
           "VS Code - Get-Content input\\people.txt | java FillArrayAtRuntime (the five names "
           "are piped in as the typed input)")

    heading(doc, "Q8. Accessing index", 2)
    para(doc, "Using the people array, print each value on a single line separated by a comma, "
              "with no comma after the last value, for example: "
              "Wilma, Fred, Barney, Betty, Pebbles")
    answer(doc, "12_Arrays_Q8_CommaList.png",
           [("IndexAccessCommaList.java", os.path.join(BASE, "IndexAccessCommaList.java"))],
           "A8_IndexAccessCommaList.txt", "VS Code - java IndexAccessCommaList")

    heading(doc, "Part B - Arrays extended exercises", 1)

    heading(doc, "Exercise 1 - Passing arrays to methods", 2)
    para(doc, "Create an int array with the values 4, 7, 2, 9, 5. Write a static method called "
              "calculateTotal() that accepts an int array, returns an int and calculates the sum "
              "of all values. Call it from main, store the result in a variable called total and "
              "print it, for example: Total: 27")
    answer(doc, "13_Ext_E1_CalculateTotal.png",
           [("CalculateTotal.java", os.path.join(BASE, "CalculateTotal.java"))],
           "E1_CalculateTotal.txt", "VS Code - java CalculateTotal")

    heading(doc, "Exercise 2 - Sorting (bubble sort)", 2)
    para(doc, "Write a program that bubble sorts an array of 20 unique values between 1 and 1000. "
              "Two neighbouring elements are compared and swapped when they are out of order, and "
              "the whole process repeats until a full pass makes no swap.")
    answer(doc, "14_Ext_E2_BubbleSort.png",
           [("BubbleSort.java", os.path.join(BASE, "BubbleSort.java"))],
           "E2_BubbleSort.txt", "VS Code - java BubbleSort")

    heading(doc, "Exercise 3 - Binary search (Task A and Task B)", 2)
    para(doc, "Task A: extend the bubble sort program with a binary search, so the sorted array is "
              "searched by checking the middle element and then the left or right half. "
              "Task B: count the comparisons needed by the binary search and by a linear search "
              "over the unsorted list, then print a comparison of the two.")
    para(doc, "Result: for a target near the end of the list the binary search needed 3 "
              "comparisons where the linear search needed 19, and for a target that is not in the "
              "list it needed 4 against 20.", size=9.5, italic=True)
    answer(doc, "15_Ext_E3_BinaryLinear.png",
           [("BinaryVsLinearSearch.java", os.path.join(BASE, "BinaryVsLinearSearch.java"))],
           "E3_BinaryVsLinearSearch.txt", "VS Code - java BinaryVsLinearSearch")

    out = os.path.join(DOCDIR, "BIT235_Week4_ArraysWorkshop_S1580887.docx")
    doc.save(out)
    return out


# --------------------------------------------------------------------------- #
# 3. Objects workshop
# --------------------------------------------------------------------------- #
MAINAPP_LINES = os.path.join(BASE, "MainApp.java")
GREETING = os.path.join(BASE, "Greeting.java")
STUDENT_CLASS = os.path.join(BASE, "Student.java")


def build_objects():
    doc = Document()
    cover(doc, "BIT235 Object Oriented Programming",
          "Week 4 Workshop - Classes and Objects",
          ["The seven exercises move from the static world to the object world: a main class, a "
           "second class, an object, a field, several objects, and finally a second class of your "
           "own.",
           "Every program was compiled with javac (release 8) and run in the VS Code integrated "
           "terminal; the screenshots below are the real runs."])

    heading(doc, "Exercise 1 - Setting things up", 1)
    para(doc, "Create a folder, open it in VS Code, then create MainApp.java with a class called "
              "MainApp, a main() method, and a print of the message: Hello from my first class. "
              "The file name must match the class name.")
    label(doc, "Answer:")
    shot(doc, "16_Obj_MainApp.png", "VS Code - java MainApp (the first line is exercise 1; the "
                                    "lines below it are exercises 3, 5 and 6 in the same run)")
    label(doc, "Program: MainApp.java (exercise 1 part)")
    code_block(doc, "public class MainApp {\n"
                    "    public static void main(String[] args) {\n"
                    "        System.out.println(\"Hello from my first class\");\n"
                    "    }\n"
                    "}")
    label(doc, "Output:")
    code_block(doc, "Hello from my first class")

    heading(doc, "Exercise 2 - Creating a second class", 1)
    para(doc, "Create Greeting.java with a class called Greeting and a method called sayHello() "
              "that prints Hi there!. The method must not be static, because it belongs to the "
              "object.")
    label(doc, "Answer:")
    label(doc, "Program: Greeting.java (exercise 2 part)")
    code_block(doc, "public class Greeting {\n"
                    "\n"
                    "    public void sayHello() {\n"
                    "        System.out.println(\"Hi there!\");\n"
                    "    }\n"
                    "}")

    heading(doc, "Exercise 3 - Creating an object", 1)
    para(doc, "In MainApp.java, create an object of the Greeting class and call the sayHello "
              "method. Expected output: Hi there!")
    label(doc, "Answer:")
    label(doc, "Program: MainApp.java (exercise 3 part)")
    code_block(doc, "Greeting firstGreeting = new Greeting();   // instantiate the object\n"
                    "firstGreeting.sayHello();                 // call its method")
    label(doc, "Output:")
    code_block(doc, "Hi there!")

    heading(doc, "Exercise 4 - Adding data (fields)", 1)
    para(doc, "In Greeting.java add the field String name; and modify sayHello so that it prints "
              "that name, for example: Hello <name>")
    label(doc, "Answer:")
    label(doc, "Program: Greeting.java (exercise 4 part)")
    code_block(doc, "public class Greeting {\n"
                    "\n"
                    "    String name;   // field: every object keeps its own copy\n"
                    "\n"
                    "    public void sayHello() {\n"
                    "        if (name == null || name.isEmpty()) {\n"
                    "            System.out.println(\"Hi there!\");\n"
                    "        } else {\n"
                    "            System.out.println(\"Hello \" + name);\n"
                    "        }\n"
                    "    }\n"
                    "}")

    heading(doc, "Exercise 5 - Using the object properly", 1)
    para(doc, "In MainApp.java create a Greeting object, set the name to your own name and call "
              "the method. Example output: Hello Sally")
    label(doc, "Answer:")
    label(doc, "Program: MainApp.java (exercise 5 part)")
    code_block(doc, "Greeting myGreeting = new Greeting();\n"
                    "myGreeting.name = \"Zhihan\";\n"
                    "myGreeting.sayHello();")
    label(doc, "Output:")
    code_block(doc, "Hello Zhihan")

    heading(doc, "Exercise 6 - Multiple objects (key concept)", 1)
    para(doc, "In MainApp.java create two Greeting objects, one with your name and one with a "
              "friend's name, and call the method on both. Each object must print its own name.")
    label(doc, "Answer:")
    label(doc, "Program: MainApp.java (exercise 6 part)")
    code_block(doc, "Greeting friendGreeting = new Greeting();\n"
                    "friendGreeting.name = \"Alex\";\n"
                    "myGreeting.sayHello();\n"
                    "friendGreeting.sayHello();")
    label(doc, "Output:")
    code_block(doc, "Hello Zhihan\nHello Alex")

    heading(doc, "Exercise 7 - Thinking in objects", 1)
    para(doc, "Create Student.java with a field studentId and a method displayId(). In MainApp.java "
              "create two Student objects with different IDs and call displayId() on each.")
    label(doc, "Answer:")
    shot(doc, "17_Obj_StudentsApp.png", "VS Code - java StudentsApp")
    label(doc, "Program: Student.java")
    code_block(doc, read(STUDENT_CLASS))
    label(doc, "Program: StudentsApp.java")
    code_block(doc, read(os.path.join(BASE, "StudentsApp.java")))
    label(doc, "Output:")
    code_block(doc, read(os.path.join(OUT, "O2_StudentsApp.txt")), size=7.5)

    heading(doc, "Final version of the two classes", 1)
    para(doc, "The complete files as they are in the project folder. MainApp runs exercises 1, 3, "
              "5 and 6 in one program, and the screenshot at exercise 1 shows that full run.")
    label(doc, "Program: Greeting.java (final)")
    code_block(doc, read(GREETING))
    label(doc, "Program: MainApp.java (final)")
    code_block(doc, read(MAINAPP_LINES))
    label(doc, "Output of java MainApp:")
    code_block(doc, read(os.path.join(OUT, "O1_MainApp.txt")), size=7.5)

    out = os.path.join(DOCDIR, "BIT235_Week4_ObjectsWorkshop_S1580887.docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    for path in (build_methods(), build_arrays(), build_objects()):
        import docx
        d = docx.Document(path)
        print("%-70s images=%d paragraphs=%d" % (os.path.basename(path), len(d.inline_shapes), len(d.paragraphs)))
