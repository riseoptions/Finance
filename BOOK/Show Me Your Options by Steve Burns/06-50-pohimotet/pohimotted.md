# 50 optsioonikauplemise põhimõtet, reeglit ja väärarusaama

[Tagasi](../README.md)

[PÕHIMÕTE] Kõik sõnastused on selle õppematerjali koostaja omad. Matemaatiline tulemus kehtib deklareeritud eeldustel; rusikareegel ei ole garantii.

## 1. Väärtus pole kasum

**Liik:** matemaatiline tulemus.

**Selgitus:** Jah, kui sisemine väärtus ei kata preemiat. ITM võrdleb alusvara strike’iga, P/L võrdleb väljamakset ka ostuhinnaga.

**Praktiline näide:** K=100, c=7, S=104: 4−7=−3.

**Kehtivus ja täpsustus:** Kehtib tähtajal; enne seda tuleb arvestada ka välist väärtust.

**Vestluses kasutamine:** Küsi „Kas ITM call võib tähtajal kahjumit anda?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „ITM tähendab võitu.”.

## 2. Suund vajab aega

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Tõus võib olla liiga väike või liiga hiline. Leping lõpeb kindlal kuupäeval; hilisem hinnatõus ei taasta aegunud õigust.

**Praktiline näide:** K=105, c=3, lõpphind 107: kahju 1; järgmisel nädalal 120 ei muuda seda.

**Kehtivus ja täpsustus:** Kehtib lõpptähtajani hoidmisel; varem võib müügihind anda kasumi.

**Vestluses kasutamine:** Küsi „Miks õige tõusuprognoos ei pruugi call’i ostjat aidata?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Piisab pikaajaliselt õigest suunast.”.

## 3. Õigus ja kohustus erinevad

**Liik:** matemaatiline tulemus.

**Selgitus:** Ta on müünud teisele valikuõiguse. Kohustus püsib kuni sulgemise või lepingu lõppemiseni; assignment pole müüja uus vabatahtlik otsus.

**Praktiline näide:** Short put K=95 võib nõuda 9500 USD aktsiaostuks.

**Kehtivus ja täpsustus:** Kontrolli arveldusviisi ja konkreetset kohustust.

**Vestluses kasutamine:** Küsi „Miks ei saa optsiooni müüja lihtsalt täitmisest loobuda?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Müüja võib kahjuliku lepingu ignoreerida.”.

## 4. Put võib kaitsta

**Liik:** väärarusaam.

**Selgitus:** Ei, see võib piirata olemasoleva portfelli riski. Kindlustust võib osta ka siis, kui loodetakse vara väärtuse kasvule.

**Praktiline näide:** Aktsia 100 ja put K=95 hinnaga 3 annavad tähtaja kahjupiiriks 8 ühikut.

**Kehtivus ja täpsustus:** Järeldus sõltub kogu portfellist, mitte ühest tehingust.

**Vestluses kasutamine:** Küsi „Kas put’i ost tõestab aktsia langusootust?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Put’i ostja on alati karu.”.

## 5. Müük võib sulgeda

**Liik:** väärarusaam.

**Selgitus:** Ei, varem ostetud call’i sulgemine lõpetab positsiooni. Avav ja sulgev tehing on eri toimingud; risk sõltub lõpppositsioonist.

**Praktiline näide:** Ostad 3-ga, müüd sama lepingu 4-ga: kasum 100 M=100 korral.

**Kehtivus ja täpsustus:** Kui müüd rohkem kui omad, võib ülejääk avada lühikese positsiooni.

**Vestluses kasutamine:** Küsi „Kas call’i müües tekib alati piiramatu risk?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Iga müük on short-positsioon.”.

## 6. Kordaja muudab suurust

**Liik:** praktiline rusikareegel.

**Selgitus:** Preemiat näidatakse sageli ühe alusvaraühiku kohta. Lepingu kordaja ja lepingute arv teisendavad noteeringu rahavooks.

**Praktiline näide:** 2×100×3 lepingut=600 USD.

**Kehtivus ja täpsustus:** Korrigeeritud ja eri tooted vajavad spetsifikatsiooni.

