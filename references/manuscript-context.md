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
a superseded mechanism or wording from the context file. Update the context
only after the author accepts the decision, or when the author explicitly asks
to record a provisional state. A factual entry may be added from an inspected
primary artifact, but its source and status must remain visible.

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
3. **Current author state** — accepted interpretations and contribution
   framing; mark each as `accepted`, `provisional`, or `rejected`.
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
- [accepted] ... (basis: ...)
- [provisional] ... (open consequence: ...)
- [rejected] ... (replacement: ...)

## Evidence roles
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
no AI-proposed decision has been recorded as accepted; and the delivered prose
follows the reconciled current state rather than the context file alone.
