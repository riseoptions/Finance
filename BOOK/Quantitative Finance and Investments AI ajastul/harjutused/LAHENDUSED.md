# Ülesannete vastused ja lahendused

## 01. Kvantinvesteerimise ajalugu ja areng

**1. Kas 2010. aasta närvivõrgumudel on generatiivne AI?**

Vastus: Mitte tingimata. Närvivõrk kirjeldab arhitektuuriperekonda; generatiivsus kirjeldab eesmärki.

**2. Miks ei tõesta 1000 testist parim kasumlik strateegia eelist?**

Vastus: Parim valiti sama juhusliku ajaloo alusel. Vajalikud on katsete register ja puutumata kinnitav valim.

**3. Arvuta 20 sõltumatu 5% testi puhul vähemalt ühe valepositiivse tõenäosus.**

Vastus: 1 − 0,95^20 ≈ 64,15%.

**4. Lahenduse kontroll:** Koosta uurimispäevik: idee, kuupäev, andmeversioon, kõik proovitud variandid, loobumise põhjus. Ära säilita ainult võitjaid.

Oodatav järelduse piir: Eelis peab üle elama sõltumatu kontrolli. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 02. Klassikaline statistika, faktorid ja portfellid

**1. Kas alfa 4% tõestab oskust?**

Vastus: Ei. Vaja on standardviga, perioodi, riskifaktoreid, kulusid ja valikuprotsessi.

**2. Mis juhtub hajutamisega, kui korrelatsioon tõuseb?**

Vastus: Muude tingimuste samaks jäädes suureneb portfelli dispersioon.

**3. Arvuta ülaltoodud portfelli risk korrelatsiooniga 0,5.**

Vastus: √0,03 = 17,32%.

**4. Lahenduse kontroll:** Käivita projekt ning ava kovariatsioon.csv. Võrdle võrdseid kaale ja pöördvolatiilsuse kaale. Viimane ei ole üldjuhul täielik riskipariteet, sest ei arvesta kõiki korrelatsioone.

Oodatav järelduse piir: Lihtne baas on kontrollvahend. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 03. Masinõpe aktsiaturu analüüsis

**1. Miks on juhuslik train_test_split probleem?**

Vastus: See segab ajarežiime ja võib tuua tulevikuinfo treeningusse.

**2. Kas SHAP tõestab põhjuslikkust?**

Vastus: Ei, see selgitab mudeli käitumist kasutatud andmete ja eelduste piires.

**3. Võidumäär 55%, võit 1%, kaotus 1%, kulu 0,15% igal tehingul: ootus?**

Vastus: 0,55% − 0,45% − 0,15% = −0,05%.

**4. Lahenduse kontroll:** Projektis võrdle ridge’i nullprognoosiga failis test_mse.csv. Vaata seejärel netotootlusi. Ära vali mudelit tagantjärele lõppkatse parima Sharpe’i järgi.

Oodatav järelduse piir: Õpi teisendus ainult minevikust. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 04. XGBoost, süvaõpe ja aegridade prognoos

**1. Kas XGBoost vajab standardiseerimist?**

Vastus: Puupõhine mudel üldiselt mitte; ridge’i puhul on see kasulik.

**2. Miks ei tohi early stopping jälgida lõppkatset?**

Vastus: Siis osaleb lõppkatse mudeli valikus ega ole enam sõltumatu.

**3. Arvuta kaks +0,4% parandust, η=0,1, algus 0%.**

Vastus: 0,08%, kui mõlemad parandused on fikseeritud; pärisõppes teine puu õpib juba uuest jäägist.

**4. Lahenduse kontroll:** Paigalda valikuline XGBoost. Projekt salvestab kõigi mudelite MSE ning valib ühe valideerimisest. Hoia testiperiood muutmata; lisa süvaõppemudel alles siis, kui oskad sama ajastust säilitada.

Oodatav järelduse piir: Mudeliperekond ei ennusta võitjat. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 05. Fundamentaalse, tehnilise ja kvantanalüüsi ühendamine

