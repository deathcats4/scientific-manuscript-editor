# Agent protocol for this repository

This repo is the single source of truth for the `scientific-manuscript-editor`
skill. Installed copies under `~/.agents/skills/`, `~/.codex/skills/`, and
`~/.zcode/skills/` are deploy targets managed by `scripts/save.sh`; never edit
an installed copy directly — edit here, then deploy.

## Mandatory after any content edit

After editing SKILL.md, README.md, CHANGELOG.md, anything under `references/`
or `agents/`, run in the same task:

    bash scripts/save.sh "<area>: <what changed> — <why>"

Works from any shell that has git's `bash` on PATH. The script appends a dated
CHANGELOG entry, commits everything, and redeploys the committed state to the
installed skill directories. Do not leave this repo dirty at the end of a task.

If the working tree is already dirty when a session starts, report that to the
user before making further edits.

## Commit message convention

Format: `<area>: <what> — <why>`. Areas: `skill`, `readme`, `reasoning`,
`naturalness`, `protection`, `style-source`, `integrity`, `section-refs`,
`synthesis`, `continuity`, `meta`. Generic messages (`update`, `fix`, `修改`,
`更新`, `wip`) are rejected by the `.githooks/commit-msg` hook.

When a change alters skill behavior rather than wording only, the commit and
CHANGELOG entry must state the scope, the behavior change, and the reason.
