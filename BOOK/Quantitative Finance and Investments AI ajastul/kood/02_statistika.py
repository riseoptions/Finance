from projekt import load_prices,OUT,metrics

def main():
 p=load_prices();r=p.pct_change(fill_method=None).dropna()
 result={c:metrics(r[c]) for c in r}
 import pandas as pd
 pd.DataFrame(result).T.to_csv(OUT/'statistika.csv');print(pd.DataFrame(result).T)
 print('Korrelatsioon:\n',r.corr())
if __name__=='__main__':main()
