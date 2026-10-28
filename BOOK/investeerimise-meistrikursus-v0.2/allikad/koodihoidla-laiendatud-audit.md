# Koodihoidla laiendatud kontroll

[Tagasi avalehele](../README.md) · [7. peatüki sisuline audit](koodiaudit.md)

Kontroll 28.10.2026 hõlmas `main` harus olevaid märkmikke `ch02.ipynb` kuni `ch12.ipynb` ning kahte Streamliti skripti. Kokku 13 lähtefaili, sealhulgas 270 märkmiku koodilahtrit ja kaks eraldiseisvat skripti. Kõik allalaadimised õnnestusid. Failide kontrollsummad identifitseerivad kontrollitud sisu; `main` võib hiljem muutuda.

**Kontrolli tasemed:** süntaksiparsimist tehti kõigile nimetatud failidele. Täielikult käivitati ainult võrguühenduseta `ch12.ipynb` kaks lahtrit. Ülejäänud märkmike API-ühenduste, kontode, mudelinimede ja kogu paketikoosluse töökindlust pole kinnitatud.

## Failipõhine tulemus

| Fail | Koodilahtrid / skriptid | Pythoni parser | Staatiliselt leitud importide juurmoodulid |
|---|---:|---|---|
| `ch02.ipynb` | 33 | Läbis | `datetime`, `matplotlib`, `pandas`, `yfinance` |
| `ch03.ipynb` | 43 | Läbis | `alpha_vantage`, `dotenv`, `eodhd`, `matplotlib`, `numpy`, `openbb`, `os`, `pandas`, `requests`, `yfinance` |
| `ch04.ipynb` | 19 | Läbis | `alpha_vantage`, `collections`, `dotenv`, `matplotlib`, `os`, `pandas`, `pytrends`, `requests`, `yfinance` |
| `ch05.ipynb` | 10 | Läbis | `dotenv`, `io`, `matplotlib`, `os`, `pandas`, `requests`, `yfinance` |
| `ch06.ipynb` | 20 | Läbis | `alpaca`, `binance`, `currency_converter`, `dotenv`, `gspread`, `ib_insync`, `oauth2client`, `os`, `pandas`, `requests`, `sqlalchemy`, `yfinance` |
| `ch07.ipynb` | 25 | Läbis | `datetime`, `matplotlib`, `numpy`, `pandas`, `sklearn`, `yfinance` |
| `ch08.ipynb` | 37 | Läbis | `anthropic`, `datetime`, `dotenv`, `google`, `math`, `matplotlib`, `mistralai`, `numpy`, `openai`, `os`, `pandas`, `plotly`, `scipy`, `sklearn`, `transformers`, `yfinance` |
| `ch09.ipynb` | 21 | 1 taaneviga | `IPython`, `datetime`, `dotenv`, `enum`, `google`, `langchain`, `langchain_community`, `langchain_core`, `langchain_openai`, `langchain_text_splitters`, `langgraph`, `openai`, `os`, `pandas`, `requests`, `sqlalchemy`, `typing_extensions` |
| `ch10.ipynb` | 39 | Läbis | `matplotlib`, `mplfinance`, `pandas`, `yfinance` |
| `ch11.ipynb` | 21 | Läbis | `alpaca`, `dotenv`, `ib_insync`, `numpy`, `os`, `pandas`, `yfinance` |
| `ch12.ipynb` | 2 | Läbis | `numpy`, `pandas` |
| `ch10_streamlit.py` | 1 | Läbis | `pandas`, `streamlit`, `yfinance` |
| `ch10_streamlit_ta.py` | 1 | Läbis | `matplotlib`, `mplfinance`, `pandas`, `streamlit`, `yfinance` |

## Konkreetne taaneviga

`ch09.ipynb` seitsmes koodilahter, esimene rida, algab ühe liigse tühikuga enne `get_prompt_by_id("earning_base")`. Selle lahtri andmine muutmata kujul `ast.parse`-ile Python 3.12-s annab `unexpected indent`. Tõenäoline parandus on eemaldada lause eest juhuslik taane. Autori faili ei ole siin muudetud ning Jupyteri sisenditeisendaja käitumist pole eraldi testitud. See on parserile nähtav probleem, mitte väide kogu agendimooduli toimimatuse kohta.

