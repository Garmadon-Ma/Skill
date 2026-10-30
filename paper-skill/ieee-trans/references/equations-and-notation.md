# IEEE Equations, Symbols, and Cross-References

Apply this reference whenever drafting or revising mathematical content. These rules combine IEEE’s official editorial and LaTeX math guidance with a conservative notation system for machine-learning and communications papers. A target Transactions template or editor instruction takes precedence.

## 1. Build a notation ledger first

Before drafting equations, record each important symbol:

| Symbol | Mathematical type and dimension | Meaning | First definition | Status |
|---|---|---|---|---|
| $x$ | scalar | sample index/time/value | Section III-A | observed/fixed/trainable |
| $\boldsymbol{x}\in\mathbb{R}^{d}$ | vector | input or feature | Section III-A | observed |
| $\boldsymbol{W}\in\mathbb{R}^{d\times C}$ | matrix | classifier/projection | Section IV-A | fixed or trainable |
| $\mathcal{D}_{\mathrm{tr}}$ | set | training dataset | Section III-A | fixed |
| $\theta$ | parameter collection | model parameters | Section IV | trainable |

Reject symbol reuse with a different type or meaning. Avoid symbols that are visually ambiguous in the selected font, especially lowercase $l$ versus 1 and $o$ versus 0. Use the same notation in text, equations, algorithms, figures, and tables.

## 2. Typography by mathematical role

| Role | IEEE-style treatment | LaTeX example |
|---|---|---|
| Scalar variable | italic lowercase | `$x$, $k$, $\lambda$` |
| Random variable | italic uppercase when this convention is used | `$X$`, with realization `$x$` |
| Vector | bold; use bold italic consistently | `$\boldsymbol{x}$`, `$\boldsymbol{\mu}$` |
| Matrix | bold uppercase | `$\boldsymbol{W}$`, `$\boldsymbol{\Sigma}$` |
| Set/dataset | calligraphic uppercase | `$\mathcal{C}$`, `$\mathcal{D}_{\mathrm{tr}}$` |
| Number system | blackboard bold | `$\mathbb{R}$`, `$\mathbb{N}$` |
| Standard function/operator | roman | `\exp`, `\log`, `\min`, `\max`, `\operatorname*{arg\,min}`, `\operatorname{diag}` |
| Acronym or word in math | roman/text | `\mathrm{ID}`, `\mathrm{out}`, `\text{otherwise}` |
| Unit | roman with a regular space after the number | `$2~\mathrm{GHz}$`, `$10~\mathrm{dB}$` |
| Variable index | italic | `$x_i$`, `$w_{c,m}$` when $i,c,m$ are indices |
| Descriptive subscript | roman | `$\mathcal{L}_{\mathrm{CE}}$`, `$N_{\mathrm{out}}$`, `$\boldsymbol{x}_{\mathrm{test}}$` |

IEEE requires variables to be italic, vectors to be bold, and functions, abbreviations, units, complete words, and descriptive subscripts/superscripts to be roman. For Greek vectors use `\boldsymbol{\mu}` rather than `\mathbf{\mu}`. Do not bold a scalar merely for emphasis.

Use a consistent roman convention for transpose and Hermitian transpose, such as `$\boldsymbol{W}^{\mathsf{T}}$` and `$\boldsymbol{W}^{\mathsf{H}}$`; do not let T or H look like scalar variables. Use `$\boldsymbol{W}^{-1}$` for an inverse.

## 3. Preferred mathematical constructions

- Norm: `$\lVert\boldsymbol{x}\rVert_2$`, not `||x||`.
- Inner product: `$\langle\boldsymbol{x},\boldsymbol{y}\rangle$`.
- Probability: `$p(\boldsymbol{x}\mid y)$` or `$\Pr\{Y=y\}$`; use `\mid`, not a raw vertical bar when conditioning.
- Expectation: `$\mathbb{E}_{(\boldsymbol{x},y)\sim\mathcal{D}}[\cdot]$`.
- Distribution: `$\mathcal{N}(\boldsymbol{\mu},\boldsymbol{\Sigma})$`.
- Indicator: define `$\mathbb{1}\{\cdot\}$` or the venue-preferred symbol once.
- Differential: use roman d, for example `$\int f(x)\,\mathrm{d}x$`.
- Custom operators: declare them with `\DeclareMathOperator` or use `\operatorname{softmax}`, never italic multi-letter strings.
- Sets: use braces for elements and state membership, e.g., `$\mathcal{Y}=\{1,\ldots,C\}$` and `$y_i\in\mathcal{Y}$`.
- Dimensions: give them at the first definition, e.g., `$\boldsymbol{W}\in\mathbb{R}^{d\times C}$`.
- Multiplication: normally use juxtaposition; use `\times` for dimensions, Cartesian products, or when needed for clarity. Do not use an asterisk as ordinary multiplication.
- Fractions: use built-up `\frac` in displayed equations; use a slash with parentheses in prose when it improves line fit.