**Vestluses kasutamine:** Küsi „Miks ekraanil olev 2 ei tähenda kahe dollari tehingut?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõik lepingud on alati 100 aktsiat.”.

## 7. Täitmine pole sulgemine

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Müües võib saada ka allesjäänud välise väärtuse. Täitmine realiseerib sisemise väärtuse, kuid võib loovutada ajaväärtuse.

**Praktiline näide:** Call maksab 6, sisemine 4: täitmisel võib 2 väärtust loovutada.

**Kehtivus ja täpsustus:** Halb likviidsus, dividendid ja intress võivad valikut muuta.

**Vestluses kasutamine:** Küsi „Miks võib optsiooni müük olla täitmisest parem?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kasumi saamiseks peab optsiooni täitma.”.

## 8. Euroopa ei tähenda lukustust

**Liik:** väärarusaam.

**Selgitus:** Sageli saab selle turul sulgeda. Euroopa piirang käib õiguse kasutamise, mitte üldise kauplemiskeelu kohta.

**Praktiline näide:** 30 päeva leping müüakse 10. päeval olemasoleva bid’i juures.

**Kehtivus ja täpsustus:** Turul peab olema sobiv vastaspool ja kauplemine avatud.

**Vestluses kasutamine:** Küsi „Kas Euroopa optsioonist saab enne tähtaega väljuda?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Euroopa lepingut peab lõpuni hoidma.”.

## 9. Väline väärtus pole ainult kell

**Liik:** väärarusaam.

**Selgitus:** Ei, seda võivad muuta ka IV ja alusvara hind. Väline väärtus on hinna ning sisemise väärtuse vahe, mitte iseseisev kellamehhanism.

**Praktiline näide:** Hind 6 ja sisemine 4 annavad 2; IV langusel võib jääda 1 samal päeval.

**Kehtivus ja täpsustus:** Erista muutuse allikad mudeli ja hetkeandmetega.

**Vestluses kasutamine:** Küsi „Kas ajaväärtuse kadu tõestab aja möödumise mõju?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kogu ajaväärtuse muutus on theta.”.

## 10. Hinnas on ootus

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Ainult siis, kui tasutud hind on tulemustega võrreldes põhjendatud. Oodatud liikumine võib olla juba preemiates; sündmuse õige ennustamine ei taga eelist.

**Praktiline näide:** Straddle maksab 12, lõpphind liigub 100-lt 109-le: −3.

**Kehtivus ja täpsustus:** Enne tähtaega sulgemisel loeb allesjäänud turuväärtus.

**Vestluses kasutamine:** Küsi „Kas oodatud suur uudis tähendab head straddle’i ostu?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Suure uudise eel tasub alati mõlemat suunda osta.”.

## 11. IV langus võib suuna üle kaaluda

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** IV langus ja ajakadu võivad delta mõju ületada. Mitu sisendit muutuvad korraga; delta üksinda ei kirjelda kogutulemust.

**Praktiline näide:** Delta mõju +1, vega mõju −1,2: neto −0,2 enne muid mõjusid.

**Kehtivus ja täpsustus:** See on lokaalne lähendus; suure muutuse korral hinnasta uuesti.

**Vestluses kasutamine:** Küsi „Kuidas saab tõusnud aktsia call odavneda?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Call peab iga aktsiatõusu korral kallinema.”.

## 12. Neli korda aega ei anna neli korda hinda

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** ATM-lähenduses kasvab võimaluse väärtus ligikaudu ruutjuurega ajast. Hinnajaotuse hajuvus kasvab tüüpilises difusioonimudelis ruutjuurega ajast.

**Praktiline näide:** 30 päeva hind 2,29; 120 päeva ligikaudu 4,57 samadel eeldustel.

**Kehtivus ja täpsustus:** Lähendus eeldab ATM-i, sama IV-d ja sobivaid intressi/dividendi eeldusi.

**Vestluses kasutamine:** Küsi „Miks pikema tähtaja hind ei kasva ajaga võrdeliselt?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kahekordne aeg kahekordistab alati preemia.”.

## 13. Delta on osatundlikkus

**Liik:** matemaatiline tulemus.

**Selgitus:** Ta mõõdab hinna tundlikkust ainult alusvara suhtes. Mõõtmise hetkel hoitakse teised sisendid paigal; need võivad päriselus ise muutuda.

