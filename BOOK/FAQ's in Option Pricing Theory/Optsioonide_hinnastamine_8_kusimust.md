# Optsioonide hinnastamine: kaheksa küsimust, mida tasub päriselt mõista

**Eestikeelne juhend ja arvutuslabor Peter Carri „FAQ’s in Option Pricing Theory” põhjal**  
Koostatud 29.10.2026. Vorming: GitHub Markdown. Siht: mõista, arvutada ja selgitada.

> Põhiidee: optsiooni hind ei ole lihtsalt ennustus tulevasest väljamaksest. Arbitraaživaba hinnastamine küsib, millise kaubeldavate varade portfelliga saab sama väljamakse tekitada ja millist riski ei saa sel viisil kõrvaldada.

## Kuidas materjali kasutada

Alusta kaheksa lühivastuse tabelist. Seejärel õpi peatükid 1–4, mis annavad hinnastamise aluse; peatükid 5–7 näitavad selle piire; peatükk 8 ühendab teooria tegeliku riskimaandamise tulemusega. Iga peatükk sisaldab intuitsiooni, arvutust, Pythoni katset, praktilist ja AI-seost, väärarusaama, ülesannet ning prompti.

**Allikate eristus:**

- **[PDF]** Carri esitluse mõte, esitatud oma sõnadega. Viited on PDF-i füüsilistele lehekülgedele; slaidile trükitud number on enamasti ühe võrra väiksem.
- **[SELGITUS]** mõiste või põhjenduse pedagoogiline lahtikirjutus.
- **[NÄIDE]** selle juhendi arvuline või programmeerimisnäide, kui pole teisiti märgitud.
- **[TÄIENDUS]** tänapäevane rakendus, AI, tarkvara või praktiline piirang. Need ei pärine 1999. aasta esitlusest.

Algallikas on 45-leheküljeline esitlus, mitte kaasaegne AI-käsiraamat. Selle vigase tekstikihi tõttu kasutati tekstituvastust; keerukad valemid on siin esitatud ühtses tähistuses ja tuletatud selgituste kaudu. AI-lahendused on juhendi lisandused. Näited on sünteetilised, mitte reaalaja turuandmed ega konkreetse tehingu soovitused.

### Sisukord

1. [Miks ei piisa diskonteeritud keskmisest väljamaksest?](#k1)
2. [Miks ei määra statistilised tõenäosused binoommudeli hinda?](#k2)
3. [Miks puudub Black–Scholesi valemist aktsia oodatav tootlus?](#k3)
4. [Kas maandamisargument on korrektne ja kuhu jäävad kaalude muutused?](#k4)
5. [Kas trinoommudelis saab optsioone maandada?](#k5)
6. [Kas pidevas ajas saab hüppeid maandada?](#k6)
7. [Miks ilmub riski turuhind ja miks näib see HJM-ist puuduvat?](#k7)
8. [Kui palju kaotan vale volatiilsusega maandades?](#k8)
9. [Pythoni labor ja kontrollitud tulemused](#labor)
10. [AI-töövoog ja promptide kogumik](#ai)
11. [Õppeplaan, teadmiste kontroll ja allikad](#ope)

## Kaheksa lühivastust

| Küsimus | Vastus, mille saad suuliselt anda |
|---|---|
| 1. Miks mitte lihtsalt keskmine väljamakse? | Tegelike tõenäosuste keskmine ei arvesta üldjuhul riski hinda. Replitseeritava optsiooni hind peab võrduma sama väljamakse tootva portfelli hinnaga. Riskineutraalse mõõdu all saabki kasutada diskonteeritud keskmist. |
| 2. Miks binoommudelis tegelik tõenäosus kaob? | Aktsia ja rahakonto katavad kaks võimalikku lõppseisundit täpselt. Hind tuleneb nende turuhindadest; tegelik tõenäosus on endiselt oluline prognoosile ja riskile. |
| 3. Miks BS-is pole oodatavat tootlust? | Delta-maandus kõrvaldab sama aktsiariski, millega kaasneb aktsia oodatav tootlus. Alles jääv hinnastamisvõrrand sõltub riskivabast intressist, volatiilsusest ja lepingu tingimustest. |
| 4. Miks ei diferentseerita osakute arvu? | Portfelli väärtuse diferentseerimisel peab seda tegema. Isefinantseerimise korral rahastatakse kaalude muutused portfelli seest ning nende netopanus väärtuse muutusesse kaob. |
| 5. Kas trinoommudelis saab maandada? | Aktsia ja rahakontoga üldist kolmeseisundilist väljamakset täpselt ei kata. Vaja võib olla kolmandat sõltumatut instrumenti või leppimist jääkriskiga. |
| 6. Kas hüppeid saab maandada? | Delta kõrvaldab esimese järgu hinnariski, kuid hüppe mittelineaarne osa jääb. Täpne maandamine sõltub hüpperiski struktuurist ja kaubeldavatest instrumentidest. |
| 7. Miks riski turuhind ilmub või kaob? | See seob tegeliku maailma ja hinnastamise dünaamika. Riskineutraalses HJM-is määrab arbitraaživabadus forward-intressi triivi volatiilsuse kaudu; riskipreemia ei kao tegelikust maailmast. |
| 8. Kui palju kaotan vale volatiilsusega? | Vahe sõltub gamma-kaalutud tegeliku ja kasutatud dispersiooni erinevusest, hinnast, teekonnast, tehingukuludest ja maandamise sagedusest. Üks volatiilsuste vahe ei anna universaalset kahjumit. |

## Eelteadmised ja tähistus

**Call** ehk ostuoptsioon annab ostjale õiguse osta vara kokkulepitud hinnaga. Euroopa call'i lõppväljamakse on $H=(S_T-K)^+=\max(S_T-K,0)$. **Put** annab müügiõiguse ning selle väljamakse on $(K-S_T)^+$. Euroopa optsiooni saab realiseerida lõpptähtajal; Ameerika optsiooni korral võib varasem realiseerimine olla lubatud.

**Väljamakse ei ole kasum.** Kui maksad call'i eest 8 ning lõppväljamakse on 20, on kasum nullintressi ja kuludeta 12. Ühe alusvaraühiku kohta saadud tulemus tuleb tegeliku lepingu puhul korrutada selle lepingukordajaga. Kordajat ei tohi vaikimisi eeldada.

| Tähis/termin | Tähendus |
|---|---|
| $S_t$, $K$, $T$, $\tau=T-t$ | Alusvara hind, täitmishind, lõpptähtaja hetk, järelejäänud aeg aastates |
| $V$, $C$, $H$ | Tuletise hind, call'i hind, lõppväljamakse |
| $r$, $\mu$, $\sigma$ | Pideva kapitalisatsiooniga riskivaba intress, aktsia oodatav tootlus, aastane volatiilsus |
| $\mathbb P$ | Tegelik/statistiline tõenäosusmõõt (*physical measure*) |
| $\mathbb Q$ | Riskineutraalne hinnastamismõõt (*risk-neutral measure*) |
| Replikatsioon (*replication*) | Sama väljamakse tekitamine teiste kaubeldavate varadega |
| Arbitraaž (*arbitrage*) | Mudeli tingimustes riskita positiivne võimalus ilma positiivse alginvesteeringuta |
| Täielik turg (*complete market*) | Kõik vaadeldava mudeli lubatud väljamaksed on kaubeldavate varadega replitseeritavad |
| Isefinantseeriv (*self-financing*) | Tehinguid rahastatakse portfellist, väljast raha lisamata ja välja võtmata |
| $\Delta=V_S$, $\Gamma=V_{SS}$ | Hinnatundlikkus ja selle muutumise kiirus |
| $\nu=V_\sigma$ | Vega: tundlikkus volatiilsuse suhtes; kontrolli ühikut, 1,00 versus üks protsendipunkt |
| $\Theta=V_t$ | Aja möödumise mõju; ajamuutuja valik mõjutab märki |
| Kalibreerimine | Mudeli parameetrite sobitamine turuhindadega |
| Prognoosimine | Tulevaste tegelike tulemuste ennustamine |

Baasmudelis eeldame dividendideta aktsiat, Euroopa optsiooni, vabalt jagatavaid positsioone, ühesugust laenu- ja hoiuseintressi ning tehingukulude puudumist. Pidevat maandamist kasutatakse teoreetilises tuletuses; arvutis ja turul on sammud diskreetsed. Muudetud eeldused tuleb alati välja öelda.

<a id="k1"></a>
## 1. Miks pole optsiooni väärtus lihtsalt diskonteeritud keskmine väljamakse?

**[PDF, lk 3–7]** Carr kasutab aktsiat, mis maksab praegu 1 ja võib tõusta 2-ni või langeda 0,50-ni. Mõlemad seisundid on tegelikus maailmas võrdselt tõenäolised, intress on null ning call'i täitmishind on 1.

### Intuitsioon

Kui saad ühe ja sama lõpptulemuse kahel viisil, ei saa nende kindlalt kättesaadavate lahenduste hinnad arbitraaživabal turul erineda. Optsiooni ostmise asemel võid osta aktsiaid ja võtta laenu. Siis tuleb vaadata selle portfelli maksumust, mitte üksnes keskmist väljamakset.

### Arvutus

Tegelik keskmine väljamakse on $0{,}5\cdot1+0{,}5\cdot0=0{,}50$. Otsime aga aktsiapositsiooni $\Delta$ ja rahasummat $b$:

$$2\Delta+b=1,\qquad 0{,}5\Delta+b=0.$$

Seega $\Delta=2/3$, $b=-1/3$ ning portfelli hind on $2/3-1/3=1/3$.

| Lõppseisund | 2/3 aktsiat | Laenu tagasimakse | Portfelli netoväärtus | Call |
|---|---:|---:|---:|---:|
| Aktsia 2 | 1,3333 | −0,3333 | 1 | 1 |
| Aktsia 0,50 | 0,3333 | −0,3333 | 0 | 0 |

Kui call maksaks 0,50, saaks selle müüa ja osta replikatsiooni 0,3333 eest. Alguses jääks üle 0,1667 ning lõpus kohustused tasakaalustuksid mõlemas seisundis. See on mudelis arbitraaž, eeldades muu hulgas võimalust optsiooni müüa ning tehinguid teha näidatud hindadega.

**Riskineutraalne keskmine töötab.** Hinnastamistõenäosus $q$ rahuldab $1=2q+0{,}5(1-q)$, millest $q=1/3$. Seega $C=E^{\mathbb Q}[H]=1/3$.

Üldiselt deterministliku intressi korral:

$$V_t=e^{-r(T-t)}E^{\mathbb Q}[H\mid\mathcal F_t].$$

Juhusliku intressi korral on diskontotegur ootuse sees. Tegeliku mõõdu all võib kirjutada $V_t=E^{\mathbb P}[M_{t,T}H\mid\mathcal F_t]$, kus $M$ on sobiv **stohhastiline diskontotegur**. See ei ole üldjuhul lihtsalt konstant $e^{-r(T-t)}$.

### Python, praktiline kasutus ja AI

**[NÄIDE]** Käivita labori `binomial()`: saad hinna 0,333333, delta 0,666667 ja laenu 0,333333.

**[TÄIENDUS]** Kui AI prognoosib tõusu tõenäosuseks 70%, saad prognoosida call'i tegelikku keskmist väljamakset. See ei luba asendada replikatsioonihinda prognoosikeskmisega. Hoia analüüsis eraldi veerud `forecast_expected_payoff`, `model_price`, `market_bid`, `market_ask`. Nende erinevus aitab esitada õige küsimuse: kas mudel on vale, prognoos ebakindel või tehing pärast kulusid huvitav?

**Väärarusaam:** riskineutraalne mõõt tähendab, et investorid on tegelikult riskineutraalsed. Ei: see on hinnastamise matemaatiline esitus.

**Ülesanne.** Sama optsiooni turuhind on 0,25. Milline vastupidine arbitraaž tekib?  
**Vastus:** osta call 0,25 eest ja müü selle replikatsioon 1/3 eest. Alguses saad 1/12; lõpptulemused tühistuvad. Praktikas tuleb kontrollida shortimise ja finantseerimise võimalikkust.

**Lisaküsimuse prompt:**

> Selgita P- ja Q-mõõdu vahet, kasutades S0=1, Su=2, Sd=0,5, K=1 ja r=0. Arvuta replikatsioon ning mõlemas lõppseisundis arbitraaži rahavood hinnale 0,50. Ära samasta tegelikku prognoosi riskineutraalse tõenäosusega. Lisa juhtum, kus lihtne diskonteeritud P-keskmine siiski sobiks.

<a id="k2"></a>
## 2. Miks ei loe binoommudelis statistilised tõenäosused?

**[PDF, lk 8–12]** Oluline on lokaalne lineaarsus: kahe võimaliku väärtuse vahel saab iga väljamakse kujutada aktsia ja raha kombinatsioonina. Mitme perioodi korral korratakse sama sammu igas sõlmes tagant ettepoole.

### Mida väide tegelikult tähendab?

Hoidkem fikseerituna praegune aktsiahind, võimalikud lõpphinnad ja intress. Siis ei sõltu replikatsioonihind tegelikust tõusutõenäosusest $p$, kui mõlemad seisundid on võimalikud. See ei tähenda, et tõenäosused ei mõjutaks majandust või turuhindu laiemalt. Uus info võib muuta juba aktsia tänast hinda.

Olgu $S_u=uS_0$, $S_d=dS_0$ ning ühe perioodi rahakasvutegur $R=e^{r\Delta t}$. Siis:

$$\Delta=\frac{H_u-H_d}{S_u-S_d},\quad b=\frac{H_d-\Delta S_d}{R},\quad V_0=\Delta S_0+b.$$

Sama hind avaldub kujul:

$$q=\frac{R-d}{u-d},\qquad V_0=\frac{qH_u+(1-q)H_d}{R}.$$

Arbitraaživabas kahe võimaliku seisundiga mudelis peab kehtima $d<R<u$, nii et $0<q<1$.

### Arvuline katse

Eelmise näite korral:

| Tegelik $p$ | Tegelik oodatav call'i väljamakse | Replikatsioonihind |
|---:|---:|---:|
| 0,20 | 0,20 | 0,3333 |
| 0,50 | 0,50 | 0,3333 |
| 0,80 | 0,80 | 0,3333 |

**Kahe sammu näide.** Aktsia 1 liigub kummalgi sammul teguriga 2 või 0,5, intress null ja K=1. Lõpphinnad on 4, 1 ja 0,25 ning call'i väljamaksed 3, 0 ja 0. Ülemises vaheolekus on call väärt 1, alumises 0; alguses 1/3. Kahe järjestikuse tõusu Q-tõenäosus on 1/9, seega ka otse $3/9=1/3$.

### Python ja praktiline vajadus

Labor muudab $p$ väärtusi, jättes replikatsioonihinna samaks. Muuda seejärel `R=1.05`: hinnastamistõenäosus muutub 0,366667-ks ja hind ligikaudu 0,349206-ks. Intress mõjutab hinda, sest rahastamine on replikatsiooni osa.

**[TÄIENDUS]** Klassifitseeriv ML-mudel võib hinnata tegelikku tõusu tõenäosust, näiteks uudiste ja hinnatunnuste abil. Binoompuu $q$ tuleb seevastu arbitraaživabaduse tingimusest. ML-mudelit hinnatakse ajaliselt hilisematel andmetel, kasutades näiteks Brieri skoori ja tõenäosuste kalibreeritust; optsioonimootorit hinnatakse replikatsiooni, hinnapiiride ja turuhindade suhtes.

**Väärarusaam:** ajaloolistest hindadest mõõdetud $p$ peab olema puu hinnastamistõenäosus. See segab prognoosimudeli hinnastamismudeliga.

**Ülesanne.** Kui $u=1{,}2$, $d=0{,}8$, $R=1$, kui suur on $q$? Kas see tõestab, et turg tõuseb pooltel juhtudel?  
**Vastus:** $q=0{,}5$. Ei; see on mudeli hinnastamistõenäosus.

**Prompt:**

> Ehita kaheperioodiline binoompuu ja näita igas sõlmes optsiooni hind, delta ja rahakonto. Kasuta S0=1, u=2, d=0,5, K=1, R=1. Kontrolli, et igal sammul replikatsioon klapib. Selgita, mis muutub ja mis ei muutu, kui tegelik tõusutõenäosus muutub 0,3-lt 0,8-le.

<a id="k3"></a>
## 3. Miks puudub Black–Scholesi valemist aktsia oodatav tootlus?

**[PDF, lk 13–19]** Carr seob tulemuse Itô valemi ja lõpmata väikese ajasammu lokaalse lineaarsusega. Tingimuslikult antud aktsiahinnale ei vaja replikatsioon aktsia oodatava tootluse teadmist.

### Intuitsioon

Kui optsiooni ja aktsia väikesed hinnamuutused tulenevad samast juhuslikust liikumisest, saab õige aktsiakogusega selle mõju tasakaalustada. Nii kaob hinnastamisvõrrandist ka sama riskiga seotud oodatav tootlus.

Olgu tegeliku maailma aktsiadünaamika:

$$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t^{\mathbb P}.$$

Itô valem annab:

$$dV=V_tdt+V_SdS+\tfrac12V_{SS}\sigma^2S^2dt.$$

Optsiooni replitseeriva isefinantseeriva portfelli aktsiapositsioon on $\Delta=V_S$. Selle väärtuse muutus on:

$$dX=\Delta\,dS+r(X-\Delta S)dt.$$

Pannes $X=V$ ja võrdsustades muutused, kaob $V_SdS$ mõlemalt poolt:

$$V_t+\tfrac12\sigma^2S^2V_{SS}+rSV_S-rV=0.$$

See on dividendideta Black–Scholesi osatuletistega diferentsiaalvõrrand. Lõpptingimus call'ile on $V(S,T)=(S-K)^+$. Lahendus on:

$$C=S\Phi(d_1)-Ke^{-r\tau}\Phi(d_2),$$

$$d_1=\frac{\ln(S/K)+(r+\sigma^2/2)\tau}{\sigma\sqrt\tau},\qquad d_2=d_1-\sigma\sqrt\tau.$$

$\Phi$ on standardnormaaljaotuse jaotusfunktsioon. Pideva dividendimääraga $q_d$ lisandub aktsiaosa ette $e^{-q_d\tau}$ ning $d_1$-s kasutatakse $r-q_d$. Ära aja dividendimäära segamini eelmise peatüki tõenäosusega $q$.

### Arvuline näide

$S=K=100$, $r=0$, $\tau=1$, $\sigma=20\%$:

- call'i hind $C\approx7{,}9656$;
- delta $\Delta\approx0{,}53983$;
- gamma $\Gamma\approx0{,}019848$;
- volatiilsusega 30% oleks hind $11{,}9235$.

Arvamused „aktsia oodatav tootlus on 5%” ja „see on 15%” annavad samade BS-sisendite korral sama hinna. Aktsia hinna või volatiilsuse muutumine muudab seda siiski.

### Python, AI ja piirid

Labori `bs(100)` arvutab hinna ja tundlikkused. Delta kontrollitakse lõpliku vahega $(C(S+h)-C(S-h))/(2h)$. See on lihtne viis AI kirjutatud tuletise või koodi kontrollimiseks.

**[TÄIENDUS]** AI võib aidata modelleerida volatiilsust, sobitada optsioonihindade pinda või kiirendada aeglast hinnastamismudelit. Implitsiitne volatiilsus on turuhinnast tagasi arvutatud mudeliparameeter, mitte automaatselt tulevase realiseerunud volatiilsuse erapooletu prognoos. Mudeli kiirendaja peab säilitama hinnapiirid ja tundlikkuste kvaliteedi; väike hinnaviga ei taga väikest deltaviga.

**Väärarusaam:** kuna $\mu$ puudub hinnast, pole tootlusprognoosist kasu. See on oluline investeerimisotsustele, tegelikule P&L-jaotusele ja riskistsenaariumidele; lihtsalt mitte BS-replikatsioonihinna eraldi sisendina.

**Ülesanne.** Kas $\sigma=0$ korral saab ülaltoodud valemit otse kasutada?  
**Vastus:** mitte jagamise tõttu nulliga. Piirväärtus on deterministlikus mudelis $\max(S-Ke^{-r\tau},0)$. Labor nõuab positiivset volatiilsust.

**Prompt:**

> Tuleta Black–Scholesi PDE isefinantseeriva portfelli kaudu. Näita täpselt, millises reas mu kaob. Erista osatuletis aja järgi ja järelejäänud aja järgi. Selgita, millised eeldused ei kehti hüpete või juhusliku volatiilsuse korral. Kontrolli näidet S=K=100, T=1, r=0, sigma=0,2.

<a id="k4"></a>
## 4. Kas Black–Scholesi maandamisargument on korrektne? Miks ei diferentseerita positsiooni suurust?

**[PDF, lk 20–22]** Carr eristab portfelli väärtuse täielikku diferentsiaali ja hoitud instrumentidelt saadud kauplemiskasu (*gains process*). See on eelkõige raamatupidamise ja isefinantseerimise küsimus. Lihtsustatud argument võib varjata rahavooge; kaalude muutusi ei tohi lihtsalt olematuks kuulutada. Korrektselt sõnastatud replikatsioon annab BS-tulemuse.

### Intuitsioon: aktsiate juurdeost tuleb kusagilt rahastada

Olgu aktsiahind 100, portfellis 0,5 aktsiat ja rahakontol 10. Väärtus on 60. Hind tõuseb 102-ni: portfell on nüüd 61. Kui soovid suurendada aktsiapositsiooni 0,6-ni, ostad 0,1 aktsiat hinnaga 10,20. Rahakontole jääb −0,20. Portfelli väärtus on endiselt $0{,}6\cdot102-0{,}20=61$.

Positsiooni muutmine ei loonud uut rikkust. See liigutas väärtust rahakonto ja aktsiate vahel.

### Täpne matemaatika

Olgu $B_t$ riskivaba konto ühe ühiku hind, $dB_t=rB_tdt$, ning $\beta_t$ selle ühikute arv:

$$X_t=\Delta_tS_t+\beta_tB_t.$$

Korrutise Itô reegel annab:

$$dX=\Delta dS+S d\Delta+d[\Delta,S]+\beta dB+B d\beta.$$

Siin $[\Delta,S]$ on ruutkovariatsioon; lõpliku variatsiooniga $B$ ruutkovariatsioon on null. **Isefinantseerimine** tähendab:

$$S d\Delta+d[\Delta,S]+B d\beta=0,$$

mistõttu

$$dX=\Delta dS+\beta dB.$$

Seega kaalude muutused ei puudu korrutise tuletisest: nende rahaline mõju tasakaalustub. Sama asja saab kirjutada stohhastilise integraalina $X_t=X_0+\int_0^t\Delta_u\,dS_u+\int_0^t\beta_u\,dB_u$.

Levinud vigane samm on nimetada $V-\Delta S$ isefinantseerivaks portfelliks ja kohe kirjutada selle muutuseks $dV-\Delta dS$, täpsustamata ümberpaigutamise rahavooge. „Hoian deltat ühe lühikese intervalli jooksul paigal” on lubatav diskreetne strateegia, kuid see ei ole sama mis muutuva $\Delta_tS_t$ täielik diferentseerimine.

### Python ja praktiline vajadus

Labor kontrollib näidet 0,5 → 0,6 aktsiat ning annab uueks rahakontoks −0,20. Simulatsioonis toimub iga tehing kujul:

```python
cash -= (new_delta - old_delta) * spot + transaction_cost
```

**[TÄIENDUS]** AI genereeritud backtest'ides on sage sisuline risk tehingute rahavoo unustamine. Nõua eraldi tehingulogis välju `time`, `spot`, `old_delta`, `new_delta`, `trade_cashflow`, `fee`, `cash_after`, `portfolio_value`. Kontrolli SQL-i või Pythoni abil identiteeti: pärast tehingut peab väärtus muutuma ainult tehingukulu võrra. Aktsiate juurdeost ei tohi paista tasuta tuluna.

**Ülesanne.** Näite juurdeostu tasu on 0,05. Mis on rahakonto ja portfelli väärtus?  
**Vastus:** rahakonto −0,25 ja portfell 60,95. Vähenemine 0,05 on kulu.

**Prompt:**

> Auditeeri minu delta-maandamise koodi isefinantseerimise seisukohast. Näita iga ümberpaigutamise eelne ja järgne raha, aktsiapositsioon ning portfelli väärtus. Kontrolli intressi, laenu, tehingukulusid ja lõpparveldust. Ära eelda, et new_delta*spot võib lisada portfelli ilma rahakontot vähendamata. [Lisa kood.]

<a id="k5"></a>
## 5. Kas trinoommudelis saab optsioone maandada?

**[PDF, lk 23–36]** Kolm lõppseisundit vajavad üldiselt kolme sõltumatut väljamaksevektorit. Carr käsitleb lisaks staatilist replikatsiooni optsioonidega, butterfly-positsioone ning staatiliste ja dünaamiliste tehingute ühendamist.

### Intuitsioon: võrrandeid on rohkem kui tundmatuid

**[NÄIDE]** Aktsia hind on 100, lõpphinnad 80, 100 või 120 ja intress null. K=100 call maksab lõpus vastavalt 0, 0 või 20. Aktsia ja raha peaksid rahuldama:

$$80\Delta+b=0,\quad100\Delta+b=0,\quad120\Delta+b=20.$$

Esimesest kahest tuleb $\Delta=b=0$, kuid siis kolmas ei kehti. Üldine call ei ole nende kahe instrumendiga täpselt replitseeritav. Lineaarse väljamaksega nõue $a+bS_T$ oleks küll.

### Mittetäielikkus tähendab hinnavahemikku, mitte arvutusviga

Martingaalitingimus annab:

$$q_d+q_m+q_u=1,\qquad80q_d+100q_m+120q_u=100.$$

Seega $q_d=q_u=a$, $q_m=1-2a$, kus kõigi kolme võimaliku seisundi puhul $0<a<1/2$. Call'i hind on $20a$; aktsia ja raha hinnad üksi ei erista näiteks hindu 4 ($a=0{,}2$) ja 6 ($a=0{,}3$). Rangelt positiivsete seisunditõenäosustega arbitraaživabade hindade vahemik on siin $(0,10)$; 0 ja 10 on selle piirid. Piirhinnad võivad võimaldada arbitraaži, kui kõik kolm seisundit on tegelikult võimalikud.

### Kolmas instrument

Lisa sama täitmishinnaga kaubeldav put, mille väljamaksevektor on $(20,0,0)$. Siis kehtib kõigis seisundites:

$$\text{call}=1\times\text{aktsia}-100\times\text{rahaühik}+1\times\text{put}.$$

See on put–call-pariteet. Kui put maksab 5, on call'i hind samuti 5. Kolmanda instrumendi **turuhind** annab uue info; üksnes väljamakse kirjeldamisest ei piisa. Instrumendid peavad olema lineaarselt sõltumatud, mitte kolm eri nime sama riski jaoks.

Mitme perioodi mudelis ei piisa automaatselt ühe optsiooni tänase hinna teadmisest. Tulevastes sõlmedes on vaja ka selle hinnadünaamika või piisava hulga teiste instrumentide hinnainfo kirjeldust. Sama lõppjaotus ei määra üldiselt teekonnast sõltuva optsiooni hinda.

### Staatiline replikatsioon ja butterfly

Võrdse täitmishindade sammuga call-butterfly on:

$$B(S_T)=(S_T-K_1)^+-2(S_T-K_2)^++(S_T-K_3)^+,$$

kus $K_2=(K_1+K_3)/2$. Näiteks K=80,100,120 annab väljamaksed 0,20,0 nendes kolmes punktis. See isoleerib keskmise piirkonna riski. Piisava arvu strike'idega saab lõpphinnast sõltuvat väljamakset tükkhaaval lineaarselt taastada. See ei tõesta kõigi teekonnast sõltuvate nõuete replitseeritavust.

### Python ja AI

Labor lahendab esmalt kahe instrumendi vähimruutude lähendi: $\Delta=0{,}5$, $b=-43{,}3333$. Jäägid `tegelik väljamakse − kate` on $(3{,}3333,-6{,}6667,3{,}3333)$. See on võrdsete kaaludega algebraline lähend, mitte ainus ega universaalselt parim riskimaandus. Seejärel lahendab `numpy.linalg.solve` kolmest instrumendist täpse süsteemi.

**[TÄIENDUS]** Praktikas saab optimeerida portfelli jääkriski koos kulude ja positsioonipiiridega. ML võib pakkuda stsenaariumide tõenäosusi; optimeerija valib positsioonid. Täpsusta, kas stsenaariumid on P- või Q-mõõdu all ja kas eesmärk on keskmine ruutviga, sabariski vähendamine või superreplikatsioon. AI ei saa luua puuduvat likviidset instrumenti.

**Oluline eristus:** trinoompuu võib olla ka täieliku pideva difusioonimudeli numbriline lähendus. Ühe diskreetse sammu mittetäielikkus ei tõesta, et lähendatav pidev mudel oleks mittetäielik. Numbrilise skeemi valitud üleminekutõenäosused võivad sisaldada lisamudeli eeldusi.

**Ülesanne.** Kas kolmanda instrumendina aitab teine aktsia, mille lõpphind on alati täpselt kaks korda esimese aktsia hind?  
**Vastus:** ei, selle väljamaksevektor ei lisa sõltumatut suunda; maatriksi astak ei suurene.

**Prompt:**

> Analüüsi turu täielikkust väljamaksemaatriksi astaku kaudu. Seisundid on S_T=80,100,120; instrumendid aktsia, raha ja valikuliselt K=100 put. Leia call'i täpne replikatsioon või jääkrisk. Erista kaalumata vähimruutude lahendus P-tõenäosustega kaalutud riskimaandusest ning arbitraaživabast hinnastamisest.

<a id="k6"></a>
## 6. Kas pidevas ajas saab hüppeid maandada?

**[PDF, lk 37]** Küsimuse vastus sõltub võimalike hüppesuuruste arvust ja instrumentide valikust. Pelgalt pideva kauplemise võimalus ei tee iga hüppelist turgu täielikuks.

### Intuitsioon

Delta sobib kohaliku puutuja tõusuks. Väike hinnamuutus on hästi kirjeldatav puutujaga; suur ootamatu hüpe võib viia kõvera puutujast kaugele. Tehing pärast hüpet ei kõrvalda juba toimunud hüppe kahju.

Kui aktsia hüppab $S$-lt $S+J$-ni, on optsiooni muutuse ja delta-katte vahe:

$$R(J)=V(S+J,t)-V(S,t)-\Delta J.$$

Väikese hüppe korral $R(J)\approx\tfrac12\Gamma J^2$, kuid suure hüppe puhul tuleb kasutada täpset ümberhindamist. Pika optsiooni ja lühikese delta-positsiooni jääk on ülaltoodud $R$; lühikese optsiooni ja pika delta-katte mõju on vastasmärgiline.

### Arvuline näide

**[NÄIDE]** Eelmise BS-call'i $S=100$, K=100, T=1, sigma=20% korral on hind 7,9656 ja delta 0,53983. Hetkelise hüppe 100 → 80 korral, hoides muud sisendid samana:

- uus call'i hind on umbes 1,1859;
- call'i väärtuse muutus on umbes −6,7796;
- delta-portfelli muutus on $0{,}53983\cdot(-20)=-10{,}7966$;
- call'i muutus miinus delta-kate on umbes +4,0169.

Müüdud call'i maandaja saab sellest hüppest umbes −4,0169 lisamõju võrreldes lineaarse kattega. See on hüppe stressitest BS-väärtusfunktsiooniga, mitte täielik hüppemudeli kalibreerimine. Reaalses sündmuses võib muutuda ka implitsiitne volatiilsus.

### Millal võib täpne maandus siiski õnnestuda?

- Ainult üks kindla suhtelise suurusega Poissoni hüpperisk, ilma sõltumatu Browni riskita: sobivalt mittetaandunud mudelis võib aktsia ja raha katta selle ühe riskiallika. Kogus leitakse hüppe väärtuste suhtest, mitte tingimata tuletisest $V_S$.
- Browni risk ja üks sõltumatu fikseeritud hüpperisk: üldjuhul on vaja kahte sõltumatult riskantset instrumenti ning raha, sobiva täisastakulise tundlikkusmaatriksiga.
- Mitu võimalikku hüppesuurust: iga suurus lisab täpse hüppekatte tingimuse. Pideva hüppesuuruste jaotuse korral ei piisa üldiselt lõplikust väikesest instrumendikomplektist suvalise nõude täpseks katmiseks.

Väide „hüppeid ei saa kunagi maandada” on seega liiga tugev. Samuti on väär „kauplen kiiremini, järelikult kaob hüpperisk”.

### Python, praktiline kasutus ja AI

Labor arvutab $R(-20)$ täpse ümberhindamise abil. Laienda katset hüpetega −30%, −10%, +10%, +30% ning volatiilsuse muutusega 20% → 40%. Kahe riski samaaegne stress on sisukam kui pelgalt delta vaatamine.

**[TÄIENDUS]** Uudiste NLP/LLM võib aidata tuvastada tulemuste avaldamise, regulatiivse otsuse või ülevõtmise sündmusi ja esitada stsenaariume. Ära tõlgenda teksti usaldusväärset kokkuvõtet kalibreeritud hüppetõenäosusena. Riskimaandamiseks võrdle aktsiat, sama alusvara optsioone ja positsioonipiiranguid. Deep hedging võib optimeerida jääkriski valitud simulaatoris; selle edukus ei tõesta turu täielikkust.

**Ülesanne.** Miks ei piisa teadaandest „turg võib homme 20% kukkuda”, et täna üks riskita delta valida?  
**Vastus:** valida tuleb kate kõigi asjakohaste seisundite ja riskiallikate jaoks. Üks lineaarne positsioon ei kata üldiselt mittelineaarse optsiooni väärtust korraga hüppe ja tavaliikumise korral.

**Prompt:**

> Koosta minu call-portfellile hüppestressid −30%, −20%, −10%, +10%, +20%. Arvuta täpne ümberhindamine, delta-lähend ja gamma-lähend ning nende vead. Erista pikk optsioon ja müüdud optsiooni delta-kate. Lisa eraldi volatiilsushüpe. Märgi, et BS-ümberhindamine on stressifunktsioon, mitte hüppemudeli tõestus.

<a id="k7"></a>
## 7. Miks ilmub riski turuhind intressi- ja volatiilsusmudelites? Miks mitte HJM-is?

**[PDF, lk 38–40]** Carri keskne tähelepanek: vahe tuleneb sellest, mille funktsioonina hinda kirjeldatakse. Lühiajaline intress või volatiilsus ei ole ise tavaline kaubeldav vara; võlakirja või teise optsiooni hind sisaldab juba turu hinnainfot. Forward-intressikõver on võlakirjahindadest tuletatav.

### Intuitsioon: prognoosist ei saa hinnastamist ilma riskitasu arvestamata

Kui mudel kirjeldab intressi ajaloolist käitumist, peab hinnastamiseks teadma, kuidas turul selle ebakindluse kandmist tasustatakse. Kui alustad juba võlakirjahindadest ja sobitad mudeli turuga riskineutraalses mõõdus, pole sama riskipreemiat vaja veel kord eraldi hinnastamisvõrrandisse kirjutada.

Olgu ühe faktori tegelik dünaamika:

$$dX_t=a_Pdt+b\,dW_t^{\mathbb P}.$$

Valime märgikokkuleppe $dW_t^{\mathbb Q}=dW_t^{\mathbb P}+\lambda_tdt$. Siis:

$$dX_t=(a_P-b\lambda_t)dt+b\,dW_t^{\mathbb Q},\qquad a_Q=a_P-b\lambda.$$

$\lambda$ on **riski turuhind** (*market price of risk*). Teistes allikates võib märgikokkulepe olla vastupidine; ära võrdle paljaid pluss- ja miinusmärke definitsiooni lugemata.

**[NÄIDE]** Kui $a_P=0{,}03$, $b=0{,}02$ ja $\lambda=0{,}5$, on $a_Q=0{,}02$. Need on faktori protsessi illustreerivad parameetrid; ühikud peavad vastama valitud faktori ja aasta definitsioonile.

Kaubeldava dividendideta aktsia lihtsas mudelis sunnib arbitraaživabadus $a_Q=rS$; seetõttu $\lambda=(\mu-r)/\sigma$. Mittekaubeldava lisafaktori puhul ei pruugi aktsia ja raha määrata kõiki riskipreemiaid.

### HJM-i vaatenurk

HJM ehk Heath–Jarrow–Morton modelleerib kogu hetkeliste forward-intresside kõverat $f(t,T)$. Nullkupongvõlakirja hind on:

$$P(t,T)=\exp\left(-\int_t^T f(t,u)du\right),\qquad f(t,T)=-\partial_T\log P(t,T).$$

Ühefaktorilises riskineutraalses HJM-is:

$$df(t,T)=\alpha_Q(t,T)dt+\sigma_f(t,T)dW_t^{\mathbb Q},$$

$$\alpha_Q(t,T)=\sigma_f(t,T)\int_t^T\sigma_f(t,u)du.$$

Riskineutraalne triiv pole vaba prognoosiparameeter: see peab olema kooskõlas volatiilsusega, et diskonteeritud võlakirjahinnad oleksid martingaalid. Mitme faktori puhul summeeritakse vastavad korrutised üle faktorite.

**Arvutus:** kui $\sigma_f=0{,}01$ on konstantne ja tähtajani on viis aastat, on $\alpha_Q=0{,}01\cdot(5\cdot0{,}01)=0{,}0005$ ehk 5 baaspunkti aastas forward-määra triivina. See ei ole lubadus, et tegelik intress tõuseb aastaga 5 baaspunkti.

**Miks lambda „kaob”?** Riskineutraalses esitusviisis kasutatakse juba Q-dünaamikat ning arbitraaživabaduse piirangut. P-mõõdus esitatud HJM võib sisaldada riskipreemiat. Riskieelistused pole maailmast kadunud; need on hinnainfos ja P ning Q seoses. Turukõver üksi ei määra kogu tulevast volatiilsusdünaamikat.

### Juhuslik volatiilsus

Kui aktsiat ja selle volatiilsust liigutavad kaks sõltumatut riskisuunda, ei kata üks aktsia üldiselt mõlemat. Teise kaubeldava optsiooni kasutamine võib sobivate tingimuste korral anda lisainstrumendi. Volatiilsusriski preemia kajastub turuhindades ja Q-parameetrites; ajaloolise volatiilsusmudeli parameetreid ei tohi automaatselt hinnastamismudelisse kopeerida.

### Python, AI ja rakendus

Laboris on riskipreemia teisendus ja HJM-i lihtne triiviarvutus. Edasine praktiline projekt on võlakirjade kõvera koostamine ning intressiriski stsenaariumid. Reaalses mootoris tuleb täpsustada päevaarvestus, kalendrid, diskonto- ja forward-kõverad ning tagatise tingimused; siinne ühe kõvera mudel on õppebaas.

**[TÄIENDUS]** PCA saab eraldada intressikõvera taseme, kalde ja kumeruse liikumisi. ML võib prognoosida P-mõõdu stsenaariume või kiirendada turuhindadega kalibreerimist. HJM-i Q-triivi piirang tuleb arvutada mudeli struktuurist, mitte lasta LLM-il vabalt ära arvata. QuantLib on võimalik järgmine tööriist pärast minimaalset laborit, mitte eeldus selle läbimiseks.

**Ülesanne.** Kui tõstad konstantse forward-volatiilsuse 1%-lt 2%-le, mitu korda muutub HJM-i drift samal tähtajal?  
**Vastus:** neli korda, sest seos on selles näites ruuteline: 0,0005 → 0,002.

**Prompt:**

> Selgita lambda rolli P- ja Q-mõõdu vahel ning HJM-i driftipiirangut. Kasuta kokkulepet dW_Q=dW_P+lambda*dt. Erista intressiprognoos, tänase võlakirjakõvera sobitamine ja optsioonihindade kalibreerimine. Näita üht arvulist näidet ja selgita, miks „HJM-is riskipreemiat pole” on ebatäpne väide.

<a id="k8"></a>
## 8. Kui palju kaotan, kui maandan vale volatiilsusega?

**[PDF, lk 41–45]** Carr eristab müügi implitsiitset volatiilsust, maandamisel kasutatud volatiilsust ja tegelikku juhuslikku volatiilsust. Lisaks teekonnal realiseeruvale P&L-ile käsitleb ta riskineutraalset oodatavat P&L-i. Need on erinevad küsimused.

### Kolm volatiilsust, kaks eri hinnangut

| Suurus | Roll |
|---|---|
| $\sigma_i$ | Volatiilsus, millele vastab optsiooni tegelik müügihind $C_{\rm sell}$ |
| $\sigma_h$ | Konstantne volatiilsus, millega arvutad maandamise delta ja gamma |
| $\sigma_t$ | Tegelik alusvara hetkeline volatiilsus pideva hinnatee mudelis |

Realiseerunud volatiilsus on ajaloolisest hinnateest hinnatud suurus. Pideva mudeli $\sigma_t$ on protsessi hetkeline parameeter. Need on seotud, kuid diskreetsest vaatlusest ei näe $\sigma_t$ täpselt.

### Teekonnapõhine P&L

**[SELGITUS]** PDF kasutab futuuri ja Blacki mudelit. Järgmine valem on sama põhimõtte dividendideta aktsia ja BS-maanduse variant: konstantne $r$, pidevad hinnateed, pidev isefinantseeriv kauplemine ja null tehingukulu.

Müü ühe ühiku call hinnaga $C_{\rm sell}$ ning halda selle katteportfelli deltaga $\Delta_h=\partial_S C_h$. Müüja lõpptulemus on:

$$\operatorname{P\&L}_T=(C_{\rm sell}-C_h(S_0,0))e^{rT}
+\frac12\int_0^T e^{r(T-t)}\Gamma_h(S_t,t)S_t^2(\sigma_h^2-\sigma_t^2)dt.$$

Esimene liige on algse müügihinna ja maandusmudeli hinna vahe koos intressiga. Teine on **gamma-kaalutud dispersioonierinevus**. Kui müüd ja maandad sama volatiilsusega, on esimene liige null.

**Tuletuse mõte:** kirjuta katteportfellile $dX=\Delta_h dS+r(X-\Delta_hS)dt$, optsioonifunktsioonile Itô valem tegeliku $\sigma_t$-ga ning lahuta. Kasutades $C_h$ PDE-d, saad veale $E=X-C_h$ võrrandi $dE=rE\,dt+\frac12\Gamma_hS^2(\sigma_h^2-\sigma_t^2)dt$. Diskonteerimine ja integreerimine annavad ülaltoodud tulemuse.

Vanilla call'i positiivse gamma korral ja $C_{\rm sell}=C_h$:

- kui $\sigma_t>\sigma_h$ kogu aja jooksul, on müüja teoreetiline P&L negatiivne;
- kui $\sigma_t<\sigma_h$ kogu aja jooksul, on see positiivne;
- kui vahe muudab märki, loeb gamma-kaalutud summa, mitte lihtsalt aastase keskmise volatiilsuse võrdlus.

Need märgijäreldused ei laiene automaatselt iga eksootilise väljamakse gamma-märgile ega hüpetele, kuludele ja diskreetsele kattele.

### Kiire hinnang ja selle piir

**[NÄIDE]** $S=100$, $\Gamma\approx0{,}019848$, $\sigma_h=20\%$ ja $\sigma_{\rm true}=30\%$ annavad alghetke aastase P&L-kiiruse:

$$\tfrac12\cdot0{,}019848\cdot100^2\cdot(0{,}20^2-0{,}30^2)\approx-4{,}962.$$

Ühe 1/252-aastase sammu hinnang on umbes −0,01969 ühiku kohta. **−4,962 ei ole täpne aastakahjum**, sest aktsiahind, gamma ja järelejäänud aeg muutuvad. Gamma on tähtaja lähenedes tugevalt koondunud täitmishinna ümbrusse.

### Carri peen vastus: riskineutraalne oodatav P&L ei sõltu maandusvolatiilsusest

Kui müügihind on fikseeritud, tehingukulud puuduvad ning diskonteeritud kauplemiskasu on Q all tõeline martingaal sobivate integreeritavuse tingimustega, siis:

$$E^{\mathbb Q}[e^{-rT}\operatorname{P\&L}_T]
=C_{\rm sell}-V_{\rm fair}.$$

Maandustehingutel on Q all null diskonteeritud oodatav kasu. Seetõttu muudab maandusstrateegia **tulemuste jaotust ja riski**, kuid mitte seda oodatavat väärtust. See ei ütle, et kahjumit pole või et kõik strateegiad on praktiliselt võrdselt head. Tegeliku P-mõõdu all võib strateegia oodatavat tulemust mõjutada; kulud muudavad tulemust samuti.

**Näide:** müügihind on 7,9656, kuid tegeliku 30% konstantse volatiilsusega Q-mudeli õiglane hind on 11,9235. Kui r=0, on Q-oodatav P&L $7{,}9656-11{,}9235=-3{,}9580$. Müügihinda samaks jättes ei paranda seda puudujääki pelgalt delta arvutamine teise volatiilsusega. Kui kasutad õiget 30% deltat, vähendad selles ideaalses mudelis maandamisriski; algset alahinnatud müüki see ei tühista.

### Python: tee väide nähtavaks

Labor simuleerib 5000 hinnateed ja 252 sammu, müük ja kate 20%, tegelik sigma 30%, $\mu=r=0$. See on **Q-katse**. Vaikeseemnega 42 saadi:

| Mõõdik | Tulemus ühe alusvaraühiku kohta |
|---|---:|
| Keskmine P&L | −3,9256 |
| Keskmise Monte Carlo standardviga | 0,02749 |
| Teoreetiline Q-keskmine | −3,9580 |
| P&L 5% / 50% / 95% kvantiil | −7,4503 / −3,7198 / −1,2097 |
| Gamma-integraali diskreetse lähendi keskmine | −3,9229 |

Keskmise erinevus teooriast on kooskõlas simulatsiooni juhusliku veaga. Diskreetne P&L ja integraali vasakpoolne lähend ei pea igal teel täpselt kattuma.

Eraldi katses on tegelik ja maandamise volatiilsus 20%. Lisame 0,1% kulu igale aktsiatehingu nominaalile, ka algsele ostule ja lõplikule müügile:

| Maandamissamme aastas | Kuludeta P&L standardhälve | Kuludega keskmine P&L |
|---:|---:|---:|
| 12 | 1,9539 | −0,2464 |
| 52 | 0,9576 | −0,3444 |
| 252 | 0,4421 | −0,6113 |

Selles katses sagedasem kate vähendab diskreetset katteviga, kuid suurendab kulusid. Erinevate sammude tabel kasutab eraldi simuleeritud teid; sama sammude arvu kuludega ja kuludeta võrdlus kasutab sama juhuslikku teed. Sageduste täpsemaks võrdlemiseks loo üks tihe hinnatee ja hõrenda seda.

### AI ja kaasaegne maandamine

**[TÄIENDUS]** Deep hedging kasutab õpitavat strateegiat, et valida maanduspositsioone valitud riskieesmärgi ja turupiirangute korral [A1]. Rakendusülesanne võiks olla: „vähenda 95% kahjumi sabariski, arvestades tehingukulusid ja positsioonilimiite”. Võrdluseks peab jääma BS-delta ja lihtne tehinguvaba vahemik. Treeni ja testi eri hinnateedel, lisa mudelist erinevaid stressistsenaariume ning raporteeri kulud. Õppekeskkonnas kasuta sünteetilisi andmeid; AI head tulemust ühes simulaatoris ei tohi nimetada garanteeritud päristuru eeliseks.

**Ülesanne.** Müüsid 30% volatiilsusega, kuid maandad 20%-ga ja tegelik sigma on 30%. Kas eelmise negatiivse integraali põhjal võib kohe väita, et Q-oodatav P&L on negatiivne?  
**Vastus:** ei. Müügihinna ja 20% mudelihinna positiivne algvahe kompenseerib Q-ootuses negatiivse integraali. Õiglase müügihinna ja nullkulude korral on Q-oodatav P&L null, kuigi üksikute teede tulemused erinevad.

**Prompt:**

> Simuleeri müüdud Euroopa call'i katmist. Hoia müügihind fikseerituna ja muuda ainult maandusvolatiilsust. Kasuta S=K=100, T=1, r=mu=0, tegelik sigma=0,30; võrdle hedge sigma 0,15, 0,20 ja 0,30. Raporteeri keskmine, standardviga, standardhälve, kvantiilid ja tehingukulud. Selgita, miks Q-oodatav P&L ja teekonnapõhine risk on eri mõisted. Seejärel korda katset mu=0,08-ga ning märgi see P-stsenaariumiks.

<a id="labor"></a>
## 9. Pythoni labor: lihtsast kontrollitava tulemuseni

### Käivitamine Thonnys

1. Ava `optsioonide_labor.py`.
2. Paigalda Thonny paketihalduriga `numpy`, kui see puudub.
3. Käivita kogu fail. Tulemused ilmuvad Shell-aknas.
4. Võrdle tulemusi failiga `labori_tulemused.txt`. Väga väikesed arvulised erinevused võivad sõltuda keskkonnast.
5. Muuda korraga üht eeldust. Kirjuta enne käivitamist üles, mida ootad.

Terminalis:

```bash
python -m pip install numpy
python optsioonide_labor.py
```

Google Colabis ava paketi `optsioonide_labor.ipynb` ja käivita lahtrid järjekorras. Labor ei vaja API-võtit, internetiandmeid, maaklerikontot ega LLM-teenust. Täielik kood on ka selle Markdown-faili lõpus, et õppematerjal ei sõltuks eraldi failidest.

### Labori kaart

| Katse | Funktsioon või osa | Mida kontrollida |
|---|---|---|
| 1–2 | `binomial()` | Hind langeb kokku kahe seisundi replikatsiooniga |
| 3 | `bs()` | Hind, delta, gamma; delta lõpliku vahe kontroll |
| 4 | Rahakonto näide | Ümberpaigutamine ei tekita raha |
| 5 | `lstsq` ja `solve` | Kahe instrumendi jääk, kolme instrumendi täpne kate |
| 6 | Hüppe ümberhindamine | Väärtuse mittelineaarne muutus versus delta |
| 7 | $a_Q$ ja HJM | Märgikokkulepe, ruuteline volatiilsusmõju |
| 8 | `hedge_simulation()` | Müügihind, Q/P, sagedus, kulud, gamma-integraal |

### Muuda katset teadlikult

```python
from optsioonide_labor import hedge_simulation

# Müügihind on 20% volatiilsuse järgi, kate 30%, tegelik sigma 30%.
pnl, integral, costs = hedge_simulation(
    real_sigma=0.30, hedge_sigma=0.30, sell_sigma=0.20,
    mu=0.0, r=0.0, cost_rate=0.0
)
print(pnl.mean(), pnl.std())
```

`integral` sisaldab ainult gamma-integraali, mitte müügihinna ja maandusmudeli hinna algvahet ega tehingukulusid. Kui `sell_sigma != hedge_sigma`, lisa teoreetiliseks võrdluseks algvahe koos intressiga. Monte Carlo standardviga on $s/\sqrt n$; ligikaudne 95% usaldusvahemik keskmisele on keskmine ±1,96 standardviga, mitte üksiktehingu riskivahemik.

**Piirid:** kood ei rakenda hüppeprotsessi, juhuslikku volatiilsust, Ameerika optsiooni varajast realiseerimist, hinnavahesid, tagatisnõudeid ega tegelikke turuandmeid. Q-simulatsiooniks sea `mu=r`; muu `mu` on kasutaja valitud tegeliku maailma stsenaarium. Hüppekatse on üks hetkeline ümberhindamine. BS-funktsioon eeldab positiivset S, K ja sigmat ning mittenegatiivset aega. Suurema labori korral lisa sisendkontrollid ka simulatsiooni sammude ja tehingukulude parameetritele.

### Arvutus- ja andmetestid enne keerukamat projekti

- Call peab dividendideta juhul rahuldama $\max(S-Ke^{-r\tau},0)\le C\le S$.
- Sama tähtaja call'i hind peab strike'i kasvades mitte suurenema ning olema strike'i suhtes kumer.
- Sama lepingu erinevad hinnastamisviisid peavad samadel eeldustel kooskõlas olema.
- Delta ja gamma valem tuleb võrrelda sõltumatu numbrilise lähendiga.
- Tehingu järel peab portfelli väärtus võrduma tehingueelse väärtusega miinus kulud.
- Suurem tehingute arv ei tohi olla automaatselt „parem”; võrrelda tuleb riski ja kogukulu.
- Ajatempel, valuuta, lepingukordaja ja optsiooni realiseerimisstiil peavad olema teada.

## 10. Ühendav praktiline projekt: optsiooniriski selgitaja

**[TÄIENDUS]** Sinu Pythoni, SQL-i ja testimise kogemusele sobiv projekt on väike süsteem, mis võtab lepingu tingimused, arvutab kontrollitavad hinnad ja riskid ning laseb AI-l tulemused eesti keeles lahti seletada.

| Etapp | Sisend ja väljund | Seos küsimustega |
|---|---|---|
| 1. Lepingu kirjeldus | JSON: S, K, T, r, sigma, call/put, Euroopa/Ameerika, kordaja | Eeldused kõigis kaheksas |
| 2. Hinnastamine | Binoommudel ja BS, ühikud ning kontrollid | 1–3 |
| 3. Rahavoogude logi | Delta-tehingud, raha, intress, kulud | 4 |
| 4. Stsenaariumimaatriks | Hindade liikumised, sõltumatud instrumendid, jääkrisk | 5–6 |
| 5. Mõõtude eristus | Eraldi prognoosi- ja hinnastamisparameetrid | 2, 3, 7 |
| 6. Katte simulatsioon | P&L, standardvead, kvantiilid ja kulud | 8 |
| 7. Selgitus | AI esitab Pythoniga arvutatud tulemused ja eeldused | Kõik |

Minimaalne tehnoloogiapakett: **Python + NumPy + SQLite + Markdown/JSON**. Graafikute jaoks võib lisada Matplotlibi; teenuseks muutmisel FastAPI. Suuremat raamistiku- või agendikihti pole alguses vaja. QuantLibi võib kasutada täiendava hinnastamismootorina ja sõltumatu võrdlusena [A2].

Näidisandmemudel SQLite'is:

```sql
CREATE TABLE runs (
  run_id TEXT PRIMARY KEY,
  model TEXT NOT NULL,
  probability_measure TEXT NOT NULL CHECK(probability_measure IN ('P','Q')),
  parameters_json TEXT NOT NULL,
  seed INTEGER,
  code_version TEXT NOT NULL
);
CREATE TABLE hedge_steps (
  run_id TEXT NOT NULL,
  path_id INTEGER NOT NULL,
  step INTEGER NOT NULL,
  spot REAL NOT NULL,
  delta REAL NOT NULL,
  cash REAL NOT NULL,
  fee REAL NOT NULL,
  portfolio_value REAL NOT NULL,
  PRIMARY KEY (run_id, path_id, step)
);
```

Salvesta raportisse mudeli eeldused koos tulemustega. Üks arv „õiglane hind 7,97” ilma sigma, tähtaja, määra ja optsioonistiilita on puudulik vastus.

<a id="ai"></a>
## 11. Kuidas kasutada AI-d nii, et vastused oleksid kontrollitavad?

### Rollide jaotus

| Ülesanne | Sobiv vahend | Milline kontroll jääb vajalikuks? |
|---|---|---|
| PDF-i mõistete otsing ja selgitamine | LLM koos allikakatketega; suurema kogu korral RAG | Allikaviide ja OCR-i valemite kontroll |
| Hind, delta, gamma, rahavood | Python või hinnastamisteek | Ühikud, eeldused, sõltumatu arvutuskontroll |
| Tegelike tootluste või volatiilsuse prognoos | Statistiline mudel või ML | Ajaliselt eraldatud test, lekke vältimine |
| Turu optsioonihindade sobitamine | Kalibreerimine ja optimeerimine | Arbitraažipiirid, likviidsus, hindade ajatemplid |
| Suur hinnastamismaht | Numbriline mootor; vajadusel õpitud asendusmudel | Hinna- ja tundlikkusvead eraldi |
| Tehingukuludega kate | Optimeerimine, vajadusel deep hedging | Võrdlus lihtsa baasstrateegiaga ja stressitest |
| Eesti keeles aruande koostamine | LLM arvutatud JSON-tulemuste peal | Ükski arv ei tohi muutuda või tekkida juurde |

Need on võimalikud töökorraldused, mitte väide, et kõik finantsettevõtted kasutaksid ühte kindlat tehnoloogiapakki. AI kasutegur tuleb mõõta: kas vähenes analüüsiaeg, viga, tehingukulu või valitud riskinäitaja?

### RAG selle PDF-i jaoks

Üks lühike PDF ei vaja tingimata vektorandmebaasi: lehekülgede või teemade järgi otsing võib olla piisav. Suurema materjalikogu korral:

1. Salvesta OCR-tekst koos leheküljenumbriga; säilita valemile viitav lehepilt.
2. Jaota sisu kaheksa küsimuse kaupa, säilitades valemi ja eeldused koos.
3. Otsi küsimusele vastavad katkendid, vajadusel semantilise otsinguga.
4. Lase LLM-il vastata ainult leitud sisu ning selgelt märgistatud lisaselgituste põhjal.
5. Saada arvutused Pythoni funktsioonile; tagasta tulemus struktureeritud JSON-ina.
6. Koosta vastus: lühivastus → eeldused → arvutus → tõlgendus → allikas → piirid.

**Oluline:** PDF-ist leitud „riskineutraalne oodatav P&L ei sõltu kattest” ei tohi vastuses lüheneda väiteks „maandamisel pole tähtsust”. Allikast tuuakse kaasa ka tingimused.

### Üldprompt kõigi lisaküsimuste jaoks

```text
Tegutse optsiooniteooria õpetaja ja Pythoni arvutuste kontrollijana.
Küsimus: [küsimus]
Minu andmed ja eesmärk: [andmed; kas soovin hinnastada, prognoosida või maandada]

Vasta eesti keeles järgmises järjekorras:
1. 2–4-lauseline lihtne vastus.
2. Täpsed eeldused: leping, mõõt P/Q, kulud, kauplemissagedus, riskiallikad.
3. Intuitiivne põhjendus ja üks praktiline olukord.
4. Valem koos tähiste ning ühikutega.
5. Väike arvuline näide, mis on Pythoniga kontrollitav.
6. Käivitatav kood ja oodatav tulemus. Kui koodi ei käivitanud, ütle seda.
7. Üks vastunäide või juhtum, kus väide enam ei kehti.
8. Kaks kontrollküsimust koos vastustega.
Erista [PDF], [SELGITUS], [NÄIDE] ja [TÄIENDUS].
Ära leiuta leheküljenumbreid, turuandmeid ega käivitustulemusi.
Kui andmeid pole, kasuta selgelt märgitud sünteetilist näidet.
```

### Prompt: keerulise väite kontrollimine

```text
Hinda väidet: [nt „AI ennustab aktsiat paremini, järelikult annab õigema optsioonihinna”].
Erista prognoosimine P all, hinnastamine Q all ja riskimaandamine.
Too üks olukord, kus väites on mõistlik tuum, ning üks arvuline vastunäide.
Lõpeta parandatud väitega, mida saab foorumis täpselt ja lühidalt öelda.
```

### Prompt: allikapõhine vastus

```text
Vasta ainult lisatud allikakatkete põhjal. Too iga põhiväite juurde füüsiline
PDF-lehekülg, kui see on metaandmetes olemas. Kui vastus vajab lisateavet,
märgi „allikast ei selgu”. Kontrolli OCR-i valemeid lehepildilt või küsi
puuduv valem. Ära esita oma AI-rakenduse ettepanekut Peter Carri väitena.
Küsimus: [...]
Allikakatked: [...]
```

### Prompt: ML-projekti aus hindamine

```text
Soovin ennustada järgmise 20 kauplemispäeva realiseerunud volatiilsust.
Paku minimaalne Python-lahendus ja lihtne ajaloolise volatiilsuse baasprognoos.
Kasuta ajaliselt järjestatud treeningut/testi ning väldi kattuvate sihtperioodide
kaudu andmeleket. Erista prognoosiviga, optsiooni hinnastamisviga ja katte P&L.
Selgita, millist lisainfot oleks vaja, et võrrelda prognoosi implitsiitse
volatiilsusega. Ära järelda prognoositäpsusest automaatselt kauplemiskasumit.
```

### Prompt: agent ainult mõõdetava kasuga

```text
Kavanda lugemisõigusega optsiooniriski analüüsiabiline, mis kasutab minu
kontrollitud hinnastamisfunktsioone. Sisend on JSON, väljund Markdown-raport.
Abiline ei saada tehingukorraldusi. Ta kontrollib puuduvad väljad, arvutab hinna
ja stressid ning selgitab tulemusi. Võrdle agendilahendust tavalise Pythoni
skriptiga: latentsus, hind, vead, korratavus ja kasulik paindlikkus.
Kas agent annab siin mõõdetavat lisaväärtust? Põhjenda.
```

### Prompt: suulise vastamise treener

```text
Küsi minult järjest PDF-i kaheksa küsimust, üks korraga.
Lase mul vastata 60–90 sekundiga. Hinda vastust neljal teljel:
intuitsioon, matemaatiline täpsus, eeldused ja praktiline rakendus (igaüks 0–2).
Seejärel küsi üks eksitavat üldistust paljastav lisaküsimus.
Anna parandatud lühivastus alles pärast minu katset.
```

<a id="ope"></a>
## 12. Õppeplaan ja õpetamisvalmidus

### Umbes 12-tunnine õpitee

| Õppesessioon | Aeg | Töö ja valmisoleku tunnus |
|---|---:|---|
| 1. Väljamakse, replikatsioon, P ja Q | 2 h | Lahendad 1/3 hinnaga näite ilma abita |
| 2. Binoompuu ja BS | 2 h | Selgitad, miks p ja mu kaovad, aga sigma jääb |
| 3. Isefinantseerimine | 1,5 h | Leiad vigase backtest'i puuduva rahavoo |
| 4. Mittetäielikkus ja hüpped | 2 h | Näitad maatriksiga, milline risk jääb katmata |
| 5. Riski turuhind ja HJM | 1,5 h | Eristad P-prognoosi ja Q-dünaamikat |
| 6. Vale volatiilsus ja kulud | 2 h | Selgitad nii P&L-integraali kui Q-ootuse sõltumatust |
| 7. Suuline test | 1 h | Vastad kõigile kaheksale 60–90 sekundiga |

### 90 minuti näidistund

- **0–10 min:** lase õppijatel pakkuda hinda 1 → 2/0,5 call'ile; kirjuta eraldi 0,50 ja 1/3 põhjendused.
- **10–25 min:** ehitage koos replikatsiooni rahavoogude tabel.
- **25–40 min:** muutke tegelikku p-d ja intressi; arutage, kumb muudab mudelihinda.
- **40–55 min:** näidake isefinantseerimist ning muutke rahakonto koodis teadlikult valeks.
- **55–70 min:** lisage kolmas seisund; seejärel put kui kolmas instrument.
- **70–82 min:** näidake katte P&L-jaotust erineva sageduse ja kuludega.
- **82–90 min:** iga õppija sõnastab ühe tõese väite koos selle piiranguga.

HJM ja hüppemudelite sügavam käsitlus jäävad järgmise tunni või iseseisva töö teemaks. Kõigi kaheksa täielik õpetamine ühe 90-minutilise tunniga ei anna tavaliselt piisavalt harjutusaega.

### Lõputest koos vastustega

1. **Miks $E^{\mathbb P}[H]$ ja $E^{\mathbb Q}[H]$ erinevad?**  
   P kirjeldab tegelikke tõenäosusi, Q hinnastab riski turuhindade ja arbitraaživabadusega kooskõlaliselt. Mõlemad kasutavad sama väljamaksefunktsiooni, kuid eri kaale.
2. **Kas parem P-prognoos võib aidata optsioonidega otsuseid teha?**  
   Jah, prognoositava riski ja tootluse hindamisel, kuid seda tuleb võrrelda turuhinna, kulude ja prognoosi ebakindlusega.
3. **Kas binoommudeli p puudumine tähendab, et tulevikuseisundid ei loe?**  
   Ei. Nende hinnatasemed ja väljamaksed määravad replikatsiooni.
4. **Mis juhtub, kui binoompuus $R>u$?**  
   Isegi parim aktsiatulemus jääb rahakontole alla. Shortimise võimaluse korral tekib mudelis arbitraaž; q ei ole sobiv tõenäosus.
5. **Miks gamma-liige Itô valemis ei kao?**  
   Browni hinnamuutuse ruut on ajasammu suurusjärgus: $(dW)^2=dt$ Itô arvutuse tähenduses.
6. **Kas delta=0,54 tähendab 54% tegelikku tõusutõenäosust?**  
   Ei. Delta on hinnatundlikkus. BS-i dividendideta call'i korral on delta $\Phi(d_1)$, Q-tõenäosus lõpus rahas olla on $\Phi(d_2)$.
7. **Miks ei tohi $d(\Delta S)$ asendada lihtsalt $\Delta dS$-ga?**  
   Kaal muutub; korrutise reeglis on lisaliikmed. Isefinantseerimise rahakonto tasakaalustab nende mõju.
8. **Kas optsiooni kate võib vajada laenu?**  
   Jah. Negatiivne rahakonto on osa replikatsioonist. Tegelik laenuhind võib erineda mudeli riskivabast määrast.
9. **Kas iga trinoomnõue on kahe instrumendiga katmatu?**  
   Ei. Lineaarsed või muul viisil nende kahe instrumendi väljamaksete hulka kuuluvad nõuded on kaetavad.
10. **Kas kolm instrumenti tagavad täielikkuse?**  
    Ainult siis, kui nende väljamaksevektorid on vajalikes seisundites sõltumatud ja mitme perioodi korral vajalik info ning kauplemisvõimalus säilivad.
11. **Kas sagedasem delta-uuendus kõrvaldab ootamatu hinnahüppe jäägi?**  
    Üldiselt ei; pärast hüpet tehtud tehing ei muuda toimunud väärtushüpet.
12. **Kas HJM sobib otse intresside P-prognoosiks?**  
    Q-kujul hinnastamismudel mitte ilma P-dünaamika ja riskipreemia täpsustuseta.
13. **Kas ajalooline ja implitsiitne volatiilsus mõõdavad täpselt sama?**  
    Ei. Esimene on hinnateest saadud hinnang; teine turuhinna mudeliparameeter, mis sisaldab ka riskihinnastamist ja mudeli mõju.
14. **Kas vale sigma tähendab tingimata negatiivset Q-oodatavat katte P&L-i?**  
    Ei. Fikseeritud müügihinna ja nullkulude korral määrab Q-ootuse müügihinna ja õiglase hinna vahe; kate muudab riski.
15. **Miks ei saa pelgalt keskmise P&L-i järgi valida parimat katet?**  
    Vaja on hinnata ka hajuvust, sabariski, kulusid, finantseerimist ja mudeliviga.
16. **Mida peab AI-raport ütlema lisaks hinnale?**  
    Lepingu tingimused, mudel, P/Q eristus, sisendid ja ühikud, arvutusmeetod, allikad, piirid ning kontrollide tulemus.

**Enesehindamine:** anna iga vastuse eest 0–2 punkti: 0 = sisuline eksimus, 1 = õige idee ilma põhjenduseta, 2 = õige idee koos põhjenduse või vastunäitega. 26/32 on mõistlik õppimise sihttase, kuid punktisumma ei asenda praktilist koodi- ja rahavoogude kontrolli ega ole kutsekvalifikatsioon.

### PDF-i kolm lisaküsimust: edasijõudnu suunad

PDF-i viimane lehekülg esitab veel kolm avatud mõtteküsimust. Need pole põhikaheksa osa, kuid sobivad jätkuks:

1. **Lõpmatu ajahorisont ja riskineutraalne hinnastamine.** „Ootan, kuni short kasumisse jõuab” ei tõesta lubatavat arbitraaži. Vaadata tuleb vahepealseid piiramatuid kahjumeid, strateegia lubatavust, peatumisaega ning integraalide/ootuste koonduvust. Prompt: „Selgita optional stopping'u eeldusi ja miks neid ei saa lõpmatu ooteajaga automaatselt kasutada.”
2. **Oodatava tootluse roll mittetäielikul turul.** Üksainus replikatsioonihind ei pruugi olla määratud; P-jaotus võib mõjutada riskipõhist või kasulikkuspõhist strateegiavalikut. Prompt: „Võrdle sama trinoomnõude arbitraaživaba hinnavahemikku ja P-kaaludega minimaalse ruutvea katet.”
3. **Piiratud kapital ja krediidirisk.** Mudeli piiramatu laenamine ühise määraga on tugev eeldus. Finantseerimiskulu ei lahendata lihtsalt kõigi valemite r-i asendamisega oma laenumääraga. Prompt: „Näita lihtsa rahavoogude näitega, kuidas eri laenu- ja hoiusemäär ning tagatis mõjutavad replikatsiooni ja hinnavahemikku.”

## 13. Meelespea selgeks vastamiseks

- Kõigepealt küsi: **kas hinnastan, prognoosin või maandan?**
- Sama väljamakse peab samadel tingimustel maksma sama palju.
- Q on hinnastamise mõõt; P on tegeliku maailma mõõt.
- Riskineutraalsus ei ole investorite iseloomuomadus.
- Delta katab kohaliku hinnariski; see ei kata automaatselt kõiki riske.
- Positsiooni muutmine peab kajastuma rahakontol.
- Riskisuundade arv ja instrumentide sõltumatus määravad katte võimalused.
- Kalibreerimine turuhindadega ei tõesta head tulevikuprognoosi.
- Q-oodatav kasum ja tegeliku tehingu risk on eri asjad.
- AI seletab ja aitab otsida; arvutus, eeldused ning kontrollid peavad olema nähtavad.

## 14. Allikad ja päritolu

**Põhiallikas:** kasutaja lisatud Peter Carr, *FAQ’s in Option Pricing Theory*, esialgne versioon 7. juuni 1999, 45-leheküljeline esitlus, failiviide `faqpres.tex`. Küsimuste nimekiri PDF lk 2; teemad vastavalt lk 3–7, 8–12, 13–19, 20–22, 23–36, 37, 38–40, 41–44; jätkuküsimused lk 45. Õppematerjal ei ole esitluse tõlge ega pikk tekstikoopia, vaid iseseisev selgitus ja arvutuslabor.

**Täiendavad allikad**, kontrollitud 29.10.2026:

- **[A1]** Hans Bühler, Lukas Gonon, Josef Teichmann, Ben Wood, *Deep Hedging* (2018 preprint; 2019 artikkel). [Autorite uurimus arXivis](https://arxiv.org/abs/1802.03042). Kasutatud piiratud ulatuses kaasaegse tehingukulude ja piirangutega õpitava riskimaandamise võimaluse selgitamiseks. Siinne labor ise ei treeni närvivõrku.
- **[A2]** [QuantLibi Black–Scholesi protsesside lähtekood](https://github.com/lballabio/QuantLib/blob/master/ql/processes/blackscholesprocess.hpp). Näide avatud lähtekoodiga hinnastamistehnoloogiast ja dividendi-/intressikõveraid kasutavatest protsessidest. Labor ei vaja QuantLibi.
- **[A3]** Peter Carr, [sama teemaga pikem artikkel, `faq2.tex`](https://citeseerx.ist.psu.edu/document?doi=4bc94be583ad44417ddf4fe5923ee8192b9e60c2&repid=rep1&type=pdf). Edasise lugemise viide; see on eraldi versioon ning selle lehekülgi ei tohi segamini ajada lisatud esitluse omadega. Siinse juhendi leheviited käivad kasutaja PDF-i kohta.

AI/RAG-i arhitektuur, SQL-skeem, õppeplaan, promptid ja enamik arvulisi näiteid on selle juhendi **[TÄIENDUS]** või **[NÄIDE]**. Need ei ole väited Carri 1999. aasta tehnoloogiakasutuse kohta.

## Lisa A. Täielik käivitatav Pythoni kood

Kopeeri järgmine plokk faili `optsioonide_labor.py`. Vajalik väline pakett on ainult NumPy.

```python
"""Kaheksa optsiooniküsimuse arvutuslabor. Python 3 + numpy. Käivita kogu fail."""
from math import exp, log, sqrt, erf, pi
import numpy as np

def normal_cdf(x):
    a = np.asarray(x)
    return np.vectorize(lambda z: 0.5*(1+erf(float(z)/sqrt(2))), otypes=[float])(a)

def bs(S, K=100., T=1., r=0., sigma=.2):
    """Euroopa call, dividendideta. Tagastab hinna, delta ja gamma."""
    S = np.asarray(S, dtype=float)
    if np.any(S <= 0) or K <= 0 or T < 0 or sigma <= 0:
        raise ValueError('S,K,sigma > 0; T >= 0')
    if T == 0:
        return np.maximum(S-K, 0), np.where(S>K,1.,np.where(S<K,0.,.5)), np.zeros_like(S)
    d1=(np.log(S/K)+(r+.5*sigma*sigma)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return (S*normal_cdf(d1)-K*exp(-r*T)*normal_cdf(d2),
            normal_cdf(d1), np.exp(-.5*d1*d1)/(sqrt(2*pi)*S*sigma*sqrt(T)))

def binomial(S=1., up=2., down=.5, K=1., R=1.):
    if not down < R < up:
        raise ValueError('Arbitraaživabaduseks peab down < R < up')
    Su,Sd=S*up,S*down
    Cu,Cd=max(Su-K,0),max(Sd-K,0)
    delta=(Cu-Cd)/(Su-Sd)
    cash=(Cd-delta*Sd)/R
    q=(R-down)/(up-down)
    return delta*S+cash,delta,cash,q

def hedge_simulation(real_sigma=.3, hedge_sigma=.2, n=5000, steps=252,
                     mu=0., r=0., cost_rate=0., seed=42, sell_sigma=None):
    """Müüdud call: raha + aktsiad - lõppväljamakse. Delta hedge_sigma järgi, hind sell_sigma järgi (vaikimisi hedge_sigma).
    Kulu: cost_rate * tehingu nominaal; arvestab algostu ja lõppmüüki.
    Sama seeme võimaldab sama sammude arvu korral ausat strateegiavõrdlust.
    """
    rng=np.random.default_rng(seed)
    dt=1/steps
    S=np.full(n,100.)
    _,delta,gamma=bs(S,r=r,sigma=hedge_sigma)
    premium=bs(S,r=r,sigma=hedge_sigma if sell_sigma is None else sell_sigma)[0]
    cash=premium-delta*S-cost_rate*np.abs(delta)*S
    integral=np.zeros(n)
    costs=cost_rate*np.abs(delta)*S
    for i in range(steps):
        # Diskonteeritud gamma-integrandi vasakpoolne Riemanni summa.
        integral += exp(-r*i*dt)*.5*gamma*S*S*(hedge_sigma**2-real_sigma**2)*dt
        S *= np.exp((mu-.5*real_sigma**2)*dt+real_sigma*sqrt(dt)*rng.standard_normal(n))
        cash *= exp(r*dt)
        if i < steps-1:
            _,new_delta,gamma=bs(S,T=1-(i+1)*dt,r=r,sigma=hedge_sigma)
            fee=cost_rate*np.abs(new_delta-delta)*S
            cash -= (new_delta-delta)*S+fee
            costs += fee
            delta=new_delta
    fee=cost_rate*np.abs(delta)*S
    cash += delta*S-fee
    costs += fee
    pnl=cash-np.maximum(S-100,0)
    return pnl, integral*exp(r), costs

def main():
    c,d,b,q=binomial()
    assert np.isclose(c,1/3) and np.isclose(d,2/3)
    print('1–2: hind, delta, raha, q:', c,d,b,q)
    for p in [.2,.5,.8]:
        print('p=',p,'P-keskmine=',p,'replikatsioonihind=',c)
    c20,delta,gamma=bs(100)
    c30=bs(100,sigma=.3)[0]
    print('3: BS sigma20/sigma30, delta, gamma:',c20,c30,delta,gamma)
    h=.001
    fd=(bs(100+h)[0]-bs(100-h)[0])/(2*h)
    assert abs(fd-delta)<1e-7
    # 4: ümberpaigutamine ei muuda hetkeportfelli väärtust.
    old_cash=10.; old_delta=.5; new_delta=.6; spot=102.
    new_cash=old_cash-(new_delta-old_delta)*spot
    assert np.isclose(old_cash+old_delta*spot,new_cash+new_delta*spot)
    print('4: uus rahakonto:',new_cash)
    # 5: 3 seisundit, 2 instrumenti; lisame sõltumatu put-väljamakse.
    A=np.array([[80.,1.],[100.,1.],[120.,1.]])
    payoff=np.array([0.,0.,20.])
    beta=np.linalg.lstsq(A,payoff,rcond=None)[0]
    print('5: aktsia+raha kaalud ja jäägid:',beta,payoff-A@beta)
    A3=np.column_stack((A,[20.,0.,0.]))
    weights=np.linalg.solve(A3,payoff)
    assert np.allclose(A3@weights,payoff)
    print('5: aktsia+raha+put kaalud:',weights)
    # 6: delta ei kata hüppest tingitud mittelineaarset muutust.
    jump_residual=bs(80)[0]-c20-delta*(80-100)
    print('6: 100 -> 80 hüppe optsioonimiinus-delta jääk:',jump_residual)
    # 7: lambda märk sõltub Browni liikumise teisenduse kokkuleppest.
    aP,bfactor,lam=.03,.02,.5
    print('7: aQ=aP-b*lambda:',aP-bfactor*lam)
    sigf=.01; tau=5
    print('7: HJM forwardi drift:',sigf**2*tau)
    # 8: võrdleme tehingukuludeta väärvolatiilsuse katet.
    pnl,integ,_=hedge_simulation()
    expected=float(c20-c30)
    print('8: keskmine P&L, standardviga, teooria:',pnl.mean(),pnl.std(ddof=1)/sqrt(len(pnl)),expected)
    print('8: P&L 5/50/95 protsentiil:',np.quantile(pnl,[.05,.5,.95]))
    print('8: gamma-integrali keskmine:',integ.mean())
    assert abs(pnl.mean()-expected)<5*pnl.std(ddof=1)/sqrt(len(pnl))+.05
    for steps in [12,52,252]:
        plain,_,_=hedge_simulation(real_sigma=.2,steps=steps)
        costly,_,fees=hedge_simulation(real_sigma=.2,steps=steps,cost_rate=.001)
        print('sammud / tasuta std / kuludega keskmine / keskmine kulu:',steps,plain.std(),costly.mean(),fees.mean())
    print('Fikseeritud müügihind sigma=20%, tegelik sigma=30%:')
    for hs in [.15,.2,.3]:
        result,_,_=hedge_simulation(hedge_sigma=hs,sell_sigma=.2)
        print('hedge sigma / Q-keskmine / std:',hs,result.mean(),result.std())
    print('Kõik arvulised kontrollid läbitud.')

if __name__=='__main__':
    main()

```