**1. Kas madal P/E tähendab alahinnatust?**

Vastus: Ei. Põhjuseks võivad olla väiksem kasv, suurem risk või ajutiselt kõrge kasum.

**2. Miks testida tunnuserühma eemaldamist?**

Vastus: Et eristada selle tegelikku lisaväärtust mudeli ülejäänud osast.

**3. Väärtusskoor 2, kvaliteet −1, momentum 0,5: keskmine?**

Vastus: 0,5. Positiivne suhteline skoor ei taga positiivset tootlust.

**4. Lahenduse kontroll:** Lisa hiljem projektile üks avaldamisajaga fundamentaaltunnus. Võrdle hinna-mudelit, fundamentaalmudelit ja nende ühendust sama kulumudeli ning testiperioodiga.

Oodatav järelduse piir: Uus tunnus peab õigustama oma kulu. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 06. Finantsandmed, alternatiivandmed ja ajaline korrektsus

**1. Kas tänased S&P 500 liikmed sobivad 2005. aasta universumiks?**

Vastus: Ei, see jätab välja hiljem kadunud ettevõtted ja lisab tulevasi võitjaid.

**2. Kas auto_adjust=True eemaldab kõik andmeprobleemid?**

Vastus: Ei. See aitab korporatiivsete sündmuste korrigeerimisega, kuid ei loo PIT-universumit ega garanteeri andmekvaliteeti.

**3. Aruanne avaldub pärast börsi sulgemist. Millal tohib seda kasutada?**

Vastus: Alles pärast avaldamist ja töötlemist; päevakauplemise näites järgmisel sobival sessioonil.

**4. Lahenduse kontroll:** 01_andmed.py genereerib vaikimisi SIM_A/B/C. --download valib ajaloolised AAPL/MSFT/JPM hinnad ainult tehnilise näite jaoks. See tänastest ellujääjatest valim ei tõenda üldist USA aktsiastrateegiat.

Oodatav järelduse piir: Sünteetiline test kontrollib mehhanismi, mitte alfat. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 07. AI abil hüpoteeside genereerimine ja kontrollimine

**1. Miks on AI pakutud usutav mehhanism ebapiisav?**

Vastus: See võib olla tagantjärele lugu; vaja on sõltumatut ja ajaliselt korrektset testi.

**2. Kas uus mudelinimi on uus majandushüpotees?**

Vastus: Ei. Algoritmi vahetamine ei loo majanduslikku põhjendust.

**3. Kulud 0,4%, brutolisatootlus 0,3% aastas: netolisaväärtus?**

Vastus: −0,1 protsendipunkti enne andme- ja arvutuskulusid.

**4. Lahenduse kontroll:** Kasuta uurimisprotokolli projekti juhendis. Küsi AI-lt kolm alternatiivset selgitust ja üks katse, mis sinu lemmikhüpoteesi ümber lükkaks.

Oodatav järelduse piir: Säilita ka ebaõnnestumised. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 08. LLM, RAG, teadmistegraaf ja AI-agent

**1. Kas iga Python-tsükkel on AI-agent?**

Vastus: Ei. Kindel skript võib olla automatiseeritud ilma mudelipõhise tööriistavalikuta.

**2. Kas õige allikaviide tähendab õiget vastust?**

Vastus: Ei, kontrollida tuleb ka seda, kas viidatud tekst toetab konkreetset väidet.

**3. 20 kontrollitud viitest 18 toetavad väidet; täpsus?**

Vastus: 90%. Veel tuleb mõõta puuduvaid fakte ja valesid viiteta väiteid.

**4. Lahenduse kontroll:** 07_rag_agent.py töötab esmalt lokaalse otsingu demonstratsioonina. --live-llm loob API kaudu tekstianalüüsi; --agent lubab kuni kolm piiratud tööriistavaliku sammu. Offline-režiim ei ole LLM ega AI-agent. Võrdle käsitsi koostatud vastusevõtmega, mitte mudeli enesehinnanguga.

