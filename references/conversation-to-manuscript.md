# From conversation to manuscript

Use this reference whenever the author is discussing an idea, doubt, context,
reference paper, mechanism, or the AI's reasoning while also working toward
manuscript text. Its purpose is to keep useful collaboration from leaking into
the paper as unnecessary qualification or self-defence.

When the context comes from project history, agent handoffs, logs, or old
drafts, first reconstruct the active project state with
[context-reconstruction.md](context-reconstruction.md).

## Three spaces

**Collaborative exploration** is the reasoning workspace. Here the editor can
explain the author's concern, inspect a source, compare interpretations, test
whether evidence is sufficient, and identify an unresolved choice. Breadth is
allowed because the goal is to help the author think.

**Author decision** is the control point. The author decides whether a proposed
mechanism, limitation, comparison, framing change, or scope change belongs in
the manuscript. A question or worry from the author authorizes explanation of
that worry; it does not by itself authorize weakening the claim or adding every
possibility discussed.

**Manuscript delivery** is the reader-facing result. It contains the smallest
set of claims, evidence, qualifications, and transitions needed for the
paragraph or section to do its scientific job. It does not carry the history of
the collaboration.

## Manuscript admission test

For each candidate sentence or clause that arose during discussion, ask:

1. What scientific or reader-facing function does it perform here?
2. If it is removed, would a reader materially misunderstand the claim,
   evidence, scope, causal relation, or logic?
3. Has the author authorized this content when it changes a mechanism,
   framework, limitation, comparison, or conclusion?

Admit the content only when the answers establish a real manuscript function
and the required author decision is present. Otherwise keep it in the
conversation, use it to improve the chosen text, or omit it from the delivery.

## Current state, not correction history

Use the conversation to maintain the author's current position, not to recreate
the route by which it was reached. When the author replaces interpretation A
with B, mark A as superseded and write from B directly. The correction helps
the editor avoid returning to A; it does not give A a role in the manuscript.

Distinguish the author's operation:

- A clear replacement or factual correction updates the active position and
  removes the superseded position from manuscript candidates.
- A refinement updates the scope, wording, or strength of the same position;
  draft the refined position without narrating the earlier version.
- An alternative the author explicitly keeps open remains available for
  discussion, but enters the manuscript only through the admission test.
- An author-requested scientific comparison keeps both positions active and
  may justify explicit contrast.

Before writing a construction such as `not A but B`, `B rather than A`, or
`although A, B`, ask:

1. Is A still a live scientific interpretation for the manuscript, rather than
   merely an earlier point in the dialogue?
2. Does contrasting A with B help the reader understand the evidence, inference,
   or conclusion actually presented?
3. Has the author requested or accepted this comparison when it affects the
   scientific framing?

If these conditions are not met, state B affirmatively and omit A. If the
author's correction is ambiguous about whether A has been rejected or retained,
resolve that ambiguity in the collaboration space rather than encoding both
positions defensively in the draft.

## Common leakage patterns

These are symptoms of a boundary error, not a checklist to reproduce in every
paragraph:

- explaining how the AI understood the prompt or proved that it followed an
  instruction;
- transferring source-reading notes, audit trails, or generic uncertainty into
  the prose merely because they were discussed;
- rebutting a mechanism that is only a different study, condition, or
  background explanation;
- adding a limitation because the editor can imagine it, when it does not
  change the paper's actual claim or scope;
- preserving the dialogue's questions and answers as if they were part of the
  scientific argument;
- turning a superseded position into an unnecessary `A rather than B` contrast
  merely to demonstrate that the editor remembered the correction.

The positive rule is: write the author's supported explanation and the
qualifications that do real scientific work. Put the rest in the collaboration
report or leave it out.

## When the author is confused or worried

First answer the concern in the collaboration space using the available
evidence. Then return to the selected manuscript function. Do not treat the
act of explaining a concern as evidence that the concern belongs in the paper.
If resolving it would require choosing between genuinely competing mechanisms,
use the
[author decision rule](evidence-and-citations.md#author-decision-rule-for-competing-mechanisms)
and pause only the affected content.

## Final separation check

Before delivery, scan the manuscript portion as if the conversation had never
occurred. It should read as an intentional scientific argument, not as a record
of the editor's caution, source inspection, self-verification, or correction
history. Review contrastive constructions and retain only those whose two sides
are scientifically live and useful to the reader.
