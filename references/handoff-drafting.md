# Handoff drafting

Use when one of three signals is present: the planning context carries
residue (a long conversation, rejected drafts, retrieval output); the task
is genuinely large (multiple sections, submission-stage revision, drafting
a full new section); or the author asks for the brief, the sub-agent, or
the plan checkpoint. The split is never a default for size alone—a clean
context with supplied materials drafts well in one pass, and the handoff
costs two to three passes. For work that stays in one context, the
entrypoint's ordinary depth rules apply unchanged.

## Why split

A long planning context carries residue—rejected drafts, back-and-forth,
retrieval output, process checks—that contaminates generation and pushes
the drafting model to perform task completion rather than write. An
isolated drafting context removes that residue. Isolation does not move
the scientific work: recovery, calibration, and author choices happen in
the planning context. A weak brief in a clean context produces fluent
mediocrity.

## Roles

- **Planner (main context).** Runs the recovery and author-control rules,
  resolves or surfaces the scientific choices, compiles the brief, decides
  what material attaches, and handles returns. Shows the author the brief
  before dispatching by default—the author corrects the plan in seconds,
  before prose exists to defend; an explicit "直接写" or equivalent
  dispatches without the checkpoint. This checkpoint is plan inspection,
  not a material-request round.
- **Writer (isolated context).** Loads this skill and drafts from the
  brief and its attachments only, with no access to the planning
  conversation. Treats the brief as a working basis on the entrypoint's
  terms: execute the scientific relations it intends rather than its
  wording or item order, calibrate its claims, and surface a deviation
  instead of silently obeying or silently dropping it. Marks unsupported
  spans and returns load-bearing gaps instead of filling them.
- **Reviewer (optional, also isolated).** Receives the original task, the
  brief, and the draft—but not the drafting reasoning—and runs the
  integrated checks. Findings return through the planner, who decides what
  is a real defect and revises or redispatches.

## The handoff brief

Compile the brief in this order, compact enough that the writer needs
nothing else:

1. **Task.** What to draft or revise, language, section, requested depth,
   delivery form, and any venue or length constraints.
2. **Argument plan, written as claims.** The sequence of paragraph claims:
   what each paragraph asserts, what it inherits from the previous one,
   and what it hands forward; the unresolved obstacle and the study move.
   Write connected scientific statements, never task items such as
   "mention X here"—the brief's genre becomes the draft's genre.
3. **Locked facts.** Verbatim numbers, units, sample and site identifiers,
   citations with their support status, terminology, and figure or table
   references that the draft must reproduce exactly.
4. **Attachments.** The supplied spans the writer needs and nothing more:
   surrounding approved prose as the style source, the display or data
   content, inspected-source excerpts. Excess attachment defeats the
   isolation.
5. **Boundaries.** What the draft may not do: no facts, claims, or
   citations beyond the brief and attachments; no retrieval unless the
   brief authorizes it, and then under the citation-selection rules;
   unsettled choices marked provisional; calibration in force wherever
   the brief's claims outrun their evidence.
6. **Return channel.** How the writer reports brief defects: missing
   load-bearing material, unreadable attachments, contradictory locked
   facts. The planner fixes the brief or asks the author; the writer never
   resolves a return by inventing.

## When not to split

The default for section work in a clean context is a single pass with the
compact recovered-basis note attached; splitting earns its cost only under
one of the three signals. Sentence-level and single-paragraph work, local
edits, and translation of supplied text never split. When no isolation
mechanism exists, the brief is still the artifact to show the author—it
doubles as the instruction the author can inspect, correct, or forward to
any agent—and the draft then follows it in the same context under the
ordinary rules.

## Completion check

The writer's draft is traceable to the brief's claims and locked facts
with no unmarked invention; every deviation the writer surfaced is
accounted for by the planner; and the author checkpoint, when used,
happened at the brief, before prose existed to defend.
