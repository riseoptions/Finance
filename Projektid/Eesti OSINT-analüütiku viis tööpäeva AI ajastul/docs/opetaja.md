# Õpetaja käsiraamat

Sihtgrupp: Pythoni ja SQLi algoskusega õppija. Viis päeva annab juhendatud terviktöö kogemuse, mitte automaatselt kutsepädevust. Risto varasema matemaatikaõpetaja ja tarkvaratestija kogemuse jaoks on rõhk arvulisel kontrollil, vigaste eelduste leidmisel ning meetodi õpetamisel.

Maht: **20 × 90 min = 30 tundi juhendatud tööd**, lisaks viis päeva igaühes 1 tund ülevaatust ja kuni 1 tund iseseisvat viimistlust: kokku 35–40 tundi. Päevas neli moodulit: 09.00–10.30, 10.45–12.15, 13.00–14.30, 14.45–16.15; kell 16.15–17.00 üleandmine. Tehniline paigaldus tee võimalusel enne kursust.

## Päevade õpetamisplaan

| Päev | Moodulid | Demonstratsioon | Õppija päevatulemus | Levinud eksimus |
|---|---|---|---|---|
| 1 | 1–4 | Muuda faili üks bait; võrdle räsisid | Uurimisplaan, allikavalik, tõendiregister | Räsi võrdsustatakse tõesusega |
| 2 | 5–8 | Käivita import kaks korda ja võrdle ridu | SQLite + hinnavõrdlus | Lepingusumma nimetatakse kuluks |
| 3 | 9–12 | Näita alguudist, kordust ja parandust | Väitemaatriks + avaldamisajatelg | Kolm teksti loetakse kolmeks sõltumatuks allikaks |
| 4 | 13–16 | Võrdle keskmist mediaaniga ja näita grupileket | Statistika, seosegraaf, ML mõõdikud | Kõrvalekalle nimetatakse rikkumiseks |
| 5 | 17–20 | Esita olematu viide ja ründetekst | Kontrollitud raport + 5 min õpetamine | Viite olemasolu võrdsustatakse järelduse õigsusega |

## Ühe mooduli 90-minutiline tunnikava

10 min: tööolukord ja eelennustus. 15 min: mõiste, üks arvuline või tekstiline näide. 20 min: õpetaja käivitatav demo. 30 min: iseseisev praktiline ülesanne. 10 min: paarilise kontroll algtõendiga. 5 min: väljumispilet „tean / järeldan / ei tea”. Iga mooduli fail sisaldab täpset tööolukorda, tehnilist käsku, kolme taseme harjutusi ja viit vastustega küsimust.

## Tööleht (kopeeri iga päeva jaoks)

- Uurimisküsimus ja ulatus:
- Väide ning konkureeriv seletus:
- Tõendi ID, URL, avaldamisaeg, kogumisaeg:
- Mida dokument sõnaselgelt ütleb:
- Milline osa on minu järeldus:
- Vasturääkiv või puuduv tõend:
- Käivitatud kood ja tulemus:
- Õigus/tingimus, mille alusel andmeid kasutan:
- Mida muudaks järgmine otsustav tõend:
- Kaaslase kontroll ja parandus:

## Lõputöö hindamine (100 punkti)

| Valdkond | Punkte | Täispunktide tingimus |
|---|---:|---|
| Uurimisküsimus ja ulatus | 15 | Vastatav küsimus, alternatiivid, peatumisreegel |
| Tõendid ja päritolu | 20 | Iga põhiväide jälgitav, aeg ja versioon eristatud |
| Python/SQL korratavus | 20 | Käivitatav import, kordus ei dubleeri, arvutused õiged |
| Analüütiline mõtlemine | 20 | 20%/−4% selgitus, sõltuvus ja teadmatus eristatud |
| ML/RAG hindamine | 10 | Baasjoon, lekke vältimine, testitulemuste piirid |
| Aruanne ja õpetamine | 15 | Selge kokkuvõte, põhjendatud piirangud, kaaslane mõistab |

Lävend 70 punkti ning puuduvad kriitilised vead: fiktiivset andmestikku ei esitata pärisjuhtumina, isikuid ei profileerita, puuduvat tõendit ei leiutata, piiranguid ei ületata. Kui mõni neist esineb, parandab õppija töö enne lõpetamist. AI abiga vastamine on lubatud, kuid õppija avab iga viidatud tõendi ja selgitab arvutust ise.

## Lõputest: 10 otsustusülesannet (igaüks 2 punkti)

1. Uudis 1,5 miljonit, leping 1,2 miljonit: mida raporteerid? **Vastus:** leping ja paranduse ajalugu; alguudise väidet ei kinnita.
2. 1,2 miljonit vs 1 miljon ja 1,25 miljonit: kasvud? **Vastus:** 20% ja −4%, nimetatud baaside suhtes.
3. Kaks organisatsiooni samal aadressil: järeldus? **Vastus:** ühine aadress; kontrolli/omandit ei järeldu.
4. Sotsiaalmeedias 80% vastuseisu: elanike seisukoht? **Vastus:** teadmata, valim pole esinduslik.
5. Sama tõendi teine import: ridade arv? **Vastus:** tõendiversioone ei lisandu, auditikirje võib lisanduda.
6. 10000 juhtu, 1% baasmäär, 80% tundlikkus, 90% spetsiifilisus: positiivse häire tabavus? **Vastus:** 80/(80+990)=7,48%.
7. Ümberkirjutatud tekst mõlemas ML-jaotuses: probleem? **Vastus:** grupileke; jaota päritolu järgi.
8. RAG leiab eelarve, küsimus küsib makseid: vastus? **Vastus:** maksete kohta tõend puudub.
9. Õige viide ja täpne tsitaat, kuid „ettevõtted on süüdi”: piisav kontroll? **Vastus:** ei, järelduse semantiline tugi puudub.
10. Agent säästab päringuid, kuid suurendab kontrolliaega: kas kasulik? **Vastus:** mõõda koguaega ja vigade kulu; päringute arv üksi ei näita kasu.

Hinda 1 punkt õige otsuse ja 1 punkt põhjenduse eest. Süvendatud suulisel kaitsmisel vali 100 küsimuse kogust üks igast päevast.

## Õpetaja järelanalüüs

Lase õppijal esmalt teha üks ekslik, kuid usutav järeldus ja seejärel see tõendiga parandada. Märgi eraldi koodi viga, allika viga, tõlgendusviga ja ulatuse viga. Õnnestunud õppimine on see, kui õppija hakkab neid iseseisvalt eristama. Väliste teenuste tõrke korral jätkub kogu põhitöö sünteetiliste andmetega; tõrget ei peideta.
