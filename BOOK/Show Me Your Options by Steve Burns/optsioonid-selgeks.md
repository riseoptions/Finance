# Optsioonid selgeks – 20 lehekülge kõige olulisemast

[Tagasi](README.md)

Markdownis pole fikseeritud leheküljemõõtu. Siin on20 eraldi õppelehte; kaasasolev [PDF](optsioonid-selgeks-20lk.pdf) on täpselt20 lehekülge, üks teema lehel. Kõik näited on hüpoteetilised. Need lehed on meelespea, täiskäsitlus on moodulites ja strateegiate atlases.

## Leht 1. Õigus enne valemit

[SELGITUS] Optsioon on tingimuslik leping. Call annab õiguse osta, put õiguse müüa kokkulepitud strike’iga. Ostja maksab preemia; müüja võtab kohustuse. Ära küsi esimesena, kas turg tõuseb. Küsi, millise õiguse ostad ja millise kohustuse võtad.

[NÄIDE] Call K105 maksab 3. S120 korral on õigus väärt 15, kuid kasum 12 ühe alusvaraühiku kohta. M100 korral tähendab see 1200 USD. S90 korral jääb õigus kasutamata ja kahju on 300.

**Piirang:** Õigus võib aeguda; aktsia omand ei lõpe samal viisil. Ostetud optsioon on siiski finantsvara.

**Kontrollküsimus:** Selgita, miks call’i ostja ei pea halba ostutehingut tegema.

**Vastus:** Ta ostis valikuõiguse. Kahjulikku täitmist võib vältida, kuid juba makstud preemia jääb kuluks.

## Leht 2. Neli baaspositsiooni

[SELGITUS] Long call ja long put ostavad õiguse. Short call ja short put müüvad õiguse. Ostetud lepingu kahju piirdub preemiaga enne täitmisest tekkivat uut positsiooni. Katmata short call’i kahju võib olla piiramatu; short put’i kahju on aktsia nullhinna korral suur, kuid lõplik.

[NÄIDE] K100,p 4,M100: short put’i maksimumkasum 400, maksimumkahju 9600. Sama put’i ostjal on vastupidine optsiooni P/L.

**Piirang:** Sell to close ei ole sama mis sell to open. Positsiooni mõju sõltub sellest, mis enne kontol olemas oli.

**Kontrollküsimus:** Kas call’i müük tekitab alati piiramatu riski?

**Vastus:** Ei. Varem ostetud call’i müük võib positsiooni täielikult sulgeda.

## Leht 3. Lepingutingimused

[SELGITUS] Kontrolli alusvara, strike’i, tähtaega, kogust, kordajat, täitmisstiili ja arveldust. Ameerika tüüpi lepingut võib täita enne tähtaega; Euroopa tüüpi üldjuhul lõpus. Füüsiline arveldus võib anda aktsiad, rahaline arveldus rahasumma. Need on eri tunnused.

[NÄIDE] Noteering 2,40, kordaja 100 ja kolm lepingut tähendab 720 USD preemiat enne kulusid. Kui üleantav vara on korporatiivse sündmusega korrigeeritud, ei pruugi standardne 100 aktsia oletus sobida.

**Piirang:** Viimane kauplemisaeg, täitmisotsuse tähtaeg ja arveldushetk võivad erineda.

**Kontrollküsimus:** Kas Euroopa optsioon tuleb alati lõpuni hoida?

**Vastus:** Ei. Täitmispiirang ei takista tavaliselt turul varem sulgemist, kui leidub sobiv vastaspool.

## Leht 4. Väljamakse ja kasum

[SELGITUS] Call’i terminalväljamakse on max(S−K,0). Put’il max(K−S,0). Kasumi saamiseks lahuta ostuhind või müüja korral lahuta kohustuse väärtus saadud preemiast. Korruta kordajaga ja lahuta kulud.

