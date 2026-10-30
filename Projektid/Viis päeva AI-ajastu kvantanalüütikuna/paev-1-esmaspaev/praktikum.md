# Päev 1: praktikum

[PRAKTIKA] Tee kõigepealt [README käivitamisjuhend](../README.md) ja käivita `python/projekt.py`. Kõik põhiharjutused kasutavad kaasasolevaid sünteetilisi andmeid.

**Fail:** `python/paev1.py`. Vajalikud teegid: NumPy, pandas, Matplotlib ja scikit-learn (import läbi ühismooduli). Thonnys ava fail ja vajuta F5; terminalis projekti juurkaustas `python python/paev1.py`.

## Täielik lühinäide

```python
from projekt import load_data, validate
p = load_data()
validate(p)
returns = p.pct_change(fill_method=None)
momentum = p.pct_change(63, fill_method=None)
print('SÜNTEETILINE andmestik:', p.shape)
print('Viimane momentum:')
print(momentum.iloc[-1].sort_values(ascending=False).round(4))
print('Puuduvaid hindu:', int(p.isna().sum().sum()))
print('Päevatootluste keskmine:')
print(returns.mean().round(6))
```

**Oodatav väljund:** andmestiku mõõtmed ja viimased momendiskoorid. Täpsed tabelid on kaasas ja [tulemuste failis](../tulemused.md). Sinu masinas võib viimaste komakohtade ümardus erineda.

## Tee ja tõlgenda

Võrdle `p.pct_change(63)` ja `p.pct_change(21)`. Ära nimeta pärast võrdlust ilusamat varianti sõltumatuks avastuseks. Ava graafik `pildid/hinnad.png`; eri hinnatasemete võrdlemiseks vaata algväärtusele 1 normaliseeritud jooni.

Kirjuta 3–5 lauset: mida sisend tähendab, mida arvutus teeb, mida saadud arv tõendab ja mida ei tõenda. Pikema teostuse täielik kood on [projekt.py](../python/projekt.py); iga funktsioon vastab ühele tööetapile: andmed, paneel, prognoos, kaalud, simulatsioon, mõõdikud.

## Tõrgete lahendamine

`ModuleNotFoundError`: paigalda pakett samasse Pythoni keskkonda, mida Thonny kasutab. `FileNotFoundError` raporti puhul: käivita esmalt põhiskript ja säilita ZIP-i kaustastruktuur. Puuduvate või duplikaatsete hindade kontroll: paranda sisendallikas, ära kommenteeri kontrolli välja. `sklearn` impordi pakett on `scikit-learn`.

Võrguharu vea korral kasuta sünteetilist faili; see ei vaja Yahoo ühendust. Ära nimeta sünteetilisi hindu pärisandmete edukaks allalaadimiseks.

Edasi: [ülesanded ja lahendused](ulesanded-lahendused.md).
