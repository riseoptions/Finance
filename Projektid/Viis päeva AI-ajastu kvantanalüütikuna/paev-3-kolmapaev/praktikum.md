# Päev 3: praktikum

[PRAKTIKA] Tee kõigepealt [README käivitamisjuhend](../README.md) ja käivita `python/projekt.py`. Kõik põhiharjutused kasutavad kaasasolevaid sünteetilisi andmeid.

**Fail:** `python/paev3.py`. Vajalikud teegid: NumPy, pandas, Matplotlib ja scikit-learn (import läbi ühismooduli). Thonnys ava fail ja vajuta F5; terminalis projekti juurkaustas `python python/paev3.py`.

## Täielik lühinäide

```python
import pandas as pd
from projekt import ROOT
m = pd.read_csv(ROOT/'raportid/prognoosimootdikud.csv')
r = pd.read_csv(ROOT/'raportid/mootdikud.csv')
print('Prognoos:')
print(m[m.period == 'valideerimine'].to_string(index=False))
print('Portfell:')
print(r[r.period == 'valideerimine'].to_string(index=False))
print('55% tabamus, 1 euro võit, 1.5 euro kaotus:', .55*1-.45*1.5)
```

**Oodatav väljund:** prognoosi ja portfelli valideerimistabelid. Täpsed tabelid on kaasas ja [tulemuste failis](../tulemused.md). Sinu masinas võib viimaste komakohtade ümardus erineda.

## Tee ja tõlgenda

Leia väikseima RMSE-ga mudel ning võrdle tema käivet. Kas madalam viga annab kõrgema netotootluse? Täiendavalt rühmita `raportid/prognoosid.csv` aastate järgi. Ära kasuta seda sama lõppkatse järgi mudeli ümbervalimiseks.

Kirjuta 3–5 lauset: mida sisend tähendab, mida arvutus teeb, mida saadud arv tõendab ja mida ei tõenda. Pikema teostuse täielik kood on [projekt.py](../python/projekt.py); iga funktsioon vastab ühele tööetapile: andmed, paneel, prognoos, kaalud, simulatsioon, mõõdikud.

## Tõrgete lahendamine

`ModuleNotFoundError`: paigalda pakett samasse Pythoni keskkonda, mida Thonny kasutab. `FileNotFoundError` raporti puhul: käivita esmalt põhiskript ja säilita ZIP-i kaustastruktuur. Puuduvate või duplikaatsete hindade kontroll: paranda sisendallikas, ära kommenteeri kontrolli välja. `sklearn` impordi pakett on `scikit-learn`.

Võrguharu vea korral kasuta sünteetilist faili; see ei vaja Yahoo ühendust. Ära nimeta sünteetilisi hindu pärisandmete edukaks allalaadimiseks.

Edasi: [ülesanded ja lahendused](ulesanded-lahendused.md).
