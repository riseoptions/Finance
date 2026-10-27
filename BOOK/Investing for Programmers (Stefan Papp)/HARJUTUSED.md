# Harjutused ja kontrollküsimused

Kõik arvud on õppeillustratsioonid. Iga mooduli tööleht: 5 kontrollküsimust, 3 eri taseme ülesannet, iseseisev Pythoni ülesanne ja juhtum. Lahendused on eraldi failis.

## M01. Investeerimise loogika ja finantsinstrumendid

### Kontrollküsimused

1. Kas indeksit ennast ostetakse?
2. Kas kõik ETF-id on indeksfondid?
3. Millal saab aktsionär raha?
4. Kas võlakiri on riskivaba?
5. Miks pole 10% miinus 4% täpne reaaltootlus?

### Ülesanded

1. **Algaja:** Aktsia 50 → 54, dividend 1. Leia kogutootlus.

2. **Kesktase:** Investeering 2000 eurot teenib 8%, inflatsioon 3%. Leia reaaltootlus.

3. **Edasijõudnu:** ETF-i alusvara kasvas dollarites 10%, dollari euroväärtus langes 8%. Leia eurotootlus.

### Iseseisev Python

Kirjuta funktsioon, mis leiab hinnapaari ja dividendi kogutootluse; kontrolli sisendi positiivset ostuhinda.

### Juhtum

Õppija tahab kolme kuu pärast sissemakseks vajalikku raha aktsia-ETF-i panna. Mida kontrollid?

## M02. Aruanded, suhtarvud ja kasvutees

### Kontrollküsimused

1. Mis eristab bilanssi ja kasumiaruannet?
2. Kas FCF on kasum?
3. Kas madal P/E on alati odav?
4. Miks salvestada aruande avaldamisaeg?
5. Mis muudab teesi kontrollitavaks?

### Ülesanded

1. **Algaja:** Varad 900, kohustised 650. Leia omakapital.

2. **Kesktase:** Hind 40, kasum 120 ja 60 aktsiat. Leia EPS ja P/E.

3. **Edasijõudnu:** Müügitulu kasvab 1000-lt 1200-le, marginaal langeb 10%-lt 6%-le. Kuidas muutub kasum?

### Iseseisev Python

Kirjuta P/E funktsioon, mis tagastab EPS<=0 korral None, ning testi positiivset ja negatiivset EPS-i.

### Juhtum

Kaks ettevõtet: P/E 8 ja P/E 30. Kumba saad nende andmete põhjal odavamaks pidada?

## M03. Andmed ja korratav uurimistöö

### Kontrollküsimused

1. Miks pole puuduv hind null?
2. Miks ei kasutata juhuslikku ajajaotust?
3. Mida tähendab auto_adjust?
4. Mida tähendab end kuupäev Yahoo päringus?
5. Mis on survivorship bias?

### Ülesanded

1. **Algaja:** Leia 80 → 84 tootlus.

2. **Kesktase:** Aktsia hind 120 → 60 splitiga 2 : 1, sul oli üks aktsia. Kas kaotasid 50%?

3. **Edasijõudnu:** Aruande periood lõpeb 31.12, avaldamine 20.02. Millal tohib näitaja ajaloolisse mudelisse lisada?

### Iseseisev Python

Lisa hinnatabelile duplikaatkuupäev ja tõenda, et kvaliteedikontroll selle tagasi lükkab.

### Juhtum

Päring tagastab ühe vara kohta 100 päeva vähem. Kas täidad eelmise hinnaga?

## M04. Tootlus, portfell ja võrdlusindeks

### Kontrollküsimused

1. Miks +20% ja −20% ei anna nulli?
2. Mis on CAGR?
3. Kas volatiilsus on maksimaalne kahjum?
4. Millal kehtivad konstantsete kaalude päevatootlused?
5. Miks võrrelda samas valuutas?

### Ülesanded

1. **Algaja:** 100 → 110 → 99. Leia kogutootlus.

2. **Kesktase:** Portfell 70% aktsiad tootlusega 12%, 30% võlakirjad tootlusega −2%.

3. **Edasijõudnu:** Kaks võrdselt kaalutud 20% volatiilsusega vara, korrelatsioon 0,5. Leia portfelli volatiilsus.

### Iseseisev Python

Arvuta kaheperioodilise võrdselt algkaalutud portfelli tootlus ja võrdle igal perioodil tasakaalustamisega. A=[100,120,120], B=[100,100,120].

