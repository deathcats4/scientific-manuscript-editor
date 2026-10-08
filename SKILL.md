---
name: scientific-manuscript-editor
description: >-
  Draft, revise, polish, translate, or review scientific manuscript prose in
  Chinese or English. Use for manuscript passages and sections, titles,
  abstracts, conclusions, evidence-to-claim reasoning, citation fit,
  reference-informed writing, academic naturalness and AI-style review, and
  cross-manuscript consistency.
metadata:
  short-description: "Author-controlled scientific manuscript editing"
  version: "1.9.0"
---

# Scientific Manuscript Editor

Turn the author's current scientific understanding into manuscript-ready prose.
Scientific truth and author decisions are boundaries; inside them, choose the
language, reasoning, and organization that make the science clear and natural.
Infer terminology and conventions from the supplied manuscript and discipline.
Keep the working model internal; deliver the prose, findings, and decisions the
author requested.

Let the scientific content, intended reader, and explicit author or venue
requirements determine openings, order, paragraph boundaries, and endings.
Structures and checklists in this skill are diagnostic tools, not prose slots.
A sound passage need not be reorganized to match them. Assess supported claims,
necessary reasoning, coherence, and readability without prescribing a sentence
position, paragraph count, or repeated rhetorical move. Honor an author-requested
structure or a journal's required format within the scientific boundaries.

## Recover the basis and choose the depth

Read the supplied manuscript, relevant figures, methods, notes, and inspected
sources before asking the author to restate them. Recover the operation, scope,
current scientific position, evidence basis, and delivery form. When these are
clear, proceed directly. Execute an outline's intended scientific relations
rather than mechanically reproducing its wording or item order; surface a
substantive deviation.

Use the lightest depth that can complete the request faithfully:

| Depth | Use and action |
|---|---|
| Local edit | Preserve the scientific proposition, evidence relationship, and sound architecture. Edit a sentence or passage directly for language, terminology, translation, or references. Expand inspection only for a concrete conflict or dependency. |
| Substantive revision | Draft or repair reasoning, interpretation, evidence relationships, or structure at any length. Load manuscript reasoning and the section reference actually in scope. |
| Manuscript-wide synthesis | Coordinate sections, prepare a submission, or reconcile Title–Abstract–Conclusion. Load continuity and the relevant synthesis guidance. |

A short passage can need substantive revision; its length does not authorize
changes outside the requested scope. Preserve effective wording and repair to
the extent the actual problem requires. An isolated grammar or terminology
correction does not trigger a manuscript-wide or full AI-pattern review.

For paragraph and section work, establish what the reader should understand,
which evidence supports it, which non-obvious inference must be recoverable,
and how the relevant parts relate. Progression, parallel comparisons, shared
context, and synthesis can each provide coherence; every paragraph need not
inherit from its immediate predecessor or prepare a successor. Necessary
inference belongs in the prose. Keep planning notes and editing history outside
the manuscript, and use orientation or synthesis when it helps the reader.
Judge a unit by its scientific function rather than a prescribed opening,
internal sequence, or closing form. The detailed procedure and examples live
in [manuscript-reasoning.md](references/manuscript-reasoning.md).

## Clarify only a consequential unresolved choice

After recovery, ask only when an unresolved operation, scope, scientific
position, source authorization, or delivery choice would change the result.
Read [author-intent-interview.md](references/author-intent-interview.md) then.
Bundle independent open choices; defer questions that depend on an unanswered
choice. Recommend an option when evidence supports it. Ordinary editorial
choices proceed directly.

When the user asks what the skill can do or cannot frame a deliverable, offer up
to three relevant routes, their outputs, and one copyable next request. If the
task already clearly implies a route, state it briefly and proceed; omit the
route note for manuscript-only output and bounded local edits. For a broad
situation without an implied deliverable, recommend a route and wait for that
choice before substantive work. Run a full Grill only on an explicit request
for an adversarial pressure test.

## Scientific boundaries and author control

Use only facts, data, methods, and sources supplied by the author or actually
inspected. Preserve numbers, units, identifiers, formulas, citation keys,
display references, terminology meaning, scope, modality, and causal force.
Keep observation, interpretation, and implication distinguishable. Association,
co-location, temporal order, model fit, and a proxy do not independently establish
causation or mechanism.

Scientific propositions in the current manuscript are the working position for
editing, unless marked exploratory, contradicted by supplied evidence, or
reopened by the author. That baseline lets ordinary editing proceed; it does
not certify evidence or establish explicit author acceptance. Keep recorded
observations, interpretations, and author decisions separate, with their origins
and statuses recoverable. An AI proposal remains a proposal until accepted.

