# Allikad, tõenditasemed ja kontrolli piirid

Kontrollimise kuupäev: **29.10.2026**. Veebiallikad olid sel kuupäeval kättesaadavad otsingu või avatud lehe kaudu. Dünaamiliste dokumentatsioonilehtede sisu ja teegiversioonid võivad muutuda. Allikad ei anna garantiid, et õppeprojekti strateegia teenib kasumit.

## Põhiallikas

**[B] Stefan Jansen. Machine Learning for Trading, Third Edition. Packt, 2026. ISBN 978-1-80324-697-0.** Kasutaja lisatud 827-leheküljeline PDF. Tiitelleht ja ilmumisandmed PDF lk 1–2; kolmanda väljaande ilmumisajaks on märgitud juuli 2026. [Peatükkide kaart](RAAMATU_KAART.md) kasutab PDF-i, mitte vananenud veebisisukorda.

Analüüsiti sisukorda, kõigi 27 peatüki algusi ning temaatiliselt valitud käsitlusi töövoost, mudelivalikust, strateegiavõrdlusest, RAG-ist, agentidest ja karjäärist. See pole iga valemi ega kõigi autori märkmike sõltumatu audit. Raamatu strateegiate arvulisi tulemusi ei ole siin reprodutseeritud. Paketi kood, sünteetilised andmed, harjutused ja õpetusnäited on iseseisvalt loodud.

## Täiendavad allikad