### Juhtum

Strateegia teenib 8%, SPY 12%, kuid strateegial on 70% võlakirju. Kas strateegia ebaõnnestus?

## M05. Tuluportfell, võlakirjad ja krüpto

### Kontrollküsimused

1. Kas kõrge dividendimäär tõendab head investeeringut?
2. Mis erineb kupongimääral ja YTM-il?
3. Miks hind intressi kasvades langeb?
4. Kas staking kaitseb hinnalanguse eest?
5. Miks 4% reegel pole garantii?

### Ülesanded

1. **Algaja:** Dividend 3 ja hind 75. Leia dividendimäär.

2. **Kesktase:** Aasta pärast makstakse 1050. Hind praegu 1000. Leia YTM.

3. **Edasijõudnu:** 100 tokenit teenivad 8% tokenites, hind langeb 25%. Leia rahaline tootlus.

### Iseseisev Python

Leia kolmeaastase 5% kupongiga võlakirja YTM hinnaga 950 ning kontrolli vastupidise hinnavalemiga.

### Juhtum

Investor müüb laiapõhjalise fondi ja ostab ühe 12% dividendimääraga ettevõtte, et tulu tõsta.

## M06. Varamonitor, valuuta ja SQL

### Kontrollküsimused

1. Mis on positsioon?
2. Miks ei piisa tickerist?
3. Kas puuduva hinna võib asendada nulliga?
4. Miks SQL-liitmine võib väärtust kahekordistada?
5. Kas hetkevaradest saab täpse tootluse?

### Ülesanded

1. **Algaja:** 5 aktsiat × 80 USD × 0,9 EUR/USD.

2. **Kesktase:** USD-vara väärtus 900 EUR ja raha 600 EUR. Leia kaal.

3. **Edasijõudnu:** Kurss 1,25 USD/EUR, vara 1000 USD. Leia EUR-väärtus ja vale korrutamise tulemus.

### Iseseisev Python

Loo SQLite tabel ja leia parameetriga päringus ainult USD-positsioonide väärtus.

### Juhtum

Üks maakler näitab 10 000 ja teine 8000. Kas kokku on 18 000?

## M07. Risk, optsioonid ja futuurid

### Kontrollküsimused

1. Kas VaR on suurim võimalik kaotus?
2. Kas stop-loss tagab hinna?
3. Mis erineb payoff ja profit mõistetel?
4. Kas futuuri tagatis on ostuhind?
5. Miks kriis vähendab hajutamise abi?

### Ülesanded

1. **Algaja:** Call K=50, preemia 3, lõpphind 58, kordaja 100.

2. **Kesktase:** Vara 100 → 80 → 88. Leia max drawdown ja kogutootlus.

3. **Edasijõudnu:** Pikk futuur 200 → 190, kordaja 20, tagatis 400.

### Iseseisev Python

Kirjuta kaitstud aktsia kasumifunktsioon: ost 100, put strike 95 ja preemia 3. Kontrolli hindu 70 ja 120.

### Juhtum

Viie aasta andmetest saad 99% VaR-i. Kas see katab järgmise kriisi?

## M08. Masinõpe: baasmeetodist ausa hindamiseni

### Kontrollküsimused

1. Mis on tunnus ja siht?
2. Miks võrrelda hinnaprognoosi eilse hinnaga?
3. Miks standardiseerida treeningul?
4. Kas klaster on ostusoovitus?
5. Kas parem RMSE tähendab kasumit?

### Ülesanded

1. **Algaja:** Tegelikud [2,4], prognoosid [1,5]. RMSE?

2. **Kesktase:** 100 juhtumist 65 tõusu, mudel 62 korda õige. Võrdle enamuse baasiga.

3. **Edasijõudnu:** Siht katab järgmised 5 kauplemispäeva. Viimane treeningotsus esmaspäeval, test algab teisipäeval. Mis viga?

### Iseseisev Python

Arvuta nullprognoosi RMSE käsitsi NumPyga sihtidele [0.01,-0.02,0.01].

### Juhtum

Test-RMSE paraneb 1%, tehingusagedus kasvab viis korda.

## M09. LLM, RAG ja piiratud uurimisagent

### Kontrollküsimused

1. Mis on RAG?
2. Kas otsinguskoor on tõeväärtus?
3. Mis eristab agenti töövoost?
4. Kus arvutada tootlus?
5. Kas kaks nõustuvat LLM-i kinnitavad fakti?

### Ülesanded

