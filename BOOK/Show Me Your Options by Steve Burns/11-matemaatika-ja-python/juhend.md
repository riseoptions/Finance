# Python ja valikuline matemaatika

[Tagasi](../README.md)

## Käivitamine Thonnys

1. Paki kogu kataloog lahti. Ava `python/01_call.py` ja vajuta Run (F5).
2. Arvulised demonstratsioonid kasutavad standardteeki. Graafikute jaoks paigalda Thonny menüüs Tools → Manage packages pakett `matplotlib`.
3. Failid08 ja09 kasutavad samas kaustas olevat `mudel.py` faili; hoia need koos.
4. Muuda ühte sisendit korraga, ennusta vastus ja alles siis käivita. VS Code pole vajalik.

## Google Colab

Ava [optsioonid.ipynb](../colab/optsioonid.ipynb). Kõik koodilahtrid on märkmikus ning mudelifunktsioon defineeritakse esimesena; eraldi failide üleslaadimist pole vaja. Näited ei kasuta API-võtit, internetiandmeid ega maaklerikontot.

## Demonstratsioonid

| Fail | Mida teeb ja sisendid | Oodatav väljund | Katsetamine |
|---|---|---|---|
| [01_call.py](../python/01_call.py) | Call’i P/L; sisendid on faili alguses | S=110 korral +200 USD | Muuda K, preemiat ja hindade loendit. |
| [02_put.py](../python/02_put.py) | Put’i P/L; sisendid on faili alguses | S=80 korral +1200 USD | Muuda K ja preemiat; pane tähele S=0 maksimumkasumit. |
| [03_tasuvus.py](../python/03_tasuvus.py) | Tasuvuspiirid; sisendid on faili alguses | Call104;put95 | Lisa kulud ühe alusvaraühiku kohta preemiale. |
| [04_covered_call.py](../python/04_covered_call.py) | Covered call’i graafik; sisendid on faili alguses | Kasumi lagi800 USD;S0 korral−9700 | Muuda strike’i ja preemiat; vaata nii lage kui langusriski. |
| [05_cash_secured.py](../python/05_cash_secured.py) | Cash-secured put’i graafik; sisendid on faili alguses | Reserveeritud9500;max kahju9200 | Muuda strike’i; sularaha olemasolu ei muuda P/L-kuju. |
| [06_bull_call.py](../python/06_bull_call.py) | Bull call spread’i graafik; sisendid on faili alguses | Max kahju400,max kasum600 | Muuda K2 ja deebetit; hoia K2>K1 ning mõistlik hind. |
| [07_straddle.py](../python/07_straddle.py) | Straddle’i graafik; sisendid on faili alguses | Tasuvus88 ja112;S100 korral−1200 | Muuda kogukulu; võrdle nõutavat liikumist. |
| [08_delta.py](../python/08_delta.py) | Delta-lähendus ja täpsem mudel; sisendid on faili alguses | Algdelta umbes0,5114;puutuja lahkneb suure muutuse korral | Muuda T või sigma; puutuja võib kaugel anda isegi negatiivse hinna, mis näitab lähenduse piiri. |
| [09_theta.py](../python/09_theta.py) | Ajaväärtuse mudelikõver; sisendid on faili alguses | 30 päeva hind ligikaudu2,2872;null päeva hind0 | Muuda S või sigma; ära käsitle kõverat turuhinna ennustusena. |
| [10_stsenaariumid.py](../python/10_stsenaariumid.py) | Kolme strateegia võrdlus; sisendid on faili alguses | S120:1200,600,800 USD;kapitalivajadused erinevad | Lisa üks sama riskieelarvega kogusearvutus, mitte ainult üks leping. |
| [11_oodatav.py](../python/11_oodatav.py) | Oodatav väärtus ja tasuvus-p; sisendid on faili alguses | E=−5 USD;piir93,85% | Muuda p, võitu, kahju ja kulu; see on kahe tulemuse mudel. |
| [12_kogus.py](../python/12_kogus.py) | Riskieelarve ja täisarvuline kogus; sisendid on faili alguses | 3 positsiooni;kogurisk480;eelarve500 | Muuda konto või ühe positsiooni riski; tulemus0 on lubatud. |

## Mis vahe on terminalmudelil ja hinnamudelil?

Demod 01–07 ja 10 kasutavad lõpptähtaja lepingulisi väljamakseid. Demod 08–09 kasutavad enne tähtaega BSM-i. Demod 11–12 kirjeldavad oodatavat väärtust ja kogusevalikut. Kõik sisendid on väljamõeldud, mitte turust alla laaditud.

## Black–Scholesi valikuline süvendus

S on alusvara hind, K strike, T aeg aastates, σ aastane volatiilsus kümnendmurruna, r pideva kapitaliseerimisega riskivaba määr ja q pidev dividendimäär. N on standardse normaaljaotuse jaotusfunktsioon.

$$d_1=\frac{\ln(S/K)+(r-q+\sigma^2/2)T}{\sigma\sqrt T},\qquad d_2=d_1-\sigma\sqrt T.$$

$$C=Se^{-qT}N(d_1)-Ke^{-rT}N(d_2).$$

$$P=Ke^{-rT}N(-d_2)-Se^{-qT}N(-d_1).$$

[MATEMAATIKA] Euroopa hinnamudel eeldab lihtsustatud pidevat hinnaprotsessi, konstantseid parameetreid ja kuludeta ideaalset maandamist. Ei modelleeri diskreetset varajast täitmist ega hinnahüppeid. Vaata [mudel.py](../python/mudel.py).

Call’i delta on $e^{-qT}N(d_1)$ ja put’il $e^{-qT}(N(d_1)-1)$. Gamma on mõlemal $e^{-qT}\varphi(d_1)/(S\sigma\sqrt T)$. Vega ühe täisühiku σ kohta on $Se^{-qT}\varphi(d_1)\sqrt T$; ühe protsendipunkti jaoks jaga 100-ga. Theta päeva kohta saadakse aastaühikust valitud päevakonventsiooni järgi. Kursus kasutab 365 kalendripäeva.

### Delta ja tõenäosuse vahe

BSM-i riskineutraalses mudelis on call’i ITM-tõenäosus N(d₂), mitte N(d₁). Call’i tähtaja kasumitõenäosus preemia c ja kuludeta on samas mudelis:

$$\Pr_Q(S_T>K+c)=N\left(\frac{\ln(S/(K+c))+(r-q-\sigma^2/2)T}{\sigma\sqrt T}\right).$$

Tegelikku tõenäosust ei saa Q-mõõdust automaatselt võtta. Makstud preemia finantseerimiskulu muudaks tähtaja tasuvusläve veel veidi. See selgitab, miks „delta = võiduprotsent” pole täpne.

## Kontrollid

[Kontrollskript](../python/kontrollid.py) testib payoff-identsusi, piiratud strateegiate äärmusi, parity’t, BSM-i referentshindu ja gamma positiivsust. Käivita fail Thonnys või terminalis `python python/kontrollid.py`. Testid ei kinnita strateegia turukasumlikkust.
