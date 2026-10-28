# Aritmeetiline keskmine ja CAGR
from math import prod
r = [0.20, -0.20]
aritmeetiline = sum(r) / len(r)
kasvutegur = prod(1 + x for x in r)
cagr = kasvutegur ** (1 / len(r)) - 1
print(f"Aritmeetiline: {aritmeetiline:.2%}")
print(f"Kogutootlus: {kasvutegur-1:.2%}; CAGR: {cagr:.4%}")
