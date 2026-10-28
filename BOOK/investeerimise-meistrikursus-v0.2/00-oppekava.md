# Õppekava ja raamatute süntees

[Tagasi avalehele](README.md)

## Sisukord

- [Raamatute rollid](#raamatute-rollid)
- [Teemade vastavustabel](#teemade-vastavustabel)
- [Õppimise järjekord](#õppimise-järjekord)
- [Iga õppetüki standard](#iga-õppetüki-standard)

## Raamatute rollid

[SCHWAGER] Minevikutootluse, riskimõõdikute ja portfellide käsitluses on keskne küsimus: millist viga teeb investor järelduse tegemisel? Peatükid 3, 4, 6–9 ja 17–21 annavad siin analüütilise lähtekoha.

[PAPP] Peatükid 2–3 annavad finantsaruannete ja andmete tööriistad; 7 riskianalüüsi ja portfellide näited; 8–11 AI, agentide, graafikute ja algoritmilise kauplemise töövõtted.

[ANALÜÜS] Nende ühendamise õppeühik on **kontrollitav väide**. Tehnoloogia tuleb kasutusele siis, kui see aitab väidet täpsemalt hinnata. Ka raamatu autor võib kasutada liiga tugevat sõnastust või lihtsustavat eeldust; kontroll kehtib mõlema autori kohta.

## Teemade vastavustabel

Kaart tugineb mõlema raamatu sisukorrale ning esimeste laborite jaoks loetud valitud lõikudele. See ei ole mõlema raamatu iga väite täielik audit.

| Teema | Schwager | Papp | Süntees ja vajalik täiendus |
|---|---|---|---|
| Investeerimise alused ja instrumendid | Riskifondid ptk 10–16; optsioonide lisa A | Ptk 1–2, 5, 12 | Süsteemne instrumentide atlas; ETF-i toimimine; optsioonide väljamaksed |
| Eksperdid ja turu efektiivsus | Ptk 1–2 | Ptk 4: investeerimisteesi vaidlustamine | Eristada hinnastamise eksimust ja kasutatavat kasumivõimalust |
| Minevikutootlus | Ptk 3, 6–8 | Ptk 4, 7, 11 | Valikukallutatus, sõltumatu test, oskuse ja juhuse lahutamine |
| Volatiilsus ja varjatud risk | Ptk 4, 8, 20; lisa B | Ptk 7 | VaR-i kvantiilidefinitsioon, ES, stress ja likviidsus |
| Korrelatsioon ja hajutamine | Ptk 9, 17–18, 21 | Ptk 7.2, 7.4, 7.6 | Korrelatsioonirežiimid; korrelatsiooni eristamine põhjuslikkusest |
| Võimendus | Ptk 5, 15 | Ptk 7: riskimaandamine | Igapäevase võimenduse hinnateekond ja sundmüügi risk |
| Portfelli koostamine | Ptk 19, 21 | Ptk 4–7 | Optimeerimisvea testimine ning kuludega rebalanseerimine |
| Finantsaruanded ja väärtus | Ptk 4: hinna roll riskis | Ptk 2, 4–6, 12 | DCF, tundlikkusanalüüs, ettevõtte ja investeeringu eristamine |
| Andmete kvaliteet | Ptk 6–7, riskifondide osa järelsõna | Ptk 3, 6 | Ajalooline kättesaadavus, valuuta, dividendide arvestus, kadunud fondid |
| Tehniline analüüs ja järeltest | Peamiselt hindamise kriitika ptk 6–8 | Ptk 10–11 | Tehinguaeg, viitaeg, kulud, andmeleke ja mitu katset |
| ML, LLM-id, RAG ja agendid | Otsene tehnoloogiline õpetus puudub | Ptk 8–9 | Võrdlus baasmeetodiga; väidete allikakontroll; mõõdetav lisaväärtus |
| Maksud, Eesti/EL nõustamisraamistik | Pole selle kursuse jaoks piisav alus | Pole Eesti-spetsiifiline alus | Eraldi ajakohased esmased allikad; veel koostamata |

Schwageri ajalooliste näidete tulemusi ei esitata 2026. aasta turu seaduspärasustena. Tema 3. peatükk rõhutab ka ise empiiriliste järelduste tingimuslikkust. VaR-i kirjeldamisel täpsustame mõlema raamatu võimalikke halvima kahju tõlgendusi: kvantiil ei ole maksimaalne kahju.

## Õppimise järjekord

Soovituslik maht on 16 nädalat, 3–5 tundi nädalas. Ajad on õppeplaan, mitte lubadus kogu meistrikursuse omandamiseks.

| Nädal | Õppeplokk | Tõend omandamisest | Seis versioonis 0.1 |
|---|---|---|---|
| 1 | Tootlus, liitintress, inflatsioon, kulud | Eristad aritmeetilist keskmist ja CAGR-i | Alusmoodul ja näited valmis |
| 2–3 | Aktsiad, ETF-id, võlakirjad ja tuletised | Selgitad instrumendi rahavood ja kahjud | Nelja instrumendi alusatlas valmis; süvaatlas pooleli |
| 4 | Turud, hinnad ja investeerimisväited | Sõnastad falsifitseeritava hüpoteesi | Spikker olemas |
| 5 | Minevikutootlus ja valik | Kontrollid oskuse ja juhuse mudeleid | Labor 1 valmis |
| 6 | Korrelatsioon ja portfell | Tuletad ning stressid portfelliriski | Labor 2 valmis |
| 7 | VaR, ES ja varjatud risk | Leiad sama VaR-iga erinevad kahjujaotused | Labor 3 valmis |
| 8 | Võimendus, optsioonid ja hinnateekond | Arvutad väljamaksed ja sundmüügi piiri | Kavandatud |
| 9 | Fundamentaalanalüüs | Koostad aruannetest põhjendatud hindamisvahemiku | Kavandatud |
| 10 | Andmetöötlus ja reprodutseeritavus | Valideerid ajaloolise andmestiku | Kontrolliplaanid olemas |
| 11 | Strateegiad ja järeltest | Kasutad ajalist testjaotust ning kulusid | Lühike sünteetiline näide valmis; pärisandmete projekt puudub |
| 12 | Masinõpe | Võrdled mudelit lihtsa baasprognoosiga | Väike regressiooninäide valmis; ML-süvamoodul puudub |
| 13 | LLM ja RAG | Seod aruande iga arvulise väite allikaga | Kavandatud |
| 14 | Automatiseeritud jälgimine | Koostad kontrollitava raporti | Kavandatud |
| 15 | Investori eesmärgid ja sobivus | Eristad riskitaluvust ja riskikandevõimet | Kavandatud |
| 16 | Lõpuprojekt ja õpetamine | Kaitsed väidet koos vastuväidete ja korduskatsega | Kavandatud |

Tugeva matemaatikataustaga õppija võib alustada laboritest ning lugeda instrumentide teemasid vajaduse tekkimisel juurde.

## Iga õppetüki standard

**5 minutit:** üks täpne väide, üks arvuline näide, üks piirang.

**30 minutit:** mehhanism, valem koos eeldustega, arvutus ja kaks kontrollküsimust.

**90 minutit:** kood, muudetavad parameetrid, alternatiivne mudel, tulemuste tõlgendamine ning lühike õpetamis- või väitlusülesanne.

Iga väite juurde kirjuta tõendusliik: matemaatiline tulemus, majandusteoreetiline mudel, empiiriline tähelepanek, rusikareegel või vaidlustatav hüpotees. Esmalt loe koodi sisendit ja mõõdiku definitsiooni; alles siis tulemust.

Korda põhiideed 1, 7 ja 30 päeva pärast: taasta valem mälu järgi, muuda üht eeldust ning selgita, kas järeldus jääb kehtima. See on soovituslik õpiharjumus; automaatseid meeldetuletusi pole loodud.

## Versiooni 0.2 õppematerjalid

Alusta [tootluse alusmoodulist](01-investeerimise-alused/README.md), seejärel vali [instrument](02-finantsinstrumendid/README.md) või [matemaatikateema](07-finantsmatemaatika/README.md). Kordamiseks on [100 põhimõtet](15-100-pohimotet/README.md), oskuste kontrolliks [50 ülesannet](17-50-ulesannet/README.md).
