# Cash-secured put’i graafik
# Õppenäide; hinnad ei ole turuandmed.
import matplotlib.pyplot as plt
K=95;preemia=3;M=100
hinnad=list(range(0,151))
pnl=[(preemia-max(K-S,0))*M for S in hinnad]
print("Reserveeritud osturaha:",K*M)
plt.plot(hinnad,pnl);plt.axhline(0,color="gray")
plt.xlabel("S tähtajal (USD)");plt.ylabel("P/L lepingu kohta (USD)")
plt.title("Cash-secured put: lõpptähtaja P/L");plt.grid();plt.show()