**Praktiline näide:** Delta 0,5 ja S +2 annab +1, kuid IV mõju võib olla −2.

**Kehtivus ja täpsustus:** Kasuta väikese muutuse ja selgete ühikute korral.

**Vestluses kasutamine:** Küsi „Miks delta ei võta kokku kõiki kreeklasi?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Delta näitab kogu tulevast kasumit.”.

## 14. Gamma muudab deltat

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Delta muutub koos alusvara hinnaga. Gamma kirjeldab seda muutust lokaalselt; suurel sammul muutub ka gamma ise.

**Praktiline näide:** Δ=0,5, Γ=0,04, S +3: uus delta ligikaudu 0,62.

**Kehtivus ja täpsustus:** Suurte hüpete puhul vaja kogu mudelit või stressistsenaariumi.

**Vestluses kasutamine:** Küsi „Miks algne delta ei sobi suure hinnahüppe jaoks?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Delta on lepingu püsiv omadus.”.

## 15. Aeg pole garanteeritud tulu

**Liik:** väärarusaam.

**Selgitus:** Ei, see isoleerib ainult aja mõju. Negatiivne gamma või vega võib turu muutumisel theta-eelise kiiresti ületada.

**Praktiline näide:** Theta +5 USD päevas, hinnahüppe kahju 300 USD.

**Kehtivus ja täpsustus:** Kehtib muu sama tundlikkushinnanguna.

**Vestluses kasutamine:** Küsi „Kas positiivne theta tagab müüjale kasumi?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Müüjale makstakse riskivaba päevatulu.”.

## 16. Protsendipunkt pole protsent

**Liik:** praktiline rusikareegel.

**Selgitus:** Platvormi ühikule vastav muutus, sageli protsendipunktides. 20%-lt 25%-le on 5 pp, kuid suhteliselt 25%; need pole sama arv.

**Praktiline näide:** Vega 0,1 ühe pp kohta annab +0,5 ühikut.

**Kehtivus ja täpsustus:** Kui vega on antud ühe täisühiku sigma kohta, tuleb kasutada 0,05.

**Vestluses kasutamine:** Küsi „Milline IV muutus läheb vega valemisse?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Vega 0,1 tuleb korrutada 0,05-ga.”.

## 17. Rho puudutab tulevast raha

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Edasilükatud strike’i makse nüüdisväärtus väheneb. Euroopa mudelis on muude sisendite samaks jäämisel sellest call’i hoidjale kasu.

**Praktiline näide:** Rho 0,08 ja intress +1 pp annavad +0,08.

**Kehtivus ja täpsustus:** Put’i rho on standardmudelis negatiivne; turg muudab ka muid sisendeid.

**Vestluses kasutamine:** Küsi „Miks intressitõus võib call’i hinda kasvatada?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõik optsioonid kallinevad intressitõusul.”.

## 18. Null delta pole null risk

**Liik:** väärarusaam.

**Selgitus:** Gamma, vega, theta ja hüpped jäävad. Hetkeline suunatasakaal ei säili tingimata ning IV võib muuta mõlema jala väärtust.

**Praktiline näide:** Short straddle’i algdelta ligikaudu 0, kuid suur tõus tekitab suure kahju.

**Kehtivus ja täpsustus:** Neutraalsus vajab ajatemplit ja mõõdiku nimetust.

**Vestluses kasutamine:** Küsi „Miks delta-neutraalne positsioon võib palju kaotada?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Neutraalne tähendab riskivaba.”.

## 19. Delta pole kasumitõenäosus

**Liik:** väärarusaam.

**Selgitus:** Ei. ITM-tõenäosus ja preemiast üle saamise tõenäosus on eri sündmused; BSM-is pole isegi delta ja ITM-tõenäosus täpselt samad.

**Praktiline näide:** K=100, c=5: ITM nõuab S>100, tähtaja kasum S>105.

**Kehtivus ja täpsustus:** Mõnes praktikas kasutatakse deltat jämeda ITM-lähendina, mitte garantiina.

**Vestluses kasutamine:** Küsi „Kas delta 0,30 tähendab 30% võimalust kasumisse jääda?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Delta on täpne võiduprotsent.”.

## 20. Kreeklase märk pöördub müügil

**Liik:** matemaatiline tulemus.

**Selgitus:** See on long put’i negatiivse delta vastasmärk. Müüja saab kasu sellest, kui alusvara tõus vähendab tema kohustuse väärtust.

**Praktiline näide:** Long put Δ=−0,4; short put Δ=+0,4.

**Kehtivus ja täpsustus:** Arvesta positsiooni märki ja kogust.

**Vestluses kasutamine:** Küsi „Miks short put’i delta on positiivne?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Put tähendab alati negatiivset deltat.”.

## 21. Covered ei tähenda kaitstud hinda

**Liik:** väärarusaam.

**Selgitus:** Aktsiate olemasolu katab call’i tarnekohustuse, mitte aktsia langust. Preemia pakub ainult väikese puhvri; aktsia võib jätkuvalt kaotada suure osa väärtusest.

**Praktiline näide:** S₀=100, c=3, S=50: kogukahju 47 ühikut.

**Kehtivus ja täpsustus:** Kahjupiiri saab muuta eraldi ostetud put’iga.

**Vestluses kasutamine:** Küsi „Mille eest covered call tegelikult kaitseb?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Covered call on põhimõtteliselt riskivaba.”.

## 22. Rahatagatis ei kõrvalda langust

**Liik:** väärarusaam.

**Selgitus:** Ei, see tagab raha ostukohustuse täitmiseks. Raha reserveerimine ei muuda strike’iga ostmist odavamaks võrreldes tugevalt langenud turuhinnaga.

**Praktiline näide:** K=95, p=3, S=20: kahju 72 ühikut.

**Kehtivus ja täpsustus:** Arvutus eeldab aktsia hinda mitte alla nulli.

**Vestluses kasutamine:** Küsi „Kas cash-secured put välistab suure kahju?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Sularahaga tagatud tähendab kapitali garantiid.”.

## 23. Krediit pole kasum

**Liik:** matemaatiline tulemus.

**Selgitus:** Laekumise kõrval tekib lühikese optsiooni kohustus. Õiglase hinnaga avamisel on raha ja vastaskohustuse väärtus esialgu ligikaudu tasakaalus.

**Praktiline näide:** Saad 300 USD; tagasiost maksab kohe ligikaudu 300 või spread’i tõttu rohkem.

**Kehtivus ja täpsustus:** Raamatupidamise detailid sõltuvad kontost, majanduslik loogika püsib.

**Vestluses kasutamine:** Küsi „Miks preemia laekumine ei suurenda kohe netovara sama palju?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kontole laekunud raha on lõplik tootlus.”.

## 24. Spread’i risk sõltub laiusest

**Liik:** matemaatiline tulemus.

**Selgitus:** Strike’ide vahe miinus krediit, korda kordaja. Kaitsev jalg piirab terminalkohustust, kuid selle ja müüdud jala vahe jääb riskiks.

**Praktiline näide:** Laius 5, krediit 1,5: (5−1,5)×100=350.

**Kehtivus ja täpsustus:** Eeldab sobivat sama tähtaja vertikaali ja kooskõlalist arveldust.

**Vestluses kasutamine:** Küsi „Kuidas leida credit spread’i maksimaalne kahju?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Maksimaalne risk on saadud 150.”.

## 25. Deebet piirab ainult määratletud paketti

**Liik:** väärarusaam.

**Selgitus:** Ei, näiteks ratio spread võib maksta deebetit ja jääda katmata. Rahavoo märk ei määra väljamakse sabade kuju; loe lepingukoguseid.

**Praktiline näide:** 1 long call ja 2 short call’i jätavad ülespoole ühe katmata kohustuse.

**Kehtivus ja täpsustus:** Long-only või korrektse debit-vertikaali puhul võib deebet olla kahjupiir.

**Vestluses kasutamine:** Küsi „Kas iga deebetiga strateegia maksimaalne kahju on deebet?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Makstud netopreemia tähendab alati piiratud riski.”.

## 26. Straddle vajab piisavat liikumist

**Liik:** matemaatiline tulemus.

**Selgitus:** Ei, kuid liikumine peab ostuhinna suhtes piisama. Mõlemale poole ostetud õigus maksab; tähtajal ei anna väike kõrvalekalle kasumit.

**Praktiline näide:** K=100, kogukulu 12: tasuvus 88 ja 112.

**Kehtivus ja täpsustus:** Enne tähtaega võib IV tõus anda kasumi ka liikumiseta.

**Vestluses kasutamine:** Küsi „Kas straddle’i ostja peab suunda ennustama?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Üks jalg võidab alati piisavalt.”.

## 27. Odavam strangle nõuab enamat

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Strike’ide vahe lisab hinnaliikumise nõuet. OTM-õigused on odavamad osalt seetõttu, et nende kasutamiseks tuleb kaugemale liikuda.

**Praktiline näide:** Put 95 ja call 105, kogukulu 6: piirid 89 ja 111.

**Kehtivus ja täpsustus:** Võrdle kogu P/L-i ja põhjendatud jaotust, mitte ainult hinda.

**Vestluses kasutamine:** Küsi „Miks väiksem preemia ei tee strangle’it automaatselt paremaks?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Odavam kombinatsioon on alati soodsam.”.

## 28. Butterfly tipp pole tõenäosus

**Liik:** väärarusaam.

**Selgitus:** See saavutatakse kitsas lõpphinna piirkonnas. P/L-graafik näitab võimalikke summasid, mitte tõenäosust iga hinnani jõuda.

**Praktiline näide:** 90/100/110 butterfly kulu 2: tippkasum 8 täpselt S=100 juures.

**Kehtivus ja täpsustus:** Mõõda ka kulusid, vahemikku ja tõenäosusmudeli usaldusväärsust.

**Vestluses kasutamine:** Küsi „Miks butterfly suur maksimumkasum võib eksitada?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõrge tipp tähendab suurt oodatavat tootlust.”.

## 29. Condor ei ela väljaspool turgu

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Ei, tegelik hind võib vahemikust väljuda. Müüakse osa sabariski; ostetud tiivad piiravad kahju, kuid korduvad kaotused võivad konto kulutada.

**Praktiline näide:** Laius 5, krediit 2: võit 200, kahju 300.

**Kehtivus ja täpsustus:** Võidutõenäosus sõltub tähtajast, strike’idest ja jaotusest.

**Vestluses kasutamine:** Küsi „Kas külgsuunaline ootus teeb iron condor’i ohutuks?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Rahulik eilne turg tagab rahuliku homse.”.

## 30. Nullkuluga kaitsel on hind

**Liik:** matemaatiline tulemus.

**Selgitus:** Loovutatud tõusupotentsiaaliga. Call’i müük rahastab put’i, kuid annab teisele õiguse saada sinu aktsia kindla hinnaga.

**Praktiline näide:** Put 95 ja call 105 mõlemad 3: null preemiat, kasum üle 105 piiratud.

**Kehtivus ja täpsustus:** Kulud võivad muuta netopreemia nullist erinevaks.

**Vestluses kasutamine:** Küsi „Mille eest maksad zero-cost collar’is?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Tasuta kindlustus ilma kompromissita.”.

## 31. Sünteetika vajab raha

**Liik:** matemaatiline tulemus.

**Selgitus:** Tema terminalväljamakse on S−K, mitte S. Puudu on strike’i tasumiseks vajalik rahajalg; risk jääb ka null netopreemia puhul.

**Praktiline näide:** S=0, K=100: sünteetika annab −100 ühikut.

**Kehtivus ja täpsustus:** Intressi ja dividendiga tuleb kasutada täpset parity’t.

**Vestluses kasutamine:** Küsi „Miks long call − put pole tasuta aktsia?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Null avamiskulu tähendab null riski.”.

## 32. Sama kuju vajab samu tingimusi

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Sama strike’i, tähtaja ja korrektse rahastuse korral. Put-call parity seob terminalrahavood; erinevad strike’id või dividendieelne täitmine rikuvad lihtsa võrdluse.

**Praktiline näide:** S=K=100, c=p=6: mõlema netokulu 94 ja terminalväärtus min(S,100).

**Kehtivus ja täpsustus:** Kontrolli ka kulusid, dividende ja exercise-stiili.

