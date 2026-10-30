# Õpetaja käsiraamat

Kursus on mõeldud 10–15 tunni iseseisva töö ja aruteluna. Allpool olevad viis 90-minutilist tundi on selle juhendatud tuum: õppija loeb loo enne tundi ning lõpetab pikemad praktikumid ja lisad pärast tundi. 7,5 kontakttundi ei võrdu automaatselt kogu 12,5-tunnise tööga.

## Ettevalmistus

Paki projekt lahti, paigalda sõltuvused, käivita `projekt.py`, `testid.py` ja `raport.py`. Hoia kaasasolevad PNG-d varuks: kui õppija arvuti ei tööta, saab sisulist arutelu tabelite ja piltidega jätkata. Ära kasuta päris ostu-müügi soovitusi õppeedukuse mõõdupuuna.

Õpiväljundit hinnatakse otsuse põhjenduse, ajastuse, arvutuse ning piirangute järgi. Õppija ei pea saama kasumlikku strateegiat. Sama andmestiku tulemuste ümberjutustamine ilma kriitikata ei ole meisterlikkus.

## Tund 1: Andmeleping ja hüpotees

**Õpieesmärgid:** Õppija sõnastab mõõdetava hüpoteesi, leiab suhtelise tootluse ja eristab sünteetilist tõendit päristuru tõendist.

**Viis mõistet:** momentum; universum; benchmark; signaalihetk; punkt-ajas andmed.

**Sissejuhatus:** Kujutle, et pead enne võistlust kirja panema, kuidas võitja valid. Pärast tulemuse teada saamist reegli muutmine pole ennustus.

**Õpetaja demonstratsioon:** Näita hinnad 80 → 88 ja 200 → 216. Lase esialgu valida suurem hinnatõus, seejärel arvuta protsendid. Käivita `python/paev1.py`; palu enne väljundi näitamist prognoosida, mida skript peaks tegema. Täielik kood ja tõrgete juhend on [päeva praktikumis](paev-1-esmaspaev/praktikum.md).

**Matemaatiline näide ja vastus:** A 10%, B 8%; järjesta A enne B-d.

**Praktiline töö:** mõlemad [päeva ülesanded](paev-1-esmaspaev/ulesanded-lahendused.md). Esimene sobib individuaalselt, teine paaristööks. Kõik viis kontrollküsimust koos vastustega on samas failis.

**Keskne küsimus ja vastus:** Miks kolme kuupäeva vaja on? Sest info, tehing ja tulemuse lõplik teadmine saabuvad eri ajal.

**Levinud väärarusaamad:** Kõrgem hind tähendab paremat vara; puuduv hind tähendab nulli; tasuta tähendab piiranguteta levitamist.

| Aeg | Tegevus | Nähtav tulemus |
|---|---|---|
| 0–10 min | Sissejuhatav olukord ja ennustus | Õppija sõnastab oma eeldused |
| 10–25 min | Mõisted ja arvuline näide | Üks käsitsi kontrollitud arv |
| 25–40 min | Õpetaja Python-demo | Sisendi ja väljundi seletus |
| 40–60 min | Praktiline ülesanne 1 | Kood või arvutus koos tõlgendusega |
| 60–75 min | Otsustamisülesanne 2 paaris | Põhjendatud otsus ja piirang |
| 75–85 min | Viis kontrollküsimust | Lüngad nähtavaks |
| 85–90 min | Väljumispilet ja järgmine samm | Üks uus teadmine, üks lahendamata küsimus |

**Kokkuvõte:** palu õppijal lõpetada lause „Selle päeva tulemus lubab järeldada ..., kuid ei luba järeldada ...”. Kui teine pool jääb tühjaks, aruta uuesti tõendi piiri. Koduseks tööks jääb loo ja praktikumitulemuse võrdlus ning oma katsepäeviku sissekanne.

## Tund 2: Aus järeltest

**Õpieesmärgid:** Õppija leiab ajastusvea, arvutab liittootluse, oskab lisada kulu ja tõlgendada mõõdiku piiri.

**Viis mõistet:** liittootlus; Sharpe; MDD; look-ahead bias; käive.

**Sissejuhatus:** Tänase lotovõidu teadmine ei aita eilset piletit valida. Arvutis saab selle vea teha ühe vale liitmisega.

**Õpetaja demonstratsioon:** Kirjuta tahvlile kuu lõpu võitja ostmine kuu alguses. Lase õppijal nimetada, millal võitja teada saab. Käivita `python/paev2.py`; palu enne väljundi näitamist prognoosida, mida skript peaks tegema. Täielik kood ja tõrgete juhend on [päeva praktikumis](paev-2-teisipaev/praktikum.md).

