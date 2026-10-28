# Finantsmatemaatika: valem kui kontrollitav mudel

[Tagasi avalehele](../README.md) · [50 lahendatud ülesannet](../17-50-ulesannet/README.md) · [24 skripti](../10-python-ja-andmed/24-naidet.md)

## Sisukord

- [Rahavoogude hindamine](#rahavoogude-hindamine)
- [Võlakirja hinnatundlikkus](#võlakirja-hinnatundlikkus)
- [Ootus ja portfelli dispersioon](#ootus-ja-portfelli-dispersioon)
- [Regressioon ja CAPM](#regressioon-ja-capm)
- [Mõõtmise ebakindlus](#mõõtmise-ebakindlus)
- [Bayes ja Kelly](#bayes-ja-kelly)
- [Õppekorraldus](#õppekorraldus)

**Õpieesmärk:** oskad nimetada iga valemi muutujad, ühikud ja eeldused ning kontrollida tulemust lihtsa piirjuhuga. See on esimene matemaatika alusmoodul; optsioonide täielik hinnastamine, risk of ruin'i süvakäsitlus ja robustse optimeerimise rakendus on veel koostamata.

## Rahavoogude hindamine

[MUDEL] Kui rahavoog $CF_t$ saabub perioodi $t$ lõpus ja perioodi diskontomäär on $y$, siis

$$PV=\sum_{t=1}^{n}\frac{CF_t}{(1+y)^t}.$$

$PV$ on tänane väärtus, $n$ perioodide arv. Valem on diskonteerimisreegel; selle majanduslik sobivus sõltub rahavoo ning määra kooskõlast. Kindel makse ja riskantne oodatav rahavoog vajavad eri käsitlust. Kui eri tähtaegadel on eri intressimäärad, tuleb kasutada tähtajale vastavat diskontotegurit.

[NÄIDE] Kolmeaastane võlakiri maksab 50, 50 ja 1050. 6% juures on hind 973.2699. Kupong üksi ei ole tootlus: ostuhind määrab, millise tootluse maksed annavad. **Piirjuht:** kui kupongimäär võrdub tootlusnõudega ja maksed on samas sageduses, on lihtsa võlakirja hind nimiväärtus.

**Python:** [näide 6](../python/lyhinaited/06_volakiri.py). **Ülesanne:** [11](../17-50-ulesannet/02-ulesanded.md#u11).

## Võlakirja hinnatundlikkus

Macaulay duration on rahavoogude aegade nüüdisväärtustega kaalutud keskmine:

$$D_M=\frac{\sum_{t=1}^{n}t\,CF_t/(1+y)^t}{P}.$$

Aastase kupongi ning aastase diskontomäära korral $D_{\mathrm{mod}}=D_M/(1+y)$. Väikese määramuutuse $\Delta y$ korral:

$$\frac{\Delta P}{P}\approx-D_{\mathrm{mod}}\Delta y.$$

Eelmise näite $D_M\approx2.8573$ ja $D_{\mathrm{mod}}\approx2.6956$. Ühe protsendipunkti tõus annab esimese järgu lähendi umbes −2.6956%. See pole täpne hinnamuutus; täpne hind tuleb uuesti diskonteerides.

Teise järgu parandus kasutab convexity't:

$$C=\frac{1}{P}\sum_{t=1}^{n}\frac{t(t+1)CF_t}{(1+y)^{t+2}},\qquad
\frac{\Delta P}{P}\approx-D_{\mathrm{mod}}\Delta y+\frac12 C(\Delta y)^2.$$

Kõik sümbolid järgivad sama aastast diskontokonventsiooni. Suurte muutuste korral on ka teise järgu lähend ebatäpne. Sissenõutava või muu optsiooniga võlakirja rahavoog võib määra muutudes ise muutuda.

**Python:** [näide 7](../python/lyhinaited/07_duration.py). **Ülesanded:** 14–16.

## Ootus ja portfelli dispersioon

Kui tulemus $r_j$ toimub tõenäosusega $p_j$, siis $E[R]=\sum_jp_jr_j$, kus $p_j\ge0$ ning $\sum_jp_j=1$. Kahe varaga ühe perioodi lihttootluse portfellis on $R_p=w_1R_1+w_2R_2$. Seetõttu

$$E[R_p]=w_1E[R_1]+w_2E[R_2].$$

Kaalud on perioodi alguse kapitaliosad. Kui rahavooge pole ja rebalanseerimist perioodi sees ei toimu, on see täpne lihttootluse seos. Portfelli dispersioon on

$$\operatorname{Var}(R_p)=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\operatorname{Cov}(R_1,R_2).$$

Kovariatsiooni kirjutame $\rho\sigma_1\sigma_2$, kus $\rho$ on korrelatsioon. Dispersioon on ruutühikutes, standardhälve selle ruutjuur. Näiteks 50/50 portfell kahe 20% standardhälbega ja nullkorrelatsiooniga vara vahel annab $\sqrt{0.02}\approx14.1421\%$.

Eristame **jaotuse dispersiooni** $E[(R-\mu)^2]$ ja **valimi dispersiooni hinnangut** $\sum(R_t-\bar R)^2/(n-1)$. Kahe definitsiooni segamine muudab väikese valimi arvutust märgatavalt.

**Python:** näited 8–10. **Süvalabor:** [hajutamine](../laborid/02-hajutamine.md). Markowitzi mudel optimeerib kaalude kaudu ootust ja dispersiooni antud eeldustel. Matemaatiline optimum on sisendite optimum, mitte garantii tulevase turu kohta.

## Regressioon ja CAPM

Ületootluste regressioonis on

$$R_{i,t}-R_{f,t}=\alpha+\beta(R_{m,t}-R_{f,t})+\varepsilon_t.$$

$R_i$ on vara tootlus, $R_f$ sama perioodi riskivaba tootlus, $R_m$ turuvõrdluse tootlus, $\alpha$ vabaliige, $\beta$ turu suhtes tundlikkus ja $\varepsilon$ jääk. Ühe seletava muutujaga OLS-is:

$$\hat\beta=\frac{\sum(x_t-\bar x)(y_t-\bar y)}{\sum(x_t-\bar x)^2},\qquad
\hat\alpha=\bar y-\hat\beta\bar x.$$

[NÄIDE] Ületootlused $x=(-2,0,2,4)\%$ ja $y=(-2,1,4,7)\%$ annavad $\beta=1.5$ ning perioodialfa 1%. Tegemist on meelega täpselt sirgele asetatud arvudega. See ei tõenda päris fondijuhi oskust.

CAPM-i tasakaalumudel annab teoreetilise seose $E[R_i]=R_f+\beta_i(E[R_m]-R_f)$. Näiteks 3% riskivaba määra, 8% turuootuse ja beeta 1.2 korral on mudeli ootus 9%. Mudel eeldab tugevalt lihtsustatud turgu ja investorikäitumist. Regressioonialfa ning CAPM-i majanduslik tõlgendus ei ole automaatselt sama asi.

**Python:** [näide 19](../python/lyhinaited/19_beeta.py). **Ülesanded:** 37–38.

## Mõõtmise ebakindlus

Sõltumatute sama jaotusega vaatluste korral on keskmise standardviga ligikaudu $s/\sqrt n$, kus $s$ on valimi standardhälve ja $n$ vaatluste arv. 100 vaatlust ning 10% standardhälve annavad keskmise standardveaks 1 protsendipunkti. Kui keskmine on 2%, on normaal-lähendi 95% vahemik umbes 0.04% kuni 3.96%.

See on meetodi korduva kasutamise katvusega seotud usaldusvahemik, mitte üksiku tulevase tootluse vahemik. Väikese valimi, sõltuvate vaatluste, paksude sabade või mudeli valimise järel tuleb meetodit kohandada. Ajaridade juhuslik segamine võib rikkuda ajalist testimist.

**Hüpoteesitest** küsib, kui kooskõlalised on andmed nullmudeliga. P-väärtus ei ole tõenäosus, et nullhüpotees on tõene. Mõju suurus, majanduslik väärtus ja eelnevalt proovitud katsete arv tuleb eraldi esitada.

## Bayes ja Kelly

Bayesi valem eristab $P(A\mid B)$ ja $P(B\mid A)$:

$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

[NÄIDE] Kui 10% mudelitest on head, test läbib 80% headest ja 20% halbadest, siis positiivse testi järel on headuse tõenäosus $0.08/(0.08+0.18)\approx30.77\%$. Positiivne signaal ei kõrvalda ebatõenäolist lähteolukorda.

Kelly binaarses kordusmudelis panustatakse kapitaliosa $f$, võit annab panuse kohta kasumit $b$ tõenäosusega $p$, kaotus võtab panuse tõenäosusega $q=1-p$. Oodatav logkasv on

$$G(f)=p\ln(1+bf)+q\ln(1-f).$$

Tuletise null annab sisemise optimumi $f^*=(bp-q)/b$, tingimusel et lubatud panused ja mudeli eeldused seda võimaldavad. Kui lubatud on ainult $0\le f<1$ ja valem annab negatiivse arvu, pole selle mängu positiivne panus optimaalne. p=0.55, b=1 korral on f*=0.10. Hinnanguline p võib olla vale ning logkasv ei esinda kõiki investori vajadusi.

**Python:** näited 21–22. **Ülesanded:** 32 ja 47.

## Õppekorraldus

**5 minutit:** vali üks valem ja ütle iga sümboli ühik. **30 minutit:** lahenda vastav käsitsi näide ja käivita skript. **90 minutit:** tuleta valem, kontrolli piirjuhte ja muuda üht eeldust.

Viis põhimõtet: ühikud enne arvutust; definitsioon enne võrdlust; eeldused enne tõlgendust; piirjuht enne keerukust; ebakindlus enne otsust.

**90 minuti tunnikava:** 15 min rahavoogude idee; 20 min tuletus; 20 min käsitsi ja Pythonis arvutus; 15 min piirjuhud; 10 min eksliku analüüsi parandamine; 10 min kokkuvõtte asemel õppija enda selgitus. Soovitus on valida üheks tunniks üks alateema, mitte proovida kogu moodulit kiirustades läbida.
