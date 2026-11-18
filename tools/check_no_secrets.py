#!/usr/bin/env python
"""Fail if anything credential-shaped is tracked in this repository.

Read-only. It looks at what git is tracking, not at the working tree, so an
untracked secret on disk is not a failure (that is what .gitignore is for) and
a tracked secret is always a failure.

    python tools/check_no_secrets.py [--staged]

Exit codes:
    0  nothing credential-shaped is tracked
    1  something is: the paths and lines are printed
    2  the check could not run (not a git repository, git missing)
"""
import argparse
import os
import re
import subprocess
import sys

# Tracked paths that must never exist in the published tree.
BANNED_PATH_PARTS = (
    "secrets/",
    "accounts/",
    "out/",
    "chrome-ud",
    "brave-ud",
    "work/keys",
    "work/tmp_dump",
    "work/ws_answers",
    "work/unit1",
    "work/unit2",
    "work/unit3",
    "work/unit4",
    "work/unit5",
    "source/",
)

BANNED_SUFFIXES = (".db", ".env", ".wa_sid", ".cookie", ".cookies")

# Credential shapes. Each pattern is (label, compiled regex).
PATTERNS = [
    ("totp setup key", re.compile(r"\btotp[_-]?(?:key|secret)\b\s*[:=]", re.I)),
    ("google authenticator seed", re.compile(r"\b4[A-Z2-7]{16}\b")),
    ("bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}")),
    ("aws access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("github token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}")),
    ("password assignment", re.compile(r"password\s*[:=]\s*[\"']?[^\s\"']{4,}", re.I)),
    ("session cookie", re.compile(r"(?:JSESSIONID|sessionid|_session)\s*[:=]", re.I)),
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]

# Lines that legitimately mention these words without holding a secret.
ALLOW_MARKERS = (
    "check_no_secrets",
    "docs/privacy.md",
)


def git(*args, cwd=None):
    try:
        out = subprocess.run(
            ["git", *args], cwd=cwd, capture_output=True, text=True, check=True
        )
    except FileNotFoundError:
        print("git is not on the path", file=sys.stderr)
        raise SystemExit(2)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.strip(), file=sys.stderr)
        raise SystemExit(2)
    return out.stdout


def tracked_files(root, staged):
    args = ["diff", "--cached", "--name-only"] if staged else ["ls-files"]
    names = [n.strip() for n in git(*args, cwd=root).splitlines() if n.strip()]
    return names


def scan(root, names):
    problems = []
    for name in names:
        norm = name.replace("\\", "/")
        low = norm.lower()
        for part in BANNED_PATH_PARTS:
            if low.startswith(part) or ("/" + part) in low:
                problems.append((norm, 0, "banned path"))
                break
        if low.endswith(BANNED_SUFFIXES):
            problems.append((norm, 0, "banned file type"))
        full = os.path.join(root, norm)
        if not os.path.isfile(full):
            continue
        if os.path.getsize(full) > 4 * 1024 * 1024:
            continue
        try:
            text = open(full, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        if any(m in norm for m in ALLOW_MARKERS):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for label, rx in PATTERNS:
                if rx.search(line):
                    problems.append((norm, lineno, label))
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--staged", action="store_true", help="check the index only")
    ap.add_argument("--root", default=None, help="repository root")
    args = ap.parse_args()

    root = args.root or os.getcwd()
    try:
        names = tracked_files(root, args.staged)
    except SystemExit:
        raise

    if not names:
        print("nothing tracked yet - nothing to check")
        return 0

    problems = scan(root, names)
    if problems:
        print("credential-shaped content is tracked:\n")
        for path, lineno, label in problems:
            where = path if lineno == 0 else f"{path}:{lineno}"
            print(f"  {where}  [{label}]")
        print(f"\n{len(problems)} problem(s). Remove them before pushing.")
        return 1

    print(f"clean: {len(names)} tracked file(s), nothing credential-shaped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
