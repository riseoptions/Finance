# Eesti OSINT-allikate kataloog

Koostatud ja valitud allikate dokumentatsioon kontrollitud **30.10.2026**. 40 kirjet; **esimesed 15 on esmased**. Kataloog eristab päriselt kontrollitud kirjeldusi, ebaõnnestunud avamisi ja veel kinnitamata lisakanaleid. See ei ole väide, et 40 liidest on tehniliselt läbi testitud.

**A** = dokumenteeritud ametlik API; **D** = avaldatud failid või dokumentide allalaadimine; **M** = käsitsi uuritav kanal; **P** = konto, leping, tasu, juurdepääsupiirang või osaliselt piiratud sisu. Sama teenuse eri osadel võivad olla eri reeglid. D ei tähenda automaatselt hulgiallalaadimise või edasilevitamise õigust. Puuduv A ei tähenda, et API-d kindlasti ei eksisteeri: selle kasutust pole siin kinnitatud.

Valikupõhimõte: esmased 15 katavad organisatsiooni, otsuse, hinna, loa, ruumi, rahastuse, meediaväite ja sõltumatu kontrolli. RIKi otsing ja avaandmed on eraldi töökanalid samas teenuses; KOV ja piirkondlik meedia on konkreetsed näited, mida asendada uuritava piirkonna kanaliga. 40 kirje hulgas on ka rahvusvahelisi platvorme, mille Eesti avalikku sisu saab uurida.

