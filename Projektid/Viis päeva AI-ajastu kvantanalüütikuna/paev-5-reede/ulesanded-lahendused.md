# Päev 5: kontrollküsimused ja ülesanded

Proovi enne vastuse lugemist iseseisvalt. Baastase: mõisted; rakendustase: arvutus ja kood; süvatase: otsuse piirangud.

## Kontrollküsimus 1

**Kas walk-forward on sama mis puutumata lõppkatse?**

Vastus: Ei. Walk-forward reguleerib sobitamist ajas; puutumatus puudutab ka uurija mudelivalikut.

## Kontrollküsimus 2

**Miks paper trading ei tõenda täielikult täitmiskvaliteeti?**

Vastus: Virtuaalne order ei pruugi mõjutada turgu ega paikneda tegelikus järjekorras.

## Kontrollküsimus 3

**Millal on automaatraport parem kui agent?**

Vastus: Kui töö on ette teada: loe tabel, kontrolli väljad, vorminda. Agent lisab mõtet siis, kui ülesannete valik vajab kohanemist.

## Kontrollküsimus 4

**Mida tuleb teha ajastusvea avastamisel pärast raporteerimist?**

Vastus: Märgi raport kehtetuks, paranda ja korda katset; teavita otsustajaid tulemuse muutunud staatusest.

## Kontrollküsimus 5

**Kas tõendi puudumine tähendab strateegia võimatust?**

Vastus: Ei. See piirab praegust järeldust. Edasine sõltumatu katse võib tuua uut infot.

## Praktiline ülesanne 1: Arvutus: usaldusvahemiku tõlgendus

[PRAKTIKA] Aktiivtootluse aastastatud keskmise vahemik on −6,51 kuni +3,47 protsendipunkti. Kas võib lubada vähemalt nullist suuremat eelist?

**Lahendus:** Ei. Null kuulub vahemikku. `-0.0651 < 0 < 0.0347` on tõene. Lisaks ei ole see tulevase tootluse garanteeritud vahemik ega faktoralpha hinnang.

## Praktiline ülesanne 2: Otsus ja kood: raporti tõend

[PRAKTIKA] Raportis on lause „strateegia võidab turgu”. Kuidas parandad? Käivita raport ning kontrolli allikaid.

**Lahendus:** `python python/raport.py` loob mõõdikutel põhineva kokkuvõtte. Asenda väide: „Sünteetilises lõppkatses jäi reegli CAGR baasile alla; päristuru eelise kohta tõend puudub.” Lisa `run.json` andmeräsi ja periood. Otsus: uus pärisandmetega uurimiskatse, mitte kapitali eraldamine.

## Vanemkvandi kriitiline küsimus

Milline täpselt on järgmine tõend, mille järel võiks otsus muutuda?

Hea vastus nimetab kontrollitava tingimuse ja selle, millised andmed selle kontrollimiseks vajalikud on. Kehv vastus kaitseb mudelit lihtsalt sellepärast, et selle peale kulus palju aega.

## Enesehindamine

Anna iga kontrollvastuse eest 0–2 punkti ning kummagi praktilise ülesande eest 0–5 punkti. 16/20 näitab head alust; edasi minekuks peab ajastuse või tõendi piiri puudutav vastus siiski olema sisuliselt õige. Õpetaja selgitab keerulise vea enne järgmist päeva.
