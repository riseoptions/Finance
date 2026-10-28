# Võlakirjad ja optsioonid

[Ülesannete sisukord](README.md) · [Matemaatika alus](../07-finantsmatemaatika/README.md)

## Sisukord

- [11. Kupongvõlakirja hind](#u11)
- [12. Nullkupongvõlakiri](#u12)
- [13. Üheaastane tootlus tähtajani](#u13)
- [14. Macaulay duration](#u14)
- [15. Duration'i lähend](#u15)
- [16. Convexity parandus](#u16)
- [17. Krediidikahju](#u17)
- [18. Call'i kasum](#u18)
- [19. Put'i kasum](#u19)
- [20. Call'i tasuvuspunkt](#u20)

<a id="u11"></a>
## 11. Kupongvõlakirja hind

**Ülesanne.** Nimiväärtus 1000, aastakupong 5%, kolm aastat, tootlusnõue 6%. Ost kupongipäeval. Leia hind.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Diskonteeri iga kupong ja lõppmakse.

**B. Matemaatika:** `P=50/1.06+50/1.06²+1050/1.06³`.

**C. Python:**

```python
vastus = 50/1.06+50/1.06**2+1050/1.06**3
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 973.269881 eurot.

**Tõlgendus ja piirang:** Eeldame lepinguliste maksete täitmist, makse ega kogunenud intressi pole.

</details>

<a id="u12"></a>
## 12. Nullkupongvõlakiri

**Ülesanne.** 1000 eurot makstakse viie aasta pärast; aastane tootlusnõue 4%. Leia hind.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Üksainus tulevane makse diskonteeritakse viieks aastaks.

**B. Matemaatika:** `P=1000/1.04^5`.

**C. Python:**

```python
vastus = 1000/1.04**5
print(f"{vastus:.6f} eurot")
```

**Kontrollitud vastus:** 821.927107 eurot.

**Tõlgendus ja piirang:** Inflatsioon ja maksehäirerisk ei ole mudelis eraldi hinnatud.

</details>

<a id="u13"></a>
## 13. Üheaastane tootlus tähtajani

**Ülesanne.** Maksad võlakirja eest 102. Aasta pärast saad kokku 105. Leia tootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Ainus tulevane makse võrreldakse ostuhinnaga.

**B. Matemaatika:** `y=105/102−1`.

**C. Python:**

```python
vastus = 100*(105/102-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 2.941176 %.

**Tõlgendus ja piirang:** 5-eurone kupong ei tähenda ostjale 5% tootlust.

</details>

<a id="u14"></a>
## 14. Macaulay duration

**Ülesanne.** 1000 nimiväärtus, kolm aastat, aastakupong 50, tootlusnõue 6%. Leia rahavoogude kaalutud aeg.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kaalud on iga makse nüüdisväärtuse osad koguhinnas.

**B. Matemaatika:** `D=(1×50/1.06+2×50/1.06²+3×1050/1.06³)/P`.

**C. Python:**

```python
vastus = (50/1.06+2*50/1.06**2+3*1050/1.06**3)/(50/1.06+50/1.06**2+1050/1.06**3)
print(f"{vastus:.6f} aastat")
```

**Kontrollitud vastus:** 2.857347 aastat.

**Tõlgendus ja piirang:** See pole tähtaja ega modified duration'i sünonüüm.

</details>

<a id="u15"></a>
## 15. Duration'i lähend

**Ülesanne.** Modified duration on 4.5 aastat. Tootlusnõue kasvab 0.5 protsendipunkti. Leia ligikaudne hinnamuutus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Esimese järgu hinnamõju on määramuutusega vastassuunaline.

**B. Matemaatika:** `ΔP/P≈−4.5×0.005`.

**C. Python:**

```python
vastus = 100*(-4.5*.005)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -2.250000 %.

**Tõlgendus ja piirang:** See on lokaalne lähend paralleelsele tootlusnõude muutusele.

</details>

<a id="u16"></a>
## 16. Convexity parandus

**Ülesanne.** Modified duration 5, convexity 30, tootlusnõue tõuseb 1 protsendipunkti. Leia teise järgu lähend.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Lisa duration'i mõjule kõverusest tulenev parandus.

**B. Matemaatika:** `ΔP/P≈−5×0.01+0.5×30×0.01²`.

**C. Python:**

```python
vastus = 100*(-5*.01+.5*30*.01**2)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -4.850000 %.

**Tõlgendus ja piirang:** Convexity on siin aastase diskontokonventsiooniga ühildatud suurus.

</details>

<a id="u17"></a>
## 17. Krediidikahju

**Ülesanne.** Ühe aasta maksehäire tõenäosus on 2% ja kahju maksehäire korral 60% positsioonist. Leia oodatav kahjumäär.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kaalutakse sündmuse kahju tõenäosusega.

**B. Matemaatika:** `EL=0.02×0.60`.

**C. Python:**

```python
vastus = 100*.02*.60
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 1.200000 %.

**Tõlgendus ja piirang:** Riskipreemia ja turuhinna krediidimarginaal ei võrdu automaatselt selle ootusega.

</details>

<a id="u18"></a>
## 18. Call'i kasum

**Ülesanne.** Call'i täitmishind 100, preemia 5, lõpphind 110. Leia ostja kasum alusvaraühiku kohta.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Õigus annab 10 väljamakse, kuid maksis 5.

**B. Matemaatika:** `kasum=max(110−100,0)−5`.

**C. Python:**

```python
vastus = max(110-100,0)-5
print(f"{vastus:.6f} rahaühikut")
```

**Kontrollitud vastus:** 5.000000 rahaühikut.

**Tõlgendus ja piirang:** Rahastamiskulu ja lepingu kordaja jäetakse välja.

</details>

<a id="u19"></a>
## 19. Put'i kasum

**Ülesanne.** Put'i täitmishind 100, preemia 4, lõpphind 85. Leia ostja kasum.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Müügiõiguse väljamaksest lahutatakse preemia.

**B. Matemaatika:** `kasum=max(100−85,0)−4`.

**C. Python:**

```python
vastus = max(100-85,0)-4
print(f"{vastus:.6f} rahaühikut")
```

**Kontrollitud vastus:** 11.000000 rahaühikut.

**Tõlgendus ja piirang:** See on tähtaja kasum, mitte optsiooni turuhind enne tähtaega.

</details>

<a id="u20"></a>
## 20. Call'i tasuvuspunkt

**Ülesanne.** Ostetud call'i täitmishind on 100 ja preemia 5. Leia tähtaja tasuvuspunkt.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kasum null tähendab, et sisemine väärtus katab preemia.

**B. Matemaatika:** `S=K+preemia`.

**C. Python:**

```python
vastus = 100+5
print(f"{vastus:.6f} alusvara hinnaühikut")
```

**Kontrollitud vastus:** 105.000000 alusvara hinnaühikut.

**Tõlgendus ja piirang:** Kulude ja preemia rahastamise arvestamine muudaks piiri.

</details>
