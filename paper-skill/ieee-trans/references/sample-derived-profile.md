# Sample-derived Structural Profile

This profile was derived from complete text extraction and visual inspection of three user-supplied two-column manuscripts. It is descriptive evidence, not an IEEE rule. Counts are approximate because equations, figure text, and PDF reading order affect extraction.

## Source manuscripts

| Manuscript | Pages | Abstract | Introduction | Related Works | Preliminary | Proposed Method | Experiments | Conclusion |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| OSR-FSCS | 15 | 204 words | 968 | 874 | 891 | 1,931 | 3,802 | 95 |
| OSR-D2EP | 13 | 235 words | 889 | 731 | 887 | 2,042 | 2,607 | 134 |
| OSR-DETF | 10 | 240 Chinese characters + 61 Latin words | 1,227 + 255 | 1,379 + 189 | 435 + 43 | 787 + 221 | 1,658 + 541 | 120 + 40 |

For the bilingual OSR-DETF working draft, the paired values are Chinese characters plus Latin-script words. Use it mainly for section order, logic, and visual allocation, not sentence-level English style.

## Observed allocation

Across the two English manuscripts, the main body excluding Abstract, Conclusion, and references allocated:

- Introduction: 11–12.5%;
- Related Works: about 10%;
- Preliminary: 10.5–12.5%;
- Proposed Method: 23–28.5%;
- Experimental Results: 36–45%.

Visual section spans were approximately:

- OSR-FSCS: Introduction pp. 1–2; Related Work pp. 2–3; Preliminary pp. 3–5; Method pp. 5–7; Experiments pp. 7–14; Conclusion p. 14; references continue to p. 15.
- OSR-D2EP: Introduction pp. 1–2; Related Works pp. 2–3; Preliminary pp. 3–4; Method pp. 4–7; Experiments pp. 7–12; Conclusion p. 12; references continue to p. 13.
- OSR-DETF: Introduction pp. 1–2; Related Works pp. 2–3; Preliminary p. 3; Method pp. 3–5; Experiments pp. 5–8; Conclusion p. 8; references continue to p. 10.

## Shared rhetorical architecture

All three papers use the same high-level chain:

1. establish a safety/security-critical RF recognition task;
2. introduce a realistic deployment complication;
3. identify an intermediate representation failure;
4. explain why standard or imported methods do not repair that failure;
5. derive geometric, probabilistic, alignment, disentanglement, or boundary requirements;
6. instantiate those requirements as named method components;
7. define a test-time score consistent with the learned representation;
8. evaluate overall performance, the target deployment condition, component necessity, and parameter behavior;
9. conclude with a claim bounded by the tested scenarios and one next deployment challenge.

## Section patterns observed

- Abstracts contain 9 approximate rhetorical sentences and move from problem to mechanism, method components, learned consequence, and dataset-level evidence.
- Introductions include a dedicated Motivation and Contribution subsection, 3–4 contribution bullets, and a roadmap paragraph.
- Related Works uses three themes: the RF task, the practical complication or adjacent learning setting, and the enabling theory/method family.
- Preliminary introduces problem formulation plus only the theoretical tools later instantiated.
- Method opens with an overview and framework figure, develops 3–4 components, gives a joint objective, and separates training from open-set testing.
- Experiments use Setup, Experimental Results, and Ablation Study. Setup covers splits, preprocessing, baselines, fairness, implementation, and metrics. Evidence progresses from a main comparison to deployment stress, component ablation, sensitivity, and geometric/distributional diagnostics.
- Conclusions are deliberately short: problem, method, component roles, evidence scope, and future work.

## Important cautions

- OSR-DETF is visibly a working draft with a template placeholder header and bilingual prose. Never reproduce those artifacts.
- The samples sometimes use broad words such as “significantly” without a formal significance test. Prefer “outperforms” with exact values unless statistical testing supports significance.
- Sample word counts are not targets to fill. Compress Preliminary when the theory is standard; expand Experiments only when each added study tests a named claim.