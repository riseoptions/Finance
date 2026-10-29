# Kontrolliaruanne

[Tagasi](README.md)

Kontrollitud 29.10.2026.

## Valminud sisu

- 5 põhimoodulit: olemus, hind, kreeklased, strateegiad, riskijuhtimine.
- Raamatu 16 peatüki ja 5 lisa kaardistus PDF-lehekülgedega.
- 21 sama tähtaja strateegiakaarti koos valemite, arvuliste tabelite ja graafikutega.
- Calendar ja diagonal eraldi mudelipõhiste tabelite ning 2 graafikuga.
- Sünteetika, parity, delta-neutraalsus, wheel ja riskimaandamine.
- 50 põhimõtet, 60 sisulist küsimust ja 20 keerulisemat väitlusküsimust.
- 30 lahendatud ülesannet kolmel raskusastmel.
- Õpetaja käsiraamat: 5 mooduli õpetamisjuhised, 90 minuti tunnimall, tööleht, hindamine ja lõputest.
- 12 väikest Python-demonstratsiooni ja Colabi märkmik.
- 20 õppelehega Markdown-meelespea ning täpselt 20-leheküljeline PDF.
- Eesti–inglise sõnastik ja ametlike täiendavate allikate loend.

## Tegelikult tehtud kontrollid

1. Käivitati kõik 12 Python-demonstratsiooni. Graafikuid kontrolliti serverikeskkonnas Matplotlibi Agg-taustaga; Thonny või Google Colabi kasutajaliidest ei avatud.
2. Käivitati märkmiku kõik 13 koodilahtrit samas Python-nimeruumis järjekorras: mudel + 12 demonstratsiooni.
3. Kontrollskript kontrollis 501 alusvarahinnal baaspositsioonide ja sünteetika identsusi, 21 strateegia teadaolevaid maksimumkahjumeid, maksimumkasumeid, tasuvuspiire ja hinnasaba kallet.
4. BSM-i tulemusi võrreldi tuntud referentsidega: S=K=100,T=1,σ=20%,r=5%,q=0 korral call≈10,45058 ja put≈5,57353. Kontrolliti parity't, IV mõju ja gamma märki.
5. Arvulisi ülesandeid võrreldi lepinguliste valemite ja otseste arvutustega. Valitud korduvad ning keerulisemad arvutused on automaatkontrollides; selgitusülesandeid hinnati sisuliselt.
6. Graafikute ja strateegiatabelite koostamisel kasutati samu sisendandmeid ning valemeid; maksimumid ja tasuvuspiirid kontrolliti eraldi etteantud võrdlusväärtustega.
7. Kontrolliti Markdowni suhteliste faili- ja pildilinkide sihtide olemasolu.
8. Loendati küsimused, põhimõtted, väitlused, ülesanded ja PDF-leheküljed.
9. PDF renderdati visuaalseks kontrolliks; kontrolliti lehtede paigutust, teksti mahtumist ja graafikuid. Kõigi 23 atlase graafiku kuju vaadati üle.

## Kontrolli piirid

Kursuse hinnad on hüpoteetilised. Pole tehtud päris optsioonitehinguid, saadud maakleri täitmishindu ega kontrollitud konkreetse konto marginaali või maksustamist. Kooditestid kinnitavad matemaatika ja rakenduse kooskõla testitud juhtudel, mitte turueelist.

Raamatukaart põhineb sisukorral ja teemakohaste lõikude kontrollil; kogu PDF-i iga lause ja algse diagrammi auditeerimist ei väideta. Algse raamatu pilttabelite arvandmeid ei taastoodeta. Kreeklaste ja hinnamudelite piirangud ning raamatu vaieldavad üldistused on eraldi välja toodud.

Lühimeelespea on kordamiseks. Detailsemad erandid, teostusriskid ja täpsed eeldused tuleb lugeda põhimoodulitest. Eri tähtajaga ja dünaamiliste protsesside jaoks pole loodud eksitavat universaalset lõpphinna payoff'i: nende puhul on näidatud mudeli- või teekonnastsenaariumid.
