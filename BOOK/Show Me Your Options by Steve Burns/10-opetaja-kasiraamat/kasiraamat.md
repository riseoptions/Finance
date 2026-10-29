# Kuidas õpetada optsioone lihtsalt ja arusaadavalt?

[Tagasi](../README.md)

Õpetaja käsiraamat. Kasuta kolme tasandit: õppija **mõistab**, **arvutab ise** ja **oskab õpetada**. Tunni eesmärk pole soovitada kauplemist, vaid lasta õppijal õigesti põhjendada mehhanismi ja piiranguid.

## Ühine 90 minuti tunnikava

| Aeg | Tegevus | Kontrollitav tulemus |
|---|---|---|
| 0–10 | Provotseeriv küsimus ja individuaalne ennustus | Õppija kirjutab oma algse seletuse |
| 10–30 | Intuitsioon ning mõisted | Õppija eristab vähemalt kaht sarnast mõistet |
| 30–45 | Kaks analoogiat ja nende piirid | Õppija nimetab ühe koha, kus analoogia eksitab |
| 45–65 | Arvuline ülesanne ning ekraani/Pythoni demo | Tulemus on ühikutega kontrollitav |
| 65–80 | Paaristöö ja vastuväite arutelu | Õppija põhjendab, mitte ei loe definitsiooni |
| 80–90 | Väljumispilet: üks arvutus ja üks miks-küsimus | Õpetaja näeb järgmise tunni vajadust |

See on ühe õppetunni mall; kogu moodul vajab õppekavas rohkem kui ühe tunni. Strateegiate moodul jaga neljaks: baaspositsioonid, vertikaalid, mitmejalgsed kombinatsioonid, eri tähtajad ja sünteetika.

## Moodul I. Olemus

**Põhimaterjal:** [I. Olemus](../01-optsioonide-alused/oppetukk.md).

**Õpieesmärgid:** Õppija eristab call/put’i ning ostja õigust ja müüja kohustust; arvutab nelja baaspositsiooni P/L-i.

**Mõisted:** Call, put, strike, premium, expiration, exercise, assignment.

### Viis võtmeselgitust

1. Õigus pole alusvara omamine.
2. Call ostab ja put müüb alusvara kokkulepitud hinnaga.
3. Ostjal on valik, müüjal kohustus.
4. Preemia tuleb P/L-ist lahutada.
5. Müügi tehing võib positsiooni sulgeda, mitte avada.

### Kaks analoogiat koos piiridega

- Jalgratta broneerimisõigus: aitab seletada call’i; piirang on järelturu ja standardtingimuste puudumine.
- Müügihinna kindlustus: aitab seletada put’i; optsioon ei nõua tegeliku kahju tõendamist.

**Arvuline näide:** K105,c 3,S110,M100 → väljamakse 500,kasum 200.

**Demonstratsioon:** Joonista K105 juurde murdepunkt; nihuta call’i payoff 3 võrra alla. Käivita python/01_call.py.

### Viis kontrollküsimust vastustega

1. **Kas ITM call võib tähtajal kahjumit anda?** Jah, kui sisemine väärtus ei kata preemiat. ITM võrdleb alusvara strike’iga, P/L võrdleb väljamakset ka ostuhinnaga.
2. **Miks ei saa optsiooni müüja lihtsalt täitmisest loobuda?** Ta on müünud teisele valikuõiguse. Kohustus püsib kuni sulgemise või lepingu lõppemiseni; assignment pole müüja uus vabatahtlik otsus.
3. **Kas put’i ost tõestab aktsia langusootust?** Ei, see võib piirata olemasoleva portfelli riski. Kindlustust võib osta ka siis, kui loodetakse vara väärtuse kasvule.
4. **Kas call’i müües tekib alati piiramatu risk?** Ei, varem ostetud call’i sulgemine lõpetab positsiooni. Avav ja sulgev tehing on eri toimingud; risk sõltub lõpppositsioonist.
5. **Kas Euroopa optsioonist saab enne tähtaega väljuda?** Sageli saab selle turul sulgeda. Euroopa piirang käib õiguse kasutamise, mitte üldise kauplemiskeelu kohta.

**Tüüpilised väärarusaamad:** ITM=kasum.; Iga müük avab lühikese positsiooni.

**Praktiline töö:** Ülesanne 1; muuda lõpphind107-ks ja lase õppijal põhjendada kahju. Lahendused: [ülesannete kogu](../08-30-ulesannet/ulesanded.md).

