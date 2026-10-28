# Portfell ja investori eesmärk: põhimõtted 51–60

[Koondloend](README.md) · [Õppekava](../00-oppekava.md)

## Sisukord

- [51. Hajutamine toimib kovariatsioonide kaudu.](#p51)
- [52. Nullkorrelatsioon ei tähenda üldiselt sõltumatust.](#p52)
- [53. Kõrge ühine korrelatsioon seab hajutamisele piiri.](#p53)
- [54. Stressis tuleb muuta ka koosliikumise eeldusi.](#p54)
- [55. Parim ajalooline portfell võib olla parim müra sobitus.](#p55)
- [56. Kaalupiirang võib olla teadmatusest tulenev kaitse.](#p56)
- [57. Rebalanseerimine taastab riskivaliku, mitte ei taga lisatootlust.](#p57)
- [58. Raha on madalama tururiskiga vara, kuid mitte riskitu eesmärk.](#p58)
- [59. Riskitaluvus ja riskikandevõime on eri asjad.](#p59)
- [60. Väike riskiprotsent suurelt summalt võib olla suur rahaline risk.](#p60)

<a id="p51"></a>
## 51. Hajutamine toimib kovariatsioonide kaudu.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Portfelli dispersioon sisaldab nii üksikriske kui koosliikumist.

**Miks oluline?** Varade arvu kõrval loevad nende suhted.

**Mehhanism:** Portfelli dispersioon = wᵀΣw.

**Näide:** Kaks 20% standardhälbega nullkorrelatsiooniga vara 50/50 annavad 14.14%.

**Vestluses kasutamine:** Põhjenda, miks kombinatsioon võib olla rahulikum kui komponendid.

**Piirang või erand:** Hajutamine ei kõrvalda kõiki riskiliike.

**Allikas või tõendus:** [MUDEL] [Hajutamise labor](../laborid/02-hajutamine.md): valemi tuletus ja piirangud.

<a id="p52"></a>
## 52. Nullkorrelatsioon ei tähenda üldiselt sõltumatust.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Pearsoni korrelatsioon näitab lineaarset seost.

**Miks oluline?** Mittelineaarne sõltuvus võib jääda mõõdikust välja.

**Mehhanism:** Sümmeetrilise X korral võivad X ja X² olla nullkorrelatsiooniga, kuid sõltuvad.

**Näide:** X väärtused −1,0,1; Y vastavalt 1,0,1.

**Vestluses kasutamine:** Paranda väidet, et nullkorrelatsiooniga riskid on täiesti eraldi.

**Piirang või erand:** Ühise normaaljaotuse korral järeldub nullkorrelatsioonist sõltumatus.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p53"></a>
## 53. Kõrge ühine korrelatsioon seab hajutamisele piiri.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Võrdsete varade lisamine ei kõrvalda püsivat ühist riski.

**Miks oluline?** Rohkem nimesid ei pruugi anda oodatud kaitset.

**Mehhanism:** Võrdsete kaalude korral σp²=σ²[ρ+(1−ρ)/n].

**Näide:** σ=20%, ρ=0.1: piirrisk on umbes 6.32%.

**Vestluses kasutamine:** Selgita süsteemse ja idiosünkraatilise riski erinevust.

**Piirang või erand:** Valem eeldab võrdseid standardhälbeid ja kõigile paaridele sama korrelatsiooni.

**Allikas või tõendus:** [MUDEL] [Hajutamise labor](../laborid/02-hajutamine.md): valemi tuletus ja piirangud.

<a id="p54"></a>
## 54. Stressis tuleb muuta ka koosliikumise eeldusi.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Rahuliku aja kovariatsioonimaatriks ei pruugi sobida stressi kirjeldamiseks.

**Miks oluline?** Üks riskiprognoos võib alahinnata ühist šokki.

**Mehhanism:** Võrdle mitut Σ-maatriksit, mitte ainult üksikvara volatiilsust.

**Näide:** 10 vara 20% riskiga: ρ 0.1→0.8 kasvatab mudeliriski 8.72%-lt 18.11%-le.

**Vestluses kasutamine:** Uuri korrelatsioonitundlikkust.

**Piirang või erand:** See stsenaarium ei tõesta, et iga kriisi korrelatsioon on 0.8.

**Allikas või tõendus:** [MUDEL] [Hajutamise labor](../laborid/02-hajutamine.md): valemi tuletus ja piirangud.

<a id="p55"></a>
## 55. Parim ajalooline portfell võib olla parim müra sobitus.

**Liik:** Vaidlustatava investeerimishüpoteesi kriitika.

**Täpne tähendus:** Optimeerija kasutab hinnangulisi sisendeid, mis võivad sisaldada juhust.

**Miks oluline?** Äärmuslikud kaalud ei tõesta majanduslikku paremust.

**Mehhanism:** Optimeeritud valimitulemus tuleb eraldi ajaperioodil kontrollida.

**Näide:** 1000 kaaluvektorist parima valik annab vähemalt sama hea treeningtulemuse kui üks juhuslik.

**Vestluses kasutamine:** Küsi sõltumatut kontrollperioodi.

**Piirang või erand:** Täpsete stabiilsete sisendite korral on optimeerimine kasulik otsustusvahend.

**Allikas või tõendus:** [SCHWAGER] ptk 21, portfelli optimeerimise piirangud; [ANALÜÜS] kontrollperioodi nõue. [Koodiaudit](../allikad/koodiaudit.md).

<a id="p56"></a>
## 56. Kaalupiirang võib olla teadmatusest tulenev kaitse.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Maksimaalne osakaal piirab sisendiveast tekkivat kontsentratsiooni.

**Miks oluline?** Veidi halvem mudelitulemus võib olla vastupidavam.

**Mehhanism:** Optimeeri sama sihtfunktsiooni kitsendusega wi≤piir.

**Näide:** Ühe vara 90% mudelikaalu piiramine 20%-le vähendab ühe hinnangu mõju.

**Vestluses kasutamine:** Arutle mudeliriski, mitte ainult tabeli optimumi üle.

**Piirang või erand:** Piirang võib ka tegeliku eelise kasutamist takistada.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p57"></a>
## 57. Rebalanseerimine taastab riskivaliku, mitte ei taga lisatootlust.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Tehing viib kaalud tagasi kokkulepitud sihile.

**Miks oluline?** Eesmärk võib olla riski kontroll, mitte turu ajastamine.

**Mehhanism:** Tõusnud vara kaal kasvab ilma tehinguteta.

**Näide:** 500/500 muutub 600/500-ks; võrdsustamiseks müü 50 tõusnud vara.

**Vestluses kasutamine:** Küsi, kas siht on risk või tootluse parandamine.

**Piirang või erand:** Püsiva trendi korral võib võitja kärpimine tootlust vähendada; kulud loevad.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p58"></a>
## 58. Raha on madalama tururiskiga vara, kuid mitte riskitu eesmärk.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Raha võib vähendada hinnakõikumist ja toetada likviidsust.

**Miks oluline?** Samas võib ostujõud langeda ja eesmärk jääda täitmata.

**Mehhanism:** Võrdle inflatsioonijärgset tootlust ning kohustuste tähtaega.

**Näide:** 0% intress ja 5% inflatsioon annavad umbes −4.76% reaaltootlust.

**Vestluses kasutamine:** Arutle puhvri ja pikaajalise kapitali eri rollide üle.

**Piirang või erand:** Hoiuse krediidirisk ja kaitseskeem sõltuvad konkreetsest korraldusest.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p59"></a>
## 59. Riskitaluvus ja riskikandevõime on eri asjad.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Emotsionaalne valmisolek kaotuseks ei võrdu majandusliku võimalusega kaotust taluda.

**Miks oluline?** Vajalikku raha ei saa sobivaks muuta pelgalt julgusega.

**Mehhanism:** Võrdle kahjustsenaariumi rahalise kohustuse ja puhvriga.

**Näide:** Järgmise kuu 5000-eurost makset ei kata pärast 30% langust 5000-eurone portfell.

**Vestluses kasutamine:** Küsi eesmärki, tähtaega ja puhvrit enne riskiarutelu.

**Piirang või erand:** See on otsustusraamistik, mitte isikupõhine investeerimissoovitus.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p60"></a>
## 60. Väike riskiprotsent suurelt summalt võib olla suur rahaline risk.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Absoluutne kahju sõltub positsiooni suurusest.

**Miks oluline?** Protsendipõhine võrdlus võib varjata tegelikku elumõju.

**Mehhanism:** Kahju eurodes = kapital × kahjumäär.

**Näide:** 2% miljonist on 20 000; 20% tuhandest on 200.

**Vestluses kasutamine:** Võrdle riski inimese kohustuste ja sissetulekuga.

**Piirang või erand:** Protsent on vajalik eri suurusega portfellide standardiseerimiseks.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.
