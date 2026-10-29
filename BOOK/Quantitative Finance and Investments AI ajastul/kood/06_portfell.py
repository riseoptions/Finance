import pandas as pd
from projekt import load_prices,portfolio,OUT
if __name__=='__main__':
 path=OUT/'test_returns.csv'
 if not path.exists():raise SystemExit('Käivita esmalt projekt.py')
 portfolio(load_prices(),pd.read_csv(path,index_col=0,parse_dates=True).index)
 print(pd.read_csv(OUT/'portfell.csv').to_string(index=False))
