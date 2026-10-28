# Investeerimise meistrikursus: väide → mudel → katse → põhjendatud järeldus

**Versioon 0.2 · 28.10.2026 · Laiendatud õppepakett; kogu meistrikursus pole veel valmis.**

See eestikeelne õppematerjal seob investeerimisväidete kriitilise analüüsi matemaatika ja käivitatava Pythoniga. Sihtlugeja tunneb matemaatikat ning Pythoni põhialuseid, kuid ei pea olema finantsspetsialist. Näited sobivad Thonnysse ja Colabi.

## Uued terviklikud osad versioonis 0.2

- [Tootluse ja investeerimise alused](01-investeerimise-alused/README.md)
- [Nelja põhiinstrumendi alusatlas](02-finantsinstrumendid/README.md)
- [Finantsmatemaatika alusmoodul](07-finantsmatemaatika/README.md)
- [10 matemaatilist paradoksi](07-finantsmatemaatika/10-paradoksi.md)
- [100 investeerimispõhimõtet, kümme teemarühma](15-100-pohimotet/README.md)
- [50 lahendatud arvutusülesannet](17-50-ulesannet/README.md)
- [24 väikest Pythoni näidet koos selgituste ja väljunditega](10-python-ja-andmed/24-naidet.md)
- [Koodihoidla laiendatud audit](allikad/koodihoidla-laiendatud-audit.md)
- [Schwageri epiloogi kriitiline kasutamine](allikad/schwageri-jarelduste-kriitika.md)

## Varasema laboriploki sisukord

1. [Õppekava ja raamatute süntees](00-oppekava.md)
2. [Labor 1: kas eilne parim fond on ka homme parem?](laborid/01-fondivoitjad.md)
3. [Labor 2: hajutamise mõju korrelatsioonistressis](laborid/02-hajutamine.md)
4. [Labor 3: sama VaR, väga erinev kahjurisk](laborid/03-varjatud-risk.md)
5. [Harjutuste lahendused](laborid/lahendused.md)
6. [Õpetaja tunnikavad ja hindamine](opetaja.md)
7. [Investeerimisväite kontrollimise spikker](otsustusspikker.md)
8. [Pappi koodinäite audit](allikad/koodiaudit.md)
9. [Allikad ja viidete ulatus](allikad/README.md)
10. [Valmidus ja jätkamise järjekord](STAATUS.md)
11. [Kvaliteedikontroll](KONTROLL.md)

## Kuidas alustada?

Paki arhiiv lahti. Ava Thonnys `python/01_fondivoitjad.py` ja käivita. NumPy puudumisel paigalda see Thonny paketihaldurist. Käsurealt, projekti juurkataloogis:

```bash
python -m pip install -r requirements.txt
python python/01_fondivoitjad.py
python python/02_hajutamine.py
python python/03_varjatud_risk.py
python python/kontrollid.py
```

Kaustas `python/lyhinaited/` olevad 24 skripti vajavad ainult Pythoni standardteeki. Ava näiteks `01_liitintress.py` ja käivita. Kõik 50 ülesande arvutused saab korrata failiga `python/50_ulesande_arvutused.py`. Koondmärkmik `colab/24-lyhinaidet.ipynb` sisaldab kõiki lühinäiteid.

Laborite jaoks pole vaja API-võtmeid, maaklerikontot ega turuandmete allalaadimist. `colab/` sisaldab kolme laborimärkmikku ja 24 näite koondmärkmikku: laadi valitud `.ipynb` Colabi ning käivita lahtrid. Märkmikud ei paigalda pakette automaatselt; vajalik on NumPy. Skriptid väljastavad tulemused ekraanile. Kaasasolevad `tulemused/*.json` on selle versiooni tegelike käivituste salvestused; uus käivitus neid automaatselt ei muuda.

## Tõendusmaterjali märgised

- **[SCHWAGER]** ja **[PAPP]**: konkreetse autori käsitlus koos peatükiviitega.
- **[TÄIENDUS]**: muu allikas või metoodiline täiendus.
- **[ANALÜÜS]**: selle kursuse iseseisev arutlus.
- **[NÄIDE]**: originaalne õpetlik näide, mitte tegeliku fondi tulemus.
- **[MUDEL]**: täpselt määratletud eeldustega matemaatiline mudel või simulatsioon.

**Simulatsioon näitab, mis juhtub eelduste kehtimisel. See ei tõesta iseenesest, et need eeldused kirjeldavad päris turgu.** Iga labor sisaldab eraldi pärisandmetega uurimise plaani. Selles versioonis pole tehtud empiirilist uuringut USA fondide ega kriiside kohta.

Materjal on originaalne süntees. Raamatute PDF-e ega Pappi koodi koopiaid arhiivi ei kuulu. Kõik kolm laboriskripti, 24 lühinäidet ja ülesannete arvutusfail on selle materjali jaoks eraldi kirjutatud.