**Tunni lõpu põhimõte:** Õigus maksab; väärtus pole kasum.

**Väljumispilet:** Selgita sama näidet ilma valemita, seejärel kirjuta üks ühikutega valem ning nimeta üks eeldus, mille muutumine muudaks järeldust.

## Moodul II. Hind

**Põhimaterjal:** [II. Hind](../02-optsiooni-hind/oppetukk.md).

**Õpieesmärgid:** Õppija jagab hinna sisemiseks ja väliseks väärtuseks ning seletab IV, aja ja spread’i mõju.

**Mõisted:** Intrinsic value, extrinsic value, implied volatility, bid, ask, liquidity.

### Viis võtmeselgitust

1. Hind sisaldab võimalust.
2. IV on hinnast tuletatud mudelisisend.
3. Aeg ja IV on eri tegurid.
4. Õige suund võib anda kahjumi.
5. Keskhind ei taga täitmist.

### Kaks analoogiat koos piiridega

- Pikem broneerimisaken: rohkem võimalusi; piiranguks erinevad tähtajad ja intress.
- Kindlustushind enne tormi: ebakindlus maksab; turu IV pole objektiivne kahjutõenäosus.

**Arvuline näide:** S104,K100,hind 6 → sisemine 4,väline 2.

**Demonstratsioon:** Näita python/09_theta.py kõverat, seejärel muuda sigma 0,2→0,4. Lase õppijal enne tulemust ennustada.

### Viis kontrollküsimust vastustega

1. **Kas ajaväärtuse kadu tõestab aja möödumise mõju?** Ei, seda võivad muuta ka IV ja alusvara hind. Väline väärtus on hinna ning sisemise väärtuse vahe, mitte iseseisev kellamehhanism.
2. **Kas oodatud suur uudis tähendab head straddle’i ostu?** Ainult siis, kui tasutud hind on tulemustega võrreldes põhjendatud. Oodatud liikumine võib olla juba preemiates; sündmuse õige ennustamine ei taga eelist.
3. **Kuidas saab tõusnud aktsia call odavneda?** IV langus ja ajakadu võivad delta mõju ületada. Mitu sisendit muutuvad korraga; delta üksinda ei kirjelda kogutulemust.
4. **Miks pikema tähtaja hind ei kasva ajaga võrdeliselt?** ATM-lähenduses kasvab võimaluse väärtus ligikaudu ruutjuurega ajast. Hinnajaotuse hajuvus kasvab tüüpilises difusioonimudelis ruutjuurega ajast.
5. **Miks positiivne brutotulemus ei taga netokasumit?** Spread, komisjon ja täitmisnihe vähendavad tulemust. Väikese tehingueelise korral võib teostus moodustada suure osa oodatavast tulust.

**Tüüpilised väärarusaamad:** Ajaväärtus sõltub ainult ajast.; Kõrge IV tähendab automaatselt head müüki.

**Praktiline töö:** Ülesanded6 ja8; leia täitmise tõttu tekkiv kulu. Lahendused: [ülesannete kogu](../08-30-ulesannet/ulesanded.md).

**Tunni lõpu põhimõte:** Hinnas on ootus ja täitmisel on hind.

**Väljumispilet:** Selgita sama näidet ilma valemita, seejärel kirjuta üks ühikutega valem ning nimeta üks eeldus, mille muutumine muudaks järeldust.

## Moodul III. Kreeklased

**Põhimaterjal:** [III. Kreeklased](../03-kreeklased/oppetukk.md).

**Õpieesmärgid:** Õppija nimetab viie mõõdiku ühikud, summeerib positsiooni riskid ja kirjeldab lähenduse piiri.

**Mõisted:** Delta, gamma, theta, vega, rho, protsendipunkt.

### Viis võtmeselgitust

1. Delta on osatundlikkus.
2. Gamma muudab deltat.
3. Theta ei ole garanteeritud päevatulu.
4. Vega vajab ühikut.
5. Rho kirjeldab intressi mõju.

### Kaks analoogiat koos piiridega

- Auto kiirus ja kiirendus: delta ja gamma; mudel ei ole füüsiline liikumisgarantii.
- Mitme nupuga helipult: üks nupp korraga annab tundlikkuse; päriselus liiguvad nupud koos.

**Arvuline näide:** Δ0,5,Γ0,04,ΔS2 → hinnamõju 1,08 enne thetat.

**Demonstratsioon:** Käivita python/08_delta.py; näita puutuja ja mudelikõvera lahknemist.

