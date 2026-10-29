# Kontrolliaruanne

Kontrollitud 29.10.2026. Tegemist on õppematerjali ja koodinäidete kontrolliga, mitte investeerimisstrateegia sertifitseerimisega.

## Käivitatud ja kontrollitud

- Sünteetilise andmestiku loomine: 1600 tööpäeva, kolm fiktiivset vara, fikseeritud juhuseeme 42.
- Ridge, histogramm-GBM ja XGBoost: ajapõhine valideerimine ning eraldi lõppkatse.
- Trendibaas, ost-ja-hoia ja raha: ühine testiperiood ning kulud 0, 5, 10, 25 ja 50 bp.
- Võrdkaalu, pöördvolatiilsuse ja 60% kaalupiiriga minimaalse dispersiooni portfellid.
- Väike MLP aegreaaknal; nullprognoosi ja ridge'i võrdlus.
- Kohalik TF-IDF otsing ja tulevikudokumentide ajafilter.
- Agenditsükkel etteantud testvastustega, lubatud tööriista kontroll ja sammulimiit.
- PDF-i lõikudeks muutmine ühe iseseisvalt loodud testdokumendiga.
- Black–Scholesi call'i hind, optsiooni tasuvus, futuuri P&L, ETF preemia ja nullkupongvõlakirja YTM.
- Kaks genereeritud andmejoonist visuaalselt üle vaadatud.

## 10 automaattesti

Kõik läbisid: sihtmuutuja ajastus; tulevikuhindade muutmise mõju puudumine mineviku tunnustele; sisse-välja kulu; lõpliku likvideerimise kulu; algse kapitaliga arvestav maksimumlangus; RAG-i kuupäevapiir; keelatud tööriista tõkestus; võltsviite tõkestus; testvastustega agenditsükkel; sammulimiit.

Käivitus: `python kood/test_kontrollid.py`. Testid kontrollivad konkreetseid vigu, mitte kogu süsteemi korrektseks kuulutamist.

## Märkmikud

Kõigi kolme `.ipynb` faili struktuuri kontrollitakse `nbformat`-iga ning koodilahtrid käivitatakse järjest eraldi töökataloogis otse Pythonis. Täpne tulemus on `tulemused/notebook_checks.json`.

Jupyteri kernelit ei saanud selles keskkonnas käivitada TCP- ega IPC-ühenduste piirangu tõttu. Seetõttu **Colabi kasutajaliidest ja Jupyteri kernelikäivitust ei ole kontrollitud**. Otsene lahtrite täitmine kontrollib Pythoni loogikat, kuid pole sama mis Colabi täielik kasutuskatse. Märkmikesse ei ole lisatud näilisi kernelikäivituse numbreid.

## Näidistulemused: ainult sünteetilised andmed

Valideerimise järgi valiti XGBoost. Lõppkatses oli nulltootluse prognoosi MSE umbes 0,00039967 ja XGBoosti MSE 0,00040232: keerukam mudel ei võitnud nullbaasi.

| Strateegia | Neto-CAGR, 10 bp | Maksimaalne langus |
|---|---:|---:|
| Ost-ja-hoia, SIM_A | −19,58% | −45,40% |
| Trend MA50 | −12,11% | −26,54% |
| Ridge | −17,69% | −41,85% |
| Histogramm-GBM | −6,60% | −34,06% |
| XGBoost, valideerimisest valitud | −14,48% | −40,41% |
| Raha, eeldatud tootlus 0 | 0,00% | 0,00% |

Täpsed arvud on `tulemused/vordlus.csv`. Testi järel ei valitud histogramm-GBM-i uueks „võitjaks”. Negatiivseid tulemusi ei peidetud ega häälestatud ilusamaks. Need ei kirjelda USA turu tegelikku tootlust: SIM_A on juhuslikult loodud õppeandmestik.

## Kontrollimata või teadlikult lihtsustatud

- Yahoo/yfinance ajalooliste hindade võrguühendust ei käivitatud; selle liidese kasutus ja andmekvaliteet vajavad kohalikku kontrolli.
- Tasulist LLM API-t ei kutsutud. Näide vajab sobiva mudeli, võtme ja konto ühendustesti. API tasud ja kontol kättesaadavad mudelid pole ette määratud.
- Agendi testvastused ei tõesta päris LLM-i otsuste kvaliteeti. Viidete ID-kontroll ei kontrolli väite sisulist tõesust.
- Pole PIT USA aktsiauniversumit, delistimisi ega turuülese alfa kinnitust. Ajaloolise andmevaliku tänased kolm ettevõtet on ainult tehniline näide.
- Kulumudel on lihtne nominaalipõhine lähend; puuduvad täpne orderiraamat, turumõju, maksud, laenutasud ja tegelik raha intress.
- LSTM/transformer, RL ja teadmistegraaf on kontseptuaalselt käsitletud; täielikku tootmisrakendust pole.
- Raamatu 27 peatüki struktuur ja valitud käsitlused analüüsiti; kõiki raamatu märkmikke ega empiirilisi tulemusi ei reprodutseeritud.
- Pärisraha tehinguid ei tehtud. Maakleriühendust koodis ei ole.

## Korratavus

`run_manifest.json` sisaldab andmefaili SHA-256 räsi ja põhiteekide versioone. `requirements-tested.txt` dokumenteerib kasutatud teegiversioonid. Erinev teegiversioon või riistvara võib muuta ümardust ja mõne mudeli tulemust. Juhuseeme üksi ei taga täielikku platvormideülest determinismi.
