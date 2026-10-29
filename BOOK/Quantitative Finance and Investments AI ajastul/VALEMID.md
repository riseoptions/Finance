# Valemid koos arvuliste kontrollidega

Kõik näited on [NÄIDE]. Protsendid sisesta Pythonis kümnendmurruna. Valemite eeldused on osa lahendusest.

| Mõiste | Valem | Arvuline kontroll |
|---|---|---|
| Lihttootlus | r=P₁/P₀−1 | 110/100−1=10% |
| Kogutootlus dividendiga | r=(P₁+D)/P₀−1 | (108+2)/100−1=10% |
| Liittootlus | ∏(1+r_t)−1 | +10%, −10% → 1,1×0,9−1=−1% |
| Logtootlus | ln(P₁/P₀) | ln(1,1)=0,09531; pole täpselt 10% |
| Portfelli tootlus | Σw_i r_i | 60%×10%+40%×(−5%)=4% |
| Portfelli dispersioon | wᵀΣw | Kahe 20% volatiilsusega võrdkaalu ja ρ=0 puhul risk 14,14% |
| Sharpe, lihtne aasta | (μ−r_f)/σ | (10%−2%)/20%=0,4 |
| CAGR | (V₁/V₀)^(1/aastad)−1 | 100→121 kahe aastaga → 10% |
| Langus tipust | V/tipptase−1 | 90/120−1=−25% |
| MSE | mean((y−ŷ)²) | y=[1,3], ŷ=[2,2] → 1 ühikut² |
| Ridge eesmärk | Σ(y−Xβ)²+λΣβ² | Suurem λ surub kordajaid; skaleeri sisendid treeningus |
| ETF preemia | hind/NAV−1 | 101/100−1=1% |
| Nullkupongi YTM | (F/P)^(1/T)−1 | (1000/900)^(1/2)−1≈5,409% |

## Black–Scholesi Euroopa call

Dividendideta alusvara, konstantne riskivaba määr r ja volatiilsus σ, pidev mudel:

$$C=S N(d_1)-K e^{-rT}N(d_2),$$
$$d_1=\frac{\ln(S/K)+(r+\sigma^2/2)T}{\sigma\sqrt T},\qquad d_2=d_1-\sigma\sqrt T.$$

S=K=100, T=1, r=0,05, σ=0,20 annab d₁=0,35, d₂=0,15 ja C≈10,4506. N on standardnormaaljaotuse jaotusfunktsioon. Mudel on arbitraažipõhine hinnastamise idealiseering, mitte aktsia suuna prognoos. Ameerika optsiooni ennetähtaegne täitmine ning dividendide mõju nõuavad teist käsitlust.

## Kvantiil ja sabarisk

Kui päevakahjumi 95% kvantiil on 2%, siis mudeli jaotuses on 5% vaatlustest sellest halvemad. ES on selle saba keskmine kahju. VaR=2% ei tähenda, et maksimaalne kahju on 2%.

## Baaspunkt ja kulud

10 bp = 0,1% = 0,001. Täielik sisse-välja ring 10 000 euroga maksab ligikaudu 20 eurot, kui mõlemal suunal kulu 10 bp ja hind vahepeal ei muutu. Kui lõppkapitalitulu arvutatakse kahe kuluperioodi liitmisel, on (1−0,001)²−1=−0,1999%; lihtsumma on −0,2%. Need on eri arvestuskonventsioonid, mitte ümardusviga mudelis.
