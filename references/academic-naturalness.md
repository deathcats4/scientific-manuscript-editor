# Academic naturalness and AI-style review

Use with [academic-protection.md](academic-protection.md) for AI-style diagnosis
or integrated naturalness revision. Review only the supplied editable scope; a
paragraph supports local observations about expression. These are editorial
heuristics for writing decisions, not authorship features or detector scores.

## Identify a defect before editing

A finding identifies a specific span and explains the writing problem. Evaluate
words, punctuation, sentence length, and parallel forms through their local
function. A phrase is actionable when it supplies empty framing or an
unsupported rhetorical relation; a repeated form is actionable when recurrence
adds no needed function. Preserve purposeful repetition identified by academic
protection.

Inspect structure before vocabulary. Within the authorized scope, read paragraph
roles, sentence relationships, and local phrasing in that order. Use the
manuscript-reasoning reference for substantive restructuring; keep the scientific
argument within the author's supplied material.

## Candidate patterns and their boundaries

| Candidate | Actual problem to establish | Repair and false-positive boundary |
|---|---|---|
| Generic opening or significance ending | The sentence could attach to unrelated studies without adding a relevant claim | State existing substantive content directly. Keep a supported contribution, scope statement, or section orientation. |
| Repeated mini-essay structure | Each paragraph restarts the same premise and ends with the same abstract takeaway | Remove duplicated work or reorganize around real relationships. Parallel studies and procedures may legitimately remain parallel. |
| Artificial opposition | A negative half invents a position solely to make the positive claim sound stronger | Retain supported claims and state the real relation. A genuine exclusion, comparison, or additive `not only X but also Y` carries content. |
| Defensive repetition | Several caveats repeat one already calibrated boundary or rebut an unclaimed stronger proposition | State the existing boundary at its proper location. Preserve limitations that change interpretation. |
| Formulaic rhythm | Repeated openings, triads, fragments, or sentence shapes add padding or obscure emphasis | Let information and reasoning determine sentence boundaries. Keep necessary list items; do not turn three findings into two to avoid a triad. |
| Empty transitions or restatement | A connective, heading echo, or summary repeats without advancing understanding | Remove the empty part while keeping the logical relation and any needed inferential step. |
| Inflated or vague evaluation | Praise substitutes for a supported result, comparison, or contribution | Use specifics already supplied. If removing it changes the author's claim, flag or follow author-control rules; do not invent supporting detail. |
| Chat or editing residue | Text speaks to the user about drafting rather than to the manuscript reader about the subject | Remove only the process text. Protect quotations, research data, methodological explanations, and substantive clauses sharing the sentence. |

Paragraph interchangeability, uniform length, and repeated closers are prompts
to inspect function. Introductory framing, topic sentences, conclusions, and
explicit inference can all be necessary; preserve reasoning while improving
surface variety.

## English checks

- Inspect ornamental framing such as `It is important to note that`, vague
  significance claims, and trailing participial clauses that merely announce
  importance. A participial clause expressing a real process or consequence
  remains content.
- Review repeated sentence-initial connectors in context. Change placement or
  combine sentences only when the underlying addition or contrast survives.
- Prefer a precise ordinary verb when a longer phrase adds nothing; retain
  technical senses and calibrated verbs. `significant` may carry statistical
  meaning; `robust` may name a method or a demonstrated property.
- Use dashes, semicolons, long sentences, passive voice, and nominalization when
  their function and rhythm support readability.

## Chinese checks

- Inspect generic setups and endings such as `随着……的不断发展` or
  `具有重要意义` for a concrete role in the current argument. Repair empty
  framing, not every occurrence of these strings.
- Check long modifier chains, unclear subjects, and translation-driven word
  order. Reorder to clarify who or what does what while retaining conditions,
  scope, and reference attachment.
- Review repeated `此外`、`然而`、`因此` against the actual logical relation.
  A necessary connection remains valid even if the same word appears nearby.
- Keep established scholarly terms and morphology. Shorten `进行分析` to `分析`
  when it improves the sentence; retain `形成`, `构建`, `性`, and `化` when
  they carry the intended scholarly relation and keep formal prose formal.

For mixed-language prose, apply each check to its local language and protect
embedded terminology, formulas, and citations. These language notes do not
override the manuscript's terminology or the authorized style source.

## Review and delivery

For a detection-only request, report the exact span, its observable defect, and a
repair direction. Separate clear findings from uncertain context. State when the
supplied scope contains no actionable defect, and return findings without a
rewrite unless the author requests one.

For integrated revision, use the entrypoint's combined workflow and proportional
final check. This is the naturalness component of that check. Repair established
problems, reread the affected passage in context, and check for template
recurrence, preserved claims and reasoning, and qualifiers or connectives whose
only role is academic decoration. Return the requested deliverable and share the
inspection when an audit or explanation is requested.

Use counts as descriptive aids. Let information and reasoning determine
sentence-length variance, connector density, paragraph ratios, and word count.
Finish when the identified defects are repaired and meaning and register are
intact.

## Protect academic fluency

Apply the entrypoint's academic naturalness invariant. Preserve a functional
pattern whenever changing it would reduce fluency, scholarly register, or
scientific fidelity; report it as non-actionable when a finding list is
requested.

## Contrastive examples

These constructed examples illustrate decisions, not reusable manuscript prose.

| Input or situation | Expected decision |
|---|---|
| `It is important to note that the estimate was 0.42 (95% CI 0.31–0.53; Fig. 2).` | Remove the empty preface; preserve the estimate, interval, punctuation within the notation, and figure reference. |
| `The association may possibly reflect X.` | Reduce duplicated modality to `may reflect X` when both qualifiers express the same uncertainty; retain the original causal strength. |
| `X predicts Y. This finding provides important insights into the prediction of Y by X.` | Remove the second sentence's empty restatement and keep the supplied scientific scope. |
| `此外，X 升高。相比之下，Y 降低。` | Keep the contrast. Whether the initial addition marker is useful depends on preceding context. |
| `结果表明 X 升高。这一发现为理解 X 的升高提供了重要参考。` | Keep the result and its original strength; remove the empty second sentence. |
| Three paragraphs report three distinct model comparisons with the same syntax | Retain necessary parallelism; flag only redundant framing, not the comparison structure itself. |
| `We surveyed 120 participants. I have made this paragraph more concise.` | Keep the first sentence and its count; remove the editing narration. |
| A prose-only draft supplies no magnitude for `a substantial improvement` | Preserve the magnitude claim and flag the evidential gap outside the draft when the supplied basis cannot resolve it. |