Oodatav järelduse piir: Tööriista tulemus on andmed, mitte käsk. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 09. Algoritmiline kauplemine ja järeltestimine

**1. Miks ei saa sulgemishinna signaal alati sama sulgemishinnaga täituda?**

Vastus: Hind on teada alles sündmuse lõpus; korraldus peab jõudma varem või järgmisse tehinguvõimalusse.

**2. Kas kõrgsagedusstrateegiat saab hinnata päevahindadega?**

Vastus: Usaldusväärselt mitte: puuduvad järjekord, spread, latentsus ja hinnatee.

**3. Signaal esmaspäeva lõpus, tehing teisipäeva lõpus: milline päevatootlus on esimene?**

Vastus: Kolmapäeva sulgemine / teisipäeva sulgemine − 1.

**4. Lahenduse kontroll:** Leia projekt.py failist dataset ja comparison. Kontrolli käsitsi kolme kuupäevaga signaali, täitmishinna ja teenitud tootluse ajastust. Gap=2 on selle näite sildihorisondiga seotud, mitte universaalne soovitus.

Oodatav järelduse piir: Simulaatori kasum ei ole päristuru tõend. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 10. Optsioonid, futuurid, ETF-id ja muud instrumendid

**1. Call K=100, preemia 8, S_T=95: kasum?**

Vastus: −8 osaku kohta. Lepingu kordaja tuleb eraldi rakendada.

**2. ETF hind 101, NAV 100: preemia?**

Vastus: 1%. See ei ole garanteeritud arbitraažikasum.

**3. Miks on futuuri tootlus tagatise suhtes eksitav võrdlusalus?**

Vastus: Tagatis on vaid osa majanduslikust riskipositsioonist; võimendus suurendab mõlemat tootluse suunda.

**4. Lahenduse kontroll:** Käivita 10_instrumendid.py. Black–Scholesi näide eeldab Euroopa call’i, konstantseid parameetreid ja dividendide puudumist. Tulemus on õppehind, mitte tänane turukvoot.

Oodatav järelduse piir: ETF-i hind ja indeksipunktid on eri ühikud. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 11. Portfelli optimeerimine ja riskijuhtimine

**1. Miks võib võrdkaal keerukat optimumi võita?**

Vastus: See väldib osaliselt oodatava tootluse hinnanguviga ja liigset kontsentratsiooni.

**2. Kas 95% VaR 2% tähendab, et kaotus ei ületa 2%?**

Vastus: Ei. Mudeli järgi ületab kahju selle läve umbes 5% juhtudest; tegelik risk võib erineda.

**3. Kapital 100→80: milline tootlus taastab algtaseme?**

Vastus: 100/80−1=25%.

**4. Lahenduse kontroll:** Vaata portfell.csv ja kovariatsioon.csv. Projekt hindab riskiparameetrid ainult enne testiperioodi; võrdleb igapäevaselt taastatud võrdkaalu ja pöördvolatiilsust koos käibekuluga. Eeldus on õppeotstarbeline.

Oodatav järelduse piir: Riskipiirang peab töötama enne kriisi. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 12. Realistlik hindamine, kulud ja üleõppimine

**1. Bruto 8%, käive 40, kulu 10 bp: ligikaudne neto?**

Vastus: 8% − 4% = 4%, enne muid kulusid ja liitmise detaile.

**2. Mida tähendab negatiivne neto, aga positiivne prognoosikorrelatsioon?**

Vastus: Prognoosis võib olla infot, kuid valitud tehingureegel ei muuda seda kasumlikuks.

**3. Kas sama holdout’i 20 korda vaatamine säilitab sõltumatuse?**

Vastus: Ei, kui tulemused mõjutavad valikuid.

**4. Lahenduse kontroll:** Projekt arvutab kulud 0, 5, 10, 25 ja 50 bp juures. Kontrolli, kas valideerimisel valitud mudel jääb netos veenvaks. Bootstrap’i tulemus on tinglik olemasolevale ajaloole, mitte uus sõltumatu tõend.

