# Kvaliteedikontroll ja valmidus

Kontrollitud 27.10.2026. **See pakett on kasutatav kompaktne põhikursus, mitte kõigi nõutud teemade ammendav süvakursus.** Süvendamist vajavad teemad on loetletud `OPPEKAVA.md` lõpus.

## Tegelikult tehtud kontrollid

| Kontroll | Tulemus |
|---|---|
| PDF-i kättesaadavus | Kõik 370 lehekülge tekstina eraldatavad; struktuur ja peatükikokkuvõtted kontrollitud |
| Raamatu detailne audit | Valitud lõigud; mitte kogu raamatu iga väide ja koodinäide |
| Moodulidemod | Kõik 13 käivitatud edukalt |
| Iseseisvate Python-ülesannete lahendused | Kõik 13 käivitatud edukalt |
| Finantsilised regressioonitestid | 14/14 läbitud |
| Koondprojekt ja lisapraktikumid | Offline-käivitus edukas |
| Colabi märkmikud | 3 faili; koodilahtrid käivitatud järjestikku kohalikus Pythonis, paigalduslahter välja arvatud |
| Graafikud | Portfelli- ja optsioonigraafik visuaalselt kontrollitud |
| Teekide ja API-de dokumendid | Põhiliidesed ametlikest dokumentidest kontrollitud |
| Yahoo, SEC, FRED võrgukutsed | Käivitamata; adapterid pole kinnitatud integratsioonitestiga |
| Live-LLM agent | API-kuju dokumentatsioonist kontrollitud; tasuline päring käivitamata |
| XGBoost valikuline haru | Kood olemas; paketti ei paigaldatud ega haru käivitatud |
| Närvivõrkude praktikum | Pole valminud; praegu meetodi valiku selgitus |

## Testkeskkond

Python 3.12.14; NumPy 2.3.5; pandas 2.2.3; Matplotlib 3.10.8; scikit-learn 1.8.0. Täpne masinloetav aruanne: `valjund/kontroll.json`. Dokumendilehtede „stable” versioon võib olla siin kasutatud versioonist uuem. Kõigi uute versioonidega ühilduvust pole tõestatud.

## Testide sisuline katvus

- Liittootlus ja algpäeva languse arvestamine maksimaalses languses.
- Osta-ja-hoia algkaalud, mitte ekslik igapäevane tasakaalustamine.
- Võlakirja nimiväärtuse juhtum ning YTM-i tagasiarvutus.
- Nullhinna ja duplikaatkuupäeva tagasilükkamine.
- Signaalide sõltumatus hilisemate hindade muutmisest.
- Signaali, täitmise ja tootluse korrektne viivitus.
- Kulude mõju ning tunnuste/sihtide ajastus.
- Agendi tööriistade lubatud loend ja teadaoleva allika leidmine.

Ühiktestid ei tõenda, et strateegia toimib turul; nad kontrollivad kirjeldatud arvutuste kooskõla.

## Teadlikud lihtsustused

Aastastamine 252 päevaga, sünteetiline tööpäevakalender, nullintress rahale, lihtne tehingukulu, maksude ja turumõju puudumine, fondi- ning võlakirjarahavoogude lihtsustatud esitamine. RSI on lihtsa liikuva keskmisega, mitte Wilderi algoritm. Juhukaalude pilv ei ole täpselt optimeeritud efektiivsuspiir. Agent kontrollib viite-ID olemasolu, mitte iga väite semantilist tõesust.

Kohalik fundamentaalnäide ja agendi fiktiivne ettevõte ei ole samad mis hinnasimulatsiooni vara — koondraport eristab neid demonstratsioone. Päris lõputöö peab instrumentide identiteedi ning allikad ühtselt siduma.

## Mida enne pärisandmetega õpetamist juurde kontrollida

Käivita laadija, säilita toorandmed ja metaandmed, kontrolli corporate actions näidet käsitsi ning võrdle üht näitajat algaruandega. Täida oma lõpuprojekti allikakaart. Pärast seda kasuta sama arvutustuuma ja teste; ära esita võrguühenduse olemasolu andmekvaliteedi tõendina.
