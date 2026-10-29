# Õppekava ja raamatu kaart

[Tagasi](README.md)

## Allika ulatus

[RAAMAT] Lisatud PDF-is on 217 lehekülge, tiitliandmetes aasta 2012 ja autorid Steve Burns ning Christopher Ebert. Sisukorras on 16 peatükki ja lisad A–E. Allpool on **PDF-i leheküljenumbrid**, mitte eraldi trükinumeratsioon. Kaardistus põhineb sisukorral ning peatükkide ja lisade teemakohaste lõikude kontrollil; tegemist pole iga lause toimetusliku auditiga. Kõik lehed on failis olemas. Tabelite ja diagrammide teksti automaatne eraldus on kohati napp; nende arvandmeid ei ole uude kursusse kopeeritud.

## Tegelik struktuur

| Peatükk/lisa | PDF lk | Põhiteema | Õppemoodul | Kriitiline täpsustus |
|---|---|---|---|---|
| 1 | 10–18 | Optsiooni kui tingimusliku lepingu mõte | I | Väide „pole vara” on analoogia: ostetud optsioon on siiski finantsvara. |
| 2 | 19–25 | Ostja ja müüja, tõenäosus ja väljamakse | I, V | Nullsummalisus ei tõesta võrdseid oodatavaid tootlusi. |
| 3 | 26–36 | Trend, võimendus ja vertikaalsed spread’id | IV, V | Suund üksi ei piisa; hinnas on juba ootused. |
| 4 | 37–47 | Theta, ajaväärtus ja tähtaja lähenemine | II, III | Theta ei ole teiste kreeklaste matemaatiline alus. |
| 5 | 48–58 | Vega ja volatiilsus | II, III | Erista eeldatavat ja realiseerunud volatiilsust. |
| 6 | 59–70 | Delta, likviidsus ja positsiooni suurus | III, V | Delta on osatundlikkus, mitte kogu hinnamuutus. |
| 7 | 71–78 | Covered call | IV | Aktsia langusrisk jääb; preemia pole dividend. |
| 8 | 79–93 | Katmata müüdud optsioonid | IV, V | Short call võib anda piiramatu kahjumi. |
| 9 | 94–105 | Kauged OTM-optsioonid | I, V | Väike hind ei võrdu soodsusega. |
| 10 | 106–115 | Straddle ja strangle | IV | Vajalik liikumine sõltub makstud preemiast. |
| 11 | 116–123 | Sünteetilised positsioonid | IV | Täpses võrdluses arvesta raha, intressi ja dividende. |
| 12 | 124–134 | Ratio, calendar ja diagonal spread | IV | Erinevad tähtajad vajavad mitme kuupäeva analüüsi. |
| 13 | 135–143 | Butterfly, condor ja pöördvariandid | IV | Paljud jalad suurendavad kulude tähtsust. |
| 14 | 144–152 | Optsioon enne lõpptähtaega | II, IV | Lõpptähtaja graafik ei näita tänast realiseeritavat kasumit. |
| 15 | 153–164 | Kindlustus, stop-loss ja hävimisrisk | V | Stop ei taga hinda; riskiprotsent pole garantii. |
| 16 | 165–175 | Meetod, reeglid ja eelis | V | Eelis vajab andmeid ja kuludejärgset kontrolli. |
| A | 176–183 | Ajaväärtuse suhtelised tabelid | II | Ruutjuure-aja seos on ATM-lähendus. |
| B | 184–193 | Tõenäosusega kaalutud strateegiad | V | Mudeli jaotus ei ole universaalne turujaotus. |
| C | 194–197 | Preemia, delta ja kasumitõenäosus | III, V | N(d 1), N(d 2) ja kasumitõenäosus on eri suurused. |
| D | 198–205 | P/L eri ajahetkedel | II, IV | Hoia eeldused samad; theta osakaalud ei ole seadused. |
| E | 206–210 | Sünteetiliste positsioonide tabel | IV | Mõned raamatu vasted on ligikaudsed, mitte täpsed. |

## Eelteadmised ja optimaalne järjekord

Vaja on protsentarvutust, koordinaatteljestiku lugemist ja arusaama aktsia ostmisest. Tuletisi ei pea oskama. Python on kontrollivahend, mitte sissepääsutingimus.

| Etapp | Sisu | Juhendatud töö | Iseseisev töö | Valmiduse tõend |
|---|---|---:|---:|---|
| I | Õigused, kohustused, 4 baaspositsiooni | 3 h | 3 h | Selgitad short put’i kohustust ja arvutad P/L-i |
| II | Hind, sisemine väärtus, aeg ja IV | 3 h | 3 h | Selgitad õige suuna korral tekkivat kahjumit |
| III | Viis kreeklast ja koostoime | 4,5 h | 4 h | Koostad ühikutega lokaalse riskihinnangu |
| IV | Strateegiad ja sünteetika | 6 h | 8 h | Võrdled 3 lahendust sama eesmärgi jaoks |
| V | Risk, kulud, tõenäosus ja protsess | 3 h | 4 h | Esitad tehinguplaani koos stressistsenaariumiga |
| Õpetamispraktika | Mikroõpetus ja väitlus | 1,5 h | 3 h | Õpetad ühe mõiste 5 minutiga |
| Kokku | | 21 h | 25 h | 46 h, näiteks 6 nädalat |

## Teemade seosed

Õigused → väljamakse → preemia arvestamine → kasum/kahjum → strateegia risk. Enne lõpptähtaega lisanduvad hinnamudel ja kreeklased. Tõenäosusjaotus koos P/L-funktsiooniga annab oodatava tulemuse; pelgalt diagramm seda ei anna.

## Õppimise rütm

Igal nädalal: loe moodul, joonista ise üks diagramm, lahenda viis ülesannet või küsimust, käivita üks demonstratsioon, selgita üks väärarusaam valjusti. Peata edasiliikumine, kui ajad segamini preemia laekumise ja kasumi tekkimise.

## Läbiv ülesanne

Väljamõeldud aktsia maksab 100 USD. Õppija võrdleb aktsia ostu, call’i ostu, bull call spread’i ja protective put’i. Kõigile lahendustele rakendatakse samu hindu 0, 80, 95, 100, 105, 110 ja 130; seejärel lisatakse kulud ja 10 000 USD konto piirang. Tulemus peab kirjeldama nii kasumit kui ka kaotatavat kapitali ning teostamise riske.
