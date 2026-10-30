# Esmaspäev: päev 1


## A. 08.45 – Idee ei ole veel strateegia

[SIMULATSIOON] Maarika avab andmetabeli. Laual pole kümmet ekraani, vaid sülearvuti, üks monitor ja ülesanne: „Kontrolli sektorimomenti.” Daniel palub enne koodi ühte lauset: mida täpselt katsetatakse?

„Kas viimase kolme kuu tugevamad sektorid on ka järgmisel kuul tugevamad?” vastab Maarika. Priya küsib, kas tugevam tähendab positiivset tootlust või tootlust teiste sektorite suhtes. Need on erinevad küsimused. Tõusval turul võib kõikidesse sektoritesse investeerides teenida, kuigi järjestamise oskus puudub.

## B. Mida Maarika teab ja mida ta ei tea?

Ta teab, et hinnainfo on mõõdetav ning momentumil on võimalikke käitumuslikke seletusi: info aeglane levik ja investorite jätkuvad ostud. Ta ei tea, kas nähtus eksisteerib just valitud sektorites, horisondil ja kulude juures. Alternatiiv oleks tagasipöördumine: kiire hinnatõus võib hoopis eelneda langusele.

Ta valib kuise ümberjaotuse, sest päeva jooksul kauplemine nõuaks detailselt ajatemplistatud noteeringuid ja täitmiskulu mudelit. Kuus ETF-i lubavad õppijal andmeid silmaga kontrollida. See piirang muudab tulemuse kohalikuks: hiljem ei saa väita, et uuriti kogu USA aktsiaturgu.

## C. 10.10 – Andmete üleandmine

Elena: „Kas su hind sisaldab dividendi?”

Maarika: „Kasutan korrigeeritud sulgemishinda.”

Elena: „Siis ära lisa dividendi teist korda. Ja selgita, millal selle hinnaga kaubelda saad.”

Noah lisab andmelepingusse `signal`, `entry` ja `exit`. Maarika esialgne tabel sisaldas ainult kuupäeva ja hinda. Kolm aega tunduvad bürokraatiana kuni hetkeni, mil tuleb tõestada, et tulevikku ei kasutatud.

## D. Intuitsioon

Momentum on nagu jooksjate järjestamine viimase ringi kiiruse järgi. Mõte on, et kiirem võib olla ka järgmisel ringil kiirem. Kuid puhanud jooksja, raja muutus või finišispurt võib järjestuse ümber pöörata. Sama muster võib ühel horisondil jätkuda ja teisel tagasi pöörduda.

[NARANG] Peatükk 3 eristab ideed ja selle teostust; peatükk 8 selgitab andmete mõju sellele, milliseid strateegiaid üldse uurida saab. [JANSEN] Peatükid 6–8 seovad uurimisküsimuse tunnuste ja sihtmuutujaga.

## E. Väike arvutus

[NÄIDE] Hind 100 → 108 tähendab tootlust $108/100-1=8\%$. Teise vara 50 → 55 tähendab 10%. Esimese vara eurodes suurem hinnatõus ei tee seda suhteliselt tugevamaks. Just seepärast normaliseeritakse graafik algväärtusele 1.

## F. 13.30 – Esimene töötav skript

[PRAKTIKA] Käivita `python/paev1.py`. Skript loeb kaasasolevad hinnad, kontrollib kuupäevi ning prindib viimased 63 päeva tootlused. Graafik `pildid/hinnad.png` näitab sünteetiliste varade ühist turukomponenti.

Maarika salvestab hüpoteesi: „Valin kuu lõpul 63 päeva tootluse järgi kaks liidrit. Täidan järgmise vaatlusrea sulgemisel. Võrdlen netotootlust samast universumist võrdkaaluga.” Ta ei lisa pärast graafiku vaatamist erireeglit kõige ilusama vara jaoks.

## G. 15.15 – Hea välimusega viga

Ühes proovifailis on kuupäev kaks korda. Keskmistamine peidaks vea. Maarika peatab laadimise ja uurib päritolu. Noah märgib, et puuduv hind ei tähenda nulltootlust ning automaatne edasi täitmine võib tekitada näilise stabiilsuse.

Õppija kaasasolev puhas fail ei sisalda seda viga; ülesandes tekitad selle ise ja kontrollid, kas programm tõesti keeldub arvutamast.

## H. 16.40 – Päeva otsus

Meeskond kinnitab uurimisküsimuse ja andmelepingu. Kasumlikkuse kohta otsust veel ei tehta. Danieli kriitiline küsimus jääb tahvlile: „Mis tulemus paneks sind oma lemmikideest loobuma?” Maarika kirjutab: „Kui kulu ja aus ajastus kaotavad eelise, ei vii ma seda pärisrahale.”

## I. Õhtune märkmik

**Viis mõistet:** momentum, universum, võrdlusportfell, signaalihetk, andmekvaliteet.

**Põhimõtted:** idee peab olema ümberlükatav; kuupäev ei kirjelda üksi info kättesaadavust; ühikute kontroll eelneb mudelile. Homme vaatame, kas arvuti simuleerib päriselt lubatud tehinguid.


---

Edasi: [teooria](teooria.md) · [praktikum](praktikum.md) · [ülesanded ja lahendused](ulesanded-lahendused.md) · [sisukord](../README.md)
