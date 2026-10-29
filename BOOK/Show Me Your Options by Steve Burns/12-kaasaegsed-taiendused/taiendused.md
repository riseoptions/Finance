# Tänapäevased täiendused ja raamatu kriitiline lugemine

[Tagasi](../README.md) · [Ametlikud allikad](../allikad.md)

## Raamatu tugevus ja kasutuspiir

[RAAMAT] 2012. aasta raamatu tugevus on vestluslik õpetamine, optsioonijalgade seostamine ja riskile tähelepanu juhtimine. Aktsiate ja ETF-ide ajaloolised hinnad pole tänased hinnapakkumised. Narratiivi kauplemisedu pole kontrollitud tulevikutootluse tõend.

## Väited, millele lisa täpsustus

| Koht PDF-is | Raamatu mõte, parafraas | Kursuse täpsustus |
|---|---|---|
| Ptk 1 ja 4, lk 10–18,37–47 | Optsioonid kui panused, mitte varad | Ostetud optsioon on finantsvara; analoogia rõhutab tingimuslikku ja aeguvat õigust. |
| Ptk 2, lk 23–24 | Strateegiate pikaajaline tasuvus on võrdne | Sama lepingu vastaspoolte P/L-id vastanduvad; see ei tõesta eri strateegiate võrdset oodatavat tootlust. |
| Ptk 4, lk 42 | Teisi kreeklasi võib mõtestada theta kaudu | Pedagoogiline rõhuasetus, mitte matemaatiline tuletus. Delta, vega ja rho on eri sisendite osatuletised. |
| Ptk 6, lk 64 | Delta koondab hinnamuutuse mõjud | Delta mõõdab S osalist mõju, mitte aja ja IV samaaegset kogumõju. |
| Ptk 3, lk 36 | Sünteetikat saab avada null netorahaga | Null deebet ei kaota tagatist ega strike’iga seotud kohustust; parity sisaldab rahastust. |
| Ptk 12, lk 125–126 | Ratio spread’i saab hiljem aktsiaostuga juhtida | Hinnaauk võib juhtimisele ette jõuda. 1×2 call ratio võib jääda piiramatu ülemise sabaga. |
| Ptk 13, lk 142 | Rohkem lepinguid võib kulude mõju vähendada | Püsikulu osakaal võib väheneda, kuid lepingupõhised kulud kasvavad kogusega; riski suurendamine ei loo eelist. |
| Ptk 15, lk 163 | Väike protsent kaitseb hävimise eest | Kasulik distsipliin, mitte garantii; korrelatsioon, hüpped, mudeliviga ja kulud jäävad. |
| LisaA, lk 176–183 | ATM-ajaväärtuse suhtelised tabelid | Ruutjuure-aja lähendus vajab paigal S-i ja IV-d; sündmuspõhine IV muudab seda. |
| LisaB, lk 184 | Võitude ja kahjude kaalutud pindade tasakaal | Null ootus pole 50% võidumäär.90%×1−10%×9=0. |
| LisaC, lk 194–196 | Delta ja võidutõenäosuse üldistused | Erista delta, ITM ja kasum; BSM-is N(d 1)≠N(d 2). „Ostjal alati alla 50%” pole universaalne turufakt. |
| LisaD, lk 198 | Ajaväärtuse kadu koondub kindlates proportsioonides viimasesse nädalasse | Osakaalud on näidistingimuste tulemused, mitte universaalsed reeglid. |
| LisaE, lk 206 | Sünteetilised vasted | Raamat märgib ise, et osa vasteid on ligikaudsed; rahastuse ja täitmise erinevused vajavad arvestamist. |

## 0DTE

[TÄIENDUS] 0DTE tähendab optsiooni, mille tähtaeg saabub samal päeval. Leping võis olla noteeritud juba varem. Cboe rõhutab rahale lähedaste optsioonide suurt hinnatundlikkust aegumise lähedal. Käesolevas kursuses ei käsitleta seda eraldi „tuluallikana”: oluline on jalgade risk ja tegutsemiseks allesjäänud aeg.

[NÄIDE] K100 call maksab 0,50. S100 juures on tähtajal kaotus 50 USD, S101 juures kasum 50 USD, M100. Katmata müüjal on vastupidine tulemus ja ülespoole puuduv lõplik kahjupiir. Väike preemia võib innustada kogust suurendama; kümme lepingut muudab 50 riski 500-ks.

## ETF, indeks ja täitmisviis

[TÄIENDUS] Erista ETF-i osakut ning arvutuslikku indeksit. Füüsiline arveldus võib anda osakud; rahaline arveldus annab lepingu tingimuste järgi arvutatud rahasumma. Ameerika ja Euroopa täitmisstiil on sellest eraldi tunnus. Cboe ametlik ülevaade selgitab nende kahe telje erinevust.

Ära tuleta tingimusi pelgalt alusvara nimest. Kontrolli konkreetse lepingu kordajat, viimast kauplemisaega, arveldusväärtuse arvutust ja täitmisotsuste kellaaegu. Selles kursuses ei ole maakleripõhiseid lõikajaid ega konto marginaaliprotsente kinnitatud.

## Likviidsus ja kulud

[TÄIENDUS] Pole üht universaalset „tänapäevast optsioonilikviidsust”. Sama alusvara aktiivne ATM-leping ja kauge strike võivad olla väga erinevad. Vaata noteeringu aega, bid/ask’i, kogust ning oma korralduse täitmist. Tehingumaht ja avatud lepingute arv on lisainfo, mitte hinnagarantii.

[NÄIDE] Neljajalgne tehing, kus iga jala hinnanihe on 0,05 ühe aktsia kohta, maksab M100 korral 20 USD ühe suuna kohta. Koos väljumisega võib see olla 40 enne komisjone. Kui teoreetiline eelis oli 15, on teostus otsustav.

## Mudelite piirid

[TÄIENDUS] Meie Black–Scholesi näited eeldavad Euroopa lepinguid, konstantset volatiilsust ja intressi, pidevat dividendimäära ning lihtsustatud kauplemistingimusi. Tegelikkuses on hüpped, erinevad strike’i-IV-d ja likviidsuskulud. Pidev dividendimäär ei taasta üksiku diskreetse dividendi täitmisotsuseid.

Ka gamma ja vega võivad suurte muutuste korral ise palju muutuda. Ühe sigma või ühe päeva theta kasutamine terve kuu jaoks on õpetlik lähendus, mitte turu täpne simulatsioon.

## Visualiseerimine ja praktiline töövoog

Alusta Thonnys terminal-P/L-ist. Lisa Matplotlibi graafik, seejärel eraldi BSM-i hinnakõver. Colab sobib jagamiseks ja parameetrite katsetamiseks. Kaasaegne interaktiivne optsioonikalkulaator on abiks ainult siis, kui näed, millist kuupäeva, IV-d ja kulusid ta eeldab. OIC pakub ametlikke hinnastamise õppematerjale; konkreetsete kommertstööriistade funktsioone ja hindu pole siin hinnatud.

## Uuendamise kontroll

Enne pärisandmetega töö alustamist kontrolli OCC riskidokumendi avaldamislehte ja lepingu spetsifikatsiooni uuesti. 29.10.2026 vaadatud OCC leht viitas June 2024 dokumendile ja T+1 arvelduse muudatusele. Sellest ei saa järeldada, et kõik tooted ja maaklerid kasutavad identset arveldust või klienditähtaega.