## Tegelikult käivitatud originaalnäide

`ch12.ipynb` mõlemad koodilahtrid töötasid NumPy 2.3.5 ja pandas 2.2.3-ga Python 3.12.14 keskkonnas. Ettevõtte mudelväärtuseks väljastati **1 695 966.71 dollarit**. See on koodis määratud eelduste tulemus, mitte ettevõtte tegelik turuväärtus ega meie soovitus.

Lahjenemisnäite asutaja lõpposalus oli **22.95%**. Seda kontrolliti ka sõltumatult: algne 50% × 75% × 80% × 85% × 90% = 22.95%. Investeeritud rahasummad ei määra selles konkreetses näites lahjenemist, sest ringides loovutatavad osakaalud on juba ette antud.

## Käivitamise eeldused ja piirid

- `ch03`–`ch06` kasutavad mitut välist andme- või kontoteenust. Edukas import ei kinnita autentimist, tellimuse õigusi ega andmete semantikat.
- `ch08`–`ch09` importivad mitut LLM-i ja agentide teeki. Nende teenuste praeguseid mudelinimesid, hinnastust ning kõigi SDK-versioonide koostoimet pole valideeritud.
- `ch06` ja `ch09` kasutavad failide või andmebaasidega seotud töövooge. Töökausta ning õigused tuleb enne jooksu määrata.
- `ch11` lähtekood sisaldab `submit_order` ja `placeOrder` kutseid. Staatiline audit neid ei täitnud. Uurimiskoodi käivitamine ei pea vaikimisi tähendama maaklerikorralduste saatmist.
- Importide loend on staatiline ülevaade, mitte valmis `requirements.txt`: Pythoni importnimi ja paigaldatava paketi nimi ei ole alati samad.

Algkursuse näidetele on turvaline ja lihtne lähtepunkt meie 24 standardteegi skripti. Pappi näidete jaoks tuleks luua eraldi keskkond, määrata täpsed sõltuvused, testida teenuseid ühekaupa ning eristada lugemine, simulatsioon ja välise mõjuga tegevused.

## SHA-256 kontrollsummad

- `ch02.ipynb`: `a9ecdfead3133e7d62ac2dbc72ded244110d28f6e9916d645e245f2da6dc1ee4`
- `ch03.ipynb`: `802a35fb89e4e93ad20933524a9530569e45a223cd026f488a76e7ba732e689e`
- `ch04.ipynb`: `f704dfceaefc3734983d4f3e831d382f054edabc49d0dc59daaeb6df95899343`
- `ch05.ipynb`: `05de43bf60adf5d009cb2093f8c280def442e734d33715f15e7d59f034e7164f`
- `ch06.ipynb`: `136c21034cf4f8f6772a0f00328c83f67c58279a8bafdc72019614e35e986418`
- `ch07.ipynb`: `5d22857abd1a1e5a56fa0a14df9737461038c9e9ceaaf93e224fe6c2fd615853`
- `ch08.ipynb`: `369c4ddc8ce88598374c5f2016eddf47af4f354eeb0ac43f7d24468e7f6011c9`
- `ch09.ipynb`: `58910dfde1603a3f664782929edd1676723098d7cf9a132af476e118555eee32`
- `ch10.ipynb`: `ca6bfaea6cc2a8bc5c50b8fb0c5cad6c584a71a42dcbe5cc75812196e0dbb8e3`
- `ch11.ipynb`: `58a06711f86aaf0c25076a5da0325ad8e53dab6792cb4b317523b511c4ecab52`
- `ch12.ipynb`: `2a2585060bec6143dfa0b11585d9a237bacfec7104b770ad3d74af73ecd805b8`
- `ch10_streamlit.py`: `e03c4da9e7d4b6afc6ccff94bc866f97a8fc9a94f74157e87f9356430b23717a`
- `ch10_streamlit_ta.py`: `26b621f301744c36d15ee3a72bf09a9cf6670d781c1a12e89c58f9b1b98cd939`
