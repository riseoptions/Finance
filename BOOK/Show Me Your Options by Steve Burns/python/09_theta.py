# Ajaväärtuse mudelikõver
# Õppenäide; hinnad ei ole turuandmed.
import matplotlib.pyplot as plt
from mudel import hind
S=K=100;sigma=0.2
paevad=list(range(0,61))
hinnad=[hind(S,K,d/365,sigma) for d in paevad]
print("30 päeva hind:",hind(S,K,30/365,sigma))
plt.plot(paevad,hinnad);plt.gca().invert_xaxis()
plt.xlabel("Allesjäänud kalendripäevad");plt.ylabel("ATM call’i mudelihind (USD/ühik)")
plt.title("Fikseeritud S=K=100, IV 20%, r=q=0")
plt.grid();plt.show()
