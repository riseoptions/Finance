# Testimis- ja kontrolliaruanne

Kontrollitud 30.10.2026. Keskkond: Python 3.12.14, SQLite 3.53.1, scikit-learn 1.8.0. Testid käivitati Linuxi terminalis; Thonny ja Colabi kasutajaliideseid ei avatud.

| Kontroll | Tulemus | Tähendus |
|---|---|---|
| Kõik 20 laborikäsku | Edukad | Skriptid käivituvad kaasasolevate andmetega |
| Automaatkontrollid | 12/12 läbis | Import, versioonid, räsi, tee piirang, SQL, viited, API skeem |
| Põhiraport | Genereeritud | Kõik 12 tõendit on raporti registris |
| Arvuline kontroll | +20%; −4%; mediaan 5%; keskmine 9,75% | Algandmetega võrreldud |
| ML testikomplekt | macro-F1 0.9441 | Sünteetiline 18-realise, 6 perekonnaga testikogum |
| Enamusrühma baasjoon | macro-F1 0.1667 | Võrdlus sama testiga |
| Tõendiotsing | 5/5 küsimusel vajalik dokument top-3 hulgas | Väike nähtav etalon, mitte sõltumatu kvaliteeditõend |
| Korpuseväline päring | Tühi tulemus | Üks vastamata küsimuse test |
| Elus PxWeb GET | Edukas, 7 kataloogikirjet | Üks metaandmete päring; ei testi kõiki tabeleid |
| Colabi märkmik | JSON ja koodilahtrite süntaks korras | Colabi enda sessioonis ei käivitatud |
| Päris LLM | Ei käivitatud | Prompti loomine ja viite/tsitaadi valideerimine testitud |

## Eluspäringu jälg

URL: https://andmed.stat.ee/api/v1/et/stat

Kogumisaeg: 2026-10-30T15:37:06.399789+00:00

SHA-256: `5465114243cac5a56cf3513d420de938669179a86a25fef027fe4c8587471bdd`. Vastus ja metaandmed on reports kaustas; andmed kirjeldavad statistikatabelite kataloogi, mitte fiktiivset projekti.

## Analüütiliste tulemuste kontroll

- E01 → 1000000; E02 → 1200000; E03 → 1250000. Erinevus algse suhtes 200000/1000000 = 20%; muudetud suhtes −50000/1250000 = −4%.
- contracts.csv 12 muutust protsentides: 20, 2, 5, −5, 10, 5, 5, 10, 5, 5, 5, 50. Summa 117; keskmine 117/12 = 9,75. Kuues ja seitsmes järjestatud väärtus on 5, seega mediaan 5.
- E04 väide 1500000 on E05-s parandatud; E06 sõltub E04-st. Raport ei loe neid sõltumatuteks kinnitusteks.
- E08 tõendab ainult sünteetilise loa väljavõtte olemasolu ja kuupäeva; tööde tegelik algus jääb teadmata.
- E09 ütleb aadress, mitte omand. Graaf säilitab selle eristuse.
- E10-sse lisatud failiräsid kattuvad CSVdega. Iga tõendi SQLite tekst ja hetktõmmis on kontrollitavad.

## Olulised piirid

ML-korpus on kunstlikult lihtne, sisaldab ühe teksti variante ning ei esinda Eesti avaliku meedia jaotust. Grupijaotus väldib sama tekstiperekonna sattumist treeningusse ja testi, kuid ei muuda korpust realistlikuks. Testis on üks vale klassifikatsioon. Suur F1 ei õigusta pärisandmetele ülekandmist.

RAG-i mõõdikud kontrollivad otsingut, mitte genereerimise faktilist õigsust. Sisuliselt vastuseta, kuid samateemaline maksete küsimus võib leida eelarve dokumendi; inimene peab tuvastama, et see ei vasta küsimusele. Viitevalideerija ei kontrolli loogilist järeldumist.

API üks päring õnnestus; registriportaalide autentimist ja 40 kanali ligipääsu ei testitud. Allikakataloog eristab dokumentatsiooni kontrolli, veebilehe avamist ja kontrollimata lisakanaleid. Raamatu kõiki võtteid ei proovitud. Tegelikud Eesti registriandmed ei ole fiktiivse juhtumi tõendid.

[Testide toorlogi](testid.txt) · [20 labori väljundid](laborite_logi.md) · [ML mõõdikud](ml_metrics.json) · [otsingu mõõdikud](rag_metrics.json).
