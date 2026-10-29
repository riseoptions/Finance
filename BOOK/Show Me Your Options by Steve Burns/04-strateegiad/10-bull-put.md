# Bull put spread (credit)

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 12; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Müü put | 1 | 100 | 6 |
| Osta put | 1 | 90 | 2 |

Algne netoväljaminek koos aktsiatega: **-400,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Krediit, kui hind püsib piisavalt kõrgel; mõõdukalt tõusev vaade.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **400,00 USD**.
- Maksimaalne kahju: **600,00 USD**.
- Tasuvuspiir(id) tähtajal: **96,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `0 − P(100) + P(90)`. P/L: `0 − P(100) + P(90) + 4,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | -10,00 | -6,00 | -600,00 |
| 80 | -10,00 | -6,00 | -600,00 |
| 90 | -10,00 | -6,00 | -600,00 |
| 95 | -5,00 | -1,00 | -100,00 |
| 100 | 0,00 | 4,00 | 400,00 |
| 105 | 0,00 | 4,00 | 400,00 |
| 110 | 0,00 | 4,00 | 400,00 |
| 120 | 0,00 | 4,00 | 400,00 |
| 130 | 0,00 | 4,00 | 400,00 |

![Bull put spread (credit): terminalväljamakse ja P/L](../pildid/10-bull-put.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Positiivne delta; sageli theta-positiivne turvalisemas hinnapiirkonnas, mitte igal pool. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Krediit pole maksimaalne risk: kahju on strike’ide vahe miinus krediit. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Sama strike’ide bull call spread koos rahastuse võrdlusega.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Krediit, kui hind püsib piisavalt kõrgel; mõõdukalt tõusev vaade. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Krediit pole maksimaalne risk: kahju on strike’ide vahe miinus krediit.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** 400,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** 400,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 600,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