1. **Algaja:** 20 väitest 16 on tõendatud. Leia osakaal.

2. **Kesktase:** RAG leiab 12 küsimusest 9 puhul vajaliku lõigu. Recall?

3. **Edasijõudnu:** Agent säästab 15 minutit, kuid 4 aruandest üks vajab 30 minuti parandusi. Keskmine ajasääst?

### Iseseisev Python

Tõenda, et agent ei käivita tööriista nimega kauple, ja selgita, miks suvalist eval-i ei tohi kasutada.

### Juhtum

LLM viitab aastaaruandele, aga väidab seal puuduvat kasvuootust.

## M10. Graafikud ja tehnilised indikaatorid

### Kontrollküsimused

1. Mida näitab OHLC?
2. Miks SMA hilineb?
3. Kas RSI 70 tähendab kindlat langust?
4. Kas Bollingeri piir on kindel tõenäosusvahemik?
5. Miks erinevad RSI-d platvormidel?

### Ülesanded

1. **Algaja:** SMA3 hindadest 8,10,12.

2. **Kesktase:** EMA eelmine 20, hind 24, alfa 0,25.

3. **Edasijõudnu:** Keskmine tõus 3 ja langus 1. Leia RSI; kas see käsib müüa?

### Iseseisev Python

Arvuta SMA3 sarjale [10,12,14,16] ja kontrolli, et esimesed kaks väärtust puuduvad.

### Juhtum

Näed kümne aasta graafikul ideaalset mustrit ning valid selle järgi parameetrid.

## M11. Algoritmiline kauplemine ja järeltest

### Kontrollküsimused

1. Mis on backtest?
2. Miks signaal ja täitmine eraldada?
3. Kas limit order tagab tehingu?
4. Mis on slippage?
5. Miks testida eri kulu tasemeid?

### Ülesanded

1. **Algaja:** Kasum enne kulusid 30, kaks tehingut tasuga 2. Neto?

2. **Kesktase:** Positsioon 10 000, ostu- ja müügikulu kumbki 0,1%, hind ei muutu. Ligikaudne kahjum?

3. **Edasijõudnu:** SMA-signaal tekib esmaspäeva sulgemisel, täitmine teisipäeva sulgemisel. Mis on esimene teenitav close-to-close tootlus?

### Iseseisev Python

Tõsta tehingukulu 0%-lt 0,3%-le ning kontrolli, et sama signaalireegli lõppväärtus ei kasva.

### Juhtum

1000 parameetrikombinatsioonist üks teenib testis suurepäraselt.

## M12. Erakapital ja iduettevõtete hindamine

### Kontrollküsimused

1. Mis on pre-money?
2. Mis on dilution?
3. Kas väiksem protsent tähendab alati väiksemat euroväärtust?
4. Mis on runway?
5. Miks exit ei pruugi jaguneda osalustega võrdeliselt?

### Ülesanded

1. **Algaja:** Pre-money 9 mln, uus raha 1 mln. Osalus?

2. **Kesktase:** Sul 15%, uus voor annab uuele investorile 25%. Uus osalus?

3. **Edasijõudnu:** Raha 300 000, kuine netokulu 25 000; järgmise kuu algusest kulu 30 000. Kestus?

### Iseseisev Python

Arvuta 10% osalus pärast kahte vooru, kus uued investorid saavad vastavalt 20% ja 25%.

### Juhtum

Sõber pakub osalust ja ütleb, et järgmise vooru hinnang teeb sind paberil rikkaks.

## M13. Otsustusprotsess, lõpp-projekt ja õpetamine

### Kontrollküsimused

1. Kas edukas tehing tõendab head meetodit?
2. Mis on hindsight bias?
3. Miks dokumenteerida ümberlükkamise tingimus?
4. Millal lisada agent?
5. Mida õpetamisel hinnata?

### Ülesanded

1. **Algaja:** Iga jooks säästab 10 min, aastas 24 jooksu. Ajasääst?

2. **Kesktase:** Arendus 6 h, iga jooks säästab 15 min. Mitu jooksu tasuvuseni?

3. **Edasijõudnu:** 10 analüüsist 8 olid hästi põhjendatud, 6 teenisid kasumit. Kas kvaliteet on 60% või 80%?

### Iseseisev Python

Loo funktsioon, mis leiab automatiseerimise tasuvuseks vajalike jooksude täisarvu.

### Juhtum

Sinu parim katse kaotab nullbaasile. Kas lõputöö ebaõnnestus?
