#!/usr/bin/env bash
# Single entry point for recording a skill change:
# optional user-facing changelog note -> commit -> deploy to installed skill
# directories.
# Usage: bash scripts/save.sh "<area>: <what changed> — <why>" [--note "<short user-facing line>"] [<path>...]
# Records only the named paths, plus CHANGELOG.md when --note is given.
# Pre-existing dirty, staged, or untracked files are never swept into the
# commit and are left for the caller to handle.
set -euo pipefail
cd "$(dirname "$0")/.."

msg="${1:-}"
if [[ -z "$msg" ]]; then
  echo 'usage: bash scripts/save.sh "<area>: <what changed> — <why>" [--note "<short user-facing line>"] [<path>...]' >&2
  exit 1
fi
shift || true

note=""
paths=()
while [[ $# -gt 0 ]]; do
  if [[ "$1" == "--note" ]]; then
    if [[ -z "${2:-}" ]]; then
      echo '--note requires a value' >&2
      exit 1
    fi
    note="$2"
    shift 2
  else
    paths+=("$1")
    shift
  fi
done

# keep the repo-local hook active even after a fresh clone
git config core.hooksPath .githooks

# when a note is recorded the save edits and commits CHANGELOG.md, so it must
# own the file exclusively; pre-existing changelog edits cannot be separated
# from ours at commit granularity (a version-release rename of the Unreleased
# heading goes in its own save, naming CHANGELOG.md without --note)
if [[ -n "$note" ]]; then
  if ! git diff --quiet -- CHANGELOG.md || ! git diff --cached --quiet -- CHANGELOG.md; then
    echo 'CHANGELOG.md already has uncommitted modifications; commit or stash them before recording a note.' >&2
    exit 1
  fi
fi

dirty=0
git diff --quiet || dirty=1
git diff --cached --quiet || dirty=1
[[ -n "$(git ls-files --others --exclude-standard)" ]] && dirty=1

if [[ "$dirty" -eq 0 && ${#paths[@]} -eq 0 && -z "$note" ]]; then
  echo "nothing to record; working tree already clean"
  exit 0
fi

if [[ ${#paths[@]} -eq 0 && "$dirty" -eq 1 ]]; then
  echo 'refusing to record unnamed changes: the working tree is dirty and no paths were named.' >&2
  echo 'name the files this change touched: bash scripts/save.sh "<msg>" [--note "<line>"] <path>...' >&2
  exit 1
fi

targets=()
if [[ ${#paths[@]} -gt 0 ]]; then
  targets+=("${paths[@]}")
fi
if [[ -n "$note" ]]; then
  targets+=(CHANGELOG.md)
fi

# A path-level commit cannot distinguish this save's hunks from pre-existing
# staged hunks in the same file. Refuse that ambiguous case rather than
# silently committing the caller's earlier staged work.
if ! git diff --cached --quiet -- "${targets[@]}"; then
  echo 'one or more named paths already have staged modifications; commit or unstage them before recording a change.' >&2
  exit 1
fi

# Validate every path before touching CHANGELOG.md. The dry run does not alter
# the index, but still catches a missing or invalid pathspec up front.
if ! git add --dry-run -- "${targets[@]}" >/dev/null; then
  echo 'one or more named paths are invalid; no files were changed.' >&2
  exit 1
fi

changelog_touched=0
rollback_changelog() {
  if [[ "$changelog_touched" -eq 1 ]]; then
    git restore --source=HEAD --staged --worktree -- CHANGELOG.md 2>/dev/null || true
  fi
}
trap rollback_changelog EXIT

if [[ -n "$note" ]]; then
  if [[ ! -f CHANGELOG.md ]]; then
    printf '# Changelog\n' > CHANGELOG.md
  fi
  entry="- $(date +%F) — $note"
  if grep -q '^## Unreleased$' CHANGELOG.md; then
    # newest first: the entry goes directly under the Unreleased heading; the
    # blank line that followed the heading is swallowed
    awk -v ins="$entry" '
      /^## Unreleased$/ && !done {
        print; print ""; print ins; done = 1; skip = 1; next
      }
      skip && /^$/ { skip = 0; next }
      { print }
    ' CHANGELOG.md > CHANGELOG.md.new && mv CHANGELOG.md.new CHANGELOG.md
  elif grep -q '^## ' CHANGELOG.md; then
    # no Unreleased section yet: create one above the newest version heading
    awk -v ins="$entry" '
      !done && /^## / { print "## Unreleased"; print ""; print ins; print ""; done = 1 }
      { print }
    ' CHANGELOG.md > CHANGELOG.md.new && mv CHANGELOG.md.new CHANGELOG.md
  else
    printf '\n## Unreleased\n\n%s\n' "$entry" >> CHANGELOG.md
  fi
  changelog_touched=1
fi

# stage only what this save records; --only keeps unrelated staged content out
# of the commit even if some exists
git add -- "${targets[@]}"
if ! git commit -m "$msg" --only -- "${targets[@]}"; then
  # a hook-rejected commit must not leave the changelog note behind; when a
  # note was recorded CHANGELOG.md was verified clean above, so this restore
  # removes only our entry. The named paths stay staged for a corrected retry.
  echo 'commit rejected; changelog note rolled back, named edits left staged' >&2
  exit 1
fi
changelog_touched=0

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
