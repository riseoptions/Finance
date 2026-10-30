# Neljapäev: päev 4


## A. 09.00 – Prognoosist ei piisa

[SIMULATSIOON] Priya vaatab kahte väljavalitud sektorit. „Miks just pool raha kummassegi?” Maarika vastab, et nii oli lihtne võrrelda. Marcus küsib: „Kas see tähendab, et see jaotus on investeerimiseks sobiv?” Ei tähenda. Võrdlusreegel ja kapitaliotsus täidavad eri eesmärke.

## B. Alternatiivid

Maarika kaalub võrdkaalu, pöördvolatiilsust ja Markowitzi optimeerimist. Kuue vara ja ebakindlate keskmiste puhul võib optimeerija koondada raha juhuslikult parimana tunduvasse varasse. Ta valib esmalt läbipaistva piirangu: kolm vara, igaüks kuni 30%, ülejäänu raha ning 12% volatiilsuse siht ilma võimenduseta.

Ta tunnistab, et see muudab korraga nii valitavate varade arvu kui ka riski. Seetõttu ei saa erinevust nimetada ainult „volatiilsussihtimise mõjuks”. Eraldi põhjusliku võrdluse jaoks tuleks muuta üht tingimust korraga.

## C. 10.25 – Riskijuhi küsimus

Marcus: „Sinu 12% siht põhineb eilsel kovariatsioonil. Mis siis, kui korrelatsioonid homme tõusevad?”

Maarika: „Tegelik risk võib olla suurem. Teen eraldi ühise languse stsenaariumi.”

Elena: „Ja langeval turul ei pruugi müük toimuda viimasel nähtud hinnal.”

Portfelli piirang ei garanteeri väljumishinda. Meeskond lisab eraldi tingimuse: andmevea korral ei väljastata uusi ordereid; olemasolevate positsioonide käsitlemise otsustab vastutav inimene.

## D. Hajutamise intuitsioon

[NARANG] Peatükid 4 ja 6: risk ning kapitalijaotus kuuluvad süsteemi tuuma. [JANSEN] Peatükid 17–19: prognoosist saab portfell alles piirangute, kulude ja riskimudeli kaudu. Kuus eri nimetust ei võrdu kuue sõltumatu riskiga. Kõik võivad sõltuda aktsiaturu ühest liikumisest.

## E. Kaks vara

[NÄIDE] Mõlema vara aastavolatiilsus on 20%, kaalud 50/50 ja korrelatsioon −0,5. Portfelli dispersioon on $0.25\cdot0.04+0.25\cdot0.04+2\cdot0.5\cdot0.5\cdot(-0.5)\cdot0.2\cdot0.2=0.01$. Volatiilsus on 10%.

See pole tasuta kindlustus: korrelatsioon on hinnang, mitte leping. Kui see tõuseb üheni, tõuseb sama portfelli volatiilsus 20%-ni.

## F. 13.15 – Portfell ja stress

[PRAKTIKA] Käivita `python/paev4.py`. Vaata viimast kaalurida ja korruta see etteantud šokkidega. Selles komplektis annab viimane piiratud portfell umbes −11,23% stressikahju enne stressiga kaasnevaid tehingukulusid. See on üks stsenaarium, mitte halvim võimalik tulemus.

Riskivariandi volatiilsust hinnatakse iga signaali ajal ainult viimase 63 vaatluspäeva tootlustega. Kui hinnang ületab 12%, vähendatakse kõiki riskivarade kaale ühtlaselt. Kui hinnang on väiksem, võimendust ei lisata.

## G. 15.10 – Odav kauplemine muutub kalliks

Elena muudab kulueelduse 10 bp-lt 50 bp-le. Kõrge käibega mudel kaotab rohkem tootlust. Sama orderisuurus võib väikese konto jaoks olla tühine ning suure konto jaoks oluline osa turu mahust. Puuduv mahumudel tähendab, et firma 45 miljonile ei saa katset automaatselt laiendada.

## H. 16.35 – Päeva otsus

Riskivariant lisatakse aruandesse eraldi portfellina. Ühe positsiooni 30% piir kehtib ümberjaotamise hetkel; hiljem võib kaal turuliikumise tõttu triivida üle piiri. Pidev piirang vajaks sagedasemat seiret ja lisatehinguid. Homme tuleb need piirid komiteele otse välja öelda.

## I. Õhtune märkmik

**Viis mõistet:** kovariatsioon, positsioonikaal, riskisiht, likviidsus, stressitest.

**Põhimõtted:** hajutamine sõltub ühisriskist; siht pole garantii; maksimaalne ajalooline langus pole maksimaalne võimalik langus; võrdle riski muutust koos tootluse muutusega.


---

Edasi: [teooria](teooria.md) · [praktikum](praktikum.md) · [ülesanded ja lahendused](ulesanded-lahendused.md) · [sisukord](../README.md)
