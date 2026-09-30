#!/usr/bin/env bash
# Single entry point for recording a skill change:
# changelog entry -> commit -> deploy to installed skill directories.
# Usage: bash scripts/save.sh "<area>: <what changed> — <why>" [<path>...]
# Records only CHANGELOG.md plus the named paths. Pre-existing dirty, staged,
# or untracked files are never swept into the commit and are left for the
# caller to handle.
set -euo pipefail
cd "$(dirname "$0")/.."

msg="${1:-}"
if [[ -z "$msg" ]]; then
  echo 'usage: bash scripts/save.sh "<area>: <what changed> — <why>" [<path>...]' >&2
  exit 1
fi
shift || true

# keep the repo-local hook active even after a fresh clone
git config core.hooksPath .githooks

# the save appends to and commits CHANGELOG.md, so it must own the file
# exclusively; pre-existing changelog edits cannot be separated from ours at
# commit granularity
if ! git diff --quiet -- CHANGELOG.md || ! git diff --cached --quiet -- CHANGELOG.md; then
  echo 'CHANGELOG.md already has uncommitted modifications; commit or stash them before recording a change.' >&2
  exit 1
fi

dirty=0
git diff --quiet || dirty=1
git diff --cached --quiet || dirty=1
[[ -n "$(git ls-files --others --exclude-standard)" ]] && dirty=1

if [[ "$dirty" -eq 0 && "$#" -eq 0 ]]; then
  echo "nothing to record; working tree already clean"
  exit 0
fi

if [[ "$#" -eq 0 ]]; then
  echo 'refusing to record unnamed changes: the working tree is dirty and no paths were named.' >&2
  echo 'name the files this change touched: bash scripts/save.sh "<msg>" <path>...' >&2
  exit 1
fi

# A path-level commit cannot distinguish this save's hunks from pre-existing
# staged hunks in the same file. Refuse that ambiguous case rather than
# silently committing the caller's earlier staged work.
if ! git diff --cached --quiet -- "$@"; then
  echo 'one or more named paths already have staged modifications; commit or unstage them before recording a change.' >&2
  exit 1
fi

# Validate every path before changing CHANGELOG.md. The dry run does not alter
# the index, but still catches a missing or invalid pathspec up front.
if ! git add --dry-run -- CHANGELOG.md "$@" >/dev/null; then
  echo 'one or more named paths are invalid; no files were changed.' >&2
  exit 1
fi

if [[ ! -f CHANGELOG.md ]]; then
  printf '# Changelog (oldest first)\n' > CHANGELOG.md
fi
printf '%s — %s\n' "$(date +%F)" "$msg" >> CHANGELOG.md

changelog_committed=0
rollback_changelog() {
  if [[ "$changelog_committed" -eq 0 ]]; then
    git restore --source=HEAD --staged --worktree -- CHANGELOG.md 2>/dev/null || true
  fi
}
trap rollback_changelog EXIT

# stage only what this save records; --only keeps unrelated staged content out
# of the commit even if some exists
git add -- CHANGELOG.md "$@"
if ! git commit -m "$msg" --only -- CHANGELOG.md "$@"; then
  # a hook-rejected commit must not leave the appended changelog line behind;
  # CHANGELOG.md was verified clean above, so this restore removes only our
  # line. The named paths stay staged for a corrected retry.
  echo 'commit rejected; changelog entry rolled back, named edits left staged' >&2
  exit 1
fi
changelog_committed=1

# deploy the committed state (never uncommitted work) to installed copies
for dest in "$HOME/.agents/skills/scientific-manuscript-editor" \
            "$HOME/.codex/skills/scientific-manuscript-editor" \
            "$HOME/.zcode/skills/scientific-manuscript-editor"; do
  if [[ -d "$dest" ]]; then
    rm -rf "$dest"
    mkdir -p "$dest"
    git archive HEAD | tar -x -C "$dest"
    echo "deployed -> $dest"
  fi
done

echo "done: $(git log -1 --oneline)"
