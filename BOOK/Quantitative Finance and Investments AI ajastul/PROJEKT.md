# USA aktsiaturu kvantitatiivne analüüs: klassikalisest statistikast AI-agentideni

See projekt õpetab uurimisprotsessi. Kaasasolevad **SIM_A, SIM_B ja SIM_C on fiktiivsed**, mitte USA aktsiate ajaloolised vaatlused. Valikuline allalaadimine asendab need USA aktsiate ajalooliste hindadega. Maakleriühendust ega tehingute saatmist ei ole.

## Kiirkäivitus Thonnys

1. Paki ZIP lahti. Ava `kood/projekt.py` Thonnys.
2. Thonny **Tools → Manage packages** kaudu paigalda `numpy`, `pandas`, `scikit-learn`, `matplotlib`. Valikuline `xgboost` lisab kolmanda mudeli. Vajadusel vali Thonny tõlgiks Python 3.11 või 3.12.
3. Vajuta Run. Kood leiab andmed ja väljundkaustad oma faili asukoha järgi.
4. Ava `tulemused/vordlus.csv`, `test_mse.csv` ja `joonised/kapital.png`.
5. Käivita `kood/test_kontrollid.py`. Tutvu [kontrolliaruandega](KONTROLL.md).

Terminalis projekti juurkaustast:

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-optional.txt
python kood/projekt.py
python kood/test_kontrollid.py
```

Põhinõuded on lubatud versioonivahemikud. `requirements-tested.txt` näitab kontrolli ajal kasutatud täpseid versioone; see ei ole universaalne platvormideülene lukufail.

## Üheksa sammu

| Samm | Fail | Sisend → väljund | Võrdlus või kontroll |
|---|---|---|---|
| 1. Andmed | `kood/01_andmed.py` | Simulaator või Yahoo → CSV ja provenance | Unikaalsed, kasvavad kuupäevad; positiivsed hinnad |
| 2. Statistika | `kood/02_statistika.py` | Hinnad → tootlused, CAGR, risk, korrelatsioon | Geomeetriline vs aritmeetiline tootlus |
| 3. Reegel | `kood/03_strateegia.py` | Hind vs MA50 → pikk positsioon või raha | Kogu valimi illustratsioon; mitte ametlik holdout |
| 4. ML | `kood/04_mudel.py` | 4 hinnatunnust → ridge, histogramm-GBM, XGBoost | Nullprognoosi MSE; valik ainult valideerimisest |
| 5. Aus test | `kood/05_testimine.py` | Külmutatud reeglid → netotulemused | 70/30 ajajaotus, gap, kulu 0–50 bp |
| 6. Portfell | `kood/06_portfell.py` | Treeningu risk → kolm kaalureeglit | Võrdkaal, pöördvolatiilsus, min-variance 60% laega |
| 7. Aruanded | `kood/07_rag_agent.py` | Ajafiltriga lõigud → tõendid või LLM-vastus | Käsitsi vastusevõti, puuduva info tunnistamine |
| 8. Agent | `kood/08_agent.py --agent` | LLM valib search/finish → auditijälg | Maksimaalselt 3 päringut; tööriistade lubatud loend |
| 9. Võrdlus | `kood/09_vordlus.py` | Salvestatud tabelid → kõrvutus | Tootlus, risk, MSE ning eraldi tekstikvaliteet/aeg/kulu |

`projekt.py` viib läbi arvulise põhivoo. `11_aegrida.py` lisab 20 tootluse aknaga väikese mitmekihilise närvivõrgu; see pole transformer ega selle kasulikkuse tõestus. `10_instrumendid.py` sisaldab optsiooni, futuuri, ETF-i ja võlakirja arvutusi.

## Ajaloolised USA andmed

```bash
python kood/01_andmed.py --download
python kood/projekt.py
```

See samm vajab internetti ja yfinance'i. Andmeallikas võib päringut piirata; tõrget ei maskeerita sünteetilisteks andmeteks. Päring kasutab AAPL/MSFT/JPM perioodi 01.01.2018 kuni 01.01.2026 (lõppkuupäev välja arvatud), kohandatud hindu. Olemasolev `andmed/hinnad.csv` kirjutatakse üle; kui soovid säilitada mõlemad katsed, kasuta eraldi projektikoopiaid.

Need kolm tänast ettevõtet on mugav näide, **mitte ajalooline ellujäämiskallutusteta USA turu universum**. Esimese hinnaveeru ost-ja-hoia on ühe aktsia baas. Kolme vara võrdkaal on eraldi portfellibaas. Üldise turuülese alfa hindamiseks lisa PIT-universum, delistimised, võrdlusindeksi kogutootlus ja faktorikontroll. Paketis pole sellise turuülese alfa tõendit.

## Täpne ajastus ja katseplaan

- Otsus kasutab sulgemise `t` andmeid.
- Täitmine eeldatakse sulgemisel `t+1`. See on fikseeritud õppeviide, mitte realistliku orderiraamatu simulatsioon.
- Esimene teenitav hinnatootlus on `t+1 → t+2`.
- Tunnusrea `t` siht on `r.shift(-2)[t]`; portfellirea `t+2` positsioon on `signal.shift(2)[t+2]`.
- Treeningu ja testi vahele jäetakse kaks tunnuserida. Nii ei ulatu viimase treeningsildi lõpp esimese testotsuse aega.
- Esimesed 70% valmis tunnuseridadest on arendusosa; selles kolm kasvava treeninguga ajavolti. Mudeliperekonna valik toimub valideerimise keskmise MSE järgi.
- Viimased 30% on külmutatud lõppkatse. Seal mudelit ümber ei treenita. Kõiki mudelitulemusi näidatakse läbipaistvuse pärast, kuid valitud mudeli lipp tuleb valideerimisest.
- Positsioonireegel on ette antud: prognoos > 0 → 100% esimese vara pikk positsioon, muidu raha. Lävendit ei häälestata lõppkatsega.
- Raha tootlus ja Sharpe'i riskivaba määr on näites 0. Kõik strateegiad alustavad ühisest testiaknast rahas ning sisenemise ja lõpliku väljumise eest on kulu.
- Tehingukulu on lihtne osa kaubeldud nominaalist. Kulu ja päevatootluse ristliige on sisenemisel lihtsustuseks eiratud. Tegu pole senditäpse raamatupidamismootoriga.
- Portfellikatse kasutab ainult enne testiakent hinnatud kovariatsiooni; taastab sihtkaalud iga päev, arvestab hinnaliikumise tekitatud kaalunihet ning käibekulu.

Kogu valimi kirjeldav statistika ei tohi juhtida juba lukustatud protokolli muutmist. Pärast holdout'i nägemist tehtud muudatus vajab uut kinnitavat perioodi; sama andmestiku uuesti käivitamine ei tekita uut tõendit.

## Uurimisprotokolli mall

```text
ID ja kuupäev:
Majanduslik hüpotees ja vastupidine seletus:
Universum ja valiku ajaline alus:
Andmeallikas, räsi, saadavusajad:
Tunnused ja sihtmuutuja:
Otsus / täitmine / tootlusperiood:
Baasmeetod:
Treening / valideerimine / gap / lõppkatse:
Kõik lubatud kandidaadid ja otsingueelarve:
Kulud ja teostatavuse piirangud:
Põhimeetrika ja loobumiskriteerium:
Kõigi katsete register:
Järeldus ja selle piir:
```

## LLM-i ja agendi kasutamine

Offline-käsk `python kood/07_rag_agent.py` näitab TF-IDF otsingut fiktiivse aruande peal. See ei tee tasulisi päringuid ja pole generatiivne RAG. Koodis olev vastusevõti on õpetaja käsitsi koostatud.

Päris LLM-i jaoks määra keskkonnas `OPENAI_API_KEY` ja oma kontol kättesaadav `OPENAI_MODEL`. Ära pane võtit faili, GitHubi ega märkmiku väljundisse. Kasuta `--live-llm` ühe vastuse jaoks või `--agent` piiratud tööriistavaliku tsükliks. Need saadavad leitud dokumendilõigud välisele API-le ja võivad olla tasulised. Paketis neid ühendusi ei käivitatud. API näide järgib [S13](ALLIKAD.md), kuid vajab sinu kontol ühendustesti.

JSON-väljundi kontroll kinnitab struktuuri ja allika ID olemasolu, **mitte väite sisulist õigsust**. Keelatud tööriist, vale viide või vigane JSON katkestab töö. Agendi sammulimiit ei ole täpne euroeelarve: tokenilimiit ja konto kulupiir peavad samuti sobima. Ajaloolises hindamises arvesta LLM-i võimaliku eeltreeningu teadmisega.

Pärisaruande kohalikuks kasutuseks:

```bash
python kood/12_dokumendid.py aruanne.pdf --available-at 2024-02-03 --output andmed/aruanded.json
python kood/07_rag_agent.py --docs andmed/aruanded.json --cutoff 2024-03-01
```

Asenda kuupäevad ja fail tegelikega. Teksti tükeldamine on lihtne lehekülje- ja märgipõhine baas; tabelid, OCR, päevasisene ajastus ja dokumentide versioonid vajavad lisatööd. Ingliskeelse dokumendi otsing töötab selle demonstratsiooni ingliskeelsete otsingusõnadega; mitmekeelse otsingu jaoks lisa eraldi hinnatud tõlge või manustused.

## Kõigi lahenduste aus võrdlus

| Lahendus | Baas | Mõõdik | Mida ei tohi väita |
|---|---|---|---|
| Hinnaprognoos | Nulltootlus | MSE ajaliselt eraldatud testis | Väiksem MSE tagab kasumi |
| Ühe vara reegel/ML | Sama vara buy-and-hold ja raha | Neto-CAGR, vol, MDD, käive | SIM_A tulemus on USA turu prognoos |
| Mitme vara portfell | Sama universumi võrdkaal | Neto, risk, kontsentratsioon | Pöördvolatiilsus on alati optimaalne |
| LLM analüüs | Käsitsi vastusevõti + lokaalne otsing | Faktitäpsus, katvus, viited | Veenev tekst tähendab paremat alfat |
| Agent | Fikseeritud RAG-töövoog | Sama kvaliteet, aeg, kogukulu, tõrked | Agent on vajalik ainult sellepärast, et see on võimalik |

LLM-i/agentide väljund **ei juhi selles projektis portfelli**. Need on uurimistöö abivahendid. Kui soovid hiljem tekstisignaali mudelisse lisada, külmuta ekstraktsiooniprompt, säilita versioonid ja tee eraldi ajaliselt korrektne ablation. Seda kasu ei ole siin ette oletatud.