**Matemaatiline näide ja vastus:** 1000 × 1.10 × 0.95 × 1.02 = 1065.90.

**Praktiline töö:** mõlemad [päeva ülesanded](paev-2-teisipaev/ulesanded-lahendused.md). Esimene sobib individuaalselt, teine paaristööks. Kõik viis kontrollküsimust koos vastustega on samas failis.

**Keskne küsimus ja vastus:** Miks baas maksab kulusid? Sest ka tema muudab kaale. Võrdlus peab olema järjekindel.

**Levinud väärarusaamad:** Koodi käivitumine tähendab ausat katset; suur Sharpe tähendab väikest maksimaalset kahju.

| Aeg | Tegevus | Nähtav tulemus |
|---|---|---|
| 0–10 min | Sissejuhatav olukord ja ennustus | Õppija sõnastab oma eeldused |
| 10–25 min | Mõisted ja arvuline näide | Üks käsitsi kontrollitud arv |
| 25–40 min | Õpetaja Python-demo | Sisendi ja väljundi seletus |
| 40–60 min | Praktiline ülesanne 1 | Kood või arvutus koos tõlgendusega |
| 60–75 min | Otsustamisülesanne 2 paaris | Põhjendatud otsus ja piirang |
| 75–85 min | Viis kontrollküsimust | Lüngad nähtavaks |
| 85–90 min | Väljumispilet ja järgmine samm | Üks uus teadmine, üks lahendamata küsimus |

**Kokkuvõte:** palu õppijal lõpetada lause „Selle päeva tulemus lubab järeldada ..., kuid ei luba järeldada ...”. Kui teine pool jääb tühjaks, aruta uuesti tõendi piiri. Koduseks tööks jääb loo ja praktikumitulemuse võrdlus ning oma katsepäeviku sissekanne.

## Tund 3: ML-i lisaväärtus

**Õpieesmärgid:** Õppija eristab regressiooni ja klassifitseerimist, valib sobiva ajajaotuse ja võrdleb mudelit netotulemuse järgi.

**Viis mõistet:** tunnus; silt; regulaarimine; Random Forest; RAG.

**Sissejuhatus:** Õppiv mudel otsib vanadest näidetest seose. Kui näitad talle eksami vastuseid enne eksamit, hindad mälu, mitte oskust.

**Õpetaja demonstratsioon:** Näita kolme mudeli sama perioodi tabelit. Palu leida, kas väikseim RMSE ja suurim netotootlus langevad kokku. Käivita `python/paev3.py`; palu enne väljundi näitamist prognoosida, mida skript peaks tegema. Täielik kood ja tõrgete juhend on [päeva praktikumis](paev-3-kolmapaev/praktikum.md).

**Matemaatiline näide ja vastus:** 55 × 1 − 45 × 1.5 − 100 × 0.1 = −22.5 eurot.

**Praktiline töö:** mõlemad [päeva ülesanded](paev-3-kolmapaev/ulesanded-lahendused.md). Esimene sobib individuaalselt, teine paaristööks. Kõik viis kontrollküsimust koos vastustega on samas failis.

**Keskne küsimus ja vastus:** Kas XGBoost on kohustuslik? Ei. Põhivõrdluse täidab päriselt testitud mets; lisamudelit vajab põhjendatud katse.

**Levinud väärarusaamad:** AI on alati parem; täpsus tähendab kasumit; scaler on ohutu enne jaotust.

| Aeg | Tegevus | Nähtav tulemus |
|---|---|---|
| 0–10 min | Sissejuhatav olukord ja ennustus | Õppija sõnastab oma eeldused |
| 10–25 min | Mõisted ja arvuline näide | Üks käsitsi kontrollitud arv |
| 25–40 min | Õpetaja Python-demo | Sisendi ja väljundi seletus |
| 40–60 min | Praktiline ülesanne 1 | Kood või arvutus koos tõlgendusega |
| 60–75 min | Otsustamisülesanne 2 paaris | Põhjendatud otsus ja piirang |
| 75–85 min | Viis kontrollküsimust | Lüngad nähtavaks |
| 85–90 min | Väljumispilet ja järgmine samm | Üks uus teadmine, üks lahendamata küsimus |

**Kokkuvõte:** palu õppijal lõpetada lause „Selle päeva tulemus lubab järeldada ..., kuid ei luba järeldada ...”. Kui teine pool jääb tühjaks, aruta uuesti tõendi piiri. Koduseks tööks jääb loo ja praktikumitulemuse võrdlus ning oma katsepäeviku sissekanne.

## Tund 4: Portfell ja stress

