# Töölehed: 16 moodulit

Tase A: mõistmine. Tase B: arvutus või praktiline kontroll. Tase C: iseseisev uurimine ja õpetamine.

## 01. Kvantinvesteerimise ajalugu ja areng

1. [A] Kas 2010. aasta närvivõrgumudel on generatiivne AI?

2. [A] Miks ei tõesta 1000 testist parim kasumlik strateegia eelist?

3. [B] Arvuta 20 sõltumatu 5% testi puhul vähemalt ühe valepositiivse tõenäosus.

4. [C] Koosta uurimispäevik: idee, kuupäev, andmeversioon, kõik proovitud variandid, loobumise põhjus. Ära säilita ainult võitjaid. Esita ka üks piirang.

## 02. Klassikaline statistika, faktorid ja portfellid

1. [A] Kas alfa 4% tõestab oskust?

2. [A] Mis juhtub hajutamisega, kui korrelatsioon tõuseb?

3. [B] Arvuta ülaltoodud portfelli risk korrelatsiooniga 0,5.

4. [C] Käivita projekt ning ava kovariatsioon.csv. Võrdle võrdseid kaale ja pöördvolatiilsuse kaale. Viimane ei ole üldjuhul täielik riskipariteet, sest ei arvesta kõiki korrelatsioone. Esita ka üks piirang.

## 03. Masinõpe aktsiaturu analüüsis

1. [A] Miks on juhuslik train_test_split probleem?

2. [A] Kas SHAP tõestab põhjuslikkust?

3. [B] Võidumäär 55%, võit 1%, kaotus 1%, kulu 0,15% igal tehingul: ootus?

4. [C] Projektis võrdle ridge’i nullprognoosiga failis test_mse.csv. Vaata seejärel netotootlusi. Ära vali mudelit tagantjärele lõppkatse parima Sharpe’i järgi. Esita ka üks piirang.

## 04. XGBoost, süvaõpe ja aegridade prognoos

1. [A] Kas XGBoost vajab standardiseerimist?

2. [A] Miks ei tohi early stopping jälgida lõppkatset?

3. [B] Arvuta kaks +0,4% parandust, η=0,1, algus 0%.

4. [C] Paigalda valikuline XGBoost. Projekt salvestab kõigi mudelite MSE ning valib ühe valideerimisest. Hoia testiperiood muutmata; lisa süvaõppemudel alles siis, kui oskad sama ajastust säilitada. Esita ka üks piirang.

## 05. Fundamentaalse, tehnilise ja kvantanalüüsi ühendamine

1. [A] Kas madal P/E tähendab alahinnatust?

2. [A] Miks testida tunnuserühma eemaldamist?

3. [B] Väärtusskoor 2, kvaliteet −1, momentum 0,5: keskmine?

4. [C] Lisa hiljem projektile üks avaldamisajaga fundamentaaltunnus. Võrdle hinna-mudelit, fundamentaalmudelit ja nende ühendust sama kulumudeli ning testiperioodiga. Esita ka üks piirang.

## 06. Finantsandmed, alternatiivandmed ja ajaline korrektsus

1. [A] Kas tänased S&P 500 liikmed sobivad 2005. aasta universumiks?

2. [A] Kas auto_adjust=True eemaldab kõik andmeprobleemid?

3. [B] Aruanne avaldub pärast börsi sulgemist. Millal tohib seda kasutada?

4. [C] 01_andmed.py genereerib vaikimisi SIM_A/B/C. --download valib ajaloolised AAPL/MSFT/JPM hinnad ainult tehnilise näite jaoks. See tänastest ellujääjatest valim ei tõenda üldist USA aktsiastrateegiat. Esita ka üks piirang.

## 07. AI abil hüpoteeside genereerimine ja kontrollimine

1. [A] Miks on AI pakutud usutav mehhanism ebapiisav?

2. [A] Kas uus mudelinimi on uus majandushüpotees?

3. [B] Kulud 0,4%, brutolisatootlus 0,3% aastas: netolisaväärtus?

4. [C] Kasuta uurimisprotokolli projekti juhendis. Küsi AI-lt kolm alternatiivset selgitust ja üks katse, mis sinu lemmikhüpoteesi ümber lükkaks. Esita ka üks piirang.

## 08. LLM, RAG, teadmistegraaf ja AI-agent

1. [A] Kas iga Python-tsükkel on AI-agent?

2. [A] Kas õige allikaviide tähendab õiget vastust?

3. [B] 20 kontrollitud viitest 18 toetavad väidet; täpsus?

4. [C] 07_rag_agent.py töötab esmalt lokaalse otsingu demonstratsioonina. --live-llm loob API kaudu tekstianalüüsi; --agent lubab kuni kolm piiratud tööriistavaliku sammu. Offline-režiim ei ole LLM ega AI-agent. Võrdle käsitsi koostatud vastusevõtmega, mitte mudeli enesehinnanguga. Esita ka üks piirang.

