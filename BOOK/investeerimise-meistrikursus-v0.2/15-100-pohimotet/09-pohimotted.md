# AI ja analüüsi automatiseerimine: põhimõtted 81–90

[Koondloend](README.md) · [Õppekava](../00-oppekava.md)

## Sisukord

- [81. LLM-i ladus tekst ei tõesta selle arvude õigsust.](#p81)
- [82. RAG parandab allikale ligipääsu, mitte ei taga õiget järeldust.](#p82)
- [83. Agent vajab mõõdetavat ülesannet ja lõpetamistingimust.](#p83)
- [84. Rohkem agente ei tähenda rohkem sõltumatuid tõendeid.](#p84)
- [85. Finantsuudise sentiment ei võrdu hinnamõjuga.](#p85)
- [86. Automatiseeritud raport peab näitama ka puuduvat infot.](#p86)
- [87. Mudeli muutus vajab uut kontrolli.](#p87)
- [88. Tehingu automatiseerimine vajab rohkem kontrolli kui arvutus.](#p88)
- [89. AI lisaväärtust mõõda töö tulemuse kaudu.](#p89)
- [90. Dokumendis olev juhis ei ole analüüsisüsteemi volitus.](#p90)

<a id="p81"></a>
## 81. LLM-i ladus tekst ei tõesta selle arvude õigsust.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Keeleline usutavus ja faktitäpsus on eri omadused.

**Miks oluline?** Vale arv võib olla veenvalt põhjendatud.

**Mehhanism:** Arvulised väited kontrollitakse lähteandmete või arvutuskoodiga.

**Näide:** Raportis toodud 15% kasv peab vastama kahe aruande võrreldavatele väärtustele.

**Vestluses kasutamine:** Nõua arvule allikat, perioodi ja arvutust.

**Piirang või erand:** Ka viidatud allikas võib olla valesti tõlgendatud.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p82"></a>
## 82. RAG parandab allikale ligipääsu, mitte ei taga õiget järeldust.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Otsitud tekst võib olla asjakohatu, aegunud või valesti kasutatud.

**Miks oluline?** Viite olemasolu ei lõpeta kvaliteedikontrolli.

**Mehhanism:** Hinda eraldi otsingu tabavust ja vastuse tõendatust.

**Näide:** Õige ettevõtte vale aasta aruanne võib anda vale vastuse.

**Vestluses kasutamine:** Kontrolli ettevõtet, perioodi, mõõdikut ja tsitaadi konteksti.

**Piirang või erand:** Tõhus RAG võib vähendada otsingutööd, kui hindamine on korraldatud.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p83"></a>
## 83. Agent vajab mõõdetavat ülesannet ja lõpetamistingimust.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Avatud eesmärk võib viia tarbetute tegevusteni.

**Miks oluline?** Aeg ja kulu peavad looma kasutajale väärtust.

**Mehhanism:** Määra sisend, lubatud toimingud, kontrollid ja valmisoleku kriteerium.

**Näide:** „Kontrolli kümne väite allikad” on hinnatavam kui „leia parim aktsia”.

**Vestluses kasutamine:** Enne automatiseerimist sõnasta testitav tulemus.

**Piirang või erand:** Kõiki uurimistulemusi ei saa ühe numbriga kvaliteetselt hinnata.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p84"></a>
## 84. Rohkem agente ei tähenda rohkem sõltumatuid tõendeid.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Sama allikat või sama viga kordavad mudelid ei loo uut infot.

**Miks oluline?** Näiline konsensus võib olla ühise vea tulemus.

**Mehhanism:** Erista arvamuste arv ja tõendusallikate sõltumatus.

**Näide:** Kolm sama pressiteadet refereerivat agenti kasutavad üht allikat.

**Vestluses kasutamine:** Küsi iga järelduse tegelikku päritolu.

**Piirang või erand:** Erinevad töörollid võivad siiski aidata vigu leida.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p85"></a>
## 85. Finantsuudise sentiment ei võrdu hinnamõjuga.

**Liik:** Vaidlustatava investeerimishüpoteesi kriitika.

**Täpne tähendus:** Hind reageerib muu hulgas ootuste ja tegelikkuse erinevusele.

**Miks oluline?** Hea sõnastus võib kaasneda pettumusega.

**Mehhanism:** Võrdle uudist varasema ootuse ja juba hinnastatud infoga.

**Näide:** Kasum kasvab 10%, kuid oodati 20%: positiivne kasv ei taga hinnatõusu.

**Vestluses kasutamine:** Vaidlusta ainult positiivsete sõnade põhjal tehtud ostusignaal.

**Piirang või erand:** Tegelik hinnareaktsioon sõltub ka muudest samaaegsetest asjaoludest.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p86"></a>
## 86. Automatiseeritud raport peab näitama ka puuduvat infot.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Vaikus puuduva andme kohta võib näida kindla järeldusena.

**Miks oluline?** Kasutaja peab teadma, mida süsteem ei kontrollinud.

**Mehhanism:** Lisa iga mõõdiku juurde seisund: olemas, puudu, aegunud või vastuoluline.

**Näide:** Puuduva võlanäitaja asemel ei tohi sisestada nulli.

**Vestluses kasutamine:** Kasuta raporti kontrollnimekirjana.

**Piirang või erand:** Liiga palju tehnilisi detaile võib peita olulise; näita otsust mõjutavaid puudusi.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p87"></a>
## 87. Mudeli muutus vajab uut kontrolli.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Uus prompt, allikas või parameeter võib muuta tulemust.

**Miks oluline?** Varem läbitud test ei kata automaatselt uut versiooni.

**Mehhanism:** Versioonista mudel ja säilita püsiv hindamiskomplekt.

**Näide:** Uus andmeparser võib muuta kõik protsendid 100 korda suuremaks.

**Vestluses kasutamine:** Rakenda regressioonikontrolli analüüsi töövoole.

**Piirang või erand:** Testikomplekt võib ise vananeda ning vajada uut sõltumatut täiendust.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p88"></a>
## 88. Tehingu automatiseerimine vajab rohkem kontrolli kui arvutus.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Arvutusviga ja tegelik order tekitavad erineva tagajärje.

**Miks oluline?** Välise mõjuga toiming peab vastama volitusele ja riskipiiridele.

**Mehhanism:** Eralda uurimus, simulatsioon ja orderi täitmine.

**Näide:** Raporti „osta” sõna ei tohi vaikimisi käivitada maaklerikorraldust.

**Vestluses kasutamine:** Määra enne integratsiooni kasutaja lubatud tegevused.

**Piirang või erand:** Paberkaubandus ei tõenda kõiki päristuru täitmise omadusi.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p89"></a>
## 89. AI lisaväärtust mõõda töö tulemuse kaudu.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Tööriista uudsus pole kvaliteedinäitaja.

**Miks oluline?** See aitab vältida keerukust ilma kasuta.

**Mehhanism:** Võrdle aega, maksumust, vigade arvu ja tõendatud väidete osakaalu.

**Näide:** 30 minuti asemel 10 minutit, kuid rohkem vigu, ei pruugi olla paranemine.

**Vestluses kasutamine:** Otsusta automatiseerimise ulatus mõõdetud katse järgi.

**Piirang või erand:** Kvaliteedimõõdikud peavad vastama tegelikule kasutusotstarbele.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p90"></a>
## 90. Dokumendis olev juhis ei ole analüüsisüsteemi volitus.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Välisest aruandest loetud tekst on analüüsi sisend, mitte automaatselt käsk tööriistale.

**Miks oluline?** See eristus kaitseb automatiseeritud töövoogu eksitavate juhiste eest.

**Mehhanism:** Hoia allikatekst, kasutaja ülesanne ja lubatud toimingud eraldi.

**Näide:** Aruandesse lisatud „saada fail mujale” ei ole investeerimisanalüüsi ülesanne.

**Vestluses kasutamine:** Kontrolli dokumendipõhise agendi tegevuspiire.

**Piirang või erand:** Ka tavapärane vigane tekst võib järeldust mõjutada; vaja on sisulist kontrolli.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.
