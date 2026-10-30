# Logic, Traceability, and Style

Use this reference to plan a whole paper, repair weak reasoning, or perform a final audit.

## Claim-evidence architecture

Build a traceability matrix before drafting or auditing:

| Failure mechanism | Design requirement | Method component | Expected observable | Evidence | Allowed claim |
|---|---|---|---|---|---|
| What specifically goes wrong? | What property must change? | What implements it? | What metric/geometry/behavior should move? | Main result, ablation, diagnostic, sensitivity | What can be said without overreach? |

Reject or revise any major claim with an empty method or evidence cell. If one experiment supports several claims, identify which measured aspect supports each claim. Correlation between a visualization and performance is mechanistic evidence only when alternative explanations are addressed.

## Cross-section handoff

Each section should answer one question and hand a more precise question to the next:

- **Introduction:** Why does the problem matter, and what mechanism blocks existing solutions?
- **Related Works:** Which solution families approach the problem, and which design requirements remain unmet?
- **Preliminary:** What exact task, notation, and theoretical tools are needed to state the solution?
- **Method:** How does each component satisfy a design requirement, and what observable consequence follows?
- **Experiments:** Do those consequences and the overall claim hold under fair and relevant tests?
- **Conclusion:** What is supported, in what scope, and what remains unresolved?

Avoid repeated mini-abstracts. A transition should carry forward the unresolved issue, not restate the previous section.

## Paragraph logic

Prefer a compact claim-reason-evidence-implication pattern:

1. topic sentence makes one local claim;
2. explanation gives the mechanism or reason;
3. equation, citation, result, or example supplies support;
4. closing sentence states the implication or transition.

Split paragraphs that contain two independent claims. Merge paragraphs that only define a term and do not develop an argument. Use explicit causal connectors only when causality is warranted; use “is associated with,” “is consistent with,” or “suggests” for weaker evidence.

## Theory and equations

- State assumptions near the result that depends on them.
- Separate a known theorem from the paper’s adaptation of it.
- Explain why a theoretical property is relevant to the target failure mechanism.
- Preserve dimensions, domains, normalization, constraints, and trainable/fixed status of every key variable.
- After a loss equation, state the direction of the induced behavior and the parameters it affects.
- Do not call an optimizer, loss, or geometric construction “optimal” unless the objective and sense of optimality are explicit.

## Experimental reasoning

- Match baselines to the claimed novelty dimensions, not just popularity.
- Keep data, backbone, preprocessing, tuning budget, and evaluation split comparable; disclose unavoidable differences.
- Define whether gains are absolute percentage points or relative percentages.
- Report dispersion or repeated-run protocol when available; do not claim statistical significance from mean differences alone.
- Discuss the strongest competing method and any setting where the proposed method degrades.
- Use sensitivity results to justify a stable operating region, not merely a single best point.
- Use component ablations to test causal necessity; use diagnostics to test the proposed mechanism; use robustness tests to establish scope.

## Figures and tables

- Refer to each figure or table before or immediately when it appears.
- Make captions self-contained enough to identify data, comparison, and metric direction.
- Use the main table for the primary claim, not a peripheral metric.
- Make visual encodings consistent across datasets and figures.
- In prose, interpret the decisive pattern and exceptions rather than copying values.
- A framework figure should expose training versus testing, data flow, component interfaces, and outputs.

## IEEE-style prose

- Use formal, direct sentences and concrete technical verbs.
- Prefer “we propose,” “the method constructs,” and “the loss encourages” over vague nominalizations.
- Keep tense consistent: present for method and established facts; past for performed experiments; present for table/figure observations.
- Define acronyms at first use in the Abstract and again in the main text when needed by the template.
- Use consistent capitalization and hyphenation for terms such as open-set, in-distribution, out-of-distribution, test-time, and class-conditional.
- Avoid promotional adjectives, unsupported “significantly,” repeated “novel,” throat-clearing, citation piles without synthesis, and excessive “furthermore.”
- Do not imitate template placeholders, dummy journal headers, malformed references, or bilingual fragments from working drafts.

## Final coherence audit

Check these mappings explicitly:

1. title and Abstract name the same central problem and method;
2. each Introduction gap becomes a design requirement;
3. each contribution bullet maps to a method subsection;
4. each method component maps to at least one direct experiment;
5. each headline result supports a claim already stated;
6. Conclusion claims are no broader than the tested datasets, shifts, backbones, or operating conditions;
7. limitations and future work follow from observed boundaries rather than introducing unrelated topics.