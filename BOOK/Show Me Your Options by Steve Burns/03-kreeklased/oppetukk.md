# III. Kreeklased: mida su positsioon kardab?

[Tagasi](../README.md) · [Strateegiad](../04-strateegiad/README.md)

[RAAMAT] Theta, vega ja delta on peatükkide 4–6 keskmes (PDF 37–70). [TÄIENDUS] Gamma ja rho süstemaatiline käsitlus, ühikute kontroll ning allolevad arvutused laiendavad raamatu põhirõhku. [OIC ametlik alus](../allikad.md).

## 1. Mida peab mõistma?

- Tõlgendad viit tundlikkust koos ühikutega.
- Vahetad ostja ja müüja korral märgi õigesti.
- Summeerid portfelli tundlikkused.
- Eristad lokaalset hinnangut kogu stsenaariumist.

## 2. Intuitsioon ja 3. analoogia

[SELGITUS] Kreeklased vastavad küsimusele: kui üks sisend natuke muutub ja teised jäävad samaks, kui palju muutub hind?

[ANALOOGIA] Autos on kiirus, kiirendus, kütusekulu ja rehvirõhk eri näidikud. Üks näidik ei asenda teisi. Delta on hinna „kiirus” alusvara suhtes, gamma selle kiiruse muutumine. Piirang: auto füüsikaline kiirus pole turuprognoos; kreeklased arvutatakse mudelist ja muutuvad turuoludega.

## 4. Mehhanism ja võrdlustabel

| Mõõdik | Mõõdab | Siin kasutatav ühik | Long call | Long put |
|---|---|---|---|---|
| Delta Δ | Hinnamuutus S muutudes | USD optsiooni kohta / 1 USD alusvara | Positiivne | Negatiivne |
| Gamma Γ | Delta muutus S muutudes | Delta muutus / 1 USD alusvara | Positiivne | Positiivne |
| Theta Θ | Hinnamuutus aja möödudes | USD / kalendripäev | Sageli negatiivne | Sageli negatiivne |
| Vega ν | Hinnamuutus IV muutudes | USD / 1 IV protsendipunkt | Positiivne | Positiivne |
| Rho ρ | Hinnamuutus intressi muutudes | USD / 1 intressi protsendipunkt | BSM-is positiivne | BSM-is negatiivne |

Müüja tundlikkused on sama lepingu ostja omad vastasmärgiga. Kordajaga M ja n lepinguga korruta nM-ga; n on lühikese positsiooni puhul negatiivne. Kombinatsioonis võivad märgid muutuda hinna ja aja funktsioonina.

### Delta: kui palju saan hinnaliikumisest?

**Intuitsioon ja analoogia.** Delta 0,50 tähendab hetkel ligikaudu poole aktsialiikumise saamist, nagu pooleldi avatud kraan. Kraaniava ise muutub: see on gamma.

**Risk ja näide.** S tõuseb 2; delta 0,50 → ligikaudu +1 ühik. M=100 korral +100 USD. Müüjal −100. Put’i delta −0,40 korral annab sama hinnatõus ligikaudu −0,80.

**Muutumine.** Tähtaja lähenedes on ITM call’i delta sageli 1 lähedal, OTM call’il 0 lähedal. ATM-i lähedal võib muutus olla järsk. Dividendidega mudelis ja eksootiliste lepingute puhul vajavad piirid täpsustamist.

**Piirang.** Delta ei mõõda IV ega aja mõju. Delta 0,30 ei tähenda automaatselt 30% kasumitõenäosust.

**Põhimõte ja küsimus.** Delta on hetke tundlikkus. Kas delta 0,50 tagab +5, kui aktsia tõuseb 10? Ei; delta muutub ja teised sisendid võivad muutuda.

### Gamma: miks risk võib kiireneda?

**Intuitsioon ja analoogia.** Gamma kirjeldab rooli tundlikkust: väike lisaliigutus võib muuta suunda üha rohkem. See pole lihtsalt eraldi kasumiallikas.

**Risk ja näide.** Delta 0,50 ja gamma 0,04; S tõuseb 3 → uus delta ligikaudu 0,62. Long call saab tõusul suurema delta; short call’i negatiivne delta muutub absoluutväärtuselt suuremaks. Long put’i negatiivne delta läheneb tõusul nullile.

