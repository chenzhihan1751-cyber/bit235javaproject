"""
BIT235 Week 01 - generate screenshot-style images for each exercise:
  ex{N}_code.png   -> editor window with syntax highlighted source
  ex{N}_output.png -> terminal window with the real console session
"""
import os
from PIL import Image, ImageDraw, ImageFont
from pygments import lex
from pygments.lexers import JavaLexer
from pygments.token import Token

BASE = r"D:\JavaDev\JavaProjects\Week01"
OUT = os.path.join(BASE, "doc", "images")
os.makedirs(OUT, exist_ok=True)

FONT_DIR = r"C:\Windows\Fonts"
F_REG = os.path.join(FONT_DIR, "consola.ttf")
F_BOLD = os.path.join(FONT_DIR, "consolab.ttf")

FS = 20
LH = 30
PAD_X = 24
PAD_Y = 18
GUTTER = 58
BAR_H = 42
TITLE_H = 0

CODE_BG = (30, 30, 30)
BAR_BG = (50, 50, 50)
BAR_TX = (200, 200, 200)
GUTTER_TX = (110, 110, 110)
LINE_TX = (212, 212, 212)

TERM_BG = (12, 12, 12)
TERM_TX = (204, 204, 204)
TERM_OK = (106, 153, 85)

# pygments token -> colour (VS Code dark+ like)
COLORS = {
    Token.Keyword: (86, 156, 214),
    Token.Keyword.Type: (78, 201, 176),
    Token.Name.Class: (78, 201, 176),
    Token.Name.Function: (220, 220, 170),
    Token.Name.Namespace: (78, 201, 176),
    Token.Name.Builtin: (78, 201, 176),
    Token.Name.Builtin.Pseudo: (86, 156, 214),
    Token.Literal.String: (206, 145, 120),
    Token.Literal.String.Char: (206, 145, 120),
    Token.Literal.Number: (181, 206, 168),
    Token.Comment: (106, 153, 85),
    Token.Operator: (212, 212, 212),
    Token.Punctuation: (212, 212, 212),
}


def colour_for(tok):
    t = tok
    while t is not None:
        if t in COLORS:
            return COLORS[t]
        t = t.parent
    return LINE_TX


def layout_code(src):
    """-> list of lines; a line = list of (text, colour)"""
    lexer = JavaLexer()
    lines = [[]]
    for tok, value in lex(src, lexer):
        if tok in Token.Text.Whitespace and "\n" in value:
            parts = value.split("\n")
            for i, p in enumerate(parts):
                if i > 0:
                    lines.append([])
                if p:
                    lines[-1].append((p, colour_for(tok)))
            continue
        if tok in Token.Text and value == "\n":
            lines.append([])
            continue
        if not value:
            continue
        for i, p in enumerate(value.split("\n")):
            if i > 0:
                lines.append([])
            if p:
                lines[-1].append((p, colour_for(tok)))
    while lines and not lines[-1]:
        lines.pop()
    return lines


def draw_window(title, body_lines, is_code, path):
    f_reg = ImageFont.truetype(F_REG, FS)
    f_bold = ImageFont.truetype(F_BOLD, FS)
    f_bar = ImageFont.truetype(F_BOLD, FS - 2)

    tmp = Image.new("RGB", (10, 10))
    d = ImageDraw.Draw(tmp)

    gutter_w = GUTTER if is_code else 0
    text_w = 0
    for ln in body_lines:
        w = sum(d.textlength(t, font=f_reg) for t, _ in ln) if isinstance(ln, list) else d.textlength(ln[0], font=f_reg)
        text_w = max(text_w, w)
    width = int(max(880, PAD_X * 2 + gutter_w + text_w + 30))
    height = BAR_H + PAD_Y * 2 + LH * len(body_lines)

    img = Image.new("RGB", (width, height), CODE_BG if is_code else TERM_BG)
    dr = ImageDraw.Draw(img)

    # title bar
    dr.rectangle([0, 0, width, BAR_H], fill=BAR_BG)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        dr.ellipse([16 + i * 22, BAR_H // 2 - 7, 30 + i * 22, BAR_H // 2 + 7], fill=c)
    dr.text((92, BAR_H // 2 - (FS - 2) // 2 - 1), title, font=f_bar, fill=BAR_TX)

    y = BAR_H + PAD_Y
    if is_code:
        for idx, ln in enumerate(body_lines, start=1):
            dr.text((PAD_X + gutter_w - 14 - d.textlength(str(idx), font=f_reg), y),
                    str(idx), font=f_reg, fill=GUTTER_TX)
            x = PAD_X + gutter_w
            for txt, col in ln:
                dr.text((x, y), txt, font=f_reg, fill=col)
                x += d.textlength(txt, font=f_reg)
            y += LH
    else:
        for txt, col in body_lines:
            dr.text((PAD_X, y), txt, font=f_reg, fill=col)
            y += LH

    dr.rectangle([0, 0, width - 1, height - 1], outline=(70, 70, 70) if is_code else (60, 60, 60))
    img.save(path)
    return path


# ---------- console transcript ----------
INPUTS = {4: ["20"], 5: ["-7"], 6: ["17"], 7: ["85"], 9: ["admin", "java123"], 10: ["17", "true"]}
PROMPTS = {
    4: ["Enter your age: "],
    5: ["Enter a number: "],
    6: ["Enter an integer: "],
    7: ["Enter your mark (0-100): "],
    9: ["Enter username: ", "Enter password: "],
    10: ["Enter your age: ", "Do you have a driver licence (true/false): "],
}


def transcript(n):
    raw = open(os.path.join(BASE, "output", f"Exercise{n}.txt"), encoding="utf-8-sig").read().rstrip("\n")
    if n in INPUTS:
        for p, v in zip(PROMPTS[n], INPUTS[n]):
            raw = raw.replace(p, p + v + "\n", 1)
    lines = [(r"D:\JavaDev\JavaProjects\Week01>java Exercise%d" % n, (140, 200, 140))]
    lines.append(("", TERM_TX))
    for l in raw.split("\n"):
        lines.append((l, TERM_TX))
    lines.append(("", TERM_TX))
    lines.append((r"D:\JavaDev\JavaProjects\Week01>", (140, 200, 140)))
    return lines


for n in range(1, 11):
    src = open(os.path.join(BASE, f"Exercise{n}.java"), encoding="utf-8").read().rstrip("\n")
    draw_window(f"Exercise{n}.java", layout_code(src), True, os.path.join(OUT, f"ex{n}_code.png"))
    draw_window(f"Command Prompt - java Exercise{n}", transcript(n), False, os.path.join(OUT, f"ex{n}_output.png"))

print("images done")
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    print(f, os.path.getsize(p), Image.open(p).size)
