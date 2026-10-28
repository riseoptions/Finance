"""[NÄIDE] Graafikud ja tehnilised indikaatorid — vt mooduli selgitust."""
from tuum import demo_hinnad,indikaatorid
print(indikaatorid(demo_hinnad().iloc[:,0]).tail().round(3).to_string())

s=demo_hinnad().iloc[:,0]
macd=s.ewm(span=12,adjust=False).mean()-s.ewm(span=26,adjust=False).mean()
signal=macd.ewm(span=9,adjust=False).mean()
print('MACD viimane:',round(macd.iloc[-1],4),'histogramm:',round((macd-signal).iloc[-1],4))
