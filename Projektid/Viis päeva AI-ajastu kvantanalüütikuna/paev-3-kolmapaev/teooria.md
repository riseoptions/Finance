# Päev 3: mida mudel õpib?

[JANSEN: ptk 7, 11–13, 22, 24; NARANG: ptk 3]

**Regressioon** ennustab arvu, näiteks järgmise perioodi tootlust. **Klassifitseerimine** ennustab klassi või selle tõenäosust, näiteks kas tootlus on positiivne. Tõenäosus 60% pole lubadus 60% tootluseks. Kalibreerimine küsib, kas 60% prognooside hulgas toimub sündmus ligikaudu 60% kordadest.

## Kolm meetodit

| Meetod | Sisend ja väljund | Tugevus | Peamine piir |
|---|---|---|---|
| Momentum-reegel | 63 päeva tootlus → järjestus | Selge, ei vaja sobitamist | Ei õpi muutuvaid seoseid |
| Ridge | 3 tunnust → järgmise kuu tootlus | Regulaaritud lineaarne baas | Mittelineaarsus vajab lisatunnuseid |
| Random Forest | Samad tunnused → puude keskmine | Tingimuslikud mittelineaarsed seosed | Väike valim, ebastabiilsus, piiratud ekstrapolatsioon |
| XGBoost, lisakatse | Järjestikku parandatud puud | Paindlik tabulaarandmetel | Rohkem seadistusvalikuid ja üleõppimisriski |
| Närvivõrk, arutelu | Palju tunnuseid / järjestus | Keerulised esitused | Andmenõudlus ja keerukus ei ole siin põhjendatud |

Random Forest keskmistab osaliselt juhuslikke puid; boosting lisab järjest mudeleid, mis parandavad olemasoleva ansambli vigu. Need pole sünonüümid. Põhipakett võrdleb esimest kolme; XGBoosti ja süvaõppe eelist ei väideta ega maskeerita testituks.

Ridge minimeerib $\sum(y_i-b-x_i^T\beta)^2+\lambda\sum\beta_j^2$. Suurem $\lambda$ surub koefitsiente nulli suunas. [NÄIDE] Ühe keskendatud tunnuse korral, kui $x^Tx=4$, $x^Ty=2$ ja $\lambda=1$, on $\hat\beta=2/(4+1)=0.4$ võrreldes OLS-i 0,5-ga. Python: `2/(4+1)`. Kahandamine lisab nihet, kuid võib vähendada hinnangu dispersiooni.

## Mõõdikud koos

$RMSE=\sqrt{\frac1n\sum(y_i-\hat y_i)^2}$ on tootluse ühikutes. Prognoosivead 1 ja −3 protsendipunkti annavad $\sqrt{(1^2+3^2)/2}=2.236$ protsendipunkti. Kõrge riskiga vara eksimus kaalub ruutveas palju.

Precision $=TP/(TP+FP)$: kui ennustasime tõusu, kui sageli tõus tuli? Recall $=TP/(TP+FN)$: kui tõus tuli, kui sageli selle leidsime? Kui TP=30, FP=20 ja FN=10, saame 60% ja 75%. Python: `30/50, 30/40`. Need ei arvesta positsiooni suurust ega kasumi suurust.

Meie lihtne skoorimisraport ühendab paneeliread. Selle mõõdikuid ei esitata sõltumatute vaatluste statistilise tõendina. Stabiilsust hinnatakse lisaks valideerimis- ja lõppperioodi eraldi tabelitega; täiendavalt tuleks võrrelda aastaid ja tururežiime.

## Ajastuse kolm kaitset

1. Tunnus on arvutatud ainult signaalihetkeks olemasolevatest hindadest.
2. Treeningu sihtperiood peab olema lõppenud enne uue signaali arvutamist.
3. Mudeli ja eeltöötluse parameetreid ei valita lõppkatse põhjal.

Tavaline juhuslik `train_test_split` ei järgi siin neid nõudeid. Ka `TimeSeriesSplit` ei lahenda ise paneeli kuupäevi ega kattuvaid silte: lõika kuupäevad, seejärel vali kõik selle kuupäeva read. Päevase kattuva kuu-tootluse märgendiga oleks vaja pikemat purge'i, mitte ainult järgmise rea välja jätmist.

LLM-i, RAG-i ja agendi erinevusi käsitleb [AI-lisa](../ai-ja-promptid.md). Mudeli võime kirjutada veenvat teksti ei valideeri tema numbreid.


Edasi: [praktikum](praktikum.md) · [ülesanded](ulesanded-lahendused.md)
