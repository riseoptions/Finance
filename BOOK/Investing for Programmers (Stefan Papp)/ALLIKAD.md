# Allikad ja kontrollimise ulatus

Kontrollimise kuupäev: **27.10.2026**. Lingid on esmased allikad või teekide ametlik dokumentatsioon. Dokumentatsiooni lugemine ei ole sama mis API eduka päringu või iga teegiversiooni testimine.

## Põhiallikas

Stefan Papp, *Investing for Programmers: Understanding Markets Through Data and Code*, Manning, ISBN 9781633435803. Kasutatud on kasutaja lisatud PDF-i. Kõigi peatükkide sisukord ja kokkuvõtted on läbi vaadatud; süvendatult valitud lõigud ML-i, agentide, RAG-i ning järeltesti kohta. Täielikku lausehaaval sisuauditit ega kõigi koodinäidete käivitamist ei tehtud. Leheküljed viitavad PDF-i trükitud numbritele.

- [Manningi raamatuinfo](https://www.manning.com/books/investing-for-programmers): ilmumine september 2025. PDF-i autoriõiguse lehel on 2026; neid ei esitata sama väljana.
- [Autori lähtekood](https://github.com/StefanPapp/investing-for-programmers): kontrollitud hoidla struktuur, peatükkide 02–12 märkmikud ning Streamliti failide olemasolu. Hoidlat tervikuna ei kloonitud ega auditeeritud; kursuse näited on iseseisvad ning lähtuvad lisatud PDF-is kontrollitud teemadest.

## Andmed ja teegid

| Allikas | Kontrollitud / kursuses kasutatud |
|---|---|
| [yfinance download](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html) | `auto_adjust`, `multi_level_index`, `start/end`; määrame olulised parameetrid selgesõnaliselt |
| [pandas pct_change](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html) | Suhtelised muutused, puuduvate väärtuste täitmisest hoidumine |
| [TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html) | Ajalised treeningu-/testiosad, `gap` |
| [scikit-learn ansamblid](https://scikit-learn.org/stable/modules/ensemble.html) | Random Forest ja võimendatud puude põhimõtted |
| [XGBoost Python API](https://xgboost.readthedocs.io/en/stable/python/python_api.html) | Valikulise XGBRegressori liides; selle paketi XGBoost-haru käivitamata |
| [SEC EDGAR API](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | Avalikud companyfacts/submissions API-d, API-võtme puudumine, CIK |
| [FRED API võti](https://fred.stlouisfed.org/docs/api/api_key.html) | API v1 võtmenõue |
| [FRED observations](https://fred.stlouisfed.org/docs/api/fred/series_observations.html) | Vaatlusandmed, reaalaja- ja vintage-parameetrid |
| [OpenAI tekstigenereerimine](https://developers.openai.com/api/docs/guides/text) | Responses API sisend ning tekstide leidmine `output` loendist |

API-kutsed Yahoo, SEC, FRED ja live-LLM teenusele ei ole siin edukate integratsioonitestidena kinnitatud. Põhiversioon on tahtlikult offline. API näidete kasutamisel kontrolli teenusetingimusi, kättesaadavust ja kulusid uuesti; teenuse hinnapakette siin ei reprodutseerita.

## Finantsinstrumentide täiendused

- [Euroopa Komisjoni PRIIPSi ülevaade](https://finance.ec.europa.eu/consumer-finance-and-payments/retail-financial-services/key-information-documents-packaged-retail-and-insurance-based-investment-products-priips_en): jaeinvestori põhiteabedokumentide raamistik. Üksiku fondi kättesaadavus tuleb eraldi maakleri ja tootedokumentidest kontrollida.
- [CME: futuuride tagatis](https://www.cmegroup.com/education/courses/introduction-to-futures/margin-know-what-is-needed): futuuritagatis ei ole alusvara sissemakse ega omand.

Valemite ja ülesannete illustratiivsed arvud on kursuse koostaja loodud, mitte turuandmed ega raamatust kopeeritud näited. Õppematerjal eristab arvulist identiteeti investeerimisprognoosist. Näiteks optsiooni payoff-valem kirjeldab tähtaja lepingulist tulemust; see ei prognoosi hinda.

## Täpsustused, mida õpetamisel rõhutada

1. FCF on tuletatud rahavoonäitaja; põhiaruanne on rahavoogude aruanne.
2. Current ratio põhineb bilansi käibevaral ja lühiajalistel kohustistel.
3. ETF-i risk sõltub alusvarast ja struktuurist; ETF-i nimetus üksi ei määra riski.
4. VaR pole maksimaalne kahju ning stop-loss ei taga kindlat hinda.
5. MCP ei taga andmete tõesust; RAG ei välista hallutsinatsioone.
6. Raamatu illustratiivne sulgemishinnapõhine signaal on kursuse järeltestis eraldatud hilisemast täitmisest.

Need on pedagoogilised ja tehnilised täpsustused, mitte väide, et kogu raamatu käsitlus oleks vigane.
