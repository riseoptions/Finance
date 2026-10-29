# 60 optsiooniküsimust vastuste ja selgitustega

[Tagasi](../README.md)

Kõik küsimused, sõnastused ja näited on [SELGITUS]/[NÄIDE], mitte raamatu tsitaadid. Eesmärk on mehhanismi seletamine. Summad on ühiku kohta, kui pole märgitud teisiti.

## 1. Kas ITM call võib tähtajal kahjumit anda?

**Lühivastus:** Jah, kui sisemine väärtus ei kata preemiat.

**Selgitus:** ITM võrdleb alusvara strike’iga, P/L võrdleb väljamakset ka ostuhinnaga.

**Näide/arvutus:** K=100, c=7, S=104: 4−7=−3.

**Levinud väärarusaam:** „ITM tähendab võitu.”

**Järeldus:** Väärtus pole kasum. Kehtib tähtajal; enne seda tuleb arvestada ka välist väärtust.

## 2. Miks õige tõusuprognoos ei pruugi call’i ostjat aidata?

**Lühivastus:** Tõus võib olla liiga väike või liiga hiline.

**Selgitus:** Leping lõpeb kindlal kuupäeval; hilisem hinnatõus ei taasta aegunud õigust.

**Näide/arvutus:** K=105, c=3, lõpphind 107: kahju 1; järgmisel nädalal 120 ei muuda seda.

**Levinud väärarusaam:** „Piisab pikaajaliselt õigest suunast.”

**Järeldus:** Suund vajab aega. Kehtib lõpptähtajani hoidmisel; varem võib müügihind anda kasumi.

## 3. Miks ei saa optsiooni müüja lihtsalt täitmisest loobuda?

**Lühivastus:** Ta on müünud teisele valikuõiguse.

**Selgitus:** Kohustus püsib kuni sulgemise või lepingu lõppemiseni; assignment pole müüja uus vabatahtlik otsus.

**Näide/arvutus:** Short put K=95 võib nõuda 9500 USD aktsiaostuks.

**Levinud väärarusaam:** „Müüja võib kahjuliku lepingu ignoreerida.”

**Järeldus:** Õigus ja kohustus erinevad. Kontrolli arveldusviisi ja konkreetset kohustust.

## 4. Kas put’i ost tõestab aktsia langusootust?

**Lühivastus:** Ei, see võib piirata olemasoleva portfelli riski.

**Selgitus:** Kindlustust võib osta ka siis, kui loodetakse vara väärtuse kasvule.

**Näide/arvutus:** Aktsia 100 ja put K=95 hinnaga 3 annavad tähtaja kahjupiiriks 8 ühikut.

**Levinud väärarusaam:** „Put’i ostja on alati karu.”

**Järeldus:** Put võib kaitsta. Järeldus sõltub kogu portfellist, mitte ühest tehingust.

## 5. Kas call’i müües tekib alati piiramatu risk?

**Lühivastus:** Ei, varem ostetud call’i sulgemine lõpetab positsiooni.

**Selgitus:** Avav ja sulgev tehing on eri toimingud; risk sõltub lõpppositsioonist.

**Näide/arvutus:** Ostad 3-ga, müüd sama lepingu 4-ga: kasum 100 M=100 korral.

**Levinud väärarusaam:** „Iga müük on short-positsioon.”

**Järeldus:** Müük võib sulgeda. Kui müüd rohkem kui omad, võib ülejääk avada lühikese positsiooni.

## 6. Miks ekraanil olev 2 ei tähenda kahe dollari tehingut?

**Lühivastus:** Preemiat näidatakse sageli ühe alusvaraühiku kohta.

**Selgitus:** Lepingu kordaja ja lepingute arv teisendavad noteeringu rahavooks.

**Näide/arvutus:** 2×100×3 lepingut=600 USD.

**Levinud väärarusaam:** „Kõik lepingud on alati 100 aktsiat.”

**Järeldus:** Kordaja muudab suurust. Korrigeeritud ja eri tooted vajavad spetsifikatsiooni.

## 7. Miks võib optsiooni müük olla täitmisest parem?

**Lühivastus:** Müües võib saada ka allesjäänud välise väärtuse.

**Selgitus:** Täitmine realiseerib sisemise väärtuse, kuid võib loovutada ajaväärtuse.

**Näide/arvutus:** Call maksab 6, sisemine 4: täitmisel võib 2 väärtust loovutada.

**Levinud väärarusaam:** „Kasumi saamiseks peab optsiooni täitma.”

**Järeldus:** Täitmine pole sulgemine. Halb likviidsus, dividendid ja intress võivad valikut muuta.

## 8. Kas Euroopa optsioonist saab enne tähtaega väljuda?

**Lühivastus:** Sageli saab selle turul sulgeda.

**Selgitus:** Euroopa piirang käib õiguse kasutamise, mitte üldise kauplemiskeelu kohta.

**Näide/arvutus:** 30 päeva leping müüakse 10. päeval olemasoleva bid’i juures.

**Levinud väärarusaam:** „Euroopa lepingut peab lõpuni hoidma.”

**Järeldus:** Euroopa ei tähenda lukustust. Turul peab olema sobiv vastaspool ja kauplemine avatud.

## 9. Kas ajaväärtuse kadu tõestab aja möödumise mõju?

**Lühivastus:** Ei, seda võivad muuta ka IV ja alusvara hind.

**Selgitus:** Väline väärtus on hinna ning sisemise väärtuse vahe, mitte iseseisev kellamehhanism.

**Näide/arvutus:** Hind 6 ja sisemine 4 annavad 2; IV langusel võib jääda 1 samal päeval.

**Levinud väärarusaam:** „Kogu ajaväärtuse muutus on theta.”

**Järeldus:** Väline väärtus pole ainult kell. Erista muutuse allikad mudeli ja hetkeandmetega.

## 10. Kas oodatud suur uudis tähendab head straddle’i ostu?

**Lühivastus:** Ainult siis, kui tasutud hind on tulemustega võrreldes põhjendatud.

**Selgitus:** Oodatud liikumine võib olla juba preemiates; sündmuse õige ennustamine ei taga eelist.

**Näide/arvutus:** Straddle maksab 12, lõpphind liigub 100-lt 109-le: −3.

**Levinud väärarusaam:** „Suure uudise eel tasub alati mõlemat suunda osta.”

**Järeldus:** Hinnas on ootus. Enne tähtaega sulgemisel loeb allesjäänud turuväärtus.

## 11. Kuidas saab tõusnud aktsia call odavneda?

**Lühivastus:** IV langus ja ajakadu võivad delta mõju ületada.

**Selgitus:** Mitu sisendit muutuvad korraga; delta üksinda ei kirjelda kogutulemust.

**Näide/arvutus:** Delta mõju +1, vega mõju −1,2: neto −0,2 enne muid mõjusid.

**Levinud väärarusaam:** „Call peab iga aktsiatõusu korral kallinema.”

**Järeldus:** IV langus võib suuna üle kaaluda. See on lokaalne lähendus; suure muutuse korral hinnasta uuesti.

## 12. Miks pikema tähtaja hind ei kasva ajaga võrdeliselt?

**Lühivastus:** ATM-lähenduses kasvab võimaluse väärtus ligikaudu ruutjuurega ajast.

**Selgitus:** Hinnajaotuse hajuvus kasvab tüüpilises difusioonimudelis ruutjuurega ajast.

**Näide/arvutus:** 30 päeva hind 2,29; 120 päeva ligikaudu 4,57 samadel eeldustel.

**Levinud väärarusaam:** „Kahekordne aeg kahekordistab alati preemia.”

**Järeldus:** Neli korda aega ei anna neli korda hinda. Lähendus eeldab ATM-i, sama IV-d ja sobivaid intressi/dividendi eeldusi.

## 13. Miks delta ei võta kokku kõiki kreeklasi?

**Lühivastus:** Ta mõõdab hinna tundlikkust ainult alusvara suhtes.

**Selgitus:** Mõõtmise hetkel hoitakse teised sisendid paigal; need võivad päriselus ise muutuda.

**Näide/arvutus:** Delta 0,5 ja S +2 annab +1, kuid IV mõju võib olla −2.

**Levinud väärarusaam:** „Delta näitab kogu tulevast kasumit.”

**Järeldus:** Delta on osatundlikkus. Kasuta väikese muutuse ja selgete ühikute korral.

## 14. Miks algne delta ei sobi suure hinnahüppe jaoks?

**Lühivastus:** Delta muutub koos alusvara hinnaga.

**Selgitus:** Gamma kirjeldab seda muutust lokaalselt; suurel sammul muutub ka gamma ise.

**Näide/arvutus:** Δ=0,5, Γ=0,04, S +3: uus delta ligikaudu 0,62.

**Levinud väärarusaam:** „Delta on lepingu püsiv omadus.”

**Järeldus:** Gamma muudab deltat. Suurte hüpete puhul vaja kogu mudelit või stressistsenaariumi.

## 15. Kas positiivne theta tagab müüjale kasumi?

**Lühivastus:** Ei, see isoleerib ainult aja mõju.

**Selgitus:** Negatiivne gamma või vega võib turu muutumisel theta-eelise kiiresti ületada.

**Näide/arvutus:** Theta +5 USD päevas, hinnahüppe kahju 300 USD.

**Levinud väärarusaam:** „Müüjale makstakse riskivaba päevatulu.”

**Järeldus:** Aeg pole garanteeritud tulu. Kehtib muu sama tundlikkushinnanguna.

## 16. Milline IV muutus läheb vega valemisse?

**Lühivastus:** Platvormi ühikule vastav muutus, sageli protsendipunktides.

**Selgitus:** 20%-lt 25%-le on 5 pp, kuid suhteliselt 25%; need pole sama arv.

**Näide/arvutus:** Vega 0,1 ühe pp kohta annab +0,5 ühikut.

**Levinud väärarusaam:** „Vega 0,1 tuleb korrutada 0,05-ga.”

**Järeldus:** Protsendipunkt pole protsent. Kui vega on antud ühe täisühiku sigma kohta, tuleb kasutada 0,05.

## 17. Miks intressitõus võib call’i hinda kasvatada?

**Lühivastus:** Edasilükatud strike’i makse nüüdisväärtus väheneb.

**Selgitus:** Euroopa mudelis on muude sisendite samaks jäämisel sellest call’i hoidjale kasu.

**Näide/arvutus:** Rho 0,08 ja intress +1 pp annavad +0,08.

**Levinud väärarusaam:** „Kõik optsioonid kallinevad intressitõusul.”

**Järeldus:** Rho puudutab tulevast raha. Put’i rho on standardmudelis negatiivne; turg muudab ka muid sisendeid.

## 18. Miks delta-neutraalne positsioon võib palju kaotada?

**Lühivastus:** Gamma, vega, theta ja hüpped jäävad.

**Selgitus:** Hetkeline suunatasakaal ei säili tingimata ning IV võib muuta mõlema jala väärtust.

**Näide/arvutus:** Short straddle’i algdelta ligikaudu 0, kuid suur tõus tekitab suure kahju.

**Levinud väärarusaam:** „Neutraalne tähendab riskivaba.”

**Järeldus:** Null delta pole null risk. Neutraalsus vajab ajatemplit ja mõõdiku nimetust.

## 19. Kas delta 0,30 tähendab 30% võimalust kasumisse jääda?

**Lühivastus:** Ei.

**Selgitus:** ITM-tõenäosus ja preemiast üle saamise tõenäosus on eri sündmused; BSM-is pole isegi delta ja ITM-tõenäosus täpselt samad.

**Näide/arvutus:** K=100, c=5: ITM nõuab S>100, tähtaja kasum S>105.

**Levinud väärarusaam:** „Delta on täpne võiduprotsent.”

**Järeldus:** Delta pole kasumitõenäosus. Mõnes praktikas kasutatakse deltat jämeda ITM-lähendina, mitte garantiina.

## 20. Miks short put’i delta on positiivne?

**Lühivastus:** See on long put’i negatiivse delta vastasmärk.

**Selgitus:** Müüja saab kasu sellest, kui alusvara tõus vähendab tema kohustuse väärtust.

**Näide/arvutus:** Long put Δ=−0,4; short put Δ=+0,4.

**Levinud väärarusaam:** „Put tähendab alati negatiivset deltat.”

**Järeldus:** Kreeklase märk pöördub müügil. Arvesta positsiooni märki ja kogust.

## 21. Mille eest covered call tegelikult kaitseb?

**Lühivastus:** Aktsiate olemasolu katab call’i tarnekohustuse, mitte aktsia langust.

**Selgitus:** Preemia pakub ainult väikese puhvri; aktsia võib jätkuvalt kaotada suure osa väärtusest.

**Näide/arvutus:** S₀=100, c=3, S=50: kogukahju 47 ühikut.

**Levinud väärarusaam:** „Covered call on põhimõtteliselt riskivaba.”

**Järeldus:** Covered ei tähenda kaitstud hinda. Kahjupiiri saab muuta eraldi ostetud put’iga.

## 22. Kas cash-secured put välistab suure kahju?

**Lühivastus:** Ei, see tagab raha ostukohustuse täitmiseks.

**Selgitus:** Raha reserveerimine ei muuda strike’iga ostmist odavamaks võrreldes tugevalt langenud turuhinnaga.

**Näide/arvutus:** K=95, p=3, S=20: kahju 72 ühikut.

**Levinud väärarusaam:** „Sularahaga tagatud tähendab kapitali garantiid.”

**Järeldus:** Rahatagatis ei kõrvalda langust. Arvutus eeldab aktsia hinda mitte alla nulli.

## 23. Miks preemia laekumine ei suurenda kohe netovara sama palju?

**Lühivastus:** Laekumise kõrval tekib lühikese optsiooni kohustus.

**Selgitus:** Õiglase hinnaga avamisel on raha ja vastaskohustuse väärtus esialgu ligikaudu tasakaalus.

**Näide/arvutus:** Saad 300 USD; tagasiost maksab kohe ligikaudu 300 või spread’i tõttu rohkem.

**Levinud väärarusaam:** „Kontole laekunud raha on lõplik tootlus.”

**Järeldus:** Krediit pole kasum. Raamatupidamise detailid sõltuvad kontost, majanduslik loogika püsib.

## 24. Kuidas leida credit spread’i maksimaalne kahju?

**Lühivastus:** Strike’ide vahe miinus krediit, korda kordaja.

**Selgitus:** Kaitsev jalg piirab terminalkohustust, kuid selle ja müüdud jala vahe jääb riskiks.

**Näide/arvutus:** Laius 5, krediit 1,5: (5−1,5)×100=350.

**Levinud väärarusaam:** „Maksimaalne risk on saadud 150.”

**Järeldus:** Spread’i risk sõltub laiusest. Eeldab sobivat sama tähtaja vertikaali ja kooskõlalist arveldust.

## 25. Kas iga deebetiga strateegia maksimaalne kahju on deebet?

**Lühivastus:** Ei, näiteks ratio spread võib maksta deebetit ja jääda katmata.

**Selgitus:** Rahavoo märk ei määra väljamakse sabade kuju; loe lepingukoguseid.

**Näide/arvutus:** 1 long call ja 2 short call’i jätavad ülespoole ühe katmata kohustuse.

**Levinud väärarusaam:** „Makstud netopreemia tähendab alati piiratud riski.”

**Järeldus:** Deebet piirab ainult määratletud paketti. Long-only või korrektse debit-vertikaali puhul võib deebet olla kahjupiir.

## 26. Kas straddle’i ostja peab suunda ennustama?

**Lühivastus:** Ei, kuid liikumine peab ostuhinna suhtes piisama.

**Selgitus:** Mõlemale poole ostetud õigus maksab; tähtajal ei anna väike kõrvalekalle kasumit.

**Näide/arvutus:** K=100, kogukulu 12: tasuvus 88 ja 112.

**Levinud väärarusaam:** „Üks jalg võidab alati piisavalt.”

**Järeldus:** Straddle vajab piisavat liikumist. Enne tähtaega võib IV tõus anda kasumi ka liikumiseta.

## 27. Miks väiksem preemia ei tee strangle’it automaatselt paremaks?

**Lühivastus:** Strike’ide vahe lisab hinnaliikumise nõuet.

**Selgitus:** OTM-õigused on odavamad osalt seetõttu, et nende kasutamiseks tuleb kaugemale liikuda.

**Näide/arvutus:** Put 95 ja call 105, kogukulu 6: piirid 89 ja 111.

**Levinud väärarusaam:** „Odavam kombinatsioon on alati soodsam.”

**Järeldus:** Odavam strangle nõuab enamat. Võrdle kogu P/L-i ja põhjendatud jaotust, mitte ainult hinda.

## 28. Miks butterfly suur maksimumkasum võib eksitada?

**Lühivastus:** See saavutatakse kitsas lõpphinna piirkonnas.

**Selgitus:** P/L-graafik näitab võimalikke summasid, mitte tõenäosust iga hinnani jõuda.

**Näide/arvutus:** 90/100/110 butterfly kulu 2: tippkasum 8 täpselt S=100 juures.

**Levinud väärarusaam:** „Kõrge tipp tähendab suurt oodatavat tootlust.”

**Järeldus:** Butterfly tipp pole tõenäosus. Mõõda ka kulusid, vahemikku ja tõenäosusmudeli usaldusväärsust.

## 29. Kas külgsuunaline ootus teeb iron condor’i ohutuks?

**Lühivastus:** Ei, tegelik hind võib vahemikust väljuda.

**Selgitus:** Müüakse osa sabariski; ostetud tiivad piiravad kahju, kuid korduvad kaotused võivad konto kulutada.

**Näide/arvutus:** Laius 5, krediit 2: võit 200, kahju 300.

**Levinud väärarusaam:** „Rahulik eilne turg tagab rahuliku homse.”

**Järeldus:** Condor ei ela väljaspool turgu. Võidutõenäosus sõltub tähtajast, strike’idest ja jaotusest.

## 30. Mille eest maksad zero-cost collar’is?

**Lühivastus:** Loovutatud tõusupotentsiaaliga.

**Selgitus:** Call’i müük rahastab put’i, kuid annab teisele õiguse saada sinu aktsia kindla hinnaga.

**Näide/arvutus:** Put 95 ja call 105 mõlemad 3: null preemiat, kasum üle 105 piiratud.

**Levinud väärarusaam:** „Tasuta kindlustus ilma kompromissita.”

**Järeldus:** Nullkuluga kaitsel on hind. Kulud võivad muuta netopreemia nullist erinevaks.

## 31. Miks long call − put pole tasuta aktsia?

**Lühivastus:** Tema terminalväljamakse on S−K, mitte S.

**Selgitus:** Puudu on strike’i tasumiseks vajalik rahajalg; risk jääb ka null netopreemia puhul.

**Näide/arvutus:** S=0, K=100: sünteetika annab −100 ühikut.

**Levinud väärarusaam:** „Null avamiskulu tähendab null riski.”

**Järeldus:** Sünteetika vajab raha. Intressi ja dividendiga tuleb kasutada täpset parity’t.

## 32. Millal covered call ja cash-secured put on võrreldavad?

**Lühivastus:** Sama strike’i, tähtaja ja korrektse rahastuse korral.

**Selgitus:** Put-call parity seob terminalrahavood; erinevad strike’id või dividendieelne täitmine rikuvad lihtsa võrdluse.

**Näide/arvutus:** S=K=100, c=p=6: mõlema netokulu 94 ja terminalväärtus min(S,100).

**Levinud väärarusaam:** „Kõik covered call’id on kõikide short put’idega samad.”

**Järeldus:** Sama kuju vajab samu tingimusi. Kontrolli ka kulusid, dividende ja exercise-stiili.

## 33. Miks calendar spread’i tasuvuspiir pole universaalne?

**Lühivastus:** Pikk jalg on lühikese lõppedes endiselt turuhinnaga optsioon.

**Selgitus:** Allesjäänud hind sõltub IV-st, ajast ja intressist, mitte ainult sisemisest väärtusest.

**Näide/arvutus:** 30/60 päeva calendar’i pika jala väärtus 30. päeval muutub IV 15% ja 30% vahel.

**Levinud väärarusaam:** „Kõik jalad võib esimesel tähtajal sisemiseks väärtuseks asendada.”

**Järeldus:** Kaks tähtaega pole üks payoff. Kui mõlemad lõpuks lõppevad, peab kirjeldama ka vahepealseid rahavooge.

## 34. Miks 1×2 call ratio spread võib ohtlik olla?

**Lühivastus:** Suurte hindade juures jääb üks neto short call.

**Selgitus:** Üks long call katab ainult ühe short call’i; teine jääb hinnatõusuga kasvavaks kohustuseks.

**Näide/arvutus:** K100 long, 2×K110 short: suure S korral payoff 120−S.

**Levinud väärarusaam:** „Kaks müüdud jalga on lihtsalt parem rahastus.”

**Järeldus:** Lisamüük võib avada piiramatu saba. Lisatud kaitsev call muudaks sabariski, kuid maksab.

## 35. Kas wheel teeb aktsia kahjumist preemiatulu?

**Lühivastus:** Ei, kogu aktsia- ja optsioonitulemus tuleb kokku liita.

**Selgitus:** Uute call’ide müük võib tuua raha, kuid vähendab taastumise tõusupotentsiaali.

**Näide/arvutus:** Ost 95, put’i krediit 3, call’i krediit 2, lõpphind 70: −20 ühikut.

**Levinud väärarusaam:** „Uus preemia tähendab vana kahju kadumist.”

**Järeldus:** Wheel ei kustuta ostuhinda. Tulemuseks on teekonnast sõltuv protsess, mitte püsiv tootlusmäär.

## 36. Kuidas võib 90% võitude korral raha kaotada?

**Lühivastus:** Harvad kahjud võivad olla keskmistest võitudest suuremad.

**Selgitus:** Tähtis on tõenäosusega kaalutud summa, mitte plussmärkide arv.

**Näide/arvutus:** 0,9×10−0,1×120=−3.

**Levinud väärarusaam:** „Rohkem võite kui kaotusi tähendab kasumlikkust.”

**Järeldus:** Võidumäär ei ole eelis. Kahe tulemuse mudel on lihtsustus; päriselt vaata kogu jaotust.

## 37. Miks positiivne brutotulemus ei taga netokasumit?

**Lühivastus:** Spread, komisjon ja täitmisnihe vähendavad tulemust.

**Selgitus:** Väikese tehingueelise korral võib teostus moodustada suure osa oodatavast tulust.

**Näide/arvutus:** Bruto E=4 USD, kulud 6 USD: neto −2.

**Levinud väärarusaam:** „Hea backtest on automaatselt kaubeldav.”

**Järeldus:** Kulud võivad eelise ära süüa. Kulud sõltuvad kogusest, turuolust ja korraldusest.

## 38. Kas 2000 USD margin tähendab kuni 2000 USD kahju?

**Lühivastus:** Ei.

**Selgitus:** Tagatisnõue on krediidiriski juhtimise mehhanism; kohustus võib olla palju suurem ja tagatist juurde nõuda.

**Näide/arvutus:** Katmata call võib hüppel kaotada 5000, kuigi algmargin oli 2000.

**Levinud väärarusaam:** „Maakler piirab alati kahju sissemaksega.”

**Järeldus:** Tagatis pole kahjupiir. Täpne margin sõltub tootest ja maaklerist.

## 39. Miks stop-loss ei taga maksimaalset kahjumit?

**Lühivastus:** Hind võib stopist üle hüpata ja likviidsus kaduda.

**Selgitus:** Stop aktiveerib korralduse, kuid täitmine toimub olemasoleva turu tingimustel.

**Näide/arvutus:** Stop 95, järgmine saadav hind 80: müük võib olla 80 lähedal.

**Levinud väärarusaam:** „Stop on sama mis ostetud put.”

**Järeldus:** Stop pole kindel hind. Stop-limit võib vältida halba hinda, kuid jääda üldse täitmata.

## 40. Mida teha, kui üks leping ületab riskieelarve?

**Lühivastus:** Selles raamistikus tehingut mitte avada.

**Selgitus:** Täisarvuline kogus ei allu soovmõtlemisele; väiksem risk vajab teist instrumenti või struktuuri.

**Näide/arvutus:** Eelarve 100, lepingu risk 350: floor(100/350)=0.

**Levinud väärarusaam:** „Üks leping on alati piisavalt väike.”

**Järeldus:** Null lepingut on korrektne vastus. Riskieelarve ise tuleb põhjendada, mitte võtta universaalse protsendina.

## 41. Miks kümme short put’i pole tingimata hajutatud?

**Lühivastus:** Alusvarad võivad kriisis ühiselt langeda.

**Selgitus:** Erinevad nimed ei võrdu sõltumatud tegurid; sektor ja turubeta ühendavad positsioone.

**Näide/arvutus:** Kümme tehnoloogiaaktsiat langevad sama uudise järel.

**Levinud väärarusaam:** „Rohkem tehinguid tähendab automaatselt väiksemat riski.”

**Järeldus:** Riskid võivad kokku kuhjuda. Hajutamist hinnatakse korrelatsiooni ja stressiga.

## 42. Miks 20% kaotus vajab 25% tõusu?

**Lühivastus:** Kasv arvutatakse väiksemalt baasilt.

**Selgitus:** Kapitali vähenemine muudab taastumisprotsendi suuremaks kui algne langusprotsent.

**Näide/arvutus:** 100→80; 80×1,25=100.

**Levinud väärarusaam:** „−20% ja +20% tasanduvad.”

**Järeldus:** Taastumine on asümmeetriline. Liitkasvu arvestus kehtib igal järjestikusel tootlusel.

## 43. Kas rollimise krediit tähendab positsiooni päästmist?

**Lühivastus:** Ei, vana positsioon suletakse ja uus risk avatakse.

**Selgitus:** Uue lepingu rahavoog võib peita realiseeritud kahju, kui vaadata ainult viimast kontolaekumist.

**Näide/arvutus:** Vana sulgemine −500, uus krediit +600 jätab uue kohustuse alles.

**Levinud väärarusaam:** „100 netolaekumist tähendab kogu tehingu kasumit.”

**Järeldus:** Roll on kaks tehingut. Võrdle mõlemat tehingut ja kõiki allesjäänud kohustusi.

## 44. Miks piiratud riskiga spread võib vajada lisaraha?

**Lühivastus:** Üks jalg võib täituda enne teist.

**Selgitus:** Terminalne kompensatsioon ei pruugi automaatselt tekkida samal hetkel; aktsiad ja raha tuleb hallata.

**Näide/arvutus:** Short put K100 assignment tähendab 10000 USD ostu, long K95 jääb esialgu alles.

**Levinud väärarusaam:** „Kaitsev jalg lahendab kõik automaatselt.”

**Järeldus:** Täitmine võib jalad lahutada. Maakleri netting ja menetlused erinevad; kontrolli konkreetset protsessi.

## 45. Miks short call’i risk suureneb mõnikord dividendi eel?

**Lühivastus:** Ostjal võib olla kasulik õigust varakult kasutada.

**Selgitus:** Dividendi saamise kasu tuleb võrrelda loovutatava välise väärtuse ja rahastuskuluga.

**Näide/arvutus:** Väline väärtus 0,1, dividend 1 võib muuta täitmise atraktiivseks.

**Levinud väärarusaam:** „Assignment toimub ainult tähtajal.”

**Järeldus:** Dividend muudab otsust. See puudutab Ameerika tüüpi call’i; dividend üksi pole piisav täpne reegel.

## 46. Miks ekraanil nähtud indeksihind võib erineda arveldusest?

**Lühivastus:** Lepingu ametlik arveldusväärtus arvutatakse kindla reegli järgi.

**Selgitus:** AM/PM aeg, komponentide hinnad ja kauplemise lõpp võivad erineda tavalisest viimase tehingu hinnast.

**Näide/arvutus:** Eeldatud 100 asemel arveldus 101 muudab K100 call’i väärtuse 0-lt 1-le.

**Levinud väärarusaam:** „Kõik optsioonid arvelduvad viimase ekraanihinnaga.”

**Järeldus:** Lõpphind pole alati arveldushind. Kontrolli alati toote spetsifikatsiooni.

## 47. Kas odav 0DTE on tingimata väiksema riskiga?

**Lühivastus:** Ei, täielik kaotus võib saabuda väga kiiresti.

**Selgitus:** Lühike aeg ja ATM gamma muudavad hinna tundlikuks; protsentuaalne risk võib olla suur.

**Näide/arvutus:** 0,5 preemia M100 tähendab 50, mis võib samal päeval täielikult kaduda.

**Levinud väärarusaam:** „Odav hind tähendab aeglast või väikest riski.”

**Järeldus:** 0DTE koondab otsused. Rahaline kahju sõltub ka lepingute arvust ja müüdud kohustustest.

## 48. Miks BSM-i hind ei pruugi olla turul teostatav?

**Lühivastus:** Mudel lihtsustab turgu ning ei sisalda sinu täitmiskulu.

**Selgitus:** Püsiv IV, pidev kauplemine ja hüpete puudumine ei kirjelda kogu tegelikkust.

**Näide/arvutus:** Mudel 3,00, bid/ask 2,70/3,30: ost 3,00 pole garanteeritud.

**Levinud väärarusaam:** „Mudeli väljund on õige hind, turg eksib.”

**Järeldus:** Mudel pole hinnapakkumine. Kasuta mudelit võrdluse ja tundlikkuste, mitte kindla täitmisena.

## 49. Miks nullsummaline leping ei tõesta kõigi strateegiate võrdset eelist?

**Lühivastus:** See seob sama lepingu vastaspooled, mitte erinevate riskide jaotusi.

**Selgitus:** Tegeliku maailma riskipreemiad, hinnad ja kulud võivad eri strateegiate ootusi muuta.

**Näide/arvutus:** Sama call’i ostja +200 tähendab müüjale −200 enne kulusid; see ei määra teise put’i oodatavat tulemust.

**Levinud väärarusaam:** „Kõigi strateegiate pikaajaline kasum on sama.”

**Järeldus:** Nullsumma ei võrdsusta strateegiaid. Riskineutraalne hinnastus erineb tegelikust tootlusprognoosist.

## 50. Miks trendisüsteemi ei saa automaatselt optsioonidele üle kanda?

**Lühivastus:** Optsioon lisab strike’i, tähtaja ja IV valiku.

**Selgitus:** Aktsiasignaali eelis ei pruugi katta preemiat ja kulusid; valikuid on rohkem ning üleoptimeerimise oht kasvab.

**Näide/arvutus:** Aktsiasignaal +2%, aga OTM call vajab tasuvuseks +8%.

**Levinud väärarusaam:** „Kasumlik aktsiameetod garanteerib kasumlikud call’id.”

**Järeldus:** Hea lugu vajab testi. Testi väljaspool treeningperioodi, realistlike hinnavahedega.

## 51. Kas positiivne ootus tähendab, et tüüpiline tehing võidab?

**Lühivastus:** Ei.

**Selgitus:** Harv suur võit võib teha keskmise positiivseks, kuigi enamik üksiktehinguid kaotab.

**Näide/arvutus:** 90% −1 ja 10% +15: E=+0,6, mediaan −1.

**Levinud väärarusaam:** „Positiivne E tähendab üle poole võite.”

**Järeldus:** Oodatav tulemus pole mediaan. Tulemuse usaldus sõltub sabatõenäosuse hinnangu kvaliteedist.

## 52. Kas payoff-graafikult saab välja lugeda oodatava kasumi?

**Lühivastus:** Ei, vaja on lõpphindade tõenäosusi.

**Selgitus:** Graafik määrab tulemuse igal hinnal, jaotus määrab nende tulemuste kaalu.

**Näide/arvutus:** S=90/110 võrdse tõenäosusega annab teise ootuse kui 90% tõenäosus S=90-le.

**Levinud väärarusaam:** „Graafiku roheline pind on võidutõenäosus.”

**Järeldus:** Tõenäosus vajab jaotust. Tihedusgraafiku ja P/L-graafiku telgi ei tohi segi ajada.

## 53. Kas võitude ja kahjude kaalutud pindade võrdsus tähendab 50% võite?

**Lühivastus:** Ei, see tähendab sobiva definitsiooni korral null ootust.

**Selgitus:** Tulemuse suurus ja tõenäosus on erinevad; väike sagedane võit võib tasakaalustuda suure harva kahjuga.

**Näide/arvutus:** 90% +1 ja 10% −9: E=0, võidumäär 90%.

**Levinud väärarusaam:** „Null ootus tähendab võrdselt võite ja kaotusi.”

