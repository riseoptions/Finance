# IV. Strateegiate atlas

[Tagasi](../README.md)

## Kuidas lugeda

Kõigis terminalnäidetes S₀=100 USD, kordaja M=100 ja sama lõpptähtaeg. Preemiad on väljamõeldud õppehinnad. Üks aktsiajalg tähendab 100 aktsiat. Valemid kehtivad kulude, dividendide ja intressita ning eeldavad, et kogu kombinatsiooni arveldamine toimub kooskõlas. **Payoff** on jalgade terminalväljamakse; **P/L** lahutab algse netoväljamineku. Aktsiaga variandil sisaldab payoff aktsia müügiväärtust. Graafikud näitavad ühe alusvaraühiku summasid.

Debit tähendab raha väljamaksmist ja credit raha laekumist; need on rahavoo perekonnad, mitte kaks kindlat strateegiat. Bull call ja bear put on allpool debit-spread’id; bull put ja bear call credit-spread’id.

## Ühised valemid

C(K)=max(S−K,0), P(K)=max(K−S,0). Liida pikkade jalgade väljamaksed, lahuta lühikeste omad ja lahuta algne netokulu. Kogu lepingu P/L = 100×ühiku P/L.

## Strateegiad

| Strateegia | Maksimaalne kasum USD | Maksimaalne kahju USD | Tähtaja tasuvuspiir(id) |
|---|---:|---:|---|
| [Long call](01-long-call.md) | Piiramatu | 300,00 | 108,00 |
| [Long put](02-long-put.md) | 9200,00 | 300,00 | 92,00 |
| [Short call (katmata)](03-short-call.md) | 300,00 | Piiramatu | 108,00 |
| [Short put](04-short-put.md) | 300,00 | 9200,00 | 92,00 |
| [Covered call](05-covered-call.md) | 800,00 | 9700,00 | 97,00 |
| [Cash-secured put](06-cash-secured-put.md) | 300,00 | 9200,00 | 92,00 |
| [Protective put](07-protective-put.md) | Piiramatu | 800,00 | 103,00 |
| [Bull call spread (debit)](08-bull-call.md) | 600,00 | 400,00 | 104,00 |
| [Bear put spread (debit)](09-bear-put.md) | 400,00 | 600,00 | 104,00 |
| [Bull put spread (credit)](10-bull-put.md) | 400,00 | 600,00 | 96,00 |
| [Bear call spread (credit)](11-bear-call.md) | 400,00 | 600,00 | 104,00 |
| [Long straddle](12-straddle.md) | Piiramatu | 1200,00 | 88,00; 112,00 |
| [Long strangle](13-strangle.md) | Piiramatu | 600,00 | 89,00; 111,00 |
| [Long call butterfly](14-butterfly.md) | 800,00 | 200,00 | 92,00; 108,00 |
| [Iron condor (credit)](15-iron-condor.md) | 200,00 | 300,00 | 93,00; 107,00 |
| [Collar](16-collar.md) | 500,00 | 500,00 | 100,00 |
| [Synthetic long (call − put)](17-synthetic-long.md) | Piiramatu | 10000,00 | 100,00 |
| [Call ratio spread 1×2](18-ratio.md) | 800,00 | Piiramatu | 102,00; 118,00 |
| [Iron butterfly (credit)](19-iron-butterfly.md) | 800,00 | 200,00 | 92,00; 108,00 |
| [Long call condor](20-call-condor.md) | 300,00 | 200,00 | 92,00; 108,00 |
| [Reverse call butterfly](21-reverse-butterfly.md) | 200,00 | 800,00 | 92,00; 108,00 |

## Eri tähtajad ja dünaamilised strateegiad

- [Calendar ja diagonal spread](22-calendar-diagonal.md): mudelipõhised vahekuupäeva graafikud.
- [Sünteetika, delta-neutraalsus, wheel ja riskimaandamine](23-sunteetika-wheel.md).

Sõna „straddle” või „strangle” võib tähistada ka müüdud kombinatsiooni. Siin põhikaartidel on **ostetud** variandid; müüdud variantide terminal-P/L on täpselt vastasmärgiga. Short straddle’i ja short strangle’i tõususuunaline kahju on katmata kujul piiramatu. Iron condor lisab short strangle’ile kaitsvad tiivad.
