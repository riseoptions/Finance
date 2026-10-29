# 30 praktilist ülesannet täielike lahendustega

[Tagasi](../README.md)

[NÄIDE] Kõik hinnad on hüpoteetilised. Kui pole märgitud teisiti, jäetakse intress, dividend, maksud ja kulud välja. P/L tähendab kasumit/kahjumit. Kõik kolm raskusastet sisaldavad arvutamist ja tõlgendamist.

## I tase: alused

### Ülesanne 1. Leia long call’i tulemus kolmel lõpphinnal.

**Andmed:** K=105, c=3, M=100; S=100,110,120.

**Lahendus sammudena:** Väljamaksed on max(S−105,0): 0,5,15. Lahuta igast 3 ja korruta 100-ga: −300, +200, +1200 USD.

**Selgitus ja tõlgendus:** Aktsia hind peab tähtajal ületama 108, et tulemus oleks positiivne.

**Levinud eksimus:** Unustatakse 300 USD preemia.

**Õpitav põhimõte:** Väärtus pole kasum.

### Ülesanne 2. Leia long put’i P/L.

**Andmed:** K=95, p=3, M=100, S=80.

**Lahendus sammudena:** Sisemine väärtus 95−80=15. P/L=(15−3)×100=1200 USD.

**Selgitus ja tõlgendus:** Maksimaalne ostja optsioonikahju on 300, kuid langus andis 1200 kasu.

**Levinud eksimus:** Kasutatakse call’i valemit S−K.

**Õpitav põhimõte:** Put annab müügiõiguse.

### Ülesanne 3. Leia call’i ja put’i tasuvuspiir.

**Andmed:** Call K=100,c=4; put K=100,p=5.

**Lahendus sammudena:** Call: S−100−4=0 → S=104. Put:100−S−5=0 → S=95.

**Selgitus ja tõlgendus:** Need on tähtaja, mitte vahepealse turuhinna piirid.

**Levinud eksimus:** Peetakse strike’i tasuvuspiiriks.

**Õpitav põhimõte:** Tasuvusse kuulub ostuhind.

### Ülesanne 4. Arvuta katmata call’i müüja kahju.

**Andmed:** K=105,c=3,M=100,S=130.

**Lahendus sammudena:** Kohustuse väärtus 25. P/L=(3−25)×100=−2200 USD.

**Selgitus ja tõlgendus:** Edasisel tõusul suureneb kahju piiramatult.

**Levinud eksimus:** Peetakse saadud preemiat maksimaalseks riskiks.

**Õpitav põhimõte:** Krediit pole kahjupiir.

### Ülesanne 5. Arvuta short put’i tulemus nullhinnal.

**Andmed:** K=95,p=3,M=100,S=0.

**Lahendus sammudena:** Müüja ostukohustus maksab 9500, saadud preemia 300. P/L=300−9500=−9200 USD.

**Selgitus ja tõlgendus:** Kahju on lõplik, kuid väga suur võrreldes preemiaga.

**Levinud eksimus:** Rahatagatist peetakse kindlustuseks.

**Õpitav põhimõte:** Võime osta ei taga ostu väärtust.

### Ülesanne 6. Leia sisemine ja väline väärtus.

**Andmed:** S=104,K=100,call’i hind 6.

**Lahendus sammudena:** Sisemine=max(104−100,0)=4. Väline=6−4=2.

**Selgitus ja tõlgendus:** Kaks dollarit maksab allesjäänud võimalus.

**Levinud eksimus:** Kõik 6 nimetatakse ajaväärtuseks.

**Õpitav põhimõte:** Hind koosneb mitmest majanduslikust osast.

### Ülesanne 7. Leia kahe lepingu ostukulu.

**Andmed:** Preemia 2,40; M=100; n=2; komisjon 1 lepingu kohta ostmisel.

**Lahendus sammudena:** Preemia=2,4×100×2=480. Komisjoni 2. Kogukulu 482 USD.

**Selgitus ja tõlgendus:** Noteering ei näita kogu kontoväljaminekut.

**Levinud eksimus:** Korrutatakse komisjon samuti 100-ga.

**Õpitav põhimõte:** Ühikud enne arve.

### Ülesanne 8. Arvuta kohene edasi-tagasi tehing.

**Andmed:** Bid=2,80, ask=3,20,M=100; komisjon 1 ostul ja 1 müügil.

**Lahendus sammudena:** Ost 320, müük 280, tasud 2. P/L=280−320−2=−42 USD.

**Selgitus ja tõlgendus:** Tururiskita hetkeline väljumine pole kuluta.

**Levinud eksimus:** Eeldatakse mõlemas suunas keskhinda 3.

