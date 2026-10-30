# User-Approved Scientific Figure Style

Use for score distributions, ROC comparisons, and line plots with uncertainty bands. These are reusable presentation defaults, not a requirement to study OSR or use a particular dataset, score, client, method, or seed. Current requests and venue requirements take precedence.

## Shared layout and typography

- Start from the executable templates in [visual-template-kit.md](visual-template-kit.md). Their `approved_plot_style.py` records the concrete dimensions, palettes, fonts, legends and line widths of the accepted figures. Do not silently replace them with seaborn/default themes or a new implementation. The original figure-specific overrides take precedence over generic ranges below.

- Use white backgrounds, thin axes, restrained color, and light grids only where they aid reading. No decorative backgrounds, 3-D effects, or large titles inside panels.
- Use consistent English axis labels, legends, and figure captions, even with Chinese body text. Match the manuscript's typography; Times-compatible serif text and STIX mathematics are suitable starting points.
- Prefer four horizontally aligned panels across the paper's two columns when four related plots are requested. Align plotting areas, axis labels, and panel labels. Do not superimpose unrelated metrics just to fit one figure.
- Put `(a)`, `(b)`, `(c)`, `(d)` centered below their respective panels, close to the x-axis labels. An approximately 4 pt gap below the rendered x-axis-label bounding box is a useful starting point. Avoid large fractional offsets that create excessive whitespace.
- Design at final publication width, approximately 7.0–7.2 inches for many two-column templates. Start with 7–9 pt labels, 6–8 pt ticks/legends, and 0.8–1.5 pt curves. Adjust panel count or spacing before shrinking labels further.
- Export vector PDF for LaTeX, SVG for later editing, and a high-resolution PNG preview. Preserve source scripts and source data. Do not use image generation or hand-drawn curves for measured results.

## Score distribution plots

- Overlay the two distributions in each panel. For ID/OOD examples, use blue solid ID and red dashed OOD curves, with matching low-opacity fills around 0.12–0.18. Keep these identities consistent across panels.
- Place a separate compact legend in the **upper-left corner of each distribution panel**. Use a white or nearly opaque white background and a thin light border if needed.
- Label the x-axis with the actual score and the y-axis `Density` for probability-density estimates. Do not confuse density with sample counts or peak-normalize curves without an explicit methodological reason and label.
- Do not annotate AUROC values or other metric boxes inside the distribution plots by default. Let the figure show overlap and separation; numerical comparisons belong in tables or discussion.
- Derive histograms or KDE curves from real per-sample scores. Record the binning/bandwidth rule, preserve tails, and use a consistent estimation procedure across groups. KDE smoothing is for visualizing a distribution, not altering test scores.
- Preserve score direction and scale. Do not independently shift, rescale, or trim groups to make separation look stronger. Shared axis limits are preferable for panels intended for direct scale comparison; if different ranges are needed, keep ticks explicit.

## ROC comparison plots

- Include the requested comparison methods, with stable colors and line styles across panels. Use a red solid line, slightly thicker than baselines, for the proposed method by default.
- Put a compact legend **inside the lower-right corner** of each ROC panel. Show method names only, without AUROC numbers. Keep method names consistent with the paper's tables, including score suffixes only when applicable.
- Use `FPR` on the horizontal axis and `TPR` on the vertical axis, spanning 0–1. A faint diagonal chance line and a gray dashed `TPR = 0.95` line are useful when relevant to the reported operating point.
- Avoid zoom insets unless requested or necessary to resolve a meaningful difference. Keep the main plot readable at publication size.
- Compute empirical ROC points from raw labels and scores. Do not smooth away crossings or construct curves from a target AUROC. Verify positive-class conventions, score orientation, test splits, and sample counts across methods before comparing curves.
- A single-run illustration is distinct from a multi-run mean. Keep the illustrated seed and provenance available in the surrounding text or reproducibility record when omitted from a compact caption. Never present a chosen run as the aggregate result, select a favorable run autonomously, or modify curves to enforce a ranking.

## Line plots with shaded uncertainty bands

- Show a mean line with visible markers and a matching translucent uncertainty band, not bars. Use the observed parameter settings on the x-axis, without inventing intermediate observations.
- Prefer one horizontal panel per metric. For OSR studies using the approved four-metric layout, order them `FPR95` ↓, `AUROC` ↑, `AUPR-IN` ↑, `AUPR-OUT` ↑, omitting accuracy unless requested. Other tasks must use their own relevant metrics.
- Distinguish panels with a restrained palette, such as blue, orange, green, and purple, and different marker shapes. Hollow markers and pale bands keep the curves clear. When curves represent methods rather than metrics, retain each method's colors across figures.
- Use a thin gray vertical dashed line for an established default parameter value when useful. Do not imply it was chosen independently of test results if that is not the actual protocol.
- Compute uncertainty from repeated runs, not from a single run or fabricated deviations. For client-averaged metrics, average clients within each run before calculating the across-run mean and sample SD (`ddof=1`). Use a different aggregation order only when the study specifies it.
- State whether the band is SD, SE, or a confidence interval and how many runs it summarizes. Do not infer statistical significance from overlap alone. Preserve computed bounds; if a physical axis limit clips a band, keep the underlying values unchanged and the convention clear.

## Captions, placement, and verification

- Use the manuscript's normal `\caption` and `\label`, following the accepted Fig. 1 caption style. Keep captions English and concise, identifying the comparison and panel mapping. Do not repeat all experimental settings, seed details, score explanations, or table values in the caption when they are already accessible in the text.
- For uncertainty plots, retain the concise definition of the line and band. Caption brevity must not leave the uncertainty statistic ambiguous.
- Place figures near their first discussion, preferably as full-width top floats for a four-panel row. Check the compiled PDF rather than relying on source order, and keep result figures out of the references when practical.
- Verify numerical invariance for layout-only edits. Keep raw scores, per-run results, plotting summaries, and generation scripts traceable. Update a generator when editing a generated figure rather than patching only its exported image.
- Inspect the compiled page at final scale for clipped ticks, overlapping legends, unreadable text, excessive caption gaps, and panel-label alignment. Do not automatically open the manuscript or preview for the user after editing.