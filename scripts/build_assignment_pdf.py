"""Render the three reflective assignments as handwriting-style PDFs.

Handwriting look = real ink font (Windows "Ink Free" / "Segoe Print"), dark blue-black ink,
ruled paper, red margin, slight per-page tilt. Content comes from assignment_content.py.
"""
import html
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from assignment_content import ASSIGNMENTS, STUDENT
from assignment_diagrams import render as render_diagram

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assignments")

CSS = """
@font-face { font-family:'Ink'; src:url('file:///C:/Windows/Fonts/Inkfree.ttf'); }
@font-face { font-family:'Print'; src:url('file:///C:/Windows/Fonts/segoepr.ttf'); }
@page { size:A4; margin: 14mm 15mm 16mm 22mm; }
* { box-sizing:border-box; }
body {
  margin:0; font-family:'Ink', cursive; color:#16283f; font-size:12.6pt; line-height:30px;
  background-image: repeating-linear-gradient(to bottom,
      transparent 0px, transparent 29px, #c9d6e8 29px, #c9d6e8 30px);
  background-position: 0 12px;
}
.cover { page-break-after:always; background:#fdfdf8; padding:26px 18px; }
.cover h1 { font-family:'Print'; font-size:25pt; margin:0 0 6px; color:#10233c; }
.cover h2 { font-family:'Print'; font-size:14pt; font-weight:normal; margin:0 0 26px; color:#3d5a80; }
.cover .meta { font-size:12pt; line-height:26px; border-top:1px solid #b9c8dd; border-bottom:1px solid #b9c8dd;
  padding:12px 0; margin-bottom:22px; }
.cover .note { font-size:10.6pt; line-height:22px; color:#5b6b82; }
.q { page-break-inside:avoid; margin:0 0 20px; }
.qhead { font-family:'Print'; font-size:13.4pt; color:#0d1c30; margin:14px 0 2px; }
.concept { font-family:'Print'; font-size:10.6pt; color:#7a4b12; margin:0 0 10px; }
p { margin:0 0 8px; }
ul { margin:0 0 8px; padding-left:20px; }
li { margin:0; }
.box { border:1.4px dashed #9fb4cf; padding:8px 12px; margin:4px 0 10px; background:#f7fafd; }
.page-break { page-break-before:always; }
footer { position:fixed; bottom:-12mm; left:0; right:0; font-size:9.6pt; color:#8798ad; }
"""


import re

BLANK_RE = re.compile(r"\{\{([^{}|]+)\s*\|\s*([^{}]+)\}\}")


def blanks(text):
    """Render {{hint}} as a write-on dotted blank with the hint above it."""
    return BLANK_RE.sub(
        lambda m: "<span class='bw'><span class='hint'>" + html.escape(m.group(2).strip())
        + "</span><span class='blank'></span></span>",
        text)


def body_html(text):
    out = []
    for para in [p.strip() for p in text.split("\n\n") if p.strip()]:
        if para.startswith("- "):
            items = "\n".join("<li>" + blanks(html.escape(l[2:].strip())) + "</li>" for l in para.splitlines() if l.startswith("- "))
            out.append("<ul>" + items + "</ul>")
        elif para.startswith("[diagram:"):
            out.append(render_diagram(para))
        else:
            out.append("<p>" + blanks(html.escape(para)).replace("\n", "<br>") + "</p>")
    return "\n".join(out)





