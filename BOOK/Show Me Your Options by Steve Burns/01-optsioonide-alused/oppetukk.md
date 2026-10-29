# I. Optsioonide olemus

[Tagasi](../README.md) · [Järgmine: hind](../02-optsiooni-hind/oppetukk.md)

[RAAMAT] Peatükid 1–3, PDF lk 10–36, vastandavad aktsia omamise ning tingimusliku õiguse ja kohustuse. Peatükk 9 (94–105) käsitleb kaugete OTM-optsioonide väikese hinna ahvatlust.

## 1. Mida peab mõistma?

- Oskad eristada call’i ja put’i ning kummagi ostjat ja müüjat.
- Oskad lugeda alusvara, täitmishinda, tähtaega, kordajat ja arveldusviisi.
- Eristad optsiooni väärtust tehingu kasumist.
- Selgitad, miks put võib olla kindlustus ja call pole aktsia.

## 2. Intuitiivne selgitus

[SELGITUS] Call annab õiguse osta ja put õiguse müüa kokkulepitud hinnaga. Ostja maksab selle valikuvõimaluse eest preemia. Müüja saab preemia ja võtab kohustuse, mille täitmist ta enam lihtsalt ümber otsustada ei saa. Positsiooni saab turul sulgeda, kui leidub vastaspool sobiva hinnaga.

**Ostmine ja müümine ei tähenda alati avamist.** Buy to open loob pika positsiooni; sell to close sulgeb selle. Sell to open loob lühikese positsiooni; buy to close sulgeb selle. Varem ostetud call’i müümine ei tee sind automaatselt katmata call’i kirjutajaks.

## 3. Õpetlik analoogia

[ANALOOGIA] Maksad 3 eurot õiguse eest osta kuu pärast jalgratas 105 euroga. Kui ratta turuhind on 120, on õigus väärt 15. Kui turuhind on 90, jätad õiguse kasutamata. Võrdluse piir: börsilepingul on standardtingimused, tagatised ja võimalik järelturg; poe broneeringul ei pruugi neid olla.

Put sarnaneb müügihinna kindlustusega. Erinevalt tavalisest kahjukindlustusest ei pea standardse put’i väärtuse saamiseks tõendama tegelikku kahjujuhtumit. Put’i võib osta ka ilma aktsiat omamata.

## 4. Kuidas mehhanism töötab?

| Positsioon | Õigus või kohustus füüsilise arvelduse korral | Maksimaalne optsiooni P/L-kahjum | Suurim kasum |
|---|---|---|---|
| Long call | Õigus osta alusvara hinnaga K | Makstud preemia | Teoreetiliselt piiramatu |
| Short call | Assignment’i korral kohustus müüa hinnaga K | Katmata kujul piiramatu | Saadud preemia |
| Long put | Õigus müüa alusvara hinnaga K | Makstud preemia | K miinus preemia, kui S langeb nulli |
| Short put | Assignment’i korral kohustus osta hinnaga K | K miinus preemia, kui S langeb nulli | Saadud preemia |

Tabel eeldab mittenegatiivse hinnaga aktsiat, üht optsiooni alusvaraühiku kohta ja kulude puudumist. Kogu lepingu tulemus saadakse kordajaga M. „Piiratud preemiaga” kirjeldab ostetud optsiooni enne sellest tekkiva aktsiapositsiooni lisariski.

**Exercise** on ostja õiguse kasutamine; **assignment** tähendab müüjale kohustuse määramist. Algne ostja ja algne müüja ei pea isiklikult vastamisi jääma: börsi kliiring korraldab kohustusi.

Ameerika tüüpi optsiooni võib täita enne lõpptähtaega, Euroopa tüüpi üldjuhul ainult tähtajal. Need pole geograafilised nimetused. Euroopa optsiooni võib sageli enne tähtaega turul müüa. Rahalise arvelduse korral vahetatakse lepingu järgi arvutatud raha, mitte aktsiaid. Kontrolli konkreetseid tingimusi [Cboe allikast](../allikad.md).

| Seisund | Call | Put |
|---|---|---|
| ITM ehk rahas | S > K | S < K |
| ATM ehk raha juures | S ligikaudu K | S ligikaudu K |
| OTM ehk rahast väljas | S < K | S > K |

ITM ei tähenda kasumlikku tehingut: sisemine väärtus võib olla väiksem kui makstud hind.

## 5. Lihtne arvuline näide

[NÄIDE] S₀ = 100, K = 105, call’i preemia c = 3, 30 päeva, M = 100.

