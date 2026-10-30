# Paragraph and Key-Sentence Blueprints

Use this reference when the user asks for detailed drafting, expansion, compression, or structural diagnosis. The word budgets are planning ranges for final English prose, not quotas. Prefer a shorter sentence that preserves the logic. As a practical default, keep most technical sentences at 15–30 words; inspect any sentence over 35 words and normally split one over 45 words.

The phrase skeletons below are functional templates, not text to copy mechanically. Replace every bracketed item with grounded paper content and vary wording to avoid repetitive prose.

## Abstract: 190–240 words, one paragraph, 8–10 sentences

| Unit | Function | Typical length | Key-sentence skeleton |
|---|---|---:|---|
| S1 | Task + importance | 18–28 words | “[Task] is important for [deployment goal] because [concrete consequence].” |
| S2 | Target condition | 18–30 | “In practice, [condition] causes [observable shift/failure].” |
| S3 | Mechanism + gap | 22–35 | “Existing methods remain limited because [mechanism], which [technical consequence].” |
| S4 | Method identity | 20–32 | “To address this issue, we propose [full method name] ([acronym]), which [central design principle].” |
| S5–S7 | Major components | 22–36 each | “First/Next, [component] [operation], thereby [local effect].” |
| S8 | Integrated consequence or inference | 20–34 | “The resulting [geometry/distribution/representation] enables [decision rule or expected behavior].” |
| S9 | Evidence | 20–35 | “Experiments on [datasets/scenarios] show [verified outcome and scope].” |
| Optional S10 | Implication | 15–25 | Use only if the implication is supported and not generic. |

Compression priority: remove general background first, then implementation detail, then secondary components. Never remove the failure mechanism, central method action, or evaluated scope.

Abstract key sentences must answer:

- What exact setting breaks existing performance?
- Why does it break at the representation/optimization/decision level?
- What does each proposed component change?
- How is the learned change used at inference?
- What evidence supports the final claim?

Avoid citations, displayed or numbered equations, footnotes, undefined abbreviations, symbol-heavy prose, contribution bullets, and future work. IEEE allows a single paragraph up to 250 words; keep a margin below the limit for production edits.

## Introduction: 800–1,100 words, normally 7–10 paragraphs

### P1. Operational context and task: 80–115 words

Use 4–6 sentences: deployment context; why the sensing/learning modality is appropriate; precise task; ID/OOD or source/target meaning; consequence of failure.

Key sentence, 18–28 words: “[Task] must therefore [required capability] under [deployment condition], where [concise definition of the open or shifted setting].”

Do not begin with more than two sentences of broad field history. Reach the paper’s actual task by sentence 3 or 4.

### P2. Practical complication: 90–125 words

Use 4–6 sentences: introduce the real-world complication; explain how it changes data; identify the observable feature/score behavior; state why the behavior matters.

Key sentence, 22–35 words: “This setting violates the common assumption that [assumption], causing [intermediate failure] rather than merely reducing closed-set accuracy.”

### P3. Existing solution direction: 75–110 words

Use 3–5 sentences. Group the closest methods by mechanism and give only enough examples to establish the dominant approach.

Key sentence, 20–32 words: “Existing approaches mainly [shared action], which improves [handled aspect] but leaves [unhandled aspect] unresolved.”

### P4. Mechanism-level limitation: 100–140 words

Use 4–7 sentences: show why the existing mechanism fails in the target condition; trace the failure through features, prototypes, density, optimization, or scores; end with the open technical requirement.

Key sentence, 24–38 words: “Consequently, a method that only [insufficient action] cannot [required behavior] because [mechanism-level reason].”

This is the logical hinge of the Introduction. If it only says “few studies consider X,” rewrite it until it explains what fails and why.

### P5. Motivation and enabling insight: 90–125 words

Introduce the theory or observation that can satisfy part of the requirement. State both its useful property and why its standard form is insufficient.

Key sentences:

- Insight, 18–30 words: “Our starting observation is that [property] provides [needed capability] by [mechanism].”
- Limitation, 20–35 words: “However, directly applying [theory/standard design] remains insufficient because [setting-specific mismatch].”

### P6–P7. Method reasoning: 160–230 words total

