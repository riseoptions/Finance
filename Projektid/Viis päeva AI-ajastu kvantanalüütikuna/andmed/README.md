# Kaasasolevate andmete leping

`synteetilised_hinnad.csv`: 2012–2025 tööpäevade kuupäevad ja kuus `SYN_` hinnaseeriat. Hinnad genereerib `python/projekt.py::make_data`, seeme 20261030. Turu ühine normaalne müra, varaspetsiifiline müra, nõrk ajas muutuv autokorrelatsioon ja üks kunstlik stressiplokk. Kalender ei välista USA börsipühi. See pole Yahoo ega börsi ajalugu.

`paneel.csv`: eelmise faili tuletis; üks rida vara ja kuusignaali kohta, tunnused `mom21`, `mom63`, `vol21`, siht `y` ja kolm aega. Poolikud lõppperioodid jäetakse välja. Fail sisaldab tulevase tulemuse silti õppimise/hindamise jaoks; see ei anna luba seda prognoosi sisendisse panna.

`dokumendid.json`: kolm täielikult väljamõeldud eestikeelset teadet retrieval-demo jaoks. Need ei ole ettevõtete aruannete väljavõtted.

Sünteetilised andmed ja projekti enda kood on loodud selle õppeülesande jaoks; paketis pole raamatute andmekoopiaid. `paris_hinnad.csv` tekib ainult valikulise võrguskripti käivitamisel ja on `.gitignore`-is. Enne pärisandmete jagamist kontrolli nende kasutustingimusi.
