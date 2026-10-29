# Long straddle

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 10; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Osta call | 1 | 100 | 6 |
| Osta put | 1 | 100 | 6 |

Algne netoväljaminek koos aktsiatega: **1200,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Suur liikumine kummas tahes suunas, piisavalt kiiresti või koos IV tõusuga.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **Piiramatu USD**.
- Maksimaalne kahju: **1200,00 USD**.
- Tasuvuspiir(id) tähtajal: **88,00; 112,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `0 + C(100) + P(100)`. P/L: `0 + C(100) + P(100) − 12,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | 100,00 | 88,00 | 8800,00 |
| 80 | 20,00 | 8,00 | 800,00 |
| 90 | 10,00 | -2,00 | -200,00 |
| 95 | 5,00 | -7,00 | -700,00 |
| 100 | 0,00 | -12,00 | -1200,00 |
| 105 | 5,00 | -7,00 | -700,00 |
| 110 | 10,00 | -2,00 | -200,00 |
| 120 | 20,00 | 8,00 | 800,00 |
| 130 | 30,00 | 18,00 | 1800,00 |

![Long straddle: terminalväljamakse ja P/L](../pildid/12-straddle.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Algdelta võib olla nulli lähedal, gamma/vega positiivsed, theta sageli negatiivne. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Mõlema õiguse eest makstakse. Pelgalt aktiivne hinnaliikumine ei taga kasumit. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Ühepoolne call/put, kui suunavaade on põhjendatud.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Suur liikumine kummas tahes suunas, piisavalt kiiresti või koos IV tõusuga. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Mõlema õiguse eest makstakse. Pelgalt aktiivne hinnaliikumine ei taga kasumit.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** -1200,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** 800,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 1200,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
