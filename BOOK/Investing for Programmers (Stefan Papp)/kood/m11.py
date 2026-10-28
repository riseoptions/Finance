"""[NÄIDE] Algoritmiline kauplemine ja järeltest — vt mooduli selgitust."""
from tuum import demo_hinnad,backtest,moodikud,tootlused
p=demo_hinnad().iloc[:,0]
for c in [0,.001,.003]:
    bt=backtest(p,cost=c)
    bh=tootlused(p.to_frame()).iloc[:,0].copy()
    bh.iloc[0]=(1+bh.iloc[0])*(1-c)-1
    bh.iloc[-1]=(1+bh.iloc[-1])*(1-c)-1
    print('Kulu',c,'SMA',moodikud(bt.neto),'osta-hoia',moodikud(bh))
