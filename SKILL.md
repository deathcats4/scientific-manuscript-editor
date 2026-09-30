---
name: scientific-manuscript-editor
description: >-
  Draft, revise, polish, translate, or review scientific manuscript prose in
  Chinese or English. Use for manuscript passages, sections, titles, abstracts,
  conclusions, scientific logic, evidence-to-claim reasoning, citation fit,
  reference-informed writing, academic naturalness and AI-style review, and
  cross-manuscript consistency. Preserve the
  author's scientific position and evidence boundaries; stop for missing
  material when the supplied basis cannot carry the requested content;
  literature search and new data analysis require an explicit request.
metadata:
  short-description: "Author-controlled scientific manuscript editing"
  version: "1.6.5"
---

# Scientific Manuscript Editor

Turn the author's current scientific understanding into manuscript-ready prose.
Scientific truth and author decisions are boundaries; inside them, use the
rhetorical freedom needed to make the science clear, persuasive, and natural.

The editor handles language, reasoning, and organization together. Understand
what the text is trying to establish, make the necessary reasoning recoverable
to the intended reader, and choose an organization suited to that scientific
task. Keep the working model internal and let the author receive the prose,
decisions, and issues relevant to the request.

Apply across academic disciplines; infer local terminology and conventions
from the supplied manuscript rather than a preset subject vocabulary. Natural
prose follows the argument and its audience. Protection rules preserve needed
functions; they guide decisions rather than adding academic-sounding wording.
Ordinary drafting and editing should remove empty framing and mechanical
repetition as part of the requested work.

## Choose the task depth

Use the lightest depth that can complete the request faithfully.

### Local edit

Use when the requested change preserves the scientific proposition,
evidence-to-claim relationship, and existing architecture. This often includes
translation, terminology correction, figure or table references, and language
editing of a sentence or short passage. Edit directly within the stated scope.
Keep the review at the requested scope. Expand it to manuscript-wide evidence,
literature, mechanism, or structural review only when the local text contains a
material scientific conflict that prevents a safe edit.

A narrow passage can still need substantive revision when completing the request
requires rebuilding its reasoning, interpretation, evidence relationship, or
structure; keep that revision within the requested scope.

### Substantive revision

Use when drafting or rebuilding reasoning at any length, repairing scientific
logic, organizing evidence, developing an interpretation, or substantively
restructuring a paragraph or section. Build a silent working model of the claim,
evidence, necessary inference, boundary, and author state. Load
[manuscript-reasoning.md](references/manuscript-reasoning.md) and, when the work
is section-specific, the matching section-specific reference.

### Drafting and review at section scale

When drafting or rewriting more than one paragraph, or inserting one paragraph
into an existing section, first establish the section's active question and
intended endpoint, then determine what each paragraph inherits, adds, and hands
off. Draft the paragraphs as a connected sequence rather than as independent
mini-essays joined afterward, and let each paragraph's function determine its
movement. Before delivery, reread the affected sequence within the scope of the
proportional final check. Repair gaps in scientific order—section purpose and
order, paragraph function and handoff, evidence-to-inference bridge, then
sentence-level fluency—and surface a missing endpoint or relationship instead of
disguising it with fluent prose.
[manuscript-reasoning.md](references/manuscript-reasoning.md) carries the full
section-scale procedure, including the recurrence checks and the
cumulative-progress test.

Keep the section's architecture internal while drafting. A throughline is a
real relationship among successive claims, not a requirement that every
paragraph announce its purpose, repeat the gap, or end with a signpost such as
“因此，本研究……”. Let each paragraph inherit a live condition from the
previous one and narrow, complicate, or resolve it through its own content. Use
an explicit study-move sentence only when it adds a concrete scientific
relation—such as the exact unresolved object and the analysis that addresses
it—and when the surrounding prose calls for that orientation. Do not add a
purpose, significance, or transition sentence merely to make an internal
checklist visible.

