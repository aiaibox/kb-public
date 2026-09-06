#!/usr/bin/env python3
"""Import a folder of distilled Markdown notes into a vault repo.

    scripts/import-distilled.py <source-dir> --into <subfolder> [--repo NAME]
                                [--source TAG] [--dry-run]

Written for bulk imports of AI chat history that has already been distilled into
topic notes. It rewrites frontmatter to the vault schema — assigning a fresh
ULID, forcing `repo:` to match the destination, and normalising `tags:` — while
preserving every original field so nothing from the import is lost.

Existing files are never overwritten. Run lint afterwards.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import time
from pathlib import Path

A32 = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
PRESERVE = ["kb", "version", "type", "topic", "subtopics", "sensitivity",
            "importance", "time_sensitivity", "source_conversations", "format",
            "turns", "permalink"]
DROP_TAGS = {"meta"}


def ulid() -> str:
    n = (int(time.time() * 1000) << 80) | int.from_bytes(os.urandom(10), "big")
    return "".join(A32[(n >> s) & 31] for s in range(125, -1, -5))


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    try:
        end = text.index("\n---", 3)
    except ValueError:
        return {}, text
    fields: dict[str, str] = {}
    key = None
    for line in text[3:end].strip().split("\n"):
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            fields[key] = m.group(2).strip()
        elif line.strip().startswith("- ") and key:
            fields[key] = (fields[key] + "," if fields[key] else "") + line.strip()[2:]
    return fields, text[end + 4:].lstrip("\n")


def normalise_tags(raw: str | None, topic: str | None, fallback: str) -> list[str]:
    tags: list[str] = []
    if raw:
        for t in raw.strip().strip("[]").split(","):
            t = t.strip().strip("\"'").lower().replace(" ", "-")
            if t and t not in DROP_TAGS:
                tags.append(t)
    if not tags and topic:
        tags = [topic.strip().lower().replace(" ", "-").replace("_", "-")]
    return (tags or [fallback])[:5]


def slugify(stem: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="directory of .md files to import")
    ap.add_argument("--into", required=True, help="destination subfolder, e.g. reference")
    ap.add_argument("--repo", help="repo root (default: the repo this script lives in)")
    ap.add_argument("--source-tag", default=None,
                    help="value for the 'source:' field (default: source dir name)")
    ap.add_argument("--strip-prefix", action="store_true",
                    help="drop a leading NN- or NN_ from filenames")
    ap.add_argument("--numeric-names", action="store_true",
                    help="name files 01.md, 02.md ... instead of using the title. "
                         "Required for repos where filenames must not describe "
                         "content, because git-crypt encrypts contents but not names.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    repo_root = Path(args.repo).resolve() if args.repo else Path(__file__).resolve().parent.parent
    repo_name = repo_root.name
    dest = repo_root / args.into
    today = dt.date.today().isoformat()
    source_tag = args.source_tag or args.source.name

    files = sorted(args.source.glob("*.md"))
    if not files:
        print(f"no .md files in {args.source}", file=sys.stderr)
        return 1

    if not args.dry_run:
        dest.mkdir(parents=True, exist_ok=True)

    written = skipped = 0
    if args.numeric_names:
        existing = len(list(dest.glob("[0-9][0-9].md"))) if dest.exists() else 0
    for index, f in enumerate(files, start=1):
        fields, body = split_frontmatter(f.read_text(encoding="utf-8"))
        heading = re.search(r"^# (.+)$", body, re.M)
        title = (heading.group(1) if heading else fields.get("title", f.stem)).strip()
        title = title.strip('"')

        if args.numeric_names:
            target = dest / f"{existing + index:02d}.md"
        else:
            stem = f.stem
            if args.strip_prefix:
                stem = re.sub(r"^\d+[-_]", "", stem)
            target = dest / f"{slugify(stem)}.md"

        if target.exists():
            print(f"  skip (exists): {target.relative_to(repo_root)}")
            skipped += 1
            continue

        tags = normalise_tags(fields.get("tags"), fields.get("topic"), f"{source_tag}-import")
        out = ["---", f"id: {ulid()}", f'title: "{title}"', f"repo: {repo_name}",
               f"tags: [{', '.join(tags)}]", f"created: {today}", f"updated: {today}",
               f"source: {source_tag}"]
        out += [f"{k}: {fields[k]}" for k in PRESERVE if fields.get(k)]
        out.append("---")
        content = "\n".join(out) + "\n\n" + body.strip() + "\n"

        if args.dry_run:
            print(f"  [dry-run] {f.name} -> {target.relative_to(repo_root)} tags={tags}")
        else:
            target.write_text(content, encoding="utf-8")
            print(f"  {f.name} -> {target.relative_to(repo_root)}")
            time.sleep(0.002)   # keep ULIDs monotonic
        written += 1

    print(f"\n{written} imported, {skipped} skipped -> {repo_name}/{args.into}")
    if not args.dry_run:
        print(f"Now run: cd {repo_root} && python3 scripts/lint.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
