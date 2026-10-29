# Lõputest ja projektikaitsmine

## Lõputest: 10 sisulist küsimust

1. Sama päeva sulgemishinnast arvutatud signaal korrutatakse sama päeva tootlusega. Mis on viga ja kuidas seda testida?
2. Tänaste indeksiliikmete 15 aasta järeltest annab kõrge alfa. Milline andmeviga on tõenäoline ja kas lihtne train/test jaotus parandab selle?
3. Klassifikaatori võidumäär on 60%, keskmine võit 0,2%, kaotus 0,5%. Kas enne kulusid on eelis?
4. Tootlus on +10% ja −10%. Leia kumulatiivne tootlus ning selgita aritmeetilise keskmise eksitavust.
5. Strateegia bruto on 7%, aastane ühe suuna nominaalkäive 50 ja kulu 10 bp. Hinda netot.
6. Kahe võrdselt kaalutud vara volatiilsus on 20%. Leia portfellirisk korrelatsioonidega 0 ja 1.
7. Call K=100, preemia 8, lõpphind 105. Leia kasum ning selgita, miks õige hinnasuund ei aita.
8. RAG leiab õige dokumendi, aga vastus on vale. Nimeta vähemalt kolm võimalikku põhjust.
9. Agent kulutab käsitsi töö 100 minuti asemel 40 minutit, kontroll võtab 30 ja parandamine 45. Kas ajasääst on positiivne?
10. Sõnasta üks 2027–2030 prognoos nii, et see eristuks faktiväitest ja sisaldaks jälgitavat indikaatorit.

## Vastused

1. Tulevikuinfo/ajastuse viga. Testis peab enne signaali infoaega teenitud tootluse mõju positsioonile olema null; kursuse näites kasutatakse kahe rea nihet ja vastavat sihti.
2. Ellujäämis- ja universumivaliku kallutatus. Ajajaotus üksi ei paranda ajalooliselt valet universumit; vaja on tolleaegset koosseisu ja kadunud varade tootlusi.
3. 0,6×0,2%−0,4×0,5%=−0,08%. Ei ole.
4. 1,1×0,9−1=−1%. Keskmine päevatootlus on 0%, kuid kapital korrutatakse, mitte ei liideta.
5. 7%−50×0,1%=2% ligikaudu, enne muid kulusid.
6. 14,14% ja 20%. Hajutamisvõit sõltub korrelatsioonist.
7. max(105−100,0)−8=−3 osaku kohta. Tõus jäi preemia tasateenimiseks liiga väikeseks.
8. Vale periood/ühik, vale lõigu tõlgendus, puuduva tabeli ignoreerimine, hallutsinatsioon, eksitav viide või eeltreeningust pärit kõrvalteadmine.
9. 100−(40+30+45)=−15 minutit. Ajavõitu ei ole; API-kulu muudab netotasuvust veel.
10. Näidis: „Kui dokumentide faktivigade määr sõltumatul testil väheneb, võib kontrollitud LLM-analüüs levida. Jälgin kord kvartalis veamäära, netoaega ja kulu.” See ei luba turuületavat tootlust.

Iga vastus 0–2 punkti: vale/puuduv 0, osaline 1, põhjendatud ja õige 2. Lävend 14/20; küsimuste 1 ja 2 sisulised vead tuleb enne projekti heakskiitu parandada.

## Lõputöö: reprodutseeritav uuring, mitte ilus kapitalikõver

Esita uurimisprotokoll, andmete päritolu ja räsi, tunnuste/sihtide ajastus, lihtne baas, üks ML-võrdlus, kulutundlikkus, portfelli risk ning 1–2 lehekülje järeldus. Lisa RAG/agent ainult uurimisabi osana; võrdle selle kvaliteeti käsitsi võtmega.

| Kriteerium | Punktid | Kontroll |
|---|---:|---|
| Küsimus ja baas | 15 | Hüpotees on ümberlükatav, baas õiglane |
| Andmed ja ajastus | 25 | PIT, nihked, jaotus, puuduvad read |
| Mudel ja katsete register | 15 | Valik valideerimisest; kõik variandid nähtavad |
| Kulud ja risk | 20 | Neto, MDD, käive, tundlikkus |
| Korratavus | 15 | Teine inimene käivitab sama töövoo |
| Selgitus ja piirangud | 10 | Ei esita simulatsiooni turu tõendina |

Lävend 70/100. Kriitiline andmeleke, võltsitud allikas või simuleeritud tulemuse ajaloolisena esitamine tähendab parandust enne läbimist, sõltumata summast. Kõrge tootlus ei anna iseenesest lisapunkte.
