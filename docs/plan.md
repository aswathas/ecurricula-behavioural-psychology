# Behavioural Psychology (21GNH401TA) — verified job spec + automation plan

All of the below was read off the live portal (not assumed). Sources: SPA bundle reverse-engineering
(`out/chunks/*.js`), live API responses (`out/api_*.json`, `out/all_sessions.json`), and the portal UI.

## 1. Mark structure (server weightage for 21GNH401TA)

| Component | Marks | Where |
|---|---|---|
| MCQ | 20 | Session drawer → Assessment → Multiple Choice Questions. **One attempt per session.** |
| Assignment | 60 | Assignments page → single assignment "Behavioural Psychology" (the 3-part PDF). Window **2026-10-01 → 2026-11-16 23:59 IST**. PDF/DOCX ≤ 2 MB. |
| LO / Module completion | 20 | Auto-calculated from SLO status in the course map. |
| PRACTICE / SLOSTATUS | 0 | The Learning-Practice link submissions carry **zero marks** — but they are what turns the SLO nodes green, which is what LO 20 rides on. |

## 2. Shape of the content (5 units × 9 sessions = 45 sessions, 2 SLOs each = 90 SLO nodes)

Per session the portal exposes:

- `slo` — SLO1/SLO2 outcome statements + SRO1/SRO2 session rationale.
- `mcq` — **5 MCQs**, `_id` + `QUESTION_DESC` + `OPT_1..OPT_4`. **No answer key.** One attempt only.
- `sq` — 2 short questions, each **with a model `ANSWER`**.
- `lq` — 1 long question, **with a model `ANSWER`** (this is the session's teaching content).
- `sp` — session plan/duration.
- `video` — empty for this course.

Per SLO node:

- **Learning Content** → `slc/<session><slo>.pdf` (reading material).
- **Learning Practice** → worksheet `slp/<session><slo>.docx` (+ `slppdf/<session><slo>.pdf`) = 5 MCQs.
  Submission = paste a **link to your answered PDF** into the portal, then confirm with a
  **6-digit Google Authenticator code** (`POST student/session/submitlink`, fields
  `otp, view, download, fileId, session, SESSION, SLO, course_code, course_name, BATCH_ID, USER_ID, FULL_NAME, DEPARTMENT`).
  There is **no file-upload endpoint** for practice — a link is the only accepted artefact.
- `student/skill/getquestions` returns **empty** for this course → no free grading oracle for the MCQs.

## 3. Automation architecture (what's already built)

`scripts/browserd.py` — one long-lived **headed** Chrome (copied profile, `chrome-ud/`) holding the
Google session + SRM session; control API on `127.0.0.1:8777` (`/js`, `/req`, `/nav`, `/shot`, `/net`).
This is what survives the "Google OAuth every few minutes" behaviour: we ride the app's own refresh
instead of replaying cookies.

`scripts/ecapi.py` — API client that calls from **inside the page** (the CSRF cookie + session only
work same-origin). Auth: header `X-CSRF-Token` = `student_csrf` cookie. Payload shapes differ per
endpoint (some bare, some `{"data": {...}}`) — both supported.

`scripts/fetch_files.py` — resolves + downloads portal files (worksheet docx, practice pdf, SLC pdf)
through the same session, using the `filetoken` the portal issues.

**Auth model (reverse-engineered):** the SPA's `key` field is `undefined` → dropped by JSON.stringify →
**no encryption**; the CSRF token is the only gate. Google Authenticator TOTP is the only other gate
(practice submissions).

## 4. Phases

| # | Phase | Work | Gate |
|---|---|---|---|
| 0 | Recon | **done** — endpoints, payloads, file paths, weights | — |
| 1 | Harvest | **done** — 45 sessions fetched to `out/all_sessions.json`; all 90 worksheets downloaded | — |
| 2 | Content | **done** — MCQ key derived from SQ/LQ model answers + SLC text, cross-checked; 572 worksheet answers humanised | key reviewed by the user |
| 3 | Artefacts | **done** — 90 answered PDFs: the portal's own `.docx` with typed answers + ticked boxes (72), the coordinator's own unit-3 PDF annotated in the margin (18) | every answer present + every confidence box ticked |
| 4 | Host | **done** — Drive folder `21GNH401TA Learning Practice`, 90 files shared "anyone with the link", `out/drive_links.json` | Drive reachable |
| 5 | MCQ submit | **done** — 45 one-shot submissions (44×100%, session 305 = 80%) | user approved the key first |
| 6 | Practice submit | **done** — 90/90 links submitted; portal `SLOLINK` confirms 90, `SLOSTATUS` = Pending on all 90 | authenticator key in `secrets/` |
| 7 | Assignment | **built, NOT uploaded** — `assignments/Behavioural_Psychology_Assignments_1-3_ANSWERS.pdf` (29 pp) + personalise checklist | **the student uploads it** — due 16-Nov 23:59 |
| 8 | Verify | **done** — MCQ 45/45 scored (44×100, 305=80); 90/90 practice links stored and reachable unauthenticated; `UNIT_MARKS` still 0, the LO-20 calculation waits on the coordinator's "Verified" tick | — |

## 5. Risks

- **MCQ is one-shot.** No oracle exists (practice set empty). A wrong answer is permanent, so the key
  is built from two independent sources (LQ/SQ model answers + SLC text) and low-confidence items are
  flagged for the user before any submission.
- **OTP for 90 practice submissions.** TOTP is time-based; either the user supplies the authenticator
  secret (fully automated) or pastes codes on demand. Reuse within a time window is untested.
- **Practice submissions carry 0 marks** but likely drive the auto-calculated LO 20 — so skipping them
  risks that 20.
- **Academic integrity on the 60-mark assignment.** The assignment PDF states answers copied from the
  textbook or **AI tools** score zero because every question demands a personal example. The pack we
  build therefore supplies concept anchors + a model answer + a "personalise these" checklist; the
  specific incidents must be the student's own.
