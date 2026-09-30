# Agent protocol for this repository

This repo is the single source of truth for the `scientific-manuscript-editor`
skill. Installed copies under `~/.agents/skills/`, `~/.codex/skills/`, and
`~/.zcode/skills/` are deploy targets managed by `scripts/save.sh`; never edit
an installed copy directly — edit here, then deploy.

## Mandatory after any content edit

After editing SKILL.md, README.md, CHANGELOG.md, anything under `references/`,
`agents/`, or `scripts/`, run in the same task, naming every file the change
touched:

    bash scripts/save.sh "<area>: <what changed> — <why>" <changed-file>...

Works from any shell that has git's `bash` on PATH. The script commits only
the named files; pre-existing dirty, staged, or untracked files are left
untouched and stay visible in `git status` for the caller to handle. It then
redeploys the committed state to the installed skill directories. Do not leave
this repo dirty at the end of a task.

CHANGELOG.md is a newest-first, version-grouped summary of user-facing
changes; full detail stays in the commit log. A save reaches the changelog
only when the change alters behavior a skill user would notice:

    bash scripts/save.sh "<area>: <what changed> — <why>" --note "<one-line user-facing summary>" <changed-file>...

The note lands under `## Unreleased`. When SKILL.md's version stamp changes,
rename `## Unreleased` to `## <version> — <date>` in its own save naming
CHANGELOG.md (and SKILL.md if the stamp edit is not yet committed), without
`--note`. Housekeeping changes (save.sh, hooks, wording-only fixes) get no
changelog note.

If the working tree is already dirty when a session starts, report that to the
user before making further edits.

## Commit message convention

Format: `<area>: <what> — <why>`. Areas: `skill`, `readme`, `reasoning`,
`naturalness`, `protection`, `style-source`, `integrity`, `section-refs`,
`synthesis`, `continuity`, `meta`. Generic messages (`update`, `fix`, `修改`,
`更新`, `wip`) are rejected by the `.githooks/commit-msg` hook.

When a change alters skill behavior rather than wording only, the commit and
CHANGELOG entry must state the scope, the behavior change, and the reason.
