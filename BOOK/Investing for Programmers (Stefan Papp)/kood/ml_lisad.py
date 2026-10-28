"""Klassifitseerimine ja klasterdamine simuleeritud andmetel; --xgboost on valikuline."""
import argparse
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score,brier_score_loss,mean_squared_error
from sklearn.cluster import KMeans
from tuum import demo_hinnad,ml_andmed,tootlused

def main(xgboost=False):
    p=demo_hinnad();d=ml_andmed(p.iloc[:,0]);cut=int(.8*len(d))
    X=d.drop(columns='target'); y=(d.target>0).astype(int)
    for name,model in [('enamus',DummyClassifier(strategy='prior')),
                      ('logistiline',make_pipeline(StandardScaler(),LogisticRegression(C=.1,max_iter=500)))]:
        model.fit(X.iloc[:cut-1],y.iloc[:cut-1])
        prob=model.predict_proba(X.iloc[cut:])[:,1]
        print(name,'täpsus',round(accuracy_score(y.iloc[cut:],prob>=.5),4),
              'Brier',round(brier_score_loss(y.iloc[cut:],prob),4))
    # Kirjeldav rühmitus ainult arendusperioodist, mitte tulevase tootluse prognoos.
    r=tootlused(p.iloc[:cut]); features=np.column_stack([r.mean()*252,r.std()*np.sqrt(252)])
    labels=make_pipeline(StandardScaler(),KMeans(n_clusters=2,n_init=10,random_state=42)).fit_predict(features)
    print('Kirjeldavad klastrid (vaid 3 demo-vara):',dict(zip(p.columns,labels.tolist())))
    if xgboost:
        from xgboost import XGBRegressor
        model=XGBRegressor(n_estimators=50,max_depth=2,learning_rate=.03,random_state=42,n_jobs=1)
        model.fit(X.iloc[:cut-1],d.target.iloc[:cut-1])
        print('XGBoost test-RMSE',float(np.sqrt(mean_squared_error(d.target.iloc[cut:],model.predict(X.iloc[cut:])))))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--xgboost',action='store_true');main(p.parse_args().xgboost)
