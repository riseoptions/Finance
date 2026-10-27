# Täielikud lahendused

Pythoni lahendusfailid `kood/lahendus_XX.py` on käivitatavad. Koodi edukas käivitamine ei asenda tulemuse sisulist põhjendamist.

## M01. Investeerimise loogika ja finantsinstrumendid

### Kontrollküsimuste vastused

1. **Kas indeksit ennast ostetakse?** Tavaliselt ostetakse seda järgivat fondiosakut või tuletisinstrumenti; indeks on arvutus.

2. **Kas kõik ETF-id on indeksfondid?** Ei. ETF kirjeldab kaubeldavat fondistruktuuri, mitte tingimata passiivset juhtimist.

3. **Millal saab aktsionär raha?** Näiteks dividendi või aktsiate müügiga; hinnatõus üksi on realiseerimata tulemus.

4. **Kas võlakiri on riskivaba?** Ei: krediidi-, intressi-, inflatsiooni-, valuuta- ja likviidsusrisk võivad jääda.

5. **Miks pole 10% miinus 4% täpne reaaltootlus?** Ostujõudu võrreldakse suhtena 1,10/1,04, mitte protsendipunktide vahena.

### Arvuliste ülesannete lahendused

1. **Algaja.** (54−50+1)/50=0,10 ehk 10%.

2. **Kesktase.** 1,08/1,03−1=4,854%; ostujõuline lõppväärtus 2097,09 eurot.

3. **Edasijõudnu.** 1,10×0,92−1=1,2%. Valuutamõju korrutatakse, mitte ei liideta lihtsalt.

### Pythoni lahendus

```python
def kogutootlus(p0,p1,d=0):
    if p0<=0: raise ValueError('Ostuhind peab olema positiivne')
    return (p1-p0+d)/p0
assert abs(kogutootlus(50,54,1)-.1)<1e-12
print(kogutootlus(50,54,1))
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Ajahorisont ja talutav rahaline puudujääk ei sobi suure turukõikumisega. Võrdle eesmärgiga sobiva tähtaja ja likviidsusega lahendusi, mitte üksnes keskmist ajaloolist tootlust.

## M02. Aruanded, suhtarvud ja kasvutees

### Kontrollküsimuste vastused

1. **Mis eristab bilanssi ja kasumiaruannet?** Bilanss on hetkeseis, kasumiaruanne hõlmab perioodi.

2. **Kas FCF on kasum?** Ei. FCF lähtub rahavoost ja kapitalikuludest; kasum kasutab tekkepõhist arvestust.

3. **Kas madal P/E on alati odav?** Ei: kasum võib olla ajutiselt kõrge või ettevõtte väljavaade halveneda.

4. **Miks salvestada aruande avaldamisaeg?** Tagantjärele testimisel võib aruannet kasutada alles pärast avaldamist.

5. **Mis muudab teesi kontrollitavaks?** Mõõdetavad väited, tähtajad ja eelnevalt sõnastatud ümberlükkamise tingimused.

### Arvuliste ülesannete lahendused

1. **Algaja.** 900−650=250.

2. **Kesktase.** EPS=2; P/E=20. Eeldus: sama perioodi kasum ja võrreldav aktsiate arv.

3. **Edasijõudnu.** 100 → 72; muutus −28%. Müügitulu kasv ei tähenda kasumi kasvu.

### Pythoni lahendus

```python
def pe(price,eps): return price/eps if eps>0 else None
assert pe(30,2)==15
assert pe(30,-2) is None
print(pe(30,2),pe(30,-2))
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Odavam kasumiühiku suhtes on esimene, kuid parem investeering pole määratav. Vaja on kasumi kvaliteeti, kasvu, võlga, sektorit ja riske.

## M03. Andmed ja korratav uurimistöö

### Kontrollküsimuste vastused

1. **Miks pole puuduv hind null?** Puuduv vaatlus ei tähenda vara väärtuse kadumist.

2. **Miks ei kasutata juhuslikku ajajaotust?** Treeningusse võiks sattuda testperioodi tulevik.

3. **Mida tähendab auto_adjust?** Hinnad korrigeeritakse teenuse corporate actions andmete järgi; rahavoogusid ei lisata siis pimesi uuesti.

4. **Mida tähendab end kuupäev Yahoo päringus?** Näites on see välistav ülemine piir.

