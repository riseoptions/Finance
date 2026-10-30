# Allikad ja teemakaart

Kontrollimise kuupäev: **30.10.2026**. Põhiallikad on kasutaja lisatud PDF-id. Analüüs hõlmas mõlema raamatu struktuuri ning projekti seisukohalt oluliste uurimise, ajastuse, mudelite, portfelli, kulude, RAG-i ja kasutuselevõtu osade sihtlugemist. Kõiki raamatute harjutusi ega kaasnevaid lähtekoodihoidlaid ei ole läbi jooksutatud. Kursus ei väida kõigi peatükkide täielikku käsitlemist.

PDF-lehekülg tähendab failis loendatavat lehekülge, trükilehekülg lehel olevat numbrit. Sisukorra viide määrab peatüki asukoha; kursuse detailne kood ja arvulised näited on originaalsed.

## Narang: miks süsteem nii üles ehitada?

**Rishi K. Narang, Inside the Black Box: A Simple Guide to Systematic Investing, Third Edition. Wiley, 2024.** ISBN 9781119931898. Lisatud failis 365 PDF-lehekülge. Põhitekstis on trükileheküljele üldjuhul lisatud 20 PDF-lehekülge.

| Peatükk | Trükilehe algus | Kursuse kasutus |
|---|---:|---|
| 1. Why Does Quant Trading Matter? | 3 | Süstemaatilise lähenemise eesmärk |
| 2. An Introduction to Quantitative Trading | 13 | Rollid ja süsteemi komponendid; skeem lk 17–19, PDF 37–39 |
| 3. Alpha Models | 23 | Hüpotees, momentum, teooria- ja andmepõhised ideed |
| 4. Risk Models | 71 | Riskipiirangud ja soovimatud ekspositsioonid |
| 5. Transaction Cost Models | 85 | Kulu liigid; lk 86, PDF 106 |
| 6. Portfolio Construction Models | 99 | Reeglipõhine ja optimeeritud kaalumine; lk 100, PDF 120 |
| 7. Execution | 127 | Orderi teostus; lk 129, PDF 149 |
| 8. Data | 143 | Andmekvaliteet ja säilitamine |
| 9. Research | 161 | Teaduslik meetod, testid ja valik; PDF 181 jj |
| 10. Risks Inherent to Quant Strategies | 191 | Mudeli-, režiimi- ja ühise investori risk |
| 11. Criticisms of Quant Trading | 213 | Kriitilise arutelu taust |
| 12. Evaluating Quants and Quant Strategies | 233 | Komitee küsimused ja tõendite kvaliteet |
| 13–15. High-Speed / High-Frequency Trading | 255–295 | Piiritlev kõrvalteema: meie projekt ei ole HFT |
| 16. Looking to the Future of Quant Trading | 297 | Inimese, ML-i ja andmete rolli muutumine |

Narang ei määra selle projekti kuut ETF-i, 63 päeva akent, 10 bp kulu ega Random Foresti parameetreid. Need on [NÄIDE]. Loo tegelased ja firma on [SIMULATSIOON].

## Jansen: kuidas uurimistsükkel rakendada?

**Stefan Jansen, Machine Learning for Trading, Third Edition. Packt, 2026.** Lisatud faili tiitliandmetes esimene avaldamine 2018, teine väljaanne 2020 ja kolmas juulis 2026; ISBN 9781803246970. Failis 827 PDF-lehekülge. Kontrollitud põhiteksti viidetes PDF-leht = trükileht + 41.

| Peatükk | Trükilehe algus / kontrollpunkt | Kursuse kasutus |
|---|---|---|
| 1–4 | Sisukord PDF 10–12 | Uurimistsükkel, andmed, mikrostruktuur, fundamentaalandmed |
| 5. Synthetic Financial Data | 97 | Sünteetiliste andmete piirid; meie lihtne generaator ei taasta raamatu generatiivmudeleid |
| 6. Strategy Research Framework | 123; lk 125–126 / PDF 166–167 | Baaslahendus, ajaprotokoll, katsepäevik ja juhtumiuuringud |
| 7. Defining the Learning Task | 147; lk 148 / PDF 189 | Sildid, ajastus ja split-aware eeltöötlus |
| 8. Financial Feature Engineering | 175 | Momentum ja volatiilsus |
| 9–10 | 201 ja 227 | Mudelipõhised ja tekstitunnused; kõrvalteemad |
| 11. The ML Pipeline | 251; lk 254 / PDF 295 | Regulaaritud lineaarne baas |
| 12. Advanced Models for Tabular Data | lk 288 / PDF 329 | Metsad ja boosting |
| 13–15 | Sisukord PDF 19–21 | Süvaõpe, latentfaktorid, põhjuslik ML; põhjendatud väljajätt põhikoodist |
| 16. Strategy Simulation | 411; lk 416 / PDF 457 | Täitmise, piirangute ja kulude kooskõla |
| 17. Portfolio Construction | 447 | Prognoosist kaaludeni |
| 18. Transaction Costs | 483 | Kulutundlikkus |
| 19. Risk Management | 513 | Stress ja riskipiirangud |
| 20. Strategy Synthesis | 541 | Tulemuste tervikhinnang |
| 21. Reinforcement Learning | lk 604 / PDF 645 | Simulatsiooni ja pärismaailma vahe; põhikoodist väljas |
| 22. RAG for Financial Research | 609 / PDF 650 | Ajafiltriga tõendid ja kontrollitud arvutused |
| 23. Knowledge Graphs | 635 | Ajastatud seosed; graafbaasi pole lihtsa ülesande jaoks vaja |
| 24. Autonomous Agents | 659; lk 660 ja 692 / PDF 701 ja 733 | Õigused, jälgitavus ja testimine |
| 25. Live Trading Systems | 695 / PDF 736 | Uurimise ja tootmise tehniline kooskõla |
| 26 | lk 725 / PDF 766 | Tehnilise vea ja statistilise halvenemise eristamine |