### Viis kontrollküsimust vastustega

1. **Miks delta ei võta kokku kõiki kreeklasi?** Ta mõõdab hinna tundlikkust ainult alusvara suhtes. Mõõtmise hetkel hoitakse teised sisendid paigal; need võivad päriselus ise muutuda.
2. **Miks algne delta ei sobi suure hinnahüppe jaoks?** Delta muutub koos alusvara hinnaga. Gamma kirjeldab seda muutust lokaalselt; suurel sammul muutub ka gamma ise.
3. **Kas positiivne theta tagab müüjale kasumi?** Ei, see isoleerib ainult aja mõju. Negatiivne gamma või vega võib turu muutumisel theta-eelise kiiresti ületada.
4. **Milline IV muutus läheb vega valemisse?** Platvormi ühikule vastav muutus, sageli protsendipunktides. 20%-lt 25%-le on 5 pp, kuid suhteliselt 25%; need pole sama arv.
5. **Miks delta-neutraalne positsioon võib palju kaotada?** Gamma, vega, theta ja hüpped jäävad. Hetkeline suunatasakaal ei säili tingimata ning IV võib muuta mõlema jala väärtust.

**Tüüpilised väärarusaamad:** Delta on täpne tõenäosus.; Null delta tähendab null riski.

**Praktiline töö:** Ülesanded19 ja27; arvuta uus netodelta. Lahendused: [ülesannete kogu](../08-30-ulesannet/ulesanded.md).

**Tunni lõpu põhimõte:** Ühik, märk, kogus, ajamoment.

**Väljumispilet:** Selgita sama näidet ilma valemita, seejärel kirjuta üks ühikutega valem ning nimeta üks eeldus, mille muutumine muudaks järeldust.

## Moodul IV. Strateegiad

**Põhimaterjal:** [IV. Strateegiad](../04-strateegiad/README.md).

**Õpieesmärgid:** Õppija liidab jalad, leiab kahjupiiri ja tasuvuse ning põhjendab lihtsamat alternatiivi.

**Mõisted:** Debit spread, credit spread, covered call, straddle, calendar, parity.

### Viis võtmeselgitust

1. Iga jalg on eraldi leping.
2. Krediit pole kasum.
3. Terminalgraafik pole tänane hind.
4. Müüdud lisakogus võib jätta piiramatu saba.
5. Kaks tähtaega vajavad mudelit.

### Kaks analoogiat koos piiridega

- Ehitusklotsid: liida lihtsad väljamaksed; piiranguks jalgade ajaliselt erinev täitmine.
- Aed kahe piirdega: collar piirab alla ja üles; piiranguks aegumine ja kaitse hind.

**Arvuline näide:** Bull call 100/110,deebet 4 → max kahju 400,max kasum 600,tasuvus 104.

**Demonstratsioon:** Näita python/06_bull_call.py, seejärel graafikut ratio spread’ist. Küsi, mis muutus, kui müüsime ühe call’i juurde.

### Viis kontrollküsimust vastustega

1. **Mille eest covered call tegelikult kaitseb?** Aktsiate olemasolu katab call’i tarnekohustuse, mitte aktsia langust. Preemia pakub ainult väikese puhvri; aktsia võib jätkuvalt kaotada suure osa väärtusest.
2. **Kuidas leida credit spread’i maksimaalne kahju?** Strike’ide vahe miinus krediit, korda kordaja. Kaitsev jalg piirab terminalkohustust, kuid selle ja müüdud jala vahe jääb riskiks.
3. **Kas iga deebetiga strateegia maksimaalne kahju on deebet?** Ei, näiteks ratio spread võib maksta deebetit ja jääda katmata. Rahavoo märk ei määra väljamakse sabade kuju; loe lepingukoguseid.
4. **Miks long call − put pole tasuta aktsia?** Tema terminalväljamakse on S−K, mitte S. Puudu on strike’i tasumiseks vajalik rahajalg; risk jääb ka null netopreemia puhul.
5. **Miks calendar spread’i tasuvuspiir pole universaalne?** Pikk jalg on lühikese lõppedes endiselt turuhinnaga optsioon. Allesjäänud hind sõltub IV-st, ajast ja intressist, mitte ainult sisemisest väärtusest.

**Tüüpilised väärarusaamad:** Kõik deebetid on piiratud riskiga.; Covered call kõrvaldab languse.

**Praktiline töö:** Ülesanne30; esita võrdlus sama riskieelarve alusel. Lahendused: [ülesannete kogu](../08-30-ulesannet/ulesanded.md).

**Tunni lõpu põhimõte:** Strateegia nimi ei asenda rahavoogude liitmist.

**Väljumispilet:** Selgita sama näidet ilma valemita, seejärel kirjuta üks ühikutega valem ning nimeta üks eeldus, mille muutumine muudaks järeldust.

## Moodul V. Risk ja mõtlemine

**Põhimaterjal:** [V. Risk ja mõtlemine](../05-riskijuhtimine/oppetukk.md).

**Õpieesmärgid:** Õppija arvutab oodatava tulemuse ja koguse, tuvastab peidetud riskid ning hindab tõendusmaterjali.

**Mõisted:** Expected value, margin, slippage, drawdown, assignment, tail risk.

### Viis võtmeselgitust

1. Võidumäär vajab võidu ja kahju suurust.
2. Tagatis pole kahjupiir.
3. Stop ei taga hinda.
4. Riskid võivad olla korrelatsioonis.
5. Backtest ei tõesta tulevikku.

### Kaks analoogiat koos piiridega

- Sillatasu ja kokkuvarisemine: sagedane tulu võib varjata harva kahju; sagedus pole kindel.
- Turvavöö ja kiirus: kaitse ei õigusta suurt kogust; erinevalt füüsikast pole turujaotus püsiv.

**Arvuline näide:** 0,9×10−0,1×120−2=−5 USD.

**Demonstratsioon:** Käivita python/11_oodatav.py; muuda p-d ning kulusid. Näita, kui kõrge peab tasuvus-p olema.

### Viis kontrollküsimust vastustega

1. **Kuidas võib 90% võitude korral raha kaotada?** Harvad kahjud võivad olla keskmistest võitudest suuremad. Tähtis on tõenäosusega kaalutud summa, mitte plussmärkide arv.
2. **Kas 2000 USD margin tähendab kuni 2000 USD kahju?** Ei. Tagatisnõue on krediidiriski juhtimise mehhanism; kohustus võib olla palju suurem ja tagatist juurde nõuda.
3. **Miks stop-loss ei taga maksimaalset kahjumit?** Hind võib stopist üle hüpata ja likviidsus kaduda. Stop aktiveerib korralduse, kuid täitmine toimub olemasoleva turu tingimustel.
4. **Mida teha, kui üks leping ületab riskieelarve?** Selles raamistikus tehingut mitte avada. Täisarvuline kogus ei allu soovmõtlemisele; väiksem risk vajab teist instrumenti või struktuuri.
5. **Kas rollimise krediit tähendab positsiooni päästmist?** Ei, vana positsioon suletakse ja uus risk avatakse. Uue lepingu rahavoog võib peita realiseeritud kahju, kui vaadata ainult viimast kontolaekumist.

**Tüüpilised väärarusaamad:** 90% võite tõestab eelist.; Rolling kustutab vana kahju.

**Praktiline töö:** Ülesanded20,21 ja29; lase ühel õppijal kaitsta, teisel kritiseerida eeldusi. Lahendused: [ülesannete kogu](../08-30-ulesannet/ulesanded.md).

**Tunni lõpu põhimõte:** Mõõda halba päeva enne hea kuu lubamist.

**Väljumispilet:** Selgita sama näidet ilma valemita, seejärel kirjuta üks ühikutega valem ning nimeta üks eeldus, mille muutumine muudaks järeldust.

## Õpetaja abimaterjal rasketele küsimustele

### „Kui müüja saab preemia kohe, miks ei ole see lihtne tulu?”

**Lihtsalt:** saad raha, sest võtad kohustuse. **Täpsemalt:** laekumise kõrval tekib tagasiostetav või täidetav leping; netovara ei kasva automaatselt saadud preemia võrra. **Näide:** short put K95 annab 300, aga S50 korral on kohustuse väärtus 4500 ja P/L −4200. **Analoogia:** kindlustusmakse pole kasum enne kahjukohustuste arvestamist; turuleping ei eelda siiski tõendatud kindlustusjuhtumit. **Kontroll:** mis juhtuks, kui hind läheks nulli?

### „Kas raamat ütleb valesti, et optsioonid pole varad?”

**Lihtsalt:** see on rõhuasetus lepingu iseloomule, mitte korrektne ülddefinitsioon. **Täpsemalt:** ostetud optsioon on finantsvara, kuid ei ole ettevõtte omandiosa ning võib aeguda. **Näide:** 300 eest ostetud lepingu turuväärtus võib olla 400. **Analoogia:** aeguv pilet võib omada väärtust ilma hoone omandiõiguseta. **Kontroll:** kas aegumine välistab tänase rahalise väärtuse?

