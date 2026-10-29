# 20 keerulisemat foorumi- ja väitlusküsimust

[Tagasi](../README.md)

Eesmärk on kontrollida argumenti, mitte inimest nurka suruda. Ühe minuti vastused on suulise selgituse põhitekstid; lisa kõrvale näite arvutus.

## 1. Kas delta 0,30 tähendab 30% võimalust kasumisse jääda?

**15 sekundi vastus:** Ei. Delta pole kasumitõenäosus.

**1 minuti selgitus:** ITM-tõenäosus ja preemiast üle saamise tõenäosus on eri sündmused; BSM-is pole isegi delta ja ITM-tõenäosus täpselt samad. Võrdle sündmusi S>K ja S>K+c. Euroopa dividendideta BSM-is on delta N(d 1), kuid riskineutraalne ITM-tõenäosus N(d 2). Tegeliku maailma tõenäosus vajab veel hinnadünaamika eeldust. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** K=100, c=5: ITM nõuab S>100, tähtaja kasum S>105.

**Vastuväide:** „Delta on täpne võiduprotsent.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Mõnes praktikas kasutatakse deltat jämeda ITM-lähendina, mitte garantiina.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 2. Miks nullsummaline leping ei tõesta kõigi strateegiate võrdset eelist?

**15 sekundi vastus:** See seob sama lepingu vastaspooled, mitte erinevate riskide jaotusi. Nullsumma ei võrdsusta strateegiaid.

**1 minuti selgitus:** Tegeliku maailma riskipreemiad, hinnad ja kulud võivad eri strateegiate ootusi muuta. Ühe lepingu kahe vastaspoole summaks tuleb enne kulusid null, sõltumata jaotusest. See on arvestuslik identsus. Oodatavate tulemuste võrdsustamiseks eri lepingute vahel oleks vaja palju tugevamaid hinna- ja jaotuseeldusi. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Sama call’i ostja +200 tähendab müüjale −200 enne kulusid; see ei määra teise put’i oodatavat tulemust.

**Vastuväide:** „Kõigi strateegiate pikaajaline kasum on sama.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Riskineutraalne hinnastus erineb tegelikust tootlusprognoosist.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 3. Kas võitude ja kahjude kaalutud pindade võrdsus tähendab 50% võite?

**15 sekundi vastus:** Ei, see tähendab sobiva definitsiooni korral null ootust. Tõenäosusega kaalutud pind pole võidumäär.

**1 minuti selgitus:** Tulemuse suurus ja tõenäosus on erinevad; väike sagedane võit võib tasakaalustuda suure harva kahjuga. Võiduprotsent mõõdab positiivsete tulemuste sagedust, kaalutud pind aga tulemuse suuruse ja tõenäosuse korrutisi. Võrdsed kaalutud pluss- ja miinuspinnad ei määra sündmuste sagedust. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** 90% +1 ja 10% −9: E=0, võidumäär 90%.

**Vastuväide:** „Null ootus tähendab võrdselt võite ja kaotusi.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Järeldus eeldab normaliseeritud jaotust ja õigesti kaalutud P/L-i.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 4. Millal covered call ja cash-secured put on võrreldavad?

**15 sekundi vastus:** Sama strike’i, tähtaja ja korrektse rahastuse korral. Sama kuju vajab samu tingimusi.

**1 minuti selgitus:** Put-call parity seob terminalrahavood; erinevad strike’id või dividendieelne täitmine rikuvad lihtsa võrdluse. Kirjuta mõlema poole terminalväärtus min(S,K). Seejärel võrdle algseid rahavooge parity abil. Kui jätad sularaha, dividendi või intressi välja, võrdled erineva kapitalibaasiga positsioone. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** S=K=100, c=p=6: mõlema netokulu 94 ja terminalväärtus min(S,100).

**Vastuväide:** „Kõik covered call’id on kõikide short put’idega samad.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Kontrolli ka kulusid, dividende ja exercise-stiili.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 5. Miks calendar spread’i tasuvuspiir pole universaalne?

**15 sekundi vastus:** Pikk jalg on lühikese lõppedes endiselt turuhinnaga optsioon. Kaks tähtaega pole üks payoff.

**1 minuti selgitus:** Allesjäänud hind sõltub IV-st, ajast ja intressist, mitte ainult sisemisest väärtusest. Esimese tähtaja hetkel on ühe jala väärtus lõplik ja teise oma hinnanguline. Järelejäänud optsiooni IV muutus liigutab kogu kasumikõverat. Ühest püsivast tasuvuspiirist rääkimine peidab selle eelduse. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** 30/60 päeva calendar’i pika jala väärtus 30. päeval muutub IV 15% ja 30% vahel.