5. **Mis on survivorship bias?** Uuritakse ainult tänaseni ellu jäänud varasid ning jäetakse kadunud ettevõtted välja.

### Arvuliste ülesannete lahendused

1. **Algaja.** 84/80−1=5%.

2. **Kesktase.** Ei: pärast splitti on kaks aktsiat hinnaga 60; väärtus endiselt 120, kui muid muutusi polnud.

3. **Edasijõudnu.** Mitte 31.12. Alles pärast avaldamist, arvestades kellaaega ja tehingu tegemise võimalust; päevamudelis konservatiivselt järgmise sobiva kauplemispäeva otsusesse.

### Pythoni lahendus

```python
import pandas as pd
from tuum import kontrolli_hindu
bad=pd.DataFrame({'x':[10,11]},index=['2024-01-01','2024-01-01'])
try: kontrolli_hindu(bad)
except ValueError: print('Duplikaat tuvastati')
else: raise AssertionError('Kontroll puudub')
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Kõigepealt selgita põhjus: hilisem noteerimine, turupüha või andmetõrge. Näite laadija kasutab ühiseid kuupäevi ja raporteerib eemaldamise; see võib valimit kallutada ja pole üldlahendus.

## M04. Tootlus, portfell ja võrdlusindeks

### Kontrollküsimuste vastused

1. **Miks +20% ja −20% ei anna nulli?** Teise perioodi protsendi alus on suurem: 100×1,2×0,8=96.

2. **Mis on CAGR?** Alg- ja lõppväärtust ühendav konstantne aastane liitkasvumäär.

3. **Kas volatiilsus on maksimaalne kahjum?** Ei. See mõõdab tootluste hajuvust.

4. **Millal kehtivad konstantsete kaalude päevatootlused?** Kui portfell tasakaalustatakse vastava sagedusega või kaalude muutus on eraldi modelleeritud.

5. **Miks võrrelda samas valuutas?** Vastasel juhul on tootluses erinev valuutamõju, mitte ainult investeerimisotsuse mõju.

### Arvuliste ülesannete lahendused

1. **Algaja.** 99/100−1=−1%; 1,1×0,9−1=−1%.

2. **Kesktase.** 0,7×0,12+0,3×(−0,02)=7,8%, ühe perioodi algkaaludega.

3. **Edasijõudnu.** Dispersioon 0,25×0,04+0,25×0,04+2×0,25×0,5×0,04=0,03; volatiilsus 17,32%.

### Pythoni lahendus

```python
import pandas as pd
from tuum import osta_hoia,tootlused
p=pd.DataFrame({'A':[100,120,120],'B':[100,100,120]})
bh=(1+osta_hoia(p,[.5,.5])).prod()-1
rb=(1+tootlused(p).mean(axis=1)).prod()-1
print('Osta-hoia',round(bh,4),'tasakaalustatud kuludeta',round(rb,4))
assert abs(bh-.2)<1e-12 and abs(rb-.21)<1e-12
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Üksnes selle võrdluse põhjal ei saa otsustada. Lisa vastava jaotusega baasportfell, risk, kulud ja eesmärk.

## M05. Tuluportfell, võlakirjad ja krüpto

### Kontrollküsimuste vastused

1. **Kas kõrge dividendimäär tõendab head investeeringut?** Ei: hind võis kukkuda ja dividend võib olla jätkusuutmatu.

2. **Mis erineb kupongimääral ja YTM-il?** Esimene kasutab nimiväärtust, teine kõiki rahavooge ja ostuhinda.

3. **Miks hind intressi kasvades langeb?** Fikseeritud rahavoogude diskonteerimise määr suureneb.

4. **Kas staking kaitseb hinnalanguse eest?** Ei; tokenite arv ja nende rahaline väärtus on eri asjad.

5. **Miks 4% reegel pole garantii?** Tulevane tootlus, inflatsioon, kulud, periood ja languste järjekord on ebakindlad.

### Arvuliste ülesannete lahendused

1. **Algaja.** 3/75=4% enne makse ja kulusid.

2. **Kesktase.** 1050/1000−1=5%, üks rahavoog aasta lõpus.

3. **Edasijõudnu.** 1,08×0,75−1=−19%.

### Pythoni lahendus

