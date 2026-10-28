"""Käivita Thonnys F5 või python kood/projekt.py. Ei saada tehinguid."""
import json
import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from tuum import ROOT, OUT, demo_hinnad, kontrolli_hindu, tootlused, moodikud, osta_hoia, backtest, ml_vordlus

def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--csv', help='Date indeksiga positiivsete korrigeeritud hindade CSV')
    args=parser.parse_args()
    p=pd.read_csv(args.csv,index_col=0,parse_dates=True) if args.csv else demo_hinnad()
    kontrolli_hindu(p)
    source='KASUTAJA_CSV: '+args.csv if args.csv else 'SIMULEERITUD; ei ole ajalooline USA turuandmestik'
    r=tootlused(p)
    stats=pd.DataFrame({c:moodikud(r[c]) for c in p}).T
    weights=[1/len(p.columns)]*len(p.columns)
    port=osta_hoia(p,weights)
    stats.loc['osta_hoia_vordsed_algkaalud']=moodikud(port)
    stats.to_csv(OUT/'moodikud.csv')
    p.to_csv(OUT/'kasutatud_hinnad.csv',index_label='Date')
    with sqlite3.connect(OUT/'kursus.sqlite') as con:
        p.rename_axis('Date').reset_index().to_sql('hinnad',con,if_exists='replace',index=False)
    bt=backtest(p.iloc[:,0]); bt.to_csv(OUT/'backtest.csv')
    ml,split=ml_vordlus(p.iloc[:,0]); ml.to_csv(OUT/'mudelid.csv',index=False)
    normalized=p/p.iloc[0]
    normalized['Portfell']=(1+port).cumprod().reindex(p.index,fill_value=1)
    ax=normalized.plot(figsize=(10,5),title='Väärtus algväärtuse suhtes — '+('SIMULATSIOON' if not args.csv else 'CSV'))
    ax.set_ylabel('Algväärtus = 1'); ax.figure.tight_layout();ax.figure.savefig(OUT/'portfell.png');plt.close(ax.figure)
    report='# USA turu analüüsi tugisüsteem: õppedemo\n\n'
    report+='Andmeallikas: '+source+'\n\n'
    report+='## Tootlus ja risk\n\n```text\n'+stats.round(4).to_string()+'\n```\n\n'
    report+='Portfell: võrdsed algkaalud, osta-ja-hoia, kuludeta; kaalud triivivad. Võrdlusvara on CSV esimene veerg.\n\n'
    report+='## Mudelid\n\n```text\n'+ml.round(6).to_string(index=False)+'\n```\n\n'
    report+='Ajapiirid: '+json.dumps(split,ensure_ascii=False)+'\n\n'
    report+='## SMA strateegia\n\n```json\n'+json.dumps(moodikud(bt.neto),indent=2)+'\n```\n\n'
    report+='Tehingukulu 0,1% ühes suunas; signaal t sulgemise järel, täitmine t+1 sulgemisel. Raha intress 0.\n\n'
    report+='Madal prognoosiviga ei tõenda kasumlikku strateegiat. Fundamentaal- ja dokumendiuuring on eraldi praktikumid; raport ei sisalda automaatset ostusoovitust.\n'
    (OUT/'raport.md').write_text(report,encoding='utf-8')
    print(stats.round(4).to_string()); print(ml.round(6).to_string(index=False));print('Raport:',OUT/'raport.md')
if __name__=='__main__': main()
