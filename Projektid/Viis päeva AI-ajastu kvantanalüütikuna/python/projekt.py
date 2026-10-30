"""Õppesimulatsioon. Käivita: python python/projekt.py (internetti ei kasuta)."""
from pathlib import Path
import json, hashlib, platform, time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, precision_score, recall_score
import sklearn

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ['SYN_XLK', 'SYN_XLF', 'SYN_XLE', 'SYN_XLV', 'SYN_XLI', 'SYN_XLP']
FEATURES = ['mom21', 'mom63', 'vol21']


def make_data():
    """Sektorilaadsed, kuid täielikult väljamõeldud hinnad; seeme pole optimeeritud."""
    rng = np.random.default_rng(20261030)
    dates = pd.bdate_range('2012-01-02', '2025-12-31')
    n = len(dates)
    market = rng.normal(.0002, .008, n)
    # Kunstlik stress; kuupäevad ei ole väide vastavate päristurgude kohta.
    market[2050:2060] -= .025
    noise = rng.normal(0, .006, (n, 6))
    r = np.zeros((n, 6))
    for t in range(1, n):
        persistence = .08 if t < n // 2 else -.03
        r[t] = market[t] + noise[t] + persistence * r[t-1]
    prices = pd.DataFrame(100 * np.exp(np.cumsum(r, axis=0)), index=dates, columns=ASSETS)
    prices.index.name = 'date'
    prices.to_csv(ROOT / 'andmed/synteetilised_hinnad.csv', float_format='%.10f')
    return prices


def load_data():
    p = pd.read_csv(ROOT / 'andmed/synteetilised_hinnad.csv', index_col=0, parse_dates=True)
    validate(p)
    return p


def validate(p):
    if not p.index.is_monotonic_increasing or not p.index.is_unique:
        raise ValueError('Kuupäevad peavad olema kasvavad ja unikaalsed.')
    if p.isna().any().any() or not np.isfinite(p.to_numpy()).all() or (p <= 0).any().any():
        raise ValueError('Puuduv, mitte-lõplik või mittepositiivne hind; automaatset täitmist ei tehta.')


def panel(p):
    """Signaal kuu viimase vaatluse järel; täitmine järgmise vaatluse sulgemisel."""
    validate(p)
    r = p.pct_change(fill_method=None)
    feats = {'mom21':p.pct_change(21, fill_method=None),
             'mom63':p.pct_change(63, fill_method=None),
             'vol21':r.rolling(21).std() * np.sqrt(252)}
    ends = p.groupby(p.index.to_period('M')).tail(1).index
    rows = []
    for signal, next_signal in zip(ends[:-1], ends[1:]):
        a, b = p.index.get_loc(signal)+1, p.index.get_loc(next_signal)+1
        if b >= len(p):
            continue
        entry, exit_ = p.index[a], p.index[b]
        for asset in p.columns:
            row = {'signal':signal, 'entry':entry, 'exit':exit_, 'asset':asset,
                   'y':p.loc[exit_, asset]/p.loc[entry, asset]-1}
            row.update({k:v.loc[signal, asset] for k,v in feats.items()})
            rows.append(row)
    return pd.DataFrame(rows).dropna().reset_index(drop=True)


def predict_walk_forward(data, start='2019-01-01', stop='2026-01-01'):
    """Igas kuus treeni üksnes juba lõppenud hoideperioodidel; paneel jaotub kuupäeva kaupa."""
    result, timing = [], []
    for signal, test in data[(data.signal >= start) & (data.signal < stop)].groupby('signal'):
        train = data[data.exit < signal]
        if len(train) < 120:
            raise ValueError('Liiga lühike treeningajalugu.')
        assert train.exit.max() < test.signal.min()
        out = test.copy()
        # Skaleeritud momentum on üksnes reegli prognoosiproksi, mitte sobitatud mudel.
        out['reegel'] = out.mom63 / 3
        models = {'ridge': make_pipeline(StandardScaler(), Ridge(alpha=10)),
                  'mets': RandomForestRegressor(n_estimators=60, max_depth=3,
                          min_samples_leaf=25, max_features=1.0, random_state=42, n_jobs=1)}
        for name, model in models.items():
            t = time.perf_counter()
            model.fit(train[FEATURES], train.y)
            out[name] = model.predict(test[FEATURES])
            timing.append({'signal':str(signal.date()), 'model':name,
                           'seconds':time.perf_counter()-t, 'train_rows':len(train)})
        result.append(out)
    return pd.concat(result, ignore_index=True), pd.DataFrame(timing)