Oodatav järelduse piir: Punktihinnang ei ole kindlus. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 13. Tänapäevase kvandi tööriistad ja tööpäev

**1. Miks salvestada CSV räsi?**

Vastus: Et teada, kas hilisem katse kasutas täpselt samu baite.

**2. Kas sama random seed tagab kõikjal sama tulemuse?**

Vastus: Ei, teegid, riistvara ja paralleelarvutus võivad erineda.

**3. Milline kontroll tuleb enne MSE arvutamist?**

Vastus: Ajastus, puuduvad read, duplikaadid ning sisendite ja sihtide vastavus.

**4. Lahenduse kontroll:** Alusta Thonnys: pandas, NumPy, scikit-learn, Matplotlib ja CSV. Lisa SQLite, kui vajad päringuid ja versioone; XGBoost pärast baasi. Colab sobib märkmike ja jagatava õppe jaoks. VS Code ning keerukam MLOps tulevad vajadusest.

Oodatav järelduse piir: Minimaalne tööriistakomplekt on tugev algus. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 14. AI eelised, piirangud ja riskid

**1. Kas mudeli „olen 95% kindel” on riskimõõt?**

Vastus: Mitte ilma eraldi kalibreerimise ja kontrollita.

**2. Kas andmeleket parandab tugevam regulariseerimine?**

Vastus: Ei. Lekkinud info tuleb eemaldada ja katse uuesti teha.

**3. AI säästab 60 min, kontroll 25 ja parandus 20: netosääst?**

Vastus: 15 minutit enne teenusekulu arvestamist.

**4. Lahenduse kontroll:** Koosta riskiregister: risk, võimalik kahju, avastamise kontroll, peatamistingimus, vastutaja. Katseta puuduva allika, tulevikudokumendi, vigase JSON-i ja keelatud tööriistaga.

Oodatav järelduse piir: Mudeli enesekindlus ei ole kalibreeritud tõenäosus. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 15. Tõenäolised arengud 2027–2030

**1. Milline väide on paremini põhjendatud: „AI kaotab kvandid” või „mõned ülesanded automatiseeruvad”?**

Vastus: Teine. See on konkreetsem ja mõõdetav; rollide täielik kadumine vajab palju tugevamat tõendit.

**2. Kas 2030. aasta täpne mudeliparemus on täna teada?**

Vastus: Ei. Võimalik on kirjeldada tingimusi ja mõõdikuid.

**3. 200 ülesannet hinnaga 0,50 ja 3 min ülevaatust: maht?**

Vastus: 100 eurot API-kulu ning 600 minutit ehk 10 tundi ülevaatust.

**4. Lahenduse kontroll:** Vaata iga kvartal üle kolm mõõdikut: faktivead, aeg, kogukulu. Võta uus tehnoloogia kasutusele alles siis, kui see ületab sinu baastöövoo ette määratud piirid.

Oodatav järelduse piir: Õpi oskusi, mitte ainult tootenimesid. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.

## 16. Isiklik õppe- ja arenguplaan

**1. Kas kursuse läbimiseks peab ML baasi võitma?**

Vastus: Ei. Tulemus peab olema korrektselt saadud ja piirangutega tõlgendatud.

**2. Millal lisada agent?**

Vastus: Kui fikseeritud töövoo piirang on selge ning agent parandab mõõdetavat kvaliteeti või kogukulu.

**3. 24 nädalat 10 h: kui palju koodiaega 40% osakaaluga?**

Vastus: 96 tundi.

**4. Lahenduse kontroll:** Valmista 15-minutiline esitlus: probleem, andmete ajastus, baas, mudel, kulud, tulemused, piirangud. Lisa üks tahtlikult vigane näide ja demonstreeri, kuidas test selle avastab.

Oodatav järelduse piir: Portfoolio peab olema korratav. Konkreetne arv sõltub andmeversioonist; hindamisel kontrolli protokolli järgimist.
