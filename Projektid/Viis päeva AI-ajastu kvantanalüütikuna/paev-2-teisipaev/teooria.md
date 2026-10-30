# Päev 2: tootlus, risk ja aus katse

[NARANG: ptk 5, 9–10; JANSEN: ptk 7, 16, 18]

Aritmeetiline keskmine $\bar r=\frac1n\sum r_t$ kirjeldab ühe perioodi keskmist. Liitkasv $W_n=W_0\prod(1+r_t)$ kirjeldab kapitali. Aastastatud geomeetriline tootlus kuiste andmete korral on $CAGR=(W_n/W_0)^{12/n}-1$. Kood eeldab ligikaudu võrdse pikkusega kuuperioode; täpne päevapõhine annualiseerimine oleks teine konventsioon.

Valimi dispersioon on $s^2=\sum(r_t-\bar r)^2/(n-1)$ ja standardhälve $s=\sqrt{s^2}$. Päevase kõikumise korrutamine $\sqrt{252}$-ga eeldab ligikaudset ajaskaleerimist; autokorrelatsiooni, paksude sabade ja muutuva volatiilsuse puhul ei kirjelda see kõiki riske.

## Sharpe ja langus

Kuiste ületootluste $x_t=r_t-r_{f,t}$ Sharpe on $\sqrt{12}\bar x/s_x$. Kui keskmine kuine ületootlus on 1% ja standardhälve 4%, on Sharpe $\sqrt{12}\cdot0.01/0.04\approx0.866$. Python: `np.sqrt(12)*.01/.04`. Meie demo kasutab $r_f=0$; päriskatses tuleb raha tootlus ja riskivaba võrdlus järjekindlalt valida.

Langus tipust $DD_t=W_t/\max_{u\le t}W_u-1$ võrdleb kapitali senise tipuga. Tee 100 → 120 → 90 → 108: suurim langus on −25%, kuigi lõppväärtus on algusest kõrgem. Koodi maksimum sisaldab algkapitali 1; muidu jääks esimese perioodi kahju märkamata. Kuiste punktide langus ei mõõda kuu sees juhtunut.

## Regressioon ja alpha

Turumudelis $r_p-r_f=\alpha+\beta(r_m-r_f)+\epsilon$ mõõdab beeta turu suhtes tundlikkust, alpha mudeliga seletamata keskmist. [NÄIDE] Kui $\beta=1.2$, turu ületootlus on 5% ja portfelli ületootlus 6%, on prognoositud alpha 0, mitte 1%. Tegelik hinnang vajab mitut vaatlust ja jääkide kontrolli. Python-näide `python/matemaatika.py` kontrollib lihtsat lineaarset seost; põhiraport faktoralphat ei hinda.

## Statistiline olulisus

Nullhüpotees võib olla: strateegia ja baasi netotootluste oodatav vahe on null. P-väärtus ei ole nullhüpoteesi tõesuse tõenäosus. Vahemik nulli ümber ei tõesta võrdsust; see võib väljendada vähest infot. Me kasutame paarisvahesid samadel kuudel, sest eraldi portfellide võrdlus kaotaks ühise turuliikumise info.

Ringplokk-bootstrap valib järjestikuste kuude lõike ning lubab lõpu järel algusesse minna. Kolme kuu plokk on õpetuslik valik, mitte tõend optimaalsetest eeldustest. Korda lisaharjutuses 1, 3 ja 6 kuu plokkidega ning vaata, kui palju vahemik muutub. Ükski neist ei korrigeeri automaatselt sadade proovitud strateegiate valikut.

## Kuluarvestus

Olgu $v$ tehingueelne triivinud kaaluvektor, $w$ kulujärgne sihtkaal ja $c$ kulu ühe kaubeldud rahaühiku kohta. NAV-i kulufraktsioon $k$ lahendab $k=c\sum_i|(1-k)w_i-v_i|$. Netotootlus on $(1-k)(1+w^Tr)-1$. Kood leiab $k$ fikspunkti iteratsiooniga. Raha ei käsitleta eraldi tasulise tehinguinstrumendina.

[NÄIDE] Nullist ühe vara 100% positsiooni ostul $k=c/(1+c)$. Kui $c=0.001$, on kulu umbes 0,0999%. See on lähedane 0,1%-le, kuid täpne arvestus väldib mitmetähenduslikkust. Maksud, finantseerimine ja lõplik likvideerimine pole mudelis.


Edasi: [praktikum](praktikum.md) · [ülesanded](ulesanded-lahendused.md)
