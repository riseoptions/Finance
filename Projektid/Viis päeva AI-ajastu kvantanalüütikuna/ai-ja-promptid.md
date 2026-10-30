# AI tööriistad ja kontrollitavad promptid

[JANSEN: ptk 22, 24; TÄIENDUS] **LLM** genereerib teksti. **RAG** lisab vastuse koostamisele otsitud tõendid. **Agent** võib valida järgmisi tööriistakutseid eesmärgi täitmiseks. Kindla järjekorraga raportiskript pole seetõttu automaatselt agent.

Meie `rag_demo.py` rakendab TF-IDF-otsingut koos avaldamisaja filtriga. See on käivitatav retrieval-komponent, mitte täielik genereeriv RAG. `raport.py` vormindab kontrollitud numbrid deterministlikult. Neid piire ei varjata agentide sildi taha.

## Minimaalne tõenditega vastuse töövoog

1. Küsimus ja otsuse kuupäev.
2. Ainult selleks hetkeks avaldatud dokumendid.
3. Lühikeste katkendite otsing koos dokumendi ID ja avaldamisajaga.
4. LLM-i mustand, mille iga fakt on seotud ID-ga; arvutused eraldi Pythonis.
5. Kontroll: viide olemas, allikas toetab väidet, arv vastab tabelile. Puuduv tõend → „ei saa järeldada”.

Semantiline vektorotsing võib hiljem parandada sünonüümide leidmist; kõigepealt loo 10–20 näidisküsimusega hindamiskogum ja mõõda õige allika leidmist. Väikese tekstitabeli jaoks pole vektorandmebaas vältimatu.

## 1. Hüpoteesi täpsustamine

> Muuda järgnev idee kontrollitavaks hüpoteesiks. Esita universum, signaali teadaoleku aeg, täitmisaeg, hoideperiood, võrdlus, kulud ja ümberlükkamise tingimus. Erista majanduslik põhjendus ning oletus. Ära väida, et strateegia töötab. Idee: [sisesta].

## 2. Lekke otsimine koodist

> Kontrolli lisatud koodi ja uurimisprotokolli. Leia kohad, kus tulevane hind, hiljem lõppev silt või testandmetelt sobitatud teisendus võib mõjutada prognoosi. Iga leiu juurde anna konkreetne minimaalne vastunäide ja test. Ära nimeta kontrolli edukaks enne testi käivitamist. Kood: [lisa].

## 3. Finantsdokumendi lugemine

> Vasta ainult lisatud katkendite põhjal, otsuse kuupäevaga [kuupäev]. Tabeli veerud: väide, dokumendi ID, avaldamisaeg, toetav fakt, piirang. Erista juhtkonna prognoos mõõdetud tulemusest. Kui tõend puudub või avaldati hiljem, ütle seda. Katkendid: [lisa].

## 4. Mudelite võrdlemine

> Võrdle tabelis reeglit, Ridge'i ja Random Forestit. Käsitle sama perioodi prognoosiviga, netotootlust, riski, käivet ja kulutundlikkust. Ära vali võitjat ainult RMSE või CAGR-i alusel. Märgi, kas andmed on sünteetilised. Nimeta järgmine sõltumatu kontroll. Tabel: [lisa].

## 5. Komitee raport

> Koosta 300-sõnaline eestikeelne uurimismemo. Struktuur: küsimus, katse, tulemus, piirangud, otsus. Kõik arvud peavad tulema lisatud tabelist. Ära muuda puuduvat väärtust nulliks. Ära esita aktiivtootlust faktoralphana. Kui materjal ei tõenda kasutuselevõttu, ütle seda otse.

## 6. Õpetaja selgitus

> Selgita [mõiste] esmalt 100-eurose näitega, seejärel ühe valemi ja 10–20-realise Python-koodiga. Lisa üks levinud väärarusaam, üks vastunäide ja kontrollküsimus vastusega. Näita, millistel eeldustel valem kehtib.

## 7. Visualiseerimise tellimus

> Joonista lisatud tabelist kapitalikõver ja langus tipust. Kapital peab algama 1-st ja algkapital kuuluma senise tipu arvutusse. Märgi sünteetilised andmed pealkirjas. Erista valideerimine ja lõppkatse, ära ühenda eraldi nullist algavaid portfelle katkematuks ajaloooks.

## 8. Piiratud agendi kavand

> Kavanda agent, kes saab ainult lugeda lubatud uurimisfaile ja koostada mustandraporti. Defineeri tööriistade sisend/väljund, ajapiir, lubatud kaustad, maksimaalne sammude arv, kulueelarve ning kontrollitud väidete mõõdik. Ära lisa maakleri-, makse- ega orderiõigusi. Väljund peab sisaldama viidete kontrolli ja lõpetama tõendi puudumisel.

## Agentide minimaalne leping

Lubatud tööriistad võiksid olla `read_metrics(run_id)`, `retrieve_evidence(question, as_of)` ja `draft_report(evidence_ids)`. Sisend valideeritakse skeemi vastu; faile ei avata mudeli vaba teeraja järgi. Arvud tulevad CSV-st, dokumentides olev tekst ei saa anda tööriistaõigust. Maksimaalselt näiteks 5 sammu on õpetuslik piir, mitte universaalne standard.

Hinda enne lisamist: kas raporti kontrollimise aeg väheneb, kas viited on õiged, kas agent loob toetamata väiteid ja kas katkestatud jooksu saab taastada? Päris API-integratsiooni ning selle kulusid selles komplektis ei käivitatud.
