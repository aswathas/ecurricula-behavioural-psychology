# Delivery plan — public publication of the behavioural coursework repository

One unit, one commit, one push. The gates are commands, not intentions.

The repository does not exist yet, so this is its initial commit and it lands on
`main` directly — there is no default branch to protect and no prior history to
rewrite. Every later change goes through a branch and a pull request.

## Unit

**Publish the public half of the behavioural-psychology repository.** The public
half is the finished documents, the structured question and figure data, the six
document builders, the documentation and the pre-push check. The private half
stays on this machine: credentials, browser profiles, portal traffic, the portal
client and every script that logs in, submits or uploads.

## Repository

- Name: `ecurricula-behavioural-psychology`
- Owner: `aswathas`
- Visibility: public
- Licence: MIT, with the course material excluded

## Steps and gates

| # | Step | Command | Gate |
|---|---|---|---|
| 1 | The builders work from the repository root | `python scripts/build_assignment_fill.py && python scripts/build_assignment_pdf.py && python scripts/build_assignment_sheet.py` | Each prints the files it wrote |
| 2 | The tree is classified | read `.gitignore` against the filesystem | Every private directory is ignored; the six builders are allowlisted |
| 3 | Nothing private is staged | `git add -A && git status --short` | Only the allowlist, `assignments/`, `work/`'s three data files, `docs/`, `tools/`, `README.md`, `LICENSE` |
| 4 | No credential-shaped content is tracked | `python tools/check_no_secrets.py` | Exit 0, "clean: N tracked file(s)" |
| 5 | The tracked tree holds no login path | `git ls-files` | No `secrets/`, `accounts/`, `out/`, `chrome-ud`, `brave-ud`, `work/keys`, `source/` |
| 6 | The remote exists and is public | `gh repo view aswathas/ecurricula-behavioural-psychology` | Public, empty or matching |
| 7 | The push lands | `git push -u origin main` | Remote branch equals local HEAD |
| 8 | The published tree is what was reviewed | `gh api repos/aswathas/ecurricula-behavioural-psychology/git/trees/HEAD?recursive=1` | The tree listing matches step 3 |

## Rollback

The private material was never committed, so there is nothing to roll back in
git. If the remote turns out to hold something that should not be there, the
fix is: `gh repo delete` (public, no history to preserve), correct the
`.gitignore` locally, re-run gates 3-5, and push again.

## Not in this unit

- The portal automation, in any form.
- The course material (question paper, session briefs, worksheet templates).
- The private machine-only repository contents.
