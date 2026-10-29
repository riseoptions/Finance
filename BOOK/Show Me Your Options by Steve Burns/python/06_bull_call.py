# Bull call spread’i graafik
# Õppenäide; hinnad ei ole turuandmed.
import matplotlib.pyplot as plt
K1=100;K2=110;deebet=4;M=100
hinnad=list(range(70,141))
pnl=[(max(S-K1,0)-max(S-K2,0)-deebet)*M for S in hinnad]
plt.plot(hinnad,pnl);plt.axhline(0,color="gray")
plt.xlabel("S tähtajal (USD)");plt.ylabel("P/L kombinatsioonile (USD)")
plt.title("Bull call spread: lõpptähtaja P/L");plt.grid();plt.show()
