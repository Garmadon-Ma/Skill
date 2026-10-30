"""Approved visual constants extracted from OSR-FETF figure generators, 2026-10-10.

No manuscript paths, experiment data, method names or seeds belong in this module.
"""
import matplotlib as mpl

BASE = {
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'Times', 'DejaVu Serif'],
    'mathtext.fontset': 'stix', 'font.size': 8.5,
    'axes.labelsize': 9, 'axes.titlesize': 9,
    'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 7.7,
    'axes.linewidth': .8, 'xtick.major.width': .8, 'ytick.major.width': .8,
    'lines.linewidth': 1.5, 'figure.dpi': 160, 'savefig.dpi': 600,
    'savefig.bbox': 'tight', 'savefig.pad_inches': .03,
    'pdf.fonttype': 42, 'ps.fonttype': 42,
    'axes.spines.top': False, 'axes.spines.right': False,
}
DIAGNOSTIC = {'font.size': 7, 'axes.labelsize': 7, 'xtick.labelsize': 6,
              'ytick.labelsize': 6, 'axes.linewidth': .6}
LINE = {'font.size': 8.5, 'axes.labelsize': 8.5, 'xtick.labelsize': 7.5,
        'ytick.labelsize': 7.5, 'axes.linewidth': .75}
BASELINES = ['#0072B2', '#009E73', '#CC79A7', '#E69F00', '#7A6250', '#6F56A5', '#4D8085']
LINESTYLES = ['--', '-.', ':', '--', '-.', '-', ':']
PROPOSED = '#D62728'
DENSITY = [('ID', '#2878B5', '-'), ('OOD', '#D9534F', '--')]
METRICS = ['#0072B2', '#D55E00', '#009E73', '#8C5DA8']
MARKERS = ['o', 's', '^', 'D']


def context(line=False):
    return mpl.rc_context({**BASE, **(LINE if line else DIAGNOSTIC)})


def legend(ax, density=False):
    leg = ax.legend(loc='upper left' if density else 'lower right',
                    fontsize=6.5 if density else 5.5, frameon=True,
                    fancybox=False, facecolor='white', framealpha=.95 if density else .96,
                    edgecolor='#D5D5D5', handlelength=1.6 if density else 1.8,
                    labelspacing=.2 if density else .15, borderpad=.3,
                    borderaxespad=.35 if density else .3)
    leg.get_frame().set_linewidth(.4)


def panel_labels(fig, axes, names):
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    for i, (ax, name) in enumerate(zip(axes, names)):
        box = ax.xaxis.label.get_window_extent(renderer).transformed(fig.transFigure.inverted())
        fig.text((ax.get_position().x0 + ax.get_position().x1) / 2,
                 box.y0 - 4 / 72 / fig.get_figheight(),
                 f'({chr(97+i)})' + (f' {name}' if name else ''),
                 ha='center', va='top', fontsize=7)


def export(fig, output):
    from pathlib import Path
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    for ext in ('pdf', 'svg', 'png'):
        fig.savefig(str(output) + '.' + ext)