# Igapäevase 2× võimenduse teekond
from math import prod
r = [.10, 1/1.10-1]
indeks = prod(1+x for x in r)-1
voimendatud = prod(1+2*x for x in r)-1
print(f"Indeks: {indeks:.4%}; päevane 2x: {voimendatud:.4%}")