| S tähtajal | Väljamakse ühe aktsia kohta | P/L ühe aktsia kohta | P/L lepingu kohta |
|---:|---:|---:|---:|
| 90 | 0 | −3 | −300 |
| 100 | 0 | −3 | −300 |
| 105 | 0 | −3 | −300 |
| 110 | 5 | 2 | 200 |
| 120 | 15 | 12 | 1200 |

Hind võib tõusta 100-lt 107-le ja ostja kaotab ikkagi 100 USD: õigus on väärt 200, kuid maksis 300. Call’i ei pea kasumi saamiseks täitma: enne tähtaega võib selle müüa näiteks 4 eest, teenides 100 USD enne kulusid.

## 6. Vajalik matemaatika

[MATEMAATIKA] Tähtajal, ühe alusvaraühiku kohta:

$$C_T=\max(S_T-K,0),\qquad P_T=\max(K-S_T,0).$$

$$\Pi_{LC}=C_T-c,\quad \Pi_{SC}=c-C_T,\quad \Pi_{LP}=P_T-p,\quad \Pi_{SP}=p-P_T.$$

Lepingu P/L = M × ühiku P/L − kulud. Long call’i tasuvuspiir on K+c; long put’il K−p. Need on **tähtaja** piirid. Enne tähtaega võib kasum tekkida neid hindu saavutamata.

Sisemine väärtus = kohese täitmise väärtus. Väline väärtus ehk tavakeeles ajaväärtus = optsiooni turuhind − sisemine väärtus. See sõltub ka IV-st, mitte ainult kalendrist. Euroopa optsioonidel võivad intress ja dividendid muuta kohese täitmise väärtusega võrdluse nüansirikkaks; Euroopa lepingut ei pruugi kohe täita saadagi.

## 7. Praktiline kasutamine

Aktsiaomanik ostab put’i, et piirata languskahjumit. Tõusule panustaja ostab call’i, et panna eelnevalt paika optsiooni eest kaotatav summa. Tulu sooviv müüja peab esmalt suutma kanda vastavat ostu- või müügikohustust. Ükski eesmärk ei tõesta, et hind on soodne.

## 8. Riskid ja väärarusaamad

100 on sage aktsiaoptsiooni kordaja, mitte universaalne seadus. Korporatiivsete sündmuste järel võib üleantav vara muutuda. Kõik optsioonid ei aegu väärtusetult ja paljud suletakse varem. Väärtusetult aeguv leping võis vahepeal olla kasumiga müüdud; statistika aegumiste kohta ei näita kõigi tehingute tootlust.

Aktsia annab ettevõtte omandiosa ja võib anda dividende. Call annab piiratud ajaks lepingulise õiguse; dividend ei laeku call’i hoidjale nagu aktsionärile.

## 9. Meeldejäävad põhimõtted

[PÕHIMÕTE] Õigus maksab, kohustus nõuab kapitali. Väärtus pole kasum. Vaata alati kogu lepingut, mitte ainult ekraanil olevat preemiat.

## 10. Kontrollküsimused

1. **Call on ITM 2 võrra, kuid maksis 3. Kas võitsid?** Tähtajal kaotad 1 ühiku kohta; ITM kirjeldab lepingut, mitte ostuhinda.
2. **Kas put tähendab alati karuturgu?** Ei; aktsiaomanik võib osta kaitse tõusuootust säilitades.
3. **Kas Euroopa optsioon tuleb tähtajani alles hoida?** Ei; täitmispiirang ei keela tavaliselt turul sulgemist.
4. **Kas short put’i suurim kahjum on preemia?** Ei; kui aktsia läheb nulli, on see M(K−p), enne kulusid.
5. **Miks müüja ei saa õiguse kasutamisest keelduda?** Ta müüs valikuõiguse; kohustuse vältimiseks peab ta positsiooni varem sulgema.

## 11. Õpetaja 1–2 minuti selgitus

Kujutlege, et ostame valiku, mitte asja. Maksame 3 õiguse eest osta 105-ga. Kui turg küsib 120, kasutame 105 hinnaga õigust ja selle majanduslik väärtus on 15. Aga meie kasum on 12, sest valik maksis 3. Kui turg küsib 90, ostaksime turult, mitte lepinguga. Õigus jääb kasutamata ja kaotame makstud 3. Teisel pool on keegi, kes sai 3, kuid lubas meie otsuse täita. Put pöörab ostuõiguse müügiõiguseks. Nüüd küsige: kellel on valik ja kes peab selle valiku tagajärje kandma? Kui see on selge, saab kõik keerulisemad strateegiad samadest tükkidest kokku panna.