Derive components rather than list them. Use the repeated chain `requirement -> component -> induced behavior -> next unresolved issue`.

Key sentence, 20–34 words: “We therefore construct [component] to [operation], which is expected to [observable technical effect].”

The last sentence of one paragraph should motivate the first sentence of the next. If a component appears without a preceding requirement, the chain is incomplete.

### Contribution lead-in and bullets: 130–200 words total

Use a 15–25 word lead-in and normally 3–4 bullets of 35–65 words each. A strong bullet contains:

1. a short noun phrase naming the contribution;
2. one sentence describing the concrete construction;
3. one sentence giving its technical effect or evidence scope.

Skeleton: “**[Contribution label]:** We [construct/formulate/design] [specific object] to [operation]. This [mechanism/evidence] [bounded effect].”

Do not use “for the first time” without a verified novelty search. Do not make “extensive experiments” a standalone scientific contribution; attach evidence to the method or robustness claim it supports.

### Roadmap: 35–55 words

One paragraph, usually one or two sentences. Use complete IEEE section references: “Section II,” “Section III,” and “Section IV-A,” not “the next section” or “Subsection IV-A.” The 800–1,100-word section total is the controlling budget; merge P3 with P4 or P6 with P7 when the lower-level ranges would exceed it.

## Related Works: 700–1,000 words, 2–4 thematic subsections

For this user, [related-work-outline.md](related-work-outline.md) takes precedence over the paragraph counts and ending templates below. Use the word ranges only when consistent with the manuscript budget and current request.

### Section opening: 35–65 words

Name the themes and their relation to the paper. Do not repeat the Introduction’s full motivation.

### Each thematic subsection: 180–300 words

Use 2–4 paragraphs or one compact synthesis paragraph when the theme is narrow:

1. **Scope/taxonomy, 35–60 words:** define the family and organize it by mechanism.
2. **Representative synthesis, 90–170 words:** compare 3–8 representative works; group citations by shared idea rather than one sentence per paper.
3. **Boundary and handoff, 35–70 words:** state what the family cannot provide under the target setting and which design requirement remains.

Key sentence skeletons:

- Synthesis, 20–35 words: “[Family A] improves [property] through [mechanism], whereas [family B] focuses on [different mechanism].”
- Limitation, 22–38 words: “Despite these advances, the methods assume [assumption] and therefore do not address [mechanism] under [target condition].”
- Handoff, 18–30 words: “This limitation motivates [required property], which is central to the proposed method.”

Avoid citation inventories, vague praise, and declaring all prior work inadequate. Distinguish task gap, assumption gap, mechanism gap, and evidence gap.

## Preliminary: 500–950 words, 2–3 subsections

### Opening: 35–70 words

List the problem formulation and only the theoretical tools needed by the method.

### Problem formulation: 180–300 words plus 1–3 equations

Use this order:

1. define input space, label/class sets, datasets/domains, and visibility at training/test time;
2. define model/feature map/classifier/score;
3. define the decision rule or optimization goal;
4. state evaluation condition or assumptions.

Key sentences:

- “Let $\mathcal{D}_{\mathrm{tr}}=\{(\boldsymbol{x}_i,y_i)\}_{i=1}^{N}$ denote [meaning], where [set and dimension definitions].”
- “Given a test sample $\boldsymbol{x}$, the model computes [output], and the decision rule is defined by [score and threshold].”
- “The objective is therefore to [task] while [constraint or deployment requirement].”

### Each theoretical foundation: 180–320 words plus 2–5 equations

Use `definition -> assumptions -> essential property -> later role`. End with a 20–35 word bridge: “Section IV uses this property to [specific construction], rather than adopting the standard form directly.”

Do not include a proposed loss or adaptation here unless it is established prior work. Do not reproduce a textbook derivation when only one property is used.

## Proposed Method

Use [method-algorithm-outline.md](method-algorithm-outline.md) for this user's paragraph and sentence functions, proof boundaries, and algorithm conventions. A manuscript-wide budget may guide length, but do not expand a concise method to meet a generic word quota or force a fixed number of subsections.

### Overview

One short paragraph, normally three to five sentences. Identify the section's method or central idea, summarize each actual module's role with a subsection reference, and end with the framework figure reference. Do not repeat the Introduction or front-load every notation definition.