**Järeldus:** Tõenäosusega kaalutud pind pole võidumäär. Järeldus eeldab normaliseeritud jaotust ja õigesti kaalutud P/L-i.

## 54. Miks sama turuvaatega SPY- ja SPX-tüüpi optsioonid vajavad eri kontrolli?

**Lühivastus:** Alusvara ja lepingutingimused erinevad.

**Selgitus:** ETF-i osakute üleandmine ja indeksilepingu rahaline arveldus toovad erineva operatiivse riski.

**Näide/arvutus:** Üks leping võib tekitada ETF-i osakud, teine rahalise makse.

**Levinud väärarusaam:** „Sama indeksiga seotud tähendab sama lepingut.”

**Järeldus:** Aktsia ja ETF pole indeksileping. Täpne stiil, kordaja ja arveldus tuleb toote kaupa kontrollida.

## 55. Miks sama aktsia eri strike’idel on eri IV?

**Lühivastus:** Turg hinnastab eri hinnapiirkondade riski erinevalt.

**Selgitus:** Languskaitse nõudlus ja sabarisk võivad anda volatiilsuskalde; üks sigma on lihtsustus.

**Näide/arvutus:** K90 put’i IV 30%, K100 call’i IV 20%.

**Levinud väärarusaam:** „Alusvaral on üks kõigile lepingutele identne IV.”

**Järeldus:** IV-kõver ei ole tasane. Erinevus võib muutuda koos tähtaja ja turuoluga.

## 56. Miks kaks 500-hinnalise ETF-i put’i ei pruugi kohe katta 100000 portfelli liikumist?

**Lühivastus:** Optsiooni delta võib olla absoluutväärtuselt alla ühe.

**Selgitus:** Nominaal vastab võimalikule lepingumahule, hetketundlikkus arvestab deltat.

**Näide/arvutus:** 2×100×500×0,5=50000 ligikaudset delta-ekspositsiooni.

**Levinud väärarusaam:** „Võrdne nimiväärtus tähendab täpset päevast kaitset.”

**Järeldus:** Nominaalne maandus pole delta-maandus. Lisaks tekib portfelli ja ETF-i erinevusest baasirisk.

## 57. Kas indeksiput garanteerib üksikaktsiaportfellile põranda?

**Lühivastus:** Ei, portfell võib indeksist erinevalt liikuda.

**Selgitus:** Maanduse alusvara pole sama mis kaitstav vara; korrelatsioon pole kindel lepinguline seos.

**Näide/arvutus:** Portfell −30%, indeks −10%: kaitse võib olla ebapiisav.

**Levinud väärarusaam:** „Korrelatsioon 0,9 tähendab 90% garanteeritud kaitset.”

**Järeldus:** Baasisrisk jääb. Sama alusvara put annab täpsema lepingu põranda kindlale kogusele.

## 58. Kas sünteetilise forward’i theta on alati null?

**Lühivastus:** Ei, rahastamise ja dividendide mõju võib jääda.

**Selgitus:** Gamma ja vega tühistumine ei tähenda kõigi ajaga seotud rahavoogude kadumist.

**Näide/arvutus:** C−P=S−K exp(−rT) dividendideta mudelis.

**Levinud väärarusaam:** „Sünteetika on kõigi kreeklaste suhtes immuunne.”

**Järeldus:** Intress ei kao sünteetikast. r=q=0 lihtsustuses kaob see konkreetne carry-mõju.

## 59. Mida tõestab edukas Python-kontroll?

**Lühivastus:** Et kood vastab kontrollitud valemitele ja juhtudele.

**Selgitus:** See ei tõesta hinnaprognoosi, turu täitmist ega strateegia tulevast tootlust.

**Näide/arvutus:** Put-call parity testi läbimine ei tõesta call’i ostu kasumlikkust.

**Levinud väärarusaam:** „Kõik testid rohelised tähendab turul eelist.”

**Järeldus:** Õppetest pole turutest. Vaja on eraldi andmekvaliteedi, teostuse ja üldistusvõime kontrolli.

## 60. Kas long call’i preemiakahju piir kehtib ka pärast aktsiaks täitmist?

**Lühivastus:** Mitte uue aktsiapositsiooni kogu edasisele riskile.

**Selgitus:** Optsiooni täitmine muudab vara ja rahavooge; hilisem aktsialangus on uus risk.

**Näide/arvutus:** K100 call täidetakse, saad 100 aktsiat; nende langus 100-lt 80-le annab uue 2000 kahju.

**Levinud väärarusaam:** „Ostetud optsioon kaitseb igavesti preemiapiiriga.”

**Järeldus:** Kindel kahjupiir vajab tervikpositsiooni. Sulge või hinda ümber täitmisel tekkinud positsioon.

