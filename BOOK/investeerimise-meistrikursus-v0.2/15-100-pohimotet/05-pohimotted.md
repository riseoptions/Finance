# Riskimõõdikud ja varjatud risk: põhimõtted 41–50

[Koondloend](README.md) · [Õppekava](../00-oppekava.md)

## Sisukord

- [41. Oodatav tootlus on jaotuse keskmine, mitte lubadus.](#p41)
- [42. Volatiilsus mõõdab kõikumist, mitte kõiki kahjuvorme.](#p42)
- [43. VaR on kahjulävend, mitte maksimaalne kahju.](#p43)
- [44. Sama VaR võib peita erineva sabakahju.](#p44)
- [45. Puuduv riskisündmus võib eksitada kõiki ajaloolisi mõõdikuid.](#p45)
- [46. Maksimaalne langus on hinnateekonna mõõdik.](#p46)
- [47. Sharpe'i suhtarv vajab sobivat ületootlust ja ajahorisonti.](#p47)
- [48. Sortino sõltub valitud sihttasemest.](#p48)
- [49. Likviidsus tähendab võimalust väljuda mõistliku hinnaga.](#p49)
- [50. Stressitest küsib „mis siis, kui”, mitte alati „kui tõenäoline”.](#p50)

<a id="p41"></a>
## 41. Oodatav tootlus on jaotuse keskmine, mitte lubadus.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Üks tulemus võib keskmisest märgatavalt erineda.

**Miks oluline?** Investor peab mõistma ka kahjustsenaariume.

**Mehhanism:** E[R] = tõenäosustega kaalutud tootluste summa.

**Näide:** 50% tõenäosusega +20% ja 50% −10% annavad ootuse +5%.

**Vestluses kasutamine:** Küsi oodatava numbri kõrvale jaotust.

**Piirang või erand:** Tõenäosused ise võivad olla hinnangulised.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p42"></a>
## 42. Volatiilsus mõõdab kõikumist, mitte kõiki kahjuvorme.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Standardhälve ei kirjelda üksi maksehäiret, likviidsust ega varjatud sündmust.

**Miks oluline?** Madal näitaja võib jätta ohtliku strateegia rahulikuks.

**Mehhanism:** Standardhälve arvutatakse vaadeldud kõrvalekalletest keskmise ümber.

**Näide:** Iga kuu −1% tootlusega rea standardhälve on null.

**Vestluses kasutamine:** Ära võrdsusta madalat volatiilsust raha säilimisega.

**Piirang või erand:** Volatiilsus on siiski asjakohane kõikumise ja teatud mudelite riski mõõdik.

**Allikas või tõendus:** [SCHWAGER] ptk 4; originaalne sõnastus ja näide. [Riskilabor](../laborid/03-varjatud-risk.md).

<a id="p43"></a>
## 43. VaR on kahjulävend, mitte maksimaalne kahju.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** VaR on kindla ajahorisondi ja usaldusnivoo kvantiil.

**Miks oluline?** Lävendi taga olev kahju võib olla väga suur.

**Mehhanism:** VaRα = väikseim kahju, mille jaotusfunktsioon ulatub α-ni.

**Näide:** 95% VaR 2% ei välista 20% kahju ülejäänud sabas.

**Vestluses kasutamine:** Täpsusta iga VaR-väite horisonti ja nivood.

**Piirang või erand:** Eri kvantiilihinnangud võivad väikeses valimis erineda.

**Allikas või tõendus:** [MUDEL] [Varjatud riski labor](../laborid/03-varjatud-risk.md): täpne diskreetne jaotus ja arvutused.

<a id="p44"></a>
## 44. Sama VaR võib peita erineva sabakahju.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Kvantiil ei määra sellest kaugemale jäävate kahjude suurust.

**Miks oluline?** Kahe strateegia riskide järjestus võib jääda nähtamatuks.

**Mehhanism:** Muuda ainult kvantiilist kõrgema saba kahjusid.

**Näide:** Laboris on A ja B 95% VaR −0.5%, ES vastavalt 15.9% ja 63.9%.

**Vestluses kasutamine:** Lisa VaR-ile saba suurust kirjeldav analüüs.

**Piirang või erand:** ES sõltub samuti jaotuse õigsusest.

**Allikas või tõendus:** [MUDEL] [Varjatud riski labor](../laborid/03-varjatud-risk.md): täpne diskreetne jaotus ja arvutused.

<a id="p45"></a>
## 45. Puuduv riskisündmus võib eksitada kõiki ajaloolisi mõõdikuid.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Andmestikus puuduvat sündmust ei saa sealt otse mõõta.

**Miks oluline?** Mõõdiku keerukus ei asenda strateegia mõistmist.

**Mehhanism:** Harvaesineva sündmuse puudumise tõenäosus n sõltumatus perioodis on (1−p)^n.

**Näide:** p=4%, n=60: krahhita ajalugu umbes 8.64%.

**Vestluses kasutamine:** Küsi, millised riskid ei saanud valimis avalduda.

**Piirang või erand:** Sõltumatuse eeldus võib olla vale; tõenäosus on mudelipõhine.

**Allikas või tõendus:** [MUDEL] [Varjatud riski labor](../laborid/03-varjatud-risk.md): täpne diskreetne jaotus ja arvutused.

<a id="p46"></a>
## 46. Maksimaalne langus on hinnateekonna mõõdik.

**Liik:** Matemaatiline seaduspärasus.

**Täpne tähendus:** Sama kogutootlus võib tulla erineva ajutise kahjuga.

**Miks oluline?** Teekond mõjutab likviidsusvajadust ja käitumist.

**Mehhanism:** Langus = väärtus/senine tipp−1.

**Näide:** 100→120→90→120 lõpetab +20%, aga sisaldab −25% langust.

**Vestluses kasutamine:** Võrdle strateegia lõpptulemuse kõrval teekonda.

**Piirang või erand:** Ajalooline maksimum ei ole tulevase languse ülempiir.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p47"></a>
## 47. Sharpe'i suhtarv vajab sobivat ületootlust ja ajahorisonti.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Lugejas ja nimetajas peavad olema võrreldava perioodi andmed.

**Miks oluline?** Vale aastastamine tekitab kunstliku eelise.

**Mehhanism:** Sharpe = ületootluse keskmine / ületootluse standardhälve.

**Näide:** 6% aastane ületootlus ja 12% standardhälve annavad 0.5.

**Vestluses kasutamine:** Küsi kasutatud riskivaba määra ja tootlussagedust.

**Piirang või erand:** Autokorrelatsioon ja ebasümmeetriline jaotus piiravad lihtsat tõlgendust.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p48"></a>
## 48. Sortino sõltub valitud sihttasemest.

**Liik:** Tingimuslik mudel või tulemus.

**Täpne tähendus:** Allapoole sihti jääv risk muutub koos investori eesmärgiga.

**Miks oluline?** Sama strateegia ei ole iga sihttaseme juures sama tulemusega.

**Mehhanism:** Downside deviation võib olla ruutjuur kõigi perioodide min(R−T,0)^2 keskmisest.

**Näide:** Tootlused −2%, +2%, siht 0: downside deviation ≈1.414%.

**Vestluses kasutamine:** Täpsusta Sortino definitsiooni enne fondide võrdlust.

**Piirang või erand:** Mõned teostused jagavad vaid negatiivsete perioodide arvuga; need annavad teise näitaja.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.

<a id="p49"></a>
## 49. Likviidsus tähendab võimalust väljuda mõistliku hinnaga.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Viimane tehinguhind ei pruugi kehtida kogu positsiooni müümisel.

**Miks oluline?** Suure positsiooni realiseerimisväärtus võib olla väiksem.

**Mehhanism:** Müügi mõju sõltub ostunõudluse sügavusest ja kiirusest.

**Näide:** 100 ühikut hinnaga 10 tabelis ei taga 100 000 ühiku müüki sama hinnaga.

**Vestluses kasutamine:** Küsi positsiooni suuruse ja väljumise tähtaja kohta.

**Piirang või erand:** Likviidsus muutub; tavapärane maht pole stressi garantii.

**Allikas või tõendus:** [SCHWAGER] ptk 4; originaalne sõnastus ja näide. [Riskilabor](../laborid/03-varjatud-risk.md).

<a id="p50"></a>
## 50. Stressitest küsib „mis siis, kui”, mitte alati „kui tõenäoline”.

**Liik:** Praktiline rusikareegel.

**Täpne tähendus:** Stsenaarium võib olla kasulik ka täpse tõenäosuseta.

**Miks oluline?** See aitab tuvastada sundmüügi ja maksevõime piire.

**Mehhanism:** Arvuta portfelli tulemus ette määratud šoki all.

**Näide:** Vara −30% ja 2× võimendus annavad lihtmudelis omakapitalile −60%.

**Vestluses kasutamine:** Kasuta puhvri ja kahjukandevõime hindamisel.

**Piirang või erand:** Halvim valitud stsenaarium ei ole loogiliselt halvim võimalik stsenaarium.

**Allikas või tõendus:** [ANALÜÜS]/[NÄIDE]: selle kirje valem, aritmeetiline näide või metoodiline põhjendus on iseseisev tõendus; tegemist pole turult mõõdetud seadusega.