## 09. Algoritmiline kauplemine ja järeltestimine

1. [A] Miks ei saa sulgemishinna signaal alati sama sulgemishinnaga täituda?

2. [A] Kas kõrgsagedusstrateegiat saab hinnata päevahindadega?

3. [B] Signaal esmaspäeva lõpus, tehing teisipäeva lõpus: milline päevatootlus on esimene?

4. [C] Leia projekt.py failist dataset ja comparison. Kontrolli käsitsi kolme kuupäevaga signaali, täitmishinna ja teenitud tootluse ajastust. Gap=2 on selle näite sildihorisondiga seotud, mitte universaalne soovitus. Esita ka üks piirang.

## 10. Optsioonid, futuurid, ETF-id ja muud instrumendid

1. [A] Call K=100, preemia 8, S_T=95: kasum?

2. [A] ETF hind 101, NAV 100: preemia?

3. [B] Miks on futuuri tootlus tagatise suhtes eksitav võrdlusalus?

4. [C] Käivita 10_instrumendid.py. Black–Scholesi näide eeldab Euroopa call’i, konstantseid parameetreid ja dividendide puudumist. Tulemus on õppehind, mitte tänane turukvoot. Esita ka üks piirang.

## 11. Portfelli optimeerimine ja riskijuhtimine

1. [A] Miks võib võrdkaal keerukat optimumi võita?

2. [A] Kas 95% VaR 2% tähendab, et kaotus ei ületa 2%?

3. [B] Kapital 100→80: milline tootlus taastab algtaseme?

4. [C] Vaata portfell.csv ja kovariatsioon.csv. Projekt hindab riskiparameetrid ainult enne testiperioodi; võrdleb igapäevaselt taastatud võrdkaalu ja pöördvolatiilsust koos käibekuluga. Eeldus on õppeotstarbeline. Esita ka üks piirang.

## 12. Realistlik hindamine, kulud ja üleõppimine

1. [A] Bruto 8%, käive 40, kulu 10 bp: ligikaudne neto?

2. [A] Mida tähendab negatiivne neto, aga positiivne prognoosikorrelatsioon?

3. [B] Kas sama holdout’i 20 korda vaatamine säilitab sõltumatuse?

4. [C] Projekt arvutab kulud 0, 5, 10, 25 ja 50 bp juures. Kontrolli, kas valideerimisel valitud mudel jääb netos veenvaks. Bootstrap’i tulemus on tinglik olemasolevale ajaloole, mitte uus sõltumatu tõend. Esita ka üks piirang.

## 13. Tänapäevase kvandi tööriistad ja tööpäev

1. [A] Miks salvestada CSV räsi?

2. [A] Kas sama random seed tagab kõikjal sama tulemuse?

3. [B] Milline kontroll tuleb enne MSE arvutamist?

4. [C] Alusta Thonnys: pandas, NumPy, scikit-learn, Matplotlib ja CSV. Lisa SQLite, kui vajad päringuid ja versioone; XGBoost pärast baasi. Colab sobib märkmike ja jagatava õppe jaoks. VS Code ning keerukam MLOps tulevad vajadusest. Esita ka üks piirang.

## 14. AI eelised, piirangud ja riskid

1. [A] Kas mudeli „olen 95% kindel” on riskimõõt?

2. [A] Kas andmeleket parandab tugevam regulariseerimine?

3. [B] AI säästab 60 min, kontroll 25 ja parandus 20: netosääst?

4. [C] Koosta riskiregister: risk, võimalik kahju, avastamise kontroll, peatamistingimus, vastutaja. Katseta puuduva allika, tulevikudokumendi, vigase JSON-i ja keelatud tööriistaga. Esita ka üks piirang.

## 15. Tõenäolised arengud 2027–2030

1. [A] Milline väide on paremini põhjendatud: „AI kaotab kvandid” või „mõned ülesanded automatiseeruvad”?

2. [A] Kas 2030. aasta täpne mudeliparemus on täna teada?

3. [B] 200 ülesannet hinnaga 0,50 ja 3 min ülevaatust: maht?

4. [C] Vaata iga kvartal üle kolm mõõdikut: faktivead, aeg, kogukulu. Võta uus tehnoloogia kasutusele alles siis, kui see ületab sinu baastöövoo ette määratud piirid. Esita ka üks piirang.

## 16. Isiklik õppe- ja arenguplaan

1. [A] Kas kursuse läbimiseks peab ML baasi võitma?

2. [A] Millal lisada agent?

3. [B] 24 nädalat 10 h: kui palju koodiaega 40% osakaaluga?

4. [C] Valmista 15-minutiline esitlus: probleem, andmete ajastus, baas, mudel, kulud, tulemused, piirangud. Lisa üks tahtlikult vigane näide ja demonstreeri, kuidas test selle avastab. Esita ka üks piirang.
