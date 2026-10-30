# Method and Algorithm Writing Outline

Use this user-approved guide for method sections, training and inference descriptions, mathematical mechanisms, and pseudocode. It takes precedence over generic paragraph and word-count templates. It applies across research topics; do not import a previous paper's modules, assumptions, or deployment protocol. Language and general collaboration preferences remain in [user-style-profile.md](user-style-profile.md). Follow [equations-and-notation.md](equations-and-notation.md) for mathematical formatting.

## Core preference

Use concise prose to explain design choices, explicit equations to specify constructions, and sufficiently detailed derivations only where they support the method's distinctive claim. Algorithms should have mathematical density without becoming implementation checklists. More sophisticated presentation means better abstraction and more informative mathematics, not more steps or decorative symbols.

## 1. Whole-section structure

Use a short overview, the actual core modules in causal or execution order, and the training/inference algorithms where needed. Do not force every paper into three subsections or into a global/local/adaptation structure.

Keep the overview to one short paragraph, normally three to five sentences.

- First sentence identifies what the section presents and, when useful, the central method idea.
- Middle sentences each summarize one module's role and reference its actual subsection.
- Final sentence references the overall framework figure.

Do not repeat the Abstract or Introduction's background, list all mathematical objects before they are needed, or pad the overview to a generic word quota. Use LaTeX labels for subsection and figure references.

## 2. Core-component paragraph functions

Default to two or three natural paragraphs per component. These are functions, not mandatory separate blocks. Merge short transitions and keep a continuous argument together.

### First paragraph — design reason and construction

1. The opening sentence carries forward the requirement from the preceding module or identifies the local problem.
2. The next sentence explains the substantive design choice, such as why a particular constraint, space, objective, or information source is used. A generic wish to improve performance is insufficient.
3. Introduce the proposed operation and give its construction formula directly.
4. Immediately after the formula, explain only new symbols, dimensions, admissible conditions, and fixed/trainable status.

If the mechanism is already motivated adequately, shorten the lead-in rather than inventing another baseline deficiency. Explain the reason for a restriction, not merely how to implement it.

### Second paragraph — consequence or mechanism

Choose the appropriate treatment instead of attaching a proof to every module.

- **Construction-led component** — give the defining property or relationship in a compact equation, then explain its role. Do not repeat general properties already established in Preliminary.
- **Analysis-led component** — derive the quantity that directly supports the central claim, showing the intermediate steps required to follow the argument.
- **Established component** — cite or refer to its existing definition and explain how it is used here. Do not present a textbook derivation as methodological novelty.

The paragraph should answer what the construction establishes, not repeat its name or expand into another mini-abstract.

### Third paragraph — objective and interface

Give the corresponding loss or output, identify which parameters it updates, and explain how it connects to the next module or joint objective. Merge this material into the preceding paragraph when brief. Reuse existing losses through cross-references instead of rewriting an equivalent equation under a new subscript.

## 3. Derivation depth and proof boundaries

Use the sequence `target -> expansion -> key relation -> supported conclusion`.

- Retain detailed steps when the proposed mechanism or claimed advantage depends on them.
- Compress routine algebra and omit duplicate proofs of properties already covered in Preliminary.
- State results through natural prose and equations by default, not numbered propositions or theorem labels.
- Keep necessary method proofs beside the construction in the main text. Do not move them to an appendix by default; respect an explicit venue or user requirement if different.
- Put essential assumptions beside the claim they govern, without repeated defensive paragraphs.
- Track the object being analyzed. A property of a classifier or feature gradient is not automatically a property of parameter updates, optimization rates, or downstream decisions.
- A condition that would make an improvement hold is not evidence that the proposed method satisfies that condition. Do not turn a generic conditional identity into method-specific superiority.
- If an effect is not derived, state its design role or empirical status precisely. Do not replace an unsupported proof with more confident wording.

Removing repetitive caveats does not strengthen the result. Removing a proof also requires removing downstream statements that claim the manuscript still proves it.

## 4. Adaptation and inference

Usually use two continuous paragraphs, adjusting when the workflow genuinely requires more.

**First paragraph** gives the available inputs or reusable modules, what is fixed, what is updated, and which previously defined objective is used. Do not repeat the same loss merely to introduce a deployment index.

**Second paragraph** specifies the reference statistics or other inference objects, score, score direction, and final decision. Conventional means or covariance estimators can be explained accurately in prose rather than each receiving a display. Retain weighting, conditioning, and inverse/regularization choices when they determine the computation.

Keep necessary threshold definitions in the method, but normally place numerical thresholds, calibration protocols, iteration counts, and other implementation constants in Experimental Setup. Deleting such a detail from method prose does not authorize changing the underlying procedure or results. Preserve the user-approved placement and do not restore a specifically removed sentence elsewhere merely to circumvent the edit.

## 5. Compact mathematical algorithms

Keep algorithm titles, inputs/outputs, and pseudocode in English unless requested otherwise. Prefer roughly ten to fifteen core numbered steps when abstraction permits; neither length nor formula count is a quota.

- Express initialization, geometric construction, objectives, optimization, aggregation, sufficient statistics, and decisions mathematically where this conveys more than prose.
- Define reusable operators for repeated constructions or finite-step updates. State their arguments, meaning, constraints, and which parameters remain fixed before use or by a clear cross-reference.
- Keep the distinctive mechanism visible. An opaque operator must not hide the very operation the paper claims as its contribution.
- Use matrix expressions to combine repeated statistics or classwise operations when equivalent to the actual computation. Verify dimensions, weighting, and singular cases required by the formula.
- Preserve meaningful loops, data dependencies, state persistence, communication boundaries, and returned objects.
- Collapse routine loading, mode changes, gradient clearing, backpropagation, and storage instructions unless they change the method. A short annotation can carry an important implementation distinction.
- Do not replace a finite optimization run with an exact argmin or replace the implemented optimizer with a plain gradient-descent update solely for appearance. A defined finite-step optimization operator is appropriate when optimizer-specific details belong in Experimental Setup.
- Do not add unnecessary symbols, nested loops, or artificial branches to make an algorithm look advanced. A shorthand is useful only if its definition and reuse reduce the reader's work.

## 6. Notation and revision audit

Before editing, verify the relevant method definitions and implementation evidence supplied for the task. Distinguish a complete object, a distributed or selected part, and an independently reconstructed object. Check local versus global indexing, matrix dimensions, normalization, and fixed versus optimized variables.

A writing revision must not silently change the architecture, loss, information available at training/test time, score, parameter sharing, or optimizer. If the manuscript and available implementation evidence disagree, flag the discrepancy rather than resolving it through an unannounced methodological change.

After an authorized revision:

1. Check that each module explains its key design choice before or alongside its construction.
2. Remove duplicated background, disconnected one-sentence paragraphs, and formulas already adequately defined elsewhere.
3. Check that every claim matches the quantity and assumptions actually analyzed.
4. Synchronize dependent symbols, algorithms, captions, cross-references, and summaries within the edit's scope. Report any remaining artifact mismatch rather than implying it was fixed.
5. Compile and inspect affected equations and algorithm layout. Do not shrink mathematics merely to force a line into a column.

Keep method-specific scientific facts in the paper's own context reference. This guide records writing decisions, not a reusable scientific argument.