# Iron butterfly (credit)

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 13; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Osta put | 1 | 90 | 2 |
| Müü put | 1 | 100 | 6 |
| Müü call | 1 | 100 | 6 |
| Osta call | 1 | 110 | 2 |

Algne netoväljaminek koos aktsiatega: **-800,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Krediidiga panus hinna lõppemisele 100 lähedal; straddle’i riskile lisatakse tiivad.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **800,00 USD**.
- Maksimaalne kahju: **200,00 USD**.
- Tasuvuspiir(id) tähtajal: **92,00; 108,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `0 + P(90) − P(100) − C(100) + C(110)`. P/L: `0 + P(90) − P(100) − C(100) + C(110) + 8,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | -10,00 | -2,00 | -200,00 |
| 80 | -10,00 | -2,00 | -200,00 |
| 90 | -10,00 | -2,00 | -200,00 |
| 95 | -5,00 | 3,00 | 300,00 |
| 100 | 0,00 | 8,00 | 800,00 |
| 105 | -5,00 | 3,00 | 300,00 |
| 110 | -10,00 | -2,00 | -200,00 |
| 120 | -10,00 | -2,00 | -200,00 |
| 130 | -10,00 | -2,00 | -200,00 |

![Iron butterfly (credit): terminalväljamakse ja P/L](../pildid/19-iron-butterfly.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Keskel sageli negatiivne gamma/vega ja positiivne theta. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Kasumi tipp on kitsas; mõlema short-jala täitmisriski peab juhtima. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Long call butterfly sarnase terminalkujuga.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Krediidiga panus hinna lõppemisele 100 lähedal; straddle’i riskile lisatakse tiivad. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Kasumi tipp on kitsas; mõlema short-jala täitmisriski peab juhtima.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** 800,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** -200,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 200,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
