# USA väärtpaberituru analüüsi- ja investeerimisotsuste tugisüsteem Pythoniga

## Õppedemo ulatus

Põhiprojekt ühendab hindade kvaliteedikontrolli, tootlused, riski, osta-ja-hoia portfelli, SMA järeltesti, mudelivõrdluse, graafiku ning raporti. Laiendatud offline-jooks lisab fundamentaalnäite, tehnilise analüüsi, kohaliku tõendiotsingu ja skriptitud agenditöövoo. Pärisandmete laadija ja live-LLM on eraldi valikulised sisendid.

Kõik paketis olevad hinnad on **simuleeritud**. Sünteetilise võlakirjasarja nimi ei tähenda, et modelleeritud oleks võlakirja kupongid või tähtaeg: see on madalama volatiilsusega illustratiivne indeksilaadne sari. Ettevõttearuanded on fiktiivsed. Tulemusi ei tohi esitleda USA turu tegeliku ajaloolise tootlusena.

## Üheksa etappi

| Etapp | Fail / tegevus | Valmidus ja kontroll |
|---|---|---|
| 1. Andmed | `laadi_yahoo.py`, `tuum.demo_hinnad` | Offline genereerimine testitud; Yahoo adapter olemas, võrgus kontrollimata |
| 2. Tootlus ja risk | `tuum.moodikud` | Algväärtus drawdown'is; valimi standardhälve; käsinäited testitud |
| 3. Portfell | `tuum.osta_hoia` | Võrdsed algkaalud; kaalude triiv; välised rahavood puuduvad |
| 4. Fundamentaalanalüüs | `m02.py`, `sec_fred.py` | Näitajate töötav illustratsioon; SEC adapter ei tõlgenda automaatselt XBRL-i täielikult |
| 5. Tehniline analüüs | `m10.py`, `tuum.indikaatorid` | SMA20/60 ja lihtne RSI14; alguses vajalikud puudumised |
| 6. Masinõpe | `m08.py`, `ml_lisad.py` | Nullbaas, Ridge, RF, logistiline, K-means; ajapõhine eraldus |
| 7. AI-uuring | `uurimisagent.otsi`, `PROMPTID.md` | Kohalik TF-IDF tõendiotsing; live-harus LLM süntees |
| 8. Agent | `uurimisagent.py --live` | Piiratud tööriistavalik ja viite-ID kontroll; päris API-jooks tegemata |
| 9. Koondamine | `koik_etapid.py` | Üks offline käivitus ja `valjund/koondraport.md` |

## Käivitamine ja tulemuse lugemine

`python kood/koik_etapid.py` loob `valjund/koondraport.md`. Avage ka `portfell.png`, `optsioonid.png`, `kaalud.png`, `mudelid.csv` ning `agent_log.json`.

Mõõdikute ühik on murdarv: −0,1774 tähendab −17,74%. Max drawdown on negatiivne arv; absoluutväärtus väljendab tipu suhtes kaotatud osa. RMSE 0,014569 tähendab ligikaudu 1,4569 protsendipunkti päevase tootluse prognoosiviga.

Näidises võib kogu portfell langeda. Juhuarvu seeme 42 teeb katse korratavaks, mitte finantsiliselt realistlikuks kõigis omadustes. Selles demojooksus on nullprognoos parem kui keerukamad võrreldud mudelid. Sobiv järeldus on katse tulemuse kirjeldamine, mitte prognoos, et üks mudeliklass ei tööta kunagi.

## Koodi lugemise järjekord

1. `tootlused`: kontroll → järjestikuste hindade suhtarv.
2. `moodikud`: liittootlus → aastastamine → tippudest langus.
3. `osta_hoia`: hinnad normaliseeritakse esimese päeva suhtes; algkaalud määravad ostetud osakud.
4. `backtest`: indikaator → signaal → hilisem täitmine → hoitud positsioon → kulu.
5. `ml_andmed`: mineviku tunnused ja ühe sammu tulevasiht.
6. `ml_vordlus`: arendusosa, lõputest, lõhe, CV ja võrreldavad prognoosid.
7. `uurimisagent`: lubatud tegevus → kontroll → vaatlus → järgmine tegevus → piiratud lõppvastus.

## Lõpuprojekti iseseisev laiendus

Vali ette kolm uuritavat vara ning võrdlusbaas; põhjenda valikut enne tulemuste nägemist. Laadi ajaloolised andmed, säilita päritolu. Lisa ühe pärisettevõtte aruandest kolm näitajat koos täpsete perioodide ja allikakohtadega. Kasuta neid aruande selgituses; ära lisa tänast suhtarvu automaatselt mineviku ML-ridadesse.

Muuda üks komponent korraga. Võrdle kuludeta ja kuludega strateegiat. Loo viis kontrollküsimust dokumendiuuringu jaoks, mille vastus ja tõend on sulle teada. Hinda agenti nende järgi; loetav tekst üksi ei ole kvaliteedimõõdik.

## Arvestustöö: 100 punkti

| Kriteerium | Punktid |
|---|---:|
| Päritolu, ajastus, ühikud ja andmekontroll | 20 |
| Finantsarvutused, rahavoogude eeldused ja testid | 20 |
| Baasvõrdlus, ajajaotus ja andmelekke vältimine | 20 |
| Riskid, kulud, piirangud ja tõendatud dokumendiväited | 15 |
| Korratav käivitus ja selge dokumentatsioon | 15 |
| 10-minutiline minitund koos kontrollküsimusega | 10 |

Lävend 60 punkti. Tulevikuandmete kasutamine või simuleeritud tulemuste esitamine pärisandmetena tuleb enne arvestust parandada. Kõrge tootlus ei anna iseenesest punkte. Õpetaja kontrollib vähemalt ühe tootluse, ühe drawdown'i, ühe ajapiiri ning ühe dokumendiviite käsitsi.

## Piirangud

Ei ole maksuarvestust, maaklerikorraldusi, lühikeste positsioonide laenukulu, turumõju, punkt-ajas indeksikoosseisu ega täielikku portfelli välisrahavoogude arvestust. Live-LLM ja välised API-d võivad muutuda. See on demonstratsiooniks ja kontrollitud õppimiseks mõeldud lähtekoht.
