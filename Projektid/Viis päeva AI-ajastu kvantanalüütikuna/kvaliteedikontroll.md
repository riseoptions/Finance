# Kvaliteedikontroll ja täitmise ulatus

## Tegelikult tehtud

- Mõlema lisatud PDF-i tiitliandmed, sisukord ja oluliste teemade sihtlugemine; allikakaart eristab trüki- ja PDF-lehti.
- Põhiprojekt käivitatud Python 3.12.14 keskkonnas. Testitud paketiversioonid on `requirements-tested.txt` ja `raportid/run.json`.
- Numbrilised tulemused toodetud kaasasolevast sünteetilisest CSV-st. Juhuseeme ja andmeräsi on säilitatud.
- Vigaste hindade ja duplikaatide tagasilükkamine kontrollitud.
- Signaal → täitmine → sildi lõpp ajajärjestus kontrollitud.
- Tulevaste hindade muutmine jättis varasemad tunnused ja kontrollitud kuu mudeliprognoosid samaks.
- Esmaostu kulu, kaalude triiv, kaalupiir, raha osakaal ja esimese perioodi languse arvestus kontrollitud käsitsi tuletatud näidetega.
- Retrieval-demo välistab otsuse kuupäevast hilisema dokumendi.
- Kõik lühiskriptid, matemaatikakontroll ja automaatraport käivitatud; väljundid kaustas `raportid/kontroll_*.txt`.
- Neli graafikut visuaalselt kontrollitud; kapitaligraafik sisaldab algväärtust 1 ja langusgraafik algkapitali.
- Märkmiku JSON ja koodisüntaks kontrollitud. Markdowni kohalikud faililingid kontrollitud.

## Teadlikud piirid ja tegemata välised katsed

- Yahoo/yfinance pärisandmete laadimise võrgukäivitust ei tehtud. Skripti süntaks kontrollitud; teenuse vastus ja õigused sõltuvad kasutaja keskkonnast.
- Google Colabi brauseri üleslaadimisdialoogi ega Windowsi Thonny kasutajaliidest siin ei käivitatud. Märkmik kasutab sama testitud projekti, mitte uut finantsimplementatsiooni.
- XGBoost, süvaõpe ja päris LLM API pole põhivõrdluses käivitatud. Random Forest täidab ML-võrdluse rolli; ülejäänud meetodite kasutusotsust selgitatakse tekstis.
- RAG-demo teeb ajafiltriga otsingu, mitte generatiivset vastamist. Automaatraport on skript, mitte agent. Täisagendi lisamine jääb põhjendatud edasise töö võimaluseks.
- Punkt-ajas päristuru universumit, orderiraamatut, osatäitmist, makse, laenukulu ega maakleri paper trading'ut ei kontrollitud.
- Testid katavad konkreetsed finants- ja ajastusomadused; need ei tõesta koodi kõigi võimalike vigade puudumist ega strateegia turueelist.

## Pedagoogiline kontroll

Viiel päeval on ühtne A–I lugu, oma teooria, praktikum ja lahendused. Igal päeval on viis kontrollküsimust, kaks praktilist ülesannet, arvutus, Python-demo ja otsustamisolukord. Lisatud on 30 tüübi ja piiranguga põhimõtet, 20 aruteluküsimust, viie tunni õpetajamaterjal, mõistesõnastik ja tulevikustsenaariumid.

Viiepäevane lugu ei väida aastate pikkuse pärisuurimise läbimist. Tulemuseks on terviklik õppekursus; järgmised pärisandme- ja kasutuselevõtu katsed on kursuses selgelt eristatud.
