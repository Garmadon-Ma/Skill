# Section Playbook

Use this playbook for empirical, method-centered IEEE Transactions manuscripts. The numeric targets reflect three 10–15 page two-column samples; obey an explicit venue limit first. Count final English prose, excluding references, captions, tables, and displayed equations unless the venue specifies otherwise.

## Whole-paper budget

For a typical 10–15 page manuscript, allocate the main body approximately as follows:

| Section | Share of main body | Sample-centered target |
|---|---:|---:|
| Introduction | 11–14% | 800–1,100 words; about 1.5–2 pages |
| Related Works | 9–12% | 700–1,000 words; about 1–1.5 pages |
| Preliminary | 7–13% | 500–950 words; about 0.75–1.5 pages |
| Proposed Method | 23–31% | 1,800–2,600 words; about 2.5–4 pages |
| Experimental Results | 36–47% | 2,500–4,000 words; about 3.5–7 pages |
| Conclusion | 1–2% | 90–160 words; about 0.25 page |

Abstract is separate: normally 190–240 words in one paragraph. For a Chinese working draft, match the same rhetorical units and remeasure after English translation; do not convert English word counts mechanically into Chinese characters.

## Abstract

Write one paragraph of roughly 8–10 sentences in this order:

1. State the task and why it matters in one sentence.
2. Identify the practical condition and observable failure.
3. Explain the mechanism behind that failure and the exact limitation of existing methods.
4. Name the proposed framework and state its central design principle.
5. Give one sentence per major method component, in execution or causal order.
6. State the representation, optimization, or decision-boundary consequence that links the components to the task.
7. Close with datasets/scenarios and the strongest evidence-supported outcome; include a representative number only when verified and useful.

Do not include citations, equations, bullets, undefined acronyms, literature surveys, implementation trivia, or future work. Avoid beginning with a generic claim such as “deep learning has achieved great success.”

## Introduction

Target 6–10 purposeful paragraphs plus contribution bullets:

1. **Operational context and task.** Move from the deployment need to the precise learning problem. Define ID/OOD or source/target conditions only as needed.
2. **Practical challenge.** Show what changes in the real setting and what degrades. Use a motivating figure early when the failure is geometric or distributional.
3. **Existing direction.** Summarize the most relevant solution families in a few sentences; reserve taxonomy detail for Related Works.
4. **Mechanism-level gap.** Explain why those methods fail under the stated condition. Name the intermediate failure—feature overlap, shortcut dependence, sparse tail coverage, unstable boundary, biased prototype—not just the final metric drop.
5. **Design requirements.** Convert each diagnosed cause into a property the solution must have.
6. **Core insight and method arc.** Introduce the theory or observation that enables the design, state its limitation in this setting, then explain the adaptation and why it should work.
7. **Contribution bullets.** Use 3–4 bullets. Each bullet should contain: component or idea; concrete action; technical effect; evidence or scope. Do not list routine implementation details as contributions.
8. **Roadmap.** End with one compact paragraph mapping the remaining sections.

The first occurrence of a claim may be broad; by the motivation subsection it must be testable. The final contribution list should predict the method subsection titles and the experimental evidence categories.

## Related Works

For this personalized installation, [related-work-outline.md](related-work-outline.md) governs subsection structure, paragraph defaults, and endings. The general guidance below is supplementary and does not override that outline.

Use 2–4 thematic subsections. Choose themes that triangulate the proposed method—for example, task-domain methods, the practical complication, and the enabling theory—rather than listing papers chronologically.

Within each subsection:

1. Define the theme and its relevance.
2. Group prior work by mechanism, supervision, representation, or inference strategy.
3. Compare representative methods with precise verbs: models, aligns, calibrates, synthesizes, regularizes, decouples.
4. State what the family handles well.
5. End with a concrete requirement in the target setting or a supported limitation. Do not invent a deficiency merely to motivate the proposed method.

Keep this section literature-facing. Do not re-explain the full problem story from the Introduction or disclose detailed equations of the proposed method. Cite original, authoritative work for methods and claims; verify citation metadata when possible.

## Preliminary

Use 2–3 subsections, generally:

1. **Problem formulation:** datasets/domains/classes, train-test visibility, variables, model outputs, score, and decision rule.
2. **Required theoretical foundation:** only the properties later instantiated by the method.
3. **Required modeling tool:** only if a second formalism is central to a later component.

For each concept, give the definition, assumptions, essential equations, and one closing sentence that states exactly how it will be used. Keep the notation table near this section when symbol density is high. Do not move a novel loss, adaptation, or claimed contribution into Preliminary merely to make the method appear shorter.

## Proposed Method

For this personalized installation, [method-algorithm-outline.md](method-algorithm-outline.md) governs the overview, component paragraph functions, derivation depth, and mathematical pseudocode. Its defaults override generic paragraph and word quotas.

Use one short overview followed by the actual modules in causal or execution order. Each component normally needs two or three connected paragraphs covering the design reason and construction, the necessary mechanism or property, and the objective/interface. Merge brief functions instead of forcing separate paragraphs. Do not invent a baseline deficiency or repeat Preliminary merely to fill a template.

Keep necessary new derivations in the main text and distinguish proved properties from intended effects. Describe adaptation and inference compactly, reuse defined losses, and place implementation constants in Experimental Setup where appropriate. Use defined operators and matrix expressions to keep algorithms mathematically informative without listing routine implementation steps.

## Experimental Results

Give experiments the largest evidence budget. Use three top-level subsections unless the study requires another split.

### A. Setup

Present in reproducibility order:

1. datasets and practical scenarios;
2. ID/OOD, source/target, train/validation/test, and repeated-task splits;
3. preprocessing and input construction;
4. baseline families and why each is relevant;
5. common backbone and fairness controls;
6. implementation, optimization, hyperparameters, hardware, and inference details;
7. metrics, operating points, direction of improvement, and averaging/variance protocol.

Do not bury data leakage prevention, class selection, or validation usage. Distinguish fixed choices from tuned hyperparameters.

### B. Main results

Order results from the principal claim to increasingly difficult deployment conditions. For each table or figure paragraph:

1. state the comparison question;
2. identify the strongest baseline under the same protocol;
3. report the proposed method’s value and an unambiguous absolute percentage-point or relative gain;
4. connect the pattern to a method mechanism;
5. mention an important exception, degradation, variance, or boundary of validity.

Use tables for comprehensive comparisons and figures for curves, trends, distributions, or source-to-target change. Interpret patterns; do not narrate every cell.

### C. Ablation and diagnostic evidence

Build an evidence ladder tied to the claims:

- component ablation for necessity;
- loss-weight and key-parameter sensitivity for stability;
- hard-scenario or source-to-target analysis for deployment robustness;
- feature/score geometry or qualitative distributions for the proposed mechanism;
- outlier/prototype/sample quality checks when generated or latent structures are claimed;
- alternative backbone, unknown-class count, imbalance ratio, or complexity tests for scope and generality.

An ablation paragraph should name the removed component, the failure mechanism it addresses, the expected consequence, the observed change, and the bounded conclusion. “This validates effectiveness” alone is not analysis.

## Conclusion

Follow [conclusion-outline.md](conclusion-outline.md) for this user's preferred sentence functions, compact continuous paragraph, and concrete future-work ending. Its causal progression takes precedence over generic word and sentence quotas.