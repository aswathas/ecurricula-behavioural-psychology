# Behavioural Psychology (21GNH401TA) — e-Curricula assignment pipeline

The written work for one SRMIST course, and the scripts that turn a question
sheet into the PDFs that were submitted.

The public half of this repository is **the documents and the builders**. The
portal automation — the browser client, the login, the OTP, the submission
calls — is not published. See [What is not published](#what-is-not-published).

---

## What is here

| Path | What it is |
|---|---|
| `assignments/` | The finished work: typed answers, filled answer sheets, the handwritten versions and the personalisation checklist. Markdown, HTML and PDF. |
| `work/assignment_questions.json` | The questions, structured: number, title, concept, stem, word count, marks. |
| `work/figure_answers.txt` | The answer to every figure question, keyed by question number. |
| `scripts/assignment_content.py` | The answers, as data. One module, one source of truth for every document. |
| `scripts/assignment_diagrams.py` | The figure renderer used by the answers. |
| `scripts/sheet_figures.py` | The figure builder for the answer-sheet worksheets. |
| `scripts/build_assignment_*.py` | The document builders. Each is standalone and reads only files in this repository. |
| `docs/plan.md` | The course and portal spec: mark structure, session shape, what the portal exposes. |
| `docs/how-to-build.md` | How to rebuild every artefact from the questions and the answers. |
| `docs/privacy.md` | What is deliberately absent, and why. |
| `docs/reviews/` | The decision log, the change inventory and the delivery plan: what was decided, why, and how it was checked. |
| `tools/check_no_secrets.py` | The pre-push check. Fails if anything credential-shaped is tracked. |

## Why it is shaped like this

The course's written work is a three-part PDF of questions. What it needed was
not a word processor; it needed a pipeline:

1. **Questions in, structured.** The question paper is read into JSON once, so
   every later step works on data instead of on a document.
2. **Answers in, structured.** Each answer carries its own word budget, taken
   from the question, so a long answer does not silently eat the next question.
3. **Documents out, from one source.** The typed answers, the fill-in sheet,
   the handwritten sheets and the checklist all come from the same content
   module. Change one answer, rebuild everything.
4. **Checked, not assumed.** The builders assert on the output: the right
   number of sections, the right word counts, the right page count. A build
   that loses a section fails instead of shipping.

## Requirements

```
python 3.9+          # standard library only
```

PDF output needs LibreOffice on the path (`soffice`) for the `.docx` path, or
any Markdown-to-PDF tool for the Markdown. The handwritten builder renders
HTML with a Windows ink font and converts it with `soffice`.

## Quick start

```bash
git clone https://github.com/aswathas/ecurricula-behavioural-psychology.git
cd ecurricula-behavioural-psychology

# the typed answers and the fill-in sheet
python scripts/build_assignment_fill.py

# the handwriting-style PDFs
python scripts/build_assignment_pdf.py

# the answer-sheet worksheets (blank, then answered)
python scripts/build_assignment_sheet.py blank
python scripts/build_assignment_sheet.py answered

# the pre-push check: nothing credential-shaped is tracked
python tools/check_no_secrets.py
```

Every builder takes an optional mode argument and prints what it wrote.
Details per builder: [docs/how-to-build.md](docs/how-to-build.md).

## How the pieces fit

```
work/assignment_questions.json  ┐
work/figure_answers.txt         ├─> scripts/assignment_content.py  ─> the answers
scripts/assignment_diagrams.py  ┘            │
                                             ├─> build_assignment_fill  -> ANSWERS_TYPED.{md,html,pdf}
                                             │                      -> ANSWERS_FILL.{md,html,pdf}
                                             ├─> build_assignment_pdf  -> A1/A2/A3_Handwritten.pdf
                                             └─> build_assignment_sheet-> SHEET / SHEET_ANSWERS.{html,pdf}
```

`work/assignment_questions.json` holds the marks and the word budget;
`work/figure_answers.txt` holds the answer to every figure question. Neither
is needed for the content module, which already carries the prose.

## What is not published

Not in this repository, on purpose:

- **Credentials.** The SRM account, the Google Authenticator setup key, the
  generated one-time codes and the recovery code.
- **Browser profiles.** A copied Chrome or Brave profile holds a live Google
  and SRM session.
- **Portal traffic.** API responses, session dumps, screenshots, cookies,
  submission logs.
- **The portal client and the submission scripts.** The login, the OTP, the
  submission calls and the upload helpers stay on the machine that owns the
  account. Publishing them would publish someone's session.
- **The course material itself.** The question paper PDF and the worksheet
  templates were fetched from the portal; they are the university's, not this
  repository's.

The published repository therefore contains no way to log in to anything.
Details: [docs/privacy.md](docs/privacy.md).

## Licence

MIT. The answers, the scripts and the documentation in this repository are
mine; the course material they are derived from is not, and is not included.

## Note on use

This is my own coursework and my own tooling for it. Use it as a reference for
building documents from structured data — not as a way to complete someone
else's assessed work.
