"""Kursuse deterministlik arvutustuumik. Kõik demoandmed on simuleeritud."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'valjund'
OUT.mkdir(exist_ok=True)

def demo_hinnad(n=756, seed=42):
    rng = np.random.default_rng(seed)
    market = rng.normal(0.00025, 0.009, n)
    innovations = rng.normal(0, [0.008, 0.010, 0.003], (n, 3))
    returns = market[:, None] * [1.1, 1.2, 0.2] + innovations
    prices = 100 * np.cumprod(1 + returns, axis=0)
    # Esimene rida on investeeringu algväärtus; hilisemad read on vaatlused.
    prices = np.vstack([np.full(3, 100.), prices])
    return pd.DataFrame(prices, index=pd.bdate_range('2022-01-03', periods=n+1),
                        columns=['AKTSIA_A_SIM', 'AKTSIA_B_SIM', 'VOLAKIRI_SIM'])

def kontrolli_hindu(p):
    if p.empty or len(p) < 2 or not p.index.is_unique or not p.index.is_monotonic_increasing:
        raise ValueError('Vaja on vähemalt kaht järjestatud, kordusteta kuupäeva.')
    if p.isna().any().any() or not np.isfinite(p.to_numpy()).all() or (p <= 0).any().any():
        raise ValueError('Puuduv, lõpmatu või mittepositiivne hind. Paranda lähteandmed.')
    return p

def tootlused(p):
    kontrolli_hindu(p)
    return p.pct_change(fill_method=None).iloc[1:]

def moodikud(r, periods=252):
    a = np.asarray(r, dtype=float)
    if len(a) < 2 or not np.isfinite(a).all() or (a <= -1).any():
        raise ValueError('Vigased tootlused; see funktsioon eeldab positiivset vara väärtust.')
    wealth = np.r_[1., np.cumprod(1+a)]
    drawdown = wealth / np.maximum.accumulate(wealth) - 1
    return {'kogutootlus': float(wealth[-1]-1),
            'CAGR': float(wealth[-1]**(periods/len(a))-1),
            'volatiilsus': float(np.std(a, ddof=1)*np.sqrt(periods)),
            'max_langus': float(drawdown.min())}

def osta_hoia(p, weights):
    kontrolli_hindu(p)
    w = np.asarray(weights)
    if len(w)!=len(p.columns) or (w<0).any() or not np.isclose(w.sum(),1):
        raise ValueError('Kaalud peavad olema mittenegatiivsed ja andma summaks 1.')
    value = (p / p.iloc[0]).mul(w, axis=1).sum(axis=1)
    return value.pct_change(fill_method=None).iloc[1:]

def bond_price(face=1000, coupon=50, years=3, y=0.06):
    if years < 1 or int(years)!=years or y <= -1:
        raise ValueError('Aastane kupong, täisarv aastaid ning y > -1.')
    return sum(coupon/(1+y)**t for t in range(1, years+1)) + face/(1+y)**years

def ytm(price, face=1000, coupon=50, years=3):
    lo, hi = -0.9, 10.0
    if not bond_price(face,coupon,years,hi) <= price <= bond_price(face,coupon,years,lo):
        raise ValueError('Hind väljaspool otsinguvahemikku.')
    for _ in range(120):
        mid=(lo+hi)/2
        if bond_price(face,coupon,years,mid)>price: lo=mid
        else: hi=mid
    return (lo+hi)/2

def indikaatorid(close):
    d=close.diff()
    # Lihtne 14 perioodi RSI; teadlikult mitte Wilderi silumine.
    gain=d.clip(lower=0).rolling(14).mean()
    loss=(-d.clip(upper=0)).rolling(14).mean()
    rsi=100-100/(1+gain/loss.replace(0,np.nan))
    rsi=rsi.mask((loss==0)&(gain>0),100).mask((loss==0)&(gain==0),50)
    return pd.DataFrame({'hind':close,'SMA20':close.rolling(20).mean(),
                         'SMA60':close.rolling(60).mean(),'RSI14_lihtne':rsi})

def backtest(close, cost=0.001):
    if not 0 <= cost < 0.1: raise ValueError('Vigane tehingukulu.')
    ind=indikaatorid(close)
    signal=(ind.SMA20>ind.SMA60).astype(float)
    # Otsus sulgemise järel t; täitmine järgmise päeva t+1 sulgemisel.
    # Positsioon teenib tootlust alates t+1 -> t+2. Kulu t+1 päeval.
    position=signal.shift(2).fillna(0)
    target_at_close=signal.shift(1).fillna(0)
    turnover=target_at_close.diff().abs().fillna(target_at_close.iloc[0])
    r=close.pct_change(fill_method=None).fillna(0)
    net=(1+position*r)*(1-cost*turnover)-1
    # Lõpus sulgeme alles oleva positsiooni ja võtame väljumiskulu.
    net.iloc[-1]=(1+net.iloc[-1])*(1-cost*target_at_close.iloc[-1])-1
    return pd.DataFrame({'vara':r,'signaal':signal,'positsioon':position,
                         'kaive':turnover,'neto':net}).iloc[1:]

def ml_andmed(close):
    r=close.pct_change(fill_method=None)
    X=pd.DataFrame({'r1':r,'r5':close.pct_change(5,fill_method=None),
                    'vol20':r.rolling(20).std(),
                    'kaugus20':close/close.rolling(20).mean()-1})
    return X.assign(target=r.shift(-1)).dropna()

def ml_vordlus(close):
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.linear_model import Ridge
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.dummy import DummyRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import TimeSeriesSplit
    d=ml_andmed(close); X=d.drop(columns='target'); y=d.target
    # Viimane 20% on puutumatu lõputest; üks rida jäetakse piiril välja.
    cut=int(len(d)*0.8); Xdev=X.iloc[:cut-1]; ydev=y.iloc[:cut-1]
    models={'null':DummyRegressor(strategy='constant',constant=0),
            'Ridge':make_pipeline(StandardScaler(),Ridge(alpha=10)),
            'RandomForest':RandomForestRegressor(n_estimators=80,max_depth=3,
                                  min_samples_leaf=20,random_state=42,n_jobs=1)}
    rows=[]
    for name,model in models.items():
        cv=[]
        for tr,va in TimeSeriesSplit(n_splits=3,gap=1).split(Xdev):
            model.fit(Xdev.iloc[tr],ydev.iloc[tr])
            cv.append(np.sqrt(mean_squared_error(ydev.iloc[va],model.predict(Xdev.iloc[va]))))
        model.fit(Xdev,ydev)
        pred=model.predict(X.iloc[cut:])
        rows.append({'mudel':name,'CV_RMSE':np.mean(cv),
                     'test_RMSE':np.sqrt(mean_squared_error(y.iloc[cut:],pred))})
    return pd.DataFrame(rows), {'treening_lopp':str(Xdev.index[-1]),
        'test_algus':str(X.index[cut]),'test_ridu':len(X)-cut}