**Õpitav põhimõte:** Täidetav hind loeb.

### Ülesanne 9. Leia delta-lähendus.

**Andmed:** Long call Δ=0,60,ΔS=2,M=100.

**Lahendus sammudena:** Hinnamuutus≈0,60×2=1,20; lepingu muutus≈120 USD.

**Selgitus ja tõlgendus:** Tulemus eeldab teisi sisendeid paigal ja väikest hinnasammu.

**Levinud eksimus:** 120 peetakse garanteeritud kasumiks.

**Õpitav põhimõte:** Delta on lokaalne.

### Ülesanne 10. Arvuta vega mõju õigetes ühikutes.

**Andmed:** Vega=0,12 ühe pp kohta; IV 25%→20%; M=100.

**Lahendus sammudena:** IV muutus=−5 pp. Hinnamuutus≈0,12×(−5)=−0,60; lepingult −60 USD.

**Selgitus ja tõlgendus:** IV langus kahjustab positiivse vegaga positsiooni.

**Levinud eksimus:** Kasutatakse kordajat −0,05 selle ühiku juures.

**Õpitav põhimõte:** Protsendipunkt pole suhteline protsent.

## II tase: kombinatsioonid

### Ülesanne 11. Võrdle covered call’i aktsia hoidmisega.

**Andmed:** S₀=100,K=105,c=3,M=100; S_T=120.

**Lahendus sammudena:** Aktsia kasum 20×100=2000. Short call: (3−15)×100=−1200. Koos +800 USD.

**Selgitus ja tõlgendus:** 800 on selle covered call’i maksimumkasum; üksikaktsia annaks siin rohkem.

**Levinud eksimus:** Loetakse ainult 300 preemiat.

**Õpitav põhimõte:** Preemia eest loovutatakse tõusu.

### Ülesanne 12. Leia protective put’i kahjupõrand.

**Andmed:** S₀=100,K=95,p=3,M=100,S_T=50.

**Lahendus sammudena:** Aktsia −5000; put (45−3)×100=4200. Koos −800 USD. Sama põrand kehtib kõikjal S≤95.

**Selgitus ja tõlgendus:** 300 kindlustuskulu lisandub 500 strike’i-vahe kahjule.

**Levinud eksimus:** Maksimaalseks kahjuks loetakse ainult 500.

**Õpitav põhimõte:** Kaitse hind kuulub kahjupiiri.

### Ülesanne 13. Leia bull call spread’i risk ja tasuvus.

**Andmed:** Osta K100 call 6-ga, müü K110 call 2-ga; M=100.

**Lahendus sammudena:** Deebet=(6−2)×100=400. Laius 1000. Max kasum=1000−400=600. Max kahju=400. Tasuvus=100+4=104.

**Selgitus ja tõlgendus:** Tõusu üle 110 enam juurde ei teenita.

**Levinud eksimus:** Max kasumiks märgitakse kogu 1000.

**Õpitav põhimõte:** Laius jaguneb riskiks ja tasuks.

### Ülesanne 14. Leia bear put spread’i tulemus.

**Andmed:** Osta K110 put 12-ga, müü K100 put 6-ga; M=100,S_T=95.

**Lahendus sammudena:** Netodeebet=6. Väljamakse=(110−95)−(100−95)=10. Kasum=(10−6)×100=400. Max kahju 600; tasuvus 104.

**Selgitus ja tõlgendus:** Langus alla 100 ei suurenda kasumit.

**Levinud eksimus:** Liidetakse mõlema put’i väljamaksed.

**Õpitav põhimõte:** Müüdud jalg lahutatakse.

### Ülesanne 15. Arvuta credit spread’i tasuvus ja maksimumid.

**Andmed:** Müü K100 put 6-ga, osta K90 put 2-ga; M=100.

**Lahendus sammudena:** Krediit 4. Maksimumkasum 400; kahju (10−4)×100=600; tasuvus 100−4=96.

**Selgitus ja tõlgendus:** Saadud 400 on tasu kuni 600 terminalriski eest.

**Levinud eksimus:** Krediit ja deebet segunevad valemis.

**Õpitav põhimõte:** Kirjuta rahavoo märk välja.

### Ülesanne 16. Leia straddle’i tulemus ja piirid.

**Andmed:** K=100,c=6,p=6,M=100,S_T=109.

**Lahendus sammudena:** Kogukulu 12; call 9, put 0. P/L=(9−12)×100=−300. Tasuvus 88 ja 112.

**Selgitus ja tõlgendus:** 9% liikumisest jäi väheks.

**Levinud eksimus:** Arvatakse, et ühe jala ITM tähendab kogukasumit.

**Õpitav põhimõte:** Vaata kogu paketti.

