"""SVG diagrams for the reflective assignments.

Every figure is drawn here so both renderers (typed PDF, handwriting PDF) can place it
from a marker in the answer body. Markers look like [diagram: name].

blank=True gives the empty template version - the structure a student draws on by hand,
with the answer content removed. Used by the handwriting sheet.
"""
import math

INK = "#16283f"
ACCENT = "#2b6cb0"
PAPER = "#fbfcff"
RULE = "#c9d6e8"
FAINT = "#b9c4d2"


def _wrap(text, width):
    """Greedy wrap on words, max `width` characters per line."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def _text(x, y, lines, size=11.0, color=INK, anchor="middle", weight="normal", lh=13):
    out = []
    for i, ln in enumerate(lines):
        out.append(f"<text x='{x}' y='{y + i * lh}' font-size='{size}' fill='{color}' "
                   f"text-anchor='{anchor}' font-weight='{weight}'>{ln}</text>")
    return "".join(out)


def _svg(w, h, body):
    return (f"<div class='diagram'><svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' "
            f"xmlns='http://www.w3.org/2000/svg'>{body}</svg></div>")


def _wedge(cx, cy, r, a0, a1, fill, stroke=INK, sw=1.4):
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if (a1 - a0) > math.pi else 0
    return (f"<path d='M {cx} {cy} L {x0:.1f} {y0:.1f} A {r} {r} 0 {large} 1 {x1:.1f} {y1:.1f} Z' "
            f"fill='{fill}' stroke='{stroke}' stroke-width='{sw}'/>")


def _guide(x0, y0, x1, y1):
    """A faint dotted line for handwriting."""
    return (f"<line x1='{x0}' y1='{y0}' x2='{x1}' y2='{y1}' stroke='{FAINT}' "
            f"stroke-width='1' stroke-dasharray='2 3'/>")


def circle(blank=False):
    """A1 Q2 - Self-Concept Circle."""
    r = 190 if blank else 138
    size = 2 * r + 30
    cx = cy = size / 2
    parts = [f"<circle cx='{cx}' cy='{cy}' r='{r}' fill='{PAPER}' stroke='{INK}' stroke-width='1.6'/>"]
    for a in (0, 90, 180, 270):
        rad = math.radians(a)
        parts.append(f"<line x1='{cx}' y1='{cy}' x2='{cx + r * math.cos(rad):.1f}' "
                     f"y2='{cy + r * math.sin(rad):.1f}' stroke='{INK}' stroke-width='1.2'/>")
    labels = [(cx, cy - r + 20, "BODY"), (cx + 0.52 * r, cy - 8, "PERSONALITY"),
              (cx, cy + r - 16, "ABILITIES"), (cx - 0.52 * r, cy - 8, "FAMILY ROLE")]
    for x, y, t in labels:
        parts.append(_text(x, y, [t], size=13, weight="600"))
    parts.append(_text(cx, cy + 8, ["write each part", "in your own words"], size=9, color="#7d8896"))
    return _svg(size, size, "".join(parts))


def wheel(blank=False):
    """A1 Q4 - Wheel of Emotions: the five emotions of that evening."""
    names = [] if blank else ["anticipation", "nervousness", "pride", "fear of\nembarrassment", "hope"]
    fills = ["#e8f0fa", "#fdf1dc", "#e6f4ea", "#fbe6e6", "#eee9f7"]
    r = 165 if blank else 140
    cx = cy = r + 20
    step = 2 * math.pi / 5
    parts = []
    for i, fl in enumerate(fills):
        a0 = -math.pi / 2 + i * step + 0.012
        a1 = -math.pi / 2 + (i + 1) * step - 0.012
        parts.append(_wedge(cx, cy, r, a0, a1, fl))
        if names:
            am = (a0 + a1) / 2
            tx, ty = cx + r * 0.62 * math.cos(am), cy + r * 0.62 * math.sin(am)
            parts.append(_text(tx, ty, names[i].split("\n"), size=10.5, color=INK))
    parts.append(f"<circle cx='{cx}' cy='{cy}' r='40' fill='{PAPER}' stroke='{INK}' stroke-width='1.4'/>")
    if blank:
        parts.append(_text(cx, cy + 4, ["write here"], size=9, color="#9aa7b6"))
    else:
        parts.append(_text(cx, cy - 4, ["the demo"], size=10.5, weight="600"))
        parts.append(_text(cx, cy + 10, ["evening"], size=10.5, weight="600"))
    parts.append(_text(cx, 18, ["Wheel of Emotions"], size=13, weight="600", color=ACCENT))
    return _svg(2 * cx, 2 * cy, "".join(parts))


def feeling_wheel(blank=False):
    """A1 Q5 - Feeling Wheel: primary emotions with the one I felt marked."""
    names = ["joy", "trust", "fear", "surprise", "sadness", "anger"]
    fills = ["#e6f4ea", "#e8f0fa", "#fdf1dc", "#eee9f7", "#eef2f7", "#fbe6e6"]
    r = 155 if blank else 138
    cx = cy = r + 20
    step = 2 * math.pi / len(names)
    parts = []
    for i, (nm, fl) in enumerate(zip(names, fills)):
        a0 = -math.pi / 2 + i * step + 0.012
        a1 = -math.pi / 2 + (i + 1) * step - 0.012
        parts.append(_wedge(cx, cy, r, a0, a1, fl))
        am = (a0 + a1) / 2
        parts.append(_text(cx + r * 0.7 * math.cos(am), cy + r * 0.7 * math.sin(am) + 3, [nm], size=10.5))
    parts.append(f"<circle cx='{cx}' cy='{cy}' r='46' fill='{PAPER}' stroke='{ACCENT}' stroke-width='1.6'/>")
    if blank:
        parts.append(_text(cx, cy - 4, ["the emotion"], size=10.5, color="#9aa7b6"))
        parts.append(_text(cx, cy + 11, ["you felt", "write it here"], size=9, color="#9aa7b6"))
    else:
        parts.append(_text(cx, cy - 4, ["embarrassment"], size=10.5, weight="600", color=ACCENT))
        parts.append(_text(cx, cy + 11, ["what I felt"], size=9.5, color="#5b6b82"))
    parts.append(_text(cx, 18, ["Feeling Wheel - the emotion named precisely"], size=13, weight="600", color=ACCENT))
    return _svg(2 * cx, 2 * cy, "".join(parts))


def johari(blank=False):
    """A1 Q9 - Johari Window."""
    w, h = (500, 340) if blank else (430, 300)
    cw, ch = w / 2, h / 2
    quads = [
        (0, 0, "OPEN", "I know it, others know it", "#e8f0fa"),
        (cw, 0, "HIDDEN", "I know it, others do not", "#fdf1dc"),
        (0, ch, "UNKNOWN", "none of us knows it yet", "#eef2f7"),
        (cw, ch, "BLIND SPOT", "others see it, I have not realised", "#fbe6e6"),
    ]
    parts = []
    for x, y, t, sub, fl in quads:
        parts.append(f"<rect x='{x}' y='{y}' width='{cw}' height='{ch}' fill='{fl}' stroke='{INK}' stroke-width='1.4'/>")
        parts.append(_text(x + cw / 2, y + 34, [t], size=13.5, weight="600"))
        parts.append(_text(x + cw / 2, y + 52, _wrap(sub, 30), size=9.8, color="#5b6b82", lh=12))
        if blank:
            for k in range(2):
                yy = y + ch - 34 + k * 20
                parts.append(_guide(x + 18, yy, x + cw - 18, yy))
    parts.append(f"<line x1='{cw}' y1='0' x2='{cw}' y2='{h}' stroke='{INK}' stroke-width='1.4'/>")
    parts.append(f"<line x1='0' y1='{ch}' x2='{w}' y2='{ch}' stroke='{INK}' stroke-width='1.4'/>")
    parts.append(_text(w / 2, 18, ["Johari Window"], size=13, weight="600", color=ACCENT))
    parts.append(_text(cw / 2, h - 8, ["known to others"], size=9.5, color="#5b6b82"))
    parts.append(_text(w - 6, h - 8, ["known to me"], size=9.5, color="#5b6b82", anchor="end"))
    return _svg(w, h, "".join(parts))


def esteem_tree(blank=False):
    """A1 Q10 - Self-Esteem Tree."""
    s = 1.18 if blank else 1.0
    w, h = 330 * s, 380 * s

    def P(x, y):
        return x * s, y * s

    parts = []
    x0, y0 = P(165, 330)
    x1, y1 = P(165, 120)
    parts.append(f"<line x1='{x0:.1f}' y1='{y0:.1f}' x2='{x1:.1f}' y2='{y1:.1f}' "
                 f"stroke='#7a5230' stroke-width='{9*s:.1f}' stroke-linecap='round'/>")
    for bx0, by0, bx1, by1 in ((165, 250, 90, 205), (165, 210, 245, 165),
                               (165, 285, 80, 250), (165, 300, 250, 265)):
        ax, ay = P(bx0, by0)
        bx, by = P(bx1, by1)
        parts.append(f"<line x1='{ax:.1f}' y1='{ay:.1f}' x2='{bx:.1f}' y2='{by:.1f}' "
                     f"stroke='#7a5230' stroke-width='{5*s:.1f}' stroke-linecap='round'/>")
    for fx, fy, fr in ((165, 105, 62), (95, 195, 34), (240, 155, 34),
                       (70, 245, 30), (255, 260, 30), (140, 150, 30)):
        cx, cy = P(fx, fy)
        parts.append(f"<circle cx='{cx:.1f}' cy='{cy:.1f}' r='{fr*s:.1f}' fill='#e6f4ea' "
                     f"stroke='#3f7d52' stroke-width='1.4'/>")
    gx0, gy = P(135, 330)
    gx1, _ = P(195, 330)
    parts.append(f"<line x1='{gx0:.1f}' y1='{gy:.1f}' x2='{gx1:.1f}' y2='{gy:.1f}' "
                 f"stroke='#7a5230' stroke-width='{7*s:.1f}' stroke-linecap='round'/>")
    for lx, ly, t, size, col in ((165, 100, "ROOTS", 10, "#3f7d52"), (95, 190, "BRANCH", 9, "#3f7d52"),
                                 (240, 150, "LEAF", 9, "#3f7d52"), (70, 240, "LEAF", 9, "#3f7d52"),
                                 (255, 255, "FRUIT", 9, "#3f7d52"), (165, 288, "TRUNK", 10, "#7a5230")):
        cx, cy = P(lx, ly)
        parts.append(_text(cx, cy, [t], size=size, weight="600", color=col))
    cx, cy = P(165, 20)
    parts.append(_text(cx, cy, ["My Self-Esteem Tree"], size=13, weight="600", color=ACCENT))
    cx, cy = P(165, 360)
    parts.append(_text(cx, cy, ["roots = what gives me strength"], size=9.5, color="#5b6b82"))
    cx, cy = P(165, 374)
    parts.append(_text(cx, cy, ["leaves = what I have done so far"], size=9.5, color="#5b6b82"))
    return _svg(w, h, "".join(parts))


def swot(blank=False):
    """A2 Q5 - SWOT grid."""
    w, h = (500, 380) if blank else (470, 350)
    quads = [
        (0, 0, "STRENGTHS", "#e8f0fa", ["long blocks of focus", "notes on everything",
                                         "honest estimates", "no agenda, no meeting"]),
        (w / 2, 0, "WEAKNESSES", "#fbe6e6", ["start before the last is done", "hard task last, at night",
                                             "yes before checking the list", "no buffer in the week"]),
        (0, h / 2, "OPPORTUNITIES", "#e6f4ea", ["batch admin into two windows", "weekly review, empty list",
                                                 "a shared board for requests"]),
        (w / 2, h / 2, "THREATS", "#fdf1dc", ["deadlines arrive in clusters", "the tracker becomes the hobby",
                                              "a fixed lab slot ends flexibility"]),
    ]
    parts = []
    for x, y, t, fl, items in quads:
        parts.append(f"<rect x='{x}' y='{y}' width='{w/2}' height='{h/2}' fill='{fl}' stroke='{INK}' stroke-width='1.4'/>")
        parts.append(_text(x + 10, y + 20, [t], size=11.5, weight="600", anchor="start"))
        if blank:
            for k in range(4):
                yy = y + 42 + k * 20
                parts.append(_guide(x + 12, yy, x + w / 2 - 12, yy))
        else:
            for i, it in enumerate(items):
                parts.append(_text(x + 10, y + 40 + i * 15, ["- " + it], size=9.6, anchor="start"))
    parts.append(_text(w / 2, 16, ["Personal SWOT - time management in a semester"], size=12.5, weight="600", color=ACCENT))
    return _svg(w, h, "".join(parts))


DIAGRAMS = {
    "circle": circle,
    "wheel": wheel,
    "feeling-wheel": feeling_wheel,
    "johari": johari,
    "esteem-tree": esteem_tree,
    "swot": swot,
}


def render(marker, blank=False):
    """Marker text like [diagram: wheel] -> the SVG html."""
    name = marker.strip().strip("[]").split(":", 1)[-1].strip()
    fn = DIAGRAMS.get(name)
    return fn(blank) if fn else ""
