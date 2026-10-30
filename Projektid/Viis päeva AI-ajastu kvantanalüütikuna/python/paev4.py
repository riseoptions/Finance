import pandas as pd
from projekt import ROOT, ASSETS
w = pd.read_csv(ROOT/'raportid/lopptest_risk_kaalud.csv', index_col=0)
shock = pd.Series([-.12,-.15,-.18,-.08,-.12,-.06],index=ASSETS)
print('Viimased kaalud:', w.iloc[-1].round(4).to_dict())
print('Stressikahju:', float(w.iloc[-1][ASSETS] @ shock))
print('Kahe vara volatiilsus:', (.25*.04+.25*.04+2*.5*.5*(-.5)*.2*.2)**.5)
