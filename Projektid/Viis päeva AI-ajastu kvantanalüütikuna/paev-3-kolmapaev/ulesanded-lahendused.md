# Päev 3: kontrollküsimused ja ülesanded

Proovi enne vastuse lugemist iseseisvalt. Baastase: mõisted; rakendustase: arvutus ja kood; süvatase: otsuse piirangud.

## Kontrollküsimus 1

**Miks skaala õppimine testandmetelt on probleem?**

Vastus: Tulevase jaotuse keskmine ja hajuvus mõjutavad mudeli sisendit. Teisenduse parameetrid peavad tulema treeningust.

## Kontrollküsimus 2

**Kas 60% suunatäpsus on piisav investeerimiseks?**

Vastus: Ei. Vaja on võitude ja kaotuste suurust, kulusid, käivet ning riski.

## Kontrollküsimus 3

**Kuidas erinevad mets ja boosting?**

Vastus: Mets keskmistab juhuslikustatud puid; boosting lisab järjest parandusi senise ansambli vigadele.

## Kontrollküsimus 4

**Miks `train.exit < signal` on rangem kui varasem signaalikuupäev?**

Vastus: Varasema signaaliga silt võib veel tulevikus lõppeda. Treenimiseks peab kogu hoideperiood olema teada.

## Kontrollküsimus 5

**Kas RAG kaotab hallutsinatsioonid?**

Vastus: Ei. Ka otsing võib eksida ja mudel võib allikat valesti tõlgendada. Vaja on viite-, aja- ja arvutuskontrolle.

## Praktiline ülesanne 1: Arvutus: tabamus ja kasum

[PRAKTIKA] 100 tehingust 55 võidavad 1 euro ja 45 kaotavad 1,5 eurot. Iga tehing maksab 0,1 eurot. Leia kogutulemus.

**Lahendus:** `55*1 - 45*1.5 - 100*.1 = -22.5` eurot. Oodatav keskmine on −0,225 eurot tehingu kohta. 55% täpsus ei kata ebasoodsat väljamakset ja kulu.

## Praktiline ülesanne 2: Otsus ja kood: milline mudel valida?

[PRAKTIKA] Mudel A RMSE on 0,04, netotootlus 6%, käive 0,2; mudel B RMSE 0,035, netotootlus 5%, käive 1,2. Risk on sarnane. Koosta väike tabel ja otsus.

**Lahendus:** `pd.DataFrame({"mudel":["A","B"],"RMSE":[.04,.035],"neto":[.06,.05],"kaive":[.2,1.2]})`. B parem RMSE ei õigusta kasutuselevõttu. A on praegu majanduslikult eelistatav kandidaat; erinevuse ebakindlus ja päris täitmiskulu tuleb siiski kontrollida. Ära vali B-d tehnoloogia nime järgi.

## Vanemkvandi kriitiline küsimus

Kas parem tulemus püsib sama käibe, riski ja kulurežiimi juures?

Hea vastus nimetab kontrollitava tingimuse ja selle, millised andmed selle kontrollimiseks vajalikud on. Kehv vastus kaitseb mudelit lihtsalt sellepärast, et selle peale kulus palju aega.

## Enesehindamine

Anna iga kontrollvastuse eest 0–2 punkti ning kummagi praktilise ülesande eest 0–5 punkti. 16/20 näitab head alust; edasi minekuks peab ajastuse või tõendi piiri puudutav vastus siiski olema sisuliselt õige. Õpetaja selgitab keerulise vea enne järgmist päeva.
