"""Valikuline pärisandmete laadimine. Vajab internetti ja yfinance'i; võtit ei vaja."""
from datetime import datetime, timezone
import json
from tuum import ROOT, kontrolli_hindu

def main():
    import yfinance as yf
    import pandas as pd
    tickers=['SPY','AAPL','MSFT']
    raw=yf.download(tickers,start='2019-01-01',end='2025-01-01',
                    auto_adjust=True,progress=False,multi_level_index=True)
    if raw is None or raw.empty: raise RuntimeError('Yahoo ei tagastanud hindu. Kasuta offline-demot.')
    close=raw['Close'].reindex(columns=tickers).sort_index()
    before=len(close); close=close.dropna(how='any')
    kontrolli_hindu(close)
    if len(close)<100: raise RuntimeError('Liiga vähe ühiseid vaatlusi.')
    path=ROOT/'andmed'/'yahoo_hinnad.csv';close.to_csv(path,index_label='Date')
    meta={'source':'Yahoo Finance läbi yfinance','tickers':tickers,'auto_adjust':True,
          'end_exclusive':'2025-01-01','downloaded_utc':datetime.now(timezone.utc).isoformat(),
          'dropped_rows':before-len(close),'note':'Tagantjärele valitud varad, mitte ajalooline indeksikoosseis.'}
    path.with_suffix('.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print(path);print('Ühiseid kuupäevi:',len(close),'eemaldatud:',before-len(close))
if __name__=='__main__': main()
