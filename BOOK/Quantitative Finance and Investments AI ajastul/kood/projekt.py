"""USA turu õppemudel. Vaikimisi AINULT sünteetilised andmed, mitte tehingukäsud."""
from pathlib import Path
import json, hashlib, platform
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error

ROOT = Path(__file__).resolve().parents[1]
DATA, OUT, FIG = (ROOT / x for x in ('andmed', 'tulemused', 'joonised'))
for folder in (DATA, OUT, FIG): folder.mkdir(exist_ok=True)
FEATURES = ['r1', 'mom20', 'vol20', 'ma_gap']

def synthetic(n=1600, seed=42):
    """Fiktiivsed total-return hinnad. Tõelise USA börsikalendri asemel tööpäevad."""
    rng = np.random.default_rng(seed)
    vol = np.where(np.arange(n) < n // 2, .009, .018)
    common = rng.normal(.00025, vol)
    r = np.column_stack([common + rng.normal(0, .006, n),
                         .8 * common + rng.normal(.00005, .009, n),
                         .5 * common + rng.normal(.0001, .008, n)])
    return pd.DataFrame(100*np.cumprod(1+r, axis=0),
                        index=pd.bdate_range('2018-01-01', periods=n),
                        columns=['SIM_A', 'SIM_B', 'SIM_C']).rename_axis('date')

def load_prices():
    path = DATA / 'hinnad.csv'
    if not path.exists():
        p = synthetic(); p.to_csv(path)
        (DATA/'provenance.json').write_text(json.dumps({'kind':'SIMULATED', 'seed':42,
             'warning':'Not US market observations; no evidence of alpha.'}, indent=2))
    p = pd.read_csv(path, index_col=0, parse_dates=True)
    if p.index.has_duplicates or not p.index.is_monotonic_increasing:
        raise ValueError('Kuupäevad peavad olema unikaalsed ja kasvavad.')
    if p.isna().any().any() or (p <= 0).any().any():
        raise ValueError('Puuduvad või mittepositiivsed hinnad: paranda andmed, ära täida tulevikust.')
    return p

def dataset(price):
    r = price.pct_change(fill_method=None)
    x = pd.DataFrame({'r1':r, 'mom20':price.pct_change(20, fill_method=None),
                      'vol20':r.rolling(20).std(), 'ma_gap':price/price.rolling(50).mean()-1})
    # Info close(t), tehing close(t+1), tootlus close(t+1)->close(t+2).
    x['target'] = r.shift(-2)
    return x.dropna()

def walk_forward(d, use_xgb=True):
    """Esimene 70%: kolm valikuvoldi. Viimane 30%: üks külmutatud lõppkatse."""
    split = int(len(d)*.7)
    # Kaks rida vahet, sest sildi lõppaeg t+2 ei tohi puutuda testi.
    train, test = d.iloc[:split-2], d.iloc[split:]
    models = {'ridge':make_pipeline(StandardScaler(), Ridge(alpha=10)),
              'hist_gbm':HistGradientBoostingRegressor(max_iter=50, max_leaf_nodes=7,
                            learning_rate=.05, l2_regularization=10, random_state=42)}
    if use_xgb:
        try:
            from xgboost import XGBRegressor
            models['xgboost'] = XGBRegressor(n_estimators=60, max_depth=2,
                learning_rate=.03, reg_lambda=10, subsample=.8, colsample_bytree=.8,
                objective='reg:squarederror', random_state=42, n_jobs=1)
        except ImportError:
            pass
    scores = []
    for name, model in models.items():
        for fold, (a,b) in enumerate(TimeSeriesSplit(n_splits=3, gap=2).split(train)):
            model.fit(train.iloc[a][FEATURES], train.iloc[a].target)
            pred = model.predict(train.iloc[b][FEATURES])
            scores.append({'model':name,'fold':fold,'mse':mean_squared_error(train.iloc[b].target,pred)})
    cv=pd.DataFrame(scores); winner=cv.groupby('model').mse.mean().idxmin()
    predictions=pd.DataFrame(index=test.index)
    for name,model in models.items():
        model.fit(train[FEATURES],train.target)
        predictions[name]=model.predict(test[FEATURES])
    predictions['zero']=0.
    cv.to_csv(OUT/'cv.csv',index=False)
    pd.DataFrame([{'model':c,'mse':mean_squared_error(test.target,predictions[c])}
                 for c in predictions]).to_csv(OUT/'test_mse.csv',index=False)
    (OUT/'valik.json').write_text(json.dumps({'selected_on_validation':winner,
        'test_start':str(test.index[0].date()), 'gap_rows':2,
        'rule':'positive forecast -> long, otherwise cash; fixed before holdout'},indent=2))
    return predictions, winner

def net_returns(r, w, bps=10.):
    """Üks riskivara + nulltootlusega raha. w = intervalli algkaal.
    Kulud kauplemishetke nominaalilt; kulu ja päevatootluse ristliige on eiratud.
    Driftiga eelkaal väldib iga päev fiktiivse rebalance'i eeldust.
    Lõpus positsioon likvideeritakse sama ühikukuluga.
    """
    w=w.reindex(r.index).fillna(0.).astype(float)
    prev=w.shift(1).fillna(0.)
    prev_r=r.shift(1).fillna(0.)
    drift=prev*(1+prev_r)/(1+prev*prev_r)
    turnover=(w-drift).abs()
    gross=w*r
    liquidation=w.iloc[-1]*(1+r.iloc[-1])/(1+gross.iloc[-1])
    cost=turnover*bps/10000
    cost.iloc[-1]+=liquidation*(1+gross.iloc[-1])*bps/10000
    return gross-cost, turnover

def metrics(r):
    wealth=(1+r).cumprod()
    peak=np.maximum.accumulate(np.r_[1.,wealth.to_numpy()])[1:]
    std=r.std(ddof=1)
    return {'CAGR':wealth.iloc[-1]**(252/len(r))-1,
        'vol':std*np.sqrt(252), 'Sharpe_rf0':r.mean()/std*np.sqrt(252) if std>0 else np.nan,
        'max_drawdown':float((wealth.to_numpy()/peak-1).min()),'total_return':wealth.iloc[-1]-1}

def comparison(p, pred, winner):
    price=p.iloc[:,0]; r=price.pct_change(fill_method=None)
    # Kõik signaalid indekseeritud otsustuspäevaga; positsioon t+2 tootlusel.
    sig=pd.DataFrame(index=p.index)
    sig['buy_hold']=1.
    sig['trend50']=(price>price.rolling(50).mean()).astype(float)
    for c in pred.columns:
        if c!='zero': sig[c]=(pred[c]>0).astype(float)
    sig['cash']=0.
    positions=sig.shift(2)
    first=p.index.get_loc(pred.index[0])+2
    last=p.index.get_loc(pred.index[-1])+2
    ix=p.index[first:last+1]
    rr=r.loc[ix]
    paths={}; rows=[]; costs=[]
    for c in positions:
        for bps in [0,5,10,25,50]:
            net,turn=net_returns(rr,positions[c].loc[ix],bps)
            costs.append({'strategy':c,'bps':bps,**metrics(net)})
            if bps==10:
                paths[c]=net; rows.append({'strategy':c,'selected':c==winner,**metrics(net),
                                            'one_way_turnover_excluding_final_exit':turn.sum()})
    returns=pd.DataFrame(paths)
    returns.to_csv(OUT/'test_returns.csv')
    pd.DataFrame(rows).to_csv(OUT/'vordlus.csv',index=False)
    pd.DataFrame(costs).to_csv(OUT/'kulutundlikkus.csv',index=False)
    kind=json.loads((DATA/'provenance.json').read_text())['kind']
    ((1+returns).cumprod()).plot(figsize=(10,5),title=f'{kind}: lõppkatse; kulu 10 bp / kaubeldud nominaal')
    plt.ylabel('Kapital, algus 1');plt.tight_layout();plt.savefig(FIG/'kapital.png',dpi=150);plt.close()
    cs=pd.DataFrame(costs)
    for name,g in cs.groupby('strategy'):plt.plot(g.bps,g.CAGR*100,label=name)
    plt.axhline(0,color='black',linewidth=.6);plt.xlabel('Kulu ühe suuna kohta, baaspunkti')
    plt.ylabel('CAGR %');plt.title(f'Kulutundlikkus: {kind}');plt.legend()
    plt.tight_layout();plt.savefig(FIG/'kulud.png',dpi=150);plt.close()
    return returns

def portfolio(p, test_index):
    from sklearn.covariance import LedoitWolf
    r=p.pct_change(fill_method=None).dropna()
    train=r.loc[r.index<test_index[0]]
    cov=LedoitWolf().fit(train).covariance_*252
    iv=1/np.sqrt(np.diag(cov)); iv/=iv.sum()
    weights={'equal':np.ones(p.shape[1])/p.shape[1], 'inverse_vol':iv}
    from scipy.optimize import minimize
    n=p.shape[1]
    opt=minimize(lambda w:float(w@cov@w),np.ones(n)/n,method='SLSQP',
                 bounds=[(0,.6)]*n,constraints=[{'type':'eq','fun':lambda w:w.sum()-1}],
                 options={'ftol':1e-12,'maxiter':500})
    if not opt.success:raise RuntimeError(opt.message)
    weights['min_variance_cap60']=opt.x
    test=r.loc[test_index]; result=[]
    for name,w in weights.items():
        gross=test.to_numpy()@w
        prev=np.vstack([np.zeros(len(w)),np.tile(w,(len(test)-1,1))*(1+test.to_numpy()[:-1])/(1+gross[:-1,None])])
        turn=np.abs(w-prev).sum(axis=1)
        net=gross-turn*.001
        net[-1]-=(1+gross[-1])*.001 # kõik pikad positsioonid suletakse
        result.append({'portfolio':name, 'weights':str(w.round(4).tolist()),
                       **metrics(pd.Series(net,index=test.index))})
    pd.DataFrame(result).to_csv(OUT/'portfell.csv',index=False)
    pd.DataFrame(cov,index=p.columns,columns=p.columns).to_csv(OUT/'kovariatsioon.csv')
    # Plokk-bootstrap hinnang ei ole sõltumatu uus turuajalugu.
    rng=np.random.default_rng(19); s=test.iloc[:,0].to_numpy(); samples=[]
    for _ in range(500):
        starts=rng.integers(0,len(s),int(np.ceil(len(s)/20)))
        b=np.concatenate([s[(a+np.arange(20))%len(s)] for a in starts])[:len(s)]
        samples.append(np.prod(1+b)-1)
    (OUT/'bootstrap.json').write_text(json.dumps({'block_days':20,'draws':500,
       'total_return_percentiles':np.quantile(samples,[.025,.5,.975]).tolist(),
       'warning':'Conditional on observed sample; not future confidence guarantee.'},indent=2))

def main():
    p=load_prices();d=dataset(p.iloc[:,0]);pred,winner=walk_forward(d)
    pred.to_csv(OUT/'prognoosid.csv'); returns=comparison(p,pred,winner);portfolio(p,returns.index)
    import sklearn
    meta={'python':platform.python_version(),'numpy':np.__version__,'pandas':pd.__version__,
      'sklearn':sklearn.__version__,'data_sha256':hashlib.sha256((DATA/'hinnad.csv').read_bytes()).hexdigest(),
      'data_kind':json.loads((DATA/'provenance.json').read_text())['kind']}
    (OUT/'run_manifest.json').write_text(json.dumps(meta,indent=2))
    print(pd.read_csv(OUT/'vordlus.csv').to_string(index=False));print('Valik valideerimise põhjal:',winner)
if __name__=='__main__':main()
