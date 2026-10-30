# Executable table and plot templates

Use these bundled files when reproducing this user's paper appearance. Style prose alone is insufficient. These are extracted/adapted from the accepted OSR-FETF generators on 2026-10-10, not generic defaults. They carry no old paper's results, paths, method list, or favored seed.

## Files and workflow

- `scripts/approved_plot_style.py` owns fonts, colors, line widths, legend formatting and panel-label placement.
- `scripts/render_paper_figures.py` renders ROC, ID/OOD score densities and metric sensitivity bands from **new-study data**.
- `scripts/render_paper_table.py` renders grouped comparison and check/cross ablation tables.
- `assets/approved-paper-tables.sty` supplies the actual one-line caption and compact table style, without restyling figures/algorithms.
- `scripts/test_visual_templates.py` generates **synthetic smoke-test fixtures only**, validates statistical invariants and produces isolated preview examples. Never use its generated values as research results.

Copy the needed scripts and `.sty` into the new project, retaining `approved_plot_style.py` beside the figure renderer, or execute them directly from the skill folder. Python needs numpy, pandas, matplotlib, scipy and scikit-learn for figures. The table renderer is standard-library only. Use an existing runtime with these dependencies. Do not run an original manuscript's script with its original data to make a new article's results.

Create a project-specific configuration and run

```text
python render_paper_figures.py figure-config.json
python render_paper_table.py table-config.json
```

Input/output paths resolve relative to the configuration, not the working directory. Each plot exports PDF, SVG, PNG and an audit JSON containing inputs, hashes, computed statistics and software versions. Tables export `.tex` plus an audit JSON. Keep these with the new manuscript. Add `\usepackage{approved-paper-tables}` to the LaTeX preamble and `\input{generated-table.tex}` in the body. If xcolor is already loaded, enable its `table` option in the original load or pass the option before loading it. If the manuscript already overrides captions, reconcile that explicitly rather than layering conflicting hooks.

Use the kit by default instead of rewriting plot aesthetics. Adapt its data input layer or config when new study content differs. Preserve the style constants unless the user or venue asks for a different appearance. Compile and visually inspect at publication size. Reusing code improves consistency but font availability, panel count and long labels still require inspection. Never promise pixel-identical output across arbitrary environments.

## Score data and figure configuration

CSV columns are `panel,method,run,sample_id,label,score`.

- `label=1` is the explicitly declared positive population, normally ID; `label=0` is the other population.
- Each method/run must contain the same test sample IDs and labels within a ROC panel. IDs must be unique within method/run.
- `score` is the actual measured detector output. `higher_is_positive` is required per method. Set it from its definition, not by inspecting whether AUROC is below 0.5. Negation is used only for a declared lower-is-positive detector; it is recorded in the config/audit.
- The methods list controls both display order and stable styling. `label` can differ from the stored method key. Do not remove a scientifically relevant scoring distinction from the study's protocol documentation.
- For a chosen illustration run set `runs` in the panel explicitly. Otherwise all supplied runs are used. No automatic best-seed selection.

Minimal config shape (replace identifiers and paths with the current study)

```json
{
  "data": "scores.csv", "output": "figures/diagnostics",
  "methods": [
    {"key": "baseline", "label": "Baseline", "higher_is_positive": true},
    {"key": "proposed", "label": "Ours", "higher_is_positive": true, "proposed": true}
  ],
  "panels": [
    {"type": "density", "key": "A", "method": "proposed", "label": "Dataset A", "xlabel": "Score", "runs": ["0"]},
    {"type": "density", "key": "B", "method": "proposed", "label": "Dataset B", "xlabel": "Score", "runs": ["0"]},
    {"type": "roc", "key": "A", "label": "Dataset A"},
    {"type": "roc", "key": "B", "label": "Dataset B"}
  ]
}
```

Use only ROC or only density panel entries for a dedicated figure. One to four horizontal panels are supported; `width` overrides publication width. ROC legends are lower-right, density legends upper-left, with no AUROC boxes. Proposed ROC is red; ID is blue solid and OOD red dashed. Captions must say whether curves are single-run or across-run means, and whether bands are SD. Do not interpret a selected run as an aggregate result.

ROC points are calculated from raw scores. Across-run mean ROC uses the union of empirical FPR knots and retains both sides of vertical segments, so its trapezoidal area equals the mean run AUROC. The renderer checks this. Bands are pointwise sample SD; the plot clips to [0,1] while the audit retains mean and unmodified SD.

Density uses Scott KDE by default, a shared evaluation grid extending four kernel SDs beyond all observed scores in the panel, and no per-class normalization/shift. Override `bandwidth` only with a documented estimation choice. One run gives a standard two-density plot. Multiple runs give the mean of per-run densities rather than pooled samples. `"band": true` adds across-run sample-SD bands, not a fabricated single-run uncertainty. `labels: ["Positive", "Negative"]` adapts the population names for a non-OSR topic. Coordinate changes/negation must be reflected in the score label and audit.