def choose_weights(g, score, p=None, cap=.5, top=2, vol_target=None):
    assets = list(g.asset)
    w = pd.Series(0., index=assets)
    if score == 'baas':
        w[:] = 1/len(w)
    else:
        selected = g.sort_values([score, 'asset'], ascending=[False, True]).head(top).asset
        w.loc[selected] = min(1/top, cap)
    if vol_target is not None:
        hist = p.loc[:g.signal.iloc[0], assets].pct_change(fill_method=None).tail(63)
        cov = hist.cov().to_numpy() * 252
        sigma = np.sqrt(w.to_numpy() @ cov @ w.to_numpy())
        w *= min(1., vol_target / sigma) if sigma > 0 else 1.
    return w


def backtest(pred, score, p=None, cost=.001, cap=.5, top=2, vol_target=None):
    """Kulud mõlemalt tehingupoolelt. Kaalud triivivad; kuine ümberjaotus, raha tootlus 0."""
    prev = pd.Series(0., index=sorted(pred.asset.unique()))
    rows, holdings = [], []
    for date, g in pred.groupby('signal'):
        w = choose_weights(g, score, p, cap, top, vol_target).reindex(prev.index)
        r = g.set_index('asset').y.reindex(prev.index)
        # Sihtkaalud mõõdetakse kulujärgsest NAV-ist: lahenda kulude fikspunkt.
        c = 0.
        for _ in range(30):
            c = cost * ((1-c)*w-prev).abs().sum()
        turnover = ((1-c)*w-prev).abs().sum()
        gross = float(w @ r)
        net = (1-c)*(1+gross)-1
        rows.append({'signal':date,'entry':g.entry.iloc[0],'exit':g.exit.iloc[0],
                     'gross':gross,'net':net,'turnover':turnover,'cost':c,
                     'exposure':w.sum()})
        holdings.append({'signal':date, **w.to_dict(), 'CASH':1-w.sum()})
        prev = w*(1+r)/(1+gross)
    return pd.DataFrame(rows).set_index('signal'), pd.DataFrame(holdings).set_index('signal')


def metrics(r):
    r = np.asarray(r, dtype=float)
    wealth = np.r_[1., np.cumprod(1+r)]
    dd = wealth/np.maximum.accumulate(wealth)-1
    vol = r.std(ddof=1)*np.sqrt(12)
    return {'CAGR':wealth[-1]**(12/len(r))-1, 'vol':vol,
            'Sharpe_rf0':r.mean()*12/vol if vol else np.nan,
            'max_drawdown_monthly':dd.min(), 'months':len(r)}


def bootstrap(excess, reps=2000, block=3):
    """Ringplokk-bootstrap; kirjeldav CI, mitte andmekaevandust korrigeeriv test."""
    x = np.asarray(excess); rng = np.random.default_rng(52); n = len(x)
    means = []
    for _ in range(reps):
        starts = rng.integers(0, n, int(np.ceil(n/block)))
        idx = np.concatenate([(s+np.arange(block)) % n for s in starts])[:n]
        means.append(x[idx].mean()*12)
    return np.quantile(means, [.025, .975])


