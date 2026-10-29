"""Kogu valimi illustratsioon, MITTE sõltumatu lõppkatse."""
from projekt import load_prices,net_returns,metrics

def main():
 p=load_prices().iloc[:,0];r=p.pct_change(fill_method=None).dropna()
 w=(p>p.rolling(50).mean()).astype(float).shift(2)
 net,_=net_returns(r,w,10);print(metrics(net))
 print('Arendusillustratsioon. Ametlik mudelite võrdlus: projekt.py lõppkatse.')
if __name__=='__main__':main()
