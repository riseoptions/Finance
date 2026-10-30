# Eesti OSINT-analüütiku viis tööpäeva AI ajastul

**Estonian OSINT Research Assistant** — praktiline eestikeelne GitHubi õppeprojekt.

20 moodulit · 5 järjestikust tööpäeva · 40 allikakanalit, neist 15 esmast · 100 sisulist küsimust vastustega.

Läbiv juhtum on täielikult fiktiivne: Näidisvald-OSINT Rannavärava õppekeskuse eelarve, leping ja avalikud väited. Projekt õpetab kontrollitavat analüüsi; ei profileeri eraisikuid ega kogu piiratud teavet.

## Kiirstart

1. Paki ZIP tervikuna lahti.
2. Ava **Thonnys `src/assistant.py` ja vajuta F5**. Python 3.10+; põhiversioon ei vaja lisapakette ega võrku.
3. Loe `reports/raport.md`; ava selles viidatud tõendid.
4. Alusta [raamatukaardist](docs/raamatukaart.md), [allikakataloogist](docs/allikad.md) ja moodulist 01.

```bash
python src/assistant.py
python src/labs.py 13
python -m unittest discover -s tests -v
```

[Thonny ja Colabi juhend](docs/keskkond.md) · [Colabi märkmik](notebooks/viis_paeva.ipynb) · [testiraport](reports/testiraport.md).

## Õpik ja õpetamine

[Juhtum](docs/juhtum.md) · [Arhitektuur](docs/arhitektuur.md) · [Mõisted](docs/sonastik.md) · [Kogumise reeglid](docs/andmekaitse.md) · [Õpetaja käsiraamat](docs/opetaja.md) · [100 küsimust](docs/100_kusimust.md).

| Päev | Moodul | Teema |
|---|---|---|
| 1 | [01](docs/moodulid/01.md) | Uurimisküsimus ja konkureerivad seletused |
| 1 | [02](docs/moodulid/02.md) | Töökeskkond ja korratavus |
| 1 | [03](docs/moodulid/03.md) | Allikaplaan ja ligipääs |
| 1 | [04](docs/moodulid/04.md) | Tõendite säilitamine ja uurimislogi |
| 2 | [05](docs/moodulid/05.md) | API päring ja vastuse kontroll |
| 2 | [06](docs/moodulid/06.md) | Üksuste ja tunnuste normaliseerimine |
| 2 | [07](docs/moodulid/07.md) | SQLite andmemudel ja idempotentsus |
| 2 | [08](docs/moodulid/08.md) | SQL kontrollid ja summade võrdlus |
| 3 | [09](docs/moodulid/09.md) | Meedia päritoluahel ja parandused |
| 3 | [10](docs/moodulid/10.md) | Sotsiaalmeedia ja foorumite valim |
| 3 | [11](docs/moodulid/11.md) | NLP ja väidete eraldamine |
| 3 | [12](docs/moodulid/12.md) | Ajajoon ja visuaalse väite kontroll |
| 4 | [13](docs/moodulid/13.md) | Kirjeldav statistika ja kõrvalekalded |
| 4 | [14](docs/moodulid/14.md) | Seos, põhjuslikkus ja baasmäär |
| 4 | [15](docs/moodulid/15.md) | Graafid ja seoste tõendus |
| 4 | [16](docs/moodulid/16.md) | Masinõpe tekstitriaažiks |
| 5 | [17](docs/moodulid/17.md) | LLM kui kontrollitav abiline |
| 5 | [18](docs/moodulid/18.md) | RAG ja otsingu hindamine |
| 5 | [19](docs/moodulid/19.md) | Professionaalne aruanne ja ülevaatus |
| 5 | [20](docs/moodulid/20.md) | Õpetamine, kaitsmine ja edasiarendus |

## Valikuline AI

ML: `python -m pip install -r requirements-optional.txt`, seejärel `python src/ml_demo.py`. RAG tõendiotsing ja LLM-prompt: `python src/rag.py`. Päris LLM-i ei käivitata ega vajata API võtit; genereerimise katse juhis on arhitektuurifailis. Agent jäetakse teadlikult välja, kuni selle kasu on mõõdetud.

## Failide ülesanded

- `docs/`: GitHubi õpik, moodulid ja õpetaja materjalid.
- `src/`: baasrakendus, API näide, 20 laborit, ML ja RAG.
- `sql/`: andmemudel ja kontrollpäringud.
- `data/`: 12 algtõendit, manifest, lepingud, seosed, NLP-korpus ja otsinguetalon.
- `reports/`: professionaalne raport, päevamemod, mõõdikud ja testilogi.
- `tests/`: vigadele ja invariantsustele suunatud automaattestid.
- `notebooks/`: Colabi käivitusmärkmik.

Raamatu 47 peatükki on kaardistatud, kuid see projekt ei taasesita raamatut ega rakenda kõiki selle tehnikaid. Eesti allikad ja AI-osa on eraldi märgitud täiendused. Allikate kontroll ja teenusepiirangud on kataloogis. Paketis ei ole algset PDF-raamatut. [Litsents](LICENSE.md).