### Core components

Normally two or three connected paragraphs. Explain the design reason and give the construction, show the necessary property or derivation, and state the objective/interface. These functions can share paragraphs. Construction-led modules need not reproduce general proofs from Preliminary; analysis-led modules should show the steps on which their central claim depends.

### Equations and objectives

Introduce the quantity, define new symbols and constraints locally, and explain the supported consequence without repeating the formula in prose. Reuse an existing objective through a cross-reference rather than renaming it solely for a new stage. No fixed sentence or word allocation is required after every display.

### Adaptation, inference, and algorithms

Usually two prose paragraphs suffice for adaptation/preparation and statistics/scoring/decision. Keep necessary definitions while moving implementation constants to the appropriate setup description. Algorithms should use compact, defined mathematical operators and matrix computations, with meaningful state and parameter boundaries preserved. Roughly ten to fifteen core steps is a useful default when the actual method permits it, not a limit or a target to pad toward.

## Experimental Results: 2,500–4,000 words

### A. Setup: 650–1,100 words

| Block | Typical length | Required content |
|---|---:|---|
| Dataset/scenario overview | 60–100 | Why each dataset tests a claim |
| Each dataset | 100–200 | acquisition, classes/domains, samples, target condition |
| Split/protocol | 120–220 | ID/OOD, source/target, train/validation/test, repetitions |
| Preprocessing | 100–220 | segmentation, transform, normalization, leakage control |
| Baselines | 200–400 | grouped families and relevance, not a literature review |
| Implementation | 120–220 | backbone, optimizer, schedule, batch, hardware, hyperparameter selection |
| Metrics | 120–260 | definition, operating point, direction, averaging/variance |

The reproducibility-critical sentence should be explicit: “All methods use [shared setting]; [method-specific exception] is retained because [reason].”

### B. Main results: 600–1,200 words

Use one 100–180 word paragraph per main table, dataset group, or deployment question. Each paragraph follows:

1. question and artifact reference;
2. proposed value;
3. strongest comparable baseline;
4. absolute percentage-point or clearly labeled relative gain;
5. mechanism-based interpretation;
6. exception, variance, or difficult setting.

Key sentence skeletons:

- “Table I compares [methods] under [protocol] using [metrics].”
- “Under [scenario], [method] achieves [value], exceeding [baseline] by [x] percentage points.”
- “The larger gain in [condition] is consistent with [component mechanism], although [boundary or exception].”

Never write “improves by 5%” when the calculation is a 5 percentage-point gain. Never infer statistical significance from means alone.

### C. Ablation and diagnostics: 1,000–2,000 words

Allocate 90–170 words per experiment. Use `hypothesis -> intervention -> observation -> interpretation -> boundary`.

Key sentence skeletons:

- “To test whether [component] is necessary for [claimed mechanism], we remove/replace [intervention] while keeping [controls] fixed.”
- “Removing [component] changes [metric] from [a] to [b], consistent with [mechanistic interpretation].”
- “Performance remains stable over [range] and degrades beyond [boundary], indicating [practical operating region].”

Prioritize, in order: component necessity; target deployment stress; parameter stability; feature/score mechanism; generated sample or prototype quality; alternative backbone/unknown count/complexity. Omit low-value sweeps that do not test a claim.

## Conclusion: 90–160 words, one paragraph, 5–7 sentences

| Sentence | Function | Typical length |
|---|---|---:|
| S1 | Exact problem and condition | 16–26 words |
| S2 | Method identity and central design | 18–30 |
| S3–S4 | Component roles and causal effect | 20–32 each |
| S5 | Evidence and evaluated scope | 18–30 |
| S6 | Limitation/future direction | 16–28 |

Use “Future work will examine [specific unresolved condition]” only when it follows from a limitation. Do not add citations, equations, numbers absent from Results, new terminology, or a second contribution list.

## Compression audit

When a manuscript exceeds its limit, compress in this order:

1. repeated background across Introduction and Related Works;
2. textbook derivations in Preliminary;
3. repeated equation explanations and obvious algebra;
4. baseline descriptions already cited;
5. cell-by-cell result narration;
6. redundant sensitivity studies.

Protect the mechanism-level gap, method reproducibility, main comparison protocol, direct ablations, and limitations.