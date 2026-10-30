# Päev 1: kontrollküsimused ja ülesanded

Proovi enne vastuse lugemist iseseisvalt. Baastase: mõisted; rakendustase: arvutus ja kood; süvatase: otsuse piirangud.

## Kontrollküsimus 1

**Miks ei piisa hüpoteesist „momentum töötab”?**

Vastus: Puuduvad universum, ajahorisont, täitmishetk, kulud ja võrdlus. Ilma nendeta saab tulemuse järel tingimusi nihutada.

## Kontrollküsimus 2

**Kas kallima osakuga ETF on tugevam?**

Vastus: Ei. Võrdle suhtelist tootlust. Hind sõltub ka osakute arvust ja splittidest.

## Kontrollküsimus 3

**Miks ei tohi puuduvat hinda asendada nulliga?**

Vastus: See looks −100% tootluse ning järgmisel real jagamise nulliga. Puuduv vaatlus on andmekvaliteedi probleem.

## Kontrollküsimus 4

**Kas baasist suurem tootlus on alpha?**

Vastus: See on aktiivtootlus valitud baasi suhtes. Alpha vajab riskitegurite mudelit ja ebakindluse hinnangut.

## Kontrollküsimus 5

**Mida tõendab sünteetilise katse positiivne tootlus?**

Vastus: Et valitud reegel teenis valitud generaatori realisatsioonil. See ei tõenda päristuru eelist.

## Praktiline ülesanne 1: Arvutus ja kood: suhteline tugevus

[PRAKTIKA] A hind muutub 80 → 88, B 200 → 216. Leia tootlused ja paremusjärjestus. Kontrolli Pythoniga.

**Lahendus:** `88/80-1 = 0.10`; `216/200-1 = 0.08`. A on tugevam, kuigi B hinnamuutus rahas on suurem. `sorted({"A":88/80-1,"B":216/200-1}.items(), key=lambda z:z[1], reverse=True)` annab A, B.

## Praktiline ülesanne 2: Otsus ja sisendkontroll

[PRAKTIKA] Lisa mälus hinnatabeli lõppu viimase rea koopia. Kas jätkata analüüsi või keskmistada?

**Lahendus:** `p=load_data(); bad=pd.concat([p,p.iloc[-1:]]); validate(bad)` peab tõstma ValueError. Peata arvutus ja selgita duplikaadi päritolu. Keskmistamine pole põhjendatud enne teadmist, kas kordus on viga või eri turu vaatlus.

## Vanemkvandi kriitiline küsimus

Milline vaadeldav tulemus muudaks sinu hüpoteesi usutamatuks?

Hea vastus nimetab kontrollitava tingimuse ja selle, millised andmed selle kontrollimiseks vajalikud on. Kehv vastus kaitseb mudelit lihtsalt sellepärast, et selle peale kulus palju aega.

## Enesehindamine

Anna iga kontrollvastuse eest 0–2 punkti ning kummagi praktilise ülesande eest 0–5 punkti. 16/20 näitab head alust; edasi minekuks peab ajastuse või tõendi piiri puudutav vastus siiski olema sisuliselt õige. Õpetaja selgitab keerulise vea enne järgmist päeva.
