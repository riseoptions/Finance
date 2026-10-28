# Labor 1. Kas eilne parim fond on ka homme parem?

[Õppekava](../00-oppekava.md) · [Kood](../python/01_fondivoitjad.py) · [Tulemused](../tulemused/01.json) · [Lahendused](lahendused.md)

## Sisukord

- [Kiirtase](#kiirtase)
- [Mõisted ja matemaatika](#mõisted-ja-matemaatika)
- [Katse ja tulemus](#katse-ja-tulemus)
- [Kriitiline analüüs](#kriitiline-analüüs)
- [Pärisandmetega uurimine](#pärisandmetega-uurimine)
- [Harjutused ja arutelu](#harjutused-ja-arutelu)

## Kiirtase

**[ANALÜÜS] Kõrge ajalooline tootlus on vaatlus. Hea investeerimisoskus on üks selle võimalikest seletustest.**

Õpieesmärk: oskad selgitada võitja valimise kallutatust, kasutada eraldi kontrollperioodi ning eristada tõendite puudumist tõendist, et oskust ei ole.

[SCHWAGER] Peatükk 3 uurib tugevatele ja nõrkadele tootlusperioodidele järgnevaid tulemusi; peatükid 6–8 käsitlevad ajaloolise tulemuslikkuse hindamise lõkse. [PAPP] Peatükid 4 ja 11 seovad investeerimisteesi ning strateegia hindamise andmeanalüüsiga. Käesolev labor on originaalne simulatsioon, mitte kummagi raamatu uuringu kordus.

[NÄIDE] 500 võrdselt võimekast fondist on üks viie aasta lõpus parim ka siis, kui mitte kellelgi pole eelist. Talle auhinna andmine ei loo uut infot tema tulevase eelise kohta, kui mudelis eelist ei eksisteeri.

## Mõisted ja matemaatika

- **Lihttootlus** (*simple return*): $r_t=P_t/P_{t-1}-1$, kui rahavoogusid ei ole.
- **Logtootlus** (*log return*): $g_t=\ln(1+r_t)$.
- **CAGR**: geomeetriline keskmine aastane kasvutempo, $(V_T/V_0)^{1/T}-1$.
- **Valikukallutatus** (*selection bias*): tulemus muutub eksitavaks, kui vaadeldava fondi valik sõltub samast tulemusest, millega tema headust põhjendad.
- **Kontrollperiood** (*out-of-sample*): periood, mida valikureegel ei saanud kasutada.

[MUDEL] Fondi $i$ aastane logtootlus on

$$g_{i,t}=\mu+a_i+\varepsilon_{i,t},\qquad \varepsilon_{i,t}\sim N(0,\sigma^2).$$

Valime $\mu=0.06$, $\sigma=0.18$, 500 fondi ja kaks viieaastast perioodi. Kõik vead on sõltumatud üle fondide ja aja. Oskus $a_i$ on kummaski perioodis sama. Esimeses katses on kõik $a_i=0$, teises on $a_i\sim N(0,0.04^2)$.

Viie aasta keskmine logtootlus on tingimuslikult normaaljaotusega:

$$\bar g_i\mid a_i\sim N(\mu+a_i,\sigma^2/5).$$

Seetõttu võib kood simuleerida otse perioodi keskmise. CAGR on $e^{\bar g_i}-1$. Üksikuid aastaradu pole selle küsimuse jaoks vaja, kuid ilma nendeta ei saa arvutada maksimaalset langust.

Treeningperioodi võitja indeks on $i^*=\arg\max_i\bar g_{i,\mathrm{enne}}$. Kui kõik oskused on null ja järgmine periood sõltumatu, ei anna see indeks uut infot järgmise perioodi tootluse kohta. Oodatav järgmise perioodi CAGR on sama mis suvalisel fondil:

$$E[\mathrm{CAGR}]=e^{\mu+\sigma^2/(2T)}-1\approx6.53\%.$$

See pole täpselt $e^{0.06}-1$ ega 6%: mittelineaarse teisenduse keskmine ja keskmise teisendus erinevad.

## Katse ja tulemus

Käivita skript. Seeme on `20261028`, katset korratakse 1000 sõltumatus simulatsioonimaailmas. Igas maailmas valitakse ainult esimese perioodi põhjal üks võitja.

| Mudel | Võitja varasem CAGR, keskmine | Võitja järgmine CAGR, keskmine | Järgmise CAGR-i vahe fondide keskmisega |
|---|---:|---:|---:|
| Kõigil sama oskus | 35.50% | 6.21% | −0.32 protsendipunkti |
| Püsiv oskuste erinevus | 39.53% | 12.49% | +5.87 protsendipunkti |

Esimese mudeli vahe Monte Carlo ligikaudne 95% vahemik on **−0.83 kuni +0.19 protsendipunkti**. Null mahub vahemikku. Teise mudeli vahemik on **+5.24 kuni +6.50 protsendipunkti**.

Vahemik on korduste keskmise simulatsioonivea hinnang valitud mudelis. See pole tegeliku fondijuhi oskuse usaldusvahemik ega ühe tulevase viieaastase perioodi prognoosivahemik. Kood võrdleb CAGR-e fondide aritmeetilise keskmisega; see võrdlusnäitaja pole automaatselt reaalselt investeeritava rebalanseeritava fondiportfelli tootlus.

## Kriitiline analüüs

**Mida katse näitab?** Ilma oskuseta võib varasem võitja välja näha erakordselt hea. Kui mudel sisaldab püsivaid oskuste erinevusi, võib minevikutootlus ometi sisaldada kasulikku infot. Seega ei toeta labor absoluutset väidet, et minevik ei ütle kunagi midagi.

**Mida katse ei näita?** See ei mõõda päris fondijuhtide oskust ega tõesta, et reaalsed fondid käituvad sõltumatult. Mudelis puuduvad tasud, ühised turufaktorid, oskuse kadumine, fondide sulgemine ja võimekuse sõltuvus fondi suurusest. 4-protsendipunktiline oskuse hajuvus on valitud õpetlik parameeter, mitte turult hinnatud suurus.

**Matemaatiliselt põhjendatud täpsustus.** Tulevane ootus pärast äärmuslikku vaatlust võib olla keskmisele lähemal ilma, et turul eksisteeriks hinna tagasipöördumise kauplemisstrateegia. Siin tuleb efekt valikust ja sõltumatust mürast.

## Pärisandmetega uurimine

Uurimisküsimus: kas varem parima tootlusega fondide rühm ületab järgmisel perioodil sama riskiprofiiliga fonde pärast tasusid?

1. Määra fondide kategooria ja esimene valikukuupäev enne tulemuste vaatamist.
2. Kasuta ajaloolist fondide universumit koos lõpetanud ja liidetud fondidega. Tänased ellujäänud ei ole piisav valim.
3. Hoia ühe fondi osakuklassid eraldi kontrolli all, et sama strateegia ei saaks kümmet häält.
4. Arvuta dividende arvestav kogutootlus samas valuutas ja samadel kuupäevadel. Dokumenteeri tasude sisaldumine.
5. Vali fondid eelneva viie aasta põhjal; mõõda järgmise perioodi tulemus ilma valikureeglit tagantjärele muutmata.
6. Võrdle sama kategooria võrdlusindeksi ja riskifaktoritega. Kõrge beetaga fondi tõusuturu edu ei ole automaatselt alfa.
7. Kasuta mitut ajalist lõiget. Kattuvaid perioode ja ühist tururiski ei tohi lugeda sõltumatuteks katseteks; kasuta sõltuvust arvestavat meetodit, näiteks ajaplokkide bootstrap'i.
8. Avalda ka valikureegli ebaõnnestumised ning alternatiivsete proovitud reeglite arv.

Selles versioonis pole sellist fondiandmestikku hangitud ega uuringut tehtud.

## Harjutused ja arutelu

1. Muuda fondide arv 500-lt 20-le. Ennusta enne käivitust, kuidas muutub varasema võitja tulemus. Kas nulloskusega mudelis peaks tema tulevane ootus muutuma?
2. Muuda oskuse hajuvus nullist 0.04-ni. Miks võib järgmise perioodi eelis tekkida?
3. Selgita, miks 35.50% minevikutootluse ja 6.21% tulevikutootluse vahe ei tõesta konkreetse tegeliku fondijuhi ebapädevust.

**Väitlusküsimus:** „Valin fondi, mis oli viie aasta jooksul parim.” Poolt: püsiva oskuse korral võib tulemus infot sisaldada. Vastu: sama tulemus võib pärineda juhusest, suurest riskist või valikukallutatusest. Kontrolli universumit, tasusid ja riskiprofiili.

**Foorumivastus:** „Varasem esikoht on põhjus fondi lähemalt uurida. Oskuse tõendamiseks vajame võrdlust sama riskiga alternatiividega ja tulemust perioodil, mida valimisel ei kasutatud.”
