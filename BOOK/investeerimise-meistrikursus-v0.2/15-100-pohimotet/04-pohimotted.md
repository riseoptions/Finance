# Võlakirjad ja optsioonid: põhimõtted 31–40

[Koondloend](README.md) · [Õppekava](../00-oppekava.md)

## Sisukord

- [31. Võlakirja kupong ei ole ostja tootlus.](#p31)
- [32. Fikseeritud maksete hind langeb diskontomäära tõustes.](#p32)
- [33. Tähtajani hoidmine ei kõrvalda kõiki riske.](#p33)
- [34. Duration on lokaalne tundlikkus, mitte täpne šokikalkulaator.](#p34)
- [35. Convexity täpsustab duration'i lähendust.](#p35)
- [36. Krediidimarginaal ei ole tasuta lisatootlus.](#p36)
- [37. Võlakirjafondi osakul ei pruugi olla sinu tähtajale vastavat lunastust.](#p37)
- [38. Optsiooni väljamakse ja kasum on erinevad.](#p38)
- [39. Optsiooni ostja ja müüja riskid pole sümmeetrilise ulatusega.](#p39)
- [40. Greeks on mudeli tundlikkus, mitte lubadus.](#p40)

<a id="p31"></a>
## 31. Võlakirja kupong ei ole ostja tootlus.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Kupong on makse nimiväärtuselt; tootlus sõltub ostuhinnast.

**Miks oluline?** Preemiaga ostetud võlakiri võib teenida kupongist vähem.

**Mehhanism:** YTM on rahavoogude ja hinna diskontovõrrandi lahend.

**Näide:** Aasta pärast 105 maksev võlakiri hinnaga 102 annab 2.9412%, mitte 5%.

**Vestluses kasutamine:** Võrdle pakkumisi hinna ja rahavoogude kaudu.

**Piirang või erand:** YTM-i tõlgendus eeldab lepingulisi makseid; reinvesteerimise mõju loeb mitme kupongi korral.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p32"></a>
## 32. Fikseeritud maksete hind langeb diskontomäära tõustes.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Suurema nimetajaga nüüdisväärtus on väiksem.

**Miks oluline?** See selgitab intressiriski.

**Mehhanism:** Iga positiivne makse CF/(1+y)^t väheneb y kasvades.

**Näide:** 100 aasta pärast: 5% juures 95.24, 10% juures 90.91.

**Vestluses kasutamine:** Vasta küsimusele, miks võlakirjafond võib langeda.

**Piirang või erand:** Makse suurus võib muutuda ujuva intressi, maksehäire või optsiooni tõttu.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p33"></a>
## 33. Tähtajani hoidmine ei kõrvalda kõiki riske.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Hinnakõikumise realiseerimata jätmine ei kõrvalda makse-, inflatsiooni- ega valuutariski.

**Miks oluline?** Nominaalse nimiväärtuse taastumine pole täielik turvalisus.

**Mehhanism:** Lepinguline makse ja selle tegelik väärtus on eri asjad.

**Näide:** 100 tagasi saamine 10% hinnatõusu järel tähendab ostujõudu umbes 90.91.

**Vestluses kasutamine:** Täpsusta, mis mõttes võlakiri on „riskivaba”.

**Piirang või erand:** Usaldusväärne samas valuutas makse võib siiski sobida kindla kohustuse katmiseks.

**Allikas või tõendus:** [TÄIENDUS] SEC Investor.gov võlakirjade riskide selgitus. [Veebiallikad](../allikad/veebiallikad.md).

<a id="p34"></a>
## 34. Duration on lokaalne tundlikkus, mitte täpne šokikalkulaator.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Modified duration annab väikese tootlusnõude muutuse esimese järgu hinnamõju.

**Miks oluline?** See aitab riski suurusjärku võrrelda.

**Mehhanism:** Hinnamuutus/hind ≈ −Dmod × tootlusnõude muutus.

**Näide:** Dmod 5 ja +0.01 šokk annavad umbes −5%.

**Vestluses kasutamine:** Võrdle võlakirjade intressitundlikkust.

**Piirang või erand:** Suured šokid, kõvera kuju muutus ja optsioonid nõuavad täpsemat mudelit.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p35"></a>
## 35. Convexity täpsustab duration'i lähendust.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Hinna ja tootlusnõude seos on mittelineaarne.

**Miks oluline?** Ühe sirgega lähendamine võib suure šoki korral eksida.

**Mehhanism:** Lisandub 0.5 × convexity × (määramuutus)^2.

**Näide:** Dmod 5, convexity 30 ja +1 pp: −5% +0.15 pp = −4.85%.

**Vestluses kasutamine:** Selgita, miks täpne hinnamuutus erineb duration'i vastusest.

**Piirang või erand:** Convexity definitsioon ja mõõtühik peavad vastama kasutatud intressikonventsioonile.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p36"></a>
## 36. Krediidimarginaal ei ole tasuta lisatootlus.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Kõrgem lubatud tootlus võib kompenseerida makse- ja likviidsusriski.

**Miks oluline?** Kupongide võrdlus peab sisaldama võimalikke kahjusid.

**Mehhanism:** Lihtsustatud oodatav krediidikahju = maksehäire tõenäosus × kahjumäär.

**Näide:** 2% maksehäire tõenäosus ja 60% kahjumäär annavad 1.2% oodatavat kahju.

**Vestluses kasutamine:** Uuri kõrge tootluslubaduse allikat.

**Piirang või erand:** Turuhinna riskipreemia ei võrdu pelgalt statistilise oodatava kahjuga.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p37"></a>
## 37. Võlakirjafondi osakul ei pruugi olla sinu tähtajale vastavat lunastust.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Tavaline fond uuendab portfelli ning osaku väärtus jääb turust sõltuvaks.

**Miks oluline?** Üksikvõlakirja lunastuse loogikat ei saa automaatselt fondile üle kanda.

**Mehhanism:** Fondiosaku hind peegeldab muutuvat alusvaraportfelli.

**Näide:** Kolmeaastane fondi hoidmine ei taga ostuhinna taastumist.

**Vestluses kasutamine:** Küsi fondi duration'i ja eesmärki.

**Piirang või erand:** Sihtkuupäevaga fondid on eraldi juhtum; ka neil on riskid.

**Allikas või tõendus:** [TÄIENDUS] SEC Investor.gov võlakirjade riskide selgitus. [Veebiallikad](../allikad/veebiallikad.md).

<a id="p38"></a>
## 38. Optsiooni väljamakse ja kasum on erinevad.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Preemia makstakse õiguse eest eraldi.

**Miks oluline?** Õige hinnasuuna prognoos ei taga optsiooni kasumit.

**Mehhanism:** Call'i kasum tähtajal = max(S−K,0)−preemia.

**Näide:** S=103, K=100, preemia=5: väljamakse 3, kasum −2.

**Vestluses kasutamine:** Küsi optsiooninäites ka makstud preemiat.

**Piirang või erand:** Tähtajaeelne müügihind sisaldab muid hinnategureid.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p39"></a>
## 39. Optsiooni ostja ja müüja riskid pole sümmeetrilise ulatusega.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Ostja kaotus piirdub preemiaga; katmata call'i müüja kahju kasvab alusvara tõustes piiramatult.

**Miks oluline?** Väike saadud preemia võib varjata suurt kohustust.

**Mehhanism:** Müüja kasum on ostja väljamakse vastand pluss preemia.

**Näide:** K=100, preemia 5, S=200: call'i müüja kasum −95.

**Vestluses kasutamine:** Ära võrdle ainult kasumlike tehingute osakaalu.

**Piirang või erand:** Tagatis, kattev vara ja optsioonikombinatsioonid muudavad kogu portfelli riski.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p40"></a>
## 40. Greeks on mudeli tundlikkus, mitte lubadus.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Delta, gamma, theta ja vega kirjeldavad hinna lokaalseid muutusi.

**Miks oluline?** Need aitavad lahutada optsiooni hinnaliikumise põhjuseid.

**Mehhanism:** Delta on hinna tuletis alusvara hinna järgi; gamma delta muutus.

**Näide:** Delta 0.5 viitab umbes 0.5 hinnamuutusele alusvara +1 korral.

**Vestluses kasutamine:** Selgita, miks alusvara suund üksi optsioonitulemust ei määra.

**Piirang või erand:** Suured muutused ja mudeliviga vähendavad lokaalse lähenduse täpsust.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.
