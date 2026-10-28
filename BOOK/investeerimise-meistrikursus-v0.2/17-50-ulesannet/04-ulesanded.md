# Tõenäosus ja statistika

[Ülesannete sisukord](README.md) · [Matemaatika alus](../07-finantsmatemaatika/README.md)

## Sisukord

- [31. Suur võiduprotsent](#u31)
- [32. Bayesi uuendus](#u32)
- [33. Mitu hüpoteesi](#u33)
- [34. Krahhita ajalugu](#u34)
- [35. Diskreetne ES](#u35)
- [36. Ruutjuurega aastastamine](#u36)
- [37. Beeta](#u37)
- [38. CAPM-i ootus](#u38)
- [39. Standardviga](#u39)
- [40. Ligikaudne usaldusvahemik](#u40)

<a id="u31"></a>
## 31. Suur võiduprotsent

**Ülesanne.** 90% tõenäosusega võidad 1, 10% tõenäosusega kaotad 20. Leia ühe katse oodatav kasum.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Sageduse kõrval loeb kahju suurus.

**B. Matemaatika:** `E=0.9×1−0.1×20`.

**C. Python:**

```python
vastus = .9*1-.1*20
print(f"{vastus:.6f} rahaühikut")
```

**Kontrollitud vastus:** -1.100000 rahaühikut.

**Tõlgendus ja piirang:** Oodatav kahju ei ütle, milline üksik katse järgmisena toimub.

</details>

<a id="u32"></a>
## 32. Bayesi uuendus

**Ülesanne.** Hea mudeli eelnev tõenäosus 10%; positiivse testi tõenäosus hea korral 80%, halva korral 20%. Leia headuse tõenäosus positiivse testi järel.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Positiivne tulemus võib pärineda mõlemast mudeliklassist.

**B. Matemaatika:** `P=0.1×0.8/(0.1×0.8+0.9×0.2)`.

**C. Python:**

```python
vastus = 100*(.1*.8)/(.1*.8+.9*.2)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 30.769231 %.

**Tõlgendus ja piirang:** Eelnev tõenäosus ja testi omadused on siin ette antud eeldused.

</details>

<a id="u33"></a>
## 33. Mitu hüpoteesi

**Ülesanne.** Teed 20 sõltumatut testi, kõigi nullhüpotees on tõene ja iga testi valepositiivsuse määr 5%. Leia vähemalt ühe valepositiivse tõenäosus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Lihtsam on arvutada, et ükski test ei anna valepositiivset, ning võtta täiend.

**B. Matemaatika:** `P=1−0.95^20`.

**C. Python:**

```python
vastus = 100*(1-.95**20)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 64.151408 %.

**Tõlgendus ja piirang:** Sõltuvad testid muudavad valemit.

</details>

<a id="u34"></a>
## 34. Krahhita ajalugu

**Ülesanne.** Igas sõltumatus kuus on krahhi tõenäosus 4%. Leia 60 kuu krahhita ajaloo tõenäosus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kõik kuud peavad jääma tavaharusse.

**B. Matemaatika:** `P=0.96^60`.

**C. Python:**

```python
vastus = 100*.96**60
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 8.635231 %.

**Tõlgendus ja piirang:** See mudel ei määra tegelikku turukrahhi tõenäosust.

</details>

<a id="u35"></a>
## 35. Diskreetne ES

**Ülesanne.** 96% tõenäosusega teenid 0.5%, 4% tõenäosusega kaotad 20%. Leia 95% ES kahjude märgikonventsioonis.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Halvim 5% sisaldab kogu 4% krahhi ning 1% tavaharu.

**B. Matemaatika:** `ES=(0.04×0.20−0.01×0.005)/0.05`.

**C. Python:**

```python
vastus = 100*(.04*.20-.01*.005)/.05
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 15.900000 %.

**Tõlgendus ja piirang:** Ainult krahhiharu keskmine oleks 20%, kuid see pole siin 95% ES.

</details>

<a id="u36"></a>
## 36. Ruutjuurega aastastamine

**Ülesanne.** Sõltumatute sama jaotusega päevase ületootluse standardhälve on 1%. Kasuta 252 päeva. Leia aastase summeeritud ületootluse standardhälbe lähend.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Sõltumatute perioodide dispersioonid liituvad.

**B. Matemaatika:** `σa≈0.01×sqrt(252)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*.01*sqrt(252)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 15.874508 %.

**Tõlgendus ja piirang:** Liitunud lihttootluse täpne jaotus ning autokorrelatsioon võivad lähendist erineda.

</details>

<a id="u37"></a>
## 37. Beeta

**Ülesanne.** Ületootluse kovariatsioon turuga on 0.018 ja turu dispersioon 0.012. Leia beeta.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Tundlikkus standardiseeritakse turu dispersiooniga.

**B. Matemaatika:** `β=0.018/0.012`.

**C. Python:**

```python
vastus = .018/.012
print(f"{vastus:.6f} suhtarv")
```

**Kontrollitud vastus:** 1.500000 suhtarv.

**Tõlgendus ja piirang:** Kovariatsioon ja dispersioon peavad pärinema samast perioodist ja definitsioonist.

</details>

<a id="u38"></a>
## 38. CAPM-i ootus

**Ülesanne.** Riskivaba määr 3%, turu oodatav tootlus 8%, beeta 1.2. Leia CAPM-i mudelitootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Mudel kompenseerib beeta kaudu tururiski.

**B. Matemaatika:** `E[R]=0.03+1.2×(0.08−0.03)`.

**C. Python:**

```python
vastus = 100*(.03+1.2*(.08-.03))
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 9.000000 %.

**Tõlgendus ja piirang:** CAPM on tingimuslik tasakaalumudel, mitte garanteeritud tootlus.

</details>

<a id="u39"></a>
## 39. Standardviga

**Ülesanne.** 100 sõltumatu samast jaotusest tootluse standardhälve on 10%. Leia valimi keskmise standardvea hinnang.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Keskmistamise müra väheneb sõltumatuse korral ruutjuurega.

**B. Matemaatika:** `SE=0.10/sqrt(100)`.

**C. Python:**

```python
from math import sqrt
vastus = 100*.10/sqrt(100)
print(f"{vastus:.6f} protsendipunkti")
```

**Kontrollitud vastus:** 1.000000 protsendipunkti.

**Tõlgendus ja piirang:** Turuandmete sõltuvus ja režiimimuutus võivad lähendi rikkuda.

</details>

<a id="u40"></a>
## 40. Ligikaudne usaldusvahemik

**Ülesanne.** Keskmine ületootlus on 2%, standardviga 1 protsendipunkt. Leia normaal-lähendi 95% vahemiku alumine piir.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Keskmisest lahutatakse 1.96 standardviga.

**B. Matemaatika:** `alumine=2−1.96×1`.

**C. Python:**

```python
vastus = 2-1.96*1
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 0.040000 %.

**Tõlgendus ja piirang:** See ei ole ühe tulevase perioodi prognoosivahemik; väike valim võib vajada teist jaotust.

</details>
