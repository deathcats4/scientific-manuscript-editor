# Changelog

Notable user-facing changes, newest first. Entries summarize what a skill user
would notice; full scope, behavior detail, and reasoning live in the commit
log.

## Unreleased

- 2026-10-05 — Added a manuscript-specific cross-session handoff with explicit evidence, decision, and context-to-prose boundaries.
- 2026-10-03 — Introduction now maps common scientific problems to candidate movements before drafting while keeping the structure flexible.
- 2026-10-02 — Added a linked evidence-gate, scientific-fidelity, and argument-and-genre review mode for higher-risk manuscript work.
- 2026-10-02 — Added a lightweight project-local MANUSCRIPT-CONTEXT.md for multi-section and cross-session work.

## 1.9.0 — 2026-09-30

- Routing narrowed to run directly when the task is clear; when the user is unsure how to frame a request, the skill proposes relevant routes with what each delivers and a copyable next request.
- README rewritten as a concise user guide synced with current routing and review behavior.

## 1.8.0 — 2026-09-30

- Conditional author-intent routing with Grill-style clarification: when a request is ambiguous between manuscript tasks, the skill asks one focused question or presents route choices instead of guessing, while direct local edits still run without any interview. Adds `references/author-intent-interview.md`.

## 1.7.0 — 2026-09-30

- Translation split rule scaled by scope: sentence, paragraph, and local translation stay single-context; multi-section or full-manuscript translation may draft unsplit but must pass continuity checks (terminology and modality, Title–Abstract–Conclusion agreement, cross-references) before delivery. Author-requested passage-by-passage confirmation runs as progressive review.

## 1.6.8 — 2026-09-30

- Consolidating repeated statements now ranks instances by the author's latest accepted position and evidence before specificity, so the most concrete wording of a superseded claim is retired instead of surviving; unrankable pairs keep both instances and report the conflict.

## 1.6.7 — 2026-09-30

- After a deletion or merge, apparatus dependencies are checked: figure, table, equation, and supplement references still resolve; the deleted span was not the only introduction of a display or supplement; demonstratives keep recoverable antecedents; citation keys, reference list, labels, and captions still agree.

## 1.6.6 — 2026-09-30

- Authorized citation retrieval searches contrary evidence (negative results, alternative mechanisms, applicability boundaries) and reports an explicit not-found; sources pass status checks (retraction, correction, preprint versus published, duplicates) and comparability before supporting a claim.

## 1.6.5 — 2026-09-30

- Planner–writer–reviewer handoffs: the reviewer is a required step receiving the writer's evidence package; the brief checkpoint pauses only on author request, unresolved scientific choices, or unsafe briefs; any post-review modification reruns the proportional final check.
- Handoff briefs require evidence closure: each paragraph claim lists its facts, displays, conditions, and citations; an unprovided dependency is a stop condition returned as a gap.

## 1.6.4 — 2026-09-29

- Revision-artifact checks hardened: consolidation leaves the surviving instance self-contained; the post-deletion reread covers dangling demonstratives, stranded connectives, and reference-list consequences; revisions are compared against the original so no new uniformity is installed. The AI-style catalogue adds vague collective attribution and narrative overreach.

## 1.6.3 — 2026-09-29

- The deletion gate runs at paragraph and manuscript level: a paragraph-scope edit may not cut a manuscript-level link (gap answered later, boundary relied on later, term defined once, first mention) without reading the far end and surfacing the removal.

## 1.6.2 — 2026-09-29

- Recurring patterns are resolved at the function level: the most specific same-function instance survives, each deleted span's function must survive somewhere in scope, and the manuscript's specific gap sentence is protected during AI-style revision.

## 1.6.1 — 2026-09-29

- Handoff splitting tightened to three signals (residue in the planning context, genuinely large task, author request); clean-context section work defaults to one pass; sentence and single-paragraph work never splits.

## 1.6.0 — 2026-09-29

- Planner–writer–reviewer handoff drafting for section-scale and larger tasks: the brief carries a claim-chain argument plan, verbatim locked facts, boundaries, and a return channel, with an author checkpoint at the brief. Local edits stay single-context. Adds `references/handoff-drafting.md`.

## 1.5.0 — 2026-09-29

- Recovery-first defaults extended to Methods, Results, and Discussion: each section reconstructs its basis from supplied materials before asking, and author outlines are executed as working bases by their scientific relations, not item-by-item.

## 1.4.0 — 2026-09-29

- Writing requests recover the author's argument basis from supplied materials before asking questions and draft directly when the basis suffices; authorized citation selection covers foundational, recent, and directly relevant sources with per-sentence verification, and prominence alone is never a citation reason.

## 1.3.0 — 2026-09-29

- Introductions keep their throughlines implicit and content-bearing: checklist-style purpose announcements are prevented while necessary scientific handoffs survive.

## 1.2.0 — 2026-09-29

- Figure and table caption rules for Results: captions work as instruction sheets for displays (descriptive title, per-panel and quantitative definitions, no findings narration), countering AI mini-essay captions.

## 1.1.0 — 2026-09-23

- Material sufficiency gate: substantive writing stops on load-bearing evidence deficits (uninspected literature, memory citations, unsupplied figures, tables, or data) and requests material or a marked provisional draft instead of substituting fluent prose.
- Format-carrier preservation: LaTeX, Word, and Markdown markup, citation commands, tracked changes, and author comments stay intact through prose edits; conversion and cleanup run only when requested.
- ZCode installation documented.

## 1.0.0 — 2026-09-22

- Initial integrated skill: combined naturalness and protection review with the style-source contract, shipping `SKILL.md`, `README.md`, and the first reference set.
