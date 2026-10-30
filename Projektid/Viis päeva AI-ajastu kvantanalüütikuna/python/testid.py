"""Finantsarvestuse ja ajalise põhjuslikkuse kontrollid. Käivita pärast projekt.py."""
import numpy as np
import pandas as pd
from projekt import load_data, validate, panel, predict_walk_forward, backtest, metrics
from rag_demo import retrieve

def test_data():
    p=load_data()
    for bad in [pd.concat([p,p.iloc[-1:]]),p.assign(SYN_XLK=np.nan),p.assign(SYN_XLK=-1)]:
        try:validate(bad)
        except ValueError:pass
        else:raise AssertionError('Vigane sisend pääses kontrollist läbi')

def test_timing():
    d=panel(load_data())
    assert (d.signal<d.entry).all() and (d.entry<d.exit).all()
    for _,g in d.groupby('signal'):assert len(g)==6
    p=load_data(); cutoff=pd.Timestamp('2021-05-31')
    d1=panel(p); changed=p.copy()
    changed.loc[changed.index>cutoff]*=1.4
    d2=panel(changed)
    a=d1[d1.signal<=cutoff].reset_index(drop=True)
    b=d2[d2.signal<=cutoff].reset_index(drop=True)
    pd.testing.assert_frame_equal(a[['mom21','mom63','vol21']],b[['mom21','mom63','vol21']])
    x,_=predict_walk_forward(d1,'2021-05-01','2021-06-01')
    y,_=predict_walk_forward(d2,'2021-05-01','2021-06-01')
    assert np.allclose(x[['reegel','ridge','mets']],y[['reegel','ridge','mets']])

def test_money():
    # Esimene ost: kulufraktsioon c/(1+c); nulltootlus ei peida ostukulu.
    d=pd.DataFrame({'signal':pd.to_datetime(['2020-01-31']),
       'entry':pd.to_datetime(['2020-02-03']),'exit':pd.to_datetime(['2020-03-02']),
       'asset':['A'],'y':[0.],'reegel':[1.]})
    bt,_=backtest(d,'reegel',cost=.01,top=1,cap=1)
    assert np.isclose(bt.net.iloc[0],-0.01/1.01)
    assert np.isclose(metrics([-.1,.2])['max_drawdown_monthly'],-.1)
    # Triiv: 50/50 muutub pärast +100% / 0% tootlust 2/3 ja 1/3.
    rows=[]
    for date,rets in [('2020-01-31',[1.,0.]),('2020-02-28',[0.,0.])]:
        for asset,r in zip(['A','B'],rets):
            rows.append({'signal':pd.Timestamp(date),'entry':pd.Timestamp(date)+pd.Timedelta(days=1),
                         'exit':pd.Timestamp(date)+pd.Timedelta(days=30),'asset':asset,'y':r,'reegel':1})
    bt,w=backtest(pd.DataFrame(rows),'baas',cost=0)
    assert np.isclose(bt.turnover.iloc[1],1/3)
    assert np.isclose(bt.net.iloc[0],.5)
    bt,w=backtest(pd.DataFrame(rows),'reegel',cost=0,top=2,cap=.3)
    assert (w[['A','B']]<=.3+1e-12).all().all()
    assert np.allclose(w.sum(axis=1),1)
    assert (w.CASH>=0).all()

def test_retrieval():
    assert all(d['id']!='D2' for d in retrieve('tulu kasvas','2024-02-29'))
    assert retrieve('tulu','2020-01-01')==[]

if __name__=='__main__':
    for f in [test_data,test_timing,test_money,test_retrieval]:
        f();print(f.__name__,'OK')