**Vastuväide:** „Kõik jalad võib esimesel tähtajal sisemiseks väärtuseks asendada.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Kui mõlemad lõpuks lõppevad, peab kirjeldama ka vahepealseid rahavooge.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 6. Miks delta-neutraalne positsioon võib palju kaotada?

**15 sekundi vastus:** Gamma, vega, theta ja hüpped jäävad. Null delta pole null risk.

**1 minuti selgitus:** Hetkeline suunatasakaal ei säili tingimata ning IV võib muuta mõlema jala väärtust. Suunariski nullimine eemaldab ainult esimese järgu hinnamõju antud hetkel. Järgmine väike hinnasamm muudab deltat gamma kaudu. IV muutus võib isegi ilma alusvara liikumiseta tekitada suure kahju. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Short straddle’i algdelta ligikaudu 0, kuid suur tõus tekitab suure kahju.

**Vastuväide:** „Neutraalne tähendab riskivaba.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Neutraalsus vajab ajatemplit ja mõõdiku nimetust.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 7. Kuidas võib 90% võitude korral raha kaotada?

**15 sekundi vastus:** Harvad kahjud võivad olla keskmistest võitudest suuremad. Võidumäär ei ole eelis.

**1 minuti selgitus:** Tähtis on tõenäosusega kaalutud summa, mitte plussmärkide arv. Palu vastasel esitada kogu tehingutulemuste jaotus ja valimi pikkus. Kui andmed ei sisalda kriisi, võib suur võidumäär olla lihtsalt sabariski puudumine valimist. Ka usaldusvahemik p hinnangule on oluline. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** 0,9×10−0,1×120=−3.

**Vastuväide:** „Rohkem võite kui kaotusi tähendab kasumlikkust.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Kahe tulemuse mudel on lihtsustus; päriselt vaata kogu jaotust.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 8. Kas iga deebetiga strateegia maksimaalne kahju on deebet?

**15 sekundi vastus:** Ei, näiteks ratio spread võib maksta deebetit ja jääda katmata. Deebet piirab ainult määratletud paketti.

**1 minuti selgitus:** Rahavoo märk ei määra väljamakse sabade kuju; loe lepingukoguseid. Rahavoo märgilt ei saa lugeda riskifunktsiooni tuletist suurtel hindadel. Loenda call’ide netokogus: kui müüdud call’e on rohkem kui ostetuid ja katvaid aktsiaid, kasvab kohustus ilma piirita. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** 1 long call ja 2 short call’i jätavad ülespoole ühe katmata kohustuse.

**Vastuväide:** „Makstud netopreemia tähendab alati piiratud riski.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Long-only või korrektse debit-vertikaali puhul võib deebet olla kahjupiir.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 9. Kas positiivne theta tagab müüjale kasumi?

**15 sekundi vastus:** Ei, see isoleerib ainult aja mõju. Aeg pole garanteeritud tulu.

**1 minuti selgitus:** Negatiivne gamma või vega võib turu muutumisel theta-eelise kiiresti ületada. Theta on osatuletis fikseeritud alusvara ja IV korral. Tegelik kauplemispäev ei fikseeri neid sisendeid. Kui tulu nimetatakse theta-korjeks, tuleb kõrvale kirjutada, milline gamma- ja hüpperisk selle eest võeti. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Theta +5 USD päevas, hinnahüppe kahju 300 USD.

**Vastuväide:** „Müüjale makstakse riskivaba päevatulu.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Kehtib muu sama tundlikkushinnanguna.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 10. Kas wheel teeb aktsia kahjumist preemiatulu?

**15 sekundi vastus:** Ei, kogu aktsia- ja optsioonitulemus tuleb kokku liita. Wheel ei kustuta ostuhinda.

**1 minuti selgitus:** Uute call’ide müük võib tuua raha, kuid vähendab taastumise tõusupotentsiaali. Wheel’i hindamine nõuab kogu tsükli omakapitali, mitte ainult positiivseid optsioonilaekumisi. Kui aktsia on sügavas miinuses, võib vana ostuhinna juures call’i preemia olla väike; madalam strike lukustab taastumiskahju. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Ost 95, put’i krediit 3, call’i krediit 2, lõpphind 70: −20 ühikut.

**Vastuväide:** „Uus preemia tähendab vana kahju kadumist.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Tulemuseks on teekonnast sõltuv protsess, mitte püsiv tootlusmäär.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 11. Miks piiratud riskiga spread võib vajada lisaraha?