### Ülesanne 17. Leia strangle’i lõpptulemus.

**Andmed:** Put K95 maksab 3,call K105 maksab 3; S_T=112,M=100.

**Lahendus sammudena:** Put 0,call 7,kogukulu 6. P/L=(7−6)×100=100. Tasuvus 89 ja 111.

**Selgitus ja tõlgendus:** Odavam pakett nõudis hinnalt strike’ist kaugemale minekut.

**Levinud eksimus:** Tasuvuspiiriks võetakse 105.

**Õpitav põhimõte:** Mõlema jala hind tuleb tagasi teenida.

### Ülesanne 18. Arvuta butterfly tipp ja serv.

**Andmed:** Long call 90 hinnaga 12; short 2 call 100 hinnaga 6; long call 110 hinnaga 2; M100.

**Lahendus sammudena:** Deebet 12−12+2=2. S100:10−0+0−2=8 →800. S120:30−40+10−2=−2 →−200. Tasuvus 92 ja 108.

**Selgitus ja tõlgendus:** Kasum tekib keskmises vahemikus, mitte lõputu tõusuga.

**Levinud eksimus:** Short-kogus 2 jäetakse arvestamata.

**Õpitav põhimõte:** Kogused määravad kuju.

### Ülesanne 19. Arvuta theta ja gamma koostoime.

**Andmed:** Δ=0,5;Γ=0,04;Θ=−0,03/päev;ΔS=2;möödub 1 päev;M100.

**Lahendus sammudena:** Lähendus=0,5×2+0,5×0,04×2²−0,03=1,05. Lepingu muutus≈105 USD.

**Selgitus ja tõlgendus:** Gamma lisab siin 0,08,theta võtab 0,03; IV jäi eelduslikult samaks.

**Levinud eksimus:** Gamma liikmes unustatakse pool või ruut.

**Õpitav põhimõte:** Teise järgu liige erineb deltast.

### Ülesanne 20. Leia riskieelarvesse mahtuv kogus.

**Andmed:** Konto 25000; eelarve 2%; spread’i max kahju 150; kogu kulureserv 10 positsiooni kohta.

**Lahendus sammudena:** Eelarve=500. Ühe kogurisk 160. n=floor(500/160)=3; kogurisk 480. Neli annaks 640.

**Selgitus ja tõlgendus:** 2% on ülesande eeldus, mitte universaalne sobivusreegel.

**Levinud eksimus:** Ümardatakse üles või ignoreeritakse kulusid.

**Õpitav põhimõte:** Kogus ümardatakse alla.

## III tase: risk ja kriitiline analüüs

### Ülesanne 21. Hinda suure võidumääraga strateegiat.

**Andmed:** p=0,9;W=10;L=120;k=2.

**Lahendus sammudena:** E=0,9×10−0,1×120−2=−5 USD. Tasuvus-p=(120+2)/(10+120)=0,93846 ehk 93,85%.

**Selgitus ja tõlgendus:** 90% võite ei kata kahjusid ja kulusid.

**Levinud eksimus:** Arvestatakse ainult võitude arvu.

**Õpitav põhimõte:** Sagedus ja suurus koos.

### Ülesanne 22. Võrdle püsiprotsendilist ja fikseeritud riski.

**Andmed:** Algkapital 10000;10 kaotust; A kaotab iga kord 10% allesjäänust; B iga kord 1000.

**Lahendus sammudena:** A=10000×0,9¹⁰≈3486,78. B=10000−10×1000=0.

**Selgitus ja tõlgendus:** Riskireegli baas muudab tulemuse; mõlemal on suur drawdown.

**Levinud eksimus:** Öeldakse, et 10% risk hävitab alati konto täpselt 10 tehinguga.

**Õpitav põhimõte:** Protsendi baas tuleb öelda.

### Ülesanne 23. Kontrolli sünteetilist forward’it.

**Andmed:** C=P=6,K100,r=q=0,M100,S_T=80 ja 120.

**Lahendus sammudena:** C−P algkulu 0. Lõpp 80:0−20=−20 →−2000. Lõpp 120:20−0=20 →2000.

**Selgitus ja tõlgendus:** Tasuta avamine sisaldab suurt kohustust.

**Levinud eksimus:** Kasumit arvutatakse ilma put-kohustuseta.

**Õpitav põhimõte:** Null deebet pole null risk.

### Ülesanne 24. Leia ratio spread’i ülemine tasuvuspiir.

**Andmed:** Long call 100 6-ga; short 2 call 110 2-ga;M100.

**Lahendus sammudena:** Deebet 2. S>110 korral P/L=(S−100)−2(S−110)−2=118−S. Ülemine piir 118; alumine 102. S150 annab−3200.

