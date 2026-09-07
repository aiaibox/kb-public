#!/usr/bin/env python3
"""public: nothing that maps a private network may be published.

Runs kb-base's rules first, then this repo's own in `check()`. The repo is the git
work tree this is run in. base/scripts must be first on sys.path BEFORE the import,
or `import lint` would find this file and load it as a module of itself.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "base" / "scripts"))
import lint  # noqa: E402
from lint import Problem, PRIVATE_IP_RE, INTERNAL_HOST_RE, ALLOW_MARKER  # noqa: E402


def check(repo_root: Path, notes: list) -> list:
    """The regexes live in base so the watcher can reuse them; the RULE is here,
    because only this repo is world-readable."""
    problems = []
    for path in notes:
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if ALLOW_MARKER in line:
                continue
            if PRIVATE_IP_RE.search(line):
                problems.append(Problem(path, lineno, "private IP address in a public repo"))
            if INTERNAL_HOST_RE.search(line):
                problems.append(Problem(path, lineno, "internal hostname in a public repo"))
    return problems


if __name__ == "__main__":
    sys.exit(lint.main(local=check))