[NÄIDE] K105,c 3,M100. S100 annab−300;S105 annab−300;S110 annab+200;S120 annab+1200. Call’i tasuvuspiir on 108.

**Piirang:** Tasuvuspiir K+c kehtib tähtajal. Enne seda võib call’i turuhind tõusta ka S<K+c korral.

**Kontrollküsimus:** S107 puhul on call rahas. Kas ostja võitis?

**Vastus:** Ei. Sisemine väärtus 2 ei kata 3 makstud preemiat: kahju 100 USD.

## Leht 5. Sisemine ja väline väärtus

[SELGITUS] Sisemine väärtus kirjeldab kohese täitmise majanduslikku kasu. Väline väärtus on turuhinna ülejääk selle suhtes. Välist osa nimetatakse sageli ajaväärtuseks, kuid seda muudavad ka IV, hind ja intress.

[NÄIDE] S104,K100,call 6: sisemine 4 ja väline 2. Kui aegumise hetkel S104, jääb väärtuseks 4. Ostja kaotab 2 ühikut ehk 200 USD.

**Piirang:** Euroopa lepingute kohene täitmine pole võimalik; intress ja dividendid muudavad lihtsa võrdluse mõnes olukorras nüansirikkaks.

**Kontrollküsimus:** Kas ajaväärtuse langus tõestab theta mõju?

**Vastus:** Mitte üksinda. Sama päeva IV langus võib samuti välist väärtust vähendada.

## Leht 6. Volatiilsuse eest maksmine

[SELGITUS] IV on optsiooni hinnast mudeli abil tuletatav volatiilsus. Kõrgem IV suurendab standardse ostetud call’i ja put’i mudeliväärtust muu sama korral. See ei tähenda, et kõrgema IV-ga ost oleks parem: maksad võimaluse eest rohkem.

[NÄIDE] Call’i delta mõju on+1, kuid IV langus annab vega kaudu−1,20. Summa on−0,20 enne gamma ja theta mõju. Õige hinnasuund võib tähendada kahjumit.

**Piirang:** Enne uudist kõrge IV võib pärast uudist langeda. Vaja on võrrelda tegelikku liikumist hinnas olnud ootusega.

**Kontrollküsimus:** Kas kõrge IV teeb müümise automaatselt kasulikuks?

**Vastus:** Ei. Kõrge preemia võib õiglaselt kajastada suurt hüppe- ja sabariski.

## Leht 7. Delta ja gamma

[SELGITUS] Delta on hinna lokaalne tundlikkus alusvara suhtes. Gamma mõõdab delta muutumist. Call’i delta on tavaliselt positiivne, put’il negatiivne; mõlema ostetud standardoptsiooni gamma on positiivne. Müüdud positsioonil pöörduvad märgid.

[NÄIDE] Δ0,50,Γ0,04 ja S+3 annavad uueks deltaks ligikaudu 0,62. Hinnamuutuse teise järgu hinnang on 0,50×3+0,5×0,04×9=1,68 ühikut.

**Piirang:** Suure muutuse puhul muutuvad ka kreeklased. Delta pole kõikide hinnamuutuse põhjuste summa ega täpne kasumitõenäosus.

**Kontrollküsimus:** Kas delta 0,5 garanteerib+5, kui S tõuseb 10?

**Vastus:** Ei. Delta on hetkeline ja ülejäänud sisendid võivad samuti muutuda.

## Leht 8. Theta, vega ja rho

[SELGITUS] Theta kirjeldab aja möödumise mõju, vega IV muutuse mõju ja rho intressi mõju. Kontrolli ühikuid: siin on theta päeva kohta ning vega ja rho ühe protsendipunkti kohta. Ostetud optsioonide theta on sageli negatiivne, kuid mitte igas olukorras.

[NÄIDE] Vega 0,12 ja IV25%→20% annavad ligikaudu−0,60 ühikut. Theta−0,04 kolme päeva jooksul annab lokaalselt−0,12. Call’i rho 0,08 ning intress+1 pp annab+0,08.

