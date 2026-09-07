"""public only: nothing that maps a private network may be published.

Imported and run by base/scripts/lint.py; findings join its report. The regexes
are defined in base lint so the watcher can reuse them; the *rule* is here
because only this repo is world-readable.
"""
from pathlib import Path
from lint import Problem, PRIVATE_IP_RE, INTERNAL_HOST_RE, ALLOW_MARKER


def check(repo_root: Path, notes: list[Path]) -> list[Problem]:
    problems: list[Problem] = []
    for path in notes:
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if ALLOW_MARKER in line:
                continue
            if PRIVATE_IP_RE.search(line):
                problems.append(Problem(path, lineno, "private IP address in a public repo"))
            if INTERNAL_HOST_RE.search(line):
                problems.append(Problem(path, lineno, "internal hostname in a public repo"))
    return problems