def run():
    for folder in ['andmed', 'raportid', 'pildid']:
        (ROOT/folder).mkdir(exist_ok=True)
    if not (ROOT/'andmed/synteetilised_hinnad.csv').exists():
        make_data()
    p = load_data(); data = panel(p)
    data.to_csv(ROOT/'andmed/paneel.csv', index=False)
    pred, timing = predict_walk_forward(data)
    pred.to_csv(ROOT/'raportid/prognoosid.csv', index=False)
    timing.to_csv(ROOT/'raportid/treeninguajad.csv', index=False)
    tables, pred_metrics, series = [], [], {}
    for period, a, b in [('valideerimine','2019','2022'), ('lopptest','2022','2026')]:
        q = pred[(pred.signal >= a) & (pred.signal < b)]
        for name in ['baas','reegel','ridge','mets','risk']:
            bt, weights = backtest(q, 'reegel' if name=='risk' else name, p,
                                  cap=.3 if name=='risk' else .5,
                                  top=3 if name=='risk' else 2,
                                  vol_target=.12 if name=='risk' else None)
            tables.append({'period':period,'model':name, **metrics(bt.net),
                           'mean_turnover':bt.turnover.mean()})
            bt.to_csv(ROOT/f'raportid/{period}_{name}.csv')
            weights.to_csv(ROOT/f'raportid/{period}_{name}_kaalud.csv')
            if period == 'lopptest': series[name] = bt.net
            if name in ['reegel','ridge','mets']:
                truth = q.y > 0; label = q[name] > 0
                pred_metrics.append({'period':period,'model':name,
                    'RMSE':np.sqrt(mean_squared_error(q.y,q[name])),
                    'precision':precision_score(truth,label,zero_division=0),
                    'recall':recall_score(truth,label,zero_division=0),
                    'positive_rate':truth.mean()})
    summary = pd.DataFrame(tables)
    summary.to_csv(ROOT/'raportid/mootdikud.csv', index=False)
    pd.DataFrame(pred_metrics).to_csv(ROOT/'raportid/prognoosimootdikud.csv',index=False)
    q = pred[pred.signal >= '2022']
    sensitivity = []
    for bps in [0,5,10,25,50]:
        bt,_ = backtest(q,'reegel',p,cost=bps/10000)
        sensitivity.append({'bps':bps, **metrics(bt.net)})
    pd.DataFrame(sensitivity).to_csv(ROOT/'raportid/kulutundlikkus.csv',index=False)
    bt,w = backtest(q,'reegel',p,cap=.3,top=3,vol_target=.12)
    stress = pd.Series([-.12,-.15,-.18,-.08,-.12,-.06],index=ASSETS)
    loss = float(w.iloc[-1][ASSETS] @ stress)
    ci = bootstrap(series['reegel']-series['baas'])
    meta = {'data_kind':'SYNTHETIC_ONLY','seed':20261030,
        'sha256':hashlib.sha256((ROOT/'andmed/synteetilised_hinnad.csv').read_bytes()).hexdigest(),
        'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,
        'sklearn':sklearn.__version__, 'cost_one_way_bps':10,
        'stress_last_portfolio':loss,'paired_excess_mean_annual_ci95':ci.tolist(),
        'decision':'Ainult töövoo õppesimulatsioon; turueelis ei ole tõendatud.'}
    (ROOT/'raportid/run.json').write_text(json.dumps(meta,indent=2,ensure_ascii=False),encoding='utf-8')
    plt.rcParams.update({'axes.spines.top':False,'axes.spines.right':False,'font.size':10})
    fig,ax = plt.subplots(figsize=(10,5)); (p/p.iloc[0]).plot(ax=ax,lw=1)
    ax.set(title='SÜNTEETILISED hinnad · mitte ETF-ide tegelik ajalugu',ylabel='Algväärtus = 1',xlabel='Aeg')
    fig.tight_layout();fig.savefig(ROOT/'pildid/hinnad.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(10,5))
    for name,r in series.items():
        dates = pd.to_datetime(q.groupby('signal').exit.first())
        start_date = q.entry.min()
        ax.plot(np.r_[np.datetime64(start_date),dates.to_numpy()],np.r_[1.,(1+r).cumprod()],label=name)
    ax.set(title='SÜNTEETILINE lõppkatse · kulud arvestatud',ylabel='Kapitali kordaja',xlabel='Hoideperioodi lõpp')
    ax.legend(ncol=5);fig.tight_layout();fig.savefig(ROOT/'pildid/kapital.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,4))
    for name,r in series.items():
        wealth=np.r_[1.,(1+r).cumprod()];dd=wealth/np.maximum.accumulate(wealth)-1
        ax.plot(dd*100,label=name)
    ax.set(title='Kuise hoideperioodi lõpu langus · sünteetilised andmed',ylabel='Langus (%)',xlabel='Hoideperiood')
    ax.legend(ncol=5,loc='upper center',bbox_to_anchor=(.5,-.2));fig.tight_layout();fig.savefig(ROOT/'pildid/langus.png',dpi=150);plt.close(fig)
    fig,ax=plt.subplots(figsize=(7,6));cor=p.pct_change(fill_method=None).corr()
    im=ax.imshow(cor,vmin=-1,vmax=1,cmap='RdBu_r')
    ax.set_xticks(range(6),ASSETS,rotation=45,ha='right');ax.set_yticks(range(6),ASSETS)
    for i in range(6):
        for j in range(6):ax.text(j,i,f'{cor.iloc[i,j]:.2f}',ha='center',va='center',color='white' if i==j else 'black')
    ax.set_title('Sünteetiliste päevatootluste korrelatsioon');fig.colorbar(im,ax=ax)
    fig.tight_layout();fig.savefig(ROOT/'pildid/korrelatsioon.png',dpi=150);plt.close(fig)
    print(summary.round(4).to_string(index=False));print(json.dumps(meta,ensure_ascii=False,indent=2))
    return summary

if __name__ == '__main__':
    run()
