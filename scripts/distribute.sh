#!/usr/bin/env bash
# Copy shared machinery from its canonical location into every repo.
#
#   personal/scripts/distribute.sh [--check]
#
# Several files are deliberately identical in all four repos: the linter, the
# note creator, the pre-commit hook, the dotfiles, the templates, and RULES.md.
# Each derives its per-repo behaviour from its own directory name, so the files
# themselves never differ. Editing a copy in place causes silent drift, which is
# exactly what this script exists to prevent.
#
# Canonical sources:
#   personal/scripts/lint.py, newnote.sh, import-distilled.py, distribute.sh
#   personal/.githooks/pre-commit, .gitignore, .gitattributes, .editorconfig
#   personal/_templates/
#   public/RULES.md, public/WORKING-RULES.md
#
# --check reports drift without writing anything; exit 1 if any is found.
set -uo pipefail

KB="${KB:-$HOME/kb}"
SRC="$KB/personal"
CANON_RULES="$KB/public/RULES.md"
CANON_WORKING="$KB/public/WORKING-RULES.md"
REPOS=("$KB/public" "$KB/personal" "$KB/business" "$KB/private")
CHECK=0
[ "${1:-}" = "--check" ] && CHECK=1

FILES=(
  "scripts/lint.py"
  "scripts/newnote.sh"
  "scripts/import-distilled.py"
  "scripts/distribute.sh"
  ".githooks/pre-commit"
  ".gitignore"
  ".gitattributes"
  ".editorconfig"
)
EXEC=("scripts/lint.py" "scripts/newnote.sh" "scripts/import-distilled.py"
      "scripts/distribute.sh" ".githooks/pre-commit")

drift=0

sync_one() {  # $1 = source file, $2 = destination file, $3 = label
  if cmp -s "$1" "$2" 2>/dev/null; then return 0; fi
  drift=$((drift + 1))
  if [ "$CHECK" = 1 ]; then
    echo "  DRIFT: $3"
  else
    mkdir -p "$(dirname "$2")"
    command cp -f "$1" "$2"
    echo "  updated: $3"
  fi
}

for repo in "${REPOS[@]}"; do
  [ -d "$repo/.git" ] || continue
  name=$(basename "$repo")

  for f in "${FILES[@]}"; do
    # .gitattributes in private/ carries the git-crypt rules and is NOT shared.
    if [ "$name" = "private" ] && [ "$f" = ".gitattributes" ]; then continue; fi
    [ "$repo" = "$SRC" ] && continue
    sync_one "$SRC/$f" "$repo/$f" "$name/$f"
  done

  [ "$repo" = "$SRC" ] || sync_one "$CANON_RULES" "$repo/RULES.md" "$name/RULES.md"
  [ "$repo" = "$SRC" ] || sync_one "$CANON_WORKING" "$repo/WORKING-RULES.md" "$name/WORKING-RULES.md"

  if [ "$repo" != "$SRC" ] && [ "$CHECK" = 0 ]; then
    for t in "$SRC"/_templates/*.md; do
      command cp -f "$t" "$repo/_templates/$(basename "$t")"
    done
    for e in "${EXEC[@]}"; do [ -f "$repo/$e" ] && chmod +x "$repo/$e"; done
  fi
done

# personal gets RULES.md from public too.
sync_one "$CANON_RULES" "$SRC/RULES.md" "personal/RULES.md"
sync_one "$CANON_WORKING" "$SRC/WORKING-RULES.md" "personal/WORKING-RULES.md"

if [ "$CHECK" = 1 ]; then
  [ "$drift" -eq 0 ] && { echo "  no drift"; exit 0; }
  echo "  $drift file(s) differ — run without --check to fix"; exit 1
fi
echo "  done ($drift file(s) changed)"
