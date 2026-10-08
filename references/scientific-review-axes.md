# Scientific review axes

Use for substantive drafting or rewriting, mechanism or causal interpretation,
abstract or conclusion revision, manuscript-wide review, submission-stage work,
or an explicit request to review scientific fidelity and prose separately. This
reference defines a scientific-paper-specific review model. It is not a pair of
independent scores and it does not require two agents.

## The review model

Run the review as three linked stages:

1. **Evidence gate** — recover the supplied facts, displays, methods,
   conditions, limitations, inspected sources, and the current author state.
   If a load-bearing dependency is missing, report the gap before committing a
   stronger claim. A fluent sentence cannot pass an evidence deficit.
2. **Scientific fidelity axis** — check whether the requested prose preserves
   what the evidence and the author support.
3. **Argument and genre axis** — check whether the reader can recover the
   scientific relation in clear, section-appropriate prose.

Finish with one integration pass. A revision passes only when both axes are
acceptable within the requested scope and the final text still satisfies the
evidence gate. The gate and the two axes answer different questions, but they
are not interchangeable: argument quality cannot upgrade evidence, and
scientific correctness cannot excuse an unreadable or structurally broken
argument.

## Scientific fidelity axis

Check the following in the supplied scope:

- **Identity and exact content:** samples, sites, groups, variables, numbers,
  units, signs, precision, formulas, citations, and display references agree
  with the source of truth.
- **Evidence role:** each load-bearing claim has the right result, display,
  method condition, limitation, or inspected source behind it; a result summary
  does not silently stand in for an unprovided boundary condition or negative
  result.
- **Inference:** the necessary bridge from observation to interpretation is
  present and no new mechanism, comparison, or conclusion is smuggled in.
- **Force and scope:** association remains distinct from causation; modality,
  spatial and temporal scope, comparison class, and conclusion strength do not
  become stronger or broader through editing.
- **Author state:** working, accepted, provisional, and rejected interpretations
  remain distinct, with observations and interpretations separately sourced.
  The current manuscript is an editing baseline, not proof of explicit
  acceptance or verified evidence. A recommendation or source interpretation
  does not become an accepted position without authorization. Use the status
  definitions in [manuscript-context.md](manuscript-context.md) when recording it.

Classify a finding as a **scientific conflict**, **unsupported dependency**,
**editorial inconsistency**, or **no finding**. A missing dependency is a gap,
not a negative finding about the prose.

## Argument and genre axis

Check the following after the scientific basis is locked:

- **Reader endpoint:** the passage gives the intended reader the understanding
  or decision the section is meant to deliver.
- **Paragraph progress and coherence:** each paragraph helps the reader
  understand, compare, rule out, or connect something needed for the section's
  question, with necessary context and relationships recoverable. Parallel
  comparisons, orientation, and synthesis need a clear role in that argument;
  they need not form a linear handoff or add a new scientific finding.
- **Evidence-to-inference visibility:** the prose makes non-obvious reasoning
  recoverable without adding a generic purpose, gap, or significance sentence.
- **Section and discipline fit:** Introduction, Methods, Results, Discussion,
  Abstract, and Conclusion perform their different rhetorical jobs; captions,
  citations, qualifiers, and display references retain their functions.
- **Expression quality:** language is idiomatic, precise, appropriately dense,
  and free of mechanical repetition, empty framing, or process residue. Apply
  the academic naturalness invariant and preserve meaningful scholarly forms.

Classify a finding as an **argument gap**, **genre mismatch**, **expression
pattern**, **redundancy**, or **no finding**. Do not relabel a scientific
conflict as a style preference.

## How the axes interact

Run the scientific fidelity axis before making a revision that could change a
claim, inference, causal verb, comparison, or conclusion. When it finds a
scientific conflict or unsupported dependency:

- keep the affected claim provisional or stop it under the material
  sufficiency gate;
- repair wording only within the supported boundary;
- do not use smoother prose, a stronger citation, or a genre convention to
  conceal the unresolved issue.

The argument and genre axis may still repair safe organization or expression
around the gap, but it cannot resolve the scientific choice. If the author
accepts a new scientific position, rerun the affected scientific checks before
finalizing the prose.

## Invocation and delivery

The user-facing default remains one integrated review. Use the full linked model
internally when the task is substantive, mechanism- or causality-sensitive,
changes the Abstract or Conclusion, spans sections, prepares a submission, or
deletes or merges text with scientific or apparatus dependencies. A local
grammar, terminology, translation, or figure-reference edit stays local unless
the passage contains a material scientific conflict.

When the author explicitly asks for “双轴审查”, “分别检查科学忠实度和表达质量”,
or equivalent, report two clearly separated sections:

1. **Scientific fidelity** — findings, evidence status, and scientific
   consequence;
2. **Argument and genre quality** — findings and reader-facing consequence.

Then report the disposition: revised safely, retained as provisional, left
unchanged because it is supported, or blocked pending author material or a
scientific decision. Do not create two independent conclusions from different
evidence packages. Independent agents are optional under the handoff rules for
interdependent evidence, interfering planning residue, or an explicit isolation
request; length alone does not require them.

## Completion check

The review records, internally or in the user-facing result as requested, that
the evidence gate was satisfied or the gap was surfaced, each active axis was
checked at the requested scope, scientific findings were not hidden by prose
improvements, and any post-review change passed both affected axes again.
