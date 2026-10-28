# Õpetaja käsiraamat: kolm 90-minutilist tundi

[Tagasi avalehele](README.md) · [Lahendused](laborid/lahendused.md)

## Tunnikavad

| Aeg | Labor 1: fondide võitjad | Labor 2: hajutamine | Labor 3: varjatud risk |
|---|---|---|---|
| 0–10 min | Õpilane valib kahe tootlusrekordi vahel | Õpilane järjestab 1, 10 ja 100 vara riski | Õpilane võrdleb 96% kasumlike kuudega strateegiaid |
| 10–25 min | CAGR, juhus ja valik | Kovariatsiooniliikmete tuletamine | Kahju märgikonventsioon ja kvantiil |
| 25–40 min | Nulloskuse mudeli ennustus | $n$ vara valemi tõestus | ES-i arvutamine tõenäosusmassidest |
| 40–55 min | Käivitus ja tulemuse selgitamine | Kolme stsenaariumi arvutus | Käivitus ja VaR/ES võrdlus |
| 55–70 min | Lisa püsiv oskus | Muuda ainult üht parameetrit | Eemalda ajaloost krahhid |
| 70–82 min | Väitlus: kas minevik aitab? | Väitlus: kas hajutamine kaob? | Väitlus: kas ES lahendab kõik? |
| 82–90 min | Kirjalik järeldus ja üks piirang | Kirjalik järeldus ja üks piirang | Kirjalik järeldus ja üks piirang |

## Viis põhimõtet igas tunnis

| Labor 1 | Labor 2 | Labor 3 |
|---|---|---|
| Rekord pole oskuse definitsioon | Nimede arv pole sõltumatute riskide arv | VaR on kvantiil |
| Valikureegel tuleb määrata varem | Kovariatsioon loeb | Kvantiil pole maksimaalne kahju |
| Tulevik peab jääma valikust välja | Kõrge korrelatsioon vähendab kaitset | ES arvestab saba suurust |
| Püsiv oskus võib infot anda | Mõju vähenemine pole mõju kadumine | Puuduv sündmus võib eksitada ka ES-i |
| Simulatsioon pole turu-uuring | Stressiparameeter pole mõõdetud fakt | Mudel ja mõõdik on eri asjad |

## Kontrollküsimused

- Labor 1: mida tähendab sõltumatu kontrollperiood; mis muutub, kui oskus pole püsiv; miks ei tõesta keskmisele lähenemine automaatselt hinnapööret?
- Labor 2: mitu kovariatsiooniliiget summas on; millal võib standardhälve langeda nullini; miks tuleb võrrelda sama ajahorisonti?
- Labor 3: mida tähendab negatiivne VaR; miks peab diskreetse jaotuse puhul massi osaliselt kaasama; millised riskid jäävad kasumliku ajaloo taha peitu?

## Hindamine: 10 punkti

2 p: väide ja mõisted on täpsed. 2 p: arvutus on korrektne ning ühikud märgitud. 2 p: kood annab taastoodetava tulemuse. 2 p: õppija toob sisulise vastunäite või piirangu. 2 p: selgitus on arusaadav ka inimesele, kes koodi ei loe.

Pelgalt skripti käivitamine annab maksimaalselt 2 punkti. Matemaatiliselt õige arvutus vale majandusliku tõlgendusega ei anna tõlgenduspunkte.

## Tüüpilised vead ja õpetaja sekkumine

- „Parim fond on alati juhus.” Palu muuta oskuse hajuvust ja selgitada erinevust.
- „Korrelatsioon 0.8 tähendab, et 80% päevadest liigutakse samas suunas.” Palu defineerida Pearsoni korrelatsioon kovariatsiooni kaudu; need ei ole samad suurused.
- „95% VaR tähendab, et rohkem ei saa kaotada.” Näita B krahhiharu.
- „ES näitab peidetud kahju ka ilma andmeteta.” Näita vaikse ajaloo arvutust ning küsi, kust võiks tulla lisainfo strateegia riski kohta.

## Kordamisülesanne

Anna õppijale üks labor, mille tulemust ta veel ei näe. Ta peab enne käivitamist kirjutama prognoosi, pärast käivitamist selgitama erinevust ning lõpuks muutma üht eeldust. Hinda ennustuse põhjendust, mitte juhusliku arvulise tulemuse tabamist.