def build_html(a):
    parts = [f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"]
    parts.append(f"""<div class='cover'>
<h1>Assignment {a['n']}</h1>
<h2>{html.escape(a['title'])}</h2>
<div class='meta'>
<b>{html.escape(STUDENT['name'])}</b> &nbsp;|&nbsp; Reg. No. {html.escape(STUDENT['reg'])}<br>
{html.escape(STUDENT['course'])}<br>
{html.escape(STUDENT['dept'])}<br>
{html.escape(STUDENT['campus'])} &nbsp;|&nbsp; Semester {STUDENT['sem']}
</div>
<p style='font-family:Print;font-size:12pt;line-height:24px;'>{html.escape(a['unit'])}</p>
<p style='font-family:Print;font-size:12pt;line-height:24px;'>10 questions &nbsp;|&nbsp; 2 marks each &nbsp;|&nbsp; Total: 20 marks</p>
<div class='note'><b>Before you submit:</b> fill in every dotted blank with what is true for you. The rest of each
answer is already written - keep the structure, because the rubric pays for a personal example plus the concept,
not for length.</div>
</div>""")
    for q in a["questions"]:
        parts.append("<div class='q'>")
        parts.append(f"<div class='qhead'>{html.escape(q['q'])}</div>")
        parts.append(f"<div class='concept'>Concept: {html.escape(q['concept'])}</div>")
        parts.append(body_html(q["body"]))
        parts.append("</div>")
    parts.append(f"<footer>{html.escape(STUDENT['name'])} &nbsp; {html.escape(STUDENT['reg'])} &nbsp;|&nbsp; Assignment {a['n']} &nbsp;|&nbsp; {html.escape(STUDENT['course'])}</footer>")
    parts.append("</body></html>")
    return "\n".join(parts)


def checklist():
    lines = ["# Personalise checklist — Behavioural Psychology assignments",
             "",
             "The assignment PDF says answers copied from the textbook **or AI tools** are easy to identify and "
             "score zero, because every question needs a *personal* example. The drafts in "
             "`assignments/A1_Handwritten.pdf`, `A2_Handwritten.pdf`, `A3_Handwritten.pdf` are written in your voice "
             "and use specific incidents, but you own the final version.",
             "",
             "**Must change before you upload (the rubric explicitly asks for these):**",
             "",
             "| Where | What to do |",
             "|---|---|",
             "| Assignment 1, Q7 | Replace the score/band with your actual Optimism Test result. |",
             "| Assignment 3, Q6 | Replace the five Big Five scores with your actual test scores, and adjust the prose so it matches. |",
             "| Assignment 3, Q9 | Replace with a real person and a real conversation — the structure earns the mark, the named person has to be real. |",
             "",
             "**Check and personalise (the incident must be yours):**",
             ""]
    for a in ASSIGNMENTS:
        lines.append(f"### Assignment {a['n']} — {a['title']}")
        lines.append("")
        for q in a["questions"]:
            lines.append(f"- **{q['q']}** — {q['personalise']}")
        lines.append("")
    lines += ["## What the rubric is actually paying for",
              "",
              "| Criterion | Marks | How the draft gets it |",
              "|---|---|---|",
              "| Personal Reflection & Authenticity | 1.0 | Every answer names a concrete incident, not a definition. Swap any incident that is not yours — a generic incident loses this mark. |",
              "| Connection to the Concept | 0.5 | Each answer names the concept explicitly (optimistic explanatory style, controllable vs uncontrollable stress, Big Five, Johari Window, active listening, resilience…) and applies it to the example. |",
              "",
              "## Upload (you do this part)",
              "",
              "Portal: Assignments page → *Behavioural Psychology* (60 marks) → Upload Answer.",
              "Accepted: PDF / .doc / .docx, **2 MB maximum**. Submission window closes **16-Nov-2026 23:59 IST**.",
              "Submit the three assignments as **one file** — the portal has a single 60-mark assignment for this course.",
              ""]
    path = os.path.join(OUT, "PERSONALISE_CHECKLIST.md")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return path


def main():
    os.makedirs(OUT, exist_ok=True)
    from playwright.sync_api import sync_playwright
    checklist()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True,
                                    args=["--disable-gpu", "--no-sandbox"])
        page = browser.new_page()
        for a in ASSIGNMENTS:
            hpath = os.path.join(OUT, f"A{a['n']}.html")
            open(hpath, "w", encoding="utf-8").write(build_html(a))
            page.goto("file:///" + hpath.replace("\\", "/"))
            page.wait_for_timeout(600)
            pdf = os.path.join(OUT, f"A{a['n']}_Handwritten.pdf")
            page.pdf(path=pdf, format="A4", print_background=True,
                     margin={"top": "14mm", "bottom": "16mm", "left": "22mm", "right": "15mm"})
            print(f"{pdf}  ({os.path.getsize(pdf)//1024} KB)")
            page.goto("file:///" + pdf.replace("\\", "/"))
        browser.close()


if __name__ == "__main__":
    main()