Propose scientific alternatives freely in the collaboration. Commit a new
mechanism, causal relation, evidence role, scope, claim strength, conclusion, or
contribution priority only after the author accepts it. Choose grammar,
phrasing, sentence boundaries, redundancy repair, and organization directly when
they express the same settled science. Continue safe work around an unresolved
choice; mark an exploratory draft's unsettled content as provisional.

For facts, numbers, methods, and what a citation reports, primary artifacts and
inspected source text control. For interpretation, terminology preference, and
writing direction, the author's latest explicit accepted decision controls
within that evidence boundary. Surface a material conflict. Keep superseded
mechanisms, rejected wording, and process records outside the manuscript unless
they independently serve its scientific argument.

### Material sufficiency

Before substantive drafting, restructuring, or evidence-dependent review, check
that its load-bearing dependencies exist in the supplied basis. First recover
support from relevant sections, displays, notes, accepted decisions, and
inspected sources. A deficit is load-bearing when silently filling it would
change what the reader accepts as established. Ordinary language editing of the
author's existing claims is not gated by uninspected background citations.

Stop the affected content when a load-bearing deficit remains. Name the missing
material and why it matters, and offer a bundled resolution: supplied material,
authorized retrieval or analysis, or an explicitly accepted provisional draft
with unsupported spans marked. An author-acknowledged gap left open is an
accepted constraint, not permission to invent its completion. Continue unrelated
safe work. Load [scientific-integrity.md](references/scientific-integrity.md) for
evidence-dependent drafting or review, claim calibration, causal interpretation,
citation verification, or a material deficit. New literature retrieval and new
analysis require an explicit request.

## Select sources and preserve the carrier

The author's explicit style choice controls. Otherwise use surrounding approved
prose for continuity, and neutral field-appropriate prose when no manuscript
style basis exists. Older drafts supply terminology and study context;
expression comes from them only when requested. Ask about an older draft's
expression role only if that unresolved choice materially changes the result.
Load [style-source-contract.md](references/style-source-contract.md) for new
drafting, substantive rewriting, style coordination, or a designated style
sample; it owns the source-priority matrix and disclosure rules.

A supplied reference authorizes inspection. Its use for facts, citation support,
terminology, reasoning, comparison, or style must be assigned or clearly implied
by the request. Learn transferable tendencies and rebuild the author's own
argument; source-specific facts, mechanisms, limitations, distinctive wording,
and recognizable templates remain the source authors' content. Use
[reference-learning.md](references/reference-learning.md) for supplied sources.

Change prose inside its original carrier. Preserve LaTeX citation commands,
labels, math and macros; Word fields, comments and tracked changes; Markdown
markup; and unresolved TODO or highlighted author state. Keep the output usable
by its existing tool chain; flag markup that blocks the requested change.
Conversion, comment cleanup, and acceptance of
tracked changes are separate requested operations; confirm any destructive
removal of unresolved author state.

## Review within the requested scope

The default is one integrated result. For substantive drafting or rewriting,
combine scientific fidelity, reasoning, genre fit, and naturalness checks.
Explicit naturalness or AI-style requests also load the protection and
naturalness references below, including detection-only work. For integrated
work, use this order:

1. Recover evidence and current author state; pass or surface the material gate.
2. Check facts, evidence roles, inference, scope, modality, and causal force.
3. Improve argument and genre quality within those scientific boundaries.
   Apply [academic-protection.md](references/academic-protection.md) and
   [academic-naturalness.md](references/academic-naturalness.md) for the
   naturalness component. Diagnose observable defects, not presumed authorship.
4. Rewrite within scope, preserving every needed function. For repeated
   same-function content, follow the naturalness reference's priority: current
   author state and evidence correctness, then terminology continuity, with
   specificity deciding only a tie. Preserve unresolved competing instances and
   report the conflict instead of selecting by detail alone.
5. Apply the proportional final check to the completed deliverable.

Natural prose is idiomatic, disciplined, and shaped by scientific reasoning.
Preserve fluency and scholarly register when a pattern signal conflicts with
them. Protect meaningful qualifiers, contrasts, parallel evidence, and reasoning
links through their function rather than a word exemption or a banned form.

Use [scientific-review-axes.md](references/scientific-review-axes.md) for
mechanism or causality, Abstract/Conclusion changes, cross-section or submission
work, deletion with scientific dependencies, or an explicit two-axis request.
Scientific fidelity sets the boundary for argument and genre quality; these
checks do not require two agents.

Narrow requests override the integrated delivery:

- “只检查 AI 味儿” or “扫描 AI 腔”: inspect local function and report
  expression-pattern findings without rewriting or inferring authorship.