## Janseni üheksa juhtumiuuringut

Ptk 6 (lk 125–126) ja ametlik juhtumiuuringute leht annavad laiema võrdluse. Meie kuue sektorilaadse sünteetilise vara katse on omaette õpetuslik kohandus, mitte ühe juhtumiuuringu reproduktsioon.

| Juhtum | Õpitav probleem | Seos kursusega |
|---|---|---|
| ETF-id | Eri varaklasside võrdlemine ühise töövooga | Kõige lähem raam; meie universum on kitsam |
| USA aktsiapaneel | Suur ristlõige ja ajalooline universum | Survivorship bias ja sõltuvused |
| USA ettevõtete tunnused | Fundamentaalinfo avaldamisviivitus | Punkt-ajas andmeleping |
| FX-paarid | Ajavöönd ja sulgemishinna määratlus | Signaali ja tehingu ajad |
| CME futuurid | Rollimine ja tähtajastruktuur | Instrumentide lisa |
| Krüpto perpetual'id | Funding ja 24/7 turud | Kulude ja kalendri erinevus |
| NASDAQ-100 mikrostruktuur | Tihedad noteeringud ja täitmine | Selgitab, miks me HFT-d ei simuleeri |
| Aktsiad + optsiooniandmed | Optsioonitunnused aktsiaprognoosiks | Prognoositunnus pole ise kaubeldav portfell |
| S&P 500 optsioonid | Straddle ja delta-risk | Hinnastamise kvandi kõrvalnäide |

## Täiendavad kontrollitud veebiallikad

- [Janseni ametlik juhtumiuuringute leht](https://ml4trading.io/case-studies/): üheksa uurimissuuna olemasolu ja kirjeldus. Mahu- ja märkmikunumbrid võivad muutuda.
- [Autori uurimistöövoo ülevaade, 05.05.2026](https://insights.ml4trading.io/p/nine-case-studies-one-end-to-end): ühine uurimise ja teostuse töövoog.
- [scikit-learn: TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html): ajas kasvavad treeningplokid ja `gap`; paneeli ajastus vajab lisaloogikat.
- [scikit-learn: levinud vead](https://scikit-learn.org/stable/common_pitfalls.html): eeltöötluse sobitamine treeningul ja pipeline.
- [scikit-learn: ansamblid](https://scikit-learn.org/stable/modules/ensemble.html): Random Foresti ja boosting'u erinevus.
- [yfinance.download dokumentatsioon](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html): allalaadimisparameetrid; meie kood määrab `auto_adjust=True` sõnaselgelt.
- [SEC EDGAR API-d](https://www.sec.gov/search-filings/edgar-application-programming-interfaces): aruannete ja XBRL JSON-i ametlik ligipääs. Meie kursus ei laadi ettevõtete pärisaruandeid; RAG-demo tekstid on väljamõeldud.

Ametlik veebileht `ml4trading.io/third-edition/` sisaldas kontrollimisel ka varasema reklaamifaasi aastaarvu ja peatükinumbreid, mis ei ühti lisatud PDF-iga. Seetõttu viitame peatükkidele PDF-i järgi, mitte reklaamiploki järgi. Veebidokumentatsiooni versioon ei tõesta, et sama versioon oli käivituskeskkonnas; tegelikud versioonid on `raportid/run.json` ja `requirements-tested.txt`.

## Allikakriitika

Raamat kirjeldab professionaalset tööviisi; see ei tõesta meie strateegia kasumlikkust. Ametlik teegidokumentatsioon selgitab API-d, mitte finantsmudeli sobivust. Meie tulevikustsenaariumid ja meeldejäävad põhimõtted on autoriõiguslikult iseseisvad selgitused, mitte Narangi ega Janseni otsesed tsitaadid.
