"""Build the handwriting answer sheet for the three assignments.

Two documents from one source:

  blank  - assignments/Behavioural_Psychology_Assignments_1-3_SHEET.pdf
           every question in the coordinator's own wording, a full-page empty
           template for each figure, and ruled space to write on. No answers.
  answers- assignments/Behavioural_Psychology_Assignments_1-3_SHEET_ANSWERS.pdf
           the same document with the model answers typed in, so the space can
           be judged against a real answer.

The rubric zeroes answers copied from the textbook, classmates or AI tools, so
the blank sheet is the artefact to print and write on; the answers copy is for
checking only.

Usage: python scripts/build_assignment_sheet.py [blank|answers]
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from assignment_content import ASSIGNMENTS, BLANK_ANSWERS, STUDENT
from sheet_figures import render as render_figure

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assignments")
QUESTIONS = os.path.join(ROOT, "work", "assignment_questions.json")
MARKER_RE = re.compile(r"^\[diagram:\s*([^\]]+)\]\s*$", re.M)
HEAD_RE = re.compile(r"^([A-Z][A-Z ]*(?:\([^)]*\))?)\s*:?\s*$")
BLANK_RE = re.compile(r"\{\{(\w+)\s*\|[^}]*\}\}")

CSS = """
@page { size: A4; margin: 14mm 16mm 14mm 16mm; }
body { font-family: "Segoe UI", system-ui, sans-serif; font-size: 10.8pt; color: #17212f; line-height: 1.5; }
.cover { page-break-after: always; }
.cover h1 { font-size: 21pt; margin: 0 0 4px; color: #0f1e33; border-bottom: 2.5px solid #2b6cb0; padding-bottom: 8px; }
.cover h2 { font-size: 13pt; margin: 2px 0 16px; color: #3d5a80; font-weight: normal; }
.cover .meta { font-size: 10.6pt; line-height: 1.7; background: #f5f8fc; border: 1px solid #d6e0ec; border-radius: 6px; padding: 12px 14px; }
.cover .unit { margin: 14px 0 4px; font-size: 11.2pt; color: #2b6cb0; font-weight: 600; }
.cover .note { margin-top: 14px; font-size: 9.8pt; color: #4b5b70; border-left: 3px solid #c3d2e4; padding: 9px 12px; background: #fbfcfe; }
.cover .note b { color: #8a5a12; }
.qhead { font-size: 12.4pt; font-weight: 600; color: #0d1c30; margin: 14px 0 1px; page-break-after: avoid; }
.qhead span { font-weight: normal; color: #8798ad; font-size: 9.4pt; }
.concept { font-size: 9.4pt; color: #2b6cb0; margin: 0 0 5px; page-break-after: avoid; }
.stem { font-size: 10.6pt; color: #1b2735; margin: 0 0 6px; page-break-after: avoid; }
.hint { font-size: 9.4pt; color: #8a5a12; font-style: italic; margin: 0 0 8px; page-break-after: avoid; }
.figblock { page-break-inside: avoid; }
.writeblock { page-break-before: always; }
.diagram { margin: 4px 0 6px; }
.diagram svg { width: 100%; height: auto; display: block; }
.wl { display: flex; align-items: flex-end; height: 9.6mm; }
.wl .n { width: 7mm; font-size: 8pt; color: #a6b1c0; text-align: right; padding-right: 3mm; }
.wl .rule { flex: 1; border-bottom: 1px dotted #aeb9c6; height: 100%; }
.ansbox { border: 1px solid #d6e0ec; background: #f8fbff; border-radius: 6px; padding: 12px 14px;
          font-size: 10.4pt; line-height: 1.62; white-space: pre-wrap; page-break-inside: avoid; }
.ansbox b { color: #2b6cb0; }
.sub { font-size: 9.6pt; color: #4b5b70; margin: 0 0 8px; }
"""


def line_count(body):
    """Ruled space sized to the model answer, so there is room for a real answer."""
    return max(12, min(30, round(len(body) / 55)))


def fill_blanks(text):
    """Replace the {{key | hint}} blanks with the reference values."""
    def sub(m):
        key = m.group(1)
        return BLANK_ANSWERS.get(key, m.group(0).split("|")[1].strip().rstrip("}"))
    return BLANK_RE.sub(sub, text)


def blocks(body):
    """Split a model answer into (heading, text) blocks on its ALLCAPS headings."""
    out, cur = {}, None
    for line in body.splitlines():
        s = line.strip()
        m = HEAD_RE.match(s)
        if m and not s.startswith("["):
            cur = m.group(1).split("(")[0].strip()
            out.setdefault(cur, [])
        elif cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def figure_answers(name, body):
    """The content that fills each figure template."""
    b = blocks(body)
    if name == "circle":
        note = ""
        if "Hardest section to write:" in body:
            note = body.split("Hardest section to write:", 1)[1].strip()
            body = body.split("Hardest section to write:", 1)[0]
            b = blocks(body)
        return {
            "BODY": fill_blanks(b.get("BODY", "")),
            "PERSONALITY": b.get("PERSONALITY", ""),
            "ABILITIES": b.get("ABILITIES", ""),
            "ROLE IN MY FAMILY": b.get("ROLE IN MY FAMILY", ""),
            "note": note,
        }
    if name == "wheel":
        m = re.search(r"five emotions mixed together were:(.*?)\.", body, re.S)
        items = [i.strip() for i in re.split(r",\s*and\s+|,\s*", m.group(1))] if m else []
        return {"sectors": items}
    if name == "feeling-wheel":
        m = re.search(r"specific emotion was\s+(.*?)\s*(?:[-,]|\.)", body)
        return {"centre": m.group(1) if m else ""}
    if name == "johari":
        ans = {}
        for key, marker in (("OPEN", "OPEN ("), ("HIDDEN", "HIDDEN ("),
                            ("BLIND SPOT", "BLIND SPOT ("), ("UNKNOWN", "UNKNOWN (")):
            if marker in body:
                seg = body.split(marker, 1)[1]
                seg = seg.split(")", 1)[1].lstrip(": ")
                ans[key] = seg.split("\n\n")[0].strip()
        return ans
    if name == "esteem-tree":
        body = body.split("Reflection (40-60 words):")[0]
        b = blocks(body)
        return {k: b.get(k, "") for k in ("ROOTS", "TRUNK", "BRANCHES", "LEAVES", "FRUITS")}
    if name == "swot":
        ans = {}
        for key in ("STRENGTHS", "WEAKNESSES", "OPPORTUNITIES", "THREATS"):
            seg = b.get(key, "")
            seg = seg.split("Honest summary:")[0]
            ans[key] = [l.strip()[2:].strip() for l in seg.splitlines() if l.strip().startswith("- ")]
        return ans
    return {}


def build_html(mode):
    """mode: 'blank' -> empty sheet, 'answers' -> the same sheet with the answers in."""
    answered = mode == "answers"
    stems = json.load(open(QUESTIONS, encoding="utf-8"))
    parts = ["<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>"]
    for a in ASSIGNMENTS:
        qs = {q["n"]: q for q in stems[str(a["n"])]}
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
<div class='note'><b>Write your own answers.</b> The rubric says answers copied from the textbook,
from classmates, or from AI tools are easy to identify and are marked zero for that question - so
everything under each question here is yours to write. Each answer needs one real example from your
own life <b>plus</b> the concept it belongs to. Where a figure is printed, fill it in and label it.
{'This copy is the answer example - do not hand it in.' if answered else 'Print this, fill it in by hand, sign it, upload it.'}</div>
</div>""")
        for q in a["questions"]:
            m = re.search(r"Q(\d+)", q["q"])
            qn = int(m.group(1)) if m else 0
            src = qs.get(qn, {})
            title = src.get("title", q["q"])
            concept = src.get("concept", q["concept"])
            stem = src.get("stem", "")
            body = q["body"]
            marker = MARKER_RE.search(body)
            fname = marker.group(1) if marker else None
            ans = figure_answers(fname, body) if (answered and fname) else {}
            text = fill_blanks(body)
            if marker:
                text = text.replace(marker.group(0), "").strip()

            head = [f"<div class='qhead'>{html.escape(title)}</div>",
                    f"<div class='concept'>Based on {html.escape(concept)}</div>"]
            if stem:
                head.append(f"<div class='stem'>{html.escape(stem)}</div>")
            if answered:
                if ans.get("note"):
                    head.append(f"<div class='hint'>Note: {html.escape(ans['note'])}</div>")
            elif q.get("personalise"):
                head.append(f"<div class='hint'>What to put here: {html.escape(q['personalise'])}</div>")

            if fname:
                # heading and figure share one page; the writing space starts the next
                parts.append("<div class='figblock'>")
                parts.extend(head)
                parts.append(render_figure(fname, blank=not answered, ans=ans))
                parts.append("</div>")
                parts.append("<div class='writeblock'>")
                parts.append(f"<div class='qhead'>{html.escape(title)} "
                             f"<span>- write your answer here</span></div>")
            else:
                parts.extend(head)

            if answered:
                parts.append(f"<div class='ansbox'>{html.escape(text)}</div>")
            else:
                for i in range(1, line_count(body) + 1):
                    parts.append(f"<div class='wl'><span class='n'>{i}</span><span class='rule'></span></div>")
            if fname:
                parts.append("</div>")
            parts.append("</div>")
    parts.append("</body></html>")
    return "\n".join(parts)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "blank"
    os.makedirs(OUT, exist_ok=True)
    from playwright.sync_api import sync_playwright
    base = "Behavioural_Psychology_Assignments_1-3_SHEET"
    name = base if mode == "blank" else base + "_ANSWERS"
    html_path = os.path.join(OUT, name + ".html")
    open(html_path, "w", encoding="utf-8").write(build_html(mode))
    pdf_path = os.path.join(OUT, name + ".pdf")
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
                                  + ("Answer sheet - write by hand" if mode == "blank"
                                     else "ANSWER EXAMPLE - reference only")
                                  + "</div>"),
                 margin={"top": "14mm", "bottom": "14mm", "left": "16mm", "right": "16mm"})
        browser.close()
    print(f"{pdf_path} ({os.path.getsize(pdf_path)//1024} KB)")


if __name__ == "__main__":
    main()
