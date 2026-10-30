# Päev 2: kontrollküsimused ja ülesanded

Proovi enne vastuse lugemist iseseisvalt. Baastase: mõisted; rakendustase: arvutus ja kood; süvatase: otsuse piirangud.

## Kontrollküsimus 1

**Miks +20% ja −20% ei tühista teineteist?**

Vastus: Tootlusprotsendid rakenduvad eri kapitalibaasidele: 1.2 × 0.8 = 0.96.

## Kontrollküsimus 2

**Kas korrektne Python-süntaks välistab lekke?**

Vastus: Ei. Tuleviku kasutamine võib olla täiesti korrektne programm, kuid vigane katse.

## Kontrollküsimus 3

**Miks võrdlusportfellile kulud lisada?**

Vastus: Ka võrdkaal vajab ümberjaotamist. Ebaühtlane kulurežiim moonutab võrdlust.

## Kontrollküsimus 4

**Kas 95% bootstrap-vahemik garanteerib tulevase tootluse?**

Vastus: Ei. See kirjeldab hinnangu varieerumist valimi ja resampling-eelduste tingimustel, mitte tuleviku tururežiimi.

## Kontrollküsimus 5

**Miks algkapital kuulub languse arvutusse?**

Vastus: Muidu jääb esimene kahjumlik periood varasemast tipust võrdlemata ja MDD võib olla liiga väike.

## Praktiline ülesanne 1: Arvutus: rikkus ja kulud

[PRAKTIKA] Alusta 1000 eurost. Tootlused +10%, −5%, +2%. Seejärel arvuta ühe täieliku portfellivahetuse ligikaudne kulu 10 bp mõlemalt poolelt.

**Lahendus:** `1000*1.10*.95*1.02 = 1065.90`. Tootlus 6,59%. Ligikaudne täieliku vahetuse kulu on 2 × 0,1% = 0,2% NAV-ist, s.o 2 eurot 1000-euroselt kapitalilt. Täpne fikspunktarvestus annab pisut teise summa.

## Praktiline ülesanne 2: Otsus ja kood: tuleviku muutmine

[PRAKTIKA] Muuda pärast 31.05.2021 hindu 40% kõrgemaks. Kas 31.05 prognoos võib muutuda?

**Lahendus:** Ei tohi. `python/testid.py` teeb selle katse ja võrdleb varasemaid tunnuseid ning sama päeva prognoose. Tulevase realiseerunud tootluse muutus on normaalne; varasema prognoosi muutus paljastaks lekke. Peata mudeli hindamine, kui test ei läbi.

## Vanemkvandi kriitiline küsimus

Mitu varianti sa enne selle tulemuse valimist proovisid?

Hea vastus nimetab kontrollitava tingimuse ja selle, millised andmed selle kontrollimiseks vajalikud on. Kehv vastus kaitseb mudelit lihtsalt sellepärast, et selle peale kulus palju aega.

## Enesehindamine

Anna iga kontrollvastuse eest 0–2 punkti ning kummagi praktilise ülesande eest 0–5 punkti. 16/20 näitab head alust; edasi minekuks peab ajastuse või tõendi piiri puudutav vastus siiski olema sisuliselt õige. Õpetaja selgitab keerulise vea enne järgmist päeva.
