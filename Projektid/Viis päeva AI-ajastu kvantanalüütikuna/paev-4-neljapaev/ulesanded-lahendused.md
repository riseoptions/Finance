# Päev 4: kontrollküsimused ja ülesanded

Proovi enne vastuse lugemist iseseisvalt. Baastase: mõisted; rakendustase: arvutus ja kood; süvatase: otsuse piirangud.

## Kontrollküsimus 1

**Kas kolm vara tähendab alati piisavat hajutatust?**

Vastus: Ei. Ühine turu- või sektoririsk võib jääda suureks; vaja on sõltuvusi ja stsenaariume.

## Kontrollküsimus 2

**Kas 12% volatiilsussiht tähendab 12% maksimaalset kaotust?**

Vastus: Ei. See on prognoositud hajuvuse siht, mitte kahjupiir ega garantiiga stop.

## Kontrollküsimus 3

**Miks 30% kaalupiir võib kuu sees rikkuda saada?**

Vastus: Hinnaliikumine muudab kaale. Meie piir kehtib ümberjaotamisel; pidev piir vajaks lisakauplemist.

## Kontrollküsimus 4

**Kas üks stressitest annab maksimaalse võimaliku kahju?**

Vastus: Ei. See annab ühe etteantud stsenaariumi kahju. Long-only võimenduseta varade korral võib kogu riskivara väärtus kaduda.

## Kontrollküsimus 5

**Miks optimeeritud portfell võib lihtsast halvem olla?**

Vastus: Optimeerija kasutab hinnanguid; mürarikkad tootlusootused võivad tekitada äärmuslikke kaale.

## Praktiline ülesanne 1: Arvutus: risk ja stress

[PRAKTIKA] Portfell hoiab A-s 30%, B-s 30%, C-s 20% ning rahas 20%. Šokid −20%, −10%, −5%. Kui suur on kahju 50 000 euro puhul?

**Lahendus:** `(.3*(-.2)+.3*(-.1)+.2*(-.05))*50000 = -5000`. Portfell kaotab 10%. Raha nulltootluse ja kuludeta stsenaariumi eeldusel jääb 45 000 eurot.

## Praktiline ülesanne 2: Otsus ja kood: ühe piirangu mõju

[PRAKTIKA] Võrdle sama top-2 reeglit kaalupiiriga 0,5 ja 0,3. Hoia kõik muu muutumatu.

**Lahendus:** `a,_=backtest(q,"reegel",p,cap=.5); b,_=backtest(q,"reegel",p,cap=.3)`; siis `metrics(a.net),metrics(b.net)`. Teises portfellis jääb 40% raha. Risk väheneb üldjuhul, kuid netotootluse suund sõltub riskivarade tootlusest. See eraldab kaalupiiri mõju paremini kui põhikursuse top-3 riskivariandi tervikvõrdlus.

## Vanemkvandi kriitiline küsimus

Milline ühine risk jääb alles, kui korrelatsioonid tõusevad?

Hea vastus nimetab kontrollitava tingimuse ja selle, millised andmed selle kontrollimiseks vajalikud on. Kehv vastus kaitseb mudelit lihtsalt sellepärast, et selle peale kulus palju aega.

## Enesehindamine

Anna iga kontrollvastuse eest 0–2 punkti ning kummagi praktilise ülesande eest 0–5 punkti. 16/20 näitab head alust; edasi minekuks peab ajastuse või tõendi piiri puudutav vastus siiski olema sisuliselt õige. Õpetaja selgitab keerulise vea enne järgmist päeva.
