# Kursuse lõputest

Aeg 60–90 minutit. 20 avatud ülesannet × 5 punkti = 100 punkti. Igas ülesandes: põhimõte 2 p, arvutus või rakendus 2 p, eeldus/piirang 1 p. Lävend 60 p. Vastused on faili teises pooles; õpetaja võib jagada õppijale ainult esimese poole.

## Küsimused

1. Selgita indeksi, indeksfondi, ETF-i ja ETF-i osaku erinevust.
2. Aktsia 100 → 109, dividend 2. Leia kogutootlus. Mis muutub korrigeeritud hinnasarja kasutamisel?
3. Ettevõtte kasum 80, aktsiaid 40, hind 30. Leia EPS ja P/E; nimeta üks võrdlemise piirang.
4. Ettevõtte müügitulu 1000 → 1200, marginaal 10% → 5%. Leia kasumi muutus.
5. Kaks perioodi +25% ja −20%. Leia liittootlus ning selgita aritmeetilise keskmise probleemi.
6. Portfell: 60% vara tootlusega 10%, 40% vara tootlusega −5%. Leia periooditootlus.
7. Portfell 100 → 130 → 91 → 105. Leia maksimaalne langus ja kogutootlus.
8. Aasta pärast makstakse 1050, hind 980. Leia YTM.
9. Staking 10% tokenites, tokeni hind −30%. Leia rahaline tootlus.
10. Call: K=100, preemia 4, lõpphind 112, kordaja 100. Leia payoff, kasum ja tasuvuspunkt.
11. Pikk futuur: hind 50 → 48, kordaja 100, tagatis 500. Leia kasum ja tagatise suhtes tootlus.
12. Selgita, miks 95% VaR 1000 ei tähenda maksimaalset kahju 1000.
13. Hinnatabelis toimub split 2 : 1. Kuidas eristad hinnalangust ja korrektsiooni?
14. EPS puudutas 31.12 lõppenud aastat ja avaldati 15.02. Millal tohib seda backtestis kasutada?
15. Mudel ennustab 100 päevast 61 õigesti; 64 päeva olid tõusupäevad. Kas ta ületab enamuse baasi?
16. Milles seisneb standardiseerija kogu andmestikul sobitamise viga?
17. Otsus tekib esmaspäeva sulgemisel, tehing teisipäeva sulgemisel. Milline close-to-close tootlus kuulub esimesele positsioonipäevale?
18. RAG vastuses on korrektne URL, aga väidet vastaval lehel pole. Kas vastus on tõendatud? Kuidas seda testida?
19. Ettevõtte pre-money 8 mln, uus raha 2 mln. Sul oli 10% ja sa ei osale. Kui suur on uusinvestori ning sinu osalus?
20. Millal on põhjendatud lisada analüüsisüsteemi agent? Paku kaks mõõdikut ja lihtsam võrdlusvariant.

---

## Vastused ja selgitused

1. Indeks on arvutus; indeksfond järgib seda; ETF on börsil kaubeldav fond; osak on investori omatav väärtpaber. ETF võib olla aktiivne ning indeksfond börsiväline.
2. (109−100+2)/100=11%. Korrigeeritud kogutootluse lähendile ei lisata dividendi uuesti; kontrolli andmeallika korrektsiooni sisu.
3. EPS=80/40=2; P/E=30/2=15. Kasumiperiood, ühekordsed mõjud ning sektori eripära võivad võrdlust muuta.
4. Kasum 100 → 60, muutus −40%. Müügitulu kasv üksi ei määra kasumi kasvu.
5. 1,25×0,8−1=0%. Aritmeetiline keskmine on +2,5%, kuid see pole kapitali liitkasv.
6. 0,6×0,10+0,4×(−0,05)=4%, eeldades perioodi alguse kaale ja kulude puudumist.
7. 91/130−1=−30% max drawdown; 105/100−1=+5% kogutootlus. Lõpptulemus varjab vahepealset riski.
8. 1050/980−1≈7,1429%, kui makse toimub täpselt aasta pärast ja laekub tervikuna.
9. 1,10×0,70−1=−23%, enne kulusid ja makse.
10. Payoff=(112−100)×100=1200; preemia 400; kasum 800. Tasuvuspunkt 104 enne kulusid. See on tulemus tähtajal.
11. (48−50)×100=−200; −200/500=−40%. Tagatis pole kahjumi ülempiir.
12. VaR on kvantiil: mudelis ligikaudu 5% juhtudest on kahju suurem. Saba suurust kirjeldab muu hulgas ES; mudel võib ka eksida.
13. Kontrolli corporate actions infot, osakute arvu ja korrigeeritud hinnasarja. 1×100 muutub 2×50-ks ilma väärtuse kaotuseta.
14. Pärast tegelikku avaldamist ja arvestades kellaaega ning täitmisviivitust; 31.12 kasutamine oleks tulevikuinfo.
15. Ei: baasi täpsus 64%, mudelil 61%. Tulu hindamine vajab lisaks muutuste suurust ja kulusid.
16. Testiperioodi jaotus mõjutab treeningtunnuseid. Sobita standardiseerija ainult treeningule ja rakenda testile muutmata.
17. Teisipäeva sulgemisest kolmapäeva sulgemiseni. Teisipäevase täitmise kulu tuleb juba teisipäeval.
18. Ei. Koosta väide–allikalõik paarid ja kontrolli, kas lõik toetab väidet, perioodi ja ühikut. Viite olemasolu testist üksi ei piisa.
19. Post-money=10 mln, uus investor 20%; sinu osalus 10%×80%=8%, kui muid lahjenemismehhanisme pole.
20. Agent on põhjendatud, kui järgmine tööriist sõltub eelnevast tulemusest ja lisakasu on mõõdetud. Võrdle fikseeritud töövooga; mõõda näiteks tõendatud väidete määra ja inimese kontrollimiseks kulunud aega, lisaks API kulu.
