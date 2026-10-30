# Katsekaart HPR-MOM-01

[NÄIDE] Protokoll fikseeritakse enne tulemuste vaatamist. Õppematerjali autor lõi allpool oleva katse ja andmegeneraatori koos; see ei ole sõltumatu eelregistreeritud finantsuuring.

| Valik | Fikseeritud reegel |
|---|---|
| Universum | Kuus sünteetilist sektorilaadset vara; pärisandmeharus XLK, XLF, XLE, XLV, XLI, XLP |
| Signaal | Viimase 63 vaatluspäeva lihttootlus |
| Sagedus | Üks otsus kuus, kuu viimase vaatlusrea sulgemise järel |
| Täitmine | Järgmise vaatlusrea sulgemisel; signaal on siis juba teada |
| Siht | Selle täitmishinna ja järgmise kuu täitmishinna vaheline tootlus |
| Baas | Kuue vara võrdkaal, igakuine tasakaalustamine |
| Reegel / ML | Kaks suurima skooriga vara, kumbki 50%; negatiivne skoor ei tähenda automaatselt rahasse minekut |
| Riskivariant | Kolm momentum-liidrit, kuni 30% igaüks; ülejäänu raha; 12% prognoositud aastavolatiilsuse siht |
| Kulud | 10 baaspunkti iga ostetud või müüdud dollari kohta; kontroll ka 0, 5, 25 ja 50 bp |
| Raha | 0% tootlus; riskivaba määr Sharpe'is samuti 0, et õppenäide jääks läbipaistev |
| Treening | Kõik varasemad read, mille hoideperiood lõppes enne signaalihetke |
| Valideerimine | Signaalid 2019–2021 |
| Lõppkatse | Signaalid 2022–2025; viimane täielik periood lõpeb 2025. aasta detsembris |
| ML | Ridge alpha=10; Random Forest 60 puud, sügavus 3, lehes vähemalt 25 rida, seeme 42 |
| Valikureegel | ML-i ei võeta kasutusse pelgalt kõrgema tootluse tõttu; vaja sõltumatuid pärisandmeid |

## Kolm aega ühe rea kohta

Näiteks 31.01 sulgemisandmetega valmib signaal. Tehing täidetakse järgmisel vaatluspäeval, näiteks 01.02 sulgemisel. Positsioon teenib tootlust sellest hetkest järgmise rebalance'i täitmiseni, näiteks 01.03 sulgemiseni. Seda tootlust ei tohi kasutada 28.02 signaali mudeli treenimisel: väljund pole veel tervikuna realiseerunud.

Koodis on kaitse `train = data[data.exit < signal]`. Viivitust ei väljendata lihtsalt ühe paneelirea nihkega, sest samal kuupäeval on kuus vara. Kõik sama kuupäeva varad kuuluvad samasse testplokki. Eeltöötluse `StandardScaler` sobitatakse uuesti ainult treeningul.

## Kuidas lugeda walk-forward-katset?

Iga kuu mudel õpib varasemast ja prognoosib uut kuud. 2023. aastal võib ta kasutada 2022. aasta juba lõppenud perioode, sest nii toimiks eelnevalt fikseeritud süsteem ka päriselt. See ei ole leke. Parameetrite muutmine 2022–2025 tulemuste järgi ja sama perioodi jätkuv nimetamine puutumata lõppkatseks oleks leke uurimisprotsessis.

Valideerimine ja lõppkatse algavad tabelites eraldi rahapositsioonist. Mõlemal arvestatakse esmast ostukulu. Seetõttu ei tohi kahe eraldi tabeli tootlusi pimesi kokku liita üheks katkematuks live-ajaloooks. Perioodi lõpus positsioone ei likvideerita; aruandes on mark-to-market väärtus.

## Mis võib hinnangut veel moonutada?

- Kuue tänapäeval tuntud ETF-i tagantjärele valimine on valikukallutatus. See ei ole kogu ajaloolise aktsiauniversumi katse.
- Sünteetiline kalender kasutab tööpäevi, sealhulgas mõningaid pärisbörsi pühi. Seda ei tohi kasutada orderite ajastamiseks.
- Korrigeeritud sulgemishind on kogutootluse ligikaudne proksi; dividendide, splittide ja revisjonide detailsus vajab kontrolli. Dividendi ei lisata teist korda.
- Simulaator eeldab võimalikku sulgemishinna täitmist ja protsentuaalset kulu. Turumõju ei ole lineaarse kulumääraga ammendatud.
- Sünteetilise generaatori omadusi teades saaks sellele üle õppida. Ära vali uut juhuseemet selle järgi, milline annab ilusama tulemuse.
- Kuus sama kuu vaatlust ei ole kuus sõltumatut turuajalugu. Statistiline hindamine peab säilitama kuupõhise sõltuvuse.

## Järgmise päriskatse edu- ja peatamisreeglid

Kogu punkt-ajas andmed ja kirjuta valikureeglid enne testi. Vaata netotootlust, riski, kulutundlikkust, osaperioode ja faktoriekspositsioone koos. Kui kulude realistlik ülemine hinnang kaotab eelise, jätka uurimist, ära vii pärisrahale. Kui leitakse ajastusviga, tühista varasemad järeldused. Kui lõppkatse on kord avatud, vajab uus mudel uut sõltumatut hindamist.
