# Conclusion Writing Outline

Use this topic-independent structure when drafting or revising the user's conclusion. Transfer the organization of approved examples, not their method names, claims, or future topics. Use Chinese working-draft prose and the English heading `Conclusion` unless requested otherwise.

## Structure and sentence functions

Write one connected paragraph, usually six to eight sentences. Merge short functions or split a dense mechanism sentence as needed; the functions matter more than the count.

1. **Return to the actual problem.** Identify the task and the condition studied, and state what capability the work seeks to provide. Start at the paper's specific scope rather than repeating broad importance claims from the Abstract.
2. **Summarize the difficulty.** Briefly explain why the existing approach or straightforward alternative is insufficient in that condition. Reuse the established diagnosis; do not introduce a new criticism of prior work.
3. **State the overall solution.** Name the method and its central design in one sentence. Connect it directly to the preceding difficulty, for example with “为此”, rather than listing modules without a reason.
4. **Explain the main mechanisms.** Use one or two sentences to say what the distinctive components do and how their roles work together. Prefer concrete operations and supported consequences over labels such as “创新框架” or “具有继承关系”.
5. **Close the method workflow when needed.** If adaptation, inference, or a decision rule is essential to the paper, briefly explain how the learned representation is used. Omit this sentence when it only repeats the preceding mechanism.
6. **Summarize the evidence.** State what the performance comparisons and relevant ablations support. Keep it concise, without a list of metric values, dataset details, or citations. Stronger claims, including SOTA or faster convergence, require corresponding evidence in the paper.
7. **End with one concrete future direction.** Identify the next capability or condition to study and explain how it extends the present work. Use the user's chosen next topic when supplied. Do not invent a proposed solution or present future work as an achieved result.

The progression is `studied problem -> remaining difficulty -> overall solution -> component roles -> experimental support -> next research capability`. It should read as a closing explanation, not another abstract or contribution list.

## Wording preferences

- Use concise, natural Chinese and explicit subjects. It is fine to start with “本文围绕……”, but do not repeat “本文提出” in every sentence.
- Avoid “首先”“其次” as substitutes for causal links. Follow the personal style profile's avoidance of colons, semicolons, and em dashes in prose.
- State what each component changes, not merely its name. Keep fixed constructions, learned modules, and inference rules distinct without reintroducing formulas or implementation settings.
- Summarize the work rather than claiming to provide an overview or survey just because a reference conclusion uses that opening. Mention a survey only if the paper actually contributes one.
- Keep result statements proportionate to the experiments. Do not turn a geometric property into a convergence guarantee or a detection guarantee.
- Do not end with a catalogue of unperformed experiments or repeated defensive disclaimers. Preserve any essential qualification concisely, then give the substantive next direction. Do not erase a known limitation merely to sound confident.
- Avoid a vague final promise such as “进一步提升鲁棒性和实用性” without naming what will be studied and what capability it adds.
- Do not add new citations, equations, results, or unexplained technical claims. Reuse established terms, but do not copy the Abstract verbatim.

## Example of a future-work connection

For an open-set recognition paper whose next topic is novel class discovery, the closing logic can be “from rejecting unknown samples to discovering and learning their underlying categories”. This is an example of a concrete capability extension, not a default future direction for all papers. Other topics should derive their ending from their own results and the user's stated research plan.

## Before updating a manuscript

Check that the paragraph closes the same problem introduced earlier, that each claimed effect already has support, and that the future direction is clearly prospective. Respect a request to show a draft for approval before replacing text. Updating this writing guide alone does not authorize rewriting an existing manuscript.