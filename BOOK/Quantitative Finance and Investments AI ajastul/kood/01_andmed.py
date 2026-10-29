"""Vaikimisi simuleerib. --download laadib Yahoo kaudu ajaloolised hinnad.
Näide: python kood/01_andmed.py --download
Valitud tänased kolm ettevõtet EI OLE ellujäämiskallutusteta USA universum.
"""
import argparse,json
from datetime import datetime,timezone
from projekt import DATA,synthetic

def main():
 p=argparse.ArgumentParser();p.add_argument('--download',action='store_true');a=p.parse_args()
 if a.download:
  import yfinance as yf
  raw=yf.download(['AAPL','MSFT','JPM'],start='2018-01-01',end='2026-01-01',auto_adjust=True,progress=False)
  prices=raw['Close'].dropna(how='all')
  if prices.empty or prices.isna().any().any():raise ValueError('Tühi või puudulik andmestik; ära jätka.')
  meta={'kind':'HISTORICAL_YAHOO','provider':'yfinance / Yahoo Finance','auto_adjust':True,
        'symbols':['AAPL','MSFT','JPM'],'end_exclusive':'2026-01-01',
        'limitation':'Current survivors, revised adjusted series; NOT point-in-time universe.'}
 else:prices=synthetic();meta={'kind':'SIMULATED','seed':42}
 prices.rename_axis('date').to_csv(DATA/'hinnad.csv')
 meta['downloaded_at_utc']=datetime.now(timezone.utc).isoformat()
 (DATA/'provenance.json').write_text(json.dumps(meta,indent=2));print(meta)
if __name__=='__main__':main()
