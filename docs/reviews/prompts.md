# Prompts — public publication unit

The prompts that produced this unit of work, verbatim from the session.

---

## 1. The instruction that opened the unit

> PUSH OUR BEHVIOURAL ECURRIAL REPO WITH GOOD DOUCMENATION IN GITHUB

**Interpretation.** Publish the course repository to GitHub, with documentation good
enough that a reader understands the pipeline without a human in the room. The
repository at that point held credentials, a live browser profile, portal traffic
and the portal client; publishing it literally would have published the account.
The unit therefore became: separate the public half from the private half, document
the public half, and push only that.

## 2. Standing instructions that shaped it

From the owner's global instructions for every project:

> New skills go to the skills repo — publish it in the same change. A skill that lives
> only on this machine is not done.

From the owner's commit discipline, applied here as:

> Every decision spoken with an AI, every edit, every prompt and every skill added is
> documented in detail and then committed and pushed. A brief with separable parts
> lands as one commit and one push per unit planned in `docs/reviews/delivery-plan.md`.

## 3. Constraints discovered while executing, not from a prompt

These came out of reading the code, not out of an instruction. They are recorded here
because they are the reason the public tree looks the way it does.

| Finding | Consequence |
|---|---|
| `scripts/account.py`, `portal.py`, `ecapi.py`, `browser*.py`, `login_browser.py`, `otp_use.py`, `totp.py`, `session_watch.py` read credentials or hold a live session | Excluded. Publishing them publishes a working path into the account. |
| `submit_mcq.py`, `submit_practice.py`, `upload_drive*.py`, `fetch_*.py`, `harvest_files.py`, `ws_fill.py`, `ws_slots.py` log in, submit or upload | Excluded, same reason. |
| `consolidate_key.py`, `build_unit3_keys.py`, `build_unit3_overlay.py`, `verify_unit3_keys.py` read or write the account-bound portal key | Excluded. |
| `build_briefs.py`, `plan_slos.py` import `account` / `ecapi` | Excluded. |
| `build_answered_typed.py`, `build_answered_worksheets.py` import `account` | Excluded. |
| `build_master_pdf.py` writes only into `out/` with a hardcoded absolute path | Excluded: it produces nothing the public tree holds. |
| `assignment_content.py`, `assignment_diagrams.py`, `sheet_figures.py`, `build_assignment_fill.py`, `build_assignment_pdf.py`, `build_assignment_sheet.py` import nothing local | Published. They are the pipeline. |
| The three builders hardcoded `C:\\Users\\ADMIN\\Projects\\behavioral-psych-eval` | Changed to derive the root from the script location, so a reader can run them. |
| `secrets/totp_key.txt`, `secrets/totp_secret.txt`, `accounts/*.json`, `out/_logindata_copy.db`, `out/drive_links.json`, the `chrome-ud*/` and `brave-ud*/` profiles | Never staged, never pushed. |

## 4. Verification prompts answered by execution, not by assertion

| Question | Answered by |
|---|---|
| Do the builders still work after the root change? | Ran all three from the repository root; each wrote its expected files into `assignments/`. |
| Is anything credential-shaped tracked? | `python tools/check_no_secrets.py` over `git ls-files`. |
| Does the published tree contain a login path? | No `secrets/`, `accounts/`, `out/`, browser profile, or portal client is tracked. |
| Does the documentation match the code? | Every command in `README.md` and `docs/how-to-build.md` was run; the builder arguments were read from the scripts. |
