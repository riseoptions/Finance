# Market Sense and Nonsense: eestikeelne õppematerjal

**Alus:** Jack D. Schwager, *Market Sense and Nonsense: How the Markets Really Work (and How They Don't)*, Wiley, autoriõiguse aastaarv 2013. Koostatud kasutaja lisatud PDF-i põhjal.

**Eesmärk:** õppida eristama head tulemust heast otsusest, nähtavat hinnakõikumist tegelikust riskist ning üksikinvesteeringu kvaliteeti selle kasulikkusest portfellis.

See on raamatu põhimõisteid ja meetodeid kattev iseseisev õppejuhend, mitte tõlge. Raamatu ajaloolisi tabeleid ja kõiki juhtumilugusid ei ole ümber kirjutatud. Nende asemel kasutatakse kontrollitavaid õppenäiteid. Raamatu ajaloolised tulemused ei kirjelda tänast turuolukorda; materjal ei vali õppijale konkreetseid investeeringuid.

## Kuidas materjali lugeda

- **[RAAMAT]** tähistab autori seisukoha või käsitluse refereeringut. See ei tähenda automaatselt üldkehtivat teaduslikku järeldust.
- **[SELGITUS]** tähistab koostaja lisatud mõisteavamist, matemaatilist tuletust või kriitilist täpsustust.
- **[NÄIDE]** tähistab koostaja väljamõeldud andmeid ja lahendust, kui pole öeldud teisiti.
- **[HARJUTUS]** ja **[KONTROLL]** on koostaja ülesanded. Lahendused avanevad plokis „Vastus ja põhjendus”.

Kõik viited kujul **PDF lk** tähistavad lisatud faili füüsilist lehekülge, lugedes esimesest leheküljest. Need ei ole trükiraamatu leheküljenumbrid. Raamatu sisukord on PDF lk 2–6, põhitekst koos lisadega lk 12–222. Matemaatikas kasutatakse kümnendmurru punkti ja tekstis tavapärast eesti komakirjutust. Tootlus 5% sisestatakse Pythonisse arvuna `0.05`.

## Sisukord

1. [Raamatu struktuur ja õppekava](#oppekava)
2. [Eelteadmised ja tootluse matemaatika](#alused)
3. [I osa: turud, tootlus ja risk — peatükid 1–9](#osa1)
4. [II osa: riskifondid — peatükid 10–16](#osa2)
5. [III osa: portfell — peatükid 17–21](#osa3)
6. [Lisa A: optsioonid](#optsioonid)
7. [Lisa B: valemid ja mõõdikute piirangud](#valemid)
8. [Praktikum Pythonis](#python)
9. [Lõppprojekt ja hindamisjuhend](#projekt)
10. [Mõistesõnastik ja kordamine](#sonastik)

<a id="oppekava"></a>
## Raamatu struktuur ja optimaalne õppekava

### Milline probleem seob raamatut tervikuks?

Raamatu proloogis kirjeldab autor vastuolu: edukate varahaldurite kliendid võivad siiski kaotada, kui nad sisenevad pärast tugevat tõusu ja väljuvad pärast langust. Seega ei piisa investeeringu keskmise tootluse teadmisest. Olulised on valiku alus, ajastus, risk ja investori käitumine.

Raamatu arutlus liigub kolmes etapis:

1. **Kas ma tõlgendan turgu ja tulemusi õigesti?** Ekspertide usaldamine, turu tõhusus, minevikutootluse kasutamine, riski mõõtmine.
2. **Mida ma tegelikult ostan?** Riskifondi strateegia, tasud, võimendus, likviidsus, andmebaasi kallutatus ja õiguslik struktuur.
3. **Kuidas komponendid koos toimivad?** Hajutamine, tasakaalustamine, ühised kahjumid ja riskipõhine jaotus.

| Algne peatükk | Õppeteema | PDF lk | Omandatav oskus |
|---|---|---:|---|
| 1. Expert Advice | Eksperdi väite kontroll | 16–21 | Koostada aus prognooside hindamise reegel |
| 2. The Deficient Market Hypothesis | Turu tõhusus ja selle kriitika | 22–49 | Eristada hinnaviga, kauplemisvõimalust ja tõestatud eelist |
| 3. The Tyranny of Past Returns | Minevikutootluse lõks | 50–72 | Eristada tulemust ja selle tekitanud tingimusi |
| 4. The Mismeasurement of Risk | Nähtav ja varjatud risk | 73–87 | Teha arvulist ja sisulist riskianalüüsi |
| 5. Why Volatility Is Not Just about Risk... | Liittootlus ja võimendusega ETF | 88–95 | Arvutada mitme perioodi tootlus |
| 6. Track Record Pitfalls | Tootlusajaloo võrreldavus | 96–102 | Leida asjakohane võrdlusperiood |
| 7. Sense and Nonsense about Pro Forma Statistics | Hüpoteetilised ja korrigeeritud tulemused | 103–104 | Tuvastada tagantjäreletarkust |
| 8. How to Evaluate Past Performance | Mõõdikud ja visuaalne analüüs | 105–126 | Kasutada mitut riski ja tootluse näitajat |
| 9. Correlation: Facts and Fallacies | Korrelatsioon, beeta ja languskuud | 127–137 | Hinnata sõltuvust ja selle ulatust |
| 10. The Origin of Hedge Funds | Long/short-loogika | 139–144 | Arvutada bruto- ja netopositsioon |
| 11. Hedge Funds 101 | Strateegiad ja fonditingimused | 145–154 | Siduda strateegia tuluallika ja riskiga |
| 12. Hedge Fund Investing: Perception and Reality | Riskifond portfelli osana | 155–161 | Hinnata võimalikku hajutuskasu |
| 13. Fear of Hedge Funds: It's Only Human | Psühholoogilised eelarvamused | 162–165 | Rakendada sama hindamisstandardit eri toodetele |
| 14. The Paradox of Hedge Fund of Funds Underperformance | Indeksite kallutatus | 166–169 | Kontrollida andmete tekkemehhanismi |
| 15. The Leverage Fallacy | Võimenduse tähendus | 170–173 | Eristada riskivõtmist ja riskimaandamist |
| 16. Managed Accounts... | Eraldi hallatav konto | 174–181 | Hinnata kontrolli, omandit ja väljumisvõimalust |
| II osa järelsõna | Investori ja fondi tootlus | 182–183 | Eristada aja- ja rahakaalutud tulemust |
| 17. Diversification: Why 10 Is Not Enough | Hajutamise saba- ja eririsk | 185–190 | Hinnata üksikfondi läbikukkumise mõju |
| 18. Diversification: When More Is Less | Näiline hajutamine | 191–194 | Leida samade riskide dubleerimine |
| 19. Robin Hood Investing | Tasakaalustamine | 195–201 | Võrrelda fikseeritud kaale ja osta-hoia strateegiat |
| 20. Is High Volatility Always Bad? | Portfellipõhine hindamine | 202–204 | Arvutada komponendi mõju koguriskile |
| 21. Portfolio Construction Principles | Portfelli koostamine | 205–213 | Koostada põhjendatud jaotus ja stressitest |
| Epiloog | 32 tähelepaneku süntees | 214–216 | Siduda kontrollküsimused otsustusprotsessiks |
| Lisa A | Optsioonide alused | 217–219 | Mõista mittelineaarset kasumit ja kahjumit |
| Lisa B | Riskiga korrigeeritud mõõdikud | 220–222 | Arvutada ja kriitiliselt tõlgendada suhtarve |

### Soovituslik õppimise järjekord

**[SELGITUS]** Säilitame allpool raamatu peatükinumbrid, kuid õppimisel tasub põhioskused varem omandada. Ajad on õppimise planeerimise hinnangud, mitte läbimise tähtajad.

| Õppeplokk | Materjal | Soovituslik aeg | Edasiliikumise tingimus |
|---|---|---:|---|
| 1. Matemaatiline alus | Eelteadmised, lisa A, peatükk 5 | 5–7 h | Arvutad liittootluse ja selgitad optsiooni kahjumit |
| 2. Tõend ja eksimus | Peatükid 1–3, 6–7 | 7–9 h | Leiad valikukallutatuse ja sobimatu võrdluse |
| 3. Risk ja mõõtmine | Peatükid 4, 8–9, lisa B | 10–14 h | Arvutad mõõdikud ning nimetad nende piirangud |
| 4. Investeerimisstruktuurid | Peatükid 10–16, järelsõna | 8–10 h | Seostad strateegia tuluallika, tasude ja varjatud riskidega |
| 5. Portfelli mõtlemine | Peatükid 17–21 | 8–10 h | Põhjendad jaotust kogu portfelli tasemel |
| 6. Rakendamine | Python, lõppprojekt ja kordamine | 8–12 h | Esitad arvutused, eeldused ja kriitilise järelduse |

Kokku ligikaudu **46–62 tundi**, mida võib jagada näiteks 8–12 nädalale. Sügavaks õppimiseks tee iga teema kohta kaks ringi: esimesel mõista ja arvuta, teisel selgita ilma materjali avamata ning muuda näite eeldusi.

**Iga õppesessiooni rütm:** 10 minutit eelneva meenutamist, 30–45 minutit uut materjali, 20–30 minutit arvutamist, 5 minutit vigade märkmikku. Edasi liigu siis, kui oskad nii vastata kui ka selgitada, millal vastus enam ei kehti.

<a id="alused"></a>
## Eelteadmised: tootlus, raha ja risk

**[SELGITUS]** Vaja on protsente, astmeid, aritmeetilist keskmist ja lihtsat tõenäosust. Programmeerimine on lisavõimalus. Eristame kolme küsimust: kui palju väärtus muutus, kui ebaühtlaselt muutus toimus ja milliseid kaotusi võib tulevik tuua.

### Tootluse põhimõisted

Kui perioodi algväärtus on $V_0$, lõppväärtus $V_1$ ja perioodi lõpus saadav väljamakse $D$, siis ilma vahepealsete sissemakseteta:

$$r=\frac{V_1+D-V_0}{V_0}.$$

Mitme perioodi jooksul, kui väljamaksed reinvesteeritakse ja uusi sissemakseid pole:

$$V_T=V_0\prod_{t=1}^{T}(1+r_t).$$

Aritmeetiline keskmine $\bar r=\frac{1}{T}\sum r_t$ kirjeldab keskmist periooditootlust. Geomeetriline keskmine $g=(\prod(1+r_t))^{1/T}-1$ kirjeldab sama lõppväärtust andvat püsivat periooditootlust. Aastane liitkasvumäär ehk CAGR kasutab astendajana aastate arvu pöördväärtust.

**[NÄIDE]** 1000 eurot kasvab esimesel aastal 20% ja langeb teisel 20%:

1. Esimese aasta lõpus $1000\cdot1.20=1200$.
2. Teise aasta lõpus $1200\cdot0.80=960$.
3. Kahe aasta kogutootlus on −4%, mitte 0%.
4. Aastane liittootlus on $\sqrt{0.96}-1\approx-2.02\%$.

Kahjumi tagasitegemiseks vajalik tõus pärast langust $d$ on $d/(1-d)$. Pärast 25% langust on vaja 33,33% tõusu; pärast 50% langust 100% tõusu.

### Riskisõnavara

| Mõiste | Sisuline küsimus |
|---|---|
| Volatiilsus | Kui palju tootlused keskmise ümber kõiguvad? |
| Kapitalilangus ehk drawdown | Kui palju on väärtus varasemast tipust langenud? |
| Likviidsusrisk | Kas saan müüa vajaliku koguse piisavalt kiiresti ja talutava hinnaga? |
| Krediidirisk | Kas võlgnik täidab kohustuse? |
| Rahastusrisk | Kas finantseerimine või tagatisnõue võib muutuda? |
| Sabariski sündmus | Kas harva esineb erakordselt suur kahjum? |
| Mudelirisk | Kas arvutus põhineb valedel eeldustel? |
| Operatsioonirisk | Kas protsess, süsteem, arvestus või kontroll võib ebaõnnestuda? |

**[HARJUTUS]** 2000 euro tootlused on +10%, −10%, +5%. Leia lõppväärtus ja kogutootlus. **[KONTROLL]** Miks ei saa tootlusi lihtsalt liita?

<details><summary>Vastus ja põhjendus</summary>

$2000\cdot1.10\cdot0.90\cdot1.05=2079$ eurot. Kogutootlus on 3,95%. Summa +5% eksib, sest iga protsent rakendub muutunud kapitalile. Liitmine sobib rahaliste kasumite, mitte üldjuhul järjestikuste protsenttootluste jaoks.

</details>

<a id="osa1"></a>
## I osa. Turud, tootlus ja risk

## 1. Ekspertide nõuanded

**Allikas:** peatükk 1, PDF lk 16–21. **Õpieesmärk:** hinnata prognoose kontrollitava tulemuse, mitte esineja enesekindluse järgi.

**[RAAMAT]** Schwager analüüsib finantstelevisiooni soovitusi, ekspertide turusuunaindeksit ja tasulisi uudiskirju. Tema järeldus on, et avalik nähtavus ja asjatundlik esinemine ei tõenda investeerimisalast lisaväärtust. Soovitus võib põhjustada kohese hinnahüppe, millest hiljem reageeriv kuulaja enam kasu ei saa. Autor möönab, et tema näited ei moodusta iseseisvalt lõplikku tõestust kõigi ekspertide kohta.

**[SELGITUS]** Kontrollimisel tuleb enne tulemuse teadasaamist fikseerida: soovituse aeg, vara, suund, ajahorisont, sisenemishind, väljumisreegel, võrdlusindeks ja kulud. Kaasata tuleb kõik soovitused, mitte üksnes õnnestumised. „Turg võib korrigeeruda” ei ole ilma ajahorisondi ja ulatuseta üheselt hinnatav prognoos.

**[NÄIDE]** Ekspert ütleb hinna 100 juures „osta”. Enne kui kuulaja jõuab tehinguni, tõuseb hind 104-ni. Hind jõuab hiljem 106-ni.

1. Saate-eelne tootlus: $106/100-1=6\%$.
2. Kuulaja teostatav brutotootlus: $106/104-1\approx1.923\%$.
3. Kui sama ajavahemiku kogukulu on lihtsustatult 0,3 protsendipunkti, jääb ligikaudu 1,623%.
4. Kui sobiv võrdlusindeks teenis 2%, ei tõenda hinnatõus eksperdi lisaväärtust.

**Praktiline töövõte:** loo prognoosipäevik, kuhu lisad ka prognoosi põhjuse ja tingimuse, mille täitumisel väide on ümber lükatud. Erista seletamise oskus, prognoosimise oskus ja tehingu kasumlikkus.

**[HARJUTUS]** 20 soovitusest 14 tõid +1% ja kuus −4%. Eelda iga tehingu puhul sama europositsiooni ja kulude puudumist. Leia keskmine tehingutootlus. **[KONTROLL]** Kas 70% tabavus tähendab head strateegiat?

<details><summary>Vastus ja põhjendus</summary>

$(14\cdot1\%-6\cdot4\%)/20=-0.5\%$. Kõrge tabavus ei korva suuremaid kaotusi. Tegemist on võrdsete positsioonide keskmise tehingutootlusega, mitte järjestikku kogu kapitali investeerimise liittootlusega. Vajame ka kahjumite suurust, positsioone, kulusid ja riski.

</details>

**Seos:** sama põhimõte kordub peatükkides 6–8: hea mulje või üks number ei asenda korrektset hindamismeetodit.

## 2. Turu tõhususe hüpotees ja Schwageri kriitika

**Allikas:** peatükk 2, PDF lk 22–49. **Õpieesmärk:** lahutada väide turu tõhususest väitest, et konkreetne inimene suudab turgu võita.

**[RAAMAT]** Autor kritiseerib käsitlust, mille järgi hinnad kajastavad infot nii täielikult, et püsiv ületootlus oleks vaid õnn. Ta kasutab muu hulgas internetimulli, hüpoteeklaenudel põhinevaid väärtpabereid, Palm/3Comi hinnastamisvastuolu, suuri turulangusi ja Medallioni tulemusi. Hindade kujunemisel loevad lisaks fundamentaalnäitajatele emotsioonid, erinevad eesmärgid ja sundtehingud. Kõik turuosalised ei maksimeeri samal viisil investeerimiskasumit: näiteks riskimaandajal on teine eesmärk kui spekulandil.

**[SELGITUS]** Turu tõhususe klassikalised vormid erinevad selle poolest, milline info peaks juba hinnas olema:

| Vorm | Hinnas kajastuv info | Mida see seab kahtluse alla? |
|---|---|---|
| Nõrk | Varasemad hinnad ja kauplemisandmed | Süsteemne ületootlus ainult ajalooliste hindade põhjal |
| Pooltugev | Kogu avalik info | Avaliku info lihtne kasutamine riskiga korrigeeritud ületootluseks |
| Tugev | Ka mitteavalik info | Ületootlus isegi informatsioonilise eelise korral |

Tõhususe hüpotees ei nõua iseenesest normaaljaotust ega tähenda, et kõigi varade õiglane väärtus oleks vaieldamatult teada. Empiiriline kontroll sõltub ka mudelist, millega „õiget” riskiga korrigeeritud tootlust hinnatakse: see on **ühishüpoteesi probleem**. Raamatu mõni kriitika käsitleb tõhusust koos teiste mudelieeldustega; neid tuleb analüüsis lahus hoida.

**[NÄIDE]** Sama rahavoogu esindav vara maksab ühel turul 100 ja teisel 102. Näiline vahe on 2. Kui ostu-, müügi-, laenu- ja maandamiskulud on kokku 2,5, pole lihtne arbitraaž kasumlik. Isegi kulude puudumisel võivad tehingute ajastus, laenamise võimalus ja ajutiselt suurenev hinnavahe tekitada riski.

**Praktiline järeldus:** erista nelja sammu: märkan vastuolu → saan seda kaubelda → suudan ebasoodsa vaheperioodi üle elada → teenin pärast kulusid riskiga põhjendamata ületootlust. Ükski nool pole automaatne.

**[HARJUTUS]** 1000 sõltumatut kauplejat ennustavad igal aastal turu suunda juhuslikult õigesti tõenäosusega 1/2. Kui palju on oodatavalt viie järjestikuse õnnestumisega kauplejaid? **[KONTROLL]** Kas ühe eduka kaupleja leidmine tõestab oskust?

<details><summary>Vastus ja põhjendus</summary>

$1000(1/2)^5=31.25$. See on oodatav arv, mitte garanteeritud tulemus. Edukate inimeste tagantjärele valimine tekitab valikuefekti. Oskuse hindamiseks on vaja pikemat, sõltumatut ja kulusid arvestavat tõendit ning sobivat riskivõrdlust. Arvutus ei tõesta omakorda, et kõik edukad kauplejad on õnnelikud juhused.

</details>

### Täiendav juhtum: miks riskide pakkimine ei kaota ühist riski?

**[RAAMAT]** Peatükk 2 käsitleb hüpoteeklaenudest moodustatud väärtpabereid ja CDO-sid. Oluline probleem oli madala kvaliteediga aluslaenude hindamine eeldustega, mis pärinesid teistsugusest laenukeskkonnast, ning laenupakettide riskide sõltuvuse alahindamine.

**[SELGITUS]** Väärtpaberistamisel suunatakse laenude rahavood eri nõudejärkudesse ehk tranche'idesse. Esimesed kahjumid kannab allutatud osa, seejärel järgmised kihid. Kõrgema nõudejärgu parem kaitse sõltub sellest, kui palju kogukahjumit enne seda ära neelatakse. Laenude arvu kasvatamine ei kõrvalda ühist kinnisvarahinna või refinantseerimise šokki. Juba riskantsete vahekihtide uuesti kokkupakkimine võib koondada sarnase kriisitundlikkuse.

**[NÄIDE]** Laenuportfelli maht on 100. Esimese kahjumi kiht on 10, keskmine kiht 10 ja kõrgem kiht 80. Kogukahjum 8 tabab ainult esimest kihti. Kogukahjum 25 hävitab kaks esimest kihti ja vähendab kõrgemat 5 võrra ehk 6,25%. Hinnang „kõrgem kiht ei saanud senises valimis kahju” ei tõesta, et tulevane kahjum ei saa ületada 20.

**[KONTROLL]** Miks ei piisa teadmisest, et igal üksiklaenul on väike maksejõuetuse tõenäosus? **Vastus:** kogukahjum sõltub ka ühise maksejõuetuse seosest, kahjumist maksejõuetuse korral ja kontsentratsioonist. Üksikriskide marginaalsed tõenäosused ei määra nende ühisjaotust.

## 3. Minevikutootluse türannia

**Allikas:** peatükk 3, PDF lk 50–72. **Õpieesmärk:** vältida hiljutise võitja mehaanilist eelistamist.

**[RAAMAT]** Autor uurib aktsiaturu tulemusi tugeva ja nõrga tootlusega perioodide järel, sektorite valikut ning riskifondistrateegiate järjestusi. Mineviku kõrge tootlus võib peegeldada tingimusi, mis ei kordu. Suur hinnatõus võib vähendada tulevast tootluspotentsiaali, kui ostuhind on kasvanud kiiremini kui majanduslik väärtus. Tema ajaloolised võrdlused toetavad ettevaatust hiljutiste võitjate tagaajamisel.

**[SELGITUS]** Eristame kolme võimalikku mehhanismi. **Püsivus** tähendab, et eelis jätkub; **keskmise poole taandumine**, et ebatavaliselt hea või halb tulemus normaliseerub; **režiimimuutus**, et varasem seos kaob. Need võivad sõltuda ajahorisondist. Väide „ära osta ainult minevikutootluse põhjal” ei võrdu väitega „osta alati kõige rohkem langenud vara”. Madal hind võib peegeldada püsivalt halvenenud äri.

**[NÄIDE]** Ettevõtte aastakasum aktsia kohta on 5 eurot. Hind tõuseb 50-lt 100-ni, kasum ei muutu.

1. Esialgne P/E on $50/5=10$.
2. Uus P/E on $100/5=20$.
3. Kasumitootlus $E/P$ langeb 10%-lt 5%-le.
4. Varasem 100% hinnatootlus ei tähenda, et järgmise ostja võimalused paranesid.

See ei määra õiglast hinda: vaja on tulevase kasvu, kapitalivajaduse, riski ja diskontomäära hinnangut. Näide näitab ostuhinna rolli, mitte konkreetset hindamisreeglit.

**[HARJUTUS]** Fond teenis 30%, sest tema investeeritud sektor tõusis 35%. Teine fond teenis 10%, sektor 4%. Kas esimene fondijuht oli osavam? **[KONTROLL]** Mida kontrolliksid enne fondide võrdlemist?

<details><summary>Vastus ja põhjendus</summary>

Lihtne erinevus sektorist on esimesel −5 ja teisel +6 protsendipunkti. Sellest ei piisa oskuse järjestamiseks: kontrolli beetasid, võimendust, perioodi, riski, tasusid ja võrdlusindeksi sobivust. Esimese fondi suurem absoluuttootlus üksi ei tõenda paremat tööd. Teise fondi +6 punkti ei ole automaatselt mudelipõhine alfa.

</details>

## 4. Riski väär mõõtmine

**Allikas:** peatükk 4, PDF lk 73–87. **Õpieesmärk:** koostada riskihinnang, mis sisaldab ka seni realiseerumata ohte.

**[RAAMAT]** Ekslikult väike riskinäitaja võib olla ohtlikum kui mõõdiku puudumine, sest tekitab põhjendamatu kindlustunde. Autor eristab tavapärases tootlusreas nähtavat kõikumist ja varjatud riske: turu-, krediidi-, likviidsus-, võimendus- ja sündmusriski ning volatiilsuse müügist tulenevat ohtu. Madala volatiilsusega ajalugu võib pärineda strateegiast, mis teenib enamasti vähe, kuid kaotab harva väga palju.

**[NÄIDE]** Strateegia annab ühel perioodil 99% tõenäosusega +1% ja 1% tõenäosusega −80%.

1. Oodatav lihttootlus on $0.99\cdot0.01+0.01\cdot(-0.80)=0.0019=0.19\%$.
2. 60 sõltumatu perioodi jooksul katastroofi puudumise tõenäosus on $0.99^{60}\approx54.72\%$.
3. Seega võib väga ohtlikul strateegial olla pikk täiesti sile tootlusajalugu.
4. Logaritmilise kasvu ootus on $0.99\ln(1.01)+0.01\ln(0.20)\approx-0.00624$ perioodi kohta. Positiivne oodatav lihttootlus ei taga positiivset pikaajalist liitkasvu.

**[SELGITUS]** Need tõenäosused on õppemudeli eeldused, mitte hinnang ühelegi fondile. Kaheaastane ajalugu ei saa tõestada, et üks-kord-sajandis tüüpi ohtu pole.

### Kuidas varjatud riski otsida?

| Kontroll | Mida uurida? | Miks ajalooline standardhälve ei piisa? |
|---|---|---|
| Tuluallikas | Kas tulu tuleb kindlustuse müümisest või krediidiriskist? | Rahulik periood võib peita suure ühekordse kahju |
| Likviidsus | Kauplemismaht, hinnavahe, väljumise aeg | Harvad hinnapakkumised võivad tootlust siluda |
| Rahastamine | Tagatisnõuded ja laenu tagasikutsumine | Sundmüük võib tekkida hinnalangusega samal ajal |
| Ühine faktor | Beeta, krediidimarginaal, turu languskuud | Erinevad nimed võivad jagada sama riski |
| Protsess | Sõltumatu hinnastamine ja varade hoidmine | Pettus ja arvestusvead ei ilmne tootluse hajuvusest |

VaR tasemel 99% on mudeli järgi kahjumi 99. protsentiil, **mitte suurim võimalik kahju**. See ei kirjelda, kui suur on kahju piiri ületamisel. Expected Shortfall vaatab halvimasse sabasse jäävate kahjude keskmist; ka see sõltub andmetest ja mudelist. Aja skaleerimine ruutjuure abil vajab eeldusi ega ole üldine riskiseadus.

**[HARJUTUS]** Fondi ühe päeva 99% VaR on 3%. Kas 8% päevakahjum muudab mudeli loogiliselt võimatuks? **[KONTROLL]** Miks ei taga stop-loss alati kahjumi piiramist täpselt määratud tasemele?

<details><summary>Vastus ja põhjendus</summary>

Ei. Mudel jätab 1% tõenäosuse VaR-i ületamiseks; üks ületus pole iseenesest vastuolu. Tuleb hinnata ületuste sagedust, sõltuvust ja suurust. Stop-loss võib hinnahüppe või vähese likviidsuse tõttu täituda halvema hinnaga. Piiratud kahjumiga tehingud võivad samuti kordudes tekitada suure kumulatiivse kaotuse.

</details>

## 5. Volatiilsus, liittootlus ja võimendusega ETF-id

**Allikas:** peatükk 5, PDF lk 88–95. **Õpieesmärk:** mõista, miks päevane võimendustegur ei kirjelda pika perioodi tootlust.

**[RAAMAT]** Kõikumine mõjutab lisaks riskile liitkasvu. Päevaselt tasakaalustatava võimendusega ETF-i tulemus võib erineda oluliselt alusvara mitme päeva tootluse korrutamisest võimendusteguriga.

**[SELGITUS]** Kui fond seab iga päeva alguses võimenduse $L$, on ideaalne, kuludeta päevatootlus $Lr_t$ ja mitme päeva tulemus:

$$R_L=\prod_t(1+Lr_t)-1,$$

mis üldjuhul ei võrdu $L[\prod_t(1+r_t)-1]$. Tulemuse määravad päevade tootlused ja nende kõikumine, mitte üksnes alusvara alg- ja lõpphind. Päevatootluste ümberjärjestamine üksi ei muuda seda ideaalset korrutist.

**[NÄIDE]** Indeks liigub 100 → 110 → 100.

1. Esimene päev: +10%.
2. Teine päev: $100/110-1=-9.0909\%$.
3. Päevane 2× fond: $100\cdot1.20\cdot(1-0.181818)=98.1818$.
4. Indeksi kogutootlus on 0%, fondil ligikaudu −1,82%, enne tasusid ja muid kõrvalekaldeid.

Võrdluseks annavad kaks järjestikust +10% päeva indeksile 21% ning ideaalsele 2× fondile 44%, mis ületab 42%. Seega ei ole õige väita, et päevase võimendusega fond peab alati pika perioodi lihtsast kordajast maha jääma.

Väikeste tootluste ja stabiilsete tingimuste korral aitab mõelda lähend $g\approx\mu-\sigma^2/2$, kus $g$ tähistab ligikaudset logaritmilist kasvumäära, $\mu$ keskmist lihttootlust ja $\sigma^2$ dispersiooni samas ajaühikus. See on lähend, mitte täpne üldvalem. Sama aritmeetilise keskmise juures vähendab suurem hajuvus tavaliselt liitkasvu.

**[HARJUTUS]** Indeksi päevatootlused on +5% ja −5%. Leia indeksi ja ideaalse päevase 3× fondi kogutootlus. **[KONTROLL]** Miks ei piisa prognoosist „indeks on aasta lõpuks kõrgemal”?

<details><summary>Vastus ja põhjendus</summary>

Indeks: $1.05\cdot0.95-1=-0.25\%$. Fond: $1.15\cdot0.85-1=-2.25\%$. Kolm korda indeksi kogutootlus oleks −0,75%, mitte −2,25%. Aasta lõpptulemus ei määra vahepealseid päevatootlusi ega fondi rahastamis- ja halduskulusid.

</details>

## 6. Tootlusajaloo lõksud

**Allikas:** peatükk 6, PDF lk 96–102. **Õpieesmärk:** hinnata, kas ajalugu kirjeldab tänast strateegiat ja võrreldavat keskkonda.

**[RAAMAT]** Viis peamist lõksu on varjatud risk, tuleviku jaoks ebaolulised andmed, suure riskiga saavutatud hea tulemus, võrreldamatute fondide võrdlemine ning pikk ajalugu, mille varasem osa ei esinda enam praegust tegevust. Autor toob näiteks olukorra, kus pikaajaline võlakirjatõus kajastas intresside langust; sama ajaloo kordumine pole iseenesest põhjendatud.

**[SELGITUS]** Pikk valim aitab vaid siis, kui selle sisu on asjakohane. Kontrolli strateegia, juhi, kapitalimahu, instrumentide, tasude ja tehingukulude muutumist. Väikese fondi võimalik eelis võib suureneva mahu tõttu kaduda: sama tehingut ei saa lõputult suurendada ilma hinda mõjutamata.

**[NÄIDE]** Fond A tegutseb 15 aastat ja selle suurim kapitalilangus on 30%. Fond B tegutseb kolm aastat ja suurim langus on 8%.

1. Esmane võrdlus näib soosivat B-d.
2. Võta ühine kolmeaastane periood. A langus oli selles 6%.
3. Nüüd pole B samas keskkonnas väiksema langusega.
4. A 30% episoodi ei tohi kustutada: see annab stressiinfot, mida B ajaloo kohta lihtsalt pole.

Õige tulemus on kaks eraldi vaadet: **võrdlus ühisel ajavahemikul** ja **iga fondi kogu teadaolev stressikogemus**. Võrdne periood parandab võrreldavust, kuid ei võrdsusta automaatselt turge ega riske.

**[HARJUTUS]** Fond vahetas kaks aastat tagasi nii juhti kui strateegiat. Müügimaterjal reklaamib kümneaastast Sharpe'i suhtarvu. Kuidas hindaksid materjali? **[KONTROLL]** Kas vanad andmed tuleks täielikult eemaldada?

<details><summary>Vastus ja põhjendus</summary>

Eralda vana ja uus režiim, nõua muutuse kuupäeva ja praeguse strateegia eraldi tulemusi. Kümneaastane suhtarv võib segada kahte erinevat protsessi. Vana ajalugu säilita läbipaistvuse jaoks, kuid ära omista seda automaatselt praegusele juhile ega mudelile. Uue strateegia lühike ajalugu jätab suure ebakindluse.

</details>

## 7. Pro forma: kasulik kohandus või tagantjäreletarkus?

**Allikas:** peatükk 7, PDF lk 103–104. **Õpieesmärk:** hinnata tulemuste ümberarvutamise põhjendatust.

**[RAAMAT]** Sama termin võib tähistada nii eksitavat hüpoteetilist ajalugu kui ka tegelikust vanast tasustruktuurist asjakohasemat kulukohandust. Keskne küsimus on, kas arvutusse on peidetud tagantjäreletarkus.

**[NÄIDE]** Uus fondifond valib täna kümnest fondist kolm parimat ja näitab nende viimase viie aasta keskmist tootlust „oma ajaloona”. Isegi kui kõigi kolme fondi algandmed on päris, on valik tehtud tulemust teades. Sellist minevikuportfelli ei pruukinud olla võimalik tolleaegse infoga valida.

**[SELGITUS]** Vastupidine näide: strateegia tehingud on teada ja tehingutasu on muutunud. Sama tehingute rea arvutamine uue tasuga võib anda kasuliku võrdluse. See ei tõesta, et uute tingimuste juures oleksid käitumine, likviidsus ja tehingumahud olnud identsed; see on tingimuslik kohandus.

Praktiline kontroll koosneb neljast küsimusest: milline oli otsuse tegemise hetkel teadaolev info; kas reegel oli siis fikseeritud; milliseid variante enne selle valimist katsetati; kas tulemust kontrolliti kasutamata andmetel? Andmete jagamine ei päästa testi, kui arendaja kohandab mudelit korduvalt sama testvalimi järgi.

**[HARJUTUS]** 100 tehingu vana kogukulu on 500 eurot ja uus oleks sama tehingurea korral 300 eurot. Brutokasum on 1400 eurot. Leia mõlemad netokasumid. **[KONTROLL]** Miks erineb see parimate fondide tagantjärele valimisest?

<details><summary>Vastus ja põhjendus</summary>

Vana netokasum on 900 ja korrigeeritud netokasum 1100 eurot. Tehingud jäid samaks ning muudeti avalikult ainult kulueeldust. Fondide tagantjärele valimisel muudeti tulemuse teadmisel investeerimisotsust ennast. Ka kulukohandus peab jääma selgelt märgistatud hüpoteetiliseks tulemuseks.

</details>

## 8. Kuidas hinnata varasemat tulemuslikkust?

**Allikas:** peatükk 8, PDF lk 105–126; lisa B, lk 220–222. **Õpieesmärk:** valida küsimusele vastav mõõdik ja mõista, millist infot see välja jätab.

**[RAAMAT]** Tootlus ilma riskita on puudulik võrdlus. Võimenduse tõstmine võib kasvatada tootlust ilma oskust parandamata. Schwager käsitleb Sharpe'i, Sortino, sümmeetrilise langusriski Sharpe'i, gain-to-pain-, tail-, MAR-, Calmar- ja return retracement-suhtarvu. Ta rõhutab ka logaritmilist väärtuskõverat, libisevate perioodide tootlust ning kapitalilanguse graafikuid.

**[SELGITUS]** Mõõdikut tuleb valida küsimuse järgi, mitte otsida ühte „võitjanumbrit”.

| Küsimus | Sobiv lähtekoht | Mida juurde kontrollida? |
|---|---|---|
| Kui hästi tasustati kogu kõikumist? | Sharpe | Jaotuse kuju, autokorrelatsioon, varjatud risk |
| Kui hästi tasustati lävendist allapoole jäävaid tulemusi? | Sortino või SDR-Sharpe | Lävend, aastastamine, nimetaja definitsioon |
| Kui suur oli netotulu võrreldes kaotusperioodidega? | GPR | Ei arvesta kahjumite järjestust |
| Kas äärmuslikud tulemused on soodsalt või ebasoodsalt viltused? | Tail ratio | Väikese sabavalimi ebakindlus |
| Kui suur oli kasv suurima languse suhtes? | MAR, Calmar | Üks sündmus ja vaatlusperioodi pikkus |
| Kui sügavad olid eri ajahetkede halvimad tagasilangused? | RRR, 2DUC | Tagasivaatav iseloom ja andmete piisavus |

### Lahendatud minianalüüs

**[NÄIDE]** Neli kuutootlust on +4%, −2%, +3%, −1%. Riskivaba tootlus on selles õppemudelis null.

1. Aritmeetiline kuutootlus: $(4-2+3-1)/4=1\%$.
2. Lõppväärtus 100 korral: $100\cdot1.04\cdot0.98\cdot1.03\cdot0.99=103.927824$.
3. Kogutootlus: 3,927824%.
4. Valimi standardhälve: $\sqrt{(3^2+(-3)^2+2^2+(-2)^2)/3}\approx2.9439\%$.
5. Kuine Sharpe: $1/2.9439\approx0.3397$. Tavapärane aastastatud hinnang: $0.3397\sqrt{12}\approx1.1767$.
6. GPR: $(4-2+3-1)/(2+1)=4/3\approx1.3333$.
7. Väärtusrida: 100 → 104 → 101,92 → 104,9776 → 103,927824. Suurim langus tipust on 2%.

Nelja kuu Sharpe ei ole usaldusväärne oskusetõend. Arvutus on korrektne, kuid hinnangu täpsus on nõrk. Samuti ei ole nelja kuu põhjal aastastatud kasvumäär järgmise aasta prognoos.

### Mida graafikult vaadata?

- **Logaritmiline NAV-graafik:** võrdne vertikaalne muutus tähendab võrdset suhtelist muutust; sobib pika kasvu võrdlemiseks. Lineaarne graafik on endiselt kasulik eurodes muutuse vaatamiseks.
- **Libisev 12 või 24 kuu tootlus:** näitab eri sisenemishetkede tulemusi sama hoidmisaja jooksul. Kattuvad aknad pole sõltumatud vaatlused.
- **Underwater-graafik:** näitab kaugust varasemast tipust ja aega, mil investor on tipust allpool.
- **2DUC:** lisab varasemast tipust langusele hilisema madalaima väärtuseni languse vaate. See on tagasivaatav analüüs, mitte reaalajas teadaolev signaal.

**[HARJUTUS]** Fondi CAGR on 12%, suurim kapitalilangus 24%. Leia MAR-suhtarv. Teisel fondil on samad arvud, kuid esimese ajalugu on kümme ja teisel kaks aastat. Kas risk on võrdne? **[KONTROLL]** Miks võib negatiivse Sharpe'i järgi järjestamine eksitada?

<details><summary>Vastus ja põhjendus</summary>

MAR = $0.12/0.24=0.5$. Sama suhtarv ei võrdsusta ajalooperioode ega varjatud riske. Negatiivse liigtootluse korral võib suurem standardhälve muuta Sharpe'i vähem negatiivseks ja näiliselt „paremaks”, kuigi risk suurenes. Negatiivne Sharpe annab infot negatiivse ajaloolise liigtootluse kohta, kuid selle põhjal lihtne paremusjärjestus on probleemne.

</details>

## 9. Korrelatsioon: mida see näitab ja mida mitte?

**Allikas:** peatükk 9, PDF lk 127–137. **Õpieesmärk:** eristada lineaarset seost, tundlikkust ja ühise kahjumi tõenäosust.

**[RAAMAT]** Madal korrelatsioon ei välista mittelineaarset sõltuvust. Kõrge korrelatsioon ei tõesta põhjuslikkust ega tähenda automaatselt, et fond kaotab turu languskuudel. Autor soovitab vaadata koos korrelatsiooni, beetat, positiivsete kuude osakaalu turu languskuudel ja keskmist tootlust neil kuudel.

**[SELGITUS]** Pearsoni korrelatsioon $\rho$ mõõdab standardiseeritud lineaarset seost. Beeta mõõdab lineaarse regressiooni tõusu:

$$\beta=\frac{\operatorname{Cov}(r_F,r_M)}{\operatorname{Var}(r_M)}=\rho\frac{\sigma_F}{\sigma_M}.$$

Regressioonis $r_F=\alpha+\beta r_M+\varepsilon$ ei ole beeta täielik tootlusprognoos: alles jäävad vabaliige ja jääk. Ühe seletava muutujaga, vabaliiget sisaldavas vähimruutude regressioonis on $R^2=\rho^2$. See kirjeldab valimis lineaarse mudeliga seletatud varieeruvust, mitte põhjusliku mõju protsenti.

**[NÄIDE 1]** Olgu turu tootlused −2%, 0%, +2% ja fondi tootlus igal kuul $1\%+0.1r_M$. Fondi tulemused on +0,8%, +1%, +1,2%. Korrelatsioon on +1, beeta 0,1 ning kõik fondi kuud on positiivsed. Täiuslik korrelatsioon ei võrdu ühiste kahjumitega.

**[NÄIDE 2]** $x=(-2,-1,0,1,2)$ ja $y=x^2$. Korrelatsioon on null, kuid $y$ on täielikult $x$-ist määratud. Optsioonistrateegias võib sarnane mittelineaarsus olla majanduslikult oluline.

**Praktiline töövõte:** arvuta seosed tootlustest, mitte ainult pikaajalist trendi näitavatest hinnatasemetest. Vaata hajuvusdiagrammi, eri režiime ja äärmuskuusid. Ühine ajatrend võib tekitada näilise seose muidu sisuliselt sõltumatute nähtuste vahel.

**[HARJUTUS]** Fondi volatiilsus on 30%, turul 15% ja korrelatsioon 0,4. Leia beeta. Fond on turu kümnest languskuust kuuel plussis: üheksa kuu tulemus on +1% või −1%, kümnendal −20%. **[KONTROLL]** Kas „60% languskuudest plussis” on piisav? Täpselt: kuus +1%, kolm −1%, üks −20%.

<details><summary>Vastus ja põhjendus</summary>

Beeta on $0.4\cdot30/15=0.8$. Languskuude keskmine fonditootlus on $(6-3-20)/10=-1.7\%$. Positiivsete kuude sagedus peidab suure kahjumi. Mõlemad tingimuslikud näitajad on vajalikud, kuid ka need ei asenda detailset sabariski analüüsi.

</details>

<a id="osa2"></a>
## II osa. Riskifondid kui investeerimisstruktuurid

**Lugemismärkus:** „riskifond” on siin ingliskeelse *hedge fund* vaste, mitte riskikapitalifond. Raamatu tasude, investorite ligipääsu ja regulatsiooni kirjeldused pärinevad ilmumisajast. Allpool õpetatakse struktuuride loogikat, mitte kehtivaid õiguslikke nõudeid ega tänaseid turutingimusi.

## 10. Riskifondide päritolu: mida tähendab hedge?

**Allikas:** peatükk 10, PDF lk 139–144. **Õpieesmärk:** eristada turu suunariski, väärtpaberivalikut ja brutopositsiooni.

**[RAAMAT]** Alfred Winslow Jonesi mudel ühendas pikad ja lühikesed aktsiapositsioonid ning võimenduse. Idee oli vähendada üldise turusuuna mõju ja suurendada väärtpaberivaliku osakaalu tulemuses. Ajalooline nimetus ei taga, et kõik hilisemad riskifondid tegelikult tururiski maandavad.

**[SELGITUS]** Pikk positsioon võidab hinnatõusust. Lühikese positsiooni lihtmudelis müüakse laenatud väärtpaber ja ostetakse see hiljem tagasi. Hinnatõus tekitab kahjumi; lisanduvad laenukulud, dividendide hüvitamine ning võimalik kohustus positsioon sulgeda.

Kui pika poole turuväärtus on $L$, lühikese poole absoluutväärtus $S$ ja omakapital $E$:

$$\text{brutoekspositsioon}=(L+S)/E,\qquad\text{netoekspositsioon}=(L-S)/E.$$

**[NÄIDE]** Omakapital on 100, pikad positsioonid 120 ja lühikesed 80. Brutoekspositsioon on 200%, netoekspositsioon 40%.

- Kui mõlemad pooled tõusevad 10%, on kasum $12-8=4$, seega 4% omakapitalist.
- Kui pikk pool tõuseb 12% ja lühikeseks müüdud aktsiad 6%, on kasum $14.4-4.8=9.6$, seega 9,6%.
- Kui pikad aktsiad langevad 10% ja lühikesed tõusevad 10%, kaotab fond $12+8=20$, kuigi netoekspositsioon oli vaid 40%.

**[HARJUTUS]** Omakapital 200, pikk pool 180, lühike 140. Leia bruto- ja netoekspositsioon. **[KONTROLL]** Kas netoekspositsioon null tähendab riskivaba portfelli?

<details><summary>Vastus ja põhjendus</summary>

Bruto $320/200=160\%$, neto $40/200=20\%$. Nullneto ei välista sektorite erinevust, ebaõnnestunud aktsiavalikut, erinevaid beetasid, likviidsus- ega laenuriski. Eurodes tasakaal ei võrdu kõigi faktorite maandamisega.

</details>

## 11. Riskifondide strateegiad ja lepingutingimused

**Allikas:** peatükk 11, PDF lk 145–154. **Õpieesmärk:** nimetada iga strateegia tuluallikas ja peamine viis, kuidas see võib ebaõnnestuda.

**[RAAMAT]** Riskifondid on väga erinevad. Neid ühendavad pigem paindlikud investeerimisvõimalused ja fondistruktuur kui üks ühine riskitase. Absoluutse tootluse eesmärk tähendab püüdu teenida eri turuolukordades, mitte lubadust alati kasumit saada.

| Strateegia | Tuluallika loogika | Peamine haavatavus |
|---|---|---|
| Long/short equity | Osta suhteliselt tugevamaid, müü nõrgemaid aktsiaid | Vale valik, netotururisk, short squeeze |
| Equity market neutral | Piira turufaktorit, teeni suhtelisest valikust | Tegelik faktorineutraalsus võib puruneda |
| Long bias / short bias | Püsivalt rohkem pikki / lühikesi positsioone | Vastassuunaline pikaajaline turuliikumine |
| Sektorifond | Sügav teadmine ühest sektorist | Sektori ühine šokk |
| Merger arbitrage | Ülevõtmishinna ja turuhinna vahe | Tehingu ebaõnnestumine, viivitus |
| Convertible arbitrage | Vahetusvõlakirja ja aktsia suhteline hinnastus | Krediidi-, likviidsus- ja dünaamilise maandamise risk |
| Statistical arbitrage | Statistilised suhtelise hinna kõrvalekalded | Mudeli lagunemine, ülerahvastatud tehingud |
| Fixed income arbitrage | Intressiinstrumentide suhtelised hinnavahed | Väikese vahe suure võimendusega kauplemine |
| Credit arbitrage | Krediidihinna erinevused, riskipreemia | Maksejõuetus ja krediidimarginaalide laienemine |
| Capital structure arbitrage | Sama ettevõtte eri nõuete hinnavahe | Vale hinnang nõuete järjekorrale ja taastumisväärtusele |
| Distressed | Raskustes ettevõtte nõuete võimalik taastumisväärtus | Pankroti tulemus, pikk ooteaeg, vähene likviidsus |
| Event driven | Ühinemine, jagunemine või restruktureerimine | Sündmuse tulemus ja ajastus |
| Emerging markets | Arenevate turgude erinevad võimalused | Poliitika, valuuta, likviidsus ja kohalik risk |
| Global macro | Makromajanduslikud trendid ja suhtelised hinnad | Vale suund, ajastus, ootamatu poliitikamuutus |
| Managed futures / CTA | Futuuride või valuutade strateegiad | Strateegiast sõltuv; trendijärgimisel külgsuunaline turg |
| Fund of funds | Teiste fondide valik ja ühendamine | Alusfondide riskid ning lisatasude kiht |

**[SELGITUS]** „Arbitraaž” nende strateegiate nimetuses ei tähenda alati riskivaba kasumit. Ka CTA ei võrdu automaatselt toorainetega ega trendijärgimisega. Trendijärgija liitub juba alanud liikumisega; ta võib pika trendi ajal teenida, kuid saada külgsuunalises turus korduvaid valesignaale. Diskretsiooniline juht teeb otsuseid kaalutluse alusel, süsteemne strateegia kasutab ette määratud reegleid; kumbki ei taga edu.

### Tingimused, mis muudavad investori tegelikku tulemust

- **Haldustasu** arvestatakse lepingus määratud varabaasilt.
- **Tulemustasu** sõltub kasumist ja lepingureeglist; see võib soodustada asümmeetrilist riskivõtmist.
- **High-water mark** on varasem väärtustipp, mille ületamine on tavaliselt uue tulemustasu eeltingimus, kuid täpne arvestus sõltub lepingust.
- **Lockup** piirab esialgset väljumist; **notice period** on etteteatamisaeg.
- **Gate** piirab väljamaksete mahtu; **side pocket** eraldab raskesti müüdavad varad, mille raha saabub hiljem.

**[NÄIDE]** 100 eurot teenib enne tasusid 10 eurot. Õppemudelis võetakse haldustasu 2 eurot algkapitalilt ja tulemustasu 20% allesjäänud 8 eurost. Tulemustasu on 1,60 ja investorile jääb 106,40. See ei ole universaalne tasuvalem: määrav on leping.

**[HARJUTUS]** Ülevõtupakkumine on 50 eurot, aktsia maksab 48. Tehingu õnnestumise korral saad 50, ebaõnnestumisel langeb hind 35-ni. Oletatav õnnestumistõenäosus on 90%. Leia oodatav rahaline kasum aktsialt ja nullkasumit andev tõenäosus. **[KONTROLL]** Kas 2-eurone hinnavahe on riskivaba?

<details><summary>Vastus ja põhjendus</summary>

Oodatav kasum on $0.9\cdot2+0.1\cdot(-13)=0.50$ eurot, ligikaudu 1,04% ostuhinnast enne kulusid ja ajaväärtust. Nullkasum: $2p-13(1-p)=0$, seega $p=13/15\approx86.67\%$. Väike tõenäosusviga võib oodatava kasumi kustutada. Ka tehingu kestus ja rahastamine loevad.

</details>

## 12. Riskifondi lisamine portfelli: taju ja tegelikkus

**Allikas:** peatükk 12, PDF lk 155–161. **Õpieesmärk:** hinnata strateegiat tegeliku portfellimõju järgi.

**[RAAMAT]** Schwager vaidlustab üldistuse, et riskifond on alati tavalisest aktsia-võlakirjaportfellist ohtlikum. Ta käsitleb hajutatud riskifondiportfellide ajaloolist käitumist ja managed futures-strateegiate erilist hajutusvõimalust. Samas eristab ta ühe fondi riski hajutatud portfelli riskist.

**[SELGITUS]** Autori ajalooline võrdlus ei tõesta kõigi riskifondide ohutust ega tänast paremust. Nähtav väiksem volatiilsus võib tulla osaliselt harvemast hinnastamisest või mittelikviidsetest varadest. Lisakasu tuleb hinnata pärast tasusid, võrreldaval perioodil ning stressis.

**[NÄIDE]** Olemasoleva portfelli aastane volatiilsus on 15%, lisataval strateegial 10% ja nende korrelatsioon null. Uus jaotus on 80% ja 20%:

$$\sigma_p=\sqrt{0.8^2\cdot0.15^2+0.2^2\cdot0.10^2}\approx12.17\%.$$

Kui oodatavad tootlused on vastavalt 8% ja 6%, on uus oodatav tootlus $0.8\cdot8\%+0.2\cdot6\%=7.6\%$. Volatiilsus vähenes koos oodatava tootluse mõningase langusega. Kas vahetus on kasulik, sõltub eesmärgist ja kogu riskipildist.

**[HARJUTUS]** Arvuta sama portfelli volatiilsus, kui korrelatsioon on 0,8. **[KONTROLL]** Kas trendijärgimine peab igas aktsiaturu krahhis kasumit teenima?

<details><summary>Vastus ja põhjendus</summary>

Dispersioonile lisandub $2\cdot0.8\cdot0.2\cdot0.15\cdot0.10\cdot0.8=0.00384$. Kogudispersioon on 0,01864, volatiilsus ligikaudu 13,65%. Trendijärgimine ei taga krahvikaitset: kiire suunamuutus, eelnev positsioon ja signaali viivitus võivad tekitada kahjumi. Pikk püsiv trend on teine olukord kui järsk langus koos kiire taastumisega.

</details>

## 13. Miks tundmatu tundub ohtlikum?

**Allikas:** peatükk 13, PDF lk 162–165. **Õpieesmärk:** märgata riskihinnangu psühholoogilist kallutatust.

**[RAAMAT]** Autor kasutab mõistulugu, et näidata, kuidas inimesed hindavad tuttavaid ja võõraid investeeringuid eri standarditega. Tuntud aktsia või fondikategooria võib tunduda turvaline ka siis, kui tegelik risk on suur; võõra nimega strateegia võib tekitada ebaproportsionaalset hirmu.

**[SELGITUS]** Tuttavlikkus pole riski mõõt. Samas ei ole ka võõras keerukas toode automaatselt parem. Kui investor ei suuda mõista hinnastamist, kulusid ja väljumist, on see sisuline piirang, mitte pelgalt eelarvamus. Eristame emotsionaalset ebamugavust ja põhjendatud teadmatust.

**[NÄIDE]** Portfell A koosneb ühe tuttava tööandja aktsiatest. Portfell B sisaldab mitut eri tuluallikaga strateegiat, kuid osa on mittelikviidsed. A puhul on silmapaistev koondumisrisk ja võimalik seos palgatuluga; B puhul likviidsus-, mudeli- ja struktuuririsk. Aus analüüs ei kuuluta kumbagi paremaks ainult nime järgi.

**Praktiline töövõte:** kirjuta esmalt riskiprofiil ilma tootenime ja turundustekstita. Seejärel võrdle: võimalik kahjum, kahjumi allikas, raha kättesaadavus, kulud, hinnastamise läbipaistvus ja teiste varadega ühine risk. Lisa „ei tea” sinna, kus infot napib.

**[HARJUTUS]** Koosta tuttava aktsiafondi ja tundmatu long/short-fondi jaoks samad viis küsimust. **[KONTROLL]** Miks ei piisa väitest „olen seda ettevõtet aastaid kasutanud”?

<details><summary>Vastus ja põhjendus</summary>

Näidisküsimused: millest tuleb tootlus; milline sündmus toob suure kahjumi; millised on kulud; kui kiiresti saan väljuda; kuidas käitutakse mu muu portfelli languse ajal? Toote tarbijana tundmine ei anna iseenesest infot ostuhinna, võlakoormuse, aktsionäri nõude ega portfelli koondumise kohta.

</details>

## 14. Miks fondifondid näivad üksikfondide indeksist kehvemad?

**Allikas:** peatükk 14, PDF lk 166–169. **Õpieesmärk:** tuvastada andmete koostamise mõju näilisele tootlusele.

**[RAAMAT]** Üksikfondide indeks võib näidata palju paremat tootlust kui reaalsete fondifondide indeks. Autor selgitab seda lisatasude kõrval andmebaaside kallutatusega. Fondifondi tegelik väärtusrida sisaldab alusfondidest saadud kasumeid ja kahjumeid ka siis, kui alusfond enam andmebaasile ei raporteeri.

| Kallutatus | Mehhanism | Mida kontrollida? |
|---|---|---|
| Survivorship bias | Kadunud või suletud fondid jäetakse välja | Kas surnud fondid on ajaloolises universumis? |
| Selection bias | Fond valib ise, kas tulemusi esitada | Kes andmebaasi puudub ja miks? |
| Backfill bias | Hiljem lisatakse valitud fondi varasem hea ajalugu | Millal fond esimest korda tegelikult raporteeris? |
| Termination bias | Kõige halvemad viimased kuud jäävad raporteerimata | Kas lõplikud kahjud on kaasatud? |
| Allocation bias | Indeks eeldab kaale või tasakaalustamist, mida investor ei saa teha | Kas jaotus on teostatav väljumispiirangutega? |

**[NÄIDE]** Kümme fondi alustavad võrdse kapitaliga. Üheksa teenivad +10%, üks kaotab −90%.

1. Kõigi kümne võrdkaaluline tootlus on $(9\cdot10\%-90\%)/10=0\%$.
2. Kui kaotanud fond eemaldatakse, näitab allesjäänute keskmine +10%.
3. Algselt kõigisse investeerinud fondifond ei saa oma kahjumit andmebaasist eemaldamisega tagasi.

**[SELGITUS]** Fondifondide andmed ei ole täiesti kallutusteta: valik ja ellujäämine võivad esineda ka nende endi tasandil. Autori eelistus kasutada neid realistlikuma üldvõrdlusena ei tähenda, et iga fondifond oleks hea investeering. Samuti ei ole indeks tingimata tegelikult ostetav portfell.

**[HARJUTUS]** Andmebaas säilitab surnud fondi, aga selle viimane raporteeritud kuu eelneb lõplikule −50% kahjumile. Kas survivorship-kallutatuse kõrvaldamine lahendas probleemi? **[KONTROLL]** Kas päris ajaloolised tootlused võivad moodustada eksitava indeksi?

<details><summary>Vastus ja põhjendus</summary>

Ei: alles jäi lõpetamisest tingitud kallutatus. Fond on nime poolest olemas, kuid lõppkahju puudub. Päris tootlused võivad olla eksitavad, kui fondide valik, perioodide lisamine või kaalud määratakse tagantjärele või pole teostatavad.

</details>

## 15. Võimenduse eksijäreldus

**Allikas:** peatükk 15, PDF lk 170–173. **Õpieesmärk:** hinnata võimendust koos positsioonide sisuga.

**[RAAMAT]** Võimendus on tööriist. Risk sõltub nii aluspositsioonidest kui nende suurusest ja rahastamisest. Täiendav maandav positsioon võib suurendada brutoekspositsiooni, kuid vähendada mõnda olulist riski. Üks jäik võimenduspiir ei kirjelda kõigi strateegiate riski võrdselt.

**[SELGITUS]** Fikseeritud strateegia proportsionaalne suurendamine tavaliselt suurendab selle hinnariski. Sellest ei järeldu, et kaks täiesti erinevat strateegiat oleksid võimenduse järgi järjestatavad. Samuti ei kao rahastusrisk siis, kui tavapärane hinnavolatiilsus on väike.

**[NÄIDE]** Portfell A on 100% ühe sektori aktsiates, aastane volatiilsus õppemudelis 25%. Portfell B on 3× suurendatud maandatud strateegia, mille võimenduseta volatiilsus on 4%. Lineaarses, kuludeta lähendis on B volatiilsus 12%, seega väiksem kui A-l. Kuid kui B kaotab likviidsuse ja tuleb tagatist lisada, võib see hinnang olla väga puudulik.

Rahastatud pika positsiooni ühe perioodi lihtmudel:

$$r_E=Lr_A-(L-1)i,$$

kus $L$ on varade suhe omakapitali, $r_A$ vara tootlus ja $i$ laenuintress samal perioodil. Tuletisinstrumentide nominaalväärtus ei ole alati selle valemiga otse võrreldav.

**[HARJUTUS]** Omakapital 100, varasid 200, laenu 100. Vara kaotab 15% ja perioodi laenukulu on 3%. Leia omakapitali lõppväärtus ja tootlus. **[KONTROLL]** Mis juhtub, kui laenuandja nõuab sulgemist enne perioodi lõppu?

<details><summary>Vastus ja põhjendus</summary>

Varade lõppväärtus 170, laenu koos intressiga tuleb tagastada 103. Omakapital 67, tootlus −33%. Valem: $2(-15\%)-1\cdot3\%=-33\%$. Vahepealne tagatisnõue võib sundida müüma ebasoodsal hetkel; lõpptähtaja mudel ei arvesta seda.

</details>

## 16. Eraldi hallatav konto

**Allikas:** peatükk 16, PDF lk 174–181. **Õpieesmärk:** mõista, kuidas omandi- ja kontrollistruktuur mõjutavad riski.

**[RAAMAT]** Managed account tähendab investori või tema esindaja nimel hoitavat kontot, millel varahaldur saab kokkulepitud piires kaubelda. Autor rõhutab läbipaistvust, raha liikumise kontrolli, varade eraldatust ja fondi väljumispiirangute vähendamist. Eriti sobiv on mudel likviidsetele strateegiatele; mittelikviidsete varade puhul on eelised piiratud.

**[SELGITUS]** „Oma konto” ei tähenda automaatselt ohutut kontot. Olulised on õigused, sõltumatu varahoid, aruandlus ja leping. Kui haldur saab vabalt raha välja kanda või positsioonid on ebaselgelt hinnatud, ei ole struktuuri lubatud eelised realiseerunud.

| Kontrollitav omadus | Küsimus |
|---|---|
| Omand | Kelle nimel on varad ja kellele kuulub nõue? |
| Raha liikumine | Kas haldur saab ainult kaubelda või ka välja kanda? |
| Hinnastamine | Kes kontrollib positsioonide väärtust? |
| Positsioonid | Kas investor või sõltumatu platvorm näeb tegelikku riski? |
| Väljumine | Kas alusvarad on müüdavad ja kui kiiresti raha laekub? |
| Kogukulu | Millised on haldus-, platvormi-, kauplemis- ja hoidmise kulud? |

**[NÄIDE]** Fondiosakut saab müüa kord kvartalis ja 60-päevase etteteatamisega. Eraldi konto hoiab likviidseid futuure, mille positsioonid saab lepinguliselt kiiresti sulgeda. Konto võib parandada kontrolli, kuid hinnašokk, turu sulgemine või tehingu täitmise probleem on endiselt võimalik. Fondi ja konto tootlused võivad erineda ka siis, kui konto välistab fondi mittelikviidsed tehingud.

**[HARJUTUS]** Haldur pakub suuremat läbipaistvust, kuid saab kontolt piiramatult raha välja kanda. Milline keskne eelis puudub? **[KONTROLL]** Kas eraldi konto kaotab krediidi- ja tururiski?

<details><summary>Vastus ja põhjendus</summary>

Puudub sõltumatu kontroll raha liikumise üle. Läbipaistvus võib aidata kõrvalekallet märgata, kuid ei asenda õiguste piiramist. Konto struktuur võib vähendada mõningaid pettuse- ja ligipääsuriske; alusvarade turu-, krediidi-, likviidsus- ja vastaspoole riskid jäävad.

</details>

### II osa järelsõna: fondi tootlus ja investori kogemus

**Allikas:** PDF lk 182–183. **[RAAMAT]** Schwager kritiseerib riskifondide hindamist ainult sektorisse eri ajal paigutatud dollarite kogutulemuse kaudu. Ta eristab investeeringu tootlust ja kapitali sissevoolu ajastuse mõju. Samuti nõustub ta, et kõrged tasud ja sektori kasv võivad investori tulemust kahjustada.

**[SELGITUS]** Ajakaalutud tootlus (TWR) aitab mõõta strateegiat väliste rahavoogude ajastusest sõltumatult. Rahakaalutud tootlus (MWR, sageli IRR) vastab investori tegelike rahavoogude küsimusele. Kumbki pole universaalselt „vale”: need vastavad eri küsimustele.

**[NÄIDE]** Investor paneb algul 100. Esimesel aastal teenitakse +50%, väärtus on 150. Ta lisab 900, kokku 1050. Teisel aastal kaotatakse 40%, lõppväärtus on 630.

- Strateegia kahe aasta TWR: $1.5\cdot0.6-1=-10\%$.
- Investor maksis kokku sisse 1000 ja sai lõpuks 630: rahaline kahjum 370.
- Aastane IRR lahendab $100(1+i)^2+900(1+i)=630$, millest $i\approx-34.73\%$.

Suur sissemakse enne halba aastat halvendab investori rahakaalutud tulemust. See ei muuda fondi enda periooditootlusi. Samas on investori kogemus majanduslikult päris, mitte mõõtmisviga.

**[HARJUTUS]** Mida kasutaksid fondijuhi hindamisel, kui sissemaksete ajastuse otsustab klient? Mida enda tegeliku rahalise kogemuse analüüsimisel?

<details><summary>Vastus ja põhjendus</summary>

Juhi strateegia võrdlemiseks sageli TWR-i, enda rahavoogude kogemuseks MWR-i koos eurodes kasumi ja kahjumiga. Kui juht kontrollib ise kapitali väljakutseid ja väljamakseid, võib ka rahavoogude ajastus kuuluda tema hindamise juurde.

</details>

<a id="osa3"></a>
## III osa. Portfelli koostamine

## 17. Hajutamine: miks kümnest ei pruugi piisata?

**Allikas:** peatükk 17, PDF lk 185–190. **Õpieesmärk:** eristada keskmist riskivähenemist konkreetse portfelli halvima juhtumi riskist.

**[RAAMAT]** Uuring, mille järgi peamine hajutuskasu saavutatakse väheste positsioonidega, võib rääkida tuhandete portfellide keskmisest. Üks investor elab läbi ühe portfelli tegeliku tulemuse. Schwager rõhutab juhuslikult halbade tulemuste koondumise riski ning ühe fondi erakorralise kahjumi mõju. Peatüki „investeeringud” on eeskätt varahaldurite portfellid, mitte lihtsalt üksikaktsiad.

**[SELGITUS]** Võrdkaalulise portfelli korral, kui üks fond kaotab osa $d$ ja kõik teised on muutumatud, on kogukahjum $d/n$. Nõrgalt sõltumatute riskide lisamine võib vähendada ühe katastroofi mõju ka siis, kui keskmine volatiilsus muutub vähe.

**[NÄIDE]** Üks fond kaotab 80%, teised ei muutu.

| Võrdkaaluliste fondide arv | Selle fondi kaal | Portfelli kahjum |
|---:|---:|---:|
| 5 | 20% | 16% |
| 10 | 10% | 8% |
| 20 | 5% | 4% |
| 40 | 2,5% | 2% |

Kui lisanduvate fondide kvaliteet on halvem või riskid kattuvad, ei pruugi kogutulemus paraneda. Samuti võib fondide arvu kasv suurendada tõenäosust, et *vähemalt üks* neist ebaõnnestub, kuid vähendada ühe ebaõnnestumise mõju. Sagedus ja kahju suurus on eri küsimused.

**[HARJUTUS]** Iga sõltumatu fondi katastroofi tõenäosus on 1%. Leia vähemalt ühe katastroofi tõenäosus kümne ja kahekümne fondi puhul. **[KONTROLL]** Kas suurem tõenäosus tähendab, et hajutamine oli halb?

<details><summary>Vastus ja põhjendus</summary>

$1-0.99^{10}\approx9.56\%$ ja $1-0.99^{20}\approx18.21\%$. See ei võrdle portfelli kahjumi suurust: kahekümne fondi korral on iga fondi kaal poole väiksem. Analüüsida tuleb kogu kahjumijaotust. Sõltumatuse eeldus on siin oluline ja finantsturul sageli ligikaudne või vale.

</details>

## 18. Hajutamine: millal rohkem tähendab vähem?

**Allikas:** peatükk 18, PDF lk 191–194. **Õpieesmärk:** tuvastada sama majandusliku panuse kordumine eri nimede all.

**[RAAMAT]** Positsioonide arvu kasvatamine võib vähendada hajutatust, kui lisatavad fondid on omavahel tugevalt seotud. Näiteks palju sarnaseid trendijärgijaid või sama tururiski kandvaid aktsiafonde võib käituda ühe suure positsioonina.

**[SELGITUS]** Võrdsete kaalude, ühesuguse volatiilsuse $\sigma$ ja kõigi paaride sama korrelatsiooni $\rho$ korral:

$$\sigma_p^2=\sigma^2\left(\rho+\frac{1-\rho}{n}\right).$$

Kui $\rho=0$, väheneb standardhälve kujul $\sigma/\sqrt n$. Kui $\rho>0$, jääb $n$ kasvades alles ühine riskitase $\sigma\sqrt\rho$. Valem ei hõlma erinevaid volatiilsusi ja kaale ega mittelineaarseid sõltuvusi.

**[NÄIDE]** Viis sõltumatut fondi, igaühe volatiilsus 10%, annavad portfelli volatiilsuseks $10\%/\sqrt5\approx4.47\%$. Nüüd lisatakse kümme omavahel identse tootlusega fondi, mis on esialgsetest viiest sõltumatud. Kõigil 15 fondil on võrdne kaal.

1. Viie algse fondi dispersioonipanus: $5(1/15)^2\cdot0.10^2$.
2. Kümme koopiat moodustavad ühe 10/15 kaaluga panuse: $(10/15)^2\cdot0.10^2$.
3. Kogudispersioon: $0.01\cdot105/225\approx0.004667$.
4. Volatiilsus: umbes 6,83% — rohkem kui enne.

**Praktiline töövõte:** rühmita fondid mitte turundusnime, vaid kaotust tekitava sündmuse järgi. Näiteks „krediidimarginaali laienemine”, „kiire trendipööre” ja „ühine sundmüük”.

**[HARJUTUS]** Iga fondi volatiilsus on 20% ja kõikide paaride korrelatsioon 0,5. Leia võrdkaalulise kümne fondi volatiilsus ning piirväärtus fondide arvu lõpmatul kasvul. **[KONTROLL]** Mida näitab keskmine paarikorrelatsioon ja mida mitte?

<details><summary>Vastus ja põhjendus</summary>

Kümne puhul $20\%\sqrt{0.5+0.5/10}\approx14.83\%$. Piirväärtus $20\%\sqrt{0.5}\approx14.14\%$. Ühise faktori risk jääb alles. Keskmine paarikorrelatsioon kirjeldab lineaarset koosliikumist, kuid võib varjata kaale, väga riskantset üksikkomponenti, klastreid ja ühiseid sabakahjumeid.

</details>

## 19. Robin Hoodi investeerimine: tasakaalustamine

**Allikas:** peatükk 19, PDF lk 195–201. **Õpieesmärk:** mõista sihtkaalude taastamise mehhanismi ja piiranguid.

**[RAAMAT]** Tasakaalustamisel vähendatakse suhteliselt kasvanud osakaale ja suurendatakse kahanenuid. Schwager näitab, kuidas see võib parandada mitme juhi portfelli tootluse-riski suhet. Ta ei väida, et meetod võidab alati; raamat käsitleb ka tasakaalustamise ühendamist võimendusega.

**[NÄIDE]** Kahel varal on kaks perioodi: A annab +20%, seejärel −10%; B annab −10%, seejärel +20%. Alguses on kummaski 50 eurot.

**Ilma tasakaalustamata:** A: $50\cdot1.20\cdot0.90=54$. B: $50\cdot0.90\cdot1.20=54$. Kokku 108.

**Tasakaalustades pärast esimest perioodi:** A on 60, B 45, kokku 105. Sihtkaal 50/50 tähendab 52,50 mõlemas; A-st müüakse 7,50 ja B-d ostetakse 7,50 eest. Teise perioodi lõpus $52.5\cdot0.90+52.5\cdot1.20=110.25$. Kogutootlus 10,25%, võrreldes 8%-ga ilma tasakaalustamata.

**[SELGITUS]** Tulemust toetab selles näites vastassuunaline liikumine. Kui üks vara püsivalt võidab ja teine kaotab, võib tasakaalustamine tulemust vähendada. Selle kindlam roll on riskijaotuse hoidmine, mitte garanteeritud lisatootlus. Arvestada tuleb kulusid, makse, hinnavahet ja väljumispiiranguid. Ühe ebaõnnestunud ettevõtte pidev juurdeostmine pole sama mis põhjendatud sihtjaotuse taastamine.

**[HARJUTUS]** A annab mõlemal perioodil +20%, B mõlemal −10%. Alusta jälle 50/50. Võrdle lõppväärtusi tasakaalustamisega ja ilma. **[KONTROLL]** Miks ei tõesta ühe tagasitesti võit universaalset paremust?

<details><summary>Vastus ja põhjendus</summary>

Ilma: $50\cdot1.2^2+50\cdot0.9^2=72+40.5=112.5$. Tasakaalustades on iga perioodi portfellitootlus 5%, seega $100\cdot1.05^2=110.25$. Tasakaalustamine jäi 2,25 euroga maha. Tulemused sõltuvad varade tootlusmustritest, kuludest ja valitud perioodist.

</details>

## 20. Kas suur volatiilsus on alati halb?

**Allikas:** peatükk 20, PDF lk 202–204. **Õpieesmärk:** hinnata uut vara kogu portfelli, mitte ainult eraldiseisva suhtarvu põhjal.

**[RAAMAT]** Madalama Sharpe'iga, kuid portfelliga negatiivselt seotud fond võib olla kasulikum lisandus kui eraldi vaadates parem fond. Teatud tingimustel võib kaitsvama komponendi suurem volatiilsus hoopis vähendada portfelli kogukõikumist.

**[SELGITUS]** Kahe komponendi korral:

$$\sigma_p^2=w_A^2\sigma_A^2+w_B^2\sigma_B^2+2w_Aw_B\rho\sigma_A\sigma_B.$$

Negatiivse korrelatsiooni korral vähendab viimane liige dispersiooni. See mõju ei kasva piiramatult: komponendi enda dispersiooniliige kasvab ruutselt. Järelikult ei saa väita „mida volatiilsem kaitse, seda parem”.

**[NÄIDE]** A volatiilsus on 20%, B-l 30%, korrelatsioon −0,5 ja kaalud 80/20:

$$\sigma_p^2=0.8^2\cdot0.2^2+0.2^2\cdot0.3^2+2\cdot0.8\cdot0.2\cdot(-0.5)\cdot0.2\cdot0.3=0.0196.$$

Portfelli volatiilsus on 14%, ehk vähem kui ainult A 20%. Kui B volatiilsus oleks 10% sama korrelatsiooni juures, oleks kogutase umbes 15,10%. Selles konkreetses võrdluses annab volatiilsem B tugevama tasakaalustava mõju.

**Praktiline töövõte:** võrdle alati „portfell enne” ja „portfell pärast”. Lisa hinnang netotootlusele, kriisiaegsele käitumisele ja kaitse kandmise kulule. Negatiivse ajaloolise korrelatsiooni tulevikus püsimine on eeldus, mitte lubadus.

**[HARJUTUS]** Arvuta näite kogurisk, kui korrelatsioon muutub nulliks. **[KONTROLL]** Kas kahjumlik kaitsekomponent võib olla mõistlik?

<details><summary>Vastus ja põhjendus</summary>

$\sqrt{0.0256+0.0036}=\sqrt{0.0292}\approx17.09\%$. See on endiselt väiksem kui ainult A puhul, kuid suurem kui negatiivse korrelatsiooniga juhul. Kaitse võib vähendada ebasobivaid portfellikahjumeid ka negatiivse eraldiseisva tootlusega; vaja on hinnata, kas kaitse kasu õigustab makstavat hinda ning kas kaitse tegelikult vajalikus olukorras toimib.

</details>

## 21. Portfelli koostamise põhimõtted

**Allikas:** peatükk 21, PDF lk 205–213. **Õpieesmärk:** ühendada mõõtmine, sisuline riskianalüüs ja selged otsustusreeglid.

**[RAAMAT]** Ajalooliste keskmistega optimeerimine võib anda matemaatiliselt täpse lahenduse valesti kirjeldatud probleemile. Autor pakub kaheksat põhimõtet. Alljärgnev on nende sisuline eestikeelne refereering, mitte sõnasõnaline tõlge.

1. Hinda tootlust koos riskiga, mitte eraldi.
2. Hinda tegelikke kaotusmehhanisme, mitte ainult volatiilsust.
3. Uuri, kas hea tulemus tuli oskusest või soodsast turust.
4. Hajuta piisavalt ka harvade suurkahjumite vastu, säilitades investeeringute kvaliteedi.
5. Eelista fondijuhtide ja strateegiate tegelikke omadusi jäikadele kategooriakastidele.
6. Vaata nii korrelatsioone kui ka ühiste kahjumite esinemist.
7. Arvesta jaotuses erinevaid riskitasemeid; võrdsed eurosummad ei tähenda võrdset riski.
8. Kui portfell on mõeldud aktsiariski tasakaalustama, uuri selle tulemust aktsiate languskuudel.

**[SELGITUS]** Viimane punkt on rollipõhine: positiivset tulemust enamikul aktsiate languskuudel ei pea nõudma igalt pikaajaliselt aktsiatesse investeerivalt portfellilt. Samuti ei muuda ligikaudne käsitsi jaotus sisendvigu olematuks. Optimeerija sobib eelduste tagajärgede uurimiseks, kui selle sisendid, piirangud ja ebakindlus on nähtavad.

### Riskipõhine lähtejaotus

Kui strateegiate muud omadused on võrdsed, võib lihtne lähtekoht olla $w_i\propto1/\sigma_i$. Volatiilsustega 10% ja 20% annab see kaalud 2/3 ja 1/3. Sel juhul on $w_i\sigma_i$ võrdsed.

See ei ole üldjuhul sama mis täpne riskipariteet. Portfelli volatiilsuse riskipanus on

$$RC_i=\frac{w_i(\Sigma w)_i}{\sigma_p},$$

kus $\Sigma$ on kovariatsioonimaatriks. Täpne riskipanus sõltub ka korrelatsioonidest. Võimenduse, mittelikviidsuse ja mittelineaarse sabariski korral ei pruugi volatiilsuse võrdsustamine üldse piisata.

### Ühiste kahjumite maatriks ehk CNR

Raamatu CNR (*coincident negative return*) vaatab tõenäosust, et rea fond kaotab, kui veeru fond kaotab. Null-lävendiga:

$$CNR_{ij}=\frac{\#\{r_i<0\ \text{ja}\ r_j<0\}}{\#\{r_j<0\}}.$$

See erineb korrelatsioonist ning on üldjuhul ebasümmeetriline. Kui fond A kaotab 4 kuud, B 8 kuud ja ühiseid kaotuskuusid on 3, siis $P(A-\mid B-)=3/8=37.5\%$, kuid $P(B-\mid A-)=3/4=75\%$.

Normaliseeritud variant võrdleb tingimuslikku sagedust fondi tavapärase kaotussagedusega:

$$NCNR_{ij}=\frac{P(i-\mid j-)}{P(i-)}.$$

Kui valim on 20 kuud, siis näites $P(A-)=4/20=20\%$ ja normaliseeritud väärtus on $0.375/0.20=1.875$. A kaotab B kahjumikuudel sagedamini kui juhuslikul kuul.

**Täpsustus:** sama ajavahemiku, samade lävendite ja ühise puuduvate andmete käsitluse korral on normaliseeritud näitaja $P(i-\cap j-)/(P(i-)P(j-))$ sümmeetriline. Toor-CNR ei ole. Väike tingimusele vastavate kuude arv teeb hinnangu ebakindlaks. Kahjumi sagedus tuleb siduda ka selle suurusega.

### Praktiline koostamisprotsess

1. Määra eesmärk, ajahorisont, rahavajadus ja talutav kahjum.
2. Koosta strateegiate loetelu koos tuluallika ja stressiriskidega.
3. Ühtlusta tootluste periood, valuuta, tasud ja rahavoogude käsitlus.
4. Arvuta mõõdikud, kuid vaata lisaks jaotust ja väärtuskõvera kulgu.
5. Uuri korrelatsiooni, beetat, languskuusid ja CNR-i.
6. Määra algkaalud ning koondumis- ja likviidsuspiirangud.
7. Võrdle tavarežiimi ja stressistsenaariumi.
8. Fikseeri tasakaalustamise, jälgimise ja strateegiast loobumise reeglid.

**[HARJUTUS]** Fond A kaotab 20 kuust neljal, B kaheksal, koos kaotavad kolmel kuul. Arvuta mõlemad CNR-id ja mõlemad normaliseeritud CNR-id. **[KONTROLL]** Miks ei tohi kogu portfelli valida ainult kõrgeima ajaloolise Sharpe'i järgi?

<details><summary>Vastus ja põhjendus</summary>

Toor-CNR: 37,5% ja 75%. Normaliseeritult $0.375/0.2=1.875$ ning $0.75/0.4=1.875$. Sharpe ei näita varjatud riski, tulevast režiimi ega lisandi mõju portfellile. Kõrgeima suhtarvu mehaaniline valik võib valida sama riski mitu korda ja üle sobitada juhuslikku minevikku.

</details>

<a id="optsioonid"></a>
## Lisa A. Optsioonide alused

**Allikas:** raamatu lisa A, PDF lk 217–219. **Õpieesmärk:** mõista peatükkide 4 ja 9 mittelineaarseid riske.

**[RAAMAT]** Ostuoptsioon (*call*) annab õiguse osta ja müügioptsioon (*put*) õiguse müüa alusvara kokkulepitud täitmishinnaga. Ostja maksab preemia, müüja võtab kohustuse. Preemiat mõjutavad muu hulgas täitmishind, järelejäänud aeg ja oodatav volatiilsus.

**[SELGITUS]** Ameerika tüüpi optsiooni saab üldjuhul kasutada enne lõpptähtaega; Euroopa tüüpi optsiooni kasutatakse lõpptähtajal. Raamatu üldkirjeldus vastab esimeses osas Ameerika tüübi õigustele, mitte kõigile optsioonidele. Alltoodud valemid kirjeldavad lihtsat lõpptähtaja kasumit ühe alusvaraühiku kohta, enne kulusid, makse ja finantseerimist.

Olgu $S_T$ alusvara lõpphind, $K$ täitmishind, $c$ call'i preemia ja $p$ put'i preemia:

| Positsioon | Kasum tähtajal | Suurim kahjum mitte-negatiivse hinnaga aktsia korral |
|---|---|---|
| Ostetud call | $\max(S_T-K,0)-c$ | $c$ |
| Müüdud call ilma katteta | $c-\max(S_T-K,0)$ | Teoreetiliselt piiramatu |
| Ostetud put | $\max(K-S_T,0)-p$ | $p$ |
| Müüdud put | $p-\max(K-S_T,0)$ | $K-p$ |

**Oluline täpsustus:** raamatus kasutatud üldistus piiramatust kasumist optsiooni ostjale ja piiramatust riskist müüjale vajab eristamist. Mitte-negatiivse hinnaga aktsia put'i ostja maksimaalne kasum on $K-p$ ning put'i müüja maksimaalne kahjum sama suur. Call'i ostja kasum ja katmata call'i müüja kahjum on teoreetiliselt piiramata. Futuuride ja muude eripäraste alusvarade korral ei tohi aktsia hinnapõranda eeldust automaatselt üle kanda.

### Samm-sammuline näide

**[NÄIDE]** Ostad call'i: $K=100$, preemia 6. Lepingu kordaja on selles näites 100.

| Lõpphind | Sisemine väärtus ühiku kohta | Kasum ühiku kohta | Kasum lepingult |
|---:|---:|---:|---:|
| 90 | 0 | −6 | −600 |
| 100 | 0 | −6 | −600 |
| 104 | 4 | −2 | −200 |
| 106 | 6 | 0 | 0 |
| 120 | 20 | 14 | 1400 |

Optsiooni rahasolek ei võrdu kasumlikkusega: hinna 104 juures on call rahas, kuid ostja on kahjumis. Kasumilävi tähtajal on $K+c=106$.

**Sisemine väärtus** call'il on $\max(S-K,0)$ ja put'il $\max(K-S,0)$. **Ajaväärtuseks** nimetatakse tavapäraselt preemia ja sisemise väärtuse vahet. Ennetähtaegse kasutamise võimalus, intress ja dividendid mõjutavad seda käsitlust; lihtne „preemia ei saa olla sisemisest väärtusest väiksem” argument ei kehti kõigile Euroopa optsioonidele samal kujul.

**Implitsiitne volatiilsus** on hinnastamismudeli volatiilsusparameeter, mis sobitab mudelihinna turupreemiaga. **Realiseerunud volatiilsus** kirjeldab hiljem toimunud hinnakõikumist. Nende erinevus ei ole iseenesest tasuta kasum: optsiooni hind sisaldab ka riskipreemiat ning mudel pole tegelikkus ise.

**[HARJUTUS]** Müüd aktsia put'i täitmishinnaga 50 ja preemiaga 3. Leia kasum, kui lõpphind on 60, 45 või 0. **[KONTROLL]** Miks ei tähenda piiratud kahjumiga optsiooni ost automaatselt head strateegiat?

<details><summary>Vastus ja põhjendus</summary>

Kasumid on 3, $3-5=-2$ ja $3-50=-47$ ühiku kohta. Ostja piiratud kahjum võib korduda palju kordi; ülehinnatud kaitse pidev ostmine võib kapitali järk-järgult vähendada. Vajalik on tõenäosuste, hinna ja positsiooni suuruse analüüs.

</details>

<a id="valemid"></a>
## Lisa B. Valemid, kokkulepped ja kontroll

**Allikas:** raamatu peatükid 5, 8–9 ja lisa B. **[SELGITUS]** Valemid on esitatud ühtsete ajamõõtmetega. Raamatu lisa B valemid kontrolliti ka PDF-i pildilt, sest tekstieraldus jätab valemipilte välja. Allpool eristatakse raamatu konventsiooni ja levinud alternatiive; sama nimega suhtarv ei taga sama arvutust.

### B1. Kasv ja kapitalilangus

Kui perioode aastas on $m$, perioode kokku $T$ ja väärtusrida sisaldab algväärtust $V_0$:

$$CAGR=\left(\frac{V_T}{V_0}\right)^{m/T}-1.$$

$$H_t=\max_{0\leq s\leq t}V_s,\qquad DD_t=\frac{V_t}{H_t}-1,\qquad MDD=-\min_t DD_t.$$

$DD_t$ on siin null või negatiivne, $MDD$ positiivne kahjumi suurus. Teiste allikatega võrdlemisel kontrolli märgikokkulepet. Vahepealsete sissemaksetega kontojäägist ei tohi CAGR-i otse arvutada; vaja on korrektset tootlusrida või rahavoogude meetodit.

### B2. Sharpe'i suhtarv

Olgu liigtootlus $e_t=r_t-r_{f,t}$. Siis:

$$\bar e=\frac1T\sum e_t,\qquad s_e=\sqrt{\frac{\sum(e_t-\bar e)^2}{T-1}},\qquad SR_m=\frac{\bar e}{s_e}.$$

Tavapärane aastastamine on $SR_{ann}=\sqrt m\,SR_m$. Konstantse riskivaba tootluse korral on $s_e=s_r$. Muutuva võrdlustootluse puhul arvuta standardhälve liigtootlusest.

**Eeldused:** ruutjuurskaleerimine eeldab muu hulgas, et perioodide sõltuvus ei muuda ajas koondatud dispersiooni; autokorrelatsiooni ja hinnasilumise korral võib see eksitada. Nullstandardhälbe korral on suhtarv määramata, mitte automaatselt lõpmatu kvaliteet.

### B3. Sortino suhtarv

Vali perioodiline minimaalne vastuvõetav tootlus ehk lävend $\tau$:

$$D_m=\sqrt{\frac1T\sum_{t=1}^{T}\min(r_t-\tau,0)^2}.$$

Jagaja on **kõikide perioodide arv**, mitte ainult kahjumiperioodide arv. Lävendit ületavad kuud annavad summasse nulli.

Sama sageduse aritmeetiline variant:

$$Sortino_m=\frac{\bar r-\tau}{D_m}.$$

Raamat kasutab lugejas aastast liitkasvu. Selle õppematerjali selgelt aastastatud raamatulähedane konventsioon on:

$$Sortino_{CAGR}=\frac{CAGR-\tau_{ann}}{\sqrt m\,D_m},\qquad\tau=(1+\tau_{ann})^{1/m}-1.$$

Aastase lugeja jagamine aastastamata kuise nimetajaga paisutaks tulemust. Aritmeetiline ja CAGR-variant ei ole identsed ega võrreldavad ilma definitsiooni teadmata. Ka downside-hälbe ruutjuur-aastastamine on konventsioon koos piirangutega, mitte tegeliku aastase kahjumijaotuse täpne tuletus.

**[NÄIDE]** Nelja tootluse +4%, −2%, +3%, −1% ja null-lävendi korral $D_m=\sqrt{(0.02^2+0.01^2)/4}\approx1.1180\%$. Aritmeetiline kuine Sortino on $1/1.1180\approx0.8944$. Raamatulähedane CAGR-variant annab aastastamise järel teise arvu; praktikum väljastab selle eraldi.

### B4. Sümmeetrilise langusriski Sharpe ehk SDR-Sharpe

Raamatu lisa B kasutab selle downside-hälbe puhul jagajat $T-1$, erinevalt Sortino jagajast $T$:

$$D_{SDR,m}=\sqrt{\frac{\sum\min(r_t-b,0)^2}{T-1}}.$$

Siin $b$ võib olla null, riskivaba tootlus või keskmine. Raamatu CAGR-lugejat kasutav aastastatud esitus:

$$SDR=\frac{CAGR-r_{f,ann}}{\sqrt2\sqrt m\,D_{SDR,m}}.$$

Tegur $\sqrt2$ käsitleb ülespoole kõrvalekallet allapoole kõrvalekalde peegelpildina. See aitab mõista mõõdiku skaalat, kuid ei muuda CAGR-lugejaga SDR-i arvuliselt identseks aritmeetilise Sharpe'iga ka sümmeetrilise jaotuse puhul. Võrdlemisel peavad ajaskaala, lugeja ja lävend olema kooskõlas.

### B5. Gain-to-pain ratio ehk GPR

$$GPR=\frac{\sum r_t}{\left|\sum\min(r_t,0)\right|}.$$

Lugejas on **kõikide** tootluste summa, mitte ainult kasumite summa. Viimase kasutamine annaks teise mõõdiku, nn profit factor'i, mis oleks sama agregeerimise korral $GPR+1$.

GPR ei ole liittootluse suhe kahjumisse. See ei arvesta tootluste järjekorda, võib varjata ühte suurt kaotust ning sõltub andmesagedusest. Päevast ja kuist GPR-i ei tohi otse samade lävenditega võrrelda. Kahjumite puudumisel on nimetaja null: teata „määramata”, mitte tõend riskitusest.

### B6. Tail ratio

Raamatus võrreldakse ülemise saba **keskmist** tootlust alumise saba keskmise absoluutväärtusega:

$$TR=\frac{\operatorname{mean}(r\text{ ülemises sabas})}{|\operatorname{mean}(r\text{ alumises sabas})|}.$$

Näiteks võta parimad ja halvimad 10% kuudest. Väikeses valimis tuleb määrata ümardamisreegel. Mõned teegid kasutavad selle nime all hoopis kahe kvantiili suhet; need pole sama arvutus.

**[NÄIDE]** Kui parima kümnendiku keskmine on +8% ja halvima oma −12%, on $TR=8/12=0.6667$. Mõõdik viitab selles valimis suurematele negatiivsetele äärmustele. See ei anna nende tulevast tõenäosust.

**Täpsustus raamatu lihtsustusele:** sümmeetrilise nullkeskmisega jaotuse puhul on ideaalne suhe 1. Pelgalt normaaljaotusest ei järeldu suhe täpselt 1, kui keskmine erineb nullist. Väikeses valimis esineb lisaks juhuslik varieerumine.

### B7. MAR ja Calmar

$$MAR=\frac{CAGR}{MDD}.$$

Calmar kasutab raamatu käsitluses sama loogikat viimase 36 kuu andmetel. Arvuta nii CAGR kui MDD samast aknast, kaasates akna algväärtuse. Väikese või nullise MDD korral võib suhtarv olla ebastabiilne või määramata.

**Terminikonflikt:** Sortino valemis tähendab MAR sageli *minimum acceptable return*. MAR-suhtarv on teine mõiste. Selles juhendis kasutatakse Sortino lävendiks tähist $\tau$.

### B8. Return retracement ratio ehk RRR ja 2DUC

Võta kuu lõpu väärtus $V_i$. Arvuta:

$$d_i=1-\frac{V_i}{\max_{0\leq j\leq i}V_j},\qquad f_i=1-\frac{\min_{i\leq j\leq T}V_j}{V_i}.$$

$$MR_i=\max(d_i,f_i),\qquad AMR=\frac1T\sum_{i=1}^{T}MR_i,\qquad RRR=\frac{CAGR-r_{f,ann}}{AMR}.$$

Käesolevas esituses on jooksev punkt maksimumi ja miinimumi hulgas, et kahjuminäitajad ei muutuks negatiivseks. Algväärtus aitab määrata varasemat tippu, kuid AMR-i keskmistatakse ainult T kuu lõppude üle. Dokumenteeri see kokkulepe teiste teostustega võrdlemiseks.

**[NÄIDE]** Väärtused on $V_0=100$, seejärel 120, 90 ja 108. Kuude $d_i$ on 0%, 25%, 10%; tulevased $f_i$ on 25%, 0%, 0%. Seega $MR_i$ on 25%, 25%, 10% ning AMR = 20%. Kui need on kuud, on CAGR $1.08^4-1\approx36.05\%$ ja nullise riskivaba tootlusega RRR ligikaudu 1,8024. Kolme kuu aastastamine on siin vaid arvutusnäide.

Tulevase miinimumi kasutamine on selles mõõdikus teadlik tagasivaatav kirjeldus. Kui kasutaksid seda mineviku tehingusignaalina, tekiks tulevikuinfo leke.

### B9. Portfell ja tingimuslikud näitajad

$$E[r_p]=\sum_i w_iE[r_i],\qquad\sigma_p^2=w^\top\Sigma w.$$

Need on ühe perioodi fikseeritud kaalude valemid. Mitme perioodi simulatsioonis tuleb eristada kaalude taastamist ja vabalt muutuvate kaaludega osta-hoia portfelli.

Turu languskuude fondi võidumäär:

$$p_+=\frac{\#\{r_F>0,\ r_M<0\}}{\#\{r_M<0\}}.$$

Keskmine tingimuslik tootlus on $\operatorname{mean}(r_F\mid r_M<0)$. Lisa alati tingimusele vastavate vaatluste arv. Kümnest kuust kuus plussi ja sajast kuust kuuskümmend plussi on sama sagedus, kuid erinev tõendihulk.

### B10. Valemite kasutamise enesekontroll

**[HARJUTUS]** Sul on aastane CAGR 10% ja kuine downside-hälve 2%. Null-lävendi korral leia raamatulähedane aastastatud Sortino. **[KONTROLL]** Mis on viga tulemuses 5?

<details><summary>Vastus ja põhjendus</summary>

$0.10/(0.02\sqrt{12})\approx1.4434$. Tulemus 5 saadi aastase lugeja jagamisel kuise nimetajaga. See segab ajaskaalu. Arvutus kasutab tavapärast ruutjuur-aastastamist ega tõesta, et tulevane aastane langusrisk võrdub täpselt kuise näitaja sellise teisendusega.

</details>

<a id="python"></a>
## Praktikum: kontrollitav analüüs Pythonis

**[SELGITUS]** Kõik järgnevad andmed on sünteetilised. Näited ei kirjelda päris fonde. Kood kasutab ainult Pythoni standardteeki ja sobib Thonnysse või Colabi. Kopeeri kogu plokk korraga. Funktsioonid tagastavad suhtarvud arvudena: näiteks tootlus `0.08` tähendab 8%.

### Samm 1. Arvuta üksiku tootlusrea põhinäitajad

Kood teeb eeldused nähtavaks: riskivaba tootlus null, kuised andmed, positiivne kapital, välised rahavood puuduvad. Nullnimetaja annab `None`. Nelja kuu andmestik sobib arvutuse õppimiseks, mitte investeerimisotsuse tegemiseks.

```python
from math import prod, sqrt, isclose
from statistics import mean, stdev


def divide_or_none(a, b):
    return a / b if b != 0 else None


def nav_series(returns, start=100.0):
    if start <= 0 or any(r <= -1 for r in returns):
        raise ValueError("See oppemudel eeldab positiivset kapitali.")
    nav = [start]
    for r in returns:
        nav.append(nav[-1] * (1 + r))
    return nav


def max_drawdown(nav):
    peak = nav[0]
    worst = 0.0
    for value in nav:
        peak = max(peak, value)
        worst = max(worst, 1 - value / peak)
    return worst


def metrics(returns, periods_per_year=12):
    r = list(returns)
    if len(r) < 2 or periods_per_year <= 0:
        raise ValueError("Vaja on vahemalt kaht vaatlust ja positiivset sagedust.")
    nav = nav_series(r)
    n = len(r)
    total = nav[-1] / nav[0] - 1
    cagr = (1 + total) ** (periods_per_year / n) - 1
    sd = stdev(r)  # Valimi standardhalve, jagaja n-1
    downside = sqrt(sum(min(x, 0) ** 2 for x in r) / n)
    loss_sum = -sum(min(x, 0) for x in r)
    mdd = max_drawdown(nav)
    annual_sd = sd * sqrt(periods_per_year)
    annual_downside = downside * sqrt(periods_per_year)
    return {
        "kogutootlus": total,
        "CAGR": cagr,
        "aastane_volatiilsus": annual_sd,
        "Sharpe_aastane_rf0": divide_or_none(
            mean(r) * periods_per_year, annual_sd),
        "Sortino_CAGR_tau0": divide_or_none(cagr, annual_downside),
        "GPR": divide_or_none(sum(r), loss_sum),
        "MDD": mdd,
        "MAR": divide_or_none(cagr, mdd),
    }


def correlation(x, y):
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("Read peavad olema sama pikkusega ja vahemalt 2 vaatlust.")
    mx, my = mean(x), mean(y)
    cross = sum((a - mx) * (b - my) for a, b in zip(x, y))
    denom = sqrt(sum((a - mx) ** 2 for a in x)
                 * sum((b - my) ** 2 for b in y))
    return divide_or_none(cross, denom)


def beta(fund, market):
    if len(fund) != len(market) or len(fund) < 2:
        raise ValueError("Read peavad olema joondatud ja vahemalt 2 vaatlust.")
    mf, mm = mean(fund), mean(market)
    cross = sum((f - mf) * (m - mm) for f, m in zip(fund, market))
    market_ss = sum((m - mm) ** 2 for m in market)
    return divide_or_none(cross, market_ss)


def down_market_stats(fund, market):
    if len(fund) != len(market):
        raise ValueError("Read peavad olema sama pikkusega.")
    selected = [f for f, m in zip(fund, market) if m < 0]
    if not selected:
        return {"n": 0, "voidumaara": None, "keskmine": None}
    return {
        "n": len(selected),
        "voidumaara": sum(f > 0 for f in selected) / len(selected),
        "keskmine": mean(selected),
    }


def cnr(row, column, loss_threshold=0.0):
    # Lahter: P(rea fond kaotab | veeru fond kaotab).
    # Lavend 0 tahendab rangelt negatiivset tootlust.
    # Positiivne lavend T tahendab kahjumit vahemalt T.
    if len(row) != len(column) or loss_threshold < 0:
        raise ValueError("Kontrolli ridade pikkust ja lavendit.")
    def loses(r):
        return r < 0 if loss_threshold == 0 else r <= -loss_threshold
    chosen = [a for a, b in zip(row, column) if loses(b)]
    if not chosen:
        return None
    return sum(loses(a) for a in chosen) / len(chosen)


def rebalanced_path(series, weights, start=100.0):
    if not series or len(series) != len(weights):
        raise ValueError("Vaja on iga vara jaoks kaalu.")
    if len({len(s) for s in series}) != 1:
        raise ValueError("Tootluste kuupaevad peavad kattuma.")
    if not isclose(sum(weights), 1.0) or any(w < 0 for w in weights):
        raise ValueError("See naide kasutab mittenegatiivseid kaale summaga 1.")
    # Iga perioodi algul taastatakse sihtkaalud, kuludeta.
    rp = [sum(w * x for w, x in zip(weights, period))
          for period in zip(*series)]
    return nav_series(rp, start)


def buy_hold_path(series, weights, start=100.0):
    # Kontrollid samad mis tasakaalustatud portfellil.
    rebalanced_path(series, weights, start)
    holdings = [nav_series(s, start) for s in series]
    return [sum(w * value for w, value in zip(weights, period))
            for period in zip(*holdings)]


r = [0.04, -0.02, 0.03, -0.01]
print("NELJA KUU OPPENAIDE")
for name, value in metrics(r).items():
    print(name, None if value is None else round(value, 6))

# Sisulised kontrollid: tuntud kasitsi lahendatud naited.
assert isclose(nav_series([0.20, -0.20])[-1], 96.0)
assert isclose(metrics(r)["kogutootlus"], 0.03927824)
assert isclose(metrics(r)["MDD"], 0.02)
assert isclose(metrics(r)["GPR"], 4 / 3)
assert metrics([0.01, 0.02])["GPR"] is None
assert isclose(correlation([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]), 0.0)

market = [-0.02, 0, 0.02]
fund = [0.01 + 0.1 * m for m in market]
assert isclose(correlation(fund, market), 1.0)
assert isclose(beta(fund, market), 0.1)
assert down_market_stats(fund, market)["voidumaara"] == 1.0

A, B = [0.20, -0.10], [-0.10, 0.20]
assert isclose(rebalanced_path([A, B], [0.5, 0.5])[-1], 110.25)
assert isclose(buy_hold_path([A, B], [0.5, 0.5])[-1], 108.0)

print("\nKONTROLLID LABITUD")
print("Tasakaalustatud:", rebalanced_path([A, B], [0.5, 0.5]))
print("Osta-hoia:", buy_hold_path([A, B], [0.5, 0.5]))

# Lopp-projekti 12 kuu sundandmed, koik arvud on protsendid / 100.
M = [x / 100 for x in [2, 1, -3, 4, -2, 1, 2, -4, 3, 1, -1, 2]]
F = [0.002 + 0.6 * x for x in M]
G = [0.01] * 11 + [-0.18]
H = [0.001 - 0.5 * x for x in M]

print("\nLOPP-PROJEKT")
for name, data in [("M", M), ("F", F), ("G", G), ("H", H)]:
    print(name, {k: None if v is None else round(v, 6)
                 for k, v in metrics(data).items()})
    print("  beeta:", beta(data, M), "languskuud:", down_market_stats(data, M))

for name, other in [("F", F), ("G", G), ("H", H)]:
    nav = rebalanced_path([M, other], [0.8, 0.2])
    rp = [nav[i] / nav[i - 1] - 1 for i in range(1, len(nav))]
    print("80% M + 20% " + name,
          {k: None if v is None else round(v, 6)
           for k, v in metrics(rp).items()})
```

### Samm 2. Tõlgenda, ära piirdu väljundiga

Nelja kuu näites peaksid nägema kogutootlust ligikaudu 0,039278, MDD-d 0,02 ja GPR-i 1,333333. Sharpe on ligikaudu 1,176697. Aastastatud kasvumäär on ligikaudu 12,2524%; see on nelja kuu tulemust aastasele skaalale teisendav arvutus, mitte prognoos.

Muuda nelja tootluse järjekorda nii, et kaks miinuskuud on järjest. Kogutootlus, Sharpe ja GPR ei muutu, kuid MDD võib muutuda. Põhjus: korrutis ja jaotuse põhjal arvutatud näitajad ei sõltu järjekorrast; tipust langus sõltub teekonnast.

### Samm 3. Lisa piirangud

Kood ei arvesta rahavooge, valuutavahetust, makse, kauplemiskulusid, fondi sulgemist, päevast tagatisnõuet ega puuduvaid andmeid. Seda ei tohi esitada tootmiskõlbliku riskisüsteemina. Praktikumi eesmärk on teha definitsioonid ja vead nähtavaks.

**[HARJUTUS]** Lisa enne arvutamist kontroll, mis välistab mittenumbrilised ja lõpmatud väärtused. Selgita, miks puuduvat kuud ei tohi automaatselt nulltootlusega asendada.

<details><summary>Vastus ja põhjendus</summary>

Kasuta näiteks `math.isfinite(x)` ning käsitle puuduvaid kuusid eraldi. Null tähendab tegelikult muutumatut väärtust; puuduv tähendab teadmata tulemust. Nulliga täitmine võib vähendada volatiilsust ja muuta korrelatsiooni. Ajaread tuleb joondada kuupäevade järgi ning puuduvate andmete reegel dokumenteerida.

</details>

<a id="projekt"></a>
## Lõppprojekt: kolmest fondist sobiva lisandi hindamine

**[SELGITUS]** See projekt on koostaja loodud rakendusülesanne. Eesmärk on teha põhjendatud analüüs, mitte õppida pähe „õige fond”. Kõik andmed on väljamõeldud ja tegelikust finantsturust oluliselt lihtsamad.

### Lähteolukord

Sul on sünteetiline turuportfell M ja kolm võimalikku lisandit. Pythoniplokis on 12 kuutootlust:

- **F:** $r_F=0.2\%+0.6r_M$. Mõõdukas positiivne turusõltuvus.
- **G:** 11 kuud +1%, seejärel −18%. Sile algus ja üks suur kahjum.
- **H:** $r_H=0.1\%-0.5r_M$. Täiusliku vastassuunalise sõltuvusega õppemudel, mida ei tohi pidada realistlikuks tasuta kaitseks.

Eesmärk on uurida 80% M + 20% lisandi portfelli, taastades kaale iga kuu. Lisaks vaata tasakaalustamata varianti. Andmed käsitlevad kuludejärgseid tootlusi ainult näite eelduse kohaselt; tegeliku analüüsi puhul tuleb tasud tõendada.

### Ülesanded

1. Arvuta igale reale kogutootlus, CAGR, volatiilsus, Sharpe, GPR ja MDD.
2. Leia iga fondi korrelatsioon ja beeta M suhtes.
3. Leia fondi keskmine tootlus ja võidumäär M languskuudel; lisa valimi suurus.
4. Koosta toor-CNR maatriks. Selgita rea ja veeru tähendust.
5. Võrdle kolme 80/20 portfelli; too välja tootluse ja riskivähenemise vahetus.
6. Arvuta kapitalilangused ka ümberjärjestatud kuudega. Millised mõõdikud muutuvad?
7. Tee stressitest: M −25%, F −20%, G −40%, H +10%.
8. Tee teine stressitest, kus H kaitse ebaõnnestub ja H tootlus on −15%.
9. Kirjuta vähemalt kolm põhjust, miks 12 kuu tulemuse järgi ei saa päris fondi valida.
10. Koosta ühe lehekülje pikkune otsustusmemo: eesmärk, arvud, riskid, puuduv info ja tingimuslik järeldus.

### Lahenduse tugipunktid

<details><summary>Ava pärast iseseisvat lahendamist</summary>

F-i beeta on täpselt 0,6 ja korrelatsioon +1, sest seos on selles mudelis deterministlik ning turu variatsioon pole null. H beeta on −0,5 ja korrelatsioon −1.

M-il on neli languskuud: −3%, −2%, −4%, −1%. Neil kuudel on F tulemused −1,6%, −1%, −2,2%, −0,4%; keskmine −1,3% ja võidumäär 0%. H tulemused on +1,6%, +1,1%, +2,1%, +0,6%; keskmine +1,35% ja võidumäär 100%.

G on kõigil neil neljal kuul +1%, kuid kaotab viimases kuus 18%, mil M tõuseb 2%. See näitab, miks hea käitumine *aktsiaturu* languskuudel ei välista mõnda muud suurt riski. G aastane kogutootlus on $1.01^{11}\cdot0.82-1\approx-8.52\%$ ja MDD 18%.

Esimese stressi ühe perioodi kaalutud tootlused:

- M + F: $0.8(-25\%)+0.2(-20\%)=-24\%$.
- M + G: $0.8(-25\%)+0.2(-40\%)=-28\%$.
- M + H: $0.8(-25\%)+0.2(10\%)=-18\%$.

Kui H hoopis kaotab 15%, on M + H tulemus −23%. Mõlemad H-stsenaariumid on algsest ajaloolisest valemist teadlikult erinevad: stressitest uurib mudeli purunemist, mitte ei korda olemasolevat regressiooni.

Lõplik valik ei tulene üksnes tabeli suurimast suhtarvust. Näiteks H näiline kasulikkus sõltub selle kaitsevõime püsimisest, maksumusest ja teostatavusest. Väike valim, kunstlikud lineaarsed seosed ning teadmata rahastus ja likviidsus takistavad tulemuste ülekandmist pärisrahale.

</details>


### Kontrolltabelid lõppprojektile

<details><summary>Arvulised tulemused ja tõlgendus</summary>

Kõik tootlused ja volatiilsused allolevas tabelis on protsentides. Suhtarvud on ühikuta. Kuna andmeid on täpselt 12 kuud, võrdub CAGR siin kogutootlusega.

| Rida | Tootlus | Aastastatud volatiilsus | Sharpe | GPR | MDD |
|---|---:|---:|---:|---:|---:|
| M | 5.813% | 8.549% | 0.702 | 0.600 | 4.000% |
| F | 6.040% | 5.130% | 1.170 | 1.154 | 2.200% |
| G | -8.515% | 19.000% | -0.368 | -0.389 | 18.000% |
| H | -1.867% | 4.275% | -0.421 | -0.250 | 2.144% |
| 80% M + 20% F | 5.868% | 7.865% | 0.763 | 0.664 | 3.640% |
| 80% M + 20% G | 3.211% | 7.160% | 0.475 | 0.370 | 3.000% |
| 80% M + 20% H | 4.360% | 5.985% | 0.742 | 0.642 | 2.780% |

**Toor-CNR:** rea kahjumi sagedus tingimusel, et veeru rida kaotab.

| Rida / tingimus | M kaotab | F kaotab | G kaotab | H kaotab |
|---|---:|---:|---:|---:|
| M | 100.0% | 100.0% | 0.0% | 0.0% |
| F | 100.0% | 100.0% | 0.0% | 0.0% |
| G | 0.0% | 0.0% | 100.0% | 12.5% |
| H | 0.0% | 0.0% | 100.0% | 100.0% |

M ja F kaotavad samadel neljal kuul. H kaotab kaheksal M-i tõusukuul. G ainus kahjum langeb ühte H kahjumiga: seetõttu on $P(H-\mid G-)=100\%$, kuid $P(G-\mid H-)=12.5\%$. Üks G kahjum on tingimusliku riski usaldusväärseks hindamiseks väga vähe.

Selles valimis paraneb F lisamisel nii tootlus kui Sharpe, H lisamisel langevad tootlus ja volatiilsus ning Sharpe paraneb mõõdukalt. G lisamisel langeb ajalooline MDD, kuid stressitestis võib G suurendada kahjumit. See on otsene näide, miks ajaloolise ühe numbri järgi ei tohi tulevast riski lukku panna.

**Ümberjärjestamine:** kui permuteerid kõigi ridade kuid koos samal viisil, jäävad üksikridade ja igakuiselt tasakaalustatud portfelli kogutootlus, standardhälve, Sharpe, GPR, korrelatsioon ja CNR samaks; kapitalilangused võivad muutuda. Kui järjestad ainult ühe rea ümber, võivad muutuda ka korrelatsioonid ja portfelli tootlus.

</details>

### Hindamisjuhend

| Kriteerium | Punktid | Täispunktide tingimus |
|---|---:|---|
| Andmete ja eelduste kirjeldus | 15 | Sagedus, ühikud, tasud, väljamaksed ja sünteetiline päritolu on selged |
| Arvutuste korrektsus | 25 | Liittootlus, standardhälve, MDD ja suhtarvud on õigesti leitud |
| Sõltuvuse analüüs | 20 | Korrelatsioon, beeta, languskuud ja CNR on õigesti tõlgendatud |
| Varjatud risk ja stress | 20 | Vähemalt kaks usutavat ebaõnnestumise mehhanismi, mitte ainult ajalooline tabel |
| Otsuse põhjendus | 20 | Portfellipõhine, tingimuslik ja piiranguid arvestav järeldus |

85–100 punkti: hea rakendusoskus. 65–84: põhialused on olemas, paranda põhjenduste või eelduste osa. Alla 65: korda vastavaid peatükke ja lahenda muudetud arvudega näited uuesti. Kõrge punktisumma ei tõenda oskust turgu prognoosida.

<a id="sonastik"></a>
## Mõistesõnastik

| Termin | Eesti selgitus |
|---|---|
| Alpha | Mudeliga seletamata tootluse komponent; sõltub kasutatud mudelist |
| Arbitrage | Rangelt võttes riskivaba hinnavastuolu kasutamine; strateegianimetustes sageli riskiga suhtelise väärtuse kauplemine |
| Backtest | Ajaloolistel andmetel tehtud strateegiasimulatsioon |
| Backfill | Varem tekkinud ajaloo hilisem lisamine andmebaasi |
| Benchmark | Sobiv võrdlusalus; peab vastama perioodile, valuutale ja riskile |
| Beta | Lineaarne tundlikkus võrdlusvara tootluse suhtes |
| CAGR | Aastane liitkasvumäär |
| Correlation | Standardiseeritud lineaarne seos, mitte põhjuslikkus |
| Credit spread | Riskantse võla ja sobiva võrdlusinstrumendi tootluse vahe |
| CTA | Raamatu kontekstis futuuride või valuutadega tegutsev juht; ei tähenda ainult tooraineid |
| Drawdown | Vara väärtuse langus varasemast tipust |
| Due diligence | Investeeringu, meeskonna, struktuuri ja riskide sisuline kontroll |
| Efficient frontier | Eeldatud sisendite korral parimat tootluse-volatiilsuse vahetust pakkuvad portfellid |
| Event risk | Sündmusest vallanduv risk, mida rahulik ajalugu ei pruugi näidata |
| Gross exposure | Pikkade ja lühikeste positsioonide absoluutväärtuste summa suhtes omakapitaliga |
| High-water mark | Tulemustasu arvestamisel kasutatav varasem väärtustipp |
| Leverage | Omakapitalist suurema majandusliku ekspositsiooni võtmine |
| Liquidity | Võime teha tehing piisavas mahus kiiresti ja mõistliku hinnamõjuga |
| Managed account | Investori või tema esindaja konto, millel halduril on määratud kauplemisõigus |
| Mean reversion | Protsessi või suhtelise hinnataseme kalduvus naasta tavapärasema taseme poole |
| Momentum / trend following | Liikumise jätkumist kasutav lähenemine; meetodid ja ajahorisondid erinevad |
| NAV | Fondi puhasväärtus või õppenäites normeeritud portfelli väärtusrida |
| Net exposure | Pikkade ja lühikeste ekspositsioonide vahe suhtes omakapitaliga |
| Pro forma | Eeldustel põhinev või kohandatud tulemus; vajab selget päritolu |
| Rebalancing | Portfelli sihtkaalude taastamine |
| Regime change | Turu või strateegia toimimistingimuste oluline muutus |
| Sharpe | Keskmise liigtootluse suhe selle standardhälbesse |
| Short squeeze | Lühikeste positsioonide sulgemise survega võimenduv hinnatõus |
| Skewness | Jaotuse asümmeetria; ei kirjelda üksi kogu sabariski |
| Survivorship bias | Ebaõnnestunud objektide väljajäämisest tekkiv kallutatus |
| Tail risk | Harvade ja suurte ebasoodsate tulemuste risk |
| Time under water | Aeg, mille jooksul väärtus pole varasemat tippu taastanud |
| VaR | Kahjumijaotuse valitud kvantiil, mitte maksimaalne kahjum |
| Volatility drag | Hajuvuse ja liitkasvu seos kindlate võrdlustingimuste korral |

## Epiloogi ideede süntees: otsuse kontrollnimekiri

**[RAAMAT + SELGITUS]** Raamatu 32 tähelepanekut koonduvad alljärgnevaks otsustusprotsessiks. See pole autori nummerdatud loendi tõlge; peatükkides on säilitatud selle peamised sisulised seosed ning lisatud täpsustused.

| Otsuse etapp | Küsimus, millele pean suutma vastata |
|---|---|
| Info | Kas väide on kontrollitav ja kogu tulemuste ajalugu nähtav? |
| Hind | Kas eristan head vara heast ostuhinnast? |
| Tuluallikas | Kas kasum tuli oskusest, turufaktorist, võimendusest või varjatud riski kandmisest? |
| Andmed | Kas võrdlen samu perioode ning väldin ellujäämise ja tagantjärele valiku kallutatust? |
| Mõõtmine | Kas kasutan sama ajaskaalat ja avalikke arvutusdefinitsioone? |
| Risk | Milline suur kahjum pole ajaloolises reas veel juhtunud? |
| Struktuur | Kes hoiab varasid, kes saab raha liigutada ja millal saan väljuda? |
| Portfell | Kas lisand vähendab minu olemasolevaid riske või dubleerib neid? |
| Stress | Mis juhtub, kui korrelatsioon, rahastus ja likviidsus halvenevad korraga? |
| Käitumine | Kas järgin eelnevat reeglit või reageerin hiljutisele võitjale ja hirmule? |
| Jälgimine | Milline uus tõend muudaks minu algset hinnangut? |

## Kordamisplaan sügavaks omandamiseks

**Esimene kordus, järgmine päev:** selgita peast, miks +20% ja −20% ei nulli teineteist, miks korrelatsioon null ei tähenda sõltumatust ning miks VaR pole kahjumi ülempiir.

**Teine kordus, nädala pärast:** lahenda peatükkide 5, 8, 9, 14, 19 ja 21 harjutused muudetud arvudega. Enne arvutamist ennusta tulemuse suund.

**Kolmas kordus, kuu pärast:** kirjuta ühe fondi kohta analüüsimemo ilma mõõdikute automaatse paremusjärjestuseta. Seejärel kontrolli, kas memo katab andmete päritolu, tasud, likviidsuse, varjatud riski ja portfellimõju.

**Omandamise lõppkriteerium:** suudad mitte ainult arvu leida, vaid öelda, millisele küsimusele see vastab, millisele ei vasta ning milline eeldus muudaks järelduse valeks.

## Allika ja kontrolli märkus

Põhiallikas on kasutaja lisatud Jack D. Schwageri *Market Sense and Nonsense*. Peatükkide juures on viited vastavatele PDF-i lehekülgedele. Raamatu empiirilisi tulemusi käsitletakse ajalooliste autori argumentidena; algandmestikke ei olnud kaasas ning nende uuringuid ei ole siin uuesti replitseeritud. Õppenäited ja harjutused on uued ning nende arvulised vastused on eraldi kontrollitud. Lisatud pole jooksvaid turuprognoose ega kehtivate fonditingimuste kontrolli.

Põhilised kriitilised täpsustused puudutavad VaR-i tähendust, turu tõhususe eristamist jaotuseeldustest, put-optsiooni piiratud maksimaalset kasumit ja kahjumit mitte-negatiivse alusvara korral, suhtarvude ajaskaalasid, tail ratio definitsiooni ning korrelatsiooni piiranguid. Need aitavad õppida raamatu ideid rakendama ilma selle lihtsustusi üldkehtivateks reegliteks muutmata.
