"""[NÄIDE] Tuluportfell, võlakirjad ja krüpto — vt mooduli selgitust."""
from tuum import bond_price,ytm
p=bond_price()
print(f"Hind {p:.2f}; jooksev tootlus {50/p:.2%}; YTM {ytm(p):.2%}")
for y in [.04,.06,.08]: print(y,round(bond_price(y=y),2))
