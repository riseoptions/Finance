# Kolmapäev: päev 3


## A. 09.05 – „Proovime XGBoosti?”

[SIMULATSIOON] Noah pakub puupõhist mudelit. Maarika vastab: „Enne otsustame, mida ta ennustab.” Nad valivad sama järgmise hoideperioodi tootluse, mida kasutatakse simulatsioonis. Suuna täpsus üksi ei vasta kapitali jaotamise küsimusele.

## B. Kolm tõsiselt võetavat alternatiivi

Reegel järjestab 63 päeva momendi järgi. Ridge-regressioon õpib 21 ja 63 päeva momendi ning 21 päeva volatiilsuse lineaarse seose tulevase tootlusega. Random Forest lubab mittelineaarseid tingimusi, näiteks erinevat momentumi mõju kõrge ja madala volatiilsuse ajal.

XGBoost on asjakohane lisakatse, kuid pole vajalik neljas sõltuvus põhiprojekti käivitamiseks. Mets on selles komplektis päriselt käivitatud ML-võrdlus. Närvivõrk jäetakse kõrvale: vähesed sõltumatud kuud ei õigusta seda ainult moekuse tõttu.

## C. 10.40 – Inseneri ja uurija erimeelsus

Noah: „Mets sobitab treeningandmeid paremini.”

Daniel: „Kas sa hindad õppimisvõimet või uut infot?”

Maarika: „Vaatame kuupõhist walk-forward-tulemust. Sama kuu varad ei lähe eri pooltele.”

Noah leiab, et `StandardScaler` oli esialgses visandis sobitatud kogu tabelile. Isegi hinnasildi kasutamiseta annab tuleviku jaotus infot. Nad panevad skaleerija Ridge'iga samasse pipeline'i ja sobitavad ainult varem lõppenud perioodidele.

## D. Intuitsioon ja allikad

Ridge on nagu mõõdukas nõuandja: ta kahandab tugevaid koefitsiente, et vähendada juhuslikke äärmusi. Mets küsib palju väikseid tingimuslikke küsimusi ja keskmistab puude vastused. [JANSEN] Peatükid 11–12 käsitlevad regulaarimist ja puuansambleid; peatükk 7 seab hindamise ajapiirid. [NARANG] Peatükk 3 eristab teooria- ja andmepõhiseid alpha-mudeleid.

## E. 55% täpsus võib hävitada kapitali

[NÄIDE] Mudel võidab 55% kordadest 1 euro ja kaotab 45% kordadest 1,5 eurot. Oodatav tulemus on $0.55\cdot1-0.45\cdot1.5=-0.125$ eurot enne kulusid. Klassifitseerimistäpsus ei mõõda võidu ja kaotuse suurust.

Meie mudelid on regressioonimudelid. Precision ja recall arvutatakse nende prognoosi märgist ainult abidiagnostikana. Portfelli kaks suurimat skoori valitakse ka siis, kui mõlemad on negatiivsed; märgipõhine klassifikatsioon ei ole tegelik orderireegel.

## F. 13.45 – Võrdlus ja LLM

[PRAKTIKA] Käivita `python/paev3.py`. Vaata valideerimise RMSE-d, precision'it, recall'i, käivet ja netotootlust koos. Madalam RMSE võib tuleneda keskmise lähedale ennustamisest ega pruugi anda head järjestust.

Maarika palub LLM-il selgitada oma funktsiooni, mitte leida „parimat aktsiat”. Ta annab sisendiks koodi ja protokolli ning nõuab vastusest näidet, kus välja `exit` väär kasutamine põhjustaks leket. Noah kontrollib soovitatud parandust käsitsi testiga.

Dokumendiotsingu demos filtreerib retriiver tekstid avaldamisaja järgi. Üks hiljem avaldatud kasumiteade jäetakse välja. LLM-i eeltreening võib siiski sisaldada tulevikusündmusi: ajalooline prompt pole ajamasin.

## G. 15.50 – Parema mudeli hind

Valideerimise parandused on väikesed ja kõik strateegiad võivad jääda baasist maha. ML tekitab sagedamini ümberjaotusi. Noah möönab: „Kiire prognoos pole kogu kulu. Lisanduvad andmed, seire ja uurimise aeg.” Maarika ei vali metsast võitjat selle järgi, et see kõlab kaasaegsemalt.

## H. 16.45 – Päeva otsus

Kõik kolm meetodit jäävad võrdlustabelisse. Operatiivseks harjutuseks kasutatakse kõige selgemat momentum-reeglit, mitte statistiliselt tõendatud parimat mudelit. LLM jääb koodi ja dokumentide kontrolli abiliseks. Agent ei saa orderiõigust.

## I. Õhtune märkmik

**Viis mõistet:** tunnus, sihtmuutuja, regulaarimine, walk-forward, RAG.

**Põhimõtted:** võrdle sama ülesannet; sobita teisendused ainult minevikul; klassifitseerimise tulemus pole kasum; keerukuse lisakasu peab katma lisakulu. Homme küsib Priya, kui palju kapitali üldse eraldada.


---

Edasi: [teooria](teooria.md) · [praktikum](praktikum.md) · [ülesanded ja lahendused](ulesanded-lahendused.md) · [sisukord](../README.md)
