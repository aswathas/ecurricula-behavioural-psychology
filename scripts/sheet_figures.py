"""Full-page handwriting templates for the assignment answer sheet.

Six figures, each drawn to fill the printable width of an A4 page so there is
real room to write by hand. Two modes per figure:

  blank=True  - the empty skeleton with dotted writing guides (the sheet he prints)
  blank=False - the same skeleton with the model answer typed in (the answer copy)

`ans` carries the filled content; each figure knows what it expects.
Sizes are SVG user units: the sheet prints the SVG at 100% of a 178 mm column,
so one unit is about 0.266 mm - a 12 unit letter is about 9 pt.
"""
import math

INK = "#16283f"
ACCENT = "#2b6cb0"
PAPER = "#fbfcff"
RULE = "#c9d6e8"
FAINT = "#b9c4d2"
TXT = "#1b2735"
MUTED = "#5b6b82"
LABEL = "#0d1c30"


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _wrap(text, width):
    """Greedy wrap on words, max `width` characters per line."""
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def _text(x, y, lines, size=12.0, color=TXT, anchor="middle", weight="normal", lh=None):
    lh = lh or size * 1.35
    out = []
    for i, ln in enumerate(lines):
        out.append(f"<text x='{x}' y='{y + i * lh}' font-size='{size}' fill='{color}' "
                   f"text-anchor='{anchor}' font-weight='{weight}'>{_esc(ln)}</text>")
    return "".join(out)


def _guides(x0, x1, ys):
    """Dotted writing lines."""
    return "".join(f"<line x1='{x0}' y1='{y}' x2='{x1}' y2='{y}' stroke='#9db0c6' "
                   f"stroke-width='1.3' stroke-dasharray='2 3'/>" for y in ys)


def _lead(x0, y0, x1, y1):
    """Dotted leader from a drawn part to its label."""
    return (f"<line x1='{x0}' y1='{y0}' x2='{x1}' y2='{y1}' stroke='#b0bccb' "
            f"stroke-width='1.2' stroke-dasharray='3 4'/>")


def _svg(w, h, body):
    return (f"<div class='diagram'><svg viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg' "
            f"preserveAspectRatio='xMidYMid meet'>{body}</svg></div>")


def _wedge(cx, cy, r, a0, a1, fill, stroke=INK, sw=1.4):
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if (a1 - a0) > math.pi else 0
    return (f"<path d='M {cx} {cy} L {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z' "
            f"fill='{fill}' stroke='{stroke}' stroke-width='{sw}'/>")


# --------------------------------------------------------------------------- circle
def circle(blank=True, ans=None):
    """A1 Q2 - Self-Concept Circle: four sections, room to write in each."""
    ans = ans or {}
    w, h = 670, 800
    cx, cy, r = 335, 395, 320
    parts = [f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{PAPER}' stroke='{INK}' stroke-width='2'/>"]
    for a in (0, 90, 180, 270):
        rad = math.radians(a)
        parts.append(f"<line x1='{cx - r * math.cos(rad):.1f}' y1='{cy - r * math.sin(rad):.1f}' "
                     f"x2='{cx + r * math.cos(rad):.1f}' y2='{cy + r * math.sin(rad):.1f}' "
                     f"stroke='{INK}' stroke-width='1.4'/>")
    # label, line box, answer slot for each quadrant
    quads = [
        ("BODY", "middle", 335, 150, 90, 580, 195, 62),
        ("ROLE IN MY FAMILY", "middle", 335, 615, 90, 580, 455, 62),
        ("PERSONALITY", "start", 78, 285, 70, 300, 305, 34),
        ("ABILITIES", "end", 592, 285, 370, 600, 305, 34),
    ]
    for label, anchor, lx, ly, x0, x1, y0, wrap in quads:
        parts.append(_text(lx, ly, [label], size=15, weight="600", color=LABEL, anchor=anchor))
        if blank:
            parts.append(_guides(x0, x1, [y0 + i * 30 for i in range(4)]))
        else:
            txt = ans.get(label, "")
            parts.append(_text(x0 if anchor != "end" else x1, y0 + 12,
                               _wrap(txt, wrap), size=10.5, anchor=anchor, lh=15))
    return _svg(w, h, "".join(parts))


# --------------------------------------------------------------------------- wheel
def wheel(blank=True, ans=None):
    """A1 Q4 - Wheel of Emotions: five sectors, a box to write each emotion in."""
    ans = ans or {}
    names = ans.get("sectors", [])
    fills = ["#e8f0fa", "#fdf1dc", "#e6f4ea", "#fbe6e6", "#eee9f7"]
    w, h = 670, 740
    cx, cy, r = 335, 360, 310
    step = 2 * math.pi / 5
    parts = []
    for i, fl in enumerate(fills):
        a0 = -math.pi / 2 + i * step + 0.01
        a1 = -math.pi / 2 + (i + 1) * step - 0.01
        parts.append(_wedge(cx, cy, r, a0, a1, fl))
    for i in range(5):
        am = math.radians(-90 + 36 + i * 72)
        bx = cx + 200 * math.cos(am)
        by = cy + 200 * math.sin(am)
        parts.append(f"<rect x='{bx - 78:.1f}' y='{by - 26:.1f}' width='156' height='52' rx='7' "
                     f"fill='{PAPER}' stroke='#9db0c6' stroke-width='1.3' stroke-dasharray='3 4'/>")
        if not blank and i < len(names):
            parts.append(_text(bx, by + 4, _wrap(names[i], 19), size=12, weight="600", color=LABEL, lh=14))
    parts.append(f"<circle cx='{cx}' cy='{cy}' r='74' fill='{PAPER}' stroke='{INK}' stroke-width='1.6'/>")
    if blank:
        parts.append(_text(cx, cy - 4, ["the moment"], size=11, color="#93a0b0"))
        parts.append(_text(cx, cy + 12, ["you recall"], size=10, color="#93a0b0"))
    else:
        parts.append(_text(cx, cy - 4, ["the demo"], size=11, weight="600", color=ACCENT))
        parts.append(_text(cx, cy + 12, ["evening"], size=11, weight="600", color=ACCENT))
    return _svg(w, h, "".join(parts))


# ---------------------------------------------------------------------- feeling wheel
def feeling_wheel(blank=True, ans=None):
    """A1 Q5 - Feeling Wheel: the six primary emotions, the precise one in the middle."""
    ans = ans or {}
    names = ["joy", "trust", "fear", "surprise", "sadness", "anger"]
    fills = ["#e6f4ea", "#e8f0fa", "#fdf1dc", "#eee9f7", "#eef2f7", "#fbe6e6"]
    w, h = 670, 740
    cx, cy, r = 335, 360, 295
    step = 2 * math.pi / len(names)
    parts = []
    for i, (nm, fl) in enumerate(zip(names, fills)):
        a0 = -math.pi / 2 + i * step + 0.01
        a1 = -math.pi / 2 + (i + 1) * step - 0.01
        parts.append(_wedge(cx, cy, r, a0, a1, fl))
        am = math.radians(-90 + 30 + i * 60)
        parts.append(_text(cx + 190 * math.cos(am), cy + 190 * math.sin(am) + 4, [nm],
                           size=13, weight="600", color=LABEL))
    parts.append(f"<circle cx='{cx}' cy='{cy}' r='108' fill='{PAPER}' stroke='{ACCENT}' stroke-width='2'/>")
    if blank:
        parts.append(_guides(cx - 80, cx + 80, [cy - 6, cy + 22]))
        parts.append(_text(cx, cy - 26, ["the precise"], size=10.5, color="#93a0b0"))
        parts.append(_text(cx, cy - 10, ["emotion you felt"], size=10.5, color="#93a0b0"))
    else:
        parts.append(_text(cx, cy + 2, _wrap(ans.get("centre", ""), 16), size=15,
                           weight="600", color=ACCENT, lh=18))
    return _svg(w, h, "".join(parts))


# --------------------------------------------------------------------------- johari
def johari(blank=True, ans=None):
    """A1 Q9 - Johari Window: four windows, room to write one thing in each."""
    ans = ans or {}
    w, h = 670, 700
    cw, ch = w / 2, h / 2
    quads = [
        (0, 0, "OPEN", "I know it, others know it"),
        (cw, 0, "HIDDEN", "I know it, others do not"),
        (0, ch, "UNKNOWN", "none of us knows it yet"),
        (cw, ch, "BLIND SPOT", "others see it, I have not realised"),
    ]
    fills = ["#e8f0fa", "#fdf1dc", "#eef2f7", "#fbe6e6"]
    parts = []
    for i, (x, y, t, sub) in enumerate(quads):
        fl = fills[i]
        parts.append(f"<rect x='{x}' y='{y}' width='{cw}' height='{ch}' fill='{fl}' stroke='{INK}' stroke-width='1.6'/>")
        parts.append(_text(x + 16, y + 40, [t], size=17, weight="600", anchor="start", color=LABEL))
        parts.append(_text(x + 16, y + 62, [sub], size=11, anchor="start", color=MUTED))
        if blank:
            parts.append(_guides(x + 18, x + cw - 18, [y + 108 + k * 30 for k in range(5)]))
        else:
            parts.append(_text(x + 18, y + 100, _wrap(ans.get(t, ""), 56), size=10.5,
                               anchor="start", lh=16))
    parts.append(_text(cw / 2, h - 8, ["known to others"], size=11, color=MUTED))
    parts.append(_text(w - 8, h - 8, ["known to me"], size=11, color=MUTED, anchor="end"))
    return _svg(w, h, "".join(parts))


# ---------------------------------------------------------------------- esteem tree
def esteem_tree(blank=True, ans=None):
    """A1 Q10 - Self-Esteem Tree: roots, trunk, branches, leaves, fruits - with
    a labelled writing column beside each part."""
    ans = ans or {}
    w, h = 670, 800
    parts = []
    # the tree itself
    parts.append(f"<line x1='40' y1='560' x2='320' y2='560' stroke='#7a5230' stroke-width='3'/>")
    parts.append(f"<path d='M 166 560 L 194 560 L 188 400 L 172 400 Z' fill='#7a5230' stroke='#5f3f24'/>")
    for x0, y0, x1, y1 in ((179, 430, 100, 335), (184, 425, 258, 330), (176, 470, 96, 425), (185, 475, 262, 435)):
        parts.append(f"<line x1='{x0}' y1='{y0}' x2='{x1}' y2='{y1}' stroke='#7a5230' stroke-width='6' "
                     f"stroke-linecap='round'/>")
    for fx, fy, fr in ((98, 305, 42), (255, 300, 42), (92, 400, 40), (258, 410, 40),
                       (176, 265, 44), (140, 350, 36)):
        parts.append(f"<circle cx='{fx}' cy='{fy}' r='{fr}' fill='#e6f4ea' stroke='#3f7d52' stroke-width='1.6'/>")
    for fx, fy in ((120, 250), (222, 235), (178, 200)):
        parts.append(f"<circle cx='{fx}' cy='{fy}' r='15' fill='#fbe6e6' stroke='#b4453c' stroke-width='1.6'/>")
    for rx, ry in ((85, 640), (132, 690), (180, 715), (230, 688), (276, 636)):
        parts.append(f"<line x1='180' y1='560' x2='{rx}' y2='{ry}' stroke='#7a5230' stroke-width='5' "
                     f"stroke-linecap='round'/>")
    # labelled writing column on the right
    groups = [
        ("FRUITS", 165, (178, 200), 2),
        ("LEAVES", 285, (255, 300), 3),
        ("BRANCHES", 405, (258, 410), 3),
        ("TRUNK", 505, (188, 470), 2),
        ("ROOTS", 645, (180, 600), 3),
    ]
    for label, y, anchor_pt, nlines in groups:
        parts.append(_lead(anchor_pt[0] + 12, anchor_pt[1], 336, y - 6))
        parts.append(_text(340, y, [label], size=14, weight="600", anchor="start", color=LABEL))
        if blank:
            parts.append(_guides(340, 640, [y + 26 + k * 28 for k in range(nlines)]))
        else:
            parts.append(_text(340, y + 22, _wrap(ans.get(label, ""), 58), size=10.5,
                               anchor="start", lh=16))
    return _svg(w, h, "".join(parts))


# ---------------------------------------------------------------------------- swot
def swot(blank=True, ans=None):
    """A2 Q5 - Personal SWOT: four boxes with room for three points each."""
    ans = ans or {}
    w, h = 670, 760
    quads = [("STRENGTHS", "#e8f0fa"), ("WEAKNESSES", "#fbe6e6"),
             ("OPPORTUNITIES", "#e6f4ea"), ("THREATS", "#fdf1dc")]
    parts = []
    for i, (t, fl) in enumerate(quads):
        x = 0 if i % 2 == 0 else w / 2
        y = 0 if i < 2 else h / 2
        parts.append(f"<rect x='{x}' y='{y}' width='{w/2}' height='{h/2}' fill='{fl}' "
                     f"stroke='{INK}' stroke-width='1.6'/>")
        parts.append(_text(x + 16, y + 36, [t], size=16, weight="600", anchor="start", color=LABEL))
        if blank:
            parts.append(_guides(x + 18, x + w / 2 - 18, [y + 78 + k * 30 for k in range(5)]))
        else:
            items = ans.get(t, [])
            ly = y + 72
            for it in items:
                for j, ln in enumerate(_wrap(it, 52)):
                    parts.append(_text(x + 18, ly, [("- " if j == 0 else "  ") + ln], size=10.5,
                                       anchor="start", color=TXT))
                    ly += 16
                ly += 6
    return _svg(w, h, "".join(parts))


FIGURES = {
    "circle": circle,
    "wheel": wheel,
    "feeling-wheel": feeling_wheel,
    "johari": johari,
    "esteem-tree": esteem_tree,
    "swot": swot,
}


def render(name, blank=True, ans=None):
    """Marker name -> the big template html."""
    fn = FIGURES.get(name)
    return fn(blank, ans) if fn else ""
