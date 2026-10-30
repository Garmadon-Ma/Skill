"""Synthetic-only executable regression/preview tests; never paper evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

import render_paper_figures as figures
import render_paper_table as tables


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2), encoding='utf-8')


def expect_error(fn, message):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError(message)


def test(out):
    out = Path(out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(408)
    rows = []
    methods = [{'key':'baseline', 'label':'Baseline', 'higher_is_positive':True},
               {'key':'distance', 'label':'Distance', 'higher_is_positive':False},
               {'key':'proposed', 'label':'Ours', 'higher_is_positive':True, 'proposed':True}]
    for panel in ('A', 'B'):
        for run in range(3):
            labels = np.tile([0,1], 60)
            for method, separation in [('baseline',2), ('distance',1.2), ('proposed',.7)]:
                values = np.round(rng.normal(size=len(labels)) + labels * separation, 1)
                if method == 'distance': values = -values
                for n, (label, score) in enumerate(zip(labels, values)):
                    rows.append(dict(panel=panel, method=method, run=str(run), sample_id=str(n), label=int(label), score=score))
    data = pd.DataFrame(rows)
    data.to_csv(out/'scores.csv', index=False)
    initial_hash = figures.digest(out/'scores.csv')
    cfg = {'data':'scores.csv', 'output':'synthetic-diagnostics', 'methods':methods,
           'panels':[{'type':'density', 'key':p, 'method':'proposed', 'label':f'Synthetic {p}', 'band':True} for p in ('A','B')]
                    +[{'type':'roc', 'key':p, 'label':f'Synthetic {p}'} for p in ('A','B')]}
    write_json(out/'diagnostics.json', cfg)
    figures.render(out/'diagnostics.json')
    assert figures.digest(out/'scores.csv') == initial_hash
    audit = json.loads((out/'synthetic-diagnostics.audit.json').read_text())
    for entry in audit['records'][2:]:
        for result in entry['computed']:
            expected = []
            for run in range(3):
                r = data[(data.panel==entry['panel']['key']) & (data.method==result['method']) & (data.run==str(run))]
                expected.append(roc_auc_score(r.label, -r.score if result['method']=='distance' else r.score))
            np.testing.assert_allclose(result['run_auroc'], expected, atol=1e-12)
            np.testing.assert_allclose(result['mean_auroc'], np.mean(expected), atol=1e-12)
        means = {r['method']:r['mean_auroc'] for r in entry['computed']}
        assert means['baseline'] > means['proposed']  # Style must not manufacture superiority.
    # Pairing validation must fail before plotting a scientifically invalid comparison.
    malformed = data[data.panel=='A'].copy()
    malformed.loc[malformed.method=='baseline', 'sample_id'] = 'duplicate'
    fig, ax = figures.plt.subplots()
    expect_error(lambda: figures.draw_roc(ax, malformed, cfg, []), 'Duplicate IDs accepted')
    figures.plt.close(fig)
    line_rows = [dict(panel='sweep', metric=metric, x=x, run=str(run), group=str(group),
                      value=30+mi*10+4*x+group+run)
                 for mi, metric in enumerate(('error','score','precision','recall'))
                 for x in (.3,.4,.5,.6,.7) for run in range(3) for group in range(2)]
    pd.DataFrame(line_rows).to_csv(out/'line.csv', index=False)
    line = {'data':'line.csv', 'output':'synthetic-lines', 'panels':[
        {'type':'line','key':'sweep','metric':m,'label':'Synthetic', 'xlabel':r'Weight $\mu$',
         'ylabel':m.title()+' (%)', 'default_x':.5} for m in ('error','score','precision','recall')]}
    write_json(out/'lines.json', line)
    figures.render(out/'lines.json')
    la = json.loads((out/'synthetic-lines.audit.json').read_text())
    np.testing.assert_allclose(la['records'][0]['computed'][0]['mean'], [32.7,33.1,33.5,33.9,34.3])
    np.testing.assert_allclose(la['records'][0]['computed'][0]['sd'], 1)
    groups = [{'key':'a','label':'Dataset A'}, {'key':'b','label':'Dataset B'}]
    metrics = [{'key':'error','label':'Error','direction':'min'}, {'key':'score','label':'Score','direction':'max'},
               {'key':'precision','label':'Precision','direction':'max'}, {'key':'recall','label':'Recall','direction':'max'}]
    table = {'caption':'Synthetic style test.', 'label':'tab:test', 'output':'comparison.tex',
             'groups':groups, 'metrics':metrics, 'rows':[], 'note':'Synthetic fixtures only. Mean ± SD. Not experimental results.'}
    for i, name in enumerate(('Baseline A','Baseline B','Ours')):
        table['rows'].append({'name':name, 'proposed':i==2, 'values':{
            g['key']:{m['key']:[20+i*3+mi*10, 1.2] for mi,m in enumerate(metrics)} for g in groups}})
    write_json(out/'table.json',table)
    tables.render(out/'table.json')
    source = (out/'comparison.tex').read_text()
    assert r'\mathbf{20.00}' in source and r'\underline{23.00}' in source
    assert r'\mathbf{56.00}' in source and r'\rowcolor{ApprovedTableOurs}' in source
    table['components'] = [{'key':'aux','label':'Global\naux.'}, {'key':'head','label':'Private\nproj.'}, {'key':'adapt','label':'Local\nadapt.'}]
    for i,r in enumerate(table['rows']):
        r['components'] = dict(aux=i!=0, head=True, adapt=i!=1)
    table.update(caption='Synthetic ablation style.', label='tab:ablation',output='ablation.tex')
    write_json(out/'ablation.json',table)
    tables.render(out/'ablation.json')
    assert r'$\times$' in (out/'ablation.tex').read_text()
    table['rows'][0]['values']['a']['error']=[1,-1]
    write_json(out/'invalid-table.json',table)
    expect_error(lambda: tables.render(out/'invalid-table.json'), 'Negative SD accepted')
    package = Path(__file__).resolve().parents[1]/'assets'/'approved-paper-tables.sty'
    shutil.copy2(package, out/package.name)
    (out/'preview.tex').write_text(r'''\documentclass[journal]{IEEEtran}
\usepackage{approved-paper-tables}
\begin{document}
Synthetic style validation only. These numbers are not research results.
\input{comparison.tex}
\input{ablation.tex}
\clearpage
\end{document}
''', encoding='utf-8')
    write_json(out/'TEST-PASSED.json', {'synthetic_only':True,'checks':['raw sklearn AUROC == mean-curve area',
               'score direction declared, not chosen by result','same paired test samples', 'source hash invariant',
               'within-run aggregation then sample SD','table ranking and check/cross','negative SD rejected']})
    print(f'PASS. Synthetic-only previews in {out}; compile preview.tex to inspect tables.')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True)
    test(parser.parse_args().out)