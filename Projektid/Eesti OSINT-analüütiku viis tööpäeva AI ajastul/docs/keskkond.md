# Käivitamine Thonnys ja Colabis

## Thonny — esimene valik

1. Laadi ZIP alla ja paki **kogu kaust** lahti. Ära käivita faili ZIPi seest.
2. Kasuta Python 3.10 või uuemat. Ava Thonnys `src/assistant.py`, vajuta F5.
3. Tulemuseks on `reports/raport.md` ja `reports/research.sqlite`. Põhiversioon ei vaja pip-pakette ega internetti.
4. Moodulite jaoks ava `src/labs.py`. Thonnys saab programmi argumentide rea sisse lülitada menüüst View/Program arguments (menüü nimetus võib versiooniti erineda). Anna mooduli number, näiteks `13`. Alternatiiv: Thonny Shellis `import labs; labs.run(13)` pärast skripti avamist/käivitamist.
5. ML jaoks ava Tools → Manage packages ja paigalda `scikit-learn==1.8.0`. Ava `src/ml_demo.py`, F5. Kui paigaldus ei sobi sinu Pythoniga, kasuta Colabi; põhikursus ei sõltu ML-i paigaldusest.
6. RAG tõendipaketi jaoks ava `src/rag.py`, F5. See loob prompti, kuid ei saada midagi välisele mudelile.

Terminalis projekti juurkaustas:

```bash
python src/assistant.py
python src/labs.py 13
python src/api_demo.py
python src/rag.py
python -m unittest discover -s tests -v
python -m pip install -r requirements-optional.txt
python src/ml_demo.py
```

Windowsis võib käsu `python` asemel vaja olla `py`. `sqlite3` on Pythoni standardteegis, seda ei paigaldata pipiga. Failid on UTF-8. Põhiversioon on testitud käesoleva keskkonna Pythonis; Thonny kasutajaliidest selles töös eraldi ei käivitatud.

## Colab — teine valik

Ava kaasasolev `notebooks/viis_paeva.ipynb` Google Colabis. Esimene lahter palub üles laadida projekti ZIPi. Järgmine lahter pakib selle `/content/osint` alla, leiab projekti juure ja käivitab baasrakenduse. Käivita lahtrid järjekorras. ML-i paigaldus on eraldi lahtris. Laadi loodud raport alla enne sessiooni sulgemist. Märkmik kasutab ainult sünteetilist õppepaketti; päristöö materjale pilve ei kanta vaikimisi.

## Elus API päring

```bash
python src/api_demo.py --live
```

See teeb **ühe GETi** Statistikaameti dokumenteeritud kataloogi-URLile. Vaikimisi näide on võrguta. Vea korral programm lõpetab ega varja ebaõnnestumist näidisandmetega. Hetke kontrolli tulemus on testiraportis. Tegelikku teenusemahtu, autentimist ega registrite lepinguid see näide ei simuleeri.

## Taastamine ja GitHub

Demo alustamiseks uuesti eemalda ainult genereeritud `reports/research.sqlite` ja käivita põhiskript. Algandmeid ära kustuta. Õpetaja kohandatud sünteetilise sisendi korral märgi see uue juhtumiversioonina. Tootmises ei kustutata uurimise tõendeid sellisel viisil.

GitHubi jaoks loo uus repositoorium ja laadi projekti failid üles GitHub Desktopiga või Gitiga. `.gitignore` välistab jooksva SQLite andmebaasi ja API toorvastused; sünteetilised õppetekstid ja raportid võib lisada. Originaalraamatut, võtmeid ega päris isikuandmeid repositooriumisse ei lisata. Veebilehe failiüleslaadimise piirangute korral on GitHub Desktop sobiv ka terve kausta jaoks.