**15 sekundi vastus:** Üks jalg võib täituda enne teist. Täitmine võib jalad lahutada.

**1 minuti selgitus:** Terminalne kompensatsioon ei pruugi automaatselt tekkida samal hetkel; aktsiad ja raha tuleb hallata. Lepingu kahjupiir kirjeldab koos lõpetatud jalgu. Operatiivne rahavajadus kirjeldab raha ja aktsiaid eri hetkedel. Need on eri mõõdikud, mistõttu korrektne terminalgraafik ei asenda maakleri protsessi tundmist. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Short put K100 assignment tähendab 10000 USD ostu, long K95 jääb esialgu alles.

**Vastuväide:** „Kaitsev jalg lahendab kõik automaatselt.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Maakleri netting ja menetlused erinevad; kontrolli konkreetset protsessi.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 12. Miks short call’i risk suureneb mõnikord dividendi eel?

**15 sekundi vastus:** Ostjal võib olla kasulik õigust varakult kasutada. Dividend muudab otsust.

**1 minuti selgitus:** Dividendi saamise kasu tuleb võrrelda loovutatava välise väärtuse ja rahastuskuluga. Täitmise majanduslik kasu sõltub dividendist, allesjäänud ajaväärtusest ja strike’i varasema maksmise kulust. Dividendist suurem ajaväärtus võib täitmist pärssida. Lihtne ühe numbri reegel on seega ainult esmane kontroll. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Väline väärtus 0,1, dividend 1 võib muuta täitmise atraktiivseks.

**Vastuväide:** „Assignment toimub ainult tähtajal.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** See puudutab Ameerika tüüpi call’i; dividend üksi pole piisav täpne reegel.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 13. Kas odav 0DTE on tingimata väiksema riskiga?

**15 sekundi vastus:** Ei, täielik kaotus võib saabuda väga kiiresti. 0DTE koondab otsused.

**1 minuti selgitus:** Lühike aeg ja ATM gamma muudavad hinna tundlikuks; protsentuaalne risk võib olla suur. 0DTE on allesjäänud aeg, mitte konkreetne strateegia. Sama päeva long call’il on piiratud preemiarisk, katmata short call’il piiramatu hinnasaba. Väike lepingu hind võib ahvatleda kogust suurendama. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** 0,5 preemia M100 tähendab 50, mis võib samal päeval täielikult kaduda.

**Vastuväide:** „Odav hind tähendab aeglast või väikest riski.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Rahaline kahju sõltub ka lepingute arvust ja müüdud kohustustest.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 14. Miks BSM-i hind ei pruugi olla turul teostatav?

**15 sekundi vastus:** Mudel lihtsustab turgu ning ei sisalda sinu täitmiskulu. Mudel pole hinnapakkumine.

**1 minuti selgitus:** Püsiv IV, pidev kauplemine ja hüpete puudumine ei kirjelda kogu tegelikkust. BSM-i hinnamudel võib anda sisemiselt kooskõlalise pinna ja siiski turust erineda. Volatiilsusnaeratus näitab, et ühe konstandiga sigma pole kõigi strike’ide jaoks piisav. Turuhinna erinevus pole automaatselt arbitraaž. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Mudel 3,00, bid/ask 2,70/3,30: ost 3,00 pole garanteeritud.

**Vastuväide:** „Mudeli väljund on õige hind, turg eksib.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Kasuta mudelit võrdluse ja tundlikkuste, mitte kindla täitmisena.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 15. Kas sünteetilise forward’i theta on alati null?

**15 sekundi vastus:** Ei, rahastamise ja dividendide mõju võib jääda. Intress ei kao sünteetikast.

**1 minuti selgitus:** Gamma ja vega tühistumine ei tähenda kõigi ajaga seotud rahavoogude kadumist. Sama strike’i ja tähtaja call’i ning put’i gamma ja vega võivad tühistuda. Kuid parity paremal poolel on diskonteeritud strike ja dividendikomponent, mille väärtus ajas muutub. „Theta puudub” nõuab lisaeeldusi. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** C−P=S−K exp(−rT) dividendideta mudelis.

**Vastuväide:** „Sünteetika on kõigi kreeklaste suhtes immuunne.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** r=q=0 lihtsustuses kaob see konkreetne carry-mõju.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 16. Miks positiivne brutotulemus ei taga netokasumit?

**15 sekundi vastus:** Spread, komisjon ja täitmisnihe vähendavad tulemust. Kulud võivad eelise ära süüa.

