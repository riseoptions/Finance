# Päev 5: praktikum

[PRAKTIKA] Tee kõigepealt [README käivitamisjuhend](../README.md) ja käivita `python/projekt.py`. Kõik põhiharjutused kasutavad kaasasolevaid sünteetilisi andmeid.

**Fail:** `python/paev5.py`. Vajalikud teegid: NumPy, pandas, Matplotlib ja scikit-learn (import läbi ühismooduli). Thonnys ava fail ja vajuta F5; terminalis projekti juurkaustas `python python/paev5.py`.

## Täielik lühinäide

```python
from raport import main
main()
print('Vaata raportid/automaatraport.md ja otsusta, milline tõend veel puudub.')
```

**Oodatav väljund:** raportid/automaatraport.md. Täpsed tabelid on kaasas ja [tulemuste failis](../tulemused.md). Sinu masinas võib viimaste komakohtade ümardus erineda.

## Tee ja tõlgenda

Võrdle automaatraportit lähte-CSV-ga. Sõnasta kolm tõendamata väidet, mida raport ei tohi esitada. Käivita `python/rag_demo.py`; hilisem D2 peab jääma veebruari otsusest välja.

Kirjuta 3–5 lauset: mida sisend tähendab, mida arvutus teeb, mida saadud arv tõendab ja mida ei tõenda. Pikema teostuse täielik kood on [projekt.py](../python/projekt.py); iga funktsioon vastab ühele tööetapile: andmed, paneel, prognoos, kaalud, simulatsioon, mõõdikud.

## Tõrgete lahendamine

`ModuleNotFoundError`: paigalda pakett samasse Pythoni keskkonda, mida Thonny kasutab. `FileNotFoundError` raporti puhul: käivita esmalt põhiskript ja säilita ZIP-i kaustastruktuur. Puuduvate või duplikaatsete hindade kontroll: paranda sisendallikas, ära kommenteeri kontrolli välja. `sklearn` impordi pakett on `scikit-learn`.

Võrguharu vea korral kasuta sünteetilist faili; see ei vaja Yahoo ühendust. Ära nimeta sünteetilisi hindu pärisandmete edukaks allalaadimiseks.

Edasi: [ülesanded ja lahendused](ulesanded-lahendused.md).
