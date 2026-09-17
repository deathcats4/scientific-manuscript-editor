# Output contracts

Select the smallest format that satisfies the user's request.

## Collaboration and manuscript boundary

Keep the reasoning workspace separate from the manuscript deliverable. The
editor may explain context, uncertainties, source differences, mechanism
options, and the reason for a proposed edit in the conversation. The manuscript
area contains only text that performs a scientific or reader-facing function
the author has authorized.

Process evidence is not manuscript evidence: showing that the AI read a paper,
followed an instruction, checked for hallucinations, or considered a risk never
constitutes a reason to add that explanation to the paper. If the user asks for
analysis plus a revision, label the two parts separately. If the user asks for
only a revision, return only manuscript-ready text.

## Ordinary polishing

Return the complete revised passage first, followed by a brief explanation of
the main changes. Explain scientific-impacting choices; do not enumerate every
grammar edit.

## Logic review

Return a concise verdict, the material logic issue(s), and a suggested direction.
Provide a rewritten passage only when the user asks for one.

## Evidence or citation review

Separate confirmed issues from items that require author or source checking.
State whether a claim should be supported, narrowed, or left as an
interpretation; do not silently insert a plausible reference.

## Translation

Return the target-language version, then note only genuine ambiguities or
decisions that could affect scientific meaning.

## Explicit narrow format

When the user asks for “只给修改稿” or an equivalent, return only the requested
text. When the user restricts the change to one issue, change that issue and
leave unrelated wording alone.
