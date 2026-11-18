# How to build every artefact

Every builder is standalone, reads only files in this repository, and writes
into `assignments/`. Run them from the repository root.

```bash
cd ecurricula-behavioural-psychology
```

## The inputs

| File | Written by | Read by |
|---|---|---|
| `work/assignment_questions.json` | the question paper, read once | `build_assignment_sheet.py` |
| `work/figure_answers.txt` | the figure answers | `scripts/assignment_content.py` |
| `scripts/assignment_content.py` | hand-written; the single source of truth | every builder |
| `scripts/assignment_diagrams.py` | the SVG-ish figure renderer | `build_assignment_pdf.py`, `build_assignment_fill.py` |
| `scripts/sheet_figures.py` | the worksheet figure builder | `build_assignment_sheet.py` |

`assignment_content.py` holds the prose, the marks and the word budget for
every assignment. It is the only file you normally edit.

## The builders

### `build_assignment_fill.py` — typed answers

```bash
python scripts/build_assignment_fill.py            # both modes
python scripts/build_assignment_fill.py fill       # only the fill-in sheet
python scripts/build_assignment_fill.py answers    # only the typed answers
```

Writes into `assignments/`:

- `Behavioural_Psychology_Assignments_1-3_ANSWERS_TYPED.{md,html,pdf}`
- `Behavioural_Psychology_Assignments_1-3_FILL.{md,html,pdf}`

`fill` is the same content laid out as a sheet to write on; `answers` is the
same content set as prose.

### `build_assignment_pdf.py` — handwriting-style PDFs

```bash
python scripts/build_assignment_pdf.py
```

Writes `assignments/A1_Handwritten.pdf`, `A2_Handwritten.pdf`,
`A3_Handwritten.pdf`: the same answers set in an ink font on ruled paper, one
file per assignment. Needs the Windows ink fonts (`Ink Free`, `Segoe Print`)
and `soffice` on the path for the PDF step.

It also writes `assignments/PERSONALISE_CHECKLIST.md` — the list of fields to
fill in by hand before submission.

### `build_assignment_sheet.py` — answer-sheet worksheets

```bash
python scripts/build_assignment_sheet.py blank
python scripts/build_assignment_sheet.py answered
```

Writes `assignments/Behavioural_Psychology_Assignments_1-3_SHEET.{html,pdf}`
and `..._SHEET_ANSWERS.{html,pdf}`. `blank` is the empty worksheet;
`answered` is the same worksheet with the content filled in, for checking.

## The PDF step

The builders write Markdown and HTML. The PDF comes from LibreOffice:

```bash
soffice --headless --convert-to pdf --outdir assignments assignments/<name>.html
```

On Windows the binary is usually
`"C:\Program Files\LibreOffice\program\soffice.exe"`. The builders call it
themselves when it is on the path; if it is not, they still write the `.md`
and `.html` and tell you what is missing.

## Checking the result

The builders assert on their own output — the number of assignments, the word
counts taken from the question file, the page count of the generated PDF. A
build that loses a section fails instead of writing a broken file.

```bash
python tools/check_no_secrets.py    # nothing credential-shaped is tracked
```

## What you need to rebuild this from scratch

1. The question paper, read into `work/assignment_questions.json` — number,
   title, concept, stem, word count, marks, per question.
2. Your answers, in `scripts/assignment_content.py`.
3. The answer to every figure question, in `work/figure_answers.txt`.
4. Python 3.9+ and LibreOffice.

You do not need the portal, an account, or a browser.
