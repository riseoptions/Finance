# Finantsinstrumentide alusatlas: aktsia, ETF, võlakiri ja optsioon

[Tagasi avalehele](../README.md) · [Näited Pythonis](../10-python-ja-andmed/24-naidet.md)

## Sisukord

- [Aktsia](#aktsia)
- [ETF ja indeksfond](#etf-ja-indeksfond)
- [Võlakiri](#võlakiri)
- [Optsioon](#optsioon)
- [Võrdlus ja õppetöö](#võrdlus-ja-õppetöö)

**Ulatus:** see versioon käsitleb nelja põhivahendit. Futuuride, forvardite, swap'ide, CFD-de, REIT-ide, toorainete, krüptovarade, erakapitali ja struktureeritud toodete täielik atlas on veel koostamata. Maksumäärasid ega Eesti maksureegleid siin ei esitata; need vajavad eraldi ajakohast kontrolli.

Õpieesmärk on siduda instrumendi õiguslik-majanduslik sisu tema rahavoogude ja kahjumehhanismiga. 5 minutiga loe võrdlustabel, 30 minutiga ühe instrumendi käsitlus, 90 minutiga lahenda selle arvutused ja selgita valeväite viga.

## Aktsia

1. **Mis see on?** Osalus ettevõtte omakapitalis. Lihtaktsia ja eelisaktsia õigused võivad erineda; eelisaktsia ei ole automaatselt riskivaba ega tavalise võlakirja asendus.
2. **Kuidas töötab?** Omand annab konkreetse väärtpaberiliigi tingimustele vastavad õigused. Ettevõtte vara ning võlausaldajate nõuded mõjutavad omanikele jäävat osa.
3. **Kust tootlus tuleb?** Hinnamuutusest ning väljamaksetest. Kasvu- ja väärtusaktsia on analüütilised kategooriad, mitte garanteeritud tootlusmehhanismid.
4. **Peamised riskid:** äri halvenemine, üle maksmine, võlg, juhtimine, konkurents ja osaluse lahjenemine.
5. **Hinnastamine:** diskonteeritud omaniku rahavood, võrreldavad suhtarvud ja stsenaariumid. Ükski neist ei kõrvalda prognoosiviga.
6. **Millal kasutamine põhjendatud?** Kui osalusriski, ajahorisondi ja hinna eeldusi saab põhjendada ning kahju on eesmärgiga kooskõlas.
7. **Millal halb valik?** Kui vajalik lühiajaline rahavoog sõltub ebakindla turuhinna säilimisest või investor ei mõista, mida ta omab.
8. **Kulud ja maksude põhimõte:** hinnavahe, tehingu- ja hoidmise tasud; maksukäsitlus võib sõltuda residentsusest, konto liigist ja väljamaksest. Siin arvutame maksueelseid näiteid.
9. **Eksiarvamus:** „Ettevõtte kasum kasvas, järelikult on aktsia nüüd odavam.” Hind, aktsiate arv ja tulevikuootus võivad samuti muutuda.
10. **Ühe minuti selgitus:** ostad osa äri tulevasest majanduslikust tulemusest, kuid see osa võib osutuda makstud hinnast vähem väärtuslikuks.

[NÄIDE] Hind 20, aktsiaid 10, kasum 25: turukapitalisatsioon 200 ja P/E 8. Kui CFO on 18 ning capex 15, on lihtsustatud vaba rahavoog 3. See pole automaatne ostu- ega müügisignaal, vaid põhjus uurida kasumi ja rahavoo erinevust. [Python](../python/lyhinaited/18_fundamentaal.py).

**Arutelu:** kas P/E 8 ettevõte on odavam kui P/E 20 ettevõte, kui nende kasv, risk ja kapitalivajadus erinevad? [PAPP] ptk 2 ja 4 annavad tausta; siinsed arvud on originaalsed.

## ETF ja indeksfond

1. **Mis see on?** ETF on börsil kaubeldav fondiosak. Indeksfond järgib indeksireeglit; ETF võib olla ka aktiivne. Indeks ise on arvutatud võrdlusnäitaja.
2. **Kuidas töötab?** Investor kaupleb osakuga börsil. Osakute loomine ja lunastamine suurte turuosaliste kaudu toetab hinna seost alusvarade väärtusega, kuid ei taga võrdset hinda igal hetkel.
3. **Kust tootlus tuleb?** Fondi varadest ja strateegiast, millest lahutatakse kulud. Füüsiline replikatsioon kasutab alusvarasid; sünteetiline lahendus võib kasutada tuletislepinguid.
4. **Peamised riskid:** alusvarade risk, kontsentratsioon, teostus, likviidsus ning struktuurist sõltuvad vastaspoole riskid.
5. **Hinnastamine:** erista börsihinda ja osaku NAV-i. Võrdle sama aja hinnanguid, kui alusvarade turud on avatud eri aegadel.
6. **Millal põhjendatud?** Kui fond pakub arusaadavat ja kulude mõttes sobivat viisi soovitud turu- või strateegiariski võtmiseks.
7. **Millal halb valik?** Kui nimi varjab võimendust, kitsast kontsentratsiooni või investorile sobimatut horisonti.
8. **Kulud ja maksud:** kulusuhe, hinnavahe, tehingu- ja valuutavahetuskulu; lisaks tootest ning investorist sõltuv maksukäsitlus. Kõiki kulusid ei näita üks kulusuhte number.
9. **Eksiarvamus:** „Kõik ETF-id on laiapõhjalised ja passiivsed.” Struktuur ei määra strateegiat.
10. **Ühe minuti selgitus:** ETF on pakend; sisu, teostus ja kulud määravad, millise majandusliku riski ostad.

[NÄIDE] NAV 100 ja turuhind 101 annavad 1% preemia. Kui ostad hinnalt 101 ja müüd hiljem NAV-i muutumata hinnalt 100, on hinnatootlus $100/101-1\approx-0.9901\%$. Preemia protsent NAV-ist ja ostja kahjuprotsent ostuhinnast erinevad.

```python
nav, ost, muuk = 100, 101, 100
print('Preemia:', ost/nav-1)
print('Tootlus:', muuk/ost-1)
```

**Arutelu:** kas 0.1% kulusuhte eelis kaalub ühe aasta jooksul üles 1% ebasoodsa ostupreemia? Sõltub ka müügihinnast, hoidmisajast ja ülejäänud kuludest. [TÄIENDUS] ETF-i struktuuri lühiselgituse allikas: [SEC](../allikad/veebiallikad.md). Näide on iseseisev.

## Võlakiri

1. **Mis see on?** Lepinguline nõue emitendi vastu; riigi- ja ettevõttevõlakirjal võib olla erinev krediidiprofiil.
2. **Kuidas töötab?** Maksegraafik määrab kupongid ja põhiosa; eritingimused võivad lubada ennetähtaegset lunastamist või muuta makseid.
3. **Kust tootlus tuleb?** Kupongidest, ostu- ja müügihinna või lunastusmakse erinevusest ning kupongide reinvesteerimisest.
4. **Peamised riskid:** maksehäire, intress, inflatsioon, likviidsus, valuuta ja lepingulised optsioonid.
5. **Hinnastamine:** maksete nüüdisväärtus sobivate diskontomääradega; krediidikahju peab kajastuma ootuses või määras kooskõlaliselt.
6. **Millal põhjendatud?** Näiteks sobiva tähtaja ja krediidiriskiga maksevoo sidumiseks tulevase kohustusega.
7. **Millal halb valik?** Kui pikk hinnatundlikkus on vastuolus vajadusega peagi väljuda või tootluslubadus varjab maksevõimetuse riski.
8. **Kulud ja maksud:** hinnavahe, tehingutasud, võimalik kogunenud intress ning investorist sõltuv maksumenetlus. Puhas hind ja koos intressiga arveldushind võivad erineda.
9. **Eksiarvamus:** „Kupong 5% tähendab minu tootlust 5%.” Ostuhind ja maksete täitmine määravad tegeliku tulemuse.
10. **Ühe minuti selgitus:** annad raha lepingulise tagasimakseootuse vastu, kuid makse väärtus ja täitmine pole iga võlakirja puhul kindlad.

[NÄIDE] 1000 nimiväärtus, 50 aastakupong, kolm aastat ja 6% tootlusnõue: hind 973.2699. [Python](../python/lyhinaited/06_volakiri.py). Määra tõustes langeb fikseeritud maksete nüüdisväärtus. [Matemaatika](../07-finantsmatemaatika/README.md).

**Arutelu:** millised riskid jäävad alles tähtajani hoidmisel? [TÄIENDUS] Riskiliikide kontroll: [SEC-i võlakirjade leht](../allikad/veebiallikad.md).

## Optsioon

1. **Mis see on?** Lepinguline õigus osta (*call*) või müüa (*put*) kindlaksmääratud tingimustel. Ostja maksab preemia; müüjal tekib vastav kohustus.
2. **Kuidas töötab?** Täitmishind, tähtaeg, täitmisviis ja lepingu kordaja määravad rahavood. Euroopa ja Ameerika tüüpi täitmisõigus erinevad ajastuse poolest.
3. **Kust tootlus tuleb?** Optsiooni turuhinna muutusest või väljamaksest võrreldes preemia ja kuludega.
4. **Peamised riskid:** alusvara muutus, ajaväärtus, volatiilsuse muutus, likviidsus ning müüjal täitmiskohustus.
5. **Hinnastamine:** tähtajal määrab lihtsa optsiooni väljamakse $\max(S-K,0)$ või $\max(K-S,0)$. Enne tähtaega mõjutavad hinda ka aeg, volatiilsus, intress ja dividendid.
6. **Millal põhjendatud?** Määratletud riskimaanduse või piiratud väljamakseprofiili loomiseks, kui kulusid ja kohustusi mõistetakse.
7. **Millal halb valik?** Kui ostetakse vaid odava preemia pärast või müüakse kohustust ainult sagedaste väikeste võitude põhjal.
8. **Kulud ja maksud:** preemia, hinnavahe, tehingu- ja võimalik täitmistasu; maksustamine sõltub jurisdiktsioonist ja tehingust. Mudelites rahastamiskulu puudub.
9. **Eksiarvamus:** „Õige suund tagab kasumi.” Liiga väike liikumine, ajakadu või volatiilsuse langus võivad anda kahjumi.
10. **Ühe minuti selgitus:** optsioon muudab hinnaliikumise rahavoo kuju; see ei loo tasuta eelist.

[NÄIDE] Call K=100, preemia 5, lõpphind 103: õige tõususuund, aga kasum $3-5=-2$. [Python](../python/lyhinaited/14_call.py). Put K=100, preemia 4, lõpphind 85: kasum 11. [Python](../python/lyhinaited/15_put.py).

**Arutelu:** kas optsiooni kasutamine on alati spekulatsioon? Väljamakseprofiili saab kasutada ka olemasoleva vara kahju piiramiseks, kuid kaitse maksab. [TÄIENDUS] Hinnategurid: [OIC](../allikad/veebiallikad.md). Black–Scholesi tuletus ja Greeks'i praktiline arvutus on veel tulevane süvamoodul.

## Võrdlus ja õppetöö

| Instrument | Põhiküsimus | Sage võrdlusviga | Esmane arvutus |
|---|---|---|---|
| Aktsia | Mida väärt on omaniku tulevane osa? | Hea äri = hea hind | Rahavood, kapitalisatsioon, suhtarv |
| ETF | Mida fond omab või lepinguliselt jälgib? | Pakend = strateegia | NAV, hind, kulud, alusvarade kaalud |
| Võlakiri | Kes maksab, millal ja mis tingimustel? | Kupong = tootlus | Rahavoogude nüüdisväärtus |
| Optsioon | Milline õigus ja kohustus tekib? | Väljamakse = kasum | Tähtaja väljamakse miinus preemia |

**Viis põhimõtet:** loe rahavoogu; erista õigus ja lubadus; kontrolli hinda; arvesta väljumist; võrdle kogukulu.

**Kontrollküsimused:** mis kuulub kogutootlusse; kas ETF võib olla aktiivne; miks võlakiri intressi tõustes odavneb; miks call võib tõusval turul kahjumis olla? Vastused peituvad vastava instrumendi punktides 3, 5 ja 9.

**90 minuti tunnikava:** 10 min instrumentide sorteerimine rahavoogude järgi; 20 min õiguste võrdlus; 20 min neli arvutust; 20 min eksiarvamuste parandamine; 10 min kulude ja väljumise arutelu; 10 min ühe minuti selgitused. Sobivad lahendatud ülesanded 5, 11, 18 ja 19.
