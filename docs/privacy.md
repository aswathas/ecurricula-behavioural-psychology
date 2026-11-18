# What is deliberately not here

This repository is public. Everything in it can be read by anyone. The rule
applied while preparing it: **the published tree must contain no way to log in
to anything, and no artefact that carries a live session.**

## Excluded, and why

| Excluded | What it is | Why |
|---|---|---|
| `secrets/` | The SRM account credentials, the Google Authenticator setup key (`totp_key.txt`, `totp_secret.txt`), the recovery code | A credential. Publishing it hands over the account. |
| `accounts/*.json` | The same credentials in JSON form, including the session cookies | Same. |
| `2fa_code.txt`, `totp_*.txt`, `recovery_code.txt` | Generated one-time codes | Short-lived secrets; still secrets. |
| `chrome-ud*/`, `brave-ud*/`, `Default/`, `Local State` | Copied browser profiles | They carry live Google and SRM session cookies. A profile is a session. |
| `out/` | API responses (`api_login_POST.json`, `api_filetoken.json`, session dumps), screenshots, cookies (`_logindata_copy.db`), submission logs, `drive_links.json` | Portal traffic. It contains session material and is not the author's work. |
| `scripts/` — the portal clients | `account.py`, `portal.py`, `ecapi.py`, `browser*.py`, `login_browser.py`, `otp_use.py`, `totp.py`, `session_watch.py` | The login, the OTP and the session plumbing. Publishing them publishes a working path into the account. |
| `scripts/` — the submission scripts | `submit_mcq.py`, `submit_practice.py`, `upload_drive*.py`, `fetch_*.py`, `harvest_files.py`, `ws_fill.py`, `ws_slots.py` | They log in, submit or upload. Same reason. |
| `scripts/` — the portal-key tooling | `consolidate_key.py`, `build_unit3_keys.py`, `build_unit3_overlay.py`, `verify_unit3_keys.py` | They read or write the portal key, which is account-bound. |
| `work/unit*/`, `work/keys/`, `work/new/`, `work/tmp_dump/`, `work/ws_answers/` | Session briefs, the portal key, the worksheet bodies | Fetched from the portal. The university's course material. |
| `source/assignments_1-3.pdf` | The question paper | The university's document, not the author's. |
| `work/.wa_sid`, `work/wacall.sh` | A session id and a shell helper | Session material. |

## What is published, and checked

`tools/check_no_secrets.py` runs over the tracked files before every push. It
fails the build when it finds:

- a tracked path under `secrets/`, `accounts/`, `out/`, or a browser-profile
  directory;
- a credential-shaped string: an SRM login, a `totp` setup key, a Google
  authenticator seed, a bearer token, a session cookie, a password
  assignment;
- a `.wa_sid`, a `.db`, a cookie jar or a `.env`.

Run it directly:

```bash
python tools/check_no_secrets.py
```

It exits non-zero and prints the offending path and line. It is also the last
step of the push sequence in `docs/reviews/delivery-plan.md`.

## The residual risk, stated plainly

The repository still contains the author's **name, registration number and
course**, and the full text of the assignment answers. That is deliberate: it
is the work being published. If a copy of this repository is ever made
without those, the point of the repository is gone.

What the repository does **not** contain is any ability to act on the
university's behalf. Anyone can read the answers. Nobody but the account
holder can submit them.
