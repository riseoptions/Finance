# Matemaatika meelespea ja kontrollarvutused

[NÄIDE / TÄIENDUS] Päevade teooria avab valemid kasutusolukorras. Siin on kokkuvõtlik kaart. Käivita `python/matemaatika.py`; tabeli lühiväljendid saab proovida Thonny konsoolis. Kõik protsendid sisesta kümnendmurruna.

| Suurus | Valem ja tähised | Arvuline näide / Python | Tõlgendus ja eeldus |
|---|---|---|---|
| Lihttootlus | $r=P_1/P_0-1$, võrreldavad hinnad $P$ | `108/100-1` → 8% | Ühe perioodi suhteline muutus; dividend käsitleda järjekindlalt |
| Logtootlus | $\ell=\ln(1+r)$ | `np.log(1.1)` → 0,09531 | Liitub ajas; pole sama mis portfelli kaalutud lihttootlus |
| Liitkapital | $W_n=W_0\prod_t(1+r_t)$ | `100*1.2*.8` → 96 | Eeldab kirjeldatud reinvesteerimist |
| Geomeetriline keskmine | $g=(\prod(1+r_t))^{1/n}-1$ | `np.sqrt(.96)-1` → −2,02% | Võrdse pikkusega perioodid |
| Oodatav väärtus | $E[X]=\sum p_i x_i$ | `.55*1-.45*1.5` → −0,125 | Tõenäosused summeeruvad üheks; need ise on hinnangud |
| Dispersioon | $\operatorname{Var}(X)=E[(X-E X)^2]$ | `np.var([-1,1])` → 1 | Populatsiooni näide; valimi hinnanguks `ddof=1` |
| Standardhälve | $\sigma=\sqrt{\operatorname{Var}(X)}$ | `np.std([-.02,.02])` → 2% | Ei kirjelda üksinda sabariski |
| Kovariatsioon | $E[(X-E X)(Y-E Y)]$ | `np.cov([-1,1],[-2,2],ddof=0)[0,1]` → 2 | Ühikud on korrutises |
| Korrelatsioon | $\rho=Cov/(\sigma_X\sigma_Y)$ | `np.corrcoef([-1,1],[-2,2])[0,1]` → 1 | Lineaarne seos, mitte põhjuslikkus |
| Lineaarne mudel | $\hat y=b+\beta x$ | `.002+1.2*.05` → 6,2% | Antud $b$ ja $\beta$; prognoos pole garanteeritud |
| Ridge ühe tunnusega | $\hat\beta=(x^Tx+\lambda)^{-1}x^Ty$ | `2/(4+1)` → 0,4 | Keskendatud tunnus; mitme tunnuse puhul maatriks |
| Portfelli ootus | $\mu_p=\sum w_i\mu_i$ | `.6*.08+.4*.03` → 6% | Sama periood ja võrreldavad ootused |
| Portfelli risk | $\sigma_p^2=w^T\Sigma w$ | `np.sqrt(.25*.04+.25*.04+2*.25*(-.5)*.04)` → 10% | Sigma on sobiva perioodi kovariatsioonimaatriks |
| Sharpe | $\sqrt{12}\bar x/s_x$ kuiste ületootluste jaoks | `np.sqrt(12)*.01/.04` → 0,866 | Aastastamise lähendus; rf ja sagedus peavad sobima |
| Langus tipust | $W_t/\max_{u\le t}W_u-1$ | `90/120-1` → −25% | Arvesta algkapitali; mõõtmise sagedus loeb |
| Brutoekspositsioon | $L=\sum|w_i|$ | `abs(1.5)+abs(-.5)` → 2 | Netokaal on siin 1, kuid bruto 2 |
| Stress | $w^Ts$ | `.3*(-.1-.2-.05)` → −10,5% | Stsenaarium ilma tõenäosusväiteta |
| Kulu | $k=c\sum|(1-k)w-v|$ | esmaost `0.001/1.001` → 0,0999% | Kulujärgsed sihtkaalud, lineaarne kulu |
| Netotootlus | $(1-k)(1+r_g)-1$ | `.998*1.03-1` → 2,794% | Kulu perioodi alguses; $r_g$ on bruto |
| RMSE | $\sqrt{mean((y-\hat y)^2)}$ | `np.sqrt((.01**2+.03**2)/2)` → 2,236 pp | Ruutkadu, tundlik äärmustele |
| Precision ja recall | $TP/(TP+FP)$; $TP/(TP+FN)$ | `30/50,30/40` → 60%, 75% | Ei hõlma kasumi suurust |

## Jaotused ja valimi ebakindlus

Normaaljaotus on kasulik lähendus mõnele arvutuslikule ülesandele, kuid finantstootlused võivad olla asümmeetrilised, paksude sabade ja ajas muutuva hajuvusega. Kui mudel eeldab normaalsust, tuleb kontrollida, kas sabaotsuseid saab sellele rajada. Meie generaator sisaldab normaalset müra ja eraldi kunstlikku stressiplokki; see ei esita realistliku turujaotuse täielikku mudelit.

Sõltumatute sama jaotusega vaatluste keskmise standardviga oleks $s/\sqrt n$. Näiteks $s=4\%$, $n=36$ annab ligikaudu 0,667 protsendipunkti kuus. Python: `.04/np.sqrt(36)`. Autokorrelatsiooni või paneelisõltuvuse korral ei saa seda valemit pimesi kasutada. Kursuse paaris-plokk-bootstrap on üks lihtne sõltuvust osaliselt säilitav alternatiiv, mitte universaalne parandus.

## Miks madalam tootlus võib olla parem?

Portfell A teenib hinnanguliselt 8% volatiilsusega 20%, portfell B 7% volatiilsusega 10%. Nullise riskivaba määra juures on suhtarvud 0,4 ja 0,7. Investor, kelle kahjutaluvus on piiratud, võib eelistada B-d. Teine investor võib vajada kõrgemat oodatavat tootlust. Otsus sõltub eesmärgist, ajahorisondist ja hinnangute usaldusväärsusest; üks suhtarv ei otsusta kõike.
