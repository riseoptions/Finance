# Sünteetika, delta-neutraalsus, wheel ja riskimaandamine

[Atlas](README.md)

## Put-call parity

[RAAMAT] Peatükk 11, PDF 116–123, ja lisa E, 206–210, seovad positsioonid sünteetiliste vastetega. [MATEMAATIKA] Euroopa call’i ja put’i sama strike’i ja tähtaja korral, pideva dividendimääraga q:

$$C-P=S_0e^{-qT}-Ke^{-rT}.$$

Dividendideta: call + strike’i nüüdisväärtusega võlakiri = put + aktsia. Terminalis on mõlemal pool väärtus max(S,K). See on rahavoogude identsus, mitte prognoos. Ameerika lepingute varajane täitmine tähendab, et lihtsat Euroopa võrdsust ei tohi üle kanda ilma täpsustuseta.

[NÄIDE] S=K=100, r=q=0, C=P=6. Long call − long put maksab null ja annab tähtajal S−100. Aktsia täpseks sünteesimiseks tuleb lisada 100 raha. Nullhinnaga sünteetiline forward ei ole tasuta aktsia.

### Sünteetilised seosed

| Kombinatsioon | Täpne terminalne vastavus, r=q=0 | Täpsustus |
|---|---|---|
| Call − put | S−K | Forward’i väljamakse |
| Aktsia + put | Call + K raha | Protective put vajab rahajala arvestust |
| Aktsia − call | K raha − put | Covered call’i võrdlus cash-secured put’iga |
| Put − call | K−S | Sünteetiline short forward |

**Näide covered call vs cash-secured put.** S₀=100, K=100, C=P=6. Covered call’i netokulu on 94; cash-secured put’i jaoks 100 raha miinus 6 krediiti on samuti 94. Mõlema P/L on min(S,100)−94. Strike 95 put’i ja strike 105 covered call’i ei saa selle seose alusel samaväärseks nimetada.

**Risk ja alternatiiv.** Sünteetika säilitab hinna suhtes riski; erinevad võivad olla intress, dividend, tehinguluba, täitmine ja maksustamine. Lihtsam alternatiiv on aktsia ise. Ühe minuti seletus: liida terminalrahavood, enne kui järeldad, et kaks nime tähendavad sama toodet.

**Küsimused.** Kas C=P alati? Ei, ainult sobivatel eeldustel. Kas sügav ITM call on täpselt aktsia? Ei, delta ja rahastamine erinevad. Kas sama payoff garanteerib sama netotootluse? Ei, hinnad ja kulud võivad erineda.

## Delta-neutraalne positsioon

[TÄIENDUS] Eesmärk on vähendada väikese hetkelise hinnamuutuse esimese järgu mõju. Osta 2 call’i, mille delta on 0,50 ja kordaja 100; müü lühikeseks 100 aktsiat. Algdelta on 0. Aktsiate laenukulud ja tagatis tuleb arvestada.

| Olukord | Call’ide delta | Aktsiate delta | Netodelta |
|---|---:|---:|---:|
| Avamisel | +100 | −100 | 0 |
| Call’i delta tõuseb 0,60-ni | +120 | −100 | +20 |
| Call’i delta langeb 0,40-ni | +80 | −100 | −20 |

Delta-neutraalsus on seisund, mitte eraldi universaalne payoff-strateegia. Algdelta null ei määra kasumit, kahjupiiri ega tasuvuspiiri: selleks on vaja kõiki jalgu ja nende hindu. Näiteks long straddle’i kaart annab konkreetse ligikaudu delta-neutraalse kombinatsiooni [graafiku ja P/L-i](12-straddle.md).

**Aeg ja IV.** Long-gamma maandatud positsioon võib saada hinnakõikumisest kasu, kuid maksab sageli thetat ning ümbermaandamise kulusid. Kasum sõltub realiseerunud kõikumisest võrreldes makstud IV-ga ja valitud maandamisest. Lihtsam alternatiiv on vähendada suunapositsiooni.

