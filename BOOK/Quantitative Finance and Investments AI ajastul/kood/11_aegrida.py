"""Väike mitmekihiline närvivõrk tootlusaknal, mitte LSTM/transformer.
Võrdlus nullprognoosi ja ridge'iga. Algandmed vaikimisi sünteetilised.
"""
import numpy as np,pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from projekt import load_prices,OUT

def main():
 p=load_prices().iloc[:,0];r=p.pct_change(fill_method=None)
 d=pd.DataFrame({f'lag_{i}':r.shift(i) for i in range(20)})
 d['y']=r.shift(-2);d=d.dropna();split=int(len(d)*.7)
 train,test=d.iloc[:split-2],d.iloc[split:];x=list(d.columns[:-1])
 rows=[{'model':'zero','mse':mean_squared_error(test.y,np.zeros(len(test)))}]
 for name,m in [('ridge',Ridge(alpha=10)),('MLP_16_8',MLPRegressor(hidden_layer_sizes=(16,8),
         alpha=10,max_iter=500,random_state=42,shuffle=False,early_stopping=False))]:
  model=make_pipeline(StandardScaler(),m)
  # Siht skaleeritakse protsendipunktideks ainult numbrilise õppimise hõlbustamiseks.
  model.fit(train[x],train.y*100);pred=model.predict(test[x])/100
  rows.append({'model':name,'mse':mean_squared_error(test.y,pred)})
 result=pd.DataFrame(rows);result.to_csv(OUT/'aegrida_mse.csv',index=False);print(result)
if __name__=='__main__':main()