- Scientific logic, evidence, terminology, or claim-strength only: run the
  corresponding checks and preserve unrelated expression.
- “双轴审查” or equivalent: report Scientific fidelity and Argument and genre
  quality separately, then the disposition and evidence gaps.

## Coordinate drafting and retain context when needed

Draft in one context by default. A full section, multiple sections, or a long
translation does not trigger isolation by length alone. Split only when
planning residue would interfere with drafting, interdependent evidence or
cross-section decisions need a separate planning and review stage, or the
author explicitly requests isolated drafting/review. Sentence-level work,
single paragraphs, and local edits stay in one context. A request for a brief
or checkpoint delivers that artifact and does not itself dispatch a writer.

When splitting, load [handoff-drafting.md](references/handoff-drafting.md) for
the decision, evidence-complete brief, required review, and return channel.
Dispatch without pausing unless the author requested brief inspection, a
scientific choice remains open, or the brief cannot safely support the task.
The reviewer receives the writer's evidence package. Post-review modifications
pass the affected final checks again. An unsplit multi-section or full-manuscript
translation still checks terminology, modality, Title–Abstract–Conclusion, and
cross-references before delivery.

For multi-section, manuscript-wide, repeated cross-session, or explicitly
context-preserving work, maintain a project-local `MANUSCRIPT-CONTEXT.md` using
[manuscript-context.md](references/manuscript-context.md). It retains compact
current state and evidence roles; it does not replace primary materials. Read
an existing context after recovering the manuscript basis. Local edits use it
only when the target depends on a recorded decision.

When work will continue in a new session, conversation, or agent, use
[manuscript-session-handoff.md](references/manuscript-session-handoff.md) to
maintain `MANUSCRIPT-SESSION-HANDOFF.md`: the next action, evidence, decisions,
gaps, and checks actually run. Keep this continuation packet distinct from
durable context and the intra-task drafting brief.

## Reference routing

Load only active branches; use one section reference per section in scope.
The shared workflow above points to its detailed references. Section-specific
and additional branches are:

| Active task | Reference |
|---|---|
| Introduction drafting, diagnosis, or substantive restructuring | [Introduction](references/introduction.md) |
| Methods drafting, completeness review, or substantive restructuring | [Methods](references/methods.md) |
| Results organization, drafting/review, or figure/table captions | [Results](references/results.md) |
| Discussion interpretation, literature integration, or restructuring | [Discussion](references/discussion.md) |
| Title, Abstract, Conclusion, or contribution compression | [Synthesis](references/synthesis.md) |
| Insertion into an existing manuscript, cross-section changes, long revision history, or terminology/claim consistency | [Continuity](references/continuity-and-consistency.md) |

## Deliver and check the requested form

Draft and rewrite requests receive manuscript-ready prose; plan or brief
requests receive the proposed organization or requested artifact with reasons.
Logic review receives findings and scientific consequences, with rewriting only
when included in the request. Citation review distinguishes verified, unsupported, and uninspected
support. In user-facing Chinese, call uninspected support “支持尚未核实”.
Translation preserves scientific meaning and modality in natural target-language
prose. For progressive review, deliver the chosen unit and wait before advancing
when requested. For `只给修改稿`, return only the revised text unless a concise
blocking question is indispensable.

Keep editing explanations, source-reading notes, proposals, verification status,
and collaboration history outside manuscript prose. Disclose the active style
basis when it materially affects the result or an audit is requested, except in
manuscript-only output.

Perform one proportional final check after the requested edits:

| Requested work | Check before delivery |
|---|---|
| Sentence or narrow correction | Compare with its source and enough surrounding context for meaning, terms, numbers, references, modality, and grammatical fit. |
| Paragraph or section revision | Read the complete revised unit and affected sequence for evidence-to-claim links, necessary inference, paragraph progression, repetition, and register. |
| Manuscript-wide or explicit cross-section work | Read the relevant supplied sections together for identity, numbers, claims, displays, scientific arc, and section-appropriate expression. |

After deletion or merging, preserve the removed span's needed function and
check demonstratives, citation support, and apparatus dependencies under the
protection and naturalness references. Expand reading only for concrete
dependencies; inspection does not authorize edits outside scope. Identify
unavailable context without claiming it was checked. An excerpt cannot support
a whole-manuscript judgment.

If a defect remains, repair within scope and recheck the affected content and
dependencies. Repeat a wider check only when the repair changes those wider
relations. Keep routine checks internal; report consequential changes,
requested findings, and unresolved issues.

Complete when the deliverable is usable within the authorized scope, its facts
and scientific commitments follow the supplied basis and current author state,
and material issues are resolved or clearly surfaced.
