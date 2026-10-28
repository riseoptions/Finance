# Tootlus ja raha ajaväärtus

[Ülesannete sisukord](README.md) · [Matemaatika alus](../07-finantsmatemaatika/README.md)

## Sisukord

- [1. Liitintress](#u1)
- [2. Reaaltootlus](#u2)
- [3. Taastumine](#u3)
- [4. CAGR](#u4)
- [5. Kogutootlus dividendiga](#u5)
- [6. Valuutamõju](#u6)
- [7. Nüüdisväärtus](#u7)
- [8. Annuiteet](#u8)
- [9. Tasude mõju](#u9)
- [10. Kahjum protsendipunktides](#u10)

<a id="u1"></a>
## 1. Liitintress

**Ülesanne.** 1000 eurot kasvab 6% aastas viis aastat. Lisamakseid pole. Leia lõppväärtus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kasv toimub igal aastal ka eelnevale kasvule.

**B. Matemaatika:** `V=1000×1.06^5`.

**C. Python:**

```python
vastus = 1000*1.06**5
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 1338.225578 eurot.

**Tõlgendus ja piirang:** Tootlus on mudelis igal aastal sama; see pole turuennustus.

</details>

<a id="u2"></a>
## 2. Reaaltootlus

**Ülesanne.** Nominaaltootlus on 8% ja inflatsioon samal aastal 5%. Leia täpne reaaltootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Võrdle investeeringu ja hinnataseme kasvutegureid.

**B. Matemaatika:** `r=(1.08/1.05)−1`.

**C. Python:**

```python
vastus = 100*(1.08/1.05-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 2.857143 %.

**Tõlgendus ja piirang:** Määrade lahutamine annab ainult lähendi.

</details>

<a id="u3"></a>
## 3. Taastumine

**Ülesanne.** Portfell kaotab 35%. Kui suur tootlus taastab algväärtuse?

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Alles jääb 65% algkapitalist.

**B. Matemaatika:** `r=0.35/0.65`.

**C. Python:**

```python
vastus = 100*.35/.65
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 53.846154 %.

**Tõlgendus ja piirang:** Taastumistootlus arvutatakse järelejäänud kapitalilt.

</details>

<a id="u4"></a>
## 4. CAGR

**Ülesanne.** Tootlused on kolmel aastal +10%, −20%, +30%. Leia CAGR.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kapitali kasv on kolme teguri korrutis.

**B. Matemaatika:** `g=(1.1×0.8×1.3)^(1/3)−1`.

**C. Python:**

```python
vastus = 100*((1.1*.8*1.3)**(1/3)-1)
print(f"{vastus:.6f} % aastas")
```

**Kontrollitud vastus:** 4.586431 % aastas.

**Tõlgendus ja piirang:** Aritmeetiline keskmine ei anna sama kapitalikasvu.

</details>

<a id="u5"></a>
## 5. Kogutootlus dividendiga

**Ülesanne.** Aktsia maksis 100, aasta lõpus 98 ning maksis lõpus dividendi 5. Leia perioodi kogutootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Hinnamuutus ja rahaline väljamakse liidetakse.

**B. Matemaatika:** `r=(98−100+5)/100`.

**C. Python:**

```python
vastus = 100*(98-100+5)/100
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 3.000000 %.

**Tõlgendus ja piirang:** Maksu ja dividendide vahepealset reinvesteerimist pole.

</details>

<a id="u6"></a>
## 6. Valuutamõju

**Ülesanne.** Dollarivara tõuseb 10%; ühe dollari euroväärtus langeb 10%. Leia eurotootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Vara ja valuuta kasvutegurid korrutuvad.

**B. Matemaatika:** `r=1.10×0.90−1`.

**C. Python:**

```python
vastus = 100*(1.1*.9-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -1.000000 %.

**Tõlgendus ja piirang:** Kurss on defineeritud eurodes ühe dollari kohta.

</details>

<a id="u7"></a>
## 7. Nüüdisväärtus

**Ülesanne.** Aasta pärast saad kindlalt 1100 eurot. Diskontomäär on 10%. Leia tänane väärtus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Tänane summa peab kasvama tulevase makseni.

**B. Matemaatika:** `PV=1100/1.1`.

**C. Python:**

```python
vastus = 1100/1.1
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 1000.000000 eurot.

**Tõlgendus ja piirang:** Riskantse makse jaoks peab diskontomäär või rahavoog riski arvestama.

</details>

<a id="u8"></a>
## 8. Annuiteet

**Ülesanne.** Maksad iga aasta lõpus 100 eurot viiel aastal, tootlus 5%. Leia väärtus pärast viimast makset.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Esimene sissemakse kasvab neli aastat, viimane null aastat.

**B. Matemaatika:** `FV=100×(1.05^5−1)/0.05`.

**C. Python:**

```python
vastus = 100*(1.05**5-1)/.05
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 552.563125 eurot.

**Tõlgendus ja piirang:** Aasta alguse sissemaksete korral oleks vastus 1.05 korda suurem.

</details>

<a id="u9"></a>
## 9. Tasude mõju

**Ülesanne.** Algus 10 000, brutotootlus 7%, tasu 1% aasta lõpus, horisont 20 aastat. Leia lõppväärtus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Tasuga väheneb igal aastal ka järgmisel aastal kasvav baas.

**B. Matemaatika:** `V=10000×[(1.07)(0.99)]^20`.

**C. Python:**

```python
vastus = 10000*(1.07*.99)**20
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 31650.417682 eurot.

**Tõlgendus ja piirang:** Tasu ajastus on selgelt määratud; 7−1 on vaid lähend netomäärale.

</details>

<a id="u10"></a>
## 10. Kahjum protsendipunktides

**Ülesanne.** Fond A teenib 12%, B 9%. Leia tootluste vahe protsendipunktides.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kahe protsendi vahe ei ole sama mis suhteline paremus.

**B. Matemaatika:** `vahe=12−9`.

**C. Python:**

```python
vastus = 12-9
print(f"{vastus:.6f} protsendipunkti")
```

**Kontrollitud vastus:** 3.000000 protsendipunkti.

**Tõlgendus ja piirang:** A tootlusmäär on B omast suhteliselt 33.33% suurem, kuid see on teine küsimus.

</details>