**Selgitus ja tõlgendus:** Tõusu jätkumine muudab esmase võidu kahjuks.

**Levinud eksimus:** Arvatakse, et short-jalad piiravad ainult kasumit.

**Õpitav põhimõte:** Netomüüdud call loob piiramatu saba.

### Ülesanne 25. Leia iron condor’i maksimumid.

**Andmed:** Long put 90 2;short put 95 3;short call 105 3;long call 110 2;M100.

**Lahendus sammudena:** Krediit 2. Keskvahemikus 95–105 kasum 200; tiiva laius 5 annab max kahju 300. Piirid 93 ja 107. S80 korral 2−5=−3 →−300.

**Selgitus ja tõlgendus:** Mõlemad tiivad ei realiseeru sama lõpphinna puhul korraga täies kahjus.

**Levinud eksimus:** Liidetakse automaatselt mõlema tiiva maksimaalne kahju.

**Õpitav põhimõte:** Ühine alusvarastsenaarium on oluline.

### Ülesanne 26. Selgita wheel’i kogu tulemust.

**Andmed:** Short put K95 preemia 3;assignment;siis short call K95 preemia 2;aktsia lõpp 70;M100.

**Lahendus sammudena:** Aktsia muutus 70−95=−25;preemiad 3+2=5;neto−20×100=−2000 USD.

**Selgitus ja tõlgendus:** 500 laekumist ei tee kogutulemust plussiks.

**Levinud eksimus:** Raporteeritakse ainult optsioonipreemiate tootlust.

**Õpitav põhimõte:** Arvesta kogu tsükkel.

### Ülesanne 27. Leia delta-maanduseks vajalik aktsiakogus.

**Andmed:** 3 long call’i;Δ=0,40;M100. Pärast hinnamuutust Δ=0,55.

**Lahendus sammudena:** Algdelta=3×100×0,4=120;neutraliseerimiseks short 120 aktsiat. Hiljem optsioonid+165,aktsiad−120 →neto+45. Uus neutraalsus vajaks veel 45 aktsia lühimüüki.

**Selgitus ja tõlgendus:** Maandamine on dünaamiline ja võib vajada kulukaid tehinguid.

**Levinud eksimus:** Algset maandust peetakse püsivaks.

**Õpitav põhimõte:** Gamma muudab tasakaalu.

### Ülesanne 28. Kontrolli parity’t intressiga.

**Andmed:** S=100,K=100,T=1,r=5%,q=0;C=10.45.

**Lahendus sammudena:** C−P=100−100 e^(−0,05)≈4,8771. P=10,45−4,8771≈5,5729.

**Selgitus ja tõlgendus:** Call ja put ei pea ATM-is võrdse hinnaga olema.

**Levinud eksimus:** Jäetakse strike’i diskonteerimine välja.

**Õpitav põhimõte:** Tulevane raha pole tänane raha.

### Ülesanne 29. Tuvasta backtest’i kolm viga.

**Andmed:** Iga ost ja müük keskhinnaga;optsiooni aegumine arvutatakse ainult aktsia päevase sulgemisega;strateegia valiti sama perioodi 100 variandi hulgast.

**Lahendus sammudena:** 1) Kasuta teostatava hinna ja tasude mudelit. 2) Kontrolli konkreetset arveldus- ja täitmisreeglit ning ajatempleid. 3) Hoia uus hindamisperiood eraldi, raporteeri kogu valikuprotsess.

**Selgitus ja tõlgendus:** Hea ajalooline tulemus võib olla täitmis-, ajastuse- või valikuviga.

**Levinud eksimus:** Parandatakse ainult komisjonitasu ja nimetatakse test realistlikuks.

**Õpitav põhimõte:** Andmetest saadud eelis peab üldistuma.

### Ülesanne 30. Võrdle kolme tõusuvarianti sama riskieelarvega.

**Andmed:** Eelarve 600 USD;A call K105,c 3;B bull call 100/110,deebet 4;C aktsia 100. M100;aktsiaid võib osta üksikult;sisend S_T=110;kulud 0.

**Lahendus sammudena:** A:2 lepingut,risk 600;kasum 2×(5−3)×100=400. B:1 spread,risk 400;kasum(10−4)×100=600;200 jääb kasutamata. C:6 aktsiat,risk 600 nullhinna korral;kasum 6×10=60.

**Selgitus ja tõlgendus:** Sama maksimaalne rahaline risk ei anna sama suunatundlikkust, kasumipiiri ega aegumisriski.

**Levinud eksimus:** Võrreldakse 100 aktsiat ja 1 optsiooni justkui sama riskiga.

**Õpitav põhimõte:** Võrdluse alus tuleb enne valida.

