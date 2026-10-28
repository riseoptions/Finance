# Portfell ja riskimõõdikud

[Ülesannete sisukord](README.md) · [Matemaatika alus](../07-finantsmatemaatika/README.md)

## Sisukord

- [21. Portfelli ootus](#u21)
- [22. Kahe vara risk](#u22)
- [23. Täiuslik koosliikumine](#u23)
- [24. Vastassuunaline liikumine](#u24)
- [25. Hajutamise piirrisk](#u25)
- [26. Korrelatsioonistress](#u26)
- [27. Sharpe](#u27)
- [28. Maksimaalne langus](#u28)
- [29. Sortino nimetaja](#u29)
- [30. Rebalanseerimise tehing](#u30)

<a id="u21"></a>
## 21. Portfelli ootus

**Ülesanne.** 60% kapitalist on varas ootusega 8%, 40% varas ootusega 3%. Leia ühe perioodi ootus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Ootus on lineaarne, sõltumata korrelatsioonist.

**B. Matemaatika:** `E[R]=0.6×0.08+0.4×0.03`.

**C. Python:**

```python
vastus = 100*(.6*.08+.4*.03)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 6.000000 %.

**Tõlgendus ja piirang:** Ühe perioodi lihttootluste ootus ei ole automaatselt mitme perioodi CAGR.

</details>

<a id="u22"></a>
## 22. Kahe vara risk

**Ülesanne.** Võrdsed kaalud, mõlema standardhälve 20%, korrelatsioon 0. Leia portfelli standardhälve.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Nullkorrelatsiooni korral liituvad kaalutud dispersioonid.

**B. Matemaatika:** `σp=sqrt(0.5²×0.2²+0.5²×0.2²)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*sqrt(.5**2*.2**2+.5**2*.2**2)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 14.142136 %.

**Tõlgendus ja piirang:** Dispersioonist tuleb võtta ruutjuur.

</details>

<a id="u23"></a>
## 23. Täiuslik koosliikumine

**Ülesanne.** Kaks 20% standardhälbega vara võrdsete kaaludega; korrelatsioon 1. Leia portfelli risk.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Ühesugune kõikumine ei tasakaalusta teineteist.

**B. Matemaatika:** `σp=sqrt(0.01+0.01+0.02)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*sqrt(.01+.01+.02)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 20.000000 %.

**Tõlgendus ja piirang:** Täiusliku positiivse korrelatsiooniga erineva riskiga varade tulemus on kaalutud standardhälve.

</details>

<a id="u24"></a>
## 24. Vastassuunaline liikumine

**Ülesanne.** Kaks 20% riskiga vara 50/50, korrelatsioon −1. Leia portfelli standardhälve.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Võrdsed kõikumised tühistavad selles mudelis teineteise.

**B. Matemaatika:** `σp=sqrt(0.01+0.01−0.02)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*sqrt(.01+.01-.02)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 0.000000 %.

**Tõlgendus ja piirang:** Tegelikult tuleb arvestada teisi riske ning korrelatsiooni muutumist.

</details>

<a id="u25"></a>
## 25. Hajutamise piirrisk

**Ülesanne.** Võrdsete varade σ=20%, kõigi paaride ρ=0.1. Leia n kasvades piirrisk.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Ühine komponent ei kao varade arvu kasvuga.

**B. Matemaatika:** `σpiir=0.2×sqrt(0.1)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*.2*sqrt(.1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 6.324555 %.

**Tõlgendus ja piirang:** Piir kehtib fikseeritud ühiskorrelatsiooniga mudelis.

</details>

<a id="u26"></a>
## 26. Korrelatsioonistress

**Ülesanne.** 10 võrdse kaaluga vara, σ=20%, ρ=0.8. Leia portfelli standardhälve.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Asenda korrelatsioon valemis enne riski võrdlemist.

**B. Matemaatika:** `σp=0.2×sqrt(0.8+0.2/10)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*.2*sqrt(.8+.2/10)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 18.110770 %.

**Tõlgendus ja piirang:** See on stsenaarium, mitte mõõdetud kriisistatistika.

</details>

<a id="u27"></a>
## 27. Sharpe

**Ülesanne.** Aastane keskmine ületootlus 6%, aastane ületootluse standardhälve 12%. Leia Sharpe.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Ületootlus standardiseeritakse kõikumisega.

**B. Matemaatika:** `S=0.06/0.12`.

**C. Python:**

```python
vastus = .06/.12
print(f"{vastus:.6f} suhtarv")
```

**Kontrollitud vastus:** 0.500000 suhtarv.

**Tõlgendus ja piirang:** Tulemus ei kirjelda üksinda sabariski ega valimi ebakindlust.

</details>

<a id="u28"></a>
## 28. Maksimaalne langus

**Ülesanne.** Kapitalirada on 100, 120, 90, 110, 130. Leia suurim tipust põhjani langus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Madalaimat väärtust võrreldakse sellele eelnenud tipuga.

**B. Matemaatika:** `DD=90/120−1`.

**C. Python:**

```python
vastus = 100*(90/120-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -25.000000 %.

**Tõlgendus ja piirang:** Hiljem uus tipp ei kustuta varem kogetud langust.

</details>

<a id="u29"></a>
## 29. Sortino nimetaja

**Ülesanne.** Kaks periooditootlust on −2% ja +2%, siht 0. Kasuta kõigi perioodide arvuga jagamist. Leia downside deviation.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Arvesta ainult alla sihi jäävat hälvet, kuid jaga kahe perioodiga.

**B. Matemaatika:** `DD=sqrt((0.02²+0²)/2)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*sqrt(.02**2/2)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 1.414214 %.

**Tõlgendus ja piirang:** Ainult negatiivsete perioodide arvuga jagamine annaks teise definitsiooni.

</details>

<a id="u30"></a>
## 30. Rebalanseerimise tehing

**Ülesanne.** 500/500 portfellis tõuseb esimene vara 20%, teine ei muutu. Kui palju esimest vara müüa, et taastada 50/50?

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Uus koguväärtus on 1100 ja kummagi sihtväärtus 550.

**B. Matemaatika:** `müük=600−1100/2`.

**C. Python:**

```python
vastus = 600-1100/2
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 50.000000 eurot.

**Tõlgendus ja piirang:** See taastab kaalud; tulevast tootluseelist pole tuletatud.

</details>
