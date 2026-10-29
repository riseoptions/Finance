# Delta-lähendus ja täpsem mudel
# Õppenäide; hinnad ei ole turuandmed.
import matplotlib.pyplot as plt
from math import log,sqrt
from mudel import hind,N
S0=100;K=100;T=30/365;sigma=0.2
v0=hind(S0,K,T,sigma)
d1=(log(S0/K)+sigma*sigma*T/2)/(sigma*sqrt(T))
delta=N(d1)
hinnad=list(range(80,121))
plt.plot(hinnad,[hind(S,K,T,sigma) for S in hinnad],label="BSM hind")
plt.plot(hinnad,[v0+delta*(S-S0) for S in hinnad],"--",label="Lokaalne delta-lähendus")
print("Algdelta:",delta)
plt.xlabel("S täna (USD)");plt.ylabel("Call’i hind ühiku kohta (USD)")
plt.title("Enne tähtaega: 30 päeva alles, IV 20%")
plt.legend();plt.grid();plt.show()