**Piirang:** Ära summeeri tundlikkusi ilma nende sisendmuutuste ja ühikuteta. Positiivne theta ei ole kontole garanteeritud laekumine.

**Kontrollküsimus:** Mitu protsendipunkti on 20%→24%?

**Vastus:** Neli. Suhteline kasv on 20%, kuid vega ühe protsendipunkti ühikus kasutatakse arvu 4.

## Leht 9. Covered call ja cash-secured put

[SELGITUS] Covered call tähendab aktsiat koos müüdud call’iga: preemia eest loovutatakse osa tõusust. Cash-secured put tähendab müüdud put’i koos ostukohustuseks reserveeritud rahaga. Mõlemad kannavad olulist langusriski.

[NÄIDE] Covered call:S₀100,K105,c 3. Maksimumkasum 8 ühikut, nullhinna korral kahju 97. Cash-secured put:K95,p 3. Maksimumkasum 3, nullhinna korral kahju 92.

**Piirang:** Need näited pole omavahel täpsed sünteetilised vasted, sest strike’id erinevad. Täpne seos vajab sama strike’i, tähtaega ja rahastust.

**Kontrollküsimus:** Mida covered call’i kate tegelikult katab?

**Vastus:** Aktsiate tarnimise kohustust, mitte aktsia turuhinna langust.

## Leht 10. Protective put ja collar

[SELGITUS] Protective put lisab aktsiale kindla tähtajani müügihinna kaitse. Collar lisab veel müüdud call’i, et kaitsekulu osaliselt või täielikult rahastada. Tulemuseks on nii alumine kui ka ülemine piir.

[NÄIDE] Aktsia 100 ja put 95 hinnaga 3: kahjupõrand−8, tõus avatud. Lisa call 105 preemiaga 3: netopreemia 0 ning terminaltulemus vahemikus−5 kuni+5 ühikut.

**Piirang:** Zero-cost tähendab ainult null netopreemiat antud näites. Tõusupotentsiaali loovutamine on majanduslik hind.

**Kontrollküsimus:** Miks ei ole collar tasuta kindlustus?

**Vastus:** Sest aktsia hinnatõus üle call’i strike’i läheb call’i ostja kasuks.

## Leht 11. Vertikaalsed spread’id

[SELGITUS] Vertikaal kasutab sama tüübi ja tähtajaga optsioone eri strike’idel. Ostud ja müügid piiravad nii kasumit kui ka kahju. Debit tähendab maksmist, credit laekumist; see ei ütle üksinda strateegia kvaliteeti.

[NÄIDE] Bull call 100/110, preemiad 6 ja 2: deebet 4, max kahju 400, max kasum 600, tasuvus 104. Bear call samade jalgade vastasmärkidega: krediit 400,max kahju 600,tasuvus 104.

**Piirang:** Ühe jala varajane täitmine võib luua ajutise aktsiapositsiooni ja rahavajaduse. Lõpptähtaja piir ei ole täielik operatiivne plaan.

**Kontrollküsimus:** Kuidas credit-vertikaali kahju leida?

**Vastus:** Strike’ide vahe miinus krediit, korda kordaja; seejärel arvesta kulud.

## Leht 12. Straddle ja strangle

[SELGITUS] Long straddle ostab sama strike’iga call’i ja put’i. Long strangle ostab eri strike’idega OTM call’i ja put’i. Mõlemad vajavad piisavat liikumist või soodsat vahepealset ümberhinnastumist.

[NÄIDE] Straddle K100,kulu 12: tasuvus 88 ja 112. Strangle put 95+call 105,kogukulu 6: tasuvus 89 ja 111. Võrdle kogu hinnavahemikku, mitte ainult makstud summat.

**Piirang:** Müüdud variandid on vastasmärgiga ja katmata call’i tõttu ülespoole piiramatu kahjuriskiga. „Kahepoolne” ei tähenda riskivaba.

**Kontrollküsimus:** Miks+9% liikumine võib straddle’ile kahju anda?

**Vastus:** K100 ja kulu 12 korral on lõppväärtus 9, seega P/L−3 ühikut.

## Leht 13. Butterfly ja condor

[SELGITUS] Butterfly koondab kasumi keskmise strike’i lähedale; condor annab laiemat platooala. Iron-variandid ühendavad call’e ja put’e. Tiivad piiravad terminalriski, kuid mitu jalga suurendab teostuse tähtsust.

[NÄIDE] Call butterfly 90/100/110, kogused+1/−2/+1, deebet 2: maksimaalne kasum 8 hinnal 100, maksimaalne kahju 2, tasuvused 92 ja 108. Iron condor 90/95/105/110 krediidiga 2: max kahju 3.

**Piirang:** P/L-tipp ei näita tõenäosust. Väike maksimumkasum võib spread’i ja komisjoni tõttu kaduda.

**Kontrollküsimus:** Kas graafiku roheline ala on võidutõenäosus?

**Vastus:** Ei. Selleks on vaja hinnajaotust, mitte ainult väljamaksefunktsiooni.

## Leht 14. Calendar ja diagonal

[SELGITUS] Calendar kasutab sama strike’i eri tähtaegadega. Diagonal muudab lisaks strike’i. Esimese tähtaja hetkel on pikk jalg veel elus: tema hind sisaldab aega ja sõltub IV-st.

[NÄIDE] Müü 30 päeva K100 call,osta 60 päeva K100 call.30. päeval arvuta pika jala 30 päeva mudeliväärtus, lahuta lühikese sisemine väärtus ja algdeebet. IV15% ja 30% annavad eri tulemused.

**Piirang:** Üks universaalne payoff-diagramm eksitaks. Vaata atlases eraldi IV-stsenaariume ning plaani, mida teha pärast esimese jala lõppu.

**Kontrollküsimus:** Miks kalendri tasuvuspiir võib muutuda?

**Vastus:** Sest allesjäänud pika optsiooni turuväärtus ja IV muutuvad.

## Leht 15. Sünteetika ja parity

[SELGITUS] Sama strike’i ja tähtajaga Euroopa call ja put on seotud: C−P=S exp(−qT)−K exp(−rT). Rahajala lisamine näitab, milline kombinatsioon jäljendab aktsiat.

[NÄIDE] r=q=0,K100,C=P6: call−put maksab 0 ja annab tähtajal S−100. S80 korral−20;S120 korral+20. Aktsia väärtuse S saamiseks lisa 100 raha.

**Piirang:** Null avamiskulu ei kõrvalda tagatist ega kahju. Sügav ITM call on aktsia ligikaudne tundlikkus, mitte täpne rahavoogude identiteet.

**Kontrollküsimus:** Miks sünteetiline long pole tasuta aktsia?

**Vastus:** Tulevase strike’iga seotud kohustus ja selle rahastamine jäävad alles.

## Leht 16. Oodatav väärtus

[SELGITUS] Võidumäär ja kasumlikkus on erinevad. Kahe tulemusega mudelis E=pW−(1−p)L−kulu. Tegelik optsioonitulemus võib moodustada pideva jaotuse; mudel peab näitama ka harvu suuri tulemusi.

[NÄIDE] p 0,9,W10,L120,kulu 2:9−12−2=−5 USD. Tasuvuseks vajalik võidumäär on(120+2)/(10+120)=93,85%.

**Piirang:** Null ootus ei tähenda 50% võite:90%×1−10%×9=0. Nullsummalisus ei võrdsusta eri strateegiate tegelikke ootusi.

**Kontrollküsimus:** Kas positiivse ootusega strateegial võib enamik tehinguid kaotada?

