# Käivitamine Thonnys, Colabis ja käsurealt

## Thonny: eelistatud algus

1. Paki ZIP lahti oma töökausta. Säilita alamkaustad.
2. Vali Thonnys sobiv Python 3.11 või uuem interpretaator. Täpsed selle paketi testiversioonid on `KVALITEET.md` failis; uusimat versiooni ei eeldata.
3. Paigalda Thonny paketihalduris `numpy`, `pandas`, `matplotlib`, `scikit-learn`. Kasuta sama interpretaatorit, millega käivitad näited.
4. Ava `kood/m01.py` ja vajuta F5. Jätka mooduli numbrite järgi.
5. Ava `kood/projekt.py` või `kood/koik_etapid.py` ja vajuta F5. Tulemused ilmuvad `valjund` kausta; graafikud salvestatakse PNG-na.

Kui Thonny kasutab liiga vana sisseehitatud Pythonit, vali uuem lokaalne interpretaator või kasuta Colabi. VS Code pole ühegi põhiharjutuse eeltingimus.

## Käsurida

Käivita kursuse juurkaustas:

```bash
python -m pip install -r requirements.txt
python kood/projekt.py
python kood/koik_etapid.py
python kood/testid.py
```

`requirements.txt` määrab ühilduvusvahemikud, mitte tõestatud ühilduvuse iga tulevase versiooniga. `requirements-tested.txt` salvestab siinse kontrollkeskkonna versioonid. Uuendamisel korda teste.

## Pärisandmed: valikuline

```bash
python -m pip install -r requirements-online.txt
python kood/laadi_yahoo.py
python kood/projekt.py --csv andmed/yahoo_hinnad.csv
```

Yahoo laadija vajab internetti, mitte API-võtit. Praeguse laadija varad on SPY, AAPL ja MSFT; koodis saad neid muuta. Esimene CSV-veerg on võrdlusvara ja ML-i katsevara; võrdselt kaalutud portfell sisaldab kõiki veerge. SPY ja selle koosseisus olevate aktsiate ühine hoidmine tekitab kattuvuse — see pole kolme sõltumatu riski hajutus.

Välise CSV esimene veerg on `Date`, järgnevad positiivsed võrreldavad hinnad. Vaja on ühist valuutat ja kooskõlalist korrigeerimist. Kontroll lükkab puuduvad ja duplikaatandmed tagasi. CSV-st ei saa automaatselt järeldada dividendide, valuuta või pärisandmete õigsust; dokumenteeri need ise.

## Colab

Laadi Colabisse üks failidest `colab/01_portfell.ipynb`, `02_masinoppe.ipynb`, `03_uurimisagent.ipynb`. Märkmikud on iseseisvad: esimene lahter loob ajutisse kataloogi vajalikud väikesed koodifailid ja paigaldab põhipaketid. Järgmised lahtrid on käivitatavad ülevalt alla. Internetti on vaja paketipaigalduseks, demoandmete jaoks mitte. GPU pole vajalik.

Colabi ajutine failisüsteem võib seansi lõppedes kaduda: laadi loodud tulemused enda arvutisse. Pilve tasuta kasutuse limiidid võivad muutuda; põhikursus töötab ka kohalikus Pythonis. Märkmike koodilahtrid on siin järjestikku täidetud kohaliku Pythoniga; Colabi veebiseanssi ennast ei käivitatud.

## Lisapraktikumid ja API-d

| Fail | Keskkond | Paketid | Võti/kulu | Väljund |
|---|---|---|---|---|
| `m01.py`–`m13.py` | Thonny | Põhipaketid | Offline tasuta | Tekst |
| `projekt.py` | Thonny/Colab | Põhipaketid | Offline tasuta | Raport, CSV, SQLite, PNG |
| `lisapraktikumid.py` | Colab/Thonny | Põhipaketid | Offline tasuta | Optsioonide ja portfellikaalude graafikud |
| `ml_lisad.py` | Colab | scikit-learn | Offline tasuta | Klassifitseerimise ja klastrite mõõdikud |
| `ml_lisad.py --xgboost` | Colab | Lisaks xgboost | Offline tasuta | Valikuline XGBoost RMSE; siin käivitamata |
| `uurimisagent.py` | Thonny/Colab | scikit-learn | Offline tasuta | Skriptitud otsingudemo, logi |
| `uurimisagent.py --live` | Thonny | Põhipaketid, standardteegi HTTP | OPENAI_API_KEY; API võib olla tasuline | LLM-i valitud tööriistad, tõenditega raport |
| `sec_fred.py sec CIK` | Thonny/käsurida | Põhipaketid + standardteek | SEC_USER_AGENT; API-võtit pole | Toorandmete JSON |
| `sec_fred.py fred SERIES` | Thonny/käsurida | Sama | FRED_API_KEY | Toorandmete JSON |

API-võtmed määra oma operatsioonisüsteemi keskkonnamuutujates; ära kirjuta neid GitHubi, märkmikusse ega raportisse. Live-agent vajab ka `OPENAI_MODEL` väärtust — vali sinu API-kontole kättesaadav Responses API tekstimudel. Mudelinime ega hinda ei kõvakodeerita. Tavapärase ChatGPT vestluse kasutamine promptidega ei käivita automaatselt selle Pythoni programmi API-haru.

## Veadiagnoos

- `ModuleNotFoundError`: pakett paigaldati teise Pythoni keskkonda. Kontrolli `sys.executable`.
- Tühi Yahoo vastus / 429: oota, väldi korduspäringute tulva, kasuta olemasolevat CSV-d või offline-demot.
- `KeyError: Close`: teenuse veerustruktuur muutus; kontrolli `raw.columns`. Laadija määrab MultiIndexi teadlikult.
- `ValueError` hinnakontrollis: vaata duplikaate, puudumisi ja nullhindu; ära peida neid automaatselt.
- SEC 403: kontrolli User-Agent'i, päringusagedust ja teenuse tingimusi.
- LLM JSON-viga: mudeli väljund ei vasta skeemile. Programm katkestab; ära käivita väljundit Pythoni koodina.
- API 401/429: kontrolli võtme õigusi, limiiti ja konto eelarvet. Ära prindi võtit logisse.