```python
from tuum import ytm,bond_price
y=ytm(950)
assert abs(bond_price(y=y)-950)<1e-8
print(f'YTM {y:.4%}')
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Kontrolli rahavoogude katet, väljamaksemäära, võlga ja dividendi ajalugu. Üks ettevõte suurendab kontsentratsiooni; väljamakse protsent ei ole kogutootlus.

## M06. Varamonitor, valuuta ja SQL

### Kontrollküsimuste vastused

1. **Mis on positsioon?** Kindlal hetkel hoitav vara kogus.

2. **Miks ei piisa tickerist?** Nimi võib muutuda ning sama sümbol esineda eri turgudel.

3. **Kas puuduva hinna võib asendada nulliga?** Ei, see muudab puuduse näiliseks väärtuse kadumiseks.

4. **Miks SQL-liitmine võib väärtust kahekordistada?** Ühele positsioonile leitakse mitu hinnakirjet, kui võtmed pole unikaalsed.

5. **Kas hetkevaradest saab täpse tootluse?** Väliste rahavoogude ja tehinguajaloo puudumisel üldiselt mitte.

### Arvuliste ülesannete lahendused

1. **Algaja.** 360 EUR.

2. **Kesktase.** 900/(900+600)=60%.

3. **Edasijõudnu.** 1000/1,25=800 EUR; vale korrutamine annaks 1250 EUR.

### Pythoni lahendus

```python
import sqlite3
with sqlite3.connect(':memory:') as c:
    c.execute('CREATE TABLE p(currency TEXT, value REAL)')
    c.executemany('INSERT INTO p VALUES (?,?)',[('USD',100),('EUR',200),('USD',50)])
    total=c.execute('SELECT SUM(value) FROM p WHERE currency=?',('USD',)).fetchone()[0]
    assert total==150
    print(total)
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Vaid siis, kui valuuta ja hindamisaeg on samad ning positsioonid ei dubleeru. Kontrolli ka negatiivset rahajääki ja laenu.

## M07. Risk, optsioonid ja futuurid

### Kontrollküsimuste vastused

1. **Kas VaR on suurim võimalik kaotus?** Ei. See on kahjujaotuse kvantiil.

2. **Kas stop-loss tagab hinna?** Ei, eriti hinnalünga korral.

3. **Mis erineb payoff ja profit mõistetel?** Payoff on lepinguline lõppväljamakse; profit arvestab ka preemiat ja vajadusel kulusid.

4. **Kas futuuri tagatis on ostuhind?** Ei, see tagab lepingu täitmist.

5. **Miks kriis vähendab hajutamise abi?** Korrelatsioonid ja likviidsus võivad muutuda; mineviku seos pole konstant.

### Arvuliste ülesannete lahendused

1. **Algaja.** Väljamakse (58−50)×100=800; preemia 300; kasum 500.

2. **Kesktase.** Drawdown −20%; kogutootlus −12%. Taastumisprotsent arvutatakse uuelt madalamalt baasilt.

3. **Edasijõudnu.** Kahjum −200, nominaal algul 4000, tagatisetootlus −50%. Lisatagatist võib vaja minna; kahjum ei piirdu tagatisega.

### Pythoni lahendus

```python
def kaitstud(s): return s-100+max(95-s,0)-3
assert kaitstud(70)==-8 and kaitstud(120)==17
print(kaitstud(70),kaitstud(120))
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Ei: sabas on vähe vaatlusi, režiim võib muutuda. Lisa ES, stressistsenaariumid, likviidsusanalüüs ja positsioonipiirid.

## M08. Masinõpe: baasmeetodist ausa hindamiseni

### Kontrollküsimuste vastused

1. **Mis on tunnus ja siht?** Tunnus on otsuse hetkel teada olev sisend; siht on prognoositav tulemus.

2. **Miks võrrelda hinnaprognoosi eilse hinnaga?** Hinnataseme püsivus võib teha lihtsa prognoosi väga tugevaks.

3. **Miks standardiseerida treeningul?** Testi statistika kasutamine tooks tulevikuinfot mudelisse.

4. **Kas klaster on ostusoovitus?** Ei, see näitab sarnasust valitud tunnustes.

5. **Kas parem RMSE tähendab kasumit?** Ei: vaja on täidetavat otsusereeglit, kulusid ja riski hindamist.

### Arvuliste ülesannete lahendused

1. **Algaja.** Vead [1,−1], ruudud [1,1], keskmine 1, ruutjuur 1.

2. **Kesktase.** Baas 65%, mudel 62%; mudel kaotab selle mõõdiku järgi.

3. **Edasijõudnu.** Treeningu silt sisaldab testiaja tootlusi. Eemalda kattuvad treeningnäited vastavalt sihi lõpuajale; pelgalt shuffle=False ei piisa.

### Pythoni lahendus

```python
import numpy as np
y=np.array([.01,-.02,.01]);rmse=np.sqrt(np.mean(y*y))
assert abs(rmse-np.sqrt(.0002))<1e-12
print(f'RMSE {rmse:.6f}')
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Kontrolli kuludega majandustulemust, ebakindlust ja mitmekordset katsetamist. Väike statistiline paranemine võib jääda kuludest väiksemaks.

