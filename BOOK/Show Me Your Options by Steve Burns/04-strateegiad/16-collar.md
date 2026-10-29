# Collar

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 15; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

Osta/hoia 100 aktsiat hinnaga 100 USD.

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Osta put | 1 | 95 | 3 |
| Müü call | 1 | 105 | 3 |

Algne netoväljaminek koos aktsiatega: **10000,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Aktsia tulevase müügihinna vahemiku piiramine; ostetud put’i rahastab call’i müük.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **500,00 USD**.
- Maksimaalne kahju: **500,00 USD**.
- Tasuvuspiir(id) tähtajal: **100,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `S + P(95) − C(105)`. P/L: `S + P(95) − C(105) − 100,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | 95,00 | -5,00 | -500,00 |
| 80 | 95,00 | -5,00 | -500,00 |
| 90 | 95,00 | -5,00 | -500,00 |
| 95 | 95,00 | -5,00 | -500,00 |
| 100 | 100,00 | 0,00 | 0,00 |
| 105 | 105,00 | 5,00 | 500,00 |
| 110 | 105,00 | 5,00 | 500,00 |
| 120 | 105,00 | 5,00 | 500,00 |
| 130 | 105,00 | 5,00 | 500,00 |

![Collar: terminalväljamakse ja P/L](../pildid/16-collar.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Positiivne piiratud delta; netovega/theta sõltuvad mõlemast strike’ist. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Null netopreemiat ei tähenda tasuta kaitset: loovutad tõusu üle 105. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Protective put säilitab kogu tõusu, kuid maksab rohkem.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Aktsia tulevase müügihinna vahemiku piiramine; ostetud put’i rahastab call’i müük. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Null netopreemiat ei tähenda tasuta kaitset: loovutad tõusu üle 105.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** 0,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** 500,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 500,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
