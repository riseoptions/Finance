# 24 väikest Pythoni näidet investeerimismatemaatikast

[Tagasi avalehele](../README.md)

Kõik näited on originaalsed [NÄIDE]/[MUDEL] arvutused, kasutavad ainult Pythoni standardteeki ja töötavad ilma võrguühenduseta. Testitud Python 3.12.14-ga. Ava skript Thonnys ja käivita. Selles kogus ei ole elusandmete allalaadimist ega LLM-i API-kutset; neid ei tohi järeldada faili pealkirjast. AI-rakendused on eraldi tulevane töö.

Näited on tahtlikult lühikesed. Sisendid on koodi alguses; tootmiskõlblik sisendivalideerimine pole nende õppe-eesmärk. Raha ümardatakse ainult väljundis. Ingliskeelsed vasted ja valemite eeldused on [alusmoodulis](../01-investeerimise-alused/README.md) ning [matemaatikamoodulis](../07-finantsmatemaatika/README.md).

## Sisukord

- [1. Liitintress](#01_liitintress)
- [2. Reaaltootlus](#02_reaaltootlus)
- [3. Kahjumist taastumine](#03_taastumine)
- [4. Aritmeetiline keskmine ja CAGR](#04_keskmised)
- [5. Nüüdisväärtus](#05_nuudisvaartus)
- [6. Võlakirja hind](#06_volakiri)
- [7. Duration ja intressitundlikkus](#07_duration)
- [8. Portfelli oodatav tootlus](#08_portfelli_ootus)
- [9. Korrelatsioon tootlustest](#09_korrelatsioon)
- [10. Kahe vara standardhälve](#10_portfelli_risk)
- [11. Sharpe’i suhtarv](#11_sharpe)
- [12. Maksimaalne langus](#12_langus)
- [13. Monte Carlo keskmise kontroll](#13_monte_carlo)
- [14. Call-optsiooni kasum tähtajal](#14_call)
- [15. Put-optsiooni kasum tähtajal](#15_put)
- [16. Igapäevase 2× võimenduse teekond](#16_voimendus)
- [17. Rebalanseerimise aritmeetika](#17_rebalanseerimine)
- [18. P/E ja vaba rahavoog](#18_fundamentaal)
- [19. Beeta ja alfa](#19_beeta)
- [20. Püsitasu pikaajaline mõju](#20_kulud)
- [21. Bayesi uuendus](#21_bayes)
- [22. Kelly panuse osakaal](#22_kelly)
- [23. Lihtne viitajaga järeltest](#23_taganttest)
- [24. Regressioon versus naiivne prognoos](#24_baasprognoos)

<a id="01_liitintress"></a>
## 1. Liitintress

**Probleem:** Kui suureks kasvab 1000 eurot viie aastaga 6% aastase tootluse korral?

**Selgitus ja tulemuse tähendus:** Iga järgmine tootlus teenitakse ka varasema tootluse pealt. Tegemist on konstantse tootluse mudeliga.

[Skript](../python/lyhinaited/01_liitintress.py)

```python
algus, tootlus, aastad = 1000, 0.06, 5
lopp = algus * (1 + tootlus) ** aastad
print(f"Lõppväärtus: {lopp:.2f} eurot")
```

Tegelik kontrollväljund:

```text
Lõppväärtus: 1338.23 eurot
```

**Võimalikud vead:** 6% sisesta 0.06, mitte 6. Sissemaksed ja maksud puuduvad.

**Jätkuülesanne:** Lisa 100-eurone sissemakse iga aasta lõpus.

<a id="02_reaaltootlus"></a>
## 2. Reaaltootlus

**Probleem:** Nominaaltootlus on 8% ning hinnatase tõuseb 5%. Kui palju kasvab ostujõud?

**Selgitus ja tulemuse tähendus:** Nominaalset kasvutegurit tuleb jagada hinnataseme kasvuteguriga.

[Skript](../python/lyhinaited/02_reaaltootlus.py)

```python
nominaal, inflatsioon = 0.08, 0.05
reaal = (1 + nominaal) / (1 + inflatsioon) - 1
print(f"Reaaltootlus: {reaal:.4%}")
```

Tegelik kontrollväljund:

```text
Reaaltootlus: 2.8571%
```

**Võimalikud vead:** 8−5=3% on ligikaudne, mitte täpne vastus. Mõlemad määrad peavad katma sama perioodi.

**Jätkuülesanne:** Arvuta reaaltootlus 4% nominaaltootluse ja 6% inflatsiooni korral.

<a id="03_taastumine"></a>
## 3. Kahjumist taastumine

**Probleem:** Kui palju peab allesjäänud kapital kasvama, et taastada algväärtus?

**Selgitus ja tulemuse tähendus:** Protsendibaas pärast kahjumit on väiksem.

[Skript](../python/lyhinaited/03_taastumine.py)

```python
for kahjum in (0.10, 0.25, 0.50, 0.80):
    vajalik = kahjum / (1 - kahjum)
    print(f"Kahjum {kahjum:.0%}: taastumiseks {vajalik:.2%}")
```

Tegelik kontrollväljund:

```text
Kahjum 10%: taastumiseks 11.11%
Kahjum 25%: taastumiseks 33.33%
Kahjum 50%: taastumiseks 100.00%
Kahjum 80%: taastumiseks 400.00%
```

**Võimalikud vead:** 100% kahjumi järel ei saa sama nullkapitaliga taastuda; valemis on siis jagamine nulliga.

**Jätkuülesanne:** Leia taastumiseks vajalik tootlus 35% kahjumi järel.

<a id="04_keskmised"></a>
## 4. Aritmeetiline keskmine ja CAGR

**Probleem:** Mida tähendab +20% ja −20% kahe aasta tootlus?

**Selgitus ja tulemuse tähendus:** Aritmeetiline keskmine on 0%, aga kapital väheneb.

[Skript](../python/lyhinaited/04_keskmised.py)

```python
from math import prod
r = [0.20, -0.20]
aritmeetiline = sum(r) / len(r)
kasvutegur = prod(1 + x for x in r)
cagr = kasvutegur ** (1 / len(r)) - 1
print(f"Aritmeetiline: {aritmeetiline:.2%}")
print(f"Kogutootlus: {kasvutegur-1:.2%}; CAGR: {cagr:.4%}")
```

Tegelik kontrollväljund:

```text
Aritmeetiline: 0.00%
Kogutootlus: -4.00%; CAGR: -2.0204%
```

**Võimalikud vead:** Kahe aasta kogutootlus ja aastane CAGR pole sama.

**Jätkuülesanne:** Võrdle tootlustega +10% ja −10%.

<a id="05_nuudisvaartus"></a>
## 5. Nüüdisväärtus

**Probleem:** Mis on 1100 euro väärtus ühe aasta pärast, kui nõutav tootlus on 10%?

**Selgitus ja tulemuse tähendus:** Diskonteerimine küsib, milline tänane summa kasvaks eeldatud määraga tulevase rahavooni.

[Skript](../python/lyhinaited/05_nuudisvaartus.py)

```python
rahavoog, maar, aeg = 1100, 0.10, 1
pv = rahavoog / (1 + maar) ** aeg
print(f"Nüüdisväärtus: {pv:.2f} eurot")
```

Tegelik kontrollväljund:

```text
Nüüdisväärtus: 1000.00 eurot
```

**Võimalikud vead:** Riskantset lubatud makset ei saa diskonteerida riskivaba määraga ilma riskikohanduseta.

**Jätkuülesanne:** Muuda nõutav tootlus 15%-ks.

<a id="06_volakiri"></a>
## 6. Võlakirja hind

**Probleem:** Leia 1000-eurose, 5% aastakupongiga ja kolmeaastase võlakirja hind 6% tootlusnõude korral.

**Selgitus ja tulemuse tähendus:** Hind on kõigi lepinguliste maksete nüüdisväärtuste summa.

[Skript](../python/lyhinaited/06_volakiri.py)

```python
nimivaartus, kupong, tootlus, aastad = 1000, 0.05, 0.06, 3
hind = sum(nimivaartus * kupong / (1+tootlus)**t
           for t in range(1, aastad+1))
hind += nimivaartus / (1+tootlus)**aastad
print(f"Hind: {hind:.4f}")
```

Tegelik kontrollväljund:

```text
Hind: 973.2699
```

**Võimalikud vead:** Eeldame maksehäire puudumist ja ostu kupongipäeval; kogunenud intress puudub.

**Jätkuülesanne:** Kontrolli, et kupongiga võrdse tootlusnõude korral on hind nimiväärtus.

<a id="07_duration"></a>
## 7. Duration ja intressitundlikkus

**Probleem:** Hinda sama võlakirja tundlikkust väikese tootlusnõude muutuse suhtes.

**Selgitus ja tulemuse tähendus:** Macaulay duration kaalub maksete aegu nüüdisväärtusega; modified duration annab lokaalse hinnatundlikkuse.

[Skript](../python/lyhinaited/07_duration.py)

```python
F, c, y, n = 1000, 0.05, 0.06, 3
cf = [F*c] * n
cf[-1] += F
pv = [v/(1+y)**t for t,v in enumerate(cf,1)]
P = sum(pv)
d_mac = sum(t*v for t,v in enumerate(pv,1))/P
d_mod = d_mac/(1+y)
print(f"Macaulay: {d_mac:.4f}; modified: {d_mod:.4f}")
print(f"Ligikaudne hinnamuutus +0.01 šokiga: {-d_mod*.01:.4%}")
```

Tegelik kontrollväljund:

```text
Macaulay: 2.8573; modified: 2.6956
Ligikaudne hinnamuutus +0.01 šokiga: -2.6956%
```

**Võimalikud vead:** Duration ei ole täpne suurte šokkide ega optsioonidega võlakirjade korral.

**Jätkuülesanne:** Võrdle 1-protsendipunktilist šokki täpse hinnaarvutusega.

<a id="08_portfelli_ootus"></a>
## 8. Portfelli oodatav tootlus

**Probleem:** 60% portfellist teenib ootuslikult 8%, 40% teenib 3%.

**Selgitus ja tulemuse tähendus:** Ühe perioodi oodatav lihttootlus on kaalutud keskmine.

[Skript](../python/lyhinaited/08_portfelli_ootus.py)

```python
kaalud, ootused = [0.6,0.4], [0.08,0.03]
assert abs(sum(kaalud)-1) < 1e-12
vastus = sum(w*r for w,r in zip(kaalud,ootused))
print(f"Portfelli oodatav tootlus: {vastus:.2%}")
```

Tegelik kontrollväljund:

```text
Portfelli oodatav tootlus: 6.00%
```

**Võimalikud vead:** Ootus pole kindel tulemus. Kaalud on perioodi alguse kaalud.

**Jätkuülesanne:** Lisa 10% rahakaal ja muuda ülejäänud kaalud 50%/40%-ks.

<a id="09_korrelatsioon"></a>
## 9. Korrelatsioon tootlustest

**Probleem:** Leia kahe väikese tootlusrea Pearsoni korrelatsioon.

**Selgitus ja tulemuse tähendus:** Korrelatsioon mõõdab standardiseeritud lineaarset koosliikumist.

[Skript](../python/lyhinaited/09_korrelatsioon.py)

```python
from statistics import mean
from math import sqrt
a, b = [.01,-.02,.03,.00], [.02,-.01,.04,.01]
da, db = [x-mean(a) for x in a], [x-mean(b) for x in b]
rho = sum(x*y for x,y in zip(da,db))/sqrt(
    sum(x*x for x in da)*sum(y*y for y in db))
print(f"Korrelatsioon: {rho:.4f}")
```

Tegelik kontrollväljund:

```text
Korrelatsioon: 1.0000
```

**Võimalikud vead:** Hinnatasemete korrelatsioon ei asenda tootluste korrelatsiooni; konstantse rea korral on näitaja määramata.

**Jätkuülesanne:** Asenda teine rida esimese vastandarvudega.

<a id="10_portfelli_risk"></a>
## 10. Kahe vara standardhälve

**Probleem:** Arvuta 50/50 portfelli standardhälve, kui mõlema vara oma on 20% ning korrelatsioon 0.

**Selgitus ja tulemuse tähendus:** Kovariatsioon määrab, kui palju üks vara teise kõikumisi tasakaalustab.

[Skript](../python/lyhinaited/10_portfelli_risk.py)

```python
from math import sqrt
w, s1, s2, rho = .5, .2, .2, 0
var = w*w*s1*s1 + (1-w)**2*s2*s2 + 2*w*(1-w)*rho*s1*s2
print(f"Portfelli standardhälve: {sqrt(var):.4%}")
```

Tegelik kontrollväljund:

```text
Portfelli standardhälve: 14.1421%
```

**Võimalikud vead:** Ära keskmista standardhälbeid ega unusta ruutjuurt.

**Jätkuülesanne:** Korda korrelatsiooniga 1 ja −1.

<a id="11_sharpe"></a>
## 11. Sharpe’i suhtarv

**Probleem:** Arvuta nelja aastase ületootluse põhjal Sharpe’i valimihinnang.

**Selgitus ja tulemuse tähendus:** Näide kasutab sama perioodi riskivaba tootluse suhtes saadud ületootlusi.

[Skript](../python/lyhinaited/11_sharpe.py)

```python
from statistics import mean, stdev
uletootlused = [.04, .08, -.02, .06]
s = mean(uletootlused)/stdev(uletootlused)
print(f"Aastaste ületootluste Sharpe: {s:.4f}")
```

Tegelik kontrollväljund:

```text
Aastaste ületootluste Sharpe: 0.9258
```

**Võimalikud vead:** Väike valim on ebakindel; nullstandardhälbe korral suhtarv puudub. Aastast näitajat ei aastastata uuesti.

**Jätkuülesanne:** Muuda üks aasta suureks kahjumiks ja jälgi tulemust.

<a id="12_langus"></a>
## 12. Maksimaalne langus

**Probleem:** Leia vara suurim tipust põhjani langus, arvestades algkapitali.

**Selgitus ja tulemuse tähendus:** Iga väärtust võrreldakse senise suurima väärtusega.

[Skript](../python/lyhinaited/12_langus.py)

```python
vaartused = [100, 120, 90, 110, 130]
tipp, suurim = vaartused[0], 0
for v in vaartused:
    tipp = max(tipp,v)
    suurim = min(suurim,v/tipp-1)
print(f"Maksimaalne langus: {suurim:.2%}")
```

Tegelik kontrollväljund:

```text
Maksimaalne langus: -25.00%
```

**Võimalikud vead:** Kui algkapital puudub reast, võib esimene kahjum jääda arvestamata; raha sisse- ja väljamaksed vajavad kohandust.

**Jätkuülesanne:** Lisa rea lõppu väärtus 70.

<a id="13_monte_carlo"></a>
## 13. Monte Carlo keskmise kontroll

**Probleem:** Võrdle normaalse logtootlusega ühe aasta lõppväärtuse simulatsiooni teoreetilise ootusega.

**Selgitus ja tulemuse tähendus:** Normaaljaotus kirjeldab siin logtootlust, nii et väärtus jääb positiivseks.

[Skript](../python/lyhinaited/13_monte_carlo.py)

```python
from random import Random
from math import exp
from statistics import mean
rng = Random(42)
mu, sigma, algus = .06, .20, 1000
vaartused = [algus*exp(rng.gauss(mu,sigma)) for _ in range(20000)]
print(f"Simulatsiooni keskmine: {mean(vaartused):.2f}")
print(f"Teoreetiline ootus: {algus*exp(mu+sigma*sigma/2):.2f}")
```

Tegelik kontrollväljund:

```text
Simulatsiooni keskmine: 1082.39
Teoreetiline ootus: 1083.29
```

**Võimalikud vead:** Simulatsioon pole turuennustus; valitud mu ja sigma on eeldused.

**Jätkuülesanne:** Suurenda korduste arvu ja võrdle keskmise viga.

<a id="14_call"></a>
## 14. Call-optsiooni kasum tähtajal

**Probleem:** Ostetud call: täitmishind 100, preemia 5, alusvara lõpphind 110.

**Selgitus ja tulemuse tähendus:** Kasum on väljamakse miinus algne preemia; siin rahastamiskulu ei arvestata.

[Skript](../python/lyhinaited/14_call.py)

```python
S, K, preemia = 110,100,5
valjamakse = max(S-K,0)
kasum = valjamakse-preemia
print(f"Väljamakse: {valjamakse:.2f}; kasum: {kasum:.2f}")
print(f"Preemiatootlus: {kasum/preemia:.2%}")
```

Tegelik kontrollväljund:

```text
Väljamakse: 10.00; kasum: 5.00
Preemiatootlus: 100.00%
```

**Võimalikud vead:** Kasum ja väljamakse pole sama. Tulemus on ühe alusvaraühiku kohta, mitte automaatselt lepingu kohta.

**Jätkuülesanne:** Leia tasuvuspunkt ja kahju alusvara hinnal 90.

<a id="15_put"></a>
## 15. Put-optsiooni kasum tähtajal

**Probleem:** Ostetud put: täitmishind 100, preemia 4, alusvara lõpphind 85.

**Selgitus ja tulemuse tähendus:** Put annab õiguse müüa; väärtus tähtajal kasvab alusvara langemisel.

[Skript](../python/lyhinaited/15_put.py)

```python
S, K, preemia = 85,100,4
valjamakse = max(K-S,0)
print(f"Väljamakse: {valjamakse:.2f}; kasum: {valjamakse-preemia:.2f}")
```

Tegelik kontrollväljund:

```text
Väljamakse: 15.00; kasum: 11.00
```

**Võimalikud vead:** Tähtajaeelne optsioonihind võib sisaldada ajaväärtust.

**Jätkuülesanne:** Leia tulemus alusvara lõpphinnal 105.

<a id="16_voimendus"></a>
## 16. Igapäevase 2× võimenduse teekond

**Probleem:** Alusvara tõuseb 10% ja langeb seejärel algtasemele. Mis juhtub 2× päevase tootlusega?

**Selgitus ja tulemuse tähendus:** Korrutatakse päevade kasvutegureid; kogutootlust ei korrutata lihtsalt kahega.

[Skript](../python/lyhinaited/16_voimendus.py)

```python
from math import prod
r = [.10, 1/1.10-1]
indeks = prod(1+x for x in r)-1
voimendatud = prod(1+2*x for x in r)-1
print(f"Indeks: {indeks:.4%}; päevane 2x: {voimendatud:.4%}")
```

Tegelik kontrollväljund:

```text
Indeks: 0.0000%; päevane 2x: -1.8182%
```

**Võimalikud vead:** Mudelis puuduvad tasud, rahastamiskulud ja jälgimisviga; kui kasvutegur muutub mittepositiivseks, pole mudel tavalise ETF-i kirjeldus.

**Jätkuülesanne:** Võrdle kahe järjestikuse +10% päevaga.

<a id="17_rebalanseerimine"></a>
## 17. Rebalanseerimise aritmeetika

**Probleem:** 50/50 portfellis kasvab üks vara 20% ja teine jääb samaks. Taasta võrdsed kaalud.

**Selgitus ja tulemuse tähendus:** Rebalanseerimine taastab sihtkaalud; see ei garanteeri suuremat tootlust.

[Skript](../python/lyhinaited/17_rebalanseerimine.py)

```python
a,b = 500*1.2,500
siht = (a+b)/2
print(f"Enne: A={a:.2f}, B={b:.2f}")
print(f"Müü A-d {a-siht:.2f}; osta B-d {siht-b:.2f}")
```

Tegelik kontrollväljund:

```text
Enne: A=600.00, B=500.00
Müü A-d 50.00; osta B-d 50.00
```

**Võimalikud vead:** Maksude, hinnavahe ja tehingukulude puudumine on lihtsustus.

**Jätkuülesanne:** Võrdle järgmist perioodi olukorras, kus sama vara tõuseb veel 20%.

<a id="18_fundamentaal"></a>
## 18. P/E ja vaba rahavoog

**Probleem:** Võrdle kasumit ja rahavoogu väljamõeldud ettevõttes.

**Selgitus ja tulemuse tähendus:** P/E kasutab omakapitali hinda ja aktsionäride kasumit; lihtsustatud FCF on äritegevuse rahavoog miinus kapitalikulud.

[Skript](../python/lyhinaited/18_fundamentaal.py)

```python
hind, aktsiaid, kasum = 20,10,25
cfo, capex = 18,15
pe = hind*aktsiaid/kasum
fcf = cfo-capex
print(f"P/E: {pe:.2f}; lihtsustatud FCF: {fcf:.2f}")
```

Tegelik kontrollväljund:

```text
P/E: 8.00; lihtsustatud FCF: 3.00
```

**Võimalikud vead:** See FCF pole automaatselt FCFF või FCFE täpne definitsioon; ettevõtte aruande ridade klassifikatsioon loeb.

**Jätkuülesanne:** Muuda kapitalikulud 15-lt 30-le.

<a id="19_beeta"></a>
## 19. Beeta ja alfa

**Probleem:** Leia OLS-seos kahe lühikese ületootlusrea vahel.

**Selgitus ja tulemuse tähendus:** Beeta mõõdab tundlikkust valitud turuvõrdluse suhtes; alfa on regressiooni vabaliige.

[Skript](../python/lyhinaited/19_beeta.py)

```python
from statistics import mean
x=[-.02,.00,.02,.04]
y=[-.02,.01,.04,.07]
beta=sum((a-mean(x))*(b-mean(y)) for a,b in zip(x,y))/sum((a-mean(x))**2 for a in x)
alfa=mean(y)-beta*mean(x)
print(f"Beeta: {beta:.4f}; perioodi alfa: {alfa:.4%}")
```

Tegelik kontrollväljund:

```text
Beeta: 1.5000; perioodi alfa: 1.0000%
```

**Võimalikud vead:** Nelja vaatlusega täiuslik seos on õpetlik konstruktsioon, mitte tõend juhioskuse kohta.

**Jätkuülesanne:** Lisa ühele fonditootlusele müra.

<a id="20_kulud"></a>
## 20. Püsitasu pikaajaline mõju

**Probleem:** Võrdle 0.2% ja 1.5% aastatasu 7% brutotootluse korral 20 aasta jooksul.

**Selgitus ja tulemuse tähendus:** Kasutame aasta lõpus varalt võetavat tasu: kasvutegur on (1+r)(1−f).

[Skript](../python/lyhinaited/20_kulud.py)

```python
algus,r,n=10000,.07,20
for f in [.002,.015]:
    lopp=algus*((1+r)*(1-f))**n
    print(f"Tasu {f:.1%}: {lopp:.2f} eurot")
```

Tegelik kontrollväljund:

```text
Tasu 0.2%: 37178.03 eurot
Tasu 1.5%: 28602.25 eurot
```

**Võimalikud vead:** r−f on ligikaudne; tegelik tasu ajastus ja lisakulud võivad mudelist erineda.

**Jätkuülesanne:** Leia kahe lõppväärtuse vahe.

<a id="21_bayes"></a>
## 21. Bayesi uuendus

**Probleem:** Hea mudeli eelnev tõenäosus on 10%; testi läbimise tõenäosus hea mudeli korral 80%, halva korral 20%.

**Selgitus ja tulemuse tähendus:** Positiivse testi tõendusjõud sõltub ka headuse eelnevast tõenäosusest.

[Skript](../python/lyhinaited/21_bayes.py)

```python
p_hea,p_pos_hea,p_pos_halb=.10,.80,.20
p_pos=p_hea*p_pos_hea+(1-p_hea)*p_pos_halb
posterior=p_hea*p_pos_hea/p_pos
print(f"P(hea | positiivne test): {posterior:.4%}")
```

Tegelik kontrollväljund:

```text
P(hea | positiivne test): 30.7692%
```

**Võimalikud vead:** Testi täpsus ja mudeli headuse tõenäosus pärast testi pole sama; sisendmäärad on siin eeldused.

**Jätkuülesanne:** Muuda hea mudeli eelnev tõenäosus 1%-ks.

<a id="22_kelly"></a>
## 22. Kelly panuse osakaal

**Probleem:** Võida panustatud euro kohta euro tõenäosusega 55%, muidu kaota panus.

**Selgitus ja tulemuse tähendus:** Kelly maksimeerib selle binaarse kordusmudeli oodatavat logkasvu.

[Skript](../python/lyhinaited/22_kelly.py)

```python
from math import log
p,b=.55,1
f=(b*p-(1-p))/b
g=p*log(1+b*f)+(1-p)*log(1-f)
print(f"Kelly osakaal: {f:.2%}; oodatav logkasv: {g:.6f}")
```

Tegelik kontrollväljund:

```text
Kelly osakaal: 10.00%; oodatav logkasv: 0.005008
```

**Võimalikud vead:** Tõenäosuse hindamisviga, sõltuvad katsed ja suured panused võivad tulemuse rikkuda; see pole isiklik panusesoovitus.

**Jätkuülesanne:** Muuda tegelik võidutõenäosus 48%-ks, hoides esialgset panust.

<a id="23_taganttest"></a>
## 23. Lihtne viitajaga järeltest

**Probleem:** Kas eelmise perioodi positiivsele tootlusele järgnev hoidmine võidab alati osta-ja-hoia strateegiat?

**Selgitus ja tulemuse tähendus:** Positsioon perioodil t põhineb ainult perioodil t−1 teada olnud tootlusel.

[Skript](../python/lyhinaited/23_taganttest.py)

```python
from math import prod
r=[.02,-.01,.03,-.02,.01]
pos=[0]+[int(x>0) for x in r[:-1]]
eelmine,kasv=0,1
for w,x in zip(pos,r):
    kulu=.001*abs(w-eelmine)
    kasv*=1+w*x-kulu
    eelmine=w
print(f"Strateegia: {kasv-1:.4%}; osta-ja-hoia: {prod(1+x for x in r)-1:.4%}")
```

Tegelik kontrollväljund:

```text
Strateegia: -3.3704%; osta-ja-hoia: 2.9485%
```

**Võimalikud vead:** Lühike konstrueeritud rida ei tõenda strateegia headust. Kulu võetakse iga ühikulise positsioonimuutuse eest, lõpp-likvideerimise kulu pole lisatud.

**Jätkuülesanne:** Lisa andmelekkega variant ja selgita, miks selle tulemus pole lubatav.

<a id="24_baasprognoos"></a>
## 24. Regressioon versus naiivne prognoos

**Probleem:** Kas sirgmudel annab ajaliselt eraldatud kontrollandmetel väiksema MSE kui nullmuutuse prognoos?

**Selgitus ja tulemuse tähendus:** Treening kasutab ainult esimest nelja vaatlust; test on eraldi. Sihtmuutuja on järgmise perioodi tootlus.

[Skript](../python/lyhinaited/24_baasprognoos.py)

```python
from statistics import mean
x_train=[-2,-1,1,2]
y_train=[-.02,-.01,.01,.02]
b=sum(x*y for x,y in zip(x_train,y_train))/sum(x*x for x in x_train)
x_test,y_test=[-3,3],[-.025,.025]
mse_model=mean((b*x-y)**2 for x,y in zip(x_test,y_test))
mse_naive=mean(y*y for y in y_test)
print(f"Mudeli MSE: {mse_model:.6f}; nullprognoosi MSE: {mse_naive:.6f}")
```

Tegelik kontrollväljund:

```text
Mudeli MSE: 0.000025; nullprognoosi MSE: 0.000625
```

**Võimalikud vead:** See pole aktsiaturu prognoositavuse tõend. Ka parem MSE ei taga kuludejärgset kauplemistulu.

**Jätkuülesanne:** Muuda kontrollperioodil seose märk ja võrdle tulemusi.