**Vestluses kasutamine:** Küsi „Millal covered call ja cash-secured put on võrreldavad?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõik covered call’id on kõikide short put’idega samad.”.

## 33. Kaks tähtaega pole üks payoff

**Liik:** väärarusaam.

**Selgitus:** Pikk jalg on lühikese lõppedes endiselt turuhinnaga optsioon. Allesjäänud hind sõltub IV-st, ajast ja intressist, mitte ainult sisemisest väärtusest.

**Praktiline näide:** 30/60 päeva calendar’i pika jala väärtus 30. päeval muutub IV 15% ja 30% vahel.

**Kehtivus ja täpsustus:** Kui mõlemad lõpuks lõppevad, peab kirjeldama ka vahepealseid rahavooge.

**Vestluses kasutamine:** Küsi „Miks calendar spread’i tasuvuspiir pole universaalne?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõik jalad võib esimesel tähtajal sisemiseks väärtuseks asendada.”.

## 34. Lisamüük võib avada piiramatu saba

**Liik:** matemaatiline tulemus.

**Selgitus:** Suurte hindade juures jääb üks neto short call. Üks long call katab ainult ühe short call’i; teine jääb hinnatõusuga kasvavaks kohustuseks.

**Praktiline näide:** K100 long, 2×K110 short: suure S korral payoff 120−S.

**Kehtivus ja täpsustus:** Lisatud kaitsev call muudaks sabariski, kuid maksab.

**Vestluses kasutamine:** Küsi „Miks 1×2 call ratio spread võib ohtlik olla?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kaks müüdud jalga on lihtsalt parem rahastus.”.

## 35. Wheel ei kustuta ostuhinda

**Liik:** väärarusaam.

**Selgitus:** Ei, kogu aktsia- ja optsioonitulemus tuleb kokku liita. Uute call’ide müük võib tuua raha, kuid vähendab taastumise tõusupotentsiaali.

**Praktiline näide:** Ost 95, put’i krediit 3, call’i krediit 2, lõpphind 70: −20 ühikut.

**Kehtivus ja täpsustus:** Tulemuseks on teekonnast sõltuv protsess, mitte püsiv tootlusmäär.

**Vestluses kasutamine:** Küsi „Kas wheel teeb aktsia kahjumist preemiatulu?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Uus preemia tähendab vana kahju kadumist.”.

## 36. Võidumäär ei ole eelis

**Liik:** matemaatiline tulemus.

**Selgitus:** Harvad kahjud võivad olla keskmistest võitudest suuremad. Tähtis on tõenäosusega kaalutud summa, mitte plussmärkide arv.

**Praktiline näide:** 0,9×10−0,1×120=−3.

**Kehtivus ja täpsustus:** Kahe tulemuse mudel on lihtsustus; päriselt vaata kogu jaotust.

**Vestluses kasutamine:** Küsi „Kuidas võib 90% võitude korral raha kaotada?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Rohkem võite kui kaotusi tähendab kasumlikkust.”.

## 37. Kulud võivad eelise ära süüa

**Liik:** matemaatiline tulemus.

**Selgitus:** Spread, komisjon ja täitmisnihe vähendavad tulemust. Väikese tehingueelise korral võib teostus moodustada suure osa oodatavast tulust.

**Praktiline näide:** Bruto E=4 USD, kulud 6 USD: neto −2.

**Kehtivus ja täpsustus:** Kulud sõltuvad kogusest, turuolust ja korraldusest.

**Vestluses kasutamine:** Küsi „Miks positiivne brutotulemus ei taga netokasumit?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Hea backtest on automaatselt kaubeldav.”.

## 38. Tagatis pole kahjupiir

**Liik:** väärarusaam.

**Selgitus:** Ei. Tagatisnõue on krediidiriski juhtimise mehhanism; kohustus võib olla palju suurem ja tagatist juurde nõuda.

**Praktiline näide:** Katmata call võib hüppel kaotada 5000, kuigi algmargin oli 2000.

**Kehtivus ja täpsustus:** Täpne margin sõltub tootest ja maaklerist.

**Vestluses kasutamine:** Küsi „Kas 2000 USD margin tähendab kuni 2000 USD kahju?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Maakler piirab alati kahju sissemaksega.”.

