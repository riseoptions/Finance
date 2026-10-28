# Hindamine, võimendus ja vead

[Ülesannete sisukord](README.md) · [Matemaatika alus](../07-finantsmatemaatika/README.md)

## Sisukord

- [41. P/E](#u41)
- [42. Tagasiostu EPS-mõju](#u42)
- [43. Lihtsustatud FCF](#u43)
- [44. Püsikasvu väärtus](#u44)
- [45. Võimendus](#u45)
- [46. Päevane 2× ETF](#u46)
- [47. Kelly](#u47)
- [48. Kauplemiskulu](#u48)
- [49. Staking'u ühikurisk](#u49)
- [50. Leia analüüsiviga](#u50)

<a id="u41"></a>
## 41. P/E

**Ülesanne.** Aktsia hind 30, aastane EPS 2. Leia P/E.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Hind väljendatakse ühe aastakasumi ühikutes.

**B. Matemaatika:** `P/E=30/2`.

**C. Python:**

```python
vastus = 30/2
print(f"{vastus:.6f} korda")
```

**Kontrollitud vastus:** 15.000000 korda.

**Tõlgendus ja piirang:** Suhtarv üksi ei tõesta odavust ega kallidust.

</details>

<a id="u42"></a>
## 42. Tagasiostu EPS-mõju

**Ülesanne.** Kasum on 100 ning aktsiate arv väheneb 100-lt 90-le. Leia EPS-i suhteline kasv, kasum muutumatu.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Sama kasum jaguneb väiksemale nimetajale.

**B. Matemaatika:** `kasv=(100/90)/(100/100)−1`.

**C. Python:**

```python
vastus = 100*((100/90)/(100/100)-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** 11.111111 %.

**Tõlgendus ja piirang:** Näide ei arvesta tagasiostu rahastamise mõju kasumile.

</details>

<a id="u43"></a>
## 43. Lihtsustatud FCF

**Ülesanne.** Äritegevuse rahavoog 18, kapitalikulud 15, kasumiaruande kasum 25. Leia CFO−capex.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Raha teenimine ja tekkepõhine kasum on eri asjad.

**B. Matemaatika:** `FCF=18−15`.

**C. Python:**

```python
vastus = 18-15
print(f"{vastus:.6f} rahaühikut")
```

**Kontrollitud vastus:** 3.000000 rahaühikut.

**Tõlgendus ja piirang:** See lühidefinitsioon ei ole automaatselt FCFF ega FCFE täielik arvutus.

</details>

<a id="u44"></a>
## 44. Püsikasvu väärtus

**Ülesanne.** Järgmise aasta dividend 4, nõutav tootlus 10%, püsikasv 2%. Leia Gordoni mudeli väärtus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kasvava geomeetrilise rahavoo nüüdisväärtus koondub, kui r>g.

**B. Matemaatika:** `V=4/(0.10−0.02)`.

**C. Python:**

```python
vastus = 4/(.10-.02)
print(f"{vastus:.6f} rahaühikut")
```

**Kontrollitud vastus:** 50.000000 rahaühikut.

**Tõlgendus ja piirang:** Lõpmatu püsikasv on tugev eeldus; r peab olema suurem kui g.

</details>

<a id="u45"></a>
## 45. Võimendus

**Ülesanne.** Ostad vara 200 eest, võlg 100 ja oma raha 100. Vara langeb 10%, võlg ei muutu. Leia omakapitali tootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Vara kahju 20 langeb 100 suurusele omakapitalile.

**B. Matemaatika:** `r=(200×0.9−100)/100−1`.

**C. Python:**

```python
vastus = 100*((200*.9-100)/100-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -20.000000 %.

**Tõlgendus ja piirang:** Intress, tagatisnõue ja müügikulu on välja jäetud.

</details>

<a id="u46"></a>
## 46. Päevane 2× ETF

**Ülesanne.** Indeks tõuseb 10% ja langeb järgmisel päeval 9.090909…%. Leia ideaalse päevase 2× toote kogutootlus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Päevased võimendatud tegurid tuleb korrutada.

**B. Matemaatika:** `r=(1+2×0.1)×(1+2×(1/1.1−1))−1`.

**C. Python:**

```python
vastus = 100*((1+2*.1)*(1+2*(1/1.1-1))-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -1.818182 %.

**Tõlgendus ja piirang:** Mudelis puuduvad tasud ja jälgimisviga; alusindeks lõpetab algtasemel.

</details>

<a id="u47"></a>
## 47. Kelly

**Ülesanne.** Võidu tõenäosus 55%, võidu korral saad panustatud euro kohta euro kasumit, muidu kaotad panuse. Leia Kelly osakaal.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Maksimeeritakse selle binaarse mudeli oodatavat logkasvu.

**B. Matemaatika:** `f*=p−(1−p)`.

**C. Python:**

```python
vastus = 100*(.55-(1-.55))
print(f"{vastus:.6f} % kapitalist")
```

**Kontrollitud vastus:** 10.000000 % kapitalist.

**Tõlgendus ja piirang:** Sisendite ebakindlus ja isiklikud piirangud pole selles optimumis arvestatud.

</details>

<a id="u48"></a>
## 48. Kauplemiskulu

**Ülesanne.** Ühe tehingu brutokasum on 0.08% kapitalist, sisse- ja väljumise kogukulu 0.10%. Leia netotulemus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kulu võib väikese eelise ära võtta.

**B. Matemaatika:** `neto=0.08−0.10`.

**C. Python:**

```python
vastus = .08-.10
print(f"{vastus:.6f} % kapitalist")
```

**Kontrollitud vastus:** -0.020000 % kapitalist.

**Tõlgendus ja piirang:** Määrad peavad katma sama positsiooni ja sama tehingutsükli.

</details>

<a id="u49"></a>
## 49. Staking'u ühikurisk

**Ülesanne.** Tokenite arv suureneb 10%, kuid ühikuhind langeb 20%. Leia väärtuse muutus baasvaluutas.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Kogus ja hind mõjutavad väärtust korrutisena.

**B. Matemaatika:** `r=1.1×0.8−1`.

**C. Python:**

```python
vastus = 100*(1.1*.8-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -12.000000 %.

**Tõlgendus ja piirang:** Tasud, lukustus ning võimalik tehniline kahju pole arvestatud.

</details>

<a id="u50"></a>
## 50. Leia analüüsiviga

**Ülesanne.** Analüütik ütleb, et +50% ja −50% annavad kokku nulli. Arvuta tegelik kapitalimuutus.

<details>
<summary>Lahendus: arutlus, matemaatika ja Python</summary>

**A. Loogika:** Protsendid rakenduvad eri baasidele.

**B. Matemaatika:** `r=1.5×0.5−1`.

**C. Python:**

```python
vastus = 100*(1.5*.5-1)
print(f"{vastus:.6f} %")
```

**Kontrollitud vastus:** -25.000000 %.

**Tõlgendus ja piirang:** Loogikaviga on kasvutegurite asemel protsentide liitmine.

</details>