| Kood | Allikas | Milleks kasutatud | Tõendi piir |
|---|---|---|---|
| S1 | [Autori koduleht](https://ml4trading.io/) ja [peatükkide ülevaade](https://ml4trading.io/third-edition/chapters/) | 27 peatüki, kuue osa ja tarkvaraökosüsteemi kontroll | Autori enda kirjeldus, mitte sõltumatu tulemuskatse |
| S2 | Gu, Kelly, Xiu, [Empirical Asset Pricing via Machine Learning](https://www.nber.org/papers/w25398), 2018 tööversioon; ajakirjaversioon 2020 | ML-i empiiriline rakendamine varahindamises | Kindel valim ja uurimisseade; ei tõesta iga ML-strateegia kasumlikkust. NBER kirje otsingus kontrollitud, otseavamisel 403 |
| S3 | Bailey jt, [The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf); [ülikooli bibliokirje](https://scholarworks.wmich.edu/math_pubs/42/) | Katsete hulga ja valiku üleõppimine | PBO pole tulevase kahjumi tõenäosus |
| S4 | [scikit-learn: TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | Ajapõhise jaotuse ja gap-parameetri kasutus | Tööriist ei otsusta ise sobivat finantshorisonti |
| S5 | Lewis jt, [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), NeurIPS 2020 | RAG-i algne teaduslik käsitlus ja ajalooline eristus | Tekstiülesannete tulemused ei ole tõend investeerimisalfale |
| S6 | [SEC EDGAR API-d](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Aruannete ja XBRL-i masinloetavad allikad | Algandmete hilisemad versioonid vajavad PIT-käsitlust |
| S7 | [XGBoost Python API](https://xgboost.readthedocs.io/en/stable/python/python_api.html) | XGBRegressor ja parameetrid | API dokumentatsioon, mitte finantsstrateegia hinnang |
| S8 | [BIS: Intelligent financial system](https://www.bis.org/publications/working-paper-1194-intelligent-financial-system-how-ai-transforming-finance), 2024; [Bank of England: Financial Stability in Focus](https://www.bankofengland.co.uk/financial-stability-in-focus/2025/april-2025), 2025 | AI kasutuse, mudeli-, kontsentratsiooni- ja teenusepakkujariskide kontekst | Institutsioonide analüüs, mitte kvantifitseeritud tulevikugarantii |
| S9 | Kim, Muhn, Nikolaev, [Financial Statement Analysis with Large Language Models](https://arxiv.org/abs/2407.17866); [Chicago Boothi ülevaade](https://www.chicagobooth.edu/research/fama-miller/finance-research/funding/a-demand-system-approach-for-fixed-income/financial-statement-analysis-with-large-language-models) | LLM-i potentsiaal kindlas finantsaruannete ülesandes | Uurimuslik tulemus; erinev mudel, prompt, andmed või kulud võivad järeldust muuta |
| S10 | [Options Industry Council: Greeks](https://prd-web.optionseducation.org/advancedconcepts/understanding-options-greeks) | Optsioonide tundlikkuste tõlgendus | Mudelipõhised lähendid, mitte täpse hinnamuutuse garantii |
| S11 | [CME: Mark-to-Market](https://www.cmegroup.com/education/courses/introduction-to-futures/mark-to-market) | Futuuride igapäevane arvestus | Konkreetse lepingu tingimused kontrollida eraldi; ajaloolise lehe kauplemiskellaaegu ei kasutata |
| S12 | [Investor.gov: ETFs](https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-2) | ETF-i turuhinna ja NAV-i eristamine | Erineva ETF-i struktuur ja riskid võivad erineda |
| S13 | [OpenAI: Text generation](https://developers.openai.com/api/docs/guides/text) | Valikuline Responses API tekstinäide | Päris-API ühendust selles paketis ei käivitatud |
| S14 | [ChatGPT Work: alustamine](https://learn.chatgpt.com/docs/get-started-with-work) | Vestlusest tööülesande ja failiväljundini | Konto, keskkond ja tööriistaload mõjutavad võimalusi |
| S15 | [BIS: In data we trust?](https://www.bis.org/publications/fsi-insight-73-data-we-trust-emerging-policy-and-supervisory-approaches-ai-data-use-financial-services), 2026 | Andmete kvaliteet ja kolmandate osapoolte sõltuvus | Järelevalveanalüüs, mitte algoritmide edetabel |
| S16 | [BIS: Artificial intelligence, monetary policy and financial stability](https://www.bis.org/speeches/20261021-artificial-intelligence-monetary-policy-and-financial-stability), 21.10.2026 | Hilisem täiendus: ühised mudelid, karjakäitumine ja operatsioonilised riskid | Kõne kirjeldab riskikanaleid, ei mõõda nende realiseerumise kindlat tõenäosust |
| S17 | [MAS: Safeguards for Agentic Finance at Runtime](https://www.mas.gov.sg/publications/monographs-or-information-paper/2026/safeguards-for-agentic-finance-at-runtime), 03.07.2026 | Agendi tegevuste lubamine, jälg ja inimese sekkumine | Pakutud juhtimisraamistik, mitte universaalne seadus ega tõend kasumlikkusele |

## Mida tähendab „tõendatud”?

| Tase | Näide | Lubatud järeldus | Liiga tugev järeldus |
|---|---|---|---|
| Matemaatiline tulemus eeldustel | Portfelli dispersioon, call'i tasuvus | Valem kehtib oma definitsioonide/eelduste all | Mudeli eeldused kehtivad alati turul |
| Empiiriline teadustulemus | ML või RAG võrdlus konkreetses uurimuses | Meetod töötas uuritud seades | Meetod võidab tulevikus kõikjal |
| Praktiline tööriist | pandas, XGBoost, ajapõhine test | Võimaldab töövoogu teostada | Tarkvara olemasolu tähendab alfat |
| Eksperimentaalne rakendus | Autonoomne uurimisagent, sünteetiline treeningandmestik | Vajab eraldi valideerimist | Demonstreeritud agent on investeerimiseks valmis |
| Prognoos | 2027–2030 stsenaariumid | Tingimuslik arenguvõimalus | Kindel tulevikufakt |

## Märgistus

- **[RAAMAT]**: lisatud PDF-i põhisisu lühike parafraas; peatükiviide on moodulis.
- **[SELGITUS]**: iseseisev pedagoogiline selgitus või süntees, mitte raamatu tsitaat.
- **[NÄIDE]**: iseseisvalt loodud arvutus, kood või fiktiivne olukord.
- **[TÄIENDUS]**: veebiallikast või sõltumatust käsitlusest lisatu; ei tähenda alati, et avaldati pärast raamatut.
- **[HILISEM TÄIENDUS]**: raamatu juulikuise ilmumisaja järel ilmunud materjal.
- **[PROGNOOS]**: autori koostatud tingimuslik stsenaarium.

Muud õppeteksti lõigud, tabelid ja õpetamisvõtted on [SELGITUS]/[NÄIDE], kui neid pole eraldi [RAAMAT]-una märgistatud. Raamatu teksti ega PDF-i paketti ei kopeerita.