### „Miks ei saa lihtsalt igal kuul 2% preemiat koguda?”

**Lihtsalt:** laekumisega käib kaasas risk. **Täpsemalt:** 2% preemiat ei kirjelda aktsiakahju, tagatist ega seda, kas järgmine leping annab sama hinna. **Näide:** 200 preemia ja 3000 aktsiakahju annavad −2800, mitte +2%. **Analoogia:** renditulu ei tühista maja väärtuse langust; optsioonil lisanduvad tähtajad ja kohustused. **Kontroll:** mis on kogu konto omakapitali muutus?

### „Kas delta järgi võib võidutõenäosust hinnata?”

**Lihtsalt:** ainult jämeda ja tingimusliku lähendina ITM-ile. **Täpsemalt:** kasum nõuab lisaks preemia katmist; mudeli riskineutraalne tõenäosus ei ole tingimata tegelik tõenäosus. **Näide:** K100 call maksab 5, nii et S103 on ITM, aga tehing miinuses. **Analoogia:** eksami miinimumkünnise ületamine pole sama kui stipendiumi saamine; künnised on eri kõrgusel. **Kontroll:** millise sündmuse tõenäosust sa tegelikult hindad?

### „Kas keerulisem kombinatsioon on professionaalsem?”

**Lihtsalt:** rohkem jalgu tähendab rohkem asju kontrollida. **Täpsemalt:** kombinatsioon on kasulik, kui see muudab riski soovitud viisil ja kasu ületab kulusid. **Näide:** 50 USD maksimumkasum võib kaduda nelja jala spread’i ja tasudesse. **Analoogia:** rohkem tööriistu ei tee parandust automaatselt paremaks. **Kontroll:** mida see lisajalg teeb halvimas stsenaariumis?

## Tööleht õppijale

1. Minu eesmärk ja ajahorisont: …
2. Alusvara, S, K, tähtaeg, kordaja, täitmis- ja arveldusviis: …
3. Kõik ostetud ja müüdud jalad koos preemiatega: …
4. Algne netorahavoog: …
5. P/L hindadel 0, 80, 100, 120: …
6. Maksimaalne kahju, maksimumkasum ja tasuvuspiirid: …
7. Delta, gamma, theta ja vega põhiline mõju: …
8. Kulud ning ühe jala assignment’i tagajärg: …
9. Lihtsam alternatiiv: …
10. Mis tõendaks, et minu põhjendus oli vale? …

## Hindamine

Iga kriteerium 0–4 punkti: mehhanism; arvutused ja ühikud; riskide ning eelduste käsitlus; selgituse arusaadavus; kriitiline alternatiivide võrdlus. Kokku 20. Arvestus soovituslikult vähemalt 14 ja mitte ühtki kriitilist kohustuseviga. Piiramatu short call’i riski nimetamine piiratud preemiaga riskiks vajab parandamist sõltumata koguskoorist.

## Lõputest koos vastustega

1. Call K105,c 3,S107,M100: **P/L −100**; õige suund ei katnud hinda.
2. Put K95,p 3,S80,M100: **P/L +1200**.
3. Credit spread’i laius 5,krediit 1,5: **max kahju 350,kasum 150**.
4. Delta 0,5 ja S+2, vega 0,12 ja IV−10 pp: **−0,20 ühiku lokaalne hinnang**, gamma/theta puuduvad.
5. Straddle K100,kulu 12: **tasuvus 88 ja 112**, mitte 100.
6. Covered call S₀100,K105,c 3,S50: **−4700**; kate puudutab tarnimist.
7. Riskieelarve 100,lepingu risk 350: **0 lepingut**.
8. p 90%,võit 10,kahju 120: **E=−3** enne kulusid.
9. Miks kalender vajab IV-eeldust? **Pikk jalg on esimesel tähtajal endiselt optsioon, mitte lõppväljamakse.**
10. Kas nullsumma tähendab 50% võite? **Ei:90%×1−10%×9=0**, kuigi võidumäär 90%.

## Mikroõpetuse ülesanne

Vali üks küsimus. Selgita seda 60–90 sekundiga inimesele, kes ei tea optsioonidest midagi. Lisa üks arvuline näide ja üks analoogia piirang. Paariline peab suutma pärast seletust ise muuta üht sisendit ning ennustada, kuidas tulemus muutub.
