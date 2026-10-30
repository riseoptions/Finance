"""Valikuline võrguharu: pip install yfinance. Võrgukäivitust pole paketis testitud."""
from pathlib import Path
import json, hashlib
from datetime import datetime, timezone
import yfinance as yf
from projekt import validate
ROOT = Path(__file__).resolve().parents[1]
TICKERS = ['XLK','XLF','XLE','XLV','XLI','XLP']
raw = yf.download(TICKERS, start='2012-01-01', end='2026-01-01',
                  auto_adjust=True, progress=False, threads=False)
if raw.empty:
    raise RuntimeError('Andmepakkuja ei tagastanud andmeid; ära asenda neid nullidega.')
p = raw['Close'].reindex(columns=TICKERS)
p.index = p.index.tz_localize(None)
validate(p)
path = ROOT/'andmed/paris_hinnad.csv'
p.to_csv(path)
meta = {'source':'Yahoo Finance via yfinance', 'version':yf.__version__,
        'retrieved_at':datetime.now(timezone.utc).isoformat(),
        'auto_adjust':True, 'end_exclusive':'2026-01-01',
        'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'note':'Eraldi sisend; põhiprojekti sünteetilisi tulemusi ei asenda.'}
(ROOT/'andmed/paris_meta.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print(path)
