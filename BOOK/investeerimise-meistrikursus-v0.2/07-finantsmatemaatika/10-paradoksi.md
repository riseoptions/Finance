# 10 matemaatilist paradoksi ja vastuintuitiivset tulemust

[Tagasi avalehele](../README.md) · [Matemaatika alus](README.md)

Need on originaalsed õpetlikud näited, mitte tegelike väärtpaberite tootlused. Iga tulemus sõltub välja toodud eeldustest.

| # | Näiliselt üllatav tulemus | Arvutus ja tähendus | Kontroll |
|---|---|---|---|
| 1 | −50% taastamiseks on vaja +100% | 100→50→100. Baas kahanes poole võrra; 50/50=100%. | Ülesanne 3 kasutab 35% kahjumit |
| 2 | Nulline keskmine võib anda kahjumi | +20%, −20%: keskmine 0%, aga 1.2×0.8−1=−4%. | Lühinäide 4 |
| 3 | Kahe riskantse vara kombinatsioon võib olla vähem kõikuv | Mõlemad σ=20%, ρ=0, w=50/50: σp=14.14%. | Ülesanne 22 |
| 4 | 90% võite võib tähendada negatiivset ootust | 0.9×1−0.1×20=−1.1. Sagedus ei asenda kahju suurust. | Ülesanne 31 |
| 5 | Indeks võib jõuda algusesse, 2× päevatoode jääda miinusesse | +10%, −9.0909%: indeks 0%, ideaalne päevane 2× −1.8182%. | Lühinäide 16 |
| 6 | Sama 2× toode võib ületada kahekordset kogutootlust | +10%, +10%: indeks 21%, päevane 2× 44%, lihtne kordaja 42%. | Põhimõte 30 |
| 7 | Nulline volatiilsus võib kaasneda kindla kaotusega | Iga periood −1%: standardhälve 0; kümne perioodi kapital 0.99^10≈0.9044. | Põhimõte 42 |
| 8 | Sama VaR võib peita väga erinevat kahju | Labori kahel jaotusel VaR −0.5%, kuid ES 15.9% ja 63.9%. | Labor 3 |
| 9 | Täpne positiivne test ei pruugi tähendada tõenäoliselt head mudelit | Eelnev headus 10%, tundlikkus 80%, valepositiivsus 20%: posterior 30.77%. | Ülesanne 32 |
| 10 | Positiivne portfelli kasv võib kaasneda negatiivse eurotootlusega | Dollarivara +10%, dollar eurodes −10%: 1.1×0.9−1=−1%. | Ülesanne 6 |

## Miks need pole tegelikud vastuolud?

Kõigis näidetes on eksiv intuitsioon jätnud midagi välja: muutuva protsendibaasi, jaotuse saba, tingimusliku tõenäosuse, koosliikumise või mõõtühiku. Matemaatika ei muuda rahandust maagiliseks; see sunnib täpsustama, mida tegelikult võrreldakse.

## Harjutus õpetamiseks

Vali tabelist üks näide. Näita esmalt ainult esimest kahte veergu ning palu õppijal tulemust ennustada. Seejärel ava arvutus. Lõpuks palu muuta üht arvu nii, et tulemus pöörduks, või põhjendada, miks seda antud eeldustel teha ei saa.

**Süvendus võimenduse kohta:** kahe perioodi konstantse päevavõimenduse L korral on vahe võimendatud kogutootluse ja L-kordse alusvara kogutootluse vahel $L(L-1)r_1r_2$. Sama tootluste kogumi järjekorra vahetamine ei muuda nende tegurite korrutist. Seega „teekonnasõltuvus” ei tähenda selles lihtmudelis, et iga permutatsioon muudab lõppväärtust; see tähendab, et üksnes alusvara alg- ja lõpphind ei määra võimendatud tulemust. Rahavood, muutuv võimendus ja sundmüük võivad teha ka järjekorra oluliseks.
