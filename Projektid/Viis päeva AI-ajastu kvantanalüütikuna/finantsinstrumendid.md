# Kõrvalpilk teistele instrumentidele

[TÄIENDUS / NÄIDE] Kõrvalnäited ei muuda ETF-projekti optsiooni- ega futuuristrateegiaks.

| Instrument | Mis see on? | Kvandi tüüpiline probleem | Väike näide ja piir |
|---|---|---|---|
| Aktsia | Osalus ettevõttes | Tootlust seletav tunnus, dividend ja korporatiivsündmus | 100 → 104 ning 2 dividend annab 6% enne kulusid, kui dividend pole juba hinnas korrigeeritud |
| Indeks | Reegliga arvutatud turumõõdik | Koosseisu muutuste mõju ja jälgimisviga | Indeksit ennast ei osteta; fond või tuletis loob ekspositsiooni |
| ETF | Börsil kaubeldava fondi osak | Hind, NAV, likviidsus ja alusvara risk | Loomise/lunastamise ja arbitraaži mehhanism aitab hinda NAV-i lähedal hoida, kuid ei taga võrdsust igal hetkel |
| Võlakiri | Lepingulised maksed ja tagasimakse | Intressikõver, krediit ja kestustundlikkus | Nullkupong 100 eurot aasta pärast, tootlus 5%: hind 100/1.05 = 95.24 |
| Optsioon | Õigus alusvara osta või müüa kokkulepitud hinnaga | Mudelihind, delta/gamma/vega ja maandamine | Call K=100, lõpphind 110, preemia 4: payoff 10, kasum 6 enne kulusid |
| Futuur | Standardne leping tulevase arveldusega | Rollimine, basis, tagatis ja päevane arveldus | Kordaja 50 ja hinna langus 10 punkti: long kaotab 500; tagatis pole maksimaalne kahju |
| Valuutapaar | Ühe valuuta hind teises | Intressierinevus, makro ja valuutarisk | EUR/USD muutus mõjutab euroinvestori dollarivara tulemust |
| Krüptovara | Digitaalne vara või selle tuletis | 24/7 kalender, hoidmine, likviidsus ja funding | Perpetual'i funding võib kasumi ära süüa; spot ja perpetual pole sama instrument |

## Hinnastamine pole ennustamine

Aktsiakvant võib küsida, kas ettevõtte kasumimuutus ennustab tootlust. Optsioonikvant võib küsida, milline hind on kooskõlas turu volatiilsuspinna ja arbitraažipiiridega. Õiglane mudelihind ei ole kindel tulevane kasum.

Delta kirjeldab optsioonihinna esimest tundlikkust alusvara hinna suhtes, gamma delta muutust ja vega volatiilsuse tundlikkust. Näiteks delta 0,5 korral muudab alusvara väike +1 ühiku muutus optsioonihinda ligikaudu +0,5, muu samaks jäädes. Suurte liikumiste korral on vaja kõrgema järgu mõjusid. Put'i lõppväärtus on $\max(K-S_T,0)$; call'i oma $\max(S_T-K,0)$.

Võlakirja modifitseeritud duratsioon $D_{mod}$ annab väikese tootlusnihke korral $\Delta P/P\approx-D_{mod}\Delta y$. Kui duratsioon on 5 ja tootlus kasvab 1 protsendipunkti, on ligikaudne hinnamõju −5%. Suure muutuse puhul on oluline kumerus; krediidikahju ei taandu ainult intressitundlikkuseks.
