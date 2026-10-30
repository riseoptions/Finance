"""Deterministlik raport; puudub LLM ja puuduvad kauplemisõigused."""
import json
import pandas as pd
from projekt import ROOT

def main():
    meta=json.loads((ROOT/'raportid/run.json').read_text(encoding='utf-8'))
    table=pd.read_csv(ROOT/'raportid/mootdikud.csv')
    if meta['data_kind'] != 'SYNTHETIC_ONLY':
        raise ValueError('See raportimall eeldab sünteetilist õppekatset.')
    lines=['# Automaatne uurimisraport', '', '**SÜNTEETILINE ÕPPEKATSE.**', '',
           '| Periood | Mudel | CAGR | Volatiilsus | Sharpe (rf=0) | Kuine MDD |',
           '|---|---|---:|---:|---:|---:|']
    for r in table.itertuples():
        lines.append(f'| {r.period} | {r.model} | {r.CAGR:.2%} | {r.vol:.2%} | {r.Sharpe_rf0:.3f} | {r.max_drawdown_monthly:.2%} |')
    lines += ['', 'Otsus: '+meta['decision'], '',
              'Järgmised tööd: punkt-ajas pärisandmed, kapasiteet, kulude kalibreerimine, sõltumatu test.', '',
              'Andmeräsi: `'+meta['sha256']+'`', '',
              'Riskivariandi viimase portfelli stsenaariumikahju: '+f"{meta['stress_last_portfolio']:.2%}.", '',
              'See pole maksimaalne võimalik kahju. Kuu sees tekkinud langusi mõõdik ei hõlma.']
    target=ROOT/'raportid/automaatraport.md'
    target.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(target)

if __name__=='__main__':main()