**Ühe minuti selgitus.** Tasakaalusta kaal kaks vastassuunalist tundlikkust. Kui hind muutub, muutub optsiooni tundlikkus ja kaal läheb tasakaalust välja. Taastasakaalustamine pole tasuta.

**Põhimõtted.** Null delta ei võrdu null risk. Maandamine muudab riski, ei kustuta kõiki kulusid.

**Kolm küsimust.** Kas vaja on ümbermaandamist? Tavaliselt jah. Kas vega kaob? Ei. Kas null delta tõestab kasumlikkust? Ei.

## Wheel-strateegia

[TÄIENDUS] Protsess: müü rahaga tagatud put; assignment’i korral osta aktsiad; müü nende vastu call; aktsiate ärakutsumise järel korda. See on järjestikuste otsuste süsteem, mitte ühe tähtaja valem.

[NÄIDE] Müüd put K=95, saad 3; hind langeb 80-ni ja ostad 100 aktsiat 9500 eest. Majanduslik soetusmaksumus pärast preemiat on 9200. Seejärel müüd call K=95 preemiaga 2. Kui aktsia kutsutakse 95-ga ära, on kahe preemia kogukasum 500 USD enne kulusid. Kui hind langeb nulli, on kogu tsükli kahju 9000 USD. Mõlemad preemiad kokku ei kaitse põhikapitali.

| Tee | Esimese tähtaja hind | Teise tähtaja hind | Tulemuse selgitus |
|---|---:|---:|---|
| Put aegub, uut tehingut ei tee | 100 | — | +300 USD |
| Assignment, siis call täidetakse | 80 | 110 | +500 USD, kuid tõus üle 95 loovutatud |
| Assignment, call aegub | 80 | 70 | Aktsiate turuväärtus 7000; kogutulemus −2000 USD |
| Assignment, ettevõtte väärtus null | 80 | 0 | Kogutulemus −9000 USD |

Teise etapi hindade graafik on [covered call’i](05-covered-call.md) kujuline, kuid arvutuses asendub netosoetusmaksumus siin 90-ga ja strike 95-ga. Üht kogu wheel’i sõltumatut payoff-diagrammi ei ole, sest uued preemiad, strike’id ja assignment sõltuvad teekonnast.

**Turuvaade ja IV.** Üldiselt positiivne suunarisk ja müüdud optsioonide negatiivne gamma/vega. Kõrgem IV tähendab kõrgemat tasu koos kõrgema tajutud riskiga. **Alternatiiv:** osta väiksem aktsiapositsioon ja hoia. **Viga:** nimetada preemiaid tootluseks, ignoreerides aktsia miinust.

**Ühe minuti seletus.** Wheel on korduv ostu- ja müügikohustuse võtmine. See teenib mõnikord preemiaid ilma aktsiat saamata, aga langusel võib jätta kauaks aktsiaomanikuks. Uus ring ei kustuta vana kahju.

**Küsimused.** Kas assignment on kasum? Ei, see on ostutehing. Kas saab pidevalt sama preemiat? Ei. Kas wheel vajab lõpphinnast rohkem andmeid? Jah, kogu teekonda ja otsuseid.

## Riskimaandamine

Kui kaitsed 100 sama aktsiat, võib 1 standardne put anda sobiva koguse, kuid 100 000 USD eri aktsiatest portfelli kaitsmine ühe ETF-i put’iga nõuab lisaks hinna, kordaja ja koosliikumise hindamist. Alusvarade erinevus tekitab baasiriski.

[NÄIDE] Portfell 100 000, ETF 500, M=100. Kaks ETF-i lepingut katavad 100 000 nimiväärtust, kuid delta −0,50 korral on hetke deltakaitse ligikaudu 50 000 USD alusvarariski ulatuses. Kogu lõppkaitse sõltub strike’ist ning sellest, kas portfell tõesti liigub nagu ETF.

**Põhimõte.** Nimiväärtuse katmine, delta maandamine ja tähtaja kahjupõrand on kolm eri eesmärki. Protective put’i [graafik](07-protective-put.md) näitab sama alusvara põrandat; eri alusvarade puhul see automaatselt ei kehti.