## Sensitivity/uncertainty line figures

CSV columns are `panel,metric,x,run,group,value`. `group` may be a client, dataset or a single constant when there is no within-run averaging. Each parameter setting must have the same run/group coverage. Values are averaged over groups within each run, then mean and sample SD are computed across runs. Input percentages must already be in percent units; the renderer does not guess a scale.

Each panel uses

```json
{"type":"line", "key":"sensitivity", "metric":"metric_key",
 "label":"", "xlabel":"Parameter", "ylabel":"Metric (%)", "default_x":0.5}
```

Use these entries in a config with `data`, `output`, `panels`, as above. `default_x` is optional and must reflect the study's declared default. Four panels use the accepted 7.05 by 2.35 inch layout, blue/orange/green/purple, hollow markers and 0.14-opacity bands. Other topics select their own metrics; an OSR configuration normally orders FPR95, AUROC, AUPR-IN, AUPR-OUT. Do not force this metric set on another field.

## Table configuration

Required keys are `caption`, `label`, `output`, `groups`, `metrics`, `rows`. Optional `wide` defaults to true. Use false for one-column tables rather than stretching small tables across two columns.

```json
{
 "caption":"Comparison Results.", "label":"tab:comparison", "output":"tables/comparison.tex", "wide":true,
 "groups":[{"key":"test_a","label":"Dataset A"},{"key":"test_b","label":"Dataset B"}],
 "metrics":[{"key":"error","label":"Error","direction":"min"},{"key":"score","label":"Score","direction":"max"}],
 "rows":[], "note":""
}
```

Populate `rows` from actual results, never this document. Each row has `name`, optional `citation` (BibTeX key) and `proposed` (boolean), and `values[group_key][metric_key]`. A cell is either a real mean or `[real_mean, real_SD]`. No SD is invented when absent. `note` is literal plain text and must state the actual uncertainty/run protocol when needed. The renderer defaults to 2 decimals, bold best and underline second-best distinct displayed means, tied ranks shared. Set `rank:false` when cells are not directly comparable. Ranking conveys no significance.

For ablations, add `components:[{"key":"module_a","label":"Module A"}, ...]` and each row's boolean `components` map. This replaces Method/Variant with centered check/cross columns. Keep the same `groups`, `metrics`, values and uncertainty scheme. Component names, metrics and group counts are study-specific. Component columns use the approved 0.67 relative width, with remaining width assigned to metrics. A metric's optional `width_weight` gives longer labels more room (the accepted four-metric table used 0.95, 0.95, 0.95, 1.15). A newline in a component/metric label creates a compact two-line heading. `font_size`, `baseline_skip`, and `tabcolsep` allow a documented density adjustment when needed; start at 8, 9.6 and 3 pt.

Appearance is one centered line `TABLE N: SHORT UPPERCASE TITLE.`, 10 pt caption in a 10 pt manuscript, centered Method including citations, vertically centered grouped headers, sparse group separators, white baseline rows, pale-blue proposed row, and inline mean ± SD. Use short headers before shrinking type. Do not install a new global caption style or alter existing figure captions to obtain this effect.

## Validation and visual reference

Bundled appearance references (all clearly labeled synthetic, never research data) are [diagnostic preview](../assets/style-previews/synthetic-diagnostics.png), [line preview](../assets/style-previews/synthetic-lines.png), and [table preview](../assets/style-previews/tables-preview.png). Inspect the relevant preview before rendering a new paper's tables/plots, then compare output typography, legend placement, panel spacing and caption hierarchy against it. Content and numerical curve shapes must come from the new study, not these previews.

Run `python scripts/test_visual_templates.py --out <isolated-output-directory>`. It checks direct sklearn AUROC against rendered mean ROC areas, source hashes, permutation/score orientation, multi-run averaging, table ranking, and required validation failures. It writes synthetic diagnostic and line PDFs/PNGs and a two-table LaTeX document. Compile the latter with the existing LaTeX toolchain to verify caption placement and grouped/checkmark headers. All fixture captions visibly identify synthetic test data. Keep test artifacts outside a manuscript's result directory.

The implementation preserves the accepted diagnostic figure constants from `gen_unseen_diagnostics.py`, the line figure constants from `gen_fig4_aux_weight.py`, and table dimensions/colors from the accepted comparison/ablation `.tex` outputs. The panel-label helper uses a fixed 4 pt distance below the x-label in all plot modes instead of a fractional offset. No absolute path to OSR-FETF is needed by another paper.