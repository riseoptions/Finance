# V. Riskijuhtimine ja kaupleja mõtlemine

[Tagasi](../README.md)

[RAAMAT] Peatükid 2, 8, 9, 15 ja 16 (PDF 19–25, 79–105, 153–175) käsitlevad võitude sagedust, harvu suuri kahjusid ning oma meetodi ja riskipiiride vajadust. [TÄIENDUS] Siin eristatakse matemaatilist kahjupiiri operatiivsest kapitalivajadusest.

## 1. Mida peab mõistma?

- Eristad võidumäära ja oodatavat tulemust.
- Arvutad positsiooni suuruse kahju, mitte preemiatulu põhjal.
- Selgitad marginaali, hinnaaukude ja assignment’i riski.
- Eristad tõestatud eelist, simulatsiooni ja head lugu.

## 2. Intuitsioon

[SELGITUS] Risk pole ainult „kui tihti ma kaotan?”. Küsi ka „kui palju, millal ja kas saan seni positsiooni hoida?”. Strateegia võib olla pikaajaliselt teoreetiliselt atraktiivne, kuid sundlikvideerimine võib konto enne tulemuse saabumist lõpetada.

## 3. Analoogia

[ANALOOGIA] Kui kogud iga päev väikest sillaületustasu, kuid vastutad silla kokkuvarisemise eest, ei mõõda viimase kuu laekumised sinu kogu riski. Piirang: tururiskil puudub teadaolev püsiv õnnetussagedus ja kahjud võivad olla korrelatsioonis.

Teine võrdlus: turvavöö vähendab kahju, kuid ei tee ohtlikku kiirust mõistlikuks. Piiratud riskiga spread ei õigusta kogu kontoga panustamist.

## 4. Mehhanism

**Positsiooni suurus.** Määra talutav rahaline kahju, arvuta ühe tervikpositsiooni kahju koos kulude reserviga ja ümarda lepingute arv alla. Kui vastus on null, pole täislepinguga tehing sellesse eelarvesse sobiv.

**Võimendus.** Odavam positsioon võib anda sama esialgse delta väiksema kapitaliga, aga selle protsentuaalne kõikumine on suurem. 300 USD preemia võib täielikult kaduda. Sama lepingute arv ei tähenda sama riski.

**Margin.** Tagatis on maakleri nõutud puhver, mitte maksimaalne kahju. See võib kasvada. Katmata call’i riski ei muuda lõplikuks see, et avamiseks nõuti 2000 USD.

**Kohustuse täitmine.** Short call’i assignment võib tekitada aktsiate tarnimise või lühikese aktsiapositsiooni. Short put võib nõuda strike×kordaja raha. Teise kaitsva jala olemasolu ei tähenda, et maakler selle automaatselt sinu soovitud hetkel kasutab.

**Aegumine.** Strike’i lähedal tekib pin risk: pole kindel, milline aktsiapositsioon kujuneb. Järelturu liikumine, täitmisotsuste tähtajad ja sundsulgemine võivad muuta tulemust. Lõpptähtaja diagramm eeldab kooskõlalist arveldust.

**Likviidsus ja kulud.** Nelja jalaga strateegial on rohkem täitmis- ja kulukohti. Limit order piirab hinda, kuid ei taga täitmist. Jalgade eraldi täitmine võib ajutiselt muuta kaitstud positsiooni katmata riskiks.

## 5. Arvulised näited

[NÄIDE] 90% tehingutest võidab 10 USD, 10% kaotab 120 USD. Keskmine on 9−12=−3 USD enne kulusid. 2 USD kuluga −5. Suur võidumäär ei aita.

10 000 USD konto, õppestsenaariumi riskieelarve 1%=100 USD. 5-laiune credit spread annab 1,50 krediiti; maksimaalne lepinguline kahju on (5−1,50)×100=350 USD. Selle eelarvega sobib **0 lepingut**. 1% pole universaalne soovitus, vaid arvutuse valitud eeldus.

Konto kaotab 20%. Algse väärtuse taastamiseks on vaja 20/80=25% kasvu. Kümme järjestikust 10% kahju allesjäänud kapitalist jätab 0,9¹⁰≈34,87% alles; kümme algkapitali 10% suurust fikseeritud kahju kulutaks kapitali ära. Need on eri reeglid.

