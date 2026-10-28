# Labor 3. Sama VaR, väga erinev kahjurisk

[Õppekava](../00-oppekava.md) · [Kood](../python/03_varjatud_risk.py) · [Tulemused](../tulemused/03.json) · [Lahendused](lahendused.md)

## Sisukord

- [Kiirtase](#kiirtase)
- [Matemaatiline vastunäide](#matemaatiline-vastunäide)
- [Mida teeb kood?](#mida-teeb-kood)
- [Ka ES võib jääda pimedaks](#ka-es-võib-jääda-pimedaks)
- [Seos raamatute ja pärisandmetega](#seos-raamatute-ja-pärisandmetega)
- [Harjutused ja väitlus](#harjutused-ja-väitlus)

## Kiirtase

**[ANALÜÜS] Riskimõõdik vastab ühele määratletud küsimusele, mitte kõigile küsimustele võimaliku kahju kohta.**

Õpieesmärk: oskad defineerida VaR-i, arvutada diskreetse jaotuse ES-i ning eristada mõõdiku piirangut andmete ja mudeli piirangust.

[SCHWAGER] Peatükk 4 rõhutab riske, mis ei pruugi senises tootlusreas ilmneda. [PAPP] Peatükk 7.2.1 näitab normaaljaotusest simuleeritud tootluste abil VaR-i arvutamist. Siinne labor uurib, mis juhtub, kui harvad kahjud muudavad jaotuse kuju.

## Matemaatiline vastunäide

[MUDEL] Tootlus $R$ on kasum positiivse märgiga; kahju $L=-R$ on kahjum positiivse märgiga. Kuu võimalikud tulemused on:

| Tõenäosus | Strateegia A tootlus | Strateegia B tootlus |
|---|---:|---:|
| 96% | +0.5% | +0.5% |
| 4% | −20% | −80% |

Need on väljamõeldud jaotused. Neid ei ole hinnatud konkreetse fondi ajaloost.

Kahjujaotuse VaR on kvantiil:

$$\operatorname{VaR}_{\alpha}(L)=\inf\{l:F_L(l)\ge\alpha\}.$$

Mõlema strateegia 95% VaR on **−0.5%**. Miinus tähendab siin kasumit, mitte trükiviga. Kõige väiksem kahju tase, milleni on kogunenud vähemalt 95% tõenäosust, on −0.5%. Mõnes riskiraportis lõigatakse negatiivne VaR nulliks; sel juhul oleks mõlema näitaja null. Kumbki esitlus ei näita 4% harude kahju suurust.

**VaR ei ole maksimaalne võimalik kahju.** VaR-i ületavate kahjude suurus võib muutuda, ilma et antud usaldusnivoo VaR muutuks.

Expected shortfall ehk halvima saba keskmine kahju on üldiselt:

$$\operatorname{ES}_{\alpha}(L)=\frac{1}{1-\alpha}\int_{\alpha}^1\operatorname{VaR}_u(L)\,du.$$

Halvima 5% tõenäosusmassist moodustab siin 4% krahh ja 1% tavapärane +0.5% kasum. Seega:

$$\operatorname{ES}_{0.95}(A)=\frac{0.04\cdot0.20+0.01\cdot(-0.005)}{0.05}=15.9\%,$$

$$\operatorname{ES}_{0.95}(B)=\frac{0.04\cdot0.80+0.01\cdot(-0.005)}{0.05}=63.9\%.$$

Diskreetse jaotuse korral ei tohi ES-i pimesi asendada avaldisega $E[L\mid L\ge\operatorname{VaR}]$: kvantiili juures olev suur tõenäosusmass muudab selle siin valeks. Kood kaasab piiril olevast massist täpselt vajaliku osa.

## Mida teeb kood?

Funktsioon `risk` järjestab kahjud, leiab jaotusfunktsiooni põhjal kvantiili ning arvutab kvantiiliintegraali. Väljund:

| Mõõdik | A | B |
|---|---:|---:|
| Kuu 95% VaR | −0.5% | −0.5% |
| Kuu 95% ES | 15.9% | 63.9% |
| Oodatav kuutootlus | −0.32% | −2.72% |

Ka 96% kasumlike kuude osakaal ei tõesta positiivset oodatavat tootlust. Sagedus ja suurus tuleb koos arvesse võtta.

## Ka ES võib jääda pimedaks

Oletame nüüd, et mudeli kuud on sõltumatud ja 60 kuu ajalukku ei satu ühtegi krahhi. Sellise ajaloo tõenäosus on:

$$P(\text{60 kuud krahhita})=0.96^{60}\approx8.64\%.$$

Kui analüütik näeb ainult seda ajalugu ning kasutab empiirilist jaotust, on nii VaR kui ES −0.5% ja ajalooline standardhälve null. Tegelikus eeldatud mudelis on suur kahjurisk endiselt olemas. Täpsema mõõdiku kasutamine ei tekita puuduvat sündmust andmetesse.

Siin on kolm eri probleemi:

1. **Mõõdik:** VaR ei kirjelda, kui suur on kahju kvantiilist kaugemal.
2. **Valim:** ajalugu ei pruugi sisaldada olulist riskisündmust.
3. **Mudel:** näiteks normaaljaotuse eeldus võib harvaesinevat kahju valesti kirjeldada.

**Vastunäide liiga tugevale kriitikale:** kui tõeline jaotus on piisavalt hästi kirjeldatud, võib VaR olla kasulik lävend või limiidi mõõdik. Selle piirangute näitamine ei tähenda, et mõõdik oleks alati kasutu. Ka ES pole automaatne lahendus likviidsus-, vastaspoole- ega mudeliriskile.

## Seos raamatute ja pärisandmetega

[TÄIENDUS] Baseli komitee 2012. aasta kauplemisportfelli raamistiku konsultatsioon esitas ülemineku VaR-ilt ES-ile ühe põhjendusena sabariski parema arvestamise. See on ajalooline metoodiline viide, mitte selles kursuses antav 2026. aasta Eesti õigusnõu. [Allikas](https://www.bis.org/publications/201205-consultation-fundamental-review-trading-book).

[ANALÜÜS] Pappi normaalse Monte Carlo näite käivitamine kontrollib mudeli arvutust. Et kontrollida mudeli asjakohasust, tuleb lisada jaotuse diagnostika ja mudelist sõltumatud stressid. Suurem simulatsioonide arv vähendab valitud jaotuse Monte Carlo müra; see ei paranda automaatselt valet jaotust.

Pärisandmetega jätkamiseks vali strateegia koos majandusliku kirjeldusega. Arvuta ajalooline VaR ja ES; võrdle normaalmudeliga; testi ette määratud šokke, likviidsuse kadumist ning võimenduse mõju. VaR-i taganttestis loe ületamisi ning uuri nende koondumist. Harvade sündmuste korral võib valim olla otsustamiseks liiga väike. Portfelli VaR-i ei saa üldjuhul saada üksikpositsioonide VaR-ide lihtsa liitmisega; vaja on ühist kahjujaotust.

## Harjutused ja väitlus

1. Kui suur on 10 000 euro suuruse positsiooni mudelipõhine 95% ES kummalgi strateegial?
2. Miks ei võrdu A ES 20%-ga?
3. Leia mõlema strateegia 99% VaR ja ES.
4. Millise arutlusvea teeb inimene, kes ütleb: „Viie aasta jooksul pole kahju olnud, järelikult on strateegia ohutu”?

**Väitlusküsimus:** „Madal VaR tõendab, et fond on turvaline.” Poolt: õigesti hinnatud VaR annab infot kindla ajahorisondi kahjulävendi kohta. Vastu: ei näita saba suurust ega garanteeri mudeli kehtivust. Kontrolli jaotust, positsioonide majanduslikku sisu ja stressi.

**Foorumivastus:** „Kõigepealt täpsustaksin VaR-i ajahorisondi, usaldusnivoo ja arvutusmeetodi. Seejärel küsiksin, kui suur võib kahju olla lävendi ületamisel ning kas ajaloo jooksul on strateegia peamine risk üldse avaldunud.”