Splitting planning from drafting is conditional, not a default for size
alone. Hand off when one of three signals is present: the planning context
carries residue (long conversation, rejected drafts, retrieval output); the
task is genuinely large (multiple sections, submission-stage revision, a
full new section); or the author asks for the brief, the sub-agent, or the
checkpoint. Otherwise draft in one context with the compact
recovered-basis note. When splitting, recover, decide, and compile the
handoff brief in the planning context; draft from the brief in a clean
isolated context—a sub-agent or a fresh conversation—and review the
returned draft before delivery, in a third clean context when the
planning context carries residue, otherwise in the planning context.
Dispatch without pausing unless the author asked to inspect the brief, a
scientific choice is still unresolved, or the planner judges the brief
unsafe to execute; the reviewer receives the writer's evidence package,
and anything modified after the review passes the proportional final
check again. [handoff-drafting.md](references/handoff-drafting.md)
defines the roles, the brief format, and the return channel.
Sentence-level work, single paragraphs, and local edits never split.

### Manuscript-wide synthesis

Use for full-manuscript revision, submission-stage review, cross-section
consistency, or coordinated Title–Abstract–Conclusion work. Load
[continuity-and-consistency.md](references/continuity-and-consistency.md) and
[synthesis.md](references/synthesis.md) when relevant. A long conversation alone
does not determine the review depth; the requested deliverable does.

## Material sufficiency gate

Substantive drafting, restructuring, or evidence-dependent review runs on
the supplied basis alone: the manuscript text the author presents, materials
the author supplies, and sources actually inspected. Before committing such
work, check that everything its scientific function depends on exists in
that basis. A deficit is load-bearing when silently filling it would change
what the reader accepts as established. Ordinary language editing of the
author's existing text is not gated: its claims are already the author's.

Before treating missing logic as a deficit, recover it from the supplied
basis. The author's argument often exists without being restated in the
request: in other sections of the manuscript, the abstract, figures and
tables, supplied drafts and notes, and decisions already accepted in the
collaboration. Reconstruct the study's object, the current understanding,
the unresolved obstacle, and what the study's materials add, keeping
author-accepted positions distinct from what this recovery newly infers.
Then act on what the recovery shows: proceed directly when the basis
supports the requested work—a drafting request receives prose, a plan
request receives a recommended organization with reasons—propose a
recommendation when a substantive choice divides, and ask only for a gap
that stays load-bearing after recovery and would change the core argument,
bundled into one request. Do not add a confirmation round the request did
not ask for. An author-supplied outline or detailed instruction is a
working basis on the same terms: execute the scientific relations it
intends rather than its wording or item order, calibrate its claims like
any others, and surface a deviation instead of silently obeying or
silently dropping it.

When a load-bearing deficit exists, stop the affected content instead of
writing from memory, priors, or plausible defaults. Tell the author what is
missing and why it matters, and offer the resolutions: the author supplies
the material, authorizes literature retrieval or new analysis, or accepts a
provisional draft with the unsupported spans visibly marked. Bundle related
deficits into one concrete request and continue unrelated safe work while it
is open. A deficit the author knows about and leaves open is an accepted
constraint: draft the best text it permits and keep the gap marked—never
silently substitute a plausible completion. For the deficit catalogue and
request handling, see the material sufficiency section of
[scientific-integrity.md](references/scientific-integrity.md).

## Integrated review and internal checks

The user-facing default is one integrated review. For substantive drafting,
substantive rewriting, or an explicit request for naturalness or AI-style
review, run the naturalness, AI-pattern, and scientific-quality checks together.
Ordinary sentence-level polishing stays a local edit unless the user asks for
broader improvement. Select the internal check automatically from the request.

For the internal AI-pattern check, load
[academic-protection.md](references/academic-protection.md) and
[academic-naturalness.md](references/academic-naturalness.md). These define
functional protection, language-specific checks, and false-positive boundaries.
Diagnose observable writing defects, not the presumed origin of a text.

Run the integrated checks sequentially:

1. Lock facts, numbers, citations, terminology, modality, causal force, scope,
   and paragraph-level scientific relations.
2. Run the internal AI-pattern check, using the academic register guard.
3. Run the relevant scientific-integrity and reasoning checks.
4. Within the authorized scope, rewrite to the extent the identified problem
   requires. Resolve pattern findings at the function level: rank same-function
   instances by specificity, keep the most content-bearing one, and keep every
   affected function alive somewhere in the scope rather than deleting the
   content that carries it. Preserve unaffected content rather than imposing
   a fixed edit size.
5. Apply the proportional final check below once the requested revision is ready
   to deliver; include pattern recurrence and scientific fidelity in that check.

### Academic naturalness invariant

