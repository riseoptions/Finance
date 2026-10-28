# Pappi 7. peatüki koodinäite piiratud audit

[Tagasi avalehele](../README.md)

Kontrollitud 28.10.2026: [ch07.ipynb](https://github.com/StefanPapp/investing-for-programmers/blob/main/ch07.ipynb).

Allalaaditud faili SHA-256: `5d22857abd1a1e5a56fa0a14df9737461038c9e9ceaaf93e224fe6c2fd615853`.

Kontroll hõlmas kõigi 25 koodilahtri süntaksi parsimist Python 3.12-s ja valitud algoritmide lugemist. Kõik 25 läbisid süntaksikontrolli. Märkmikku ei käivitatud tervikuna: turuandmete ühendused, võtmetega teenused ja välised Exceli failid ei ole valideeritud. Süntaksi kehtivus ei tõenda teekide/API-de ühilduvust.

## Sisulised leiud

| Koht | Koodist nähtav asjaolu | Mõju ja parandamise suund |
|---|---|---|
| Esimene VaR-lahter | Tootlused simuleeritakse `np.random.normal(mu, sigma, num_simulations)` abil | Sabariski hindamine sõltub normaalmudeli sobivusest; lisa ajalooline ja stressipõhine võrdlus |
| Sama lahter | `time_horizon = 1` on määratud, aga simulatsiooni avaldis ei kasuta seda | Ainult selle muutuja muutmine ei muuda horisonti; mitme päeva mudel tuleb eraldi rakendada |
| Sama lahter | Tulemus saadakse ühe aktsia hinnamuutuse jaotusest | Dollaritulemus on ühe aktsia kohta, mitte suvalise portfelli VaR |
| Simulatsioonid | Juhuarvuseeme pole nendes näidetes fikseeritud | Sama sisendi korral võib tulemus muutuda; õppelaboris kasuta eraldi generaatorit ning seemet |
| Portfellide võrdlus | Keskmised, kovariatsioonid ja parim Sharpe hinnatakse samast ajaloolisest andmestikust | See kirjeldab valimi optimeerimist, mitte sõltumatult tõendatud tulevast tulemuslikkust |
| Juhuslikud portfellid | Valitakse parim 10 000 juhuslikult genereeritud kaaluvektorist | Tulemus ei tõesta globaalset optimumi ega ole täpne efektiivsuspiir |
| Hindade kogumine | Kasutatakse jooksva kuupäevaga akent ning võrguallikaid | Korduv käivitus võib muuta nii valimit kui andmete versiooni; salvesta andmed ja kuupäevad |
| Korrelatsiooni näide | Analüüs kasutab logtootlusi, mõnes teises lahtris lihttootlusi | Definitsioon tuleb säilitada; portfelli ühe perioodi lihttootlus on kaalutud lihttootluste summa, logtootluste summa pole täpne asendus |
| Aastatootluse joonis | Kood võtab `^GSPC` rea `Close` | Indeksi hinnaseeria ei ole automaatselt dividende reinvesteeriv kogutootlus; kontrolli allika definitsiooni |
| Andmete laadimine | `yfinance`, `pandas`, `scikit-learn`, joonised ja Exceli sisend | Keskkonna terviktest vajab versioonide, failide, andmevormingute ja võrgu kontrolli |

Need leiud ei tähenda, et õppemärkmik peaks olema tootmiskõlblik investeerimissüsteem. Need näitavad, mida tuleb lisada enne selle kasutamist investeerimisväite empiirilise tõendina. Selles arhiivis ei muudeta ega levitata autori märkmikku.

## Meie laborite kontrollitud keskkond

Python 3.12.14, NumPy 2.3.5. Graafiku loomisel Matplotlib 3.10.8; graafik on arhiivis valmis ja laboriskriptid Matplotlibi ei vaja. Kõik kolm laboriskripti käivitati. Märkmike kood kontrolliti skriptidega samaks ning käivitati eraldi ilma Colabi kasutajaliideseta. Colabi pilvekeskkonna integratsiooni pole testitud.

Matemaatiliste kontrollide hulka kuuluvad nullkorrelatsiooni hajutamisvalem, täiusliku korrelatsiooni piirjuht, VaR/ES-i täpsed väärtused, jaotuse masside jagamise invariantsus ning ES-i nihkeomadus. Simulatsiooni tulemusi võrreldi nulloskuse mudeli teoreetilise ootusega. Need kontrollid ei ole empiiriline turu-uuring.

## Laiendatud kontroll versioonis 0.2

Vaata [13 lähtefaili auditit](koodihoidla-laiendatud-audit.md). Siinne detailne 7. peatüki analüüs jääb kehtima; kogu koodi ühilduvust endiselt ei väideta.
