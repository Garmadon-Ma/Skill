# User-Approved Paper Table Style

Use this style for the user's research papers across topics. The approved example is the OSR-FETF comparison table, but its method selection, metrics, data, and client groups are not universal requirements. Explicit current instructions and mandatory venue formatting take precedence.

## Caption hierarchy

- Use a real LaTeX `\caption` and `\label`, not manually typed table numbers or a screenshot.
- Prefer a single centered line with a colon, for example `TABLE II: OVERALL OSR PERFORMANCE.` Keep the title short rather than reducing the font to force it onto one line. This supersedes the former two-line preference. Mandatory venue formatting takes precedence.
- In a 10 pt working draft, use 10 pt regular-weight type for the caption. Avoid the tiny small-cap title appearance of the previous draft. This is a personal working-draft preference, not an IEEE requirement.
- Keep the title to a short descriptive phrase. Put neither the full evaluation protocol nor an explanation of every metric in it.
- Apply caption changes locally to the intended table or table family. Do not accidentally change figure or algorithm captions. If IEEEtran's original caption formatter has been restored in the manuscript, `\captionsetup` alone may not take effect. Inspect the active formatter and verify the rendered PDF.

## Alignment and density

- Center the entire Method column horizontally, including its heading, method names, citation markers, and proposed-method row. Use `c`, not `l`, for short method cells.
- Vertically center Method across all levels of a grouped header. For a two-level header, place `\multirow{2}{*}{\textbf{Method}}` in the first row and leave the corresponding second-row cell empty. Booktabs rule spacing may need a small optical adjustment after rendering.
- Center numerical columns. With tabularx, prefer a locally scoped `\renewcommand{\tabularxcolumn}[1]{m{#1}}` when vertical centering is needed.
- Show mean and standard deviation on the same line by default. A compact form is `$94.09\,{\scriptstyle\pm1.05}$` as a typography example only, never as reusable data. Do not split every cell into two lines when the table is wide enough for inline values.
- Keep body rows uniform and compact without touching rules or clipping text. For a dense full-width table, the approved starting settings are 8 pt body type with 9.6 pt baseline spacing, `\tabcolsep=3pt`, and `\arraystretch=1.20`. Adjust to content rather than forcing these values.
- Choose width by content. Use a single column for a small table and two columns for a wide comparison or repeated metric groups. Do not stretch every table across the page or shrink all text merely to force a fit.

## Rules and color

- Prefer booktabs top, middle, and bottom rules, with partial rules under group headings. Avoid a dense grid.
- Use a thin vertical separator after the Method/component block and between repeated metric groups, matching the approved tables. Do not put a vertical line between every metric column.
- Default to a white background without gray row banding. A continuous pale-blue proposed-method row is acceptable, matching the approved example. Preserve explicitly requested exceptions.
- If a highlighted row looks like disconnected colored blocks, inspect column padding and color coverage rather than adding more coloring commands.
- Bold the best and underline the second-best comparable reported means within each displayed group, with ties handled consistently. Highlighting is not evidence of statistical significance. Do not rank metrics with incompatible definitions.

## Minimal notes

- Prefer one short note, or two when abbreviations genuinely need explanation.
- Example for inline uncertainty: `Three-seed mean $\pm$ SD (\%). Bold/underline indicate best/second-best.` Replace seed count, units, and statistics with the actual protocol.
- For means alone: `Three-seed means (\%). Bold/underline indicate best/second-best.`
- Explain only otherwise-undefined abbreviations used in the table. Avoid repeating the caption, full method descriptions, the obvious row color, or information already clearly stated in the setup.
- Keep material protocol differences or limitations accessible in the text or a concise note. Shortening notes must not hide a comparison condition.

## Reproducible updates

- Use the actual renderer and local caption package linked in [visual-template-kit.md](visual-template-kit.md), not only these prose rules. The renderer supports grouped comparison tables and checkmark/cross ablations, one- or two-column width, and inline uncertainty. Reuse its parameters across new papers while replacing all study content.

- Preserve original results. If tables are generated, update the renderer and regenerate the affected tables together, rather than patching only generated LaTeX.
- Method exclusions are manuscript-specific decisions, not permanent skill rules. Preserve excluded experiments in the original records. If an exclusion is requested, synchronize the displayed rows, relevant prose, citations, and ranking marks without strengthening claims beyond the evidence.
- Before delivery, compile and inspect the actual table pages for caption hierarchy, horizontal and vertical centering, inline uncertainty, continuous shading, readable type, and overflow. Check references and numeric invariance separately.
- Do not automatically open the manuscript or PDF after editing unless requested.