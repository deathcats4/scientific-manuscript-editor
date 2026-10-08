# Persistent manuscript context

Use this reference when a project has a `MANUSCRIPT-CONTEXT.md` file, or when
the work is multi-section, manuscript-wide, repeated across sessions, or the
author asks for a persistent context. The file is a compact project artifact,
not a second manuscript and not a session log.

## When to create or read it

Create `MANUSCRIPT-CONTEXT.md` lazily in the manuscript project or manuscript
folder when one of these conditions holds:

- the task spans multiple sections or requires manuscript-wide synthesis;
- the same manuscript will be edited across sessions;
- terminology, accepted interpretations, or evidence roles would otherwise
  need to be recovered repeatedly; or
- the author explicitly asks to preserve the working context.

Do not create or load it for an isolated sentence edit unless the target
depends on a project decision recorded there. If the file exists, read it after
recovering the supplied manuscript basis for section-scale, manuscript-wide,
cross-session, and continuity work. A context file is a pointer to the current
state; it does not replace the manuscript, figures, methods, data, or inspected
sources.

## Precedence and reconciliation

Use this order when sources disagree:

1. primary artifacts and inspected source text for facts, numbers, methods,
   conditions, and what a citation actually reports;
2. the author's latest explicit accepted decision for interpretation,
   terminology, scope, and claim strength;
3. the context file for a compact record of the current state;
4. older drafts, process notes, or an earlier context entry.

Surface a conflict that changes the requested content. Do not silently restore
a superseded mechanism or wording from the context file. A current manuscript
claim may be recorded as `working`, and an inspected observation may be recorded
with its source. Change a scientific decision to `accepted` only after explicit
author acceptance. Record a provisional proposal when needed for the ongoing
task or requested by the author, keeping its unresolved consequence visible.

## Separate observation, interpretation, and acceptance

Each entry carries one proposition, its origin, and a single decision status
where applicable. Split a measured observation from the interpretation it may
support; an accepted value does not confer acceptance on its interpretation.
Distinguish the current manuscript, an explicit author decision, an inspected
primary artifact, and an editor's recovery or proposal as origins.

For scientific positions, use these statuses:

| Status | Meaning and editing consequence |
|---|---|
| `working` | A position present in the manuscript supplied for editing, with no separate explicit acceptance recovered. Use it as the editing baseline unless reopened or contradicted; ordinary edits need no new confirmation. |
| `accepted` | The author explicitly accepted this particular interpretation or decision. Cite the recoverable decision, not only the draft in which the wording appears. |
| `provisional` | An exploratory interpretation or editor proposal not accepted as the manuscript's position. Keep its open choice and consequence visible. |
| `rejected` | The author rejected the position; retain it only to prevent a likely regression. |

Decision status and evidence verification answer different questions. Author
acceptance does not verify a source or prove a mechanism. Record inspected
observations and verification limits under evidence roles; list unanswered
choices under open decisions rather than mixing statuses in one claim.

For example, a constructed record separates: the reported mean is higher in
group A than B (observation; source location); prior accumulation is a possible
explanation (interpretation; `working` or `provisional` with its origin); and an
author decision to retain that explanation (if explicitly made, `accepted`).
Do not combine the comparison and explanation into one accepted entry with an
open qualification appended.

## Keep the file small

Record only information that will change a later manuscript decision. Prefer a
single current entry over a history of edits. Keep rejected or superseded items
only when they prevent a likely regression; label them clearly. Do not copy
full paragraphs, long quotations, full reference lists, or the collaboration
transcript into this file.

The context has seven parts:

1. **Manuscript identity and scope** — working title, study object, section
   scope, sample/site naming, and the intended audience when it affects claims.
2. **Canonical terminology** — preferred terms, allowed variants,
   non-interchangeable terms, abbreviations, symbols, and units.
3. **Current author state** — individual interpretations and contribution
   decisions with their origins; mark each as `working`, `accepted`,
   `provisional`, or `rejected` using the definitions above.
4. **Evidence roles** — the result, display, method condition, limitation, or
   inspected source that supports each load-bearing claim; link to the source
   or manuscript location rather than copying it.
5. **Claim boundaries** — permitted causal force, scope, modality, comparison,
   and conclusion strength.
6. **Open decisions** — unresolved choices that must stay outside committed
   manuscript prose, with the consequence of each option.
7. **Superseded entries** — old terms or interpretations retained only to stop
   regression, each with the replacement and date or decision reference.

## Suggested format

```markdown
# Manuscript context

## Identity and scope
- Working title:
- Study object:
- Current manuscript scope:
- Intended reader or venue constraint:

## Canonical terminology
| Concept | Preferred term | Allowed variant | Do not merge with | Status/source |
| --- | --- | --- | --- | --- |

## Current author state
- [working] ... (origin: current manuscript; location: ...)
- [accepted] ... (origin: explicit author decision; basis: ...)
- [provisional] ... (origin: ...; open consequence: ...)
- [rejected] ... (origin: explicit author decision; replacement: ...)

## Evidence roles
- Observation: ... (source/location; inspected or uninspected)
- Claim or interpretation: ...
  - Supports: ... (location/source)
  - Limits: ... (location/source)

## Claim boundaries
- Causal force:
- Spatial/temporal/comparative scope:
- Modality and uncertainty:
- Conclusion boundary:

## Open decisions
- Decision: ...
  - Option A would ...
  - Option B would ...

## Superseded entries
- Old term or interpretation → current replacement; retain to prevent regression.
```

The format is a starting point, not a checklist. Omit empty sections. Use the
manuscript's own terminology and keep evidence links resolvable in the current
project.

## Completion check

Before delivery, confirm that every context entry changed by the task is either
still supported, explicitly updated, or marked as an open or superseded state;
observations and interpretations have separate recoverable origins; every
accepted decision has an explicit author basis rather than inferred approval;
and the delivered prose follows the reconciled current state rather than the
context file alone.