**Õpieesmärgid:** Õppija arvutab kaalutud tootluse, eristab volatiilsussihti kahjupiirist ja selgitab korrelatsiooni rolli.

**Viis mõistet:** kaal; kovariatsioon; hajutamine; likviidsus; stress.

**Sissejuhatus:** Kuus vihmavarju ei kaitse tulekahju eest. Instrumentide arv ei ütle, millise ühise sündmuse vastu nad kaitsevad.

**Õpetaja demonstratsioon:** Näita sama kahe vara portfelli korrelatsiooniga −0.5 ja +1. Võrdle 10% ja 20% volatiilsust. Käivita `python/paev4.py`; palu enne väljundi näitamist prognoosida, mida skript peaks tegema. Täielik kood ja tõrgete juhend on [päeva praktikumis](paev-4-neljapaev/praktikum.md).

**Matemaatiline näide ja vastus:** 30/30/20 ning šokid −20/−10/−5% annavad −10%, 50 000 pealt −5000.

**Praktiline töö:** mõlemad [päeva ülesanded](paev-4-neljapaev/ulesanded-lahendused.md). Esimene sobib individuaalselt, teine paaristööks. Kõik viis kontrollküsimust koos vastustega on samas failis.

**Keskne küsimus ja vastus:** Miks raha jääb alles? Sest piiratud kaalud ei summeeru üheni ja võimendust ei lisata.

**Levinud väärarusaamad:** 30% piir kehtib alati; riskisiht on garantii; MDD on maksimaalne võimalik kahju.

| Aeg | Tegevus | Nähtav tulemus |
|---|---|---|
| 0–10 min | Sissejuhatav olukord ja ennustus | Õppija sõnastab oma eeldused |
| 10–25 min | Mõisted ja arvuline näide | Üks käsitsi kontrollitud arv |
| 25–40 min | Õpetaja Python-demo | Sisendi ja väljundi seletus |
| 40–60 min | Praktiline ülesanne 1 | Kood või arvutus koos tõlgendusega |
| 60–75 min | Otsustamisülesanne 2 paaris | Põhjendatud otsus ja piirang |
| 75–85 min | Viis kontrollküsimust | Lüngad nähtavaks |
| 85–90 min | Väljumispilet ja järgmine samm | Üks uus teadmine, üks lahendamata küsimus |

**Kokkuvõte:** palu õppijal lõpetada lause „Selle päeva tulemus lubab järeldada ..., kuid ei luba järeldada ...”. Kui teine pool jääb tühjaks, aruta uuesti tõendi piiri. Koduseks tööks jääb loo ja praktikumitulemuse võrdlus ning oma katsepäeviku sissekanne.

## Tund 5: Komitee ja otsus

**Õpieesmärgid:** Õppija koostab tõendite piire austava raporti, eristab tehnilist kontrolli turueelisest ja määrab järgmise katse.

**Viis mõistet:** OOS; paper trading; seire; päritolu; otsustusvärav.

**Sissejuhatus:** Hea teadlane võib öelda, et tõend pole veel piisav. Raha eraldamisel on see kasulik tulemus, mitte piinlik vaikus.

**Õpetaja demonstratsioon:** Käivita raport, ava lähte-CSV ja palu õppijal kontrollida üht lauset ning üht arvu. Käivita `python/paev5.py`; palu enne väljundi näitamist prognoosida, mida skript peaks tegema. Täielik kood ja tõrgete juhend on [päeva praktikumis](paev-5-reede/praktikum.md).

**Matemaatiline näide ja vastus:** Vahemik −6.51 kuni +3.47 protsendipunkti sisaldab nulli.

**Praktiline töö:** mõlemad [päeva ülesanded](paev-5-reede/ulesanded-lahendused.md). Esimene sobib individuaalselt, teine paaristööks. Kõik viis kontrollküsimust koos vastustega on samas failis.

**Keskne küsimus ja vastus:** Millal jätkata? Kui järgmine katse eemaldab konkreetse puuduse, näiteks pärisandmete või täitmiskulu ebakindluse.

**Levinud väärarusaamad:** Paper trading tõendab kasumit; agent vajab kõiki õigusi; ebaõnnestunud hüpotees on raisatud töö.

| Aeg | Tegevus | Nähtav tulemus |
|---|---|---|
| 0–10 min | Sissejuhatav olukord ja ennustus | Õppija sõnastab oma eeldused |
| 10–25 min | Mõisted ja arvuline näide | Üks käsitsi kontrollitud arv |
| 25–40 min | Õpetaja Python-demo | Sisendi ja väljundi seletus |
| 40–60 min | Praktiline ülesanne 1 | Kood või arvutus koos tõlgendusega |
| 60–75 min | Otsustamisülesanne 2 paaris | Põhjendatud otsus ja piirang |
| 75–85 min | Viis kontrollküsimust | Lüngad nähtavaks |
| 85–90 min | Väljumispilet ja järgmine samm | Üks uus teadmine, üks lahendamata küsimus |

