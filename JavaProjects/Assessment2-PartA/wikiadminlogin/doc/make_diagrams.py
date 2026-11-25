"""
Draw the two diagrams used in the Assessment 2 Part A document.

The document must not describe its structure or its request flow as a list or a
text tree, so both pictures are rendered here as PNG files and inserted as
figures instead.

Run:  python doc/make_diagrams.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "screenshots"
SCALE = 2  # draw at 2x, then downsample so the text stays sharp

INK = (23, 21, 38)
MUTED = (91, 90, 114)
BRAND = (59, 42, 114)
GOLD = (140, 100, 24)
PAPER = (255, 255, 255)
BG = (252, 251, 255)
SHELL = (244, 241, 251)
LINE = (226, 221, 242)
OK = (47, 107, 52)
OK_FILL = (238, 247, 238)
BAD = (163, 35, 31)
BAD_FILL = (253, 236, 235)
WARN_FILL = (255, 246, 224)

F = "C:/Windows/Fonts/"
FONT_TITLE = ImageFont.truetype(F + "segoeuib.ttf", 48 * SCALE)
FONT_H = ImageFont.truetype(F + "segoeuib.ttf", 36 * SCALE)
FONT_H_S = ImageFont.truetype(F + "segoeuib.ttf", 32 * SCALE)
FONT_BODY = ImageFont.truetype(F + "segoeui.ttf", 29 * SCALE)
FONT_SMALL = ImageFont.truetype(F + "segoeui.ttf", 25 * SCALE)
FONT_CODE = ImageFont.truetype(F + "consola.ttf", 27 * SCALE)
FONT_CODE_S = ImageFont.truetype(F + "consola.ttf", 24 * SCALE)


def s(v):
    return int(v * SCALE)


def canvas(w, h, fill=BG):
    return Image.new("RGB", (s(w), s(h)), fill)


def box(d, x, y, w, h, fill, outline, width=3, radius=14):
    d.rounded_rectangle(
        [s(x), s(y), s(x + w), s(y + h)],
        radius=s(radius), fill=fill, outline=outline, width=s(width),
    )


def text(d, x, y, txt, font, fill=INK, anchor="la"):
    d.text((s(x), s(y)), txt, font=font, fill=fill, anchor=anchor)


def center_text(d, cx, y, txt, font, fill=INK):
    d.text((s(cx), s(y)), txt, font=font, fill=fill, anchor="ma")


def wrap(d, x, y, txt, font, max_w, fill=INK, line_gap=10):
    words = txt.split()
    line = ""
    cy = y
    for word in words:
        probe = (line + " " + word).strip()
        if d.textlength(probe, font=font) <= s(max_w):
            line = probe
        else:
            d.text((s(x), s(cy)), line, font=font, fill=fill, anchor="la")
            cy += (font.size // SCALE) + line_gap
            line = word
    if line:
        d.text((s(x), s(cy)), line, font=font, fill=fill, anchor="la")
        cy += (font.size // SCALE) + line_gap
    return cy


def arrow(d, points, color=BRAND, width=4, dash=False, head=15):
    pts = [(s(px), s(py)) for px, py in points]
    if dash:
        for a, b in zip(pts, pts[1:]):
            x1, y1 = a
            x2, y2 = b
            length = max(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 1)
            pos = 0.0
            while pos < length - s(12):
                t1 = pos / length
                t2 = min((pos + s(8)) / length, 1)
                d.line([(x1 + (x2 - x1) * t1, y1 + (y2 - y1) * t1),
                        (x1 + (x2 - x1) * t2, y1 + (y2 - y1) * t2)],
                       fill=color, width=s(width))
                pos += s(16)
    else:
        d.line(pts, fill=color, width=s(width), joint="curve")

    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    vx, vy = x2 - x1, y2 - y1
    length = max((vx * vx + vy * vy) ** 0.5, 1)
    ux, uy = vx / length, vy / length
    px, py = -uy, ux
    d.polygon(
        [(x2, y2),
         (x2 - ux * s(head) + px * s(head * 0.55), y2 - uy * s(head) + py * s(head * 0.55)),
         (x2 - ux * s(head) - px * s(head * 0.55), y2 - uy * s(head) - py * s(head * 0.55))],
        fill=color,
    )


# ------------------------------------------------------------------ figure 1

def layers():
    W, H = 1860, 960
    img = canvas(W, H)
    d = ImageDraw.Draw(img)

    text(d, 70, 50, "wikiadminlogin: how the packages depend on each other", FONT_TITLE, BRAND)
    text(d, 70, 106, "One arrow per dependency. Nothing points back up to the controller.",
         FONT_BODY, MUTED)

    top_y, box_h = 190, 310

    # controller
    box(d, 70, top_y, 540, box_h, PAPER, BRAND)
    text(d, 96, top_y + 22, "controller", FONT_H, BRAND)
    text(d, 96, top_y + 68, "LoginController.java", FONT_CODE, INK)
    wrap(d, 96, top_y + 150,
         "Maps /, /login, /welcome and /logout. Puts the LoginForm in the Model "
         "and returns a view name.", FONT_BODY, 480, MUTED)

    # service
    box(d, 660, top_y, 540, box_h, PAPER, BRAND)
    text(d, 686, top_y + 22, "service", FONT_H, BRAND)
    text(d, 686, top_y + 68, "AuthService.java", FONT_CODE, INK)
    wrap(d, 686, top_y + 150,
         "Rejects empty input, normalises the username, compares both halves and "
         "builds the LoginResult.", FONT_BODY, 480, MUTED)

    # repository
    box(d, 1250, top_y, 540, box_h, PAPER, BRAND)
    text(d, 1276, top_y + 22, "repository", FONT_H, BRAND)
    text(d, 1276, top_y + 66, "AdminAccountRepository", FONT_CODE, INK)
    text(d, 1276, top_y + 98, "InMemoryAdminAccount" + "Repository", FONT_CODE, INK)
    wrap(d, 1276, top_y + 150,
         "Hands out the one hard-coded account as an Optional, so Part B can swap "
         "the class for a JPA version.", FONT_BODY, 480, MUTED)

    arrow(d, [(612, top_y + 155), (656, top_y + 155)])
    arrow(d, [(1202, top_y + 155), (1246, top_y + 155)])
    text(d, 634, top_y + 118, "asks", FONT_SMALL, MUTED, anchor="ra")
    text(d, 1224, top_y + 118, "reads", FONT_SMALL, MUTED, anchor="ra")

    # model
    my = 620
    box(d, 380, my, 1090, 150, PAPER, GOLD)
    text(d, 406, my + 20, "model", FONT_H, GOLD)
    text(d, 406, my + 64, "AdminAccount   ·   LoginForm   ·   LoginResult", FONT_CODE, INK)
    text(d, 406, my + 102, "plain objects, no Spring annotations", FONT_SMALL, MUTED)

    # model -> service, and model -> controller, two parallel arrows so they never cross
    arrow(d, [(930, my), (930, 508)], color=GOLD, width=3, dash=True)
    text(d, 946, 556, "the service builds it", FONT_SMALL, MUTED)
    arrow(d, [(470, my), (470, 508)], color=GOLD, width=3, dash=True)
    text(d, 482, 556, "bound from the form", FONT_SMALL, MUTED)

    # views
    vy = 810
    box(d, 70, vy, 800, 110, SHELL, LINE, 2)
    text(d, 96, vy + 18, "views  ·  src/main/resources/templates", FONT_H_S, INK)
    text(d, 96, vy + 60, "login.html   login-error.html   welcome.html   error.html",
         FONT_CODE, MUTED)

    arrow(d, [(330, 500), (330, vy - 8)])
    text(d, 96, 742, "view name + Model", FONT_SMALL, MUTED)
    arrow(d, [(292, 742), (326, 742)], width=2, head=10)

    img.resize((s(W) // SCALE, s(H) // SCALE), Image.LANCZOS).save(OUT / "08-layers.png")
    print("saved 08-layers.png")


# ------------------------------------------------------------------ figure 2

def flow():
    W, H = 1860, 1250
    img = canvas(W, H)
    d = ImageDraw.Draw(img)

    text(d, 70, 46, "One request, from the click to the page that comes back",
         FONT_TITLE, BRAND)
    text(d, 70, 102, "Every box is a call the server makes, in the order it makes it.",
         FONT_BODY, MUTED)

    cx = 930
    bw, bh = 1010, 104

    def node(y, title, sub, fill=PAPER, outline=BRAND, title_font=FONT_H_S):
        box(d, cx - bw // 2, y, bw, bh, fill, outline)
        center_text(d, cx, y + 16, title, title_font, outline)
        center_text(d, cx, y + 60, sub, FONT_CODE_S, MUTED)

    node(150, "GET /login", "browser asks for the form")
    arrow(d, [(cx, 254), (cx, 292)])
    node(292, "DispatcherServlet  →  LoginController.showLoginForm()",
         "matched by @GetMapping(\"/login\")")
    arrow(d, [(cx, 396), (cx, 434)])
    node(434, "Model.addAttribute(\"loginForm\", new LoginForm())",
         "returns the view name \"login\"")
    arrow(d, [(cx, 538), (cx, 576)])
    node(576, "Thymeleaf renders login.html",
         "two inputs, method=\"post\", action=\"/login\"")
    arrow(d, [(cx, 680), (cx, 718)])
    node(718, "POST /login  →  submitLogin()  →  AuthService.authenticate()",
         "the repository supplies the stored account", fill=SHELL)

    arrow(d, [(cx, 822), (cx, 852)])

    # decision
    dy = 860
    half, tall = 210, 66
    d.polygon(
        [(s(cx), s(dy)), (s(cx + half), s(dy + tall)),
         (s(cx), s(dy + 2 * tall)), (s(cx - half), s(dy + tall))],
        fill=WARN_FILL, outline=GOLD, width=s(3),
    )
    center_text(d, cx, dy + tall - 18, "both match?", FONT_H_S, GOLD)

    # results
    ry = 1080
    box(d, 90, ry, 700, 120, OK_FILL, OK)
    text(d, 116, ry + 14, "session + 302 /welcome", FONT_H_S, OK)
    text(d, 116, ry + 56, "showWelcome()  →  welcome.html", FONT_CODE_S, OK)

    box(d, 1070, ry, 700, 120, BAD_FILL, BAD)
    text(d, 1096, ry + 14, "login-error.html", FONT_H_S, BAD)
    text(d, 1096, ry + 56, "one message for either wrong half", FONT_CODE_S, BAD)

    arrow(d, [(cx - half, dy + tall), (440, dy + tall), (440, ry - 6)], color=OK)
    arrow(d, [(cx + half, dy + tall), (1420, dy + tall), (1420, ry - 6)], color=BAD)
    text(d, 452, dy + tall - 34, "yes", FONT_SMALL, OK)
    text(d, 1408, dy + tall - 34, "no", FONT_SMALL, BAD, anchor="ra")

    img.resize((s(W) // SCALE, s(H) // SCALE), Image.LANCZOS).save(OUT / "09-request-flow.png")
    print("saved 09-request-flow.png")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    layers()
    flow()
