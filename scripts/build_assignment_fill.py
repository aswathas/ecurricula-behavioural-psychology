"""Render the assignment pack in normal text, in two modes.

  FILL    - every {{key | hint}} becomes a dotted write-on blank; the cover lists the blanks.
  ANSWERS - the same document with every blank filled from BLANK_ANSWERS (the reference copy).

Questions, concepts, prose and diagram markers come from assignment_content.py;
the figures come from assignment_diagrams.py. One PDF and one Markdown file per mode.

Usage: python scripts/build_assignment_fill.py [fill|answers]
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from assignment_content import ASSIGNMENTS, BLANK_ANSWERS, STUDENT
from assignment_diagrams import render as render_diagram

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assignments")
BLANK_RE = re.compile(r"\{\{([^{}|]+?)\s*\|\s*([^{}]+?)\}\}")

CSS = """
@page { size: A4; margin: 18mm 16mm 16mm 16mm; }
body { font-family: "Segoe UI", system-ui, sans-serif; font-size: 10.6pt; color: #17212f; line-height: 1.55; }
.cover { page-break-after: always; }
.cover h1 { font-size: 22pt; margin: 0 0 4px; color: #0f1e33; border-bottom: 2.5px solid #2b6cb0; padding-bottom: 8px; }
.cover h2 { font-size: 13.5pt; margin: 2px 0 18px; color: #3d5a80; font-weight: normal; }
.cover .meta { font-size: 10.6pt; line-height: 1.7; background: #f5f8fc; border: 1px solid #d6e0ec; border-radius: 6px; padding: 12px 14px; }
.cover .unit { margin: 16px 0 4px; font-size: 11.4pt; color: #2b6cb0; font-weight: 600; }
.cover .note { margin-top: 16px; font-size: 9.8pt; color: #5b6b82; border-left: 3px solid #c3d2e4; padding: 8px 12px; background: #fbfcfe; }
.cover h3 { font-size: 10.4pt; margin: 20px 0 6px; color: #1f4e79; text-transform: uppercase; letter-spacing: .4px; }
.bl { font-size: 9.6pt; color: #5b6b82; margin: 0; padding-left: 22px; }
.bl li { margin: 2px 0; }
.q { page-break-inside: avoid; margin: 0 0 16px; }
.qhead { font-size: 11.8pt; font-weight: 600; color: #0d1c30; margin: 14px 0 2px; }
.concept { font-size: 9.6pt; color: #8a5a12; margin: 0 0 8px; }
p { margin: 0 0 7px; }
ul { margin: 0 0 8px; padding-left: 20px; }
.bw { display: inline-block; vertical-align: bottom; margin: 0 3px; }
.hint { display: block; font-size: 8.6pt; color: #7d8896; font-style: italic; line-height: 1.25; }
.blank { display: block; border-bottom: 1px dotted #64707f; height: 1.25em; min-width: 200px; }
.diagram { display: block; margin: 4px auto 12px; }
"""


def blanks(text, mode):
    """FILL: a write-on dotted blank with the hint above it. ANSWERS: the filled text."""
    if mode == "answers":
        return BLANK_RE.sub(lambda m: html.escape(BLANK_ANSWERS.get(m.group(1).strip(), m.group(2).strip())), text)
    return BLANK_RE.sub(
        lambda m: "<span class='bw'><span class='hint'>" + html.escape(m.group(2).strip())
        + "</span><span class='blank'></span></span>",
        text)


def body_html(text, mode):
    out = []
    for para in [p.strip() for p in text.split("\n\n") if p.strip()]:
        if para.startswith("- "):
            items = "\n".join("<li>" + blanks(html.escape(l[2:].strip()), mode) + "</li>"
                              for l in para.splitlines() if l.startswith("- "))
            out.append("<ul>" + items + "</ul>")
        elif para.startswith("[diagram:"):
            out.append(render_diagram(para))
        else:
            out.append("<p>" + blanks(html.escape(para), mode).replace("\n", "<br>") + "</p>")
    return "\n".join(out)


def blank_hints(a):
    """Every blank hint in this assignment, in order."""
    hints = []
    for q in a["questions"]:
        hints += [m.group(2).strip() for m in BLANK_RE.finditer(q["body"])]
    return hints


def build_html(mode):
    parts = ["<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>"]
    for a in ASSIGNMENTS:
        note = ("<b>Before you submit:</b> fill in every dotted blank with what is true for you. The rest of each "
                "answer is already written - keep the structure, because the rubric pays for a personal example plus "
                "the concept, not for length."
                if mode == "fill" else
                "<b>Reference copy:</b> every answer is written out here. Use it to check the fill-in copy, or to "
                "copy any answer across. The blanks in the FILL copy are the personal facts only.")
        hints = blank_hints(a)
        blist = ("<ul class='bl'>" + "".join("<li>" + html.escape(h) + "</li>" for h in hints)
                 + "</ul>") if mode == "fill" else ""
        blhead = "<h3>Blanks to fill in this assignment</h3>" if mode == "fill" else ""
        parts.append(f"""<div class='cover'>
<h1>Assignment {a['n']}</h1>
<h2>{html.escape(a['title'])}</h2>
<div class='meta'>
<b>{html.escape(STUDENT['name'])}</b> &nbsp;|&nbsp; Reg. No. {html.escape(STUDENT['reg'])}<br>
{html.escape(STUDENT['course'])}<br>
{html.escape(STUDENT['dept'])}<br>
{html.escape(STUDENT['campus'])} &nbsp;|&nbsp; Semester {STUDENT['sem']}
</div>
<p class='unit'>{html.escape(a['unit'])}</p>
<p>10 questions &nbsp;|&nbsp; 2 marks each &nbsp;|&nbsp; Total: 20 marks</p>
<div class='note'>{note}</div>
{blhead}
{blist}
</div>""")
        for q in a["questions"]:
            parts.append("<div class='q'>")
            parts.append(f"<div class='qhead'>{html.escape(q['q'])}</div>")
            parts.append(f"<div class='concept'>Concept: {html.escape(q['concept'])}</div>")
            parts.append(body_html(q["body"], mode))
            parts.append("</div>")
    parts.append("</body></html>")
    return "\n".join(parts)


def build_md(mode):
    base = ("Behavioural_Psychology_Assignments_1-3_FILL" if mode == "fill"
            else "Behavioural_Psychology_Assignments_1-3_ANSWERS_TYPED")
    lines = ["# Behavioural Psychology - assignments" + (" (fill in the blanks)" if mode == "fill" else " (answers written out)"), "",
             f"**{STUDENT['name']}** | Reg. No. {STUDENT['reg']}  ",
             f"{STUDENT['course']}  ",
             f"{STUDENT['dept']}  ",
             f"{STUDENT['campus']} | Semester {STUDENT['sem']}", ""]
    lines += ["Fill in every `______ (hint)` blank with what is true for you. The rest is written and ready.",
              "One file for the portal: the three assignments as one document, 2 MB maximum, due 16-Nov-2026 23:59 IST.",
              ""] if mode == "fill" else [
              "Every answer is written out. The matching fill-in copy is `Behavioural_Psychology_Assignments_1-3_FILL.pdf`.",
              "One file for the portal: the three assignments as one document, 2 MB maximum, due 16-Nov-2026 23:59 IST.", ""]
    for a in ASSIGNMENTS:
        lines += [f"## Assignment {a['n']} - {a['title']}", "",
                  f"*{a['unit']}*  ", "10 questions | 2 marks each | Total: 20 marks", ""]
        if mode == "fill":
            lines += ["**Blanks to fill in this assignment:**", ""]
            lines += [f"- {h}" for h in blank_hints(a)]
            lines += [""]
        lines += ["---", ""]
        for q in a["questions"]:
            lines += [f"### {q['q']}", "", f"*Concept: {q['concept']}*", ""]
            for para in [p.strip() for p in q["body"].split("\n\n") if p.strip()]:
                if para.startswith("- "):
                    lines += ["- " + l[2:].strip() for l in para.splitlines() if l.startswith("- ")]
                elif para.startswith("[diagram:"):
                    lines += [f"*[figure: {para.split(':', 1)[1].strip('] ').strip()}]*", ""]
                    continue
                else:
                    if mode == "fill":
                        lines += [BLANK_RE.sub(lambda m: "______ (" + m.group(2).strip() + ")", para)]
                    else:
                        lines += [BLANK_RE.sub(lambda m: BLANK_ANSWERS.get(m.group(1).strip(), m.group(2).strip()), para)]
                lines += [""]
    path = os.path.join(OUT, base + ".md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


def render(mode):
    os.makedirs(OUT, exist_ok=True)
    from playwright.sync_api import sync_playwright
    base = ("Behavioural_Psychology_Assignments_1-3_FILL" if mode == "fill"
            else "Behavioural_Psychology_Assignments_1-3_ANSWERS_TYPED")
    md_path = build_md(mode)
    html_path = os.path.join(OUT, base + ".html")
    open(html_path, "w", encoding="utf-8").write(build_html(mode))
    pdf_path = os.path.join(OUT, base + ".pdf")
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True,
                                    args=["--disable-gpu", "--no-sandbox"])
        page = browser.new_page()
        page.goto("file:///" + html_path.replace("\\", "/"))
        page.wait_for_timeout(900)
        page.pdf(path=pdf_path, format="A4", print_background=True, display_header_footer=True,
                 header_template="<div></div>",
                 footer_template=("<div style='font-size:8px;width:100%;padding:0 16mm;color:#8798ad;'>"
                                  f"{html.escape(STUDENT['name'])} | {html.escape(STUDENT['reg'])} | "
                                  f"{html.escape(STUDENT['course'])}</div>"),
                 margin={"top": "18mm", "bottom": "16mm", "left": "16mm", "right": "16mm"})
        browser.close()
    return pdf_path, md_path


def main():
    modes = sys.argv[1:] or ["fill", "answers"]
    for mode in modes:
        if mode not in ("fill", "answers"):
            print("unknown mode:", mode)
            continue
        pdf, md = render(mode)
        print(f"{mode}: {pdf} ({os.path.getsize(pdf)//1024} KB) | {md} ({os.path.getsize(md)//1024} KB)")


if __name__ == "__main__":
    main()