**Vastus:** Jah.90%−1 ja 10%+15 annavad E+0,6, kuigi mediaan on−1.

## Leht 17. Positsiooni suurus

[SELGITUS] Alusta rahalisest riskieelarvest ja ühe tervikpositsiooni maksimaalsest kahjust koos kuludega. Jaga ja ümarda alla. Kui vastus on null, ei sobi täisleping antud piirangusse. Margin ei ole maksimaalne kahju.

[NÄIDE] Konto 25000, õppestsenaariumi eelarve 2%=500. Üks spread risk 150+kulureserv 10=160. Lubatud kogusfloor(500/160)=3, kogurisk 480.

**Piirang:** Protsent pole universaalne soovitus. Korrelatsioon ja samaaegsed stresskahjud võivad üksiktehingute piirid üle kaaluda.

**Kontrollküsimus:** Miks ei tohiks kogust üles ümardada?

**Vastus:** Sest siis ületatakse juba enda valitud riskipiir enne turu muutumist.

## Leht 18. Täitmine, kulud ja 0DTE

[SELGITUS] Stop-loss ei garanteeri hinda. Lõpptähtaja lähedal jälgi, millised aktsiad ja rahavood võivad tekkida.0DTE tähendab samal päeval aegumist; ATM gamma võib olla suur. Väike preemia pole piisav riskimõõdik.

[NÄIDE] Bid 2,80,ask 3,20,M100: kohene ost-müük annab−40 enne komisjone. Neli jalga ning väljumine võivad väikese teoreetilise eelise ära kulutada.

**Piirang:** Maakleri lõikajad, arveldusviis ja kauplemise peatamine võivad mõjutada teostust. Kursus ei kinnita ühegi konto konkreetseid reegleid.

**Kontrollküsimus:** Kas piiratud spread’i risk välistab ajutise suure rahavajaduse?

**Vastus:** Ei. Ühe jala assignment võib nõuda aktsiaostu või tarnimist enne teise jala juhtimist.

## Leht 19. Õpi Pythoniga kontrollima

[SELGITUS] Alusta väikesest töötavast skriptist. Muuda üht sisendit, ennusta tulemus ja käivita. Thonny sobib terminalvalemiteks, Matplotlib graafikuteks ja Colab jagatavaks märkmikuks. Turuhinda pole aluste kontrolliks vaja.

[NÄIDE] P/L_call=(max(S−K,0)−c)×M. Võrdle arvutust S=0,K,K+c ja suure S korral. Seejärel võrdle short-positsiooni vastasmärki.

**Piirang:** BSM-i kõver enne tähtaega pole terminalpayoff. Edukas test näitab valemi kooskõla, mitte tulevast turukasumlikkust.

**Kontrollküsimus:** Mida peaks koodi test esimesena kontrollima?

**Vastus:** Lihtsaid teadaolevaid piire, ühikuid, vastasmärke ja rahavoogude identsusi.

## Leht 20. Oskan seletada ja otsustada

[SELGITUS] Hea seletus vastab viiele küsimusele: mida ostan, mida võlgnen, millal tulemus selgub, kui palju võin kaotada ja millised eeldused võivad murduda? Strateegia nimi on alles lühend selle analüüsi jaoks.

[NÄIDE] Selgita bull call spread’i: maksan 400, saan terminalis kuni 1000, seega teenin kuni 600 ja kaotan kuni 400. Tõus peab tähtajal ületama 104; ennetähtaegne hind sõltub ka ajast ja IV-st.

**Piirang:** Kui ei suuda selgitada ühe jala assignment’i või maksimaalset kahju, on vajalik täiendav õppimine. Keerukus ei asenda eelist.

**Kontrollküsimus:** Milline on kursuse lõppkontroll?

**Vastus:** Õpeta teisele üks strateegia, lase tal muuta lõpphinda ning kontrolli, kas ta arvutab ja põhjendab tulemuse iseseisvalt.

