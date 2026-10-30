"""Render real score/metric CSVs using the user's approved figure style.

Usage: python render_paper_figures.py config.json
See references/visual-template-kit.md for schemas. Tests use synthetic data ONLY.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde
from sklearn.metrics import roc_curve

import approved_plot_style as style


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def integrate(y, x):
    return float(np.trapz(y, x))


def align_roc(x, y, grid):
    """Preserve empirical vertical segments and trapezoidal AUROC exactly."""
    if not (np.isfinite(x).all() and np.isfinite(y).all()
            and np.all(np.diff(x) >= 0) and np.all(np.diff(y) >= 0)
            and x[0] == y[0] == 0 and x[-1] == y[-1] == 1):
        raise ValueError('Invalid empirical ROC')
    knots, first, counts = np.unique(x, return_index=True, return_counts=True)
    positions = np.searchsorted(grid, knots)
    if not np.array_equal(grid[positions], knots):
        raise ValueError('Union grid must contain every empirical FPR knot')
    values = np.repeat(np.interp(grid, x, y), 2)
    values[2 * positions] = y[first]
    values[2 * positions + 1] = y[first + counts - 1]
    if not np.isclose(integrate(values, np.repeat(grid, 2)), integrate(y, x), atol=1e-12, rtol=0):
        raise AssertionError('ROC alignment changed AUROC')
    return values


def stats(values):
    values = np.asarray(values)
    return values.mean(axis=0), values.std(axis=0, ddof=1) if len(values) > 1 else None


def score_panel(data, panel, cfg):
    rows = data[data.panel == str(panel['key'])].copy()
    if 'runs' in panel:
        rows = rows[rows.run.isin([str(r) for r in panel['runs']])]
    if rows.empty:
        raise ValueError(f'No scores for panel {panel["key"]}')
    if not rows.label.isin([0, 1]).all() or not np.isfinite(rows.score).all():
        raise ValueError('Scores must be finite and label must be 0 or 1')
    # Orientation is a declared method property, never inferred from test AUROC.
    for method in cfg['methods']:
        if method['higher_is_positive'] is False:
            rows.loc[rows.method == method['key'], 'score'] *= -1
    return rows


def draw_roc(ax, rows, cfg, audits):
    curves = {}
    reference = {}
    methods = cfg['methods']
    expected_runs = set(rows.run.unique())
    for method in methods:
        sub = rows[rows.method == method['key']]
        if set(sub.run.unique()) != expected_runs:
            raise ValueError('Every ROC method must have the same run coverage')
        for run, r in sub.groupby('run', sort=True):
            if r.sample_id.duplicated().any() or set(r.label) != {0, 1}:
                raise ValueError('Need unique sample IDs and both classes per run')
            labels = r.set_index('sample_id').label.sort_index()
            if run in reference and not labels.equals(reference[run]):
                raise ValueError('Methods do not use the same test samples/labels')
            reference[run] = labels
            x, y, _ = roc_curve(r.label, r.score, pos_label=1, drop_intermediate=False)
            curves[method['key'], run] = (x, y)
    grid = np.unique(np.concatenate([x for x, _ in curves.values()]))
    xplot = np.repeat(grid, 2)
    ax.plot([0, 1], [0, 1], color='#BDBDBD', ls=':', lw=.55)
    for i, method in enumerate(methods):
        runs = [curves[method['key'], r] for r in sorted(expected_runs)]
        mean, sd = stats([align_roc(x, y, grid) for x, y in runs])
        areas = [integrate(y, x) for x, y in runs]
        if not np.isclose(integrate(mean, xplot), np.mean(areas), atol=1e-12, rtol=0):
            raise AssertionError('Mean ROC area differs from mean run AUROC')
        ours = method.get('proposed', False)
        color = method.get('color', style.PROPOSED if ours else style.BASELINES[i % 7])
        ls = method.get('linestyle', '-' if ours else style.LINESTYLES[i % 7])
        if sd is not None:
            ax.fill_between(xplot, np.clip(mean-sd, 0, 1), np.clip(mean+sd, 0, 1),
                            color=color, alpha=.10, linewidth=0, zorder=1)
        ax.plot(xplot, mean, color=color, ls=ls, lw=1.2 if ours else .8,
                label=method.get('label', method['key']), zorder=5 if ours else 3)
        audits.append({'method': method['key'], 'runs': sorted(expected_runs),
                       'run_auroc': areas, 'mean_auroc': integrate(mean, xplot),
                       'fpr': xplot.tolist(), 'mean': mean.tolist(),
                       'sd': None if sd is None else sd.tolist()})
    if cfg.get('operating_tpr', .95) is not None:
        level = cfg.get('operating_tpr', .95)
        ax.axhline(level, color='#8C8C8C', ls='--', lw=.6, label=f'TPR = {level:g}')
    ax.set(xlim=(-.015, 1.015), ylim=(-.015, 1.035), xlabel='FPR', ylabel='TPR')
    ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
    ax.grid(color='#E9E9E9', lw=.35)
    style.legend(ax)


def draw_density(ax, rows, panel, audits):
    rows = rows[rows.method == panel['method']]
    if rows.empty:
        raise ValueError('No scores for selected density method')
    models = {}
    lo, hi = np.inf, -np.inf
    for run, r in rows.groupby('run', sort=True):
        if set(r.label) != {0, 1} or r.sample_id.duplicated().any():
            raise ValueError('Need both classes and unique sample IDs per run')
        for positive in (1, 0):
            v = r[r.label == positive].score.to_numpy()
            if len(v) < 2 or np.ptp(v) == 0:
                raise ValueError('KDE requires at least two nonidentical scores')
            model = gaussian_kde(v, bw_method=panel.get('bandwidth', 'scott'))
            models[run, positive] = model
            margin = 4 * float(np.sqrt(model.covariance[0, 0]))
            lo, hi = min(lo, v.min()-margin), max(hi, v.max()+margin)
    x = np.linspace(lo, hi, 768)
    maximum = 0
    labels = panel.get('labels', ['ID', 'OOD'])
    for index, positive in enumerate((1, 0)):
        _, color, ls = style.DENSITY[index]
        mean, sd = stats([model(x) for (run, cls), model in models.items() if cls == positive])
        ax.fill_between(x, mean, color=color, alpha=.14, linewidth=0)
        if sd is not None and panel.get('band', False):
            ax.fill_between(x, np.maximum(0, mean-sd), mean+sd, color=color, alpha=.14, linewidth=0)
        ax.plot(x, mean, color=color, ls=ls, lw=1, label=labels[index])
        maximum = max(maximum, float((mean + (sd if sd is not None and panel.get('band', False) else 0)).max()))
        audits.append({'label': labels[index], 'runs': sorted(rows.run.unique()),
                       'bandwidth': panel.get('bandwidth', 'scott'), 'x': x.tolist(),
                       'mean': mean.tolist(), 'sd': None if sd is None else sd.tolist()})
    ax.set(xlim=(lo, hi), ylim=(0, maximum*1.06), xlabel=panel.get('xlabel', 'Score'), ylabel='Density')
    ax.xaxis.set_major_locator(MaxNLocator(nbins=3)); ax.yaxis.set_major_locator(MaxNLocator(nbins=3))
    style.legend(ax, density=True)


def draw_line(ax, data, panel, index, audits):
    rows = data[(data.panel == str(panel['key'])) & (data.metric == panel['metric'])]
    if rows.empty or rows.duplicated(['x', 'run', 'group']).any() or not np.isfinite(rows[['x', 'value']]).all().all():
        raise ValueError('Invalid/missing line records, or duplicated x/run/group')
    coverage = [set(zip(r.run, r.group)) for _, r in rows.groupby('x')]
    if any(c != coverage[0] for c in coverage):
        raise ValueError('Parameter settings must have matching run/group coverage')
    per_run = rows.groupby(['x', 'run'], sort=True).value.mean()
    means, sds, xs = [], [], []
    for x, r in per_run.groupby(level='x', sort=True):
        mean, sd = stats(r.to_numpy())
        xs.append(x); means.append(float(mean)); sds.append(None if sd is None else float(sd))
    mean = np.array(means)
    sd = np.array(sds) if all(s is not None for s in sds) else None
    color = panel.get('color', style.METRICS[index % 4])
    if sd is not None:
        ax.fill_between(xs, mean-sd, mean+sd, color=color, alpha=.14, linewidth=0, zorder=1)
    ax.plot(xs, mean, color=color, marker=style.MARKERS[index % 4], markersize=3.5,
            lw=1.4, markerfacecolor='white', markeredgewidth=1.1, zorder=3)
    if 'default_x' in panel:
        ax.axvline(panel['default_x'], color='#8C8C8C', ls=(0, (3, 3)), lw=.7, zorder=0)
    ax.set(xlabel=panel['xlabel'], ylabel=panel['ylabel'])
    ax.set_xticks(xs)
    if 'ylim' in panel:
        ax.set_ylim(panel['ylim'])
    ax.yaxis.set_major_locator(MaxNLocator(nbins=4, min_n_ticks=3))
    ax.grid(axis='y', color='#D9DDE2', lw=.5, alpha=.7)
    audits.append({'x': xs, 'mean': means, 'sd': sds,
                   'runs': sorted(rows.run.unique()), 'averaging': 'group mean within run, then run mean/sample SD'})


def render(config_path):
    config_path = Path(config_path).resolve()
    cfg = json.loads(config_path.read_text(encoding='utf-8'))
    panels = cfg['panels']
    if not 1 <= len(panels) <= 4:
        raise ValueError('Use one to four horizontal panels per figure')
    line = all(p['type'] == 'line' for p in panels)
    if any(p['type'] == 'line' for p in panels) and not line:
        raise ValueError('Keep metric sensitivity plots separate from score diagnostics')
    src = (config_path.parent / cfg['data']).resolve()
    data = pd.read_csv(src, dtype={'panel': str, 'method': str, 'run': str, 'sample_id': str, 'group': str})
    expected = {'panel', 'metric', 'x', 'run', 'group', 'value'} if line else {'panel', 'method', 'run', 'sample_id', 'label', 'score'}
    if not expected.issubset(data.columns) or data[list(expected)].isna().any().any():
        raise ValueError(f'Input requires nonmissing columns {sorted(expected)}')
    if not line:
        names = [m['key'] for m in cfg['methods']]
        if len(names) != len(set(names)) or any(type(m.get('higher_is_positive')) is not bool for m in cfg['methods']):
            raise ValueError('Methods must be unique with explicit boolean higher_is_positive')
        if any(p['type'] == 'density' and p['method'] not in names for p in panels):
            raise ValueError('Density method must be declared in methods')
    output = (config_path.parent / cfg['output']).resolve()
    sha = digest(src)
    records = []
    with style.context(line):
        width = cfg.get('width', 7.05 if line else 7.16) if len(panels) > 1 else cfg.get('width', 3.5)
        fig, axes = plt.subplots(1, len(panels), figsize=(width, 2.35 if line else 2.08), squeeze=False)
        axes = axes.ravel()
        fig.subplots_adjust(left=.072 if line else .057, right=.992 if line else .995,
                            bottom=.34 if line else .27, top=.97 if line else .96,
                            wspace=.65 if line else .43)
        for i, (ax, p) in enumerate(zip(axes, panels)):
            audit = []
            if p['type'] == 'line': draw_line(ax, data, p, i, audit)
            elif p['type'] == 'roc': draw_roc(ax, score_panel(data, p, cfg), cfg, audit)
            elif p['type'] == 'density': draw_density(ax, score_panel(data, p, cfg), p, audit)
            else: raise ValueError('Unknown panel type')
            ax.tick_params(length=3 if line else 2, pad=2 if line else 1.5)
            ax.xaxis.labelpad = 4 if line else 2
            ax.yaxis.labelpad = 3 if line else 2
            records.append({'panel': p, 'computed': audit})
        style.panel_labels(fig, axes, [p.get('label', '') for p in panels])
        style.export(fig, output)
        plt.close(fig)
    if digest(src) != sha:
        raise AssertionError('Source data changed')
    manifest = {'config': cfg, 'source': str(src), 'source_sha256': sha,
                'renderer_sha256': digest(__file__), 'style_sha256': digest(style.__file__),
                'python': sys.version, 'matplotlib': matplotlib.__version__,
                'positive_label': 1, 'band': 'sample SD, ddof=1; ROC display clipped to [0,1]',
                'records': records}
    Path(str(output)+'.audit.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Saved {output}.pdf/.svg/.png and audit.json; source scores unchanged.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('config')
    render(parser.parse_args().config)