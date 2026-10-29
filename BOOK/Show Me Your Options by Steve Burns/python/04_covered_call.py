# Covered call’i graafik
# Õppenäide; hinnad ei ole turuandmed.
import matplotlib.pyplot as plt
S0=100;K=105;preemia=3;M=100
hinnad=list(range(0,151))
pnl=[(S-S0+preemia-max(S-K,0))*M for S in hinnad]
plt.plot(hinnad,pnl);plt.axhline(0,color="gray")
plt.xlabel("S tähtajal (USD)");plt.ylabel("P/L 100 aktsiale + 1 short call (USD)")
plt.title("Covered call: lõpptähtaja P/L");plt.grid();plt.show()