**Muutumine.** Lühikese tähtajaga ATM-lepingul võib gamma olla suur. Sügaval ITM/OTM piirkonnas on see sageli väike. Tähtajal on väljamakse murdepunkt: strike’i juures ei saa kasutada tavalist siledat tuletist.

**Piirang.** Püsiva gammaga suurte hüpete arvutamine on ebatäpne. Positiivne gamma ei tähenda tasuta kasumit: selle eest makstakse sageli theta kaudu.

**Põhimõte ja küsimus.** Väike tänane delta võib muutuda suureks homseks riskiks. Kas delta-neutraalne short straddle on ohutu? Ei, tal on negatiivne gamma ja vega.

### Theta: mida teeb üks möödunud päev?

**Intuitsioon ja analoogia.** Õigus on nagu aeguv broneering, mille tulevaste võimaluste aken lüheneb. Piirang: broneeringu väärtus ei vähene alati ühtlases tempos; ka turg muutub.

**Risk ja näide.** Theta −0,04 päevas → kolme päeva lokaalne hinnang −0,12 ühikut ehk −12 USD lepingult. Müüjal oleks muu samana püsimisel +12.

**Muutumine.** ATM-optsiooni ajakadu võib tähtaja lähedal kiireneda. Kaugel OTM võib väärtus olla juba peaaegu null. Sügava ITM put’i theta võib intressi mõjul olla positiivne. Platvorm võib kasutada erinevat päeva- ja aastakonventsiooni.

**Piirang.** Reedest esmaspäevani ei saa universaalselt lubada täpselt 3×reedest thetat: turu hinnastus ja IV muutuvad. Theta pole kontole eraldi makstav intress.

**Põhimõte ja küsimus.** Ajaeelis kehtib tingimustel. Kas müüja võidab alati ühe päeva möödudes? Ei, hinnahüpe võib ajakadu kordades ületada.

### Vega: mida maksab teadmatus?

**Intuitsioon ja analoogia.** Kindlustuse hind tõuseb, kui tajutav ebakindlus suureneb. Piirang: vega on tuletisinstrumendi mudelitundlikkus, mitte kindlustusmatemaatiline kahjutõenäosus.

**Risk ja näide.** Vega 0,15; IV 20%-lt 24%-le = +4 protsendipunkti. Hinnang +0,60 ehk +60 USD. Müüjale −60. 20%→24% on suhteliselt 20% tõus, aga vega valemis kasutame 4 punkti.

**Muutumine.** Pikema tähtajaga ja ATM-lepingute vega on sageli suurem. Spread’i jalgadel on eri vega; erinevate tähtaegade IV ei pruugi koos liikuda.

**Piirang.** IV muutuse mõju ei ole suurte sammude puhul lineaarne. Kaua hoitud optsiooni lõppväljamakse sõltub lõpphinnast, mitte eraldi IV-numbrist.

**Põhimõte ja küsimus.** Sa võid prognoosida suunda õigesti ja osta ebakindlust liiga kallilt. Kas kõrge IV tähendab head müüki? Ainult IV tasemest seda järeldada ei saa.

### Rho: tulevase raha tänane hind

**Intuitsioon ja analoogia.** Hiljem makstav 100 pole sama mis täna makstav 100. Call lükkab strike’i maksmise tulevikku; put’i tulevase müügitulu tänane väärtus sõltub intressist.

**Risk ja näide.** Call’i rho 0,08; intress 3%-lt 4%-le → +0,08 ehk +8 USD. Put’i rho −0,07 → −7 USD. Müüja märgid pöörduvad.

**Muutumine.** Pika tähtaja korral on mõju sageli suurem. Lühikese tähtaja puhul võivad delta ja vega domineerida, kuid see ei tee rhod olematuks.

**Piirang.** Tegelikult võivad koos intressiga muutuda aktsia, dividendiootus ja IV. Rho arvutatakse muu sama eeldusel.

**Põhimõte ja küsimus.** Väike tänane mõju võib pika lepingu puhul oluline olla. Kas intressitõus tagab call’i hinnatõusu? Ei, rho annab ainult ühe komponendi.

## 5. Kümme arvulist kontrollnäidet

Kõik on lokaalsed hinnangud, M=100, kui pole öeldud teisiti.