**Kokkuvõte:** palu õppijal lõpetada lause „Selle päeva tulemus lubab järeldada ..., kuid ei luba järeldada ...”. Kui teine pool jääb tühjaks, aruta uuesti tõendi piiri. Koduseks tööks jääb loo ja praktikumitulemuse võrdlus ning oma katsepäeviku sissekanne.

## Kuidas selgitada inimesele ilma matemaatika ja programmeerimiseta?

Alusta valikust, mitte valemist. Sul on kuus võimalikku investeeringut ja üks piiratud rahakott. Eelmine kuu oli mõnel parem; kas sama infot kasutades oleksid saanud järgmise kuu kohta midagi kasulikku teada? Pane reegel enne proovimist kirja. Näita käega, milline kuupäev on minevik ja milline tulevik.

Kasuta 100 eurot. +10% tähendab 110 eurot; sellest −10% jätab 99 eurot. Nii avaneb liitkasv ilma logaritmita. Kulu jaoks võta igalt vahetuselt üks münt. Hajutamise jaoks vali kaks tegevust, millel ei lähe alati korraga halvasti. Täpsusta, et halb ilm võib mõlemat korraga tabada.

Python on selles võrdluses kalkulaator, mis järgib reegleid väga kiiresti. Vale reegel muutub kiiresti paljudeks valedeks arvutusteks. ML otsib näidetest seoseid; ta ei tea iseenesest, kas näide oli tol ajal teada või kas tehing oli võimalik. LLM kirjutab loetava selgituse; veenev lause ei ole tõend.

Lase õppijal olla komitee liige: „Mida sa tahaksid enne oma raha usaldamist teada?” See viib loomulikult andmete, kulude ja kahju juurde. Alles seejärel näita valemit.

## Hindamisrubriik

| Mõõde | 0 punkti | 1 punkt | 2 punkti |
|---|---|---|---|
| Hüpotees | Ebamäärane soov | Osaliselt mõõdetav | Universum, aeg, reegel, baas |
| Ajastus | Tulevikuinfo kasutus | Mõistab probleemi | Suudab tuua töötava kontrolli |
| Arvestus | Protsendid/kulud valed | Väike viga | Liitkasv, kaalud ja kulud korrektsed |
| Mudelivõrdlus | Valib nime järgi | Üks mõõdik | Prognoos, kasum, risk ja keerukus |
| Otsus | Kasumilubadus | Mainib piiranguid | Nimetab tõendi ja järgmise katse |

Kokku 10 punkti; 8–10 on hea alus. Ajastuse või tõendamata kasumilubaduse eest saadud 0 vajab parandamist sõltumata summast. Ära anna lisapunkte lihtsalt rohkemate teekide või keerukama koodi eest.

## Lõputest koos hindamisvõtmega

1. Sõnasta ETF-momendi hüpotees nii, et seda saab ümber lükata. **Võti:** universum, 63 päeva tunnus, järgmine täitmisaeg, kulud, võrdlusportfell; 2 p.
2. Näita, miks varasema kuupäevaga silt võib siiski lekkida. **Võti:** sildi hoideperiood lõpeb tulevikus; `exit < signal`; 2 p.
3. 50/50 portfell, tootlused +10% ja −4%, kulu 0,2% NAV-ist. Kui kaalud on kulujärgsed, mis on netotootlus? **Võti:** bruto 3%; `0.998*1.03-1=2.794%`; 2 p.
4. Võrdle täpsemat, suurema käibega mudelit lihtsa reegliga. **Võti:** neto, risk, sõltumatu periood, ebakindlus ja hoolduskulu; 2 p.
5. Komitee küsib luba pärisrahale pärast sünteetilist testi. **Võti:** luba ei tulene sellest tõendist; nimeta punkt-ajas pärisandmed ja täitmise kontroll; 2 p.

## Rollimäng

Jaga rollid uurija, kaupleja, riskijuht ja portfellihaldur. Igaüks esitab ühe küsimuse ning nimetab tõendi, mis võiks tema seisukohta muuta. Uurija ei tohi vastata „AI ütles”. Portfellihaldur ei tohi valida ainult suurima CAGR-i järgi. Lõpptulemus on ühe lõigu pikkune komitee otsus koos puuduva tõendi loendiga.
