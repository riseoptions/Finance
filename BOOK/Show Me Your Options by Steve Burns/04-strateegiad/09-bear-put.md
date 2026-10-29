# Bear put spread (debit)

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 12; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Osta put | 1 | 110 | 12 |
| Müü put | 1 | 100 | 6 |

Algne netoväljaminek koos aktsiatega: **600,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Mõõdukas langusootus piiratud kahjumiga.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **400,00 USD**.
- Maksimaalne kahju: **600,00 USD**.
- Tasuvuspiir(id) tähtajal: **104,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `0 + P(110) − P(100)`. P/L: `0 + P(110) − P(100) − 6,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | 10,00 | 4,00 | 400,00 |
| 80 | 10,00 | 4,00 | 400,00 |
| 90 | 10,00 | 4,00 | 400,00 |
| 95 | 10,00 | 4,00 | 400,00 |
| 100 | 10,00 | 4,00 | 400,00 |
| 105 | 5,00 | -1,00 | -100,00 |
| 110 | 0,00 | -6,00 | -600,00 |
| 120 | 0,00 | -6,00 | -600,00 |
| 130 | 0,00 | -6,00 | -600,00 |

![Bear put spread (debit): terminalväljamakse ja P/L](../pildid/09-bear-put.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Negatiivne delta; muude kreeklaste netomärk sõltub hinnast ja ajast. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Tugeva languse lisakasu loovutatakse; short put’i assignment nõuab tähelepanu. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Long put.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Mõõdukas langusootus piiratud kahjumiga. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Tugeva languse lisakasu loovutatakse; short put’i assignment nõuab tähelepanu.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** 400,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** -600,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 600,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
