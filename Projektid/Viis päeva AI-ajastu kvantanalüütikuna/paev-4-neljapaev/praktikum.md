# Päev 4: praktikum

[PRAKTIKA] Tee kõigepealt [README käivitamisjuhend](../README.md) ja käivita `python/projekt.py`. Kõik põhiharjutused kasutavad kaasasolevaid sünteetilisi andmeid.

**Fail:** `python/paev4.py`. Vajalikud teegid: NumPy, pandas, Matplotlib ja scikit-learn (import läbi ühismooduli). Thonnys ava fail ja vajuta F5; terminalis projekti juurkaustas `python python/paev4.py`.

## Täielik lühinäide

```python
import pandas as pd
from projekt import ROOT, ASSETS
w = pd.read_csv(ROOT/'raportid/lopptest_risk_kaalud.csv', index_col=0)
shock = pd.Series([-.12,-.15,-.18,-.08,-.12,-.06],index=ASSETS)
print('Viimased kaalud:', w.iloc[-1].round(4).to_dict())
print('Stressikahju:', float(w.iloc[-1][ASSETS] @ shock))
print('Kahe vara volatiilsus:', (.25*.04+.25*.04+2*.5*.5*(-.5)*.2*.2)**.5)
```

**Oodatav väljund:** viimased kaalud ning stressikahju ligikaudu −11,23%. Täpsed tabelid on kaasas ja [tulemuste failis](../tulemused.md). Sinu masinas võib viimaste komakohtade ümardus erineda.

## Tee ja tõlgenda

Muuda šokivektori tehnoloogiasektori kahju −12%-lt −25%-le. Muutus portfelli kahjus võrdub selle vara kaal korda −13 protsendipunkti. Kontrolli, et raha kaal ei saa sama aktsiašokki.

Kirjuta 3–5 lauset: mida sisend tähendab, mida arvutus teeb, mida saadud arv tõendab ja mida ei tõenda. Pikema teostuse täielik kood on [projekt.py](../python/projekt.py); iga funktsioon vastab ühele tööetapile: andmed, paneel, prognoos, kaalud, simulatsioon, mõõdikud.

## Tõrgete lahendamine

`ModuleNotFoundError`: paigalda pakett samasse Pythoni keskkonda, mida Thonny kasutab. `FileNotFoundError` raporti puhul: käivita esmalt põhiskript ja säilita ZIP-i kaustastruktuur. Puuduvate või duplikaatsete hindade kontroll: paranda sisendallikas, ära kommenteeri kontrolli välja. `sklearn` impordi pakett on `scikit-learn`.

Võrguharu vea korral kasuta sünteetilist faili; see ei vaja Yahoo ühendust. Ära nimeta sünteetilisi hindu pärisandmete edukaks allalaadimiseks.

Edasi: [ülesanded ja lahendused](ulesanded-lahendused.md).
