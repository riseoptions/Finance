# Teisipäev: päev 2


## A. 08.50 – Liiga ilus esimene graafik

[SIMULATSIOON] Maarika näitab Danielile järsult tõusvat joont. Ta oli järjestanud varad kuu lõpuhinna järgi ning kasutanud sama kuu tootlust. „Kas ostsid kuu alguses seda, mille võitja sa kuu lõpus teada said?” küsib Daniel. Maarika vaatab koodi. Korrutamine oli matemaatiliselt õige; ajaline tähendus oli vale.

## B. Paranduse plaan

Ta peab lahutama kaks küsimust: kas reegel valib häid varasid ja kas simulatsioon lubab teostamatuid tehinguid. Ta ei hakka kohe otsima paremat mudelit. Kõigepealt fikseerib ta täitmise järgmise vaatluspäeva sulgemisele. Nii jääb andmete valmimise ja orderi vahele terve vaatlusvahemik.

Ta kaalub lihtsat `.shift(1)` parandust, kuid loobub paneelitabelis pimedast nihkest: üks rida tähendaks teist ETF-i, mitte järgmist kuud. Ta ühendab read selgesõnaliste aegade kaudu.

## C. 10.35 – Kaupleja küsib puuduva numbri

Elena: „Kus on ostu ja müügi kulu?”

Maarika: „Mul on üks 10 baaspunkti tasu kuus.”

Elena: „Kui midagi ei muutu, miks maksad sama palju kui kogu portfelli vahetamisel?”

Maarika arvutab käibe tegelike triivinud kaalude ja uute sihtkaalude vahelt. Turu liikumise tõttu ei ole vana 50/50 portfell kuu lõpus enam 50/50. Ka võrdkaalubaas maksab ümberjaotamise eest.

## D. Mida järeltest teeb?

[JANSEN] Peatükk 16: simulatsioon seob prognoosi positsiooni, hinna ja piirangutega. [NARANG] Peatükid 5 ja 9: kulud ning testimise kord on strateegia uurimise osad. Backtest on kontrollitud ajalooline katse, mitte tagantjärele kirjutatud ostusoovitus.

Loos parandatud tulemus ei pea enam hea olema. Vea leidmine on väärtuslik: see takistab vale järelduse kalliks muutumist.

## E. Matemaatiline üllatus

[NÄIDE] +20% ja −20% annavad aritmeetilise keskmise 0%, kuid kapital muutub $1.2\cdot0.8=0.96$: kaotus 4%. Geomeetriline keskmine perioodi kohta on $\sqrt{0.96}-1\approx-2.02\%$.

Kui portfell vahetatakse täielikult, on ostude ja müükide kogumaht ligikaudu 200% NAV-ist. Kulu 10 bp tehingupoole kohta tähendab ligikaudu 20 bp, mitte 10 bp. Täpne simulaator arvestab ka kulude mõju investeeritavale kapitalile.

## F. 13.00 – Baasversioon

[PRAKTIKA] Käivita `python/paev2.py`. Vaata `raportid/lopptest_reegel.csv`: igal real on tootlus, käive ja kulu. Kontrolli käsitsi üht kuud. `python/projekt.py` võrdleb kõiki mudeleid sama täitmismootoriga.

Maarika jätab lõppkatse failid selle loo etapis suletuks. Õppematerjal annab need korratavuse huvides kaasa, kuid õppija võiks kolmapäevani vaadata ainult valideerimistabelit. Fikseeritud algoritme jooksutatakse tehniliselt ühe käsuga; see ei anna luba lõppperioodi järgi parameetreid valida.

## G. 15.20 – Statistiline lõks

Daniel küsib, mitu vaatenurka Maarika proovis. „63 päeva, 42 päeva ja üks viis päeva vahele jättev variant.” Kui avaldatakse ainult parim, pole selle tulemus enam ühe hüpoteesi neutraalne test. Maarika kirjutab kõik katsed päevikusse ja jätab põhikatsesse eelnevalt määratud 63 päeva.

Kuue ETF-i tootlused on korreleerunud. Tavaline sõltumatute ridade t-test annaks liiga kindla mulje. Õppenäite ringplokk-bootstrap kasutab kuiste portfellitootluste paarisvahesid ning säilitab lühikest ajalist sõltuvust. See ei paranda kõiki valikukallutatusi.

## H. 16.30 – Päeva otsus

Baasversioon on kontrollitav, mitte heaks kiidetud. Maarika dokumenteerib eemaldatud ajastusvea ja kulumudeli. Homme peab keerukam mudel võistlema just selle ausa baasiga, mitte vana vigase graafikuga.

## I. Õhtune märkmik

**Viis mõistet:** liittootlus, Sharpe, langus tipust, tulevikuinfo leke, valikukallutatus.

**Põhimõtted:** ilus joon ei kontrolli ajastust; kulu sõltub tehingust; sõltuvad read pole sõltumatud tõendid; ka ebaõnnestunud katsed kuuluvad päevikusse.


---

Edasi: [teooria](teooria.md) · [praktikum](praktikum.md) · [ülesanded ja lahendused](ulesanded-lahendused.md) · [sisukord](../README.md)
