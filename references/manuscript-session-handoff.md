# Manuscript session handoff

Use this reference when manuscript work will continue in a new session, fresh
conversation, or new agent, or when the author explicitly asks for a
continuation handoff. This is a compact continuation packet, not manuscript
prose, not a session transcript, and not a replacement for
`MANUSCRIPT-CONTEXT.md`.

Keep the three artifacts distinct:

- **`MANUSCRIPT-CONTEXT.md`** is the durable project state: terminology,
  working, accepted, or provisional author state, evidence roles, claim
  boundaries, and regression guards.
- **`MANUSCRIPT-SESSION-HANDOFF.md`** is the next-session workset: the current
  task, the exact next action, attached evidence, open decisions, and material
  gaps. It may point to the context file instead of repeating it.
- **`handoff-drafting.md`** is an intra-task planner–writer–reviewer split for
  one drafting or revision task. It is not a cross-session summary.

## When to create or read it

Create or update a project-local `MANUSCRIPT-SESSION-HANDOFF.md` only when:

- the work will cross a session, conversation, or agent boundary;
- the author asks to save a continuation point; or
- a long task has reached a clean milestone and the next action is specific.

Do not create one for an isolated sentence edit or use it as a general log of
what happened. Read it after recovering the supplied manuscript basis and the
durable context, if one exists. The manuscript and primary artifacts remain the
source of truth.

## Recover the state before writing the handoff

Reconcile information in this order:

1. primary manuscript, data, figures, methods, and inspected source text for
   facts, numbers, conditions, and citation support;
2. the author's latest explicit accepted decision for interpretation,
   terminology, scope, and claim strength;
3. `MANUSCRIPT-CONTEXT.md` for the durable current state;
4. the current session's notes for work completed and the next action.

If these sources conflict, surface the conflict instead of choosing silently.
Do not promote an agent proposal to accepted author state merely because it
appears in the handoff.

## Compile the continuation packet

Keep the packet short and actionable. Use this order:

1. **Destination.** The next session's goal and the first concrete action.
2. **Current task.** Manuscript, section, language, requested operation,
   scope, venue or length constraint, and delivery form.
3. **Current author state.** Only positions that affect the next action;
   carry their origins and `working`, `accepted`, or `provisional` status under
   [manuscript-context.md](manuscript-context.md). Keep observations and
   interpretations separate; list unanswered choices under open decisions.
4. **Evidence package.** Links or paths to the relevant manuscript spans,
   displays, methods, and inspected sources; identify missing load-bearing
   material and its consequence.
5. **Completed work.** The exact files or sections changed and the checks that
   have actually run.
6. **Open decisions.** The smallest remaining choices, their consequences,
   and who must decide them. Keep unresolved scientific choices outside
   committed prose.
7. **Next validation.** What the next session must verify before delivery,
   including continuity, evidence, and any return to the author.
8. **Regression guards.** Retain a superseded term or interpretation only
   when it could re-enter the draft; record its replacement and mark it as
   `superseded—do not write`.

Use this starting shape and omit empty sections:

```markdown
# Manuscript session handoff

## Destination
- Next session goal:
- First action:

## Current task
- Manuscript/section:
- Operation and scope:
- Delivery:

## Current author state
- [working] ... (origin: current manuscript; location: ...)
- [accepted] ... (origin: explicit author decision; basis: ...)
- [provisional] ... (origin: ...; consequence: ...)

## Evidence package
- Claim or task dependency: ...
  - Source/path: ...
  - Role and limit: ...

## Completed work
- ... (file or manuscript location; check actually run)

## Open decisions
- Decision: ...
  - Option/consequence: ...

## Next validation
- ...

## Regression guards
- [superseded—do not write] Old term/interpretation → replacement: ...
```

## Context-to-prose boundary

The handoff tells the next session what to recover and what to do; it does not
tell the manuscript to narrate the collaboration. Do not copy its task history,
open decisions, rejected alternatives, or regression guards into manuscript
prose. An exclusion belongs in the manuscript only when the reader needs an
evidence-based scientific comparison or limitation; write that relation from
the evidence, not as a report of the author's prior discussion.

Never use the handoff alone to supply a fact, citation, mechanism, or causal
claim. Reopen the linked primary material when the next action depends on it.

## Completion check

The next session can begin with the stated first action without rereading the
full transcript; each scientific position has a recoverable origin and status;
missing evidence and unresolved decisions are visible; superseded material is
kept only as a regression guard; and no process record has been turned into
manuscript content.
