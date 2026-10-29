# Straddle’i graafik
# Õppenäide; hinnad ei ole turuandmed.
import matplotlib.pyplot as plt
K=100;kogukulu=12;M=100
hinnad=list(range(50,151))
pnl=[(abs(S-K)-kogukulu)*M for S in hinnad]
plt.plot(hinnad,pnl);plt.axhline(0,color="gray")
plt.xlabel("S tähtajal (USD)");plt.ylabel("P/L kombinatsioonile (USD)")
plt.title("Long straddle: lõpptähtaja P/L");plt.grid();plt.show()
