# Päev 2: praktikum

[PRAKTIKA] Tee kõigepealt [README käivitamisjuhend](../README.md) ja käivita `python/projekt.py`. Kõik põhiharjutused kasutavad kaasasolevaid sünteetilisi andmeid.

**Fail:** `python/paev2.py`. Vajalikud teegid: NumPy, pandas, Matplotlib ja scikit-learn (import läbi ühismooduli). Thonnys ava fail ja vajuta F5; terminalis projekti juurkaustas `python python/paev2.py`.

## Täielik lühinäide

```python
from projekt import load_data, panel, backtest, metrics
p = load_data()
d = panel(p)
d['reegel'] = d.mom63 / 3
validation = d[(d.signal >= '2019') & (d.signal < '2022')]
for name in ['baas', 'reegel']:
    result, weights = backtest(validation, name, p)
    print(name, metrics(result.net))
    print(result[['entry','exit','gross','cost','net']].head(2))
print('Üks käsitsi kontroll:', 1.2*.8-1)
```

**Oodatav väljund:** valideerimisperioodi baas- ja reeglipõhised mõõdikud. Täpsed tabelid on kaasas ja [tulemuste failis](../tulemused.md). Sinu masinas võib viimaste komakohtade ümardus erineda.

## Tee ja tõlgenda

Leia üks kuu ja kontrolli `(1-cost)*(1+gross)-1`. Seejärel võrdle kulumäärasid failis `raportid/kulutundlikkus.csv`. Kui muudad parameetreid, on see uus uurimiskatse, mis tuleb päevikusse kirjutada.

Kirjuta 3–5 lauset: mida sisend tähendab, mida arvutus teeb, mida saadud arv tõendab ja mida ei tõenda. Pikema teostuse täielik kood on [projekt.py](../python/projekt.py); iga funktsioon vastab ühele tööetapile: andmed, paneel, prognoos, kaalud, simulatsioon, mõõdikud.

## Tõrgete lahendamine

`ModuleNotFoundError`: paigalda pakett samasse Pythoni keskkonda, mida Thonny kasutab. `FileNotFoundError` raporti puhul: käivita esmalt põhiskript ja säilita ZIP-i kaustastruktuur. Puuduvate või duplikaatsete hindade kontroll: paranda sisendallikas, ära kommenteeri kontrolli välja. `sklearn` impordi pakett on `scikit-learn`.

Võrguharu vea korral kasuta sünteetilist faili; see ei vaja Yahoo ühendust. Ära nimeta sünteetilisi hindu pärisandmete edukaks allalaadimiseks.

Edasi: [ülesanded ja lahendused](ulesanded-lahendused.md).
