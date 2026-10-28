# Investeerimise alused: mida tootlus tegelikult tähendab?

[Tagasi avalehele](../README.md) · [24 Pythoni näidet](../10-python-ja-andmed/24-naidet.md) · [Ülesanded 1–10](../17-50-ulesannet/01-ulesanded.md)

## Sisukord

- [Õpieesmärgid ja õppetasemed](#õpieesmärgid-ja-õppetasemed)
- [Rahavoog, hind ja omandiõigus](#rahavoog-hind-ja-omandiõigus)
- [Tootluse arvutamine](#tootluse-arvutamine)
- [Kasv läbi aja](#kasv-läbi-aja)
- [Inflatsioon, valuuta ja kulud](#inflatsioon-valuuta-ja-kulud)
- [Sissemaksed ning kaks tulemusmõõdikut](#sissemaksed-ning-kaks-tulemusmõõdikut)
- [Hind, väärtus ja alternatiivkulu](#hind-väärtus-ja-alternatiivkulu)
- [Kontrollküsimused ja õpetamine](#kontrollküsimused-ja-õpetamine)

## Õpieesmärgid ja õppetasemed

Oskad arvutada liht-, kogu-, geomeetrilist ja reaaltootlust; eristada tootlust sissemaksest; arvestada valuutat ja tasusid ning sõnastada, millisele küsimusele valitud mõõdik vastab.

**5 minutit:** loe näidet +20% ja −20%, reaaltootluse valemit ning põhivigu.

**30 minutit:** tuleta valemid ja lahenda ülesanded 1–10.

**90 minutit:** käivita lühinäited 1–5 ja 20, muuda sisendeid ning selgita tulemust õpilasele, kes pole varem investeerinud.

Selle mooduli matemaatilised näited on [ANALÜÜS]/[NÄIDE]/[MUDEL]. [PAPP] ptk 1–2 annavad investeerimise ja finantsnäitajate tausta; [SCHWAGER] ptk 3 ja 5 aitavad küsida, mida minevikutootlus ning keskmised tegelikult näitavad. Autorite teksti asemel kasutame eraldi konstrueeritud arvutusi.

## Rahavoog, hind ja omandiõigus

Investeeringut aitab mõista kolm küsimust: **mida ma oman, milliseid makseid võin saada ning mis tingimustel saan väljuda?** Aktsia on osalus ettevõttes; võlakiri on lepinguline nõue; fondiosak on osalus fondis. Õigus ja makse ei ole sama: lubatud makse võib jääda täitmata ning omanikule ei pruugita jooksvalt midagi välja maksta.

**Hind** on summa, millega tehing praegu toimub. **Väärtus** on hinnang tulevaste kasude ja riskide põhjal. **Tootlus** on investori kapitali ja rahavoogude tegelik või mudeldatud muutus. Nende eristamine väldib arutlust „ettevõte on hea, järelikult peab aktsia tõusma”. Hea äri võib olla ostetud hinnaga, mis eeldab juba erakordset tulevikku.

## Tootluse arvutamine

Ühe perioodi lihttootlus (*simple return*) ilma välise rahavoota on

$$r=\frac{V_1-V_0}{V_0}.$$

$V_0$ on algväärtus ja $V_1$ lõppväärtus. Kui väärtus kasvab 100-lt 110-le, siis $r=0.10=10\%$. „Kümme protsenti” tähendab 0.10 osa algkapitalist; kümme protsendipunkti tähendab kahe protsendimäära aritmeetilist vahet.

Kui vara maksab perioodi lõpus dividendi või muud raha $D$, mida lõppväärtus veel ei sisalda:

$$r_{\mathrm{kogu}}=\frac{V_1-V_0+D}{V_0}.$$

[NÄIDE] Aktsia hinnaga 100 lõpetab hinnal 98 ja maksab dividendi 5. Hinnatootlus on −2%, kogutootlus +3%. Dividenditootlus üksi oleks 5%, kuid seegi ei kirjelda tervikut. Mitme perioodi võrdluses tuleb määrata, kas dividendid reinvesteeritakse ning milliste kuludega.

Logtootlus (*log return*) on $g=\ln(1+r)$. Logtootlused liituvad läbi aja, sest logaritm teisendab korrutise summaks. Lihttootlused liituvad kaalutult ühe perioodi portfellis. Neid kahte mugavust ei tohi segi ajada: portfelli logtootlus ei võrdu üldjuhul komponentide logtootluste kaalutud keskmisega.

## Kasv läbi aja

Kahe perioodi kapital on $V_2=V_0(1+r_1)(1+r_2)$. Üldiselt:

$$V_n=V_0\prod_{t=1}^{n}(1+r_t).$$

[NÄIDE] 100 eurot, +20%, seejärel −20%: $100\times1.2\times0.8=96$. Aritmeetiline keskmine on null, kuid kahjum on 4%. CAGR ehk geomeetriline keskmine aastane kasvutempo on võrdsete aastaperioodide korral:

$$\operatorname{CAGR}=\left(\frac{V_n}{V_0}\right)^{1/n}-1.$$

Siin $\sqrt{0.96}-1\approx-2.0204\%$. See on konstantne aastamäär, mis annaks sama lõppkapitali, mitte väide, et mõlemal aastal teeniti tegelikult see määr.

**Miks geomeetriline keskmine ei ületa aritmeetilist?** Positiivsetele kasvuteguritele kehtib AM–GM võrratus. Seega sama aritmeetilise keskmise juures annab konstantne tootlus vähemalt sama suure korrutise kui kõikumine. See ei tähenda, et iga kõrgema volatiilsusega vara teeniks vähem: tema keskmine võib olla kõrgem.

**Kahjumist taastumine.** Pärast osakaalu $d$ kaotamist jääb kapitali $1-d$. Taastumiseks on vaja $g$, mille korral $(1-d)(1+g)=1$. Seega $g=d/(1-d)$. Näiteks 35% kahjumi järel on vajalik kasv umbes 53.85%.

## Inflatsioon, valuuta ja kulud

Reaaltootlus (*real return*) mõõdab ostujõu muutust:

$$1+r_{\mathrm{reaal}}=\frac{1+r_{\mathrm{nominaal}}}{1+\pi},$$

kus $\pi$ on sama perioodi inflatsioon. 8% nominaaltootlus ja 5% inflatsioon annavad 2.8571%, mitte täpselt 3%. Nominaalmäära ja inflatsiooni lahutamine on väikeste määrade lähend.

Valuutariski jaoks defineeri kõigepealt kursi suund. Kui $X$ on eurot ühe dollari kohta, siis dollarivara euroväärtuse tegur on

$$1+r_{\mathrm{EUR}}=(1+r_{\mathrm{USD}})\frac{X_1}{X_0}.$$

Dollari odavnemine 10% ja vara kallinemine dollarites 10% annavad eurodes $1.1\times0.9-1=-1\%$. Vastupidise kursinoteeringu korral peab kasutama pöördtegurit. Fondi eurodes noteerimine ei määra üksi tema alusvarade valuutariski.

Aasta lõpus varalt võetava proportsionaalse tasu $f$ korral on mudeli netokasvutegur $(1+r)(1-f)$. 7% brutotootlus ja 1% tasu annavad 5.93% netotootluse. Reaalne toode võib võtta tasusid jooksvalt, lisada tehingutasu ja hinnavahe; seepärast kirjuta ajastus välja. Kulude üldist mõju selgitab ka [SEC-i teabeleht](../allikad/veebiallikad.md), kuid selle mooduli arvud on iseseisvad näited.

## Sissemaksed ning kaks tulemusmõõdikut

[NÄIDE] Algkapital 100 kasvab esimese aasta lõpuks 110-ni. Lisad siis 100. Teisel aastal tootlus 0%, lõppkapital 210. Konto kasv on 110%, kuid investeerimisstrateegia pole teeninud 110%.

**Ajaga kaalutud tootlus** (*time-weighted return*, TWR) lõikab ajaloo väliste rahavoogude juures perioodideks ja korrutab nende kasvutegurid. Näites on kahe aasta TWR $1.1\times1-1=10\%$ ning aastane geomeetriline määr umbes 4.88%.

**Rahaga kaalutud tootlus** (*money-weighted return*, sageli IRR) arvestab investori kapitali ajastust. Aastamäär $i$ lahendab näites

$$100(1+i)^2+100(1+i)=210.$$

Seades $x=1+i$, saame $x^2+x-2.1=0$, millest $i=(-1+\sqrt{9.4})/2-1\approx3.2971\%$. Investoril oli suurem summa turul just nulltootlusega teisel aastal.

TWR sobib väliste rahavoogude mõjust eraldatud strateegia hindamiseks; rahaga kaalutud määr kirjeldab paremini kapitali tegelikku ajastust. Ebatavaliste mitme märgivahetusega rahavoogude korral võib IRR-l olla mitu lahendit; siis ei piisa ühe kalkulaatorinumbri esitamisest.

## Hind, väärtus ja alternatiivkulu

Raha ajaväärtus küsib, kuidas võrrelda eri aegadel saadavaid summasid. Kui aasta pärast saadav kindel 1100 on diskonteeritud 10%-ga, on väärtus täna 1000. Riskantse rahavoo puhul tuleb määrata, kuidas risk kajastub rahavoos või diskontomääras.

Alternatiivkulu pole eraldi teenustasu. See on loobutud võrreldav võimalus. 3% tootlus pole iseenesest „hea” või „halb”, kui me ei tea riski, horisonti, likviidsust ja alternatiive. Võrdlus 10% lootusega riskantse varaga ei tee 3% kindlamat makset automaatselt halvemaks.

## Kontrollküsimused ja õpetamine

1. Miks on +20% ja −20% järel kapital väiksem? **Vastus:** teine protsent rakendub muutunud baasile.
2. Miks ei piisa fondi hinna graafikust? **Vastus:** dividendid, kulud, valuuta ning sissemaksed võivad muuta investori tulemust.
3. Millal sobib aritmeetiline keskmine? **Vastus:** näiteks sama jaotusega ühe perioodi tootluse ootuse hinnanguks, mitte otse mitme perioodi kapitalikasvuks.
4. Kas 100% kahjumist saab sama kapitaliga taastuda? **Vastus:** ei, nullkapital vajab uut ressurssi.
5. Miks TWR ja IRR võivad erineda? **Vastus:** kapitali maht oli eri tootlusperioodidel erinev.

**Viis meeldejäävat põhimõtet:** määra ajahorisont; kasuta õiget protsendibaasi; arvesta rahavooge; erista raha ja ostujõudu; võrdle sama riski ja perioodiga alternatiive.

**90 minuti kava:** 10 min algprobleem; 20 min kasvutegurid; 15 min inflatsioon ja valuuta; 20 min Pythoni katsed; 15 min rahavoogude näide; 10 min selgitus kaasõppijale. Hindamisel nõua nii arvu kui ka selle tähendust.