| Nr | Andmed | Arvutus | Tulemus |
|---|---|---|---|
| 1 | Call Δ=0,50; ΔS=2 | 0,50×2×100 | +100 USD |
| 2 | Put Δ=−0,40; ΔS=−3 | (−0,40)×(−3)×100 | +120 USD |
| 3 | 2 short call’i, Δ=0,60; ΔS=1 | −2×100×0,60 | −120 USD |
| 4 | Δ=0,50; Γ=0,04; ΔS=3 | 0,50+0,04×3 | Uus Δ≈0,62 |
| 5 | Sama, hinna muutus | (0,50×3+0,5×0,04×9)×100 | +168 USD |
| 6 | Θ=−0,04; 3 päeva | −0,04×3×100 | −12 USD |
| 7 | 3 short lepingut; long Θ=−0,05 | −3×100×(−0,05) | +15 USD päevas |
| 8 | ν=0,15; IV +4 pp | 0,15×4×100 | +60 USD |
| 9 | ρ=0,08; intress +0,5 pp | 0,08×0,5×100 | +4 USD |
| 10 | 100 aktsiat + 2 put’i Δ=−0,50 | 100+2×100×(−0,50) | Algdelta 0 |

## 6. Vajalik matemaatika

$$\Delta V\approx\Delta\,\Delta S+\tfrac12\Gamma(\Delta S)^2+\Theta\,\Delta t+\nu\,\Delta IV_{pp}+\rho\,\Delta r_{pp}.$$

Siin Δt on **möödunud kalendripäevad**. Vega ja rho on ühe protsendipunkti kohta. Ristmõjud ja kõrgemad tuletised jäävad välja. See ei ole täpne hinnavalem ega sõltumatute kasumiallikate loend.

## 7. Praktiline kasutamine

Koosta enne tehingut kolm veergu: mis juhtub S tõusul/langusel, IV tõusul/langusel ja ühe päeva möödudes? Seejärel tee ühine stress: S −10%, IV +15 pp. Suure muutuse puhul hinnasta positsioon uuesti, ära korruta lihtsalt tänast deltat kümnega.

## 8. Riskid ja 9. meelespea

[PÕHIMÕTE] Delta näitab suunda, gamma näitab suunariski muutumist, theta aja mõju, vega IV mõju ja rho intressi mõju. Ühikud enne arve. Kreeklased kirjeldavad riskikaarti, mitte võidugarantiid.

## 10. Kümme kontrollküsimust vastustega

1. **Kas delta on kõigi kreeklaste kokkuvõte?** Ei. See hoiab muud sisendid paigal.
2. **Kas short put’i delta on negatiivne?** Ei, tavalise short put’i delta on positiivne, sest long put’i delta on negatiivne.
3. **Kas gamma muudab long put’i deltat tõusul negatiivsemaks?** Ei, positiivne gamma viib selle nulli poole.
4. **Kas ATM 0DTE on aeglane positsioon?** Ei, gamma võib olla väga suur.
5. **Kas theta on alati ostjal negatiivne?** Ei, näiteks mõne sügava ITM put’i puhul on erandeid.
6. **Kas vega 0,10 ja IV +5 pp tähendab +0,005?** Ei, selles ühikus +0,50.
7. **Kas suur vega on alati halb?** Ei, sõltub soovitud riskist ja IV muutusest.
8. **Kas rho on protsendiline tootlus?** Ei, siin absoluutne hinnamuutus ühe intressipunkti kohta.
9. **Kas delta-neutraalne jääb neutraalseks?** Üldjuhul mitte; gamma ja muutuvad sisendid nihutavad deltat.
10. **Kas kümnepäevane kadu on täpselt 10×theta?** Ei, theta ise muutub.

## 11. Õpetaja selgitus

Optsiooni hind on nagu mitme nupuga aparaat. Üks nupp on aktsiahind, teine aeg, kolmas ebakindlus ja neljas intress. Delta ütleb, kui tundlik on hind esimese nupu väikese liigutuse suhtes. Gamma ütleb, kuidas see tundlikkus muutub. Theta kirjeldab kella ja vega ebakindluse nuppu. Kui call’i delta on pool ja aktsia tõuseb kaks dollarit, on esimene hinnang üks dollar kasu. Kuid kui samal ajal IV langeb ja vega mõju on miinus poolteist, võib summa olla negatiivne. Seega ei vaidle delta ja vega teineteisele vastu: nad kirjeldavad eri muudatusi. Ärge õppige ainult märki; öelge alati, millise ühiku kohta number kehtib.
