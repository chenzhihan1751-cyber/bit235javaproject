"""Fill the BIT235 Week 7 homework docx with the screenshots and the GitHub link.

The template is a plain list of headings with empty "Screenshot:" lines, so the
pictures are inserted straight after the matching line, each with a one line
caption. Order of the images follows the order of the headings in the document.
"""
import os
import sys
import io

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(BASE, "doc", "screenshots")
DEST = os.path.join(BASE, "doc", "BIT235_Workshop7_S1580887.docx")
REPO = ("https://github.com/chenzhihan1751-cyber/bit235javaproject"
        "/tree/main/JavaProjects/Week07-SpringBoot")

# (anchor text, [(image file, caption)])
JOBS = [
    ("Screenshot:", [
        ("01_extension_pack.png",
         'VS Code Extensions view filtered by "spring boot": Spring Boot Extension Pack '
         "(VMware) is installed, together with Spring Boot Tools and Spring Boot Dashboard."),
    ]),
    ("Screenshot:", [
        ("02_spring_initializr.png",
         '"Spring Initializr Java Support" (Microsoft) is installed - it is the extension '
         "used to create the project from a template."),
    ]),
    ("Screenshot:", [
        ("03_spring_boot_run.png",
         "Integrated terminal in VS Code: mvn spring-boot:run. Spring Boot 4.1.2 starts the "
         "embedded Tomcat on port 8080 and TestwikiappApplication is started."),
    ]),
    ("Screenshots:", [
        ("04_home_page.png",
         "Home page: http://127.0.0.1:8080/ (index.html, CSS embedded in the head)."),
        ("05_topics_page.png",
         "Topics page: http://127.0.0.1:8080/topics - the list is rendered by "
         "WikiController with a Thymeleaf template."),
        ("06_topic_page.png",
         "Topic page: http://127.0.0.1:8080/topics/mvc-in-spring-boot - one item from the "
         "same model, rendered by topic.html."),
    ]),
]


def usable_width(doc):
    section = doc.sections[0]
    return (section.page_width - section.left_margin - section.right_margin) / 914400.0


def add_after(doc, anchor_el, text, size=9, italic=True, bold=False, space_before=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(4)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if text:
        run = p.add_run(text)
        run.font.size = Pt(size)
        run.italic = italic
        run.bold = bold
        run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)
    anchor_el.addnext(p._p)
    return p._p


def add_picture_after(doc, anchor_el, path, width_in):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(10)
    p.add_run().add_picture(path, width=Inches(width_in))
    anchor_el.addnext(p._p)
    return p._p


def main():
    doc = docx.Document(r"C:\temp\ws7.docx")
    width = min(6.2, usable_width(doc) - 0.1)
    print("picture width: %.2f in" % width)

    # GitHub link
    for p in doc.paragraphs:
        if p.text.strip().startswith("GitHub Link:"):
            run = p.add_run(" " + REPO)
            run.font.size = Pt(10)
            break

    anchors = [p for p in doc.paragraphs if p.text.strip() in ("Screenshot:", "Screenshots:")]
    print("anchors found:", [a.text.strip() for a in anchors])
    if len(anchors) != len(JOBS):
        raise SystemExit("anchor count does not match the plan")

    for anchor, (_, items) in zip(anchors, JOBS):
        cur = anchor._p
        for fname, caption in items:
            cur = add_picture_after(doc, cur, os.path.join(IMG, fname), width)
            cur = add_after(doc, cur, caption)

    doc.save(DEST)
    check = docx.Document(DEST)
    print("saved:", DEST)
    print("images:", len(check.inline_shapes), "paragraphs:", len(check.paragraphs))


if __name__ == "__main__":
    main()
