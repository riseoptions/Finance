# Päev 4: portfelli matemaatika

[NARANG: ptk 4–7; JANSEN: ptk 17–19]

Portfelli ühe perioodi tootlus $r_p=\sum w_i r_i$ eeldab perioodi alguskaale. Kui portfelli kaalud muutuvad, tuleb tootlusi ühendada periooditi. Raha kaal on $1-\sum w_i$; meie demokontol selle tootlus on null.

Oodatav tootlus $\mu_p=w^T\mu$ on hinnangute kaalutud summa. [NÄIDE] Kaalud 60/40 ja oodatavad tootlused 8%/3% annavad 6%. Python: `.6*.08+.4*.03`. Hinnangute viga kandub portfelli; „oodatav” ei tähenda kindlat.

Kovariatsioon $\operatorname{Cov}(X,Y)=E[(X-E X)(Y-E Y)]$ mõõdab ühist muutumist ühikute korrutises. Korrelatsioon $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ on ühikuta. Portfelli dispersioon $\sigma_p^2=w^T\Sigma w$. Kahe vara korral lisandub ristliige $2w_1w_2\rho\sigma_1\sigma_2$.

## Optimeerimine ja selle piir

Markowitzi ülesande üks kuju on $\max_w\{w^T\hat\mu-\frac\gamma2w^T\hat\Sigma w\}$ tingimustel $\sum w_i=1$ ja $w_i\ge0$. Parameeter $\gamma$ väljendab riski vältimist. Kui prognoositud tootlused on mürarikkad, optimeerib lahendus ka müra. Seetõttu võivad positsioonipiirid ja lihtsad kaalud olla mõistlikud isegi siis, kui optimeerija on tehniliselt olemas.

Meie riskivariant ei lahenda Markowitzi ülesannet. Ta valib kolm liidrit ja kasutab selgeid piire. Esmased kaalud on 0,3; 10% jääb rahasse. Kui prognoositud volatiilsus on 18%, korrutatakse kaalud $12/18=2/3$-ga: iga kaal 20%, raha 40%. Kui prognoositud risk on 8%, kaale ei võimendata.

## Võimendus ja stress

Brutoekspositsioon $L=\sum|w_i|$. Kui $L=2$, annab riskivarade −10% muutus ligikaudu −20% enne finantseerimist ja sundmüüke. Long-only portfelli ja raha puhul on $L\le1$; lühikesed positsioonid vajaksid laenukulu ja kättesaadavuse arvestust.

Stressikahju $w^Ts$ kasutab etteantud šokivektorit $s$. Kaalud 0,3/0,3/0,3/0,1 raha ning riskivarade −10%/−20%/−5% annavad −10,5%. Python: `.3*(-.10-.20-.05)`. See ei anna šoki tõenäosust. VaR oleks kindla jaotuse kvantiil; Expected Shortfall kirjeldaks selle piiri taha jäävat keskmist kahju. Mõlemad sõltuvad mudelist, stressitest ei pea üldse tõenäosust eeldama.

## Täitmine

Spread on ostu- ja müügihinna vahe. Slippage on tegeliku ja võrdlushinna erinevus; selles võib sisalduda spread, viivitus ja turumõju. Sama kulu ei tohi eri nimede all kaks korda maha arvata. TWAP jaotab tehingu ajas, VWAP mahuprofiili järgi; kumbki ei garanteeri parimat hinda ega kõrvalda turumõju.

Tehingu suurust võrreldakse saadaoleva mahu ja turusügavusega. ETF-i ekraanil kuvatav maht pole kogu likviidsuse ammendav mõõt, kuid turuosaliste tegelikku võimekust ei saa sellest piiranguta eeldada. Meie õpetusmootor ei hinda kapasiteeti; selle jaoks on vaja täitmiste ja mahuandmeid.


Edasi: [praktikum](praktikum.md) · [ülesanded](ulesanded-lahendused.md)