## 39. Stop pole kindel hind

**Liik:** praktiline rusikareegel.

**Selgitus:** Hind võib stopist üle hüpata ja likviidsus kaduda. Stop aktiveerib korralduse, kuid täitmine toimub olemasoleva turu tingimustel.

**Praktiline näide:** Stop 95, järgmine saadav hind 80: müük võib olla 80 lähedal.

**Kehtivus ja täpsustus:** Stop-limit võib vältida halba hinda, kuid jääda üldse täitmata.

**Vestluses kasutamine:** Küsi „Miks stop-loss ei taga maksimaalset kahjumit?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Stop on sama mis ostetud put.”.

## 40. Null lepingut on korrektne vastus

**Liik:** praktiline rusikareegel.

**Selgitus:** Selles raamistikus tehingut mitte avada. Täisarvuline kogus ei allu soovmõtlemisele; väiksem risk vajab teist instrumenti või struktuuri.

**Praktiline näide:** Eelarve 100, lepingu risk 350: floor(100/350)=0.

**Kehtivus ja täpsustus:** Riskieelarve ise tuleb põhjendada, mitte võtta universaalse protsendina.

**Vestluses kasutamine:** Küsi „Mida teha, kui üks leping ületab riskieelarve?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Üks leping on alati piisavalt väike.”.

## 41. Riskid võivad kokku kuhjuda

**Liik:** praktiline rusikareegel.

**Selgitus:** Alusvarad võivad kriisis ühiselt langeda. Erinevad nimed ei võrdu sõltumatud tegurid; sektor ja turubeta ühendavad positsioone.

**Praktiline näide:** Kümme tehnoloogiaaktsiat langevad sama uudise järel.

**Kehtivus ja täpsustus:** Hajutamist hinnatakse korrelatsiooni ja stressiga.

**Vestluses kasutamine:** Küsi „Miks kümme short put’i pole tingimata hajutatud?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Rohkem tehinguid tähendab automaatselt väiksemat riski.”.

## 42. Taastumine on asümmeetriline

**Liik:** matemaatiline tulemus.

**Selgitus:** Kasv arvutatakse väiksemalt baasilt. Kapitali vähenemine muudab taastumisprotsendi suuremaks kui algne langusprotsent.

**Praktiline näide:** 100→80; 80×1,25=100.

**Kehtivus ja täpsustus:** Liitkasvu arvestus kehtib igal järjestikusel tootlusel.

**Vestluses kasutamine:** Küsi „Miks 20% kaotus vajab 25% tõusu?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „−20% ja +20% tasanduvad.”.

## 43. Roll on kaks tehingut

**Liik:** väärarusaam.

**Selgitus:** Ei, vana positsioon suletakse ja uus risk avatakse. Uue lepingu rahavoog võib peita realiseeritud kahju, kui vaadata ainult viimast kontolaekumist.

**Praktiline näide:** Vana sulgemine −500, uus krediit +600 jätab uue kohustuse alles.

**Kehtivus ja täpsustus:** Võrdle mõlemat tehingut ja kõiki allesjäänud kohustusi.

**Vestluses kasutamine:** Küsi „Kas rollimise krediit tähendab positsiooni päästmist?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „100 netolaekumist tähendab kogu tehingu kasumit.”.

## 44. Täitmine võib jalad lahutada

**Liik:** praktiline rusikareegel.

**Selgitus:** Üks jalg võib täituda enne teist. Terminalne kompensatsioon ei pruugi automaatselt tekkida samal hetkel; aktsiad ja raha tuleb hallata.

**Praktiline näide:** Short put K100 assignment tähendab 10000 USD ostu, long K95 jääb esialgu alles.

**Kehtivus ja täpsustus:** Maakleri netting ja menetlused erinevad; kontrolli konkreetset protsessi.

**Vestluses kasutamine:** Küsi „Miks piiratud riskiga spread võib vajada lisaraha?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kaitsev jalg lahendab kõik automaatselt.”.

## 45. Dividend muudab otsust

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Ostjal võib olla kasulik õigust varakult kasutada. Dividendi saamise kasu tuleb võrrelda loovutatava välise väärtuse ja rahastuskuluga.