## M09. LLM, RAG ja piiratud uurimisagent

### Kontrollküsimuste vastused

1. **Mis on RAG?** Vastuse genereerimine eelnevalt otsitud allikakonteksti toel.

2. **Kas otsinguskoor on tõeväärtus?** Ei, see väljendab sobivust kasutatud esitusruumis.

3. **Mis eristab agenti töövoost?** Agent valib järgmise tegevuse dünaamiliselt; töövoog võib olla täielikult ette määratud.

4. **Kus arvutada tootlus?** Deterministlikus kontrollitud koodis, mitte ainult LLM-i tekstivastuses.

5. **Kas kaks nõustuvat LLM-i kinnitavad fakti?** Ei. Kinnituseks on algallikas ja kontrollitav arvutus.

### Arvuliste ülesannete lahendused

1. **Algaja.** 16/20=80%; lisa hinnang puuduvatele olulistele väidetele.

2. **Kesktase.** 9/12=75%, kui igal küsimusel on selgelt määratud vajalik tõend.

3. **Edasijõudnu.** 15−30/4=7,5 minutit aruande kohta. See ei arvesta tuvastamata vigade kahju ega API hinda.

### Pythoni lahendus

```python
from uurimisagent import invoke
try: invoke({'tool':'kauple'})
except ValueError: print('Lubamatu tööriist blokeeritud')
else: raise AssertionError('Tööriistade piirang puudub')
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Viide on olemas, kuid ei toeta väidet. Märgi vastus kontrollis läbikukkunuks; nõua täpset lõiku ja erista prognoos aruande faktist.

## M10. Graafikud ja tehnilised indikaatorid

### Kontrollküsimuste vastused

1. **Mida näitab OHLC?** Perioodi avamis-, kõrgeimat, madalaimat ja sulgemishinda.

2. **Miks SMA hilineb?** See kasutab mineviku keskmist ning reageerib uuele hinnale osaliselt.

3. **Kas RSI 70 tähendab kindlat langust?** Ei; trend võib jätkuda.

4. **Kas Bollingeri piir on kindel tõenäosusvahemik?** Ei, tavapärased hinnasarjad ei vasta sellise lihtsa tõlgenduse eeldustele.

5. **Miks erinevad RSI-d platvormidel?** Silumine, algväärtustamine, andmed ja periood võivad erineda.

### Arvuliste ülesannete lahendused

1. **Algaja.** (8+10+12)/3=10.

2. **Kesktase.** 0,25×24+0,75×20=21.

3. **Edasijõudnu.** RS=3, RSI=100−100/4=75. See ei ole iseseisev põhjendatud müügikorraldus.

### Pythoni lahendus

```python
import pandas as pd
s=pd.Series([10,12,14,16]).rolling(3).mean()
assert s.iloc[:2].isna().all() and list(s.iloc[2:])==[12,14]
print(s.to_string())
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

See on hüpoteesi loomine sama andmestiku abil. Vaja on hilisemat puutumatut testi, kulusid ja eri režiime; visuaalne sobivus ei ole tõendus.

## M11. Algoritmiline kauplemine ja järeltest

### Kontrollküsimuste vastused

1. **Mis on backtest?** Eelnevalt määratud reeglite ajalooline simulatsioon eeldatud täitmistega.

2. **Miks signaal ja täitmine eraldada?** Otsuse tegemiseks vajaliku hinnaga ei saa pärast selle teadasaamist automaatselt kaubelda.

3. **Kas limit order tagab tehingu?** Ei, see piirab hinda.

4. **Mis on slippage?** Eeldatud ning tegeliku täitmishinna erinevus.

5. **Miks testida eri kulu tasemeid?** Väike brutoeelis võib realistlike kulude korral kaduda.