## 6. Matemaatika

$$E(X)=pW-(1-p)L-k.$$

Kahe tulemuse mudelis on W võit, L kahju positiivse arvuna ja k keskmine kulu. Tasuvuseks peab $p>(L+k)/(W+L)$. Pideva tulemusega strateegia puhul on $E[\Pi]=\int\Pi(s)f(s)\,ds$; kõige raskem on põhjendada jaotust f.

$$n=\left\lfloor\frac{\text{riskieelarve}}{\text{ühe positsiooni maksimaalne kahju + kulureserv}}\right\rfloor.$$

Katmata piiramatu kahjuga positsioonile ei saa seda valemit rakendada lõpliku tegeliku maksimumiga. Stresskahjum on eraldi hinnang, mitte garantii.

## 7. Praktiline kontrollnimekiri

- [ ] Alusvara, strike, tähtaeg, kordaja, üleantav vara ja arveldus on kontrollitud.
- [ ] Tean, kas avan või sulgen kohustuse.
- [ ] Arvutan nii kõigi jalgade ühise P/L-i kui ka üksiku jala täitmise tagajärje.
- [ ] Tean maksimaalset kahju, krediiti/deebetit ja tasuvuspiire.
- [ ] Kapital katab ka assignment’i ja võimaliku tagatisnõude.
- [ ] Bid/ask, kogused ja kõik tehingukulud on arvestatud.
- [ ] Tean dividendi ja oluliste uudiste kuupäevi.
- [ ] Olen hinnanud S ±10%, IV muutuse ja aja mõju.
- [ ] Sarnased positsioonid ei kuhja sama sektoririski.
- [ ] Mul on enne tähtaega tegutsemise plaan ja maakleri lõikajad.
- [ ] Eristan riskineutraalset hinnamudelit tegeliku maailma tõenäosusprognoosist.
- [ ] Tehingupäevikus on ka põhjendus, mitte ainult tulemus.

## 8. Väärarusaamad

Stop-loss on korraldus, mitte hinnagarantii. Rolling sulgeb vana ja avab uue tehingu; saadud uus krediit ei kustuta realiseeritud kahju. Viis sama sektori short put’i ei anna viit sõltumatut riski. Mõõdukast IV-st hinnatud jaotus võib alahinnata haruldasi hüppeid. Müüja ja ostja sama lepingu P/L-id vastanduvad enne kulusid, kuid eri strateegiate riskipreemiad ja tegelikud oodatavad tulemused ei pea olema võrdsed.

## 9. Põhimõtted

[PÕHIMÕTE] Mõõda halba päeva enne hea kuu lubamist. Tagatis pole kahjupiir. Riskide nimekiri peab muutma positsiooni suurust või tehinguotsust, muidu on see pelk rituaal.

## 10. Kontrollküsimused

1. **Kas 95% võite tõestab eelist?** Ei; vaja on kahjude suurust ja kulusid.
2. **Kas kahel eri aktsial on sõltumatu risk?** Mitte tingimata; kriisis võivad mõlemad langeda.
3. **Kas spread’i max loss on alati konto rahavajadus?** Ei, jalgade täitmine võib ajutiselt nõuda rohkem kapitali.
4. **Kas rollimine päästab kahjumi?** Ei; vana kahjum jääb ning uus risk lisandub.
5. **Kas riskieelarvega 100 saab võtta 350 riskiga lepingu?** Ei, täisarvuline lubatud kogus on null.

## 11. Õpetaja selgitus

Küsime, kumb mäng on parem: võita üheksa korda kümnest või viis korda kümnest? Õige vastus on, et andmeid pole piisavalt. Üheksa kümneeurost võitu annab 90, kuid üks 120-eurone kaotus teeb tulemuseks miinus 30. Sama juhtub optsioonipreemiate kogumisel: laekumiste rida näeb ilus välja, kuni harv kahju selle ületab. Seetõttu arvutame enne tehingut kõigepealt maksimaalse kahju ja konto taluvuse. Kui üks leping on liiga suur, ei tee lepingut väiksemaks ei hea tunne ega stop-loss. Mõnikord on korrektne arvutus just null lepingut. See pole mudeli puudus, vaid mudeli kõige kasulikum vastus.
