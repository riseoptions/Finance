# Covered call

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 7; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

Osta/hoia 100 aktsiat hinnaga 100 USD.

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Müü call | 1 | 105 | 3 |

Algne netoväljaminek koos aktsiatega: **9700,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Olemasoleva 100 aktsia tõusupotentsiaali osaline loovutamine preemia eest. Sobib analüüsiks, kui ollakse valmis aktsiaid strike’iga müüma.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **800,00 USD**.
- Maksimaalne kahju: **9700,00 USD**.
- Tasuvuspiir(id) tähtajal: **97,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `S − C(105)`. P/L: `S − C(105) − 97,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | 0,00 | -97,00 | -9700,00 |
| 80 | 80,00 | -17,00 | -1700,00 |
| 90 | 90,00 | -7,00 | -700,00 |
| 95 | 95,00 | -2,00 | -200,00 |
| 100 | 100,00 | 3,00 | 300,00 |
| 105 | 105,00 | 8,00 | 800,00 |
| 110 | 105,00 | 8,00 | 800,00 |
| 120 | 105,00 | 8,00 | 800,00 |
| 130 | 105,00 | 8,00 | 800,00 |

![Covered call: terminalväljamakse ja P/L](../pildid/05-covered-call.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Kogu delta tavaliselt 0 ja 1 vahel; negatiivne gamma/vega ning sageli positiivne theta. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Aktsia languskahju jääb peaaegu tervikuna alles. Dividendieelne assignment võib lõpetada omamise. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Aktsia hoidmine või collar.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Olemasoleva 100 aktsia tõusupotentsiaali osaline loovutamine preemia eest. Sobib analüüsiks, kui ollakse valmis aktsiaid strike’iga müüma. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Aktsia languskahju jääb peaaegu tervikuna alles. Dividendieelne assignment võib lõpetada omamise.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** 300,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** 800,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 9700,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
