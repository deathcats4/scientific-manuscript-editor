#!/usr/bin/env bash
# Single entry point for recording a skill change:
# changelog entry -> commit -> deploy to installed skill directories.
# Usage: bash scripts/save.sh "naturalness: what changed — why"
set -euo pipefail
cd "$(dirname "$0")/.."

msg="${1:-}"
if [[ -z "$msg" ]]; then
  echo 'usage: bash scripts/save.sh "<area>: <what changed> — <why>"' >&2
  exit 1
fi

# keep the repo-local hook active even after a fresh clone
git config core.hooksPath .githooks

dirty=0
git diff --quiet || dirty=1
git diff --cached --quiet || dirty=1
[[ -n "$(git ls-files --others --exclude-standard)" ]] && dirty=1

if [[ "$dirty" -eq 0 ]]; then
  echo "nothing to record; working tree already clean"
  exit 0
fi

if [[ ! -f CHANGELOG.md ]]; then
  printf '# Changelog (oldest first)\n' > CHANGELOG.md
fi
printf '%s — %s\n' "$(date +%F)" "$msg" >> CHANGELOG.md

git add -A
git commit -m "$msg"

# deploy the committed state (never uncommitted work) to installed copies
for dest in "$HOME/.agents/skills/scientific-manuscript-editor" \
            "$HOME/.codex/skills/scientific-manuscript-editor" \
            "$HOME/.zcode/skills/scientific-manuscript-editor"; do
  if [[ "$(basename "$dest")" == "scientific-manuscript-editor" && -d "$dest" ]]; then
    rm -rf "$dest"
    mkdir -p "$dest"
    git archive HEAD | tar -x -C "$dest"
    echo "deployed -> $dest"
  fi
done

echo "done: $(git log -1 --oneline)"