| Nr | Allikas | Ligipääs | Kasutus | Kontrolliallikas | Staatus/piirang |
|---|---|---|---|---|---|
| 1 ★ | [e-äriregistri avalik otsing](https://ariregister.rik.ee/) | M/P | Organisatsiooni registritunnus ja staatus | S1 | Ametlik juhend kontrollitud; portaalis dokumentide tingimused eraldi |
| 2 ★ | [e-äriregistri avaandmed ja API](https://avaandmed.ariregister.rik.ee/et/avaandmete-allalaadimine) | D/A/P | Organisatsioonide andmefailid; XML API eraldi lepingu alusel | S1,S2 | Dokumentatsioon kontrollitud; kasusaajad pole avaandmed alates 10.07.2026 |
| 3 ★ | [Riigihangete register](https://riigihanked.riik.ee/) | M/D | Hange, leping, muudatus, vaidlustus | S3,S4 | Juhend kontrollitud; veebiliidese automatiseerimiseks ei anta siin luba |
| 4 ★ | [Statistikaamet PxWeb](https://andmed.stat.ee/) | A/D/M | Hinnaindeksid ja piirkondlik taust | S5 | API dokumentatsioon kontrollitud; valikulise GETi tulemus testiraportis |
| 5 ★ | [Maa- ja Ruumiameti geoportaal](https://geoportaal.maaamet.ee/) | A/D/M | Kaardikihid ja ajaloolised ortofotod | S6 | WMS/WFS juhend kontrollitud; viita kihile ja ajale |
| 6 ★ | [PLANIS planeeringute infosüsteem](https://planeerimine.ee/digi/menetluse-infosysteem/) | M/A | Planeeringud, menetlus, WMS/WFS | S7 | Ametlik üleminekujuhis kontrollitud; PLANKi asemel PLANIS |
| 7 ★ | [Ehitisregister](https://www.ehr.ee/) | M/P | Ehitusload ja ehitise andmed | S8 | Ametlik kirjeldus kontrollitud; portaal tööriistaga ei avanenud; API kasutus ei kinnitatud |
| 8 ★ | [KOTKAS](https://kotkas.envir.ee/) | M/P | Keskkonnaload ja avalikud menetlusdokumendid | S9 | Ametlik kirjeldus kontrollitud; portaali otseavamisel 403 |
| 9 ★ | [Riigi Teataja](https://www.riigiteataja.ee/) | M/D | Kehtiv õigus ja kohalikud määrused | S10 | Avaleht nõuab JavaScripti; vali kehtiv redaktsioon käsitsi |
| 10 ★ | [Ametlikud Teadaanded](https://www.ametlikudteadaanded.ee/) | M/P | Planeeringu- ja menetlusteated | S11 | RIKi ametlik kirjeldus kontrollitud; arhiveeritud teatel võivad olla piirangud |
| 11 ★ | [KOV ametlik veeb ja dokumendiregister: Tartu näide](https://tartu.ee/) | M/D | Volikogu otsus, eelarve, protokoll | S12 | Avaleht ja planeeringute viide kontrollitud; konkreetne register valida KOV järgi |
| 12 ★ | [RTK toetatud projektid](https://rtk.ee/toetuste-ulevaated-oigusaktid/ulevaade-toetatud-projektidest/toetatud-projektid) | D/M | Toetuse otsused ja projektide tabelid | S13 | Ametlik tabelite leht kontrollitud; otsus ei ole väljamakse |
| 13 ★ | [ERR](https://www.err.ee/) | M | Avalikud uudised ja parandused | S14 | Avaleht kontrollitud; täisteksti masskogumine ei kuulu projekti |
| 14 ★ | [Riigikontroll](https://www.riigikontroll.ee/) | M/D | Auditiaruanded ja metoodiline taust | S15 | Ametlik aruannete leht kontrollitud |
| 15 ★ | [Andmete teabevärav](https://andmed.eesti.ee/) | M/D | Andmestike ja litsentside leidmine | S16 | Portaal avanes tekstita; konkreetse andmestiku tingimusi kontrollida eraldi |
| 16 | [e-kinnistusraamat](https://www.rik.ee/et/e-kinnistusraamat/e-kinnistusraamat) | P/M | Projektiala kinnistu õiguste kontroll vajadusel | S17 | Ametlik kirjeldus kontrollitud; tasu ja ligipääsu alus |
| 17 | [AKI juhised](https://www.aki.ee/teabe-avalikkus/teabe-valdajale/avaliku-teabe-taaskasutamine-avaandmed) | M | Avaliku teabe ja isikuandmete taaskasutuse piirid | S18 | Ametlik juhend kontrollitud |
| 18 | [Eesti Pank](https://www.eestipank.ee/) | M/D | Majanduslik taust ja analüüsid | S19 | Avaleht kontrollitud; konkreetne statistikatabel valida eraldi |
| 19 | [Keskkonnaportaal](https://keskkonnaportaal.ee/) | M/D | Keskkonnaandmete leidmine | - | Otseavamine ebaõnnestus 502; ligipääsu ja failide tingimusi kontrollida |
| 20 | [Kultuurimälestiste register](https://register.muinas.ee/) | M/P | Muinsuskaitse tingimuste lähtekoht | - | Otseavamine andis 403; kasutaja peab ametlikus veebis kontrollima |
| 21 | [Rahvusarhiiv](https://www.ra.ee/) | M/P | Projektiala ajaloolised dokumendid | - | Otseavamisel ajalimiit; digikoopia ja juurdepääsu tingimused eraldi |
| 22 | [DIGAR](https://www.digar.ee/) | M/P | Ajaloolised väljaanded ja ajalehed | - | Otseavamisel 403; autoriõigus ja kohalkasutuse piirangud kontrollida |
| 23 | [TED Euroopa hanketeated](https://ted.europa.eu/) | M/D | Eesti rahvusvahelise piirmääraga hanked | S3 | RHR ametlik juhend kinnitab teadete saatmist; otsene API selles projektis testimata |
| 24 | [Postimees](https://www.postimees.ee/) | M/P | Uudised, algväited ja parandused | - | Kataloogikandidaat; konkreetse lehe juurdepääs ja taaskasutus kontrollimata |
| 25 | [Tartu Postimees](https://tartu.postimees.ee/) | M/P | Kohaliku arendusprojekti kajastus | - | Kataloogikandidaat; tasuline sisu ainult lubatud ligipääsuga |
| 26 | [Delfi](https://www.delfi.ee/) | M/P | Uudised, faktikontroll ja avalik debatt | - | Kataloogikandidaat; täistekstide kogumise tingimused kontrollida |
| 27 | [Äripäev](https://www.aripaev.ee/) | M/P | Äri- ja ehitusvaldkonna kajastus | - | Kataloogikandidaat; tellimus ei tähenda masskopeerimise luba |
| 28 | [Facebooki avalikud projektilehed](https://www.facebook.com/) | M/P | Avalikud ametlikud projektiteated | - | Käsitsi; nähtavus ja tingimused kontrollida konkreetsel lehel |
| 29 | [Instagrami avalikud projektikanalid](https://www.instagram.com/) | M/P | Projektifotod ja avalikud teated | - | Käsitsi; ei koguta jälgijaid ega autoriprofiile |
| 30 | [TikToki avalikud projektivideod](https://www.tiktok.com/) | M/P | Avalikud videoväited ja nende päritolu | - | Käsitsi; ilma juurdepääsutõketest möödumiseta |
| 31 | [YouTube ametlikud KOV kanalid](https://www.youtube.com/) | M/P | Volikogu istungite ja arutelude salvestised | - | Kataloogikandidaat; kanali ametlikkus ja video tingimused eraldi |
| 32 | [X avalikud asutuste teated](https://x.com/) | M/P | Avalik kommunikatsioon ja viited | - | API-d ei eeldata tasuta ega lubatuks; ainult käsitsi hinnatud avalik sisu |
| 33 | [Hinnavaatluse foorum](https://foorum.hinnavaatlus.ee/) | M/P | Tehniliste väidete ja aruteluteemade avastamine | - | Kataloogikandidaat; foorum ei ole registriandmete asendus |
| 34 | [Ehitusfoorum](https://www.ehitusfoorum.com/) | M/P | Ehitusväidete ja terminite arutelu | - | Kataloogikandidaat; arvamused kontrollida tehniliste algallikatega |
| 35 | [Reddit r/Eesti](https://www.reddit.com/r/Eesti/) | M/P | Eesti avaliku debati teemad | - | Kataloogikandidaat; valikukallutatus, ei profileerita kasutajaid |
| 36 | [Tallinna ametlik veeb](https://www.tallinn.ee/) | M/D | Võrdlusprojekti eelarve ja menetlus | - | Kataloogikandidaat; iga dokumendiregistri piirang eraldi |
| 37 | [Transpordiamet](https://www.transpordiamet.ee/) | M/D | Taristuprojektide ja liiklusmõju taust | - | Kataloogikandidaat; allalaaditav fail kinnitada enne importi |
| 38 | [Keskkonnaamet](https://www.keskkonnaamet.ee/) | M/D | Avalikustamised ja selgitused | S9 | Ametlikud KMH ja loateadete juhised kontrollitud |
| 39 | [Riigi kinnisvararegistri avaandmed](https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/riigi-kinnisvararegister/avaandmed) | D/M | Riigi kinnisvara aruanded | S20 | Ametlik XML aruannete suunaleht kontrollitud |
| 40 | [RIHA](https://www.riha.ee/) | M | Registri vastutaja, andmekoosseis ja dokumentatsioon | S21 | RHR ja EHR kirjeldused kontrollitud; RIHA ei anna iseenesest andmetele ligipääsu |

## Olulised kontrollitulemused

- RIKi avalikud failid ja XML API on eri ligipääsuteed; API üldjuhul eeldab lepingut. Tegelike kasusaajate andmed eemaldati avaandmetest 10.07.2026. [RIKi teade](https://avaandmed.ariregister.rik.ee/et/avaandmete-allalaadimine).
- RHRi tingimused eristavad avaandmeid veebiliidese eriotstarbelise programmiga kasutamisest. Projektil pole luba veebiliidest kraapida [S4]. Kasuta ametlikku eksporti ja dokumente.
- PLANK on ajalooline nimetus; uute planeeringute esitamine toimub alates 08.01.2026 PLANISes [S7]. Vana URLi ei tohi käsitleda ajakohase andmekogu tagatisena.
- WMS on kaardipiltide teenus; WFS annab objektandmeid. Kihtide ajakohasus ja viitamisnõuded tuleb üle kontrollida [S6].
- Avalik teave võib sisaldada isikuandmeid; avalikkus ei anna piiramatut taaskasutusõigust [S18]. Õppeprojekt ei tee eraisikute masskogumist.

## Kogumise otsustusreegel

1. Kirjuta konkreetne uurimisküsimus ja vajalikud väljad.
2. Ava ametlik dokumentatsioon ning salvesta selle versioon ja kontrolliaeg.
3. Vali esmalt lubatud allalaadimine või dokumenteeritud API. Kui neid pole, tee piiratud käsitsi väljavõte lubatud ulatuses.
4. Konto, tasu, captcha, 401/403 või teenusetingimuse takistuse korral peata vastav tee. Ära vaheta selle vältimiseks identiteeti.
5. Säilita ainult vajalik tekst, viide, aeg ja päritolu. Autoriõigusega täistekste ei lisata avalikku GitHubi.

## Kontrollitud viited

- **S1**: <https://www.rik.ee/et/e-ariregister/avaandmete-teenus>
- **S2**: <https://avaandmed.ariregister.rik.ee/et/node/2>
- **S3**: <https://www.rtk.ee/riigihangete-register>
- **S4**: <https://rtk.ee/riigihangete-korraldamine/registri-haldamine/rhr-kasutustingimused>
- **S5**: <https://www.stat.ee/sites/default/files/2021-02/API-juhend.pdf>
- **S6**: <https://geoportaal.maaamet.ee/est/Teenused/WMSWFS-teenused-p65.html>
- **S7**: <https://planeerimine.ee/plank-juhendid/>
- **S8**: <https://kliimaministeerium.ee/e-ehitus>
- **S9**: <https://www.keskkonnaamet.ee/keskkonnateadlikkus-avalikustamised/raagi-kaasa/keskkonnamoju-hindamiste-avalik-valjapanek>
- **S10**: <https://www.riigiteataja.ee/>
- **S11**: <https://www.rik.ee/et/muud-teenused/ametlikud-teadaanded>
- **S12**: <https://tartu.ee/>
- **S13**: <https://rtk.ee/toetuste-ulevaated-oigusaktid/ulevaade-toetatud-projektidest/toetatud-projektid>
- **S14**: <https://www.err.ee/>
- **S15**: <https://www.riigikontroll.ee/>
- **S16**: <https://www.aki.ee/teabe-avalikkus/teabe-valdajale/avaliku-teabe-taaskasutamine-avaandmed>
- **S17**: <https://www.rik.ee/et/e-kinnistusraamat/e-kinnistusraamat>
- **S18**: <https://www.aki.ee/teabe-avalikkus/teabe-valdajale/avaliku-teabe-taaskasutamine-avaandmed>
- **S19**: <https://www.eestipank.ee/>
- **S20**: <https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/riigi-kinnisvararegister/avaandmed>
- **S21**: <https://www.riha.ee/Infos%C3%BCsteemid/Vaata/RHR>