### Arvuliste ülesannete lahendused

1. **Algaja.** 30−2×2=26.

2. **Kesktase.** Ligikaudu 20; täpses järjestikuses proportsionaalses mudelis 10000×(0,999²−1)=−19,99.

3. **Edasijõudnu.** Teisipäeva sulgemisest kolmapäeva sulgemiseni. Esmaspäevast teisipäevani uut positsiooni veel ei hoitud.

### Pythoni lahendus

```python
from tuum import demo_hinnad,backtest
s=demo_hinnad().iloc[:,0]
a=(1+backtest(s,0).neto).prod();b=(1+backtest(s,.003).neto).prod()
assert b<=a+1e-12
print('Kuludeta',a,'kuludega',b)
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Kui sama test määras võitja, pole see enam puutumatu test. Säilita katsete logi ning hinda väljavalitud reeglit uuel perioodil; juhuslik võitja on tõenäoline.

## M12. Erakapital ja iduettevõtete hindamine

### Kontrollküsimuste vastused

1. **Mis on pre-money?** Ettevõtte kokkuleppeline väärtus enne uue raha lisamist.

2. **Mis on dilution?** Olemasoleva osaluse protsendi vähenemine uute osade loomisel.

3. **Kas väiksem protsent tähendab alati väiksemat euroväärtust?** Ei: ettevõtte koguväärtus võib kasvada.

4. **Mis on runway?** Rahavaru hinnanguline kestus netokulu alusel.

5. **Miks exit ei pruugi jaguneda osalustega võrdeliselt?** Eri osakuklasside õigused ja likvideerimiseelistused võivad muuta jaotust.

### Arvuliste ülesannete lahendused

1. **Algaja.** 1/(9+1)=10%.

2. **Kesktase.** 15%×75%=11,25%, kui ise ei osale ja muud lahjenemist pole.

3. **Edasijõudnu.** Esimese kuu järel 275 000; edasi 275000/30000=9,167 kuud; kokku ligikaudu 10,17 kuud pideva kulumudeli järgi.

### Pythoni lahendus

```python
share=.1
for new in [.2,.25]: share*=1-new
assert abs(share-.06)<1e-12
print(f'Lõpposalus {share:.1%}')
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Uuri lepingulisi õigusi, rahastuse tõenäosust, lahjenemist, kohustusi ja väljumisvõimalust. Järgmine hinnang ei ole realiseeritud müügihind.

## M13. Otsustusprotsess, lõpp-projekt ja õpetamine

### Kontrollküsimuste vastused

1. **Kas edukas tehing tõendab head meetodit?** Ei, üksik tulemus võib olla juhuslik.

2. **Mis on hindsight bias?** Tagantjärele peetakse toimunut etteaimatavamaks kui see otsustamise hetkel oli.

3. **Miks dokumenteerida ümberlükkamise tingimus?** See piirab lõputut valikuliste põhjenduste lisamist.

4. **Millal lisada agent?** Kui dünaamiline tööriistavalik annab mõõdetava kasu võrreldes lihtsa töövooga.

5. **Mida õpetamisel hinnata?** Mõistmist, korrektset arvutust, eeldusi, tõendeid ja iseseisvat rakendamist.

### Arvuliste ülesannete lahendused

1. **Algaja.** 240 min = 4 tundi enne arendus- ja hoolduskulu.

2. **Kesktase.** 6×60/15=24 jooksu, kui hoolduskulu puudub.

3. **Edasijõudnu.** Need on eri mõõdikud: põhjendatuse määr 80%, positiivse tulemuse määr 60%. Vaja on juhtumite seost, riskitaset ja võrdlusbaasi; neid ei saa asendada ühe skooriga.

### Pythoni lahendus

```python
from math import ceil
def tasuvus(arendus_tunnid,saast_min):
    if saast_min<=0: raise ValueError('Sääst peab olema positiivne')
    return ceil(arendus_tunnid*60/saast_min)
assert tasuvus(7,16)==27
print(tasuvus(7,16))
```

Tõlgendus: kontrollväited (`assert`) seovad arvutuse teadaoleva tulemusega; töölehe küsimus määrab, mida funktsioon kontrollib.

### Juhtumi lahendus

Ei. Kui katse oli korrektne, on negatiivne tulemus väärtuslik. Selgita piiranguid ning ära vali tagantjärele ilusamat perioodi.
