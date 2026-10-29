# II. Miks optsiooni hind muutub?

[Tagasi](../README.md) · [Kreeklased](../03-kreeklased/oppetukk.md)

[RAAMAT] Peatükid 4–6 ja 14 (PDF lk 37–70, 144–152), lisad A ja D (176–183, 198–205) seovad hinna aja, volatiilsuse ja alusvara liikumisega.

## 1. Mida peab mõistma?

- Eristad sisemist ja välist väärtust.
- Eristad hinnasuunda, liikumise suurust ja selle toimumise aega.
- Oskad selgitada IV languse mõju.
- Arvestad bid’i, ask’i ja täidetava hinnaga.

## 2. Intuitiivne selgitus

[SELGITUS] Optsioon annab võimaluse saada kasu tulevasest soodsast hinnast ja loobuda ebasoodsast tehingust. Suurem võimalike tulemustega vahemik võib olla õiguse ostjale väärtuslik. Kuid turg nõuab selle võimaluse eest juba hinda. Kasulik tulemus ja kasulikult ostetud õigus on erinevad asjad.

## 3. Analoogia

[ANALOOGIA] Kontserdipiletite broneerimisõigus homseni on vähem paindlik kui õigus järgmise kuuni. Pikema akna sees võib tulla rohkem soodsaid võimalusi. Piirang: optsiooni hinnas mõjutavad võrdlust intress, dividend, eri tähtaegade IV ja täitmisviis. Euroopa put’i puhul ei saa väidet „pikem on alati kallim” üldreegliks teha.

## 4. Mehhanism

| Muutus, muu sama | Tavaline long call | Tavaline long put | Miks? |
|---|---|---|---|
| S suureneb | Kallineb | Odavneb | Ostuõigus kasulikum, müügiõigus vähem kasulik |
| K suureneb | Odavneb | Kallineb | Osta kallimalt vähem kasulik; müüa kallimalt kasulikum |
| IV suureneb | Üldjuhul kallineb | Üldjuhul kallineb | Valikuõigus saab laiemast jaotusest kasu |
| Riskivaba intress suureneb | BSM-is kallineb | BSM-is odavneb | Tulevase täitmishinna nüüdisväärtus väheneb |
| Oodatav dividend suureneb | Tavaliselt odavneb | Tavaliselt kallineb | Ex-dividend hinnalangus on ootustes |
| Aeg möödub | Sageli odavneb | Sageli odavneb | Väheneb allesjäänud võimalus; erandeid on |

Tabel pole üheaegselt muutuva turu ennustus. IV ehk implied volatility saadakse optsiooni hinnast mudeli abil tagasi arvutades; see ei ole kõigi turuosaliste ühine kindel prognoos. Ajalooline volatiilsus mõõdab juba toimunud kõikumist. Realiseerunud volatiilsus kirjeldab valitud perioodil tegelikult toimunut.

Nõudlus ja pakkumine mõjutavad tehinguhinda. IV on üks viis seda hinda väljendada, mitte hinnast sõltumatu nähtamatu jõud.

## 5. Arvulised näited

[NÄIDE] Call K=100, S=104, hind 6. Sisemine väärtus on 4 ja väline väärtus 2. Kui S jääb tähtajani 104 juurde, on lõppväärtus 4: 2 kaob.

Enne uudist: hind 5, delta 0,50, vega 0,12 ühe IV protsendipunkti kohta. Aktsia tõuseb 2, IV langeb 10 protsendipunkti. Väikese muutuse lähendus annab +1−1,20=−0,20; hind ligikaudu 4,80 enne gamma ja theta arvestamist. Hinnasuund oli õige, tehing võib olla miinuses. Kümnepunktine IV muutus on juba piisavalt suur, et lokaalne lähendus vajaks kontrolli.

Bid=2,80 ja ask=3,20. Kohe ask’ist ostes ja bid’i müües kaotad 0,40×100=40 USD enne komisjonitasu. Keskhind 3 ei tähenda, et 3-ga saab tehingu teha.

## 6. Vajalik matemaatika

[MATEMAATIKA] Väikese volatiilsuse ja lühikese tähtaja ATM-lähendus, S=K, r=q=0:

$$C\approx P\approx\frac{S\sigma\sqrt T}{\sqrt{2\pi}}.$$

Näiteks S=100, σ=0,20 ja T=30/365 annavad ligikaudu 2,29. 120 päeva korral ligikaudu 4,57. Neljakordne aeg ei anna neljakordset hinda. See on mudelilähendus, mitte hinnapakkumine.

Aegumise väljamakse ei sisalda enam ajaväärtust. Enne aegumist vajatakse hinna saamiseks kas turuandmeid või hinnamudelit. [Python 09](../python/09_theta.py) näitab ATM-hinna mittelineaarset vähenemist fikseeritud S ja IV korral.

## 7. Praktiline kasutamine

Enne uudist küsi: kui suur liikumine on hinnas? Kui ostad straddle’i 8 eest hinnal 100, on tähtaja tasuvuspiirid 92 ja 108. Liikumine 106-ni võib tunduda suur, aga ei kata preemiat. Enne tähtaega tuleb mõlema jala allesjäänud turuväärtus siiski juurde arvestada.

## 8. Riskid ja väärarusaamad

Kõrge IV ei tõesta ülehinnatust: sündmuse risk võibki olla suur. Madal IV ei tõesta odavust. Väiksem nominaalne preemia võib peita väikest kasumitõenäosust. Tehingumaht ja avatud lepingute arv ei taga kitsast hinnavahet ega täitmist sinu koguses. Eri strike’ide IV võib erineda (skew); eri tähtaegadel on oma IV-struktuur.

## 9. Põhimõtted

[PÕHIMÕTE] Hinda võimalust koos hinnasildiga. Kasumi jaoks peab realiseeruv olukord olema ostuhinna suhtes piisavalt soodne. Keskhind pole lubadus.

## 10. Kontrollküsimused

1. **Kas 6-eurone optsioon on kallim ost kui 1-eurone?** Nominaalselt jah; suhtelist soodsust ei saa ilma strike’i, aja ja riskita otsustada.
2. **Miks uudise järel IV langeb?** Osa teadmatusest on lahendatud; hinnas olnud sündmuserisk väheneb.
3. **Kas ajaväärtus sõltub ainult ajast?** Ei; ka S, IV, intress ja dividendid mõjutavad seda.
4. **Kas aktsia suurem kõikumine tagab call’i kasumi?** Ei; tähtaja lõpphind, ostuhind ja müügiaeg määravad tulemuse.
5. **Kas suur maht kõrvaldab spread’i?** Ei; kontrolli hetke bid’i/ask’i, koguseid ja täitmist.

## 11. Õpetaja selgitus

Mõelge kahest hinnast: mida saaks lepingust kätte kohe ja mida väärt on veel allesjäänud võimalus. Kui ostuõigus lubab osta 100-ga ja aktsia maksab 104, on kohe kasutatav väärtus 4. Kui leping maksab 6, maksame veel 2 võimaluse eest, et tulevik muutub soodsamaks. See 2 ei ole ainult kell: ka teadmatus ja võimalikud hinnahüpped loevad. Kui tähtajal on hind ikka 104, saame lepingust 4, mitte 6. Seetõttu võib hea hinnasuuna prognoosiga raha kaotada. Õige küsimus ei ole ainult „kas tõuseb?”, vaid „kas tõuseb piisavalt, õigel ajal ja minu makstud hinnaga võrreldes?”.