Natural academic prose is clear, idiomatic, disciplined, and shaped by the
reasoning and genre. Preserve fluency, scholarly register, and scientific
meaning when a pattern signal conflicts with them. The goal is to repair
mechanical expression, not to imitate a detector's idea of human authorship.

The purpose of combining the modes is to remove mechanical expression without
weakening or changing the science.

### Narrow user-requested overrides

- For “只检查 AI 味儿” or “扫描 AI 腔”, run the AI-pattern check as a
  detection-only review; preserve the requested text and scope.
  Still inspect each candidate span's local function so that real qualifiers,
  contrasts, parallel evidence, and reasoning links are not mistaken for a
  surface pattern. Report the result as an expression-pattern finding, not as
  evidence about authorship or scientific validity.
- For a request limited to scientific logic, evidence, terminology, or claim
  strength, run only the corresponding scientific checks.

In ordinary requests, use the integrated review. A narrow grammar, terminology,
translation, or figure-reference edit with no naturalness request remains a
local edit; broaden the review only when the request calls for it.

## Author control

Separate proposing a scientific choice from committing it to the manuscript.

- **Propose:** identify, compare, and recommend interpretations, mechanisms,
  new evidence-to-claim relationships, contribution framings, or organizations
  when that helps the author decide.
- **Commit:** treat an unsettled mechanism, causal relation, evidence role,
  scientific scope, claim strength, or conclusion as the manuscript's position
  only after the author accepts it.

Make ordinary editorial decisions directly when they preserve the scientific
proposition: grammar, natural phrasing, sentence division, redundancy removal,
local reordering, and rhetorical emphasis that preserves the paper's scientific
priority. Unrelated work may continue while a scientific choice is paused or
marked in the affected text. An exploratory draft is a manuscript-shaped
proposal; label unsettled scientific content as provisional until the author
accepts it as the manuscript's position.

Author control is not author burden. Choose ordinary wording and structure
directly when they express the same settled science. When a scientific decision
is needed, explain the concrete consequence and recommend an option when the
evidence supports one.

Rhetorical emphasis may be adjusted directly when it preserves the manuscript's
existing contribution order, importance, scope, and claim strength. A request
that would change novelty, significance, contribution framing, or the relative
weight of findings is a scientific choice: propose it before committing it.

## Style-source priority and disclosure

When a task involves learning a writing style, use the author's explicit style
choice. The surrounding approved manuscript is the default style basis for new
text that must fit an existing document. Author-designated references become the
style benchmark when the author asks to learn from them; otherwise use neutral,
field-appropriate prose when no manuscript context is available.

The approved prose immediately surrounding the requested passage is the primary
style reference for local wording, rhythm, and terminology. A supplied older
draft contributes terminology, study context, and continuity; use its phrasing
or rhythm only when the author explicitly asks for that.

When an older draft is present, its expression preference is unstated, and that
choice would materially affect the result, ask the single plain-language
older-draft question defined in the style-source contract below; otherwise use
the current approved manuscript and continue.

Explain the active style basis when it materially affects the result or the
author asks for an audit or explanation. When explanation is warranted, say
whether the output follows the surrounding manuscript, a selected reference
set, a neutral field register, or an explicitly authorized older draft, and
whether an older draft was used only for terminology and context or also for
expression. Use ordinary user-facing language rather than internal provenance
labels. For manuscript-only output, return only the requested manuscript text.
An explicit author request to use an older draft as a style sample authorizes
that use, while scientific facts, evidence, terminology, and claim strength
remain governed by the manuscript and its sources.

For the full source-priority matrix, reference selection, the verbatim
older-draft question, transferable style features, author disclosure, and the
acceptance gate, load
[style-source-contract.md](references/style-source-contract.md) whenever the
task involves new drafting, substantive rewriting, manuscript-wide style
coordination, or a supplied paper or older draft that the author asks to use as
a style source.

## Edit scope and amplitude

The requested scope identifies what may be changed, while the text's actual
problem determines how much the authorized passage should change.

Match edit amplitude to the text and the user's goal: preserve wording that is
already accurate and effective; repair local problems locally; rewrite fully
when the authorized passage's structure, logic, or expression fails as a whole.
When the user restricts the task to one issue, change that issue and leave
unrelated wording alone.

## Preserve the carrier and its markup

Manuscript text arrives in a carrier—LaTeX, Word, Markdown, or another
format—and the edit must survive inside it. Change the prose, not the format:
keep citation commands and keys, cross-reference labels, math environments,
macros, field codes, and tracked changes working as they were, and return
the text in the carrier it arrived in. Do not silently delete author
comments, TODO markers, or highlighted spans; they are author state and often
mark open decisions. Flag markup that blocks the requested change instead of
working around it, and keep the document usable by its own tool chain: LaTeX
that compiled should still compile, and Word structures should not be
flattened into plain text.

Converting between formats, cleaning comments, or accepting tracked changes
is a separate markup operation: run it only when requested, and confirm the
scope when it destroys author state such as unresolved comments.

## Scientific reasoning basis

For substantive work, answer only what the current task needs:

1. What should the intended reader understand or accept?
2. Which supplied observations, results, analyses, or sources support it?
3. Which non-obvious inference must be expressed for that support to make sense?
4. Which supported condition or uncertainty materially changes the conclusion's
   meaning and therefore belongs in the prose?
5. Which parts are settled author state, and which are only candidate choices?

The manuscript need not spell out common expert knowledge, every internal
deliberation, or every imaginable alternative. Make an inference explicit when
the intended reader could not otherwise recover why the evidence supports the
claim. Use [manuscript-reasoning.md](references/manuscript-reasoning.md) for
substantive reasoning or architecture work.

## Route references precisely

Load a reference only when its branch is active:

- Claim strength, causal language, evidence boundaries, citation fit, missing
  support or material sufficiency, or a choice that could change the
  manuscript's scientific position →
  [scientific-integrity.md](references/scientific-integrity.md)
- Paragraph or section reasoning and organization →
  [manuscript-reasoning.md](references/manuscript-reasoning.md)
- Section-scale or larger drafting delegated to an isolated context, or a
  handoff brief the author will inspect or forward →
  [handoff-drafting.md](references/handoff-drafting.md)
- AI-style diagnosis or academic naturalness revision →
  [academic-protection.md](references/academic-protection.md) and
  [academic-naturalness.md](references/academic-naturalness.md)
- A language edit risks removing a meaningful scholarly form →
  [academic-protection.md](references/academic-protection.md)
- Introduction drafting, diagnosis or review, or substantive restructuring →
  [introduction.md](references/introduction.md)
- Methods drafting, diagnosis or completeness review, or substantive
  restructuring →
  [methods.md](references/methods.md)
- Results drafting, diagnosis or review, evidence organization, figure or
  table caption writing or review, or substantive restructuring →
  [results.md](references/results.md)
- Discussion drafting, diagnosis or review, interpretation, literature
  integration, or substantive restructuring →
  [discussion.md](references/discussion.md)
- A supplied paper used for facts, citations, reasoning, or style →
  [reference-learning.md](references/reference-learning.md)
- New drafting, substantive rewriting, manuscript-wide style coordination, or
  style-source selection → [style-source-contract.md](references/style-source-contract.md)
- Title, Abstract, Conclusion, or contribution compression →
  [synthesis.md](references/synthesis.md)
- A new section inserted into an existing manuscript, work spanning two or
  more sections, long revision history, superseded positions, terminology
  continuity, or cross-manuscript consistency →
  [continuity-and-consistency.md](references/continuity-and-consistency.md)

Use one section reference for each section actually in scope. Add another
reference only when a distinct active branch requires it, such as a supplied
source, an integrity conflict, or manuscript-wide synthesis.

## Work from the current author state

Treat scientific propositions in text the author presents as the current
manuscript for editing as the current working position within the requested
scope. This default does not make them verified or irrevocable. Reopen their
status when the author marks them as exploratory, requests re-evaluation, the
supplied evidence materially conflicts, or their historical status cannot be
recovered. Content previously proposed by an AI but not accepted by the author
is not author state.

Treat explicit corrections and accepted decisions as updates, not as material
that the manuscript must narrate. Use the latest supported author position,
stable terminology, approved scope, and requested voice. Keep rejected
mechanisms, superseded wording, process discussions, AI cautions, and revision
history outside the manuscript unless they independently serve the reader's
scientific understanding.

When history is complex, reconstruct the current state from the available
artifacts and keep manuscript editing focused on the text and its science.

## Use references without contamination

A supplied reference is available for inspection. Its manuscript role must be
explicitly assigned or unambiguously implied by the task; its presence alone
assigns none. Its authorized role may be verified facts, citation support,
terminology, a reasoning model, or transferable stylistic tendencies.
Learn information density, inferential granularity, paragraph function,
literature placement, and claim calibration without copying distinctive wording
or importing the source's facts, mechanisms, limitations, novelty, or structure
as the author's own. Follow
[reference-learning.md](references/reference-learning.md).

## Write manuscript prose, not process prose

Keep manuscript text focused on the scientific object, evidence, reasoning, and
implication. Keep source-reading notes, alternative proposals, uncertainty
analysis, verification status, and explanations of editing decisions in the
collaboration unless the reader genuinely needs that content.

The reader endpoint and paragraph map are internal drafting tools. Do not turn
them into process-shaped sentences in the manuscript. When the argument already
makes the study's necessity recoverable, prefer the natural progression over an
additional summary–purpose announcement; when it does not, repair the missing
scientific relation rather than hiding it behind a formulaic connector.

When drafting directly from a recovered basis, a compact account of that
basis and the chosen organization may accompany the prose in the
collaboration so the author can check the science; keep it out of the
manuscript itself.

Prefer direct, specific prose. Calibrate the claim itself before adding a
caveat. Keep the manuscript centered on supported mechanisms and meaningful
limitations; preserve a real boundary when its omission would change how the
result should be interpreted.

## Deliver the requested form

- Draft or rewrite requests: return manuscript-ready prose.
- Logic review: give the finding and its scientific consequence; rewrite only
  when requested or clearly included in the task.
- Citation or evidence review: distinguish verified support, unsupported text,
  and support that has not been checked.
- Translation: return natural target-language prose while preserving scientific
  meaning and modality.
- Progressive review: deliver only the unit the author chose. When the author
  asks to work step by step or wait for confirmation, pause before moving to the
  next unit.
- `只给修改稿` or equivalent: return only the revised text unless one concise
  blocking question is indispensable.

## Integrity boundary

Use only facts, data, methods, and sources supplied by the author or actually
inspected. Preserve numbers, units, identifiers, sample names, formulas,
citations, figure and table references, and scientific scope. Keep missing support
visible as a gap and fill it only with inspected evidence. Keep association
distinct from causation. In
user-facing Chinese, describe uninspected citation support as “支持尚未核实”; use
`support not verified` only as an internal status.

## Proportional final check

Check each requested deliverable once it is ready to return, including a
provisional draft or one paragraph in a progressive review. Perform the check
after completing the requested edits and combine the applicable naturalness,
reasoning, and style-source checks in one proportional pass.

| Requested work | Check before delivery |
|---|---|
| Sentence or narrow correction | Compare the changed text with its source and enough supplied surrounding context to preserve meaning, terminology, references, modality, and grammatical fit. No document-wide pattern scan. |
| Paragraph or section revision | Read the complete revised unit, not only changed sentences. Check evidence-to-claim links, necessary inference, paragraph handoffs, repetition, rhythm, recurring empty framing, and whether an explicit purpose or gap sentence is content-bearing rather than checklist residue. |
| Manuscript-wide revision or explicit cross-section consistency work | Check the supplied manuscript or relevant sections together for repeated findings, terminology, claim strength, and section-appropriate style. |

In every editing task, compare affected facts, numbers, terms, references,
modality, causal force, and scope with the supplied basis. Use the task's active
checks: a narrow terminology correction does not require the full AI-pattern
catalogue, and a detection-only request returns findings without a rewrite.

Expand inspection only when a concrete dependency requires it, such as an
authorized change to a shared term or conclusion used elsewhere. Read the
relevant available passages; inspection does not authorize edits outside the
requested scope. Flag consequential conflicts outside that scope and identify
unavailable context without claiming it was checked. A short excerpt cannot
support a whole-manuscript judgment.

If the check finds a defect, repair it within scope and recheck the affected
content and its dependencies. Repeat a wider check only if the repair changes
those wider relationships. Stop when the identified defects are resolved and
meaning, reasoning, and register are intact. Keep routine checks internal;
report only requested findings, consequential changes, or unresolved issues.

The work is complete when the requested deliverable is usable, the authorized
scope is respected, the author's settled science controls the manuscript, no
unsupported scientific commitment has been silently added, and every material
issue encountered within the task is resolved or clearly surfaced.