**1 minuti selgitus:** Väikese tehingueelise korral võib teostus moodustada suure osa oodatavast tulust. Väike keskmine teoreetiline eelis võib haihtuda halva täitmisega. Katseta stresskuluga, mitte ainult ajaloolise keskmise spread’iga. Likviidsus kipub olema kehvem just olukorras, kus tahad kiiresti väljuda. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Bruto E=4 USD, kulud 6 USD: neto −2.

**Vastuväide:** „Hea backtest on automaatselt kaubeldav.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Kulud sõltuvad kogusest, turuolust ja korraldusest.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 17. Miks kümme short put’i pole tingimata hajutatud?

**15 sekundi vastus:** Alusvarad võivad kriisis ühiselt langeda. Riskid võivad kokku kuhjuda.

**1 minuti selgitus:** Erinevad nimed ei võrdu sõltumatud tegurid; sektor ja turubeta ühendavad positsioone. Korrelatsioon tavaperioodil ei pruugi kirjeldada ühist kriisilangust. Sama majandusteguri müümine kümne aktsia kaudu ei ole kümme sõltumatut panust. Vaata portfelli ühiseid stresskahjumeid. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Kümme tehnoloogiaaktsiat langevad sama uudise järel.

**Vastuväide:** „Rohkem tehinguid tähendab automaatselt väiksemat riski.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Hajutamist hinnatakse korrelatsiooni ja stressiga.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 18. Miks trendisüsteemi ei saa automaatselt optsioonidele üle kanda?

**15 sekundi vastus:** Optsioon lisab strike’i, tähtaja ja IV valiku. Hea lugu vajab testi.

**1 minuti selgitus:** Aktsiasignaali eelis ei pruugi katta preemiat ja kulusid; valikuid on rohkem ning üleoptimeerimise oht kasvab. Aktsiastrateegia tulemused ei sisalda optsioonide strike’i- ja tähtajavalikut ega IV-d. Need lisavalikud võivad andmetesse sobitamise riski kasvatada. Hoia hindamise periood eraldi ja testi põhjendatud lihtsat baasvarianti. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Aktsiasignaal +2%, aga OTM call vajab tasuvuseks +8%.

**Vastuväide:** „Kasumlik aktsiameetod garanteerib kasumlikud call’id.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Testi väljaspool treeningperioodi, realistlike hinnavahedega.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 19. Kas positiivne ootus tähendab, et tüüpiline tehing võidab?

**15 sekundi vastus:** Ei. Oodatav tulemus pole mediaan.

**1 minuti selgitus:** Harv suur võit võib teha keskmise positiivseks, kuigi enamik üksiktehinguid kaotab. Keskmine võib olla positiivne mõne harva suure võidu tõttu, samal ajal kui kõige tavalisem tulemus on kaotus. See mõjutab nii positsiooni suurust kui ka psühholoogilist taluvust. Mõlemad pooled vajavad kapitali, et jaotuse tulemusi üle elada. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** 90% −1 ja 10% +15: E=+0,6, mediaan −1.

**Vastuväide:** „Positiivne E tähendab üle poole võite.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Tulemuse usaldus sõltub sabatõenäosuse hinnangu kvaliteedist.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

## 20. Kas indeksiput garanteerib üksikaktsiaportfellile põranda?

**15 sekundi vastus:** Ei, portfell võib indeksist erinevalt liikuda. Baasisrisk jääb.

**1 minuti selgitus:** Maanduse alusvara pole sama mis kaitstav vara; korrelatsioon pole kindel lepinguline seos. Optsiooni täpne lepinguline kaitse puudutab tema enda alusvara. Portfelli maandamine teise varaga vajab mudelit nende koosliikumisest. Mudeliviga võib tekkida ka siis, kui optsioon ise maksab täiesti korrektselt. Arutelu lahendamiseks tuleb kõigepealt kokku leppida, kas räägime ühe lepingu lõpptähtajast, kogu portfellist või vahepealsest turuväärtusest. Vastasel juhul võivad kaks näiliselt vastuolulist vastust kirjeldada hoopis eri küsimusi.

**Arvuline põhjendus:** Portfell −30%, indeks −10%: kaitse võib olla ebapiisav.

**Vastuväide:** „Korrelatsioon 0,9 tähendab 90% garanteeritud kaitset.” Selle hindamiseks palu sõnastada konkreetsed eeldused ning näidata kõiki rahavooge, mitte üksikut võidukat tulemust.

**Piirang ja täpsustus:** Sama alusvara put annab täpsema lepingu põranda kindlale kogusele.

**Jätkuküsimus:** Milline andmestik või vastunäide paneks sind oma väidet muutma?

