# Long call butterfly

[Atlas](README.md) · [Riskijuhtimine](../05-riskijuhtimine/oppetukk.md)

[RAAMAT] Teemaseos: peatükk 13; täpsed PDF-vahemikud on [kaardil](../00-oppekava.md). [NÄIDE] Kõik allolevad hinnad ja tulemused on kursuse enda arvutused.

## 1. Koosseis

| Jalg | Kogus | Strike | Preemia ühiku kohta |
|---|---:|---:|---:|
| Osta call | 1 | 90 | 12 |
| Müü call | 2 | 100 | 6 |
| Osta call | 1 | 110 | 2 |

Algne netoväljaminek koos aktsiatega: **200,00 USD**; negatiivne number tähendab krediiti.

## 2. Eesmärk ja 3. turuvaade

Hind lõpeb keskmise strike’i lähedal; piiratud kuluga keskpiirkonna panus.

## 4. Millal kaaluda ja lihtne analoogia

[ANALOOGIA] Mõtle igast ostetud jalast kui õiguse ostmisest ja müüdud jalast kui võõrale antud valikust. Kogu pakett peab teenima kirjeldatud eesmärki. Piirang: ükski jalg ei tunne teise olemasolu; varajane täitmine võib neid ajaliselt lahutada. Kontrolli enne, kas sama eesmärk on saavutatav lihtsamalt.

## 5. Kasum, 6. kahjum ja 7. tasuvuspiir

- Maksimaalne kasum: **800,00 USD**.
- Maksimaalne kahju: **200,00 USD**.
- Tasuvuspiir(id) tähtajal: **92,00; 108,00 USD**.

[MATEMAATIKA] Payoff ühe ühiku kohta: `0 + C(90) − 2×C(100) + C(110)`. P/L: `0 + C(90) − 2×C(100) + C(110) − 2,00`. Siin C ja P tähendavad lõpptähtaja sisemisi väärtusi, mitte tänaseid preemiaid.

| S tähtajal | Payoff ühiku kohta | P/L ühiku kohta | P/L kogu kombinatsioonile |
|---:|---:|---:|---:|
| 0 | 0,00 | -2,00 | -200,00 |
| 80 | 0,00 | -2,00 | -200,00 |
| 90 | 0,00 | -2,00 | -200,00 |
| 95 | 5,00 | 3,00 | 300,00 |
| 100 | 10,00 | 8,00 | 800,00 |
| 105 | 5,00 | 3,00 | 300,00 |
| 110 | 0,00 | -2,00 | -200,00 |
| 120 | 0,00 | -2,00 | -200,00 |
| 130 | 0,00 | -2,00 | -200,00 |

![Long call butterfly: terminalväljamakse ja P/L](../pildid/14-butterfly.png)

Graafik näitab hinnavahemikku 70–130; tabeli S=0 rida näitab languse äärmust. Piiramatu risk või kasum jätkub graafiku servast edasi.

## 8. Aeg ja volatiilsus

Keskme lähedal sageli negatiivne gamma/vega ja positiivne theta; tiibadel võivad märgid pöörduda. Enne tähtaega tuleb positsiooni väärtus arvutada kõigi jalgade hetkehinnast; terminaltasuvuspiir ei ole kohustuslik tingimus vahepealse kasumi jaoks.

## 9. Riskid ja levinud viga

Kõrge keskpunkti kasum ei tähenda suurt tõenäosust sinna jõuda. Neli lepingut tekitavad kulusid. Üldine viga on võrrelda ainult saadud preemiat, jättes tähelepanuta netokapitali ja äärmise stsenaariumi.

## 10. Lihtsam alternatiiv

Laiem condor või tehingust loobumine.

## 11. Selgita algajale ühe minutiga

Alusta eesmärgist: Hind lõpeb keskmise strike’i lähedal; piiratud kuluga keskpiirkonna panus. Seejärel loe koosseisust ette, millised õigused ostad ja millised kohustused müüd. Võta tabelist hind 100 ja hind 120 ning näita mõlema jala panust. Ütle eraldi algne rahavoog ja lõpptulemus. Lõpeta piiranguga: Kõrge keskpunkti kasum ei tähenda suurt tõenäosust sinna jõuda. Neli lepingut tekitavad kulusid.

## Meelespea

[PÕHIMÕTE] Liida kõik jalad enne hinnangu andmist. Preemia muudab P/L-i, mitte lepingu väljamakse reeglit. Kasumi ülempiir ei ütle midagi kahjumi ülempiiri kohta.

## Kolm küsimust vastustega

1. **Mis on tulemus S=100 korral?** 800,00 USD: asenda S valemis 100-ga ja korruta 100-ga. Viga oleks algne rahavoog unustada.
2. **Mis on tulemus S=120 korral?** -200,00 USD. See kontrollib, kas arvestasid müüdud call’ide kohustust ja võimalikke aktsiaid.
3. **Kas 200,00 USD tähendab igal hetkel just nii suurt rahavajadust?** Ei. See on terminalmudeli kahjupiir (või piiramatus); tagatis, varajane assignment ja aktsiate üleandmine vajavad eraldi kontrolli.
