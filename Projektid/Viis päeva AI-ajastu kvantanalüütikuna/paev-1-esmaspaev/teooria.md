# Päev 1: andmetest uurimisküsimuseni

[NARANG: ptk 2, 3, 8; JANSEN: ptk 2, 6–8]

**Süstemaatiline investeerimine** tähendab eelnevalt määratud korratavaid otsustusreegleid. See ei tähenda inimese puudumist. Inimene valib universumi, eesmärgi, kulud ja kontrollid. **Faktor** on tootluse ühine seletaja või varade omadus, näiteks turuekspositsioon, väärtus või momentum. Kõik korrelatsioonid pole kaubeldavad faktoripreemiad.

**Alpha** sõltub võrdlusmudelist. Baasportfellist kõrgem tootlus on aktiivtootlus, mitte automaatselt riskiga korrigeeritud alpha. Kui strateegia võtab rohkem tururiski, võib suurem tootlus tulla beetast. Meie portfellid on long-only; turuneutraalsust ei väideta.

## Hinnast tootluseni

[NÄIDE] Lihttootlus $r_t=P_t/P_{t-1}-1$ mõõdab väärtuse suhtelist muutust. Hind $P$ peab olema võrreldavas ühikus. Hinnad 100 ja 105 annavad 5%; Python: `105/100-1`. Kui dividend on juba korrigeeritud hindades, ära lisa seda uuesti.

Logaritmiline tootlus $\ell_t=\ln(P_t/P_{t-1})$ liitub ajas: 100 → 110 → 121 annab $2\ln(1.1)=\ln(1.21)$. Python: `np.log(1.1)*2`. Logtootlused ei liitu portfelli kaaludega täpselt samal viisil kui lihttootlused. Portfelli mootor kasutab lihttootlusi.

63 päeva momentum $m_t=P_t/P_{t-63}-1$ on tunnus, mitte 63 järgmise päeva prognoos. 100 → 115 annab 15%; see ei tähenda, et järgmise kuu tootlus on 5%. Reegli `mom63/3` kasutatakse ainult võrreldava suurusjärguga prognoosiproksina; järjestus jääb samaks.

## Andmeleping

| Väli | Tähendus | Kontroll |
|---|---|---|
| date | Hinnavaatluse aeg | Unikaalne, kasvav |
| price | Positiivne hinnaproksi | Pole NaN-i, lõpmatust ega nulli |
| signal | Millal tunnused teada on | Enne tehingut |
| entry | Millal positsioon avaneb | Pärast signaali |
| exit | Millal silt tervikuna realiseerub | Pärast sisenemist |
| source / retrieved_at | Päritolu ja laadimisaeg | Taastatav versioon |

Üldine punkt-ajas nõue: analüüsihetkel peab olema teada nii väärtus kui ka selle kättesaadavus. Raamatupidamisperioodi lõpp pole avaldamiskuupäev. Hiljem parandatud makroandmed võivad rikkuda ajaloolise testi, kui kasutatakse revisjoni, mida tol hetkel veel ei olnud.

## Pärisandmete haru

`python/laadi_parisandmed.py` laadib eraldi faili. See ei asenda põhisüsteemi sünteetilist sisendit. Nii ei segune ettevalmistatud õppetulemused kogemata teise allikaga. Yahoo/yfinance pole börsi ametlik punkt-ajas andmebaas; tasuta ligipääs ei anna automaatselt õigust andmeid edasi müüa või avalikult levitada. Kontrolli pakkuja tingimusi ja parandusi.

Joonista esmalt normaliseeritud hinnad ja päevatootlused. Vaata äärmusi, duplikaate ja pikki muutumatu hinna perioode. Suur muutus võib olla splitiviga või pärissündmus: ära eemalda seda üksnes sellepärast, et ta mudelit häirib.


Edasi: [praktikum](praktikum.md) · [ülesanded](ulesanded-lahendused.md)
