# Personal Writing Profile

Apply this reusable profile across research topics. The current user request, factual grounding, mathematical correctness, and venue requirements take precedence. This file controls presentation and collaboration, not the paper's scientific setting.

## Scope and Reference Routing

- For Abstract, Introduction, or Motivation and Contribution work, read [abstract-introduction-outline.md](abstract-introduction-outline.md). It is the preferred structural blueprint for this user and overrides conflicting generic sentence counts or paragraph sequences.
- For Related Work, read [related-work-outline.md](related-work-outline.md). Use its subsection and sentence functions as the default across research topics.
- For method sections, mechanism analysis, adaptation/inference, and pseudocode, read [method-algorithm-outline.md](method-algorithm-outline.md). Use its compact paragraph functions and mathematical algorithm style instead of generic multi-paragraph quotas.
- For Conclusion, read [conclusion-outline.md](conclusion-outline.md). Prefer one connected paragraph summarizing the problem, method mechanisms, experimental support, and one concrete future direction.
- For comparison tables and table typography, read [table-style.md](table-style.md). It records the approved caption size, centered method column, compact values, and minimal table notes.
- For distribution plots, ROC curves, and shaded-error line plots, read [figure-style.md](figure-style.md). It records the approved panel layout, legend positions, compact captions, and reproducible statistical presentation.
- Do not assume that the user's next paper concerns open-set recognition, radio signals, clients, federated learning, neural collapse, or ETF. Identify the current task and its actual mechanisms from its materials.
- Only for OSR-FETF work, read [osr-fetf-context.md](osr-fetf-context.md). Its terminology and technical constraints do not apply to unrelated papers.
- Borrow the organization of a supplied example, not its wording, scientific claims, components, datasets, or results.

## Collaboration and Editing

- Discuss the logic before a major rewrite when the user is still developing the argument. Lead with one recommended formulation rather than many near-identical alternatives.
- If the user says to show an outline or draft for review first, return it in chat without editing files. An explicit “修改”, “更新”, or “替换” authorizes the agreed scope, not a rewrite of accepted neighboring content.
- During sentence-level polishing, provide the revised passage directly. Skip repeated praise and explanations unless the technical meaning changes or the user asks for analysis.
- Preserve approved wording and paragraph boundaries. Do not restore expressions or standalone paragraphs that the user has removed.
- After an authorized local edit, verify in proportion to the change and give a concise summary and output link. Do not automatically open source files or PDFs.
- Store stable, explicit preferences narrowly. A one-off instruction about a sentence is not automatically a universal ban or requirement.

## Language and Typography

- Use Chinese for discussion and working-draft prose unless English is requested. Keep section/subsection headings in English, including the preferred heading `Motivation and Contribution`.
- Keep table captions and contents, algorithm captions, and pseudocode in English by default. A request to translate a heading does not authorize translating its body.
- Use established technical terms directly in English when following the user's bilingual style. Introduce the current topic's acronym at first use and reuse it consistently. Do not force terms from an earlier paper into a new one.
- Capitalize an English word when it begins a sentence. For an IEEE introduction with an initial-cap treatment, capitalize the first letter and use the template's drop-cap mechanism, for example `\IEEEPARstart{S}{pecific}` when that is the actual opening word.
- Prefer plain, natural Chinese, clear subjects, familiar verbs, and short complete sentences. Each sentence should have one main purpose, and the previous sentence should supply the reason for the next.
- Avoid colons, semicolons, and em dashes in prose and explanations. Preserve punctuation required by code, equations, reference titles, or the venue template.
- Avoid empty announcements such as “成为关键问题”, “亟待解决的重要挑战”, and “具有重要意义” when the concrete problem or benefit already makes the point.
- Avoid “在此基础上” and “基于上述设计”. Use substantive subjects and causal links. “结合上述分析，本文提出……” is acceptable for the framework summary.
- Do not use “首先”“其次” to replace an actual reasoning chain. Avoid repeating “本文” or “提出” in every sentence or contribution.
- Prefer the actual capability being improved over a vague claim such as “提升实用性”. Describe a concrete construction or operation instead of relying on labels such as “继承关系”.
- Do not insert coordinate-system language as a rhetorical explanation when it is not needed. Preserve precise mathematical terminology when technically necessary.
- In the main text, state mathematical results in natural prose followed by the necessary equations and derivation. Avoid numbered theorem/proposition labels such as “命题 1” unless formal numbering is needed for later reference; retain the assumptions and proof logic when simplifying the presentation.
- Avoid unnecessary “旨在” when an effect is already supported and can be stated directly. Do not turn an intended or conditional effect into a proven result merely to remove hedging.
- Explain different requirements concretely. Do not automatically append “两者存在矛盾” or “单一结构难以兼顾”, especially after the user has removed them. A difference in objectives is not itself proof of incompatibility.
- Put necessary assumptions or qualifications beside the claims they govern, briefly. Avoid repeatedly interrupting the argument with unrelated boundary discussions. Removing a redundant caveat does not strengthen the underlying claim.

## Paragraphs and Contributions

- Keep a continuous causal analysis together unless its function changes or readability requires a split. Do not start a new paragraph merely because a theory name or a training-stage phrase appears.
- In methods, explain why the key design choice is needed before or alongside its construction. Prefer a few connected paragraphs and reuse Preliminary rather than reproving established properties.
- Prefer compact mathematical pseudocode to operation-by-operation checklists. Defined reusable operators and matrix expressions are welcome when they reduce length without hiding the method. Requests for a more sophisticated algorithm mean greater mathematical information density, not gratuitous complexity.
- Put the purpose-led opening of `Motivation and Contribution` in its own short paragraph.
- Keep “本文的主要贡献如下。” at the end of the framework-summary paragraph, immediately before the contribution list.
- Default to three contributions with distinct functions: problem and overall solution, concrete method innovation, and experimental verification. Vary opening verbs naturally.
- Keep the organization paragraph separate after the contribution list. Check actual section numbers and contents rather than copying the reference article's roadmap.
- Treat paragraph and sentence counts as defaults. Preserve logical functions rather than padding text to meet a quota.
- In Related Work, default to one continuous paragraph per thematic subsection with broadly balanced coverage. Use changes in problems, conditions, or mechanisms to connect studies; choose a different paragraph structure when the user or actual content calls for it.

## Citations and Evidence

- When naming a specific work, use the first author's surname followed by `et al.` and the citation immediately after it, for example `Fu et al.~\cite{key} 提出……`. Do not alternate with “Fu 等”. General claims can use citation-only attribution.
- Prefer directly relevant recent work from strong journals or conferences, while retaining foundational sources where needed. Do not substitute a newer but less relevant citation just for recency.
- Attach references to the exact claim they support. Avoid repeatedly using the same source for unrelated claims or adding redundant references to a simple statement.
- In Related Work, prioritize relevant studies not already developed in the Introduction. Reuse foundational or closely related sources when necessary, adding a new technical comparison or angle rather than repeating their earlier description. Citation variety must not displace the closest work.
- For a brief “受……研究启发” statement, prefer one directly relevant reference when sufficient. Explain the ensuing action and its purpose instead of inserting a detached literature tutorial.
- Separate established foundations from the proposed construction. Do not frame the whole method as a restatement of one cited work, and do not remove necessary attribution to manufacture novelty. Closely related work must still be discussed accurately.
- Keep result statements concise. Omit scoring details and numerical inventories from the abstract unless requested or central to the claim. “SOTA” may be used as a concise term when supported by the actual comparison and scope.
- Distinguish intended effects, interpretations, experiments, and proved statements. Do not manufacture incompatibility, convergence acceleration, universal guarantees, superiority, or significance.
- Specify each baseline's evaluation/decision rule when relevant. Choose it from the method or a validation-only protocol, never because its test result is weaker.

## Maintaining This Profile

- Add only reusable preferences explicitly stated or repeatedly confirmed by the user.
- Move project-specific facts into a clearly scoped reference rather than expanding universal instructions.
- The latest user preference supersedes an older conflicting preference. Preserve scientific accuracy and explain conflicts briefly instead of storing an inaccurate rule.