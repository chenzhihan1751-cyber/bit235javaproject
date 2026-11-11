"""Build BIT235_Workshop6_S1580887.docx from the workshop template.

For every "Your answer (screenshot)" cell a full-width answer row is added
right under the exercise row: screenshot first, then the program source and
the real console output, in the order requested on 2026-10-28.
"""
import os
import sys
import io
from copy import deepcopy

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.table import _Cell

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(BASE, "doc", "screenshots")
OUT = os.path.join(BASE, "output")
SRC = BASE
DEST = os.path.join(BASE, "doc", "BIT235_Workshop6_S1580887.docx")
REPO = "https://github.com/chenzhihan1751-cyber/bit235javaproject"

EXERCISES = [
    dict(n=1, img="01_SongList.png", code=["SongList.java"], out="SongList.txt"),
    dict(n=2, img="02_SongListSorted.png", code=["SongListSorted.java"],
         out="SongListSorted.txt"),
    dict(n=3, img="03_ReverseWordSentence.png", code=["ReverseWordSentence.java"],
         out="ReverseWordSentence.txt"),
    dict(n=4, img="04_DecodeMessage.png", code=["DecodeMessage.java"],
         out="DecodeMessage.txt"),
    dict(n=5, img="05_ParagraphSearch.png", code=["ParagraphSearch.java"],
         out="ParagraphSearch.txt"),
    dict(n=6, img="06_IdentifyPartsDemo.png",
         code=["IdentifyMyParts.java", "IdentifyPartsDemo.java"],
         out="IdentifyPartsDemo.txt"),
    dict(n=7, img="07_BoxesDriver.png", code=["Boxes.java", "BoxesDriver.java"],
         out="BoxesDriver.txt"),
]

NOTES = {
    6: [
        "Answer (written part):",
        "Class variables : x   - it is declared static, so there is exactly one "
        "copy for the whole class and every object shares it "
        "(also reachable as IdentifyMyParts.x).",
        "Instance variables : y   - it has no static modifier, so every object "
        "created with new gets its own copy of y.",
        "Output: a.y = 5 and b.y = 6 because y belongs to the object. a.x = 1 and "
        "b.x = 2 both write the same static field x, so the second write wins and "
        "a.x, b.x and IdentifyMyParts.x all print 2.",
    ],
    7: [
        "Notes: Boxes.java is the class (constructor, setSize, toString, draw), "
        "BoxesDriver.java is the driver class with main(). Boxes refuses a size "
        "outside 1..10 and keeps the previous size, so a box can never be drawn "
        "larger than 10 x 10.",
    ],
}


def set_font(run, name="Consolas", size=7, bold=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), name)


def add_par(container, text="", font="Consolas", size=7, bold=False,
            space_before=0, space_after=0):
    p = container.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.0
    if text:
        set_font(p.add_run(text), font, size, bold)
    return p


def read_text(path):
    with open(path, "r", encoding="utf-8-sig") as fh:
        return fh.read().replace("\r\n", "\n").rstrip("\n")


def compact_cell(cell):
    """Drop the empty filler paragraphs of the template answer cell."""
    keep_first_empty = all(not p.text.strip() for p in cell.paragraphs)
    for p in list(cell.paragraphs):
        if p.text.strip():
            continue
        # never drop a paragraph that carries an image (the Exercise 7 example)
        if p._p.findall(".//" + qn("w:drawing")) or p._p.findall(".//" + qn("w:pict")):
            continue
        if keep_first_empty:
            keep_first_empty = False
            continue
        p._p.getparent().remove(p._p)


def strip_height(tr):
    """Remove the fixed w:trHeight so the row grows with its content."""
    trpr = tr.trPr
    if trpr is None:
        return
    for el in list(trpr):
        if el.tag == qn("w:trHeight"):
            trpr.remove(el)


def clear_cell(cell):
    """Leave one empty paragraph in the (merged) cell.

    The copied row may carry a nested table from the question cell (the key
    table of Exercise 4), so nested tables are removed as well.
    """
    for tbl in cell._tc.findall(qn("w:tbl")):
        cell._tc.remove(tbl)
    for p in list(cell.paragraphs)[1:]:
        p._p.getparent().remove(p._p)
    first = cell.paragraphs[0]
    for r in list(first.runs):
        r._r.getparent().remove(r._r)


def build_answer(cell, ex):
    clear_cell(cell)

    cap = add_par(cell, "Exercise %d - VS Code run (screenshot)" % ex["n"],
                  font="Calibri", size=9, bold=True, space_before=4)
    cap.alignment = WD_ALIGN_PARAGRAPH.LEFT

    pic_par = cell.add_paragraph()
    pic_par.paragraph_format.space_after = Pt(2)
    pic_par.add_run().add_picture(os.path.join(IMG, ex["img"]), width=Inches(5.9))

    for name in ex["code"]:
        add_par(cell, "Program: " + name, font="Consolas", size=9, bold=True,
                space_before=6)
        for line in read_text(os.path.join(SRC, name)).split("\n"):
            add_par(cell, line if line.strip() else " ", size=7)

    add_par(cell, "Output:", font="Consolas", size=9, bold=True, space_before=6)
    for line in read_text(os.path.join(OUT, ex["out"])).split("\n"):
        add_par(cell, line if line.strip() else " ", size=7)

    for note in NOTES.get(ex["n"], []):
        bold = note.startswith("Answer (written part)") or note.startswith("Notes:")
        add_par(cell, note, font="Calibri", size=9.5, bold=bold, space_before=6)


def main():
    doc = docx.Document(r"C:\temp\ws6.docx")

    # 1. GitHub link on the cover line
    for p in doc.paragraphs:
        if p.text.strip().startswith("GitHub Link:"):
            p.add_run(" " + REPO)
            break

    # 2. one answer row per exercise, processed bottom-up per table so the
    #    row indexes and the "Your answer" mapping stay valid
    for table in doc.tables:
        targets = []
        for ri, row in enumerate(table.rows):
            label = row.cells[0].text
            if "Your answer" in label:
                num = None
                for ex in EXERCISES:
                    if ("Exercise %d" % ex["n"]) in label:
                        num = ex["n"]
                if num is None:
                    raise SystemExit("cannot map exercise for row %d: %r" % (ri, label))
                targets.append((ri, num))

        for ri, num in sorted(targets, reverse=True):
            row = table.rows[ri]
            new_tr = deepcopy(row._tr)
            # the template reserves a fixed height for the screenshot cell; the
            # answer now lives in its own full width row, so both rows may grow
            # with their content instead of keeping that reserved blank space
            for cell in row.cells:
                compact_cell(cell)
            strip_height(row._tr)
            strip_height(new_tr)
            row._tr.addnext(new_tr)
            c0 = _Cell(new_tr.tc_lst[0], table)
            c1 = _Cell(new_tr.tc_lst[1], table)
            merged = c0.merge(c1)
            ex = next(e for e in EXERCISES if e["n"] == num)
            build_answer(merged, ex)
            print("filled exercise", num, "in table row", ri)

    doc.save(DEST)
    print("saved:", DEST)
    check = docx.Document(DEST)
    print("tables:", len(check.tables), "images:", len(check.inline_shapes))


if __name__ == "__main__":
    main()




