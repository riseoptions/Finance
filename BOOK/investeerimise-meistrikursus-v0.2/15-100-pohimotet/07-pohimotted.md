# Tõendid ja statistiline mõtlemine: põhimõtted 61–70

[Koondloend](README.md) · [Õppekava](../00-oppekava.md)

## Sisukord

- [61. Ajalooline võitja valitakse juba tulemuse järgi.](#p61)
- [62. Oskuse puudumise mudel ei tõesta oskuse puudumist turul.](#p62)
- [63. Ellujäänute valim ei kirjelda kõiki alustajaid.](#p63)
- [64. Teadmise kuupäev on sama tähtis kui sündmuse kuupäev.](#p64)
- [65. Üks testperiood ei jää puutumata pärast korduvat häälestamist.](#p65)
- [66. Paljud katsed suurendavad juhuleidude võimalust.](#p66)
- [67. Statistiline olulisus ei võrdu majandusliku kasulikkusega.](#p67)
- [68. P-väärtus ei ole hüpoteesi vääruse tõenäosus.](#p68)
- [69. Kattuvad aknad ei ole sõltumatud kordused.](#p69)
- [70. Korrelatsioon ei määra põhjuslikku mehhanismi.](#p70)

<a id="p61"></a>
## 61. Ajalooline võitja valitakse juba tulemuse järgi.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Esikoht sisaldab valikust tulenevat optimismi.

**Miks oluline?** Tulemus üksi ei lahuta oskust juhusest.

**Mehhanism:** Maksimum paljudest mürarikastest hinnangutest ületab tavaliselt tüüpilist hinnangut.

**Näide:** 500 võrdse oskusega fondi hulgas tekib ikka üks võitja.

**Vestluses kasutamine:** Küsi, kui suurest hulgast võitja valiti.

**Piirang või erand:** Oskuste püsiva erinevuse korral võib varasem edu infot sisaldada.

**Allikas või tõendus:** [MUDEL] [Fondide valiku labor](../laborid/01-fondivoitjad.md): eeldused, kood ja kontrolltulemused.

<a id="p62"></a>
## 62. Oskuse puudumise mudel ei tõesta oskuse puudumist turul.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Simulatsiooni eeldus ja pärismaailma järeldus on eri tasandid.

**Miks oluline?** Vastasel juhul tõestad ainult seda, mida sisse kirjutasid.

**Mehhanism:** Võrdle nulloskuse ja püsiva oskuse mudeleid.

**Näide:** Laboris tekib 0.04 oskuse hajuvusega tulevane eelis, nulloskusega mitte.

**Vestluses kasutamine:** Nõua alternatiivset seletust ja empiirilist testi.

**Piirang või erand:** Kumbki mudel ei mõõda päris fondijuhtide oskust ilma andmeteta.

**Allikas või tõendus:** [MUDEL] [Fondide valiku labor](../laborid/01-fondivoitjad.md): eeldused, kood ja kontrolltulemused.

<a id="p63"></a>
## 63. Ellujäänute valim ei kirjelda kõiki alustajaid.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Sulgunud fondide väljajätmine võib kallutada hinnangut.

**Miks oluline?** Investeerija ei teadnud ette, kes ellu jääb.

**Mehhanism:** Valim peab vastama otsuse hetkel kättesaadavale universumile.

**Näide:** Kümnest fondist viis kaovad; ainult viie jätkaja keskmine jätab osa kogemusest välja.

**Vestluses kasutamine:** Küsi andmestiku lõpetatud fondide kohta.

**Piirang või erand:** Kallutatuse täpne suund ja suurus vajavad andmeid, mitte oletatud protsenti.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p64"></a>
## 64. Teadmise kuupäev on sama tähtis kui sündmuse kuupäev.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Aruande perioodilõpp ei ole avaldamishetk.

**Miks oluline?** Tulevase info kasutamine teeb järeltesti teostamatuks.

**Mehhanism:** Signaal saab kasutada ainult selleks hetkeks avaldatud andmeid.

**Näide:** 31.12 lõppenud aasta aruanne võib ilmuda alles järgmisel kevadel.

**Vestluses kasutamine:** Kontrolli andmetabeli avaldamis- ja parandamisaega.

**Piirang või erand:** Ajalooliselt parandatud andmed vajavad eraldi versioonide käsitlust.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p65"></a>
## 65. Üks testperiood ei jää puutumata pärast korduvat häälestamist.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Testitulemuse järgi mudelit muutes kasutad seda treeninguks.

**Miks oluline?** Nähtav edu võib tulla kaudsest üleõppimisest.

**Mehhanism:** Hoia lõplik kontroll eraldi või kasuta ranget ajalist hindamiskava.

**Näide:** Pärast kümmet testikomplekti järgi tehtud parandust pole test enam uus.

**Vestluses kasutamine:** Küsi, mitu korda mudelit kontrolltulemuste järgi muudeti.

**Piirang või erand:** Ka korrektselt eraldatud test ei garanteeri režiimimuutuses edu.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p66"></a>
## 66. Paljud katsed suurendavad juhuleidude võimalust.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Üksiku testi olulisuslävi ei ole sama kui kõigi testide ühine veamäär.

**Miks oluline?** Mõni muljetavaldav tulemus võib tekkida pelgalt otsimise käigus.

**Mehhanism:** Sõltumatute nulltestide puhul vähemalt ühe valepositiivse tõenäosus = 1−(1−α)^m.

**Näide:** 20 testi ja α=0.05 annavad umbes 64.15%.

**Vestluses kasutamine:** Küsi proovitud strateegiate koguarvu.

**Piirang või erand:** Testide sõltuvus muudab täpse valemi; mitmese testimise parandus vajab sobivat meetodit.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p67"></a>
## 67. Statistiline olulisus ei võrdu majandusliku kasulikkusega.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Väga väike eelis võib suure valimiga olla täpselt hinnatud.

**Miks oluline?** Tehingukulu võib kogu eelise ära võtta.

**Mehhanism:** Võrdle netomõju suurust ja selle ebakindlust.

**Näide:** Keskmine brutokasu 0.02% tehingult ja kulu 0.05% annavad kahju.

**Vestluses kasutamine:** Küsi p-väärtuse kõrvale eurodes või protsentides mõju.

**Piirang või erand:** Ebaoluline tulemus ei tõesta mõju täpset puudumist.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p68"></a>
## 68. P-väärtus ei ole hüpoteesi vääruse tõenäosus.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** P-väärtus kirjeldab andmete äärmuslikkust nullmudeli kehtimisel.

**Miks oluline?** Vale tõlgendus loob põhjendamatut kindlust.

**Mehhanism:** See on tingimuslik tõenäosus mudeli suhtes, mitte mudeli posterior.

**Näide:** p=0.03 ei tähenda 97% tõenäosust, et strateegia töötab.

**Vestluses kasutamine:** Paranda statistilise testi järelduse sõnastust.

**Piirang või erand:** Test vajab sobivaid eeldusi ja eelnevalt määratud analüüsi.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p69"></a>
## 69. Kattuvad aknad ei ole sõltumatud kordused.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Sama vaatlus osaleb mitmes aknas.

**Miks oluline?** Tavapärane standardviga võib näida liiga väike.

**Mehhanism:** Sõltuvust tuleb arvestada ajaplokkide või sobiva kovariatsioonihinnanguga.

**Näide:** Kaks järjestikust 12 kuu akent jagavad 11 kuud.

**Vestluses kasutamine:** Küsi efektiivset informatsioonihulka.

**Piirang või erand:** Täpset sõltuvust ei saa tuletada üksnes akende arvust.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p70"></a>
## 70. Korrelatsioon ei määra põhjuslikku mehhanismi.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Koosliikumine võib tulla ühisest põhjusest, valikust või juhusest.

**Miks oluline?** Vale põhjuslik lugu võib anda halva prognoosi.

**Mehhanism:** Vaja on mehhanismi ning alternatiivsete seletuste kontrolli.

**Näide:** Kaks ettevõtet võivad tõusta sama intressišoki tõttu, mitte teineteise mõjul.

**Vestluses kasutamine:** Erista „liigub koos” ja „põhjustab”.

**Piirang või erand:** Põhjuslik analüüs võib nõuda katset või eraldi identifitseerimisoletusi.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.
