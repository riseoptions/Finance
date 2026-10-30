# Viis päeva AI-ajastu kvantanalüütikuna

**Üks realistlik töönädal kvantitatiivses investeerimisfirmas – ideest matemaatilise mudeli, AI-analüüsi ja investeerimisotsuseni.**

Eestikeelne jutustav ja praktiline kursus. Narangi *Inside the Black Box*, 3. väljaanne (2024), annab süsteemi mõtestamise raami; Janseni *Machine Learning for Trading*, 3. väljaanne (2026), uurimistöö tehnilise raami. See on iseseisev originaalne õppeprojekt, mitte raamatute tõlge ega nende kõigi peatükkide asendus.

Sa töötad koos fiktiivse analüütiku Maarikaga: sõnastad hüpoteesi, avastad andmelekke, võrdled lihtsat reeglit Ridge'i ja Random Forestiga, piirad portfelli riski ning kaitsed otsust investeerimiskomitees. Kõige tähtsam väljund pole kasuminumber, vaid kontrollitav otsus.

> **Andmete staatus:** komplektis olevad hinnad ja kõik arvutatud tulemused on SÜNTEETILISED. `SYN_XLK` ei ole XLK tegelik hind. Töövoog ei tõenda turueelise olemasolu. Pärisandmete laadimine on eraldi, valikuline ja selle võrgupäringut siin ei testitud.

## Õppejärjekord ja maht

Eelteadmised: Pythoni muutujad, funktsioonid ja tabelid; protsendid, keskmine ja standardhälve. SQL tuleb kasuks, kuid pole käivitamiseks vajalik. Iga päev 150 minutit: lugu 25, teooria 30, praktikum 55, ülesanded 30, kokkuvõte 10. Kokku 12,5 tundi; lisade ja süvaülesannete aeg on eraldi.

| Päev | Küsimus | Loe ja tee | Päeva väljund |
|---|---|---|---|
| 1 | Mida üldse katsetame? | [Esmaspäev](paev-1-esmaspaev/lugu.md) | Hüpotees ja andmeleping |
| 2 | Kas ajalugu on ausalt simuleeritud? | [Teisipäev](paev-2-teisipaev/lugu.md) | Baasstrateegia ja kulud |
| 3 | Kas ML lisab väärtust? | [Kolmapäev](paev-3-kolmapaev/lugu.md) | Kolme meetodi võrdlus |
| 4 | Kui palju riski võtame? | [Neljapäev](paev-4-neljapaev/lugu.md) | Piiratud portfell ja stress |
| 5 | Mida tõendid lubavad otsustada? | [Reede](paev-5-reede/lugu.md) | Raport ja edasise katse otsus |

Alusta [sissejuhatusest](00-sissejuhatus.md) ja [tegelastest](00-tegelased-ja-tookeskkond.md). Iga päev sisaldab eraldi lugu, teooriat, praktikumi ning lahendustega ülesandeid.

## Käivitamine Windows 11-s

1. Paki ZIP lahti. Säilita kaustastruktuur.
2. Thonnys vali **Tools → Manage packages** ja paigalda `numpy`, `pandas`, `matplotlib`, `scipy`, `scikit-learn` (paketi nimi erineb impordist `sklearn`).
3. Ava `python/projekt.py` ja vajuta F5. Failiteed lähtuvad skripti asukohast, mitte aktiivsest kaustast.
4. Vaata `raportid/mootdikud.csv`, `raportid/run.json` ja `pildid/kapital.png`.
5. Käivita `python/testid.py` ning `python/raport.py`. Päevade lühiskriptid eeldavad, et `projekt.py` on vähemalt korra käivitatud.

Terminalis projekti juurkaustast:

```bash
python -m pip install -r requirements.txt
python python/projekt.py
python python/testid.py
python python/raport.py
```

[Colabi märkmik](colab/kursus.ipynb) palub ZIP-i üles laadida ja käivitab sama koodi. Google Colab vajab brauseriühendust; andmeanalüüs ise ei vaja turuandmete allalaadimist. VS Code pole vajalik.

Põhikood on tahtlikult ühes loetavas moodulis. Suurema ettevõtte süsteem jaotaks andmed, prognoosid, tehingud ja seire teenusteks; siin vähendaks see õppimise selgust.

## Täiendavad materjalid

- [Allikad ja raamatute teemakaart](allikad.md)
- [Uurimisprotokoll ja ajastus](uurimisprotokoll.md)
- [Matemaatiline meelespea](matemaatika.md)
- [30 põhimõtet](kvandi-30-pohimotet.md) ja [20 keerulist küsimust](20-keerulist-kusimust.md)
- [Varem ja nüüd](enne-ja-nuud.md), [tulevikustsenaariumid](tulevik-2027-2030.md)
- [Ametid](kvandi-ametid.md), [finantsinstrumendid](finantsinstrumendid.md), [sõnastik](sonastik.md)
- [Õpetaja käsiraamat](opetaja-kasiraamat.md) ja [AI-promptid](ai-ja-promptid.md)
- [Kontrollitud simulatsioonitulemused](tulemused.md) ja [kvaliteedikontroll](kvaliteedikontroll.md)

## Tehnilised piirid

Kuine, long-only, võimenduseta uurimissimulaator. Täitmine järgmise vaatluspäeva sulgemisel on mudelieeldus. Korrigeeritud hinnad on tootluse proksi, mitte ajalooliselt kaubeldavad nominaalhinnad. Põhimudel ei simuleeri orderiraamatut, makse, turumõju, osatäitmisi ega sulgemisoksjoni piiranguid. Kuupõhine langus alahindab võimalikku päevasisest langust. Tehinguid pärisrahaga ei tehta.

Algne andmestik on deterministlik. Treeninguajad sõltuvad arvutist; teekide versioonid salvestatakse. Testitud versioonid on failis `requirements-tested.txt`; tavaliseks kasutamiseks on `requirements.txt` paindlikum. Raamatute PDF-e, API-võtmeid ega võõrast lähtekoodi pakett ei sisalda.