**Praktiline näide:** Väline väärtus 0,1, dividend 1 võib muuta täitmise atraktiivseks.

**Kehtivus ja täpsustus:** See puudutab Ameerika tüüpi call’i; dividend üksi pole piisav täpne reegel.

**Vestluses kasutamine:** Küsi „Miks short call’i risk suureneb mõnikord dividendi eel?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Assignment toimub ainult tähtajal.”.

## 46. Lõpphind pole alati arveldushind

**Liik:** praktiline rusikareegel.

**Selgitus:** Lepingu ametlik arveldusväärtus arvutatakse kindla reegli järgi. AM/PM aeg, komponentide hinnad ja kauplemise lõpp võivad erineda tavalisest viimase tehingu hinnast.

**Praktiline näide:** Eeldatud 100 asemel arveldus 101 muudab K100 call’i väärtuse 0-lt 1-le.

**Kehtivus ja täpsustus:** Kontrolli alati toote spetsifikatsiooni.

**Vestluses kasutamine:** Küsi „Miks ekraanil nähtud indeksihind võib erineda arveldusest?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõik optsioonid arvelduvad viimase ekraanihinnaga.”.

## 47. 0DTE koondab otsused

**Liik:** tingimuslik seaduspärasus.

**Selgitus:** Ei, täielik kaotus võib saabuda väga kiiresti. Lühike aeg ja ATM gamma muudavad hinna tundlikuks; protsentuaalne risk võib olla suur.

**Praktiline näide:** 0,5 preemia M100 tähendab 50, mis võib samal päeval täielikult kaduda.

**Kehtivus ja täpsustus:** Rahaline kahju sõltub ka lepingute arvust ja müüdud kohustustest.

**Vestluses kasutamine:** Küsi „Kas odav 0DTE on tingimata väiksema riskiga?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Odav hind tähendab aeglast või väikest riski.”.

## 48. Mudel pole hinnapakkumine

**Liik:** praktiline rusikareegel.

**Selgitus:** Mudel lihtsustab turgu ning ei sisalda sinu täitmiskulu. Püsiv IV, pidev kauplemine ja hüpete puudumine ei kirjelda kogu tegelikkust.

**Praktiline näide:** Mudel 3,00, bid/ask 2,70/3,30: ost 3,00 pole garanteeritud.

**Kehtivus ja täpsustus:** Kasuta mudelit võrdluse ja tundlikkuste, mitte kindla täitmisena.

**Vestluses kasutamine:** Küsi „Miks BSM-i hind ei pruugi olla turul teostatav?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Mudeli väljund on õige hind, turg eksib.”.

## 49. Nullsumma ei võrdsusta strateegiaid

**Liik:** väärarusaam.

**Selgitus:** See seob sama lepingu vastaspooled, mitte erinevate riskide jaotusi. Tegeliku maailma riskipreemiad, hinnad ja kulud võivad eri strateegiate ootusi muuta.

**Praktiline näide:** Sama call’i ostja +200 tähendab müüjale −200 enne kulusid; see ei määra teise put’i oodatavat tulemust.

**Kehtivus ja täpsustus:** Riskineutraalne hinnastus erineb tegelikust tootlusprognoosist.

**Vestluses kasutamine:** Küsi „Miks nullsummaline leping ei tõesta kõigi strateegiate võrdset eelist?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kõigi strateegiate pikaajaline kasum on sama.”.

## 50. Hea lugu vajab testi

**Liik:** praktiline rusikareegel.

**Selgitus:** Optsioon lisab strike’i, tähtaja ja IV valiku. Aktsiasignaali eelis ei pruugi katta preemiat ja kulusid; valikuid on rohkem ning üleoptimeerimise oht kasvab.

**Praktiline näide:** Aktsiasignaal +2%, aga OTM call vajab tasuvuseks +8%.

**Kehtivus ja täpsustus:** Testi väljaspool treeningperioodi, realistlike hinnavahedega.

**Vestluses kasutamine:** Küsi „Miks trendisüsteemi ei saa automaatselt optsioonidele üle kanda?” ning palu vastajal põhjendada, millist rahavoogu või riski ta arvestas. Eksitav vastus oleks „Kasumlik aktsiameetod garanteerib kasumlikud call’id.”.

