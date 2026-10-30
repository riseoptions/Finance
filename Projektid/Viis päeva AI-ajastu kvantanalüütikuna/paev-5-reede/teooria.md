# Päev 5: kasutuselevõtu otsus

[NARANG: ptk 10, 12; JANSEN: ptk 20, 24–26]

**Out-of-sample** tähendab, et hinnatavat vaatlust ei kasutatud selle prognoosi mudeli sobitamiseks. **Walk-forward** kordab seda läbi aja. **Puutumata lõppkatse** nõuab lisaks, et selle tulemusi ei kasutatud uurimisvalikute tegemiseks. Need mõisted ei ole vahetatavad.

**Paper trading** kontrollib reaalajas andmevoogu, orderite olekuid ja täitmise ligikaudset käitumist. Selles puudub pärisorderi turumõju ja võivad puududa järjekorraefektid. Ka paper trading'u kasum pole lõplik tõend.

## Otsustamise ahel

| Värav | Tõend | Ebaõnnestumise tagajärg |
|---|---|---|
| Andmed | Päritolu, ajastus, kvaliteet | Katse seisma |
| Kood | Arvestus- ja lekkevastased testid | Varasemad numbrid tühistada |
| Majanduslik loogika | Miks keegi peaks seda tootlust loovutama? | Uus hüpotees |
| Statistika | Aus ajajaotus, ebakindlus, kõik katsetused | Lisatõend või loobumine |
| Täitmine | Kulud, mahud, osatäitmised | Väiksem maht või teistsugune reegel |
| Operatsioonid | Vastutaja, seire, taastamine | Kasutuselevõttu ei toimu |

## Seireplaan

Andmetasand: duplikaadid, hilinenud fail, puuduvad varad ja muutunud skeem. Mudelitasand: tunnuste jaotus, prognooside äärmused, realiseerunud vead alles siltide küpsemisel. Portfellitasand: ekspositsioon, käive, kulud ja langus. Taristutasand: viimase eduka jooksu aeg ning sama sisendi korduvkäivituse idempotentsus.

[NÄIDE] Kui 6 vara asemel saabub 5, peatub uus otsustusraport. Kui käive ületab tavapärase vahemiku, tekitatakse kontrolliülesanne. Kui kulud ületavad eelarve, vaatab kaupleja täitmised üle. Need on õpetuslikud häired, mitte universaalsed finantsläved. Ära peata strateegiat automaatselt lihtsalt ühe halva päeva tõttu; vea ja tavapärase riski eristamiseks on vaja eelnevaid reegleid.

## MLOps minimaalsel kujul

Salvesta sisendi räsi, koodi versioon, paketiversioonid, parameetrid, treeningu lõppaeg, prognoos ja hiljem realiseerunud tulemus. Meie pakett salvestab andmeräsi, keskkonna ja prognoositabeli. Git commit lisatakse kasutaja enda hoidlas. Suures süsteemis lisanduvad mudeliregister, versioonitud teenus ja rollback.

LLM-raport võib olla abiline, kuid numbrid peavad tulema kontrollitud tabelist. Uus agent on põhjendatud siis, kui ta vähendab mõõdetavalt inimese kontrolliaega, säilitades viidete täpsuse. Vajalik mõõdik on näiteks kontrollitud väidete osakaal või raporti valmimise aeg, mitte pelgalt sõnade arv.

Reedene otsus on **täiendav uurimine**. Võrdkaal edestas siin teisi CAGR-is, ent ka see on sünteetiline tulemus. Ühtegi mudelit ei kuulutata päristuru võitjaks.


Edasi: [praktikum](praktikum.md) · [ülesanded](ulesanded-lahendused.md)
