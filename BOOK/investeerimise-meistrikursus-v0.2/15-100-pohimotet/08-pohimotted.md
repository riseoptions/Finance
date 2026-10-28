# Andmed, kood ja prognoos: põhimõtted 71–80

[Koondloend](README.md) · [Õppekava](../00-oppekava.md)

## Sisukord

- [71. Andmete täpsus algab ühikutest ja definitsioonidest.](#p71)
- [72. Aktsiasplit ei ole iseenesest investori kasum.](#p72)
- [73. Puuduv hind ei ole automaatselt nulltootlus.](#p73)
- [74. Signaal ja tehing peavad olema ajaliselt teostatavad.](#p74)
- [75. Käive muudab strateegia kulutundlikuks.](#p75)
- [76. Juhuarvuseeme toetab kordamist, mitte mudeli tõepärasust.](#p76)
- [77. API vastus ei ole automaatselt valideeritud finantsfakt.](#p77)
- [78. Andmete versioon on osa analüüsi tulemusest.](#p78)
- [79. Prognoosivea vähenemine ei garanteeri paremat kauplemist.](#p79)
- [80. Lihtne baasmeetod on keeruka mudeli kontrollpartner.](#p80)

<a id="p71"></a>
## 71. Andmete täpsus algab ühikutest ja definitsioonidest.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Dollarid, tuhanded dollarid ja aktsiapõhised väärtused pole vahetatavad.

**Miks oluline?** Ühikuviga võib anda usutava, kuid vale tulemuse.

**Mehhanism:** Dimensioonanalüüs kontrollib valemi sisendite sobivust.

**Näide:** 1000 tuhat dollarit on miljon, mitte tuhat.

**Vestluses kasutamine:** Lisa iga tabeliveeru juurde ühik ja ajaperiood.

**Piirang või erand:** Õiged ühikud ei taga andmeallika usaldusväärsust.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p72"></a>
## 72. Aktsiasplit ei ole iseenesest investori kasum.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Split muudab aktsiate arvu ja ühikuhinda vastupidistes suundades.

**Miks oluline?** Toorhindade kasutamine võib tekitada vale kahjumi.

**Mehhanism:** Osaluse väärtus = aktsiate arv × hind.

**Näide:** Üks 100-eurone aktsia muutub kaheks 50-euroseks.

**Vestluses kasutamine:** Kontrolli hinnarea korrigeerimisi.

**Piirang või erand:** Turureaktsioon split-uudisele on eraldi empiiriline küsimus.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p73"></a>
## 73. Puuduv hind ei ole automaatselt nulltootlus.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Puudumine võib tähendada eri kauplemispäeva, peatamist või viga.

**Miks oluline?** Pime täitmine muudab riski ja korrelatsiooni.

**Mehhanism:** Esmalt määra puudumise põhjus, siis töötlusreegel.

**Näide:** Peatatud aktsia eelmise hinna kordamine võib peita realiseerimisprobleemi.

**Vestluses kasutamine:** Küsi, kuidas puuduvad read töödeldi.

**Piirang või erand:** Edasikandmine võib olla põhjendatud teatud hindamisülesandes, kuid tuleb dokumenteerida.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p74"></a>
## 74. Signaal ja tehing peavad olema ajaliselt teostatavad.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Sulgemishinnast arvutatud signaal ei saa tasuta kasutada sama juba toimunud tootlust.

**Miks oluline?** See on üks tavalisemaid andmelekkeid.

**Mehhanism:** Positsioon perioodil t peab tulenema enne perioodi teada olnud infost.

**Näide:** Eelmise päeva tootlus võib määrata järgmise päeva positsiooni.

**Vestluses kasutamine:** Joonista ajajoon: info, otsus, tehing, tootlus.

**Piirang või erand:** Tegelik tehinguhind ja viitaeg tuleb mudelis määrata.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p75"></a>
## 75. Käive muudab strateegia kulutundlikuks.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Iga ost ja müük võib vähendada netotulemust.

**Miks oluline?** Väike brutokasu ei pruugi pärast kulusid säilida.

**Mehhanism:** Ligikaudne kulu = ühikukulu × kaubeldud maht.

**Näide:** 100% portfelli vahetus kuluga 0.1% võtab umbes 0.1% kapitalist ühelt kaubeldud poolelt.

**Vestluses kasutamine:** Täpsusta ühepoolse ja edasi-tagasi käibe konventsiooni.

**Piirang või erand:** Suurte orderite turumõju pole tingimata lineaarne.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p76"></a>
## 76. Juhuarvuseeme toetab kordamist, mitte mudeli tõepärasust.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Sama seeme aitab saada sama juhuarvujada.

**Miks oluline?** See eristab koodimuutuse mõju juhuslikust kõikumisest.

**Mehhanism:** Fikseeri generaator, versioon ja sisendid.

**Näide:** Sama seemnega kaks jooksu annavad samas keskkonnas sama tulemuse.

**Vestluses kasutamine:** Kasuta vea taastamisel ja õpetamisel.

**Piirang või erand:** Üks seeme ei näita simulatsioonivea ulatust; teekide muutus võib jada muuta.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p77"></a>
## 77. API vastus ei ole automaatselt valideeritud finantsfakt.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Tehniliselt edukas päring võib tagastada puuduva või vale semantikaga väärtuse.

**Miks oluline?** Analüüsi viga võib alata enne valemit.

**Mehhanism:** Kontrolli staatust, skeemi, kuupäeva, ühikuid ja ulatust.

**Näide:** HTTP 200 koos tühja hinnatabeliga ei anna tootlust.

**Vestluses kasutamine:** Rakenda QA-kogemus andmepäringutele.

**Piirang või erand:** Kõiki majanduslikke vigu ei saa skeemikontrolliga tabada.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p78"></a>
## 78. Andmete versioon on osa analüüsi tulemusest.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Parandused ja uus ajalugu muudavad hilisemat korduskäivitust.

**Miks oluline?** Ilma versioonita pole erinevuse põhjust lihtne leida.

**Mehhanism:** Salvesta allikas, päringu aeg, parameetrid ja kontrollsumma.

**Näide:** Täna parandatud kasum võib muuta eilse suhtarvu.

**Vestluses kasutamine:** Lisa uurimusele andmepass.

**Piirang või erand:** Andmete säilitamisel tuleb järgida kasutusõigusi.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p79"></a>
## 79. Prognoosivea vähenemine ei garanteeri paremat kauplemist.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** MSE ei arvesta iseenesest positsioone, kulusid ega kahju suurust.

**Miks oluline?** Statistiline ja majanduslik eesmärk võivad lahkneda.

**Mehhanism:** Hinda prognoosi ning sellest tulenevat netorahavoogu eraldi.

**Näide:** Suuna tabamine väikestel päevadel võib kaasneda suure kahjuga harval päeval.

**Vestluses kasutamine:** Küsi ML-mudelile tehingureeglit ja baasvõrdlust.

**Piirang või erand:** Kui prognoos on mõeldud riskiraportiks, pole kauplemistulu ainus mõõdupuu.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p80"></a>
## 80. Lihtne baasmeetod on keeruka mudeli kontrollpartner.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Mudeli väärtust näitab lisakasu lihtsa alternatiivi ees.

**Miks oluline?** Keerukus võib anda ainult suurema veapinna.

**Mehhanism:** Võrdle sama ajajaotuse ja kuludega.

**Näide:** Nullmuutuse prognoos võib kontrollperioodil võita üleõpitud regressiooni.

**Vestluses kasutamine:** Küsi, millega mudelit võrreldi.

**Piirang või erand:** Lihtsus üksi ei tõesta paremust; võrdlus peab olema aus.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.