## 4. Equation as part of a sentence

An equation must be grammatically connected to the prose.

### Incomplete lead-in: no colon

```latex
The total objective is defined as
\begin{equation}
  \mathcal{L}_{\mathrm{total}}
  = \mathcal{L}_{\mathrm{id}}
  + \lambda_{\mathrm{rx}}\mathcal{L}_{\mathrm{rx}}
  + \lambda_{\mathrm{mi}}\mathcal{L}_{\mathrm{mi}}.
  \label{eq:total_loss}
\end{equation}
```

### Complete lead-in: colon allowed

```latex
The three objectives are combined as follows:
\begin{equation}
  \mathcal{L}_{\mathrm{total}}
  = \mathcal{L}_{1}+\lambda_{2}\mathcal{L}_{2}.
  \label{eq:combined_objective}
\end{equation}
```

End a displayed equation with a period when it ends the sentence and with a comma only when the sentence continues and the comma is grammatically necessary. Do not treat display math as punctuation-free artwork.

After the display, define symbols and interpret behavior:

> where $\lambda_{\mathrm{mi}}\ge 0$ controls the disentanglement strength. Minimizing the third term reduces the estimated dependence between the two latent representations, whereas the first two terms preserve their task-specific information.

Do not write only “where all symbols have their usual meanings.”

## 5. IEEE heading hierarchy

When producing LaTeX, let the IEEE template format headings; do not imitate their font sizes manually. Use the hierarchy consistently:

- primary section: Roman numeral and uppercase heading, e.g., `I. INTRODUCTION`;
- secondary heading: capital letter and period, upper/lowercase, e.g., `A. Problem Formulation`;
- tertiary run-in heading: Arabic numeral and parenthesis, ending with a colon, e.g., `1) Datasets and Preprocessing:`;
- quaternary run-in heading: label such as `1a)` and a colon, used sparingly.

Introduction, Conclusion, and Acknowledgment are singular headings. References and Acknowledgment are not numbered. Prefer no more than three active heading levels in an ordinary method paper.

## 6. Numbering and references

- Number equations consecutively through the article unless the target Transactions explicitly permits section numbering.
- Place the parenthesized number flush right using the template; use `\label{...}` and `\eqref{...}` rather than manual numbers.
- Number only equations cited later or needed for the argument. Do not number decorative restatements.
- Use subequations `(7a)–(7c)` for tightly coupled parts when that improves referencing.
- At the start of a sentence write “Equation (7)”; elsewhere write “in (7),” “from (7),” or “substituting (7) into (8).” Avoid “Eq. (7)” when enforcing the IEEE editorial convention.
- Use “Section IV-A,” “Fig. 2,” “Table III,” and “Algorithm 1.” Capitalize “Section” and do not write “Subsection IV-A.”
- Refer to external locations as `[12, eq. (8)]`, `[12, Fig. 2]`, or `[12, Sec. IV]` rather than “equation (8) of reference [12].”
- Appendix equations may continue the article sequence; `(A1), (A2), ...` is also permissible when used consistently.

## 7. Correct LaTeX environments

Use:

- single-line unnumbered: `\[ ... \]` or `equation*`;
- single-line numbered: `equation`;
- multiline: `align` or `align*`;
- alternatives/conditions: `cases` with textual conditions in `\text{...}`.

Do not use `$$ ... $$` or `eqnarray`; IEEE’s math guide identifies both as obsolete or spacing-prone. Do not insert repeated `\;`, `\quad`, or manual spaces to fake alignment. Align at mathematical relations such as `=`, `\le`, or `\approx` using `&`.

```latex
\begin{align}
  \boldsymbol{z}_{t}
  &= (1-t)\boldsymbol{z}_{0}+t\boldsymbol{z}_{1}
     +\sigma(t)\boldsymbol{\epsilon}, \label{eq:path_a}\\
  \boldsymbol{\epsilon}
  &\sim \mathcal{N}(\boldsymbol{0},\boldsymbol{I}). \label{eq:path_b}
\end{align}
```

For cases, keep conditions roman and columns left-aligned:

```latex
\begin{equation}
  G(\boldsymbol{x})=
  \begin{cases}
    \mathrm{ID},  & \text{if } S(\boldsymbol{x})\ge \tau,\\
    \mathrm{OOD}, & \text{otherwise}.
  \end{cases}
  \label{eq:decision}
\end{equation}
```

Use `\left(`, `\right)`, `\left[`, and `\right]` when delimiters must grow. Do not allow a line break to leave unmatched or visually misleading fences.

## 8. Long equations in two columns

- Compose in the actual two-column IEEE template early and check every display against one-column width.
- First simplify notation or introduce a well-defined intermediate quantity.
- If a break is needed, break at a relation or binary operator and align continued lines consistently; preserve logical grouping inside delimiters.
- Do not reduce equation font size locally merely to force a fit.
- Use a page-wide equation only when semantic readability cannot be preserved in one column and the target template supports it.
- Put limits above/below large operators in ordinary display math, but allow LaTeX to place limits to the side when the operator occurs inside a fraction.

## 9. Loss functions and optimization statements

For each new loss, supply four items:

1. **Object:** what data and representation it acts on.
2. **Formula:** normalized expectation or finite-sample average with valid index bounds.
3. **Direction:** what minimizing/maximizing it pushes together, separates, suppresses, or calibrates.
4. **Optimization scope:** which parameters receive gradients and which anchors/prototypes/statistics remain fixed.

Example pattern:

```latex
\begin{equation}
  \mathcal{L}_{\mathrm{ctr}}
  = \frac{1}{2N}\sum_{i=1}^{N}
    \left\lVert
      f_{\theta}(\boldsymbol{x}_{i})-\boldsymbol{w}_{y_i}
    \right\rVert_{2}^{2},
  \label{eq:center_loss}
\end{equation}
```

Then state whether `$\boldsymbol{w}_{y_i}$` is fixed or trainable and explain the induced feature geometry. Do not claim that a loss “guarantees” separation unless a result proves it under explicit assumptions; “encourages,” “promotes,” or “is designed to” is usually accurate.

## 10. Symbols, units, numbers, and ranges

- Insert a leading zero for decimals: `0.05`, not `.05`.
- Use numerals with units and a regular space: `100 MHz`, `20 ms`, `2 A`.
- Keep units roman. For compound units use a center dot, slash, or negative exponent consistently, e.g., `$\mathrm{V}\cdot\mathrm{s}$`, `V/s`, or `$\mathrm{V}\cdot\mathrm{s}^{-1}$`.
- Use an en dash for a closed range (`10–20 dB`) or write “from 10 to 20 dB”; never “from 10–20 dB.”
- Repeat the percent sign where needed for clarity in a range and always escape it in LaTeX: `20\%–30\%`.
- Distinguish an absolute percentage-point gain from a relative percentage gain.
- Use baseline ellipses correctly: `$x_1,x_2,\ldots,x_n$`; use centered dots for operations: `$x_1+x_2+\cdots+x_n$`.

## 11. Abstract, title, and nomenclature constraints

- Avoid mathematical symbols in the title and Abstract; IEEE warns that they may not display reliably in indexing systems.
- The Abstract is one paragraph and must not contain numbered equations, numbered references, or footnotes.
- When symbol density is high, add a Nomenclature after the Abstract and Index Terms or a notation table near Preliminary, subject to the target journal template.
- A Nomenclature entry gives the symbol/acronym and a definition; do not write an equality sign between the symbol and prose definition.
- Even with a notation table, give local reminders for symbols whose role, dimension, or fixed/trainable status is essential to an equation.

## 12. Formula audit checklist

For every displayed equation verify:

- it is needed and cited or interpreted;
- its lead-in is grammatically complete;
- variables are italic and vectors/matrices bold;
- standard functions and descriptive subscripts are roman;
- dimensions, domains, indices, and summation limits are valid;
- all symbols are defined before or immediately after first use;
- fixed, observed, sampled, and trainable quantities are distinguishable;
- punctuation matches the surrounding sentence;
- numbering and `\label`/`\eqref` are consecutive and unique;
- the equation fits a column without tiny fonts or broken fences;
- the following prose states its mechanism, not merely repeats its name.

## Official IEEE sources

- [IEEE Math Typesetting Guide for LaTeX Users](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Math-Typesetting-Guide-for-LaTeX-Users.pdf)
- [IEEE Editorial Style Manual for Authors](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Editorial-Style-Manual-for-Authors.pdf)
- [IEEE Author Center: Structure Your Article](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/structure-your-article/)