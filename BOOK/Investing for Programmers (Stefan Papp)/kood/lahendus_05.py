"""Iseseisva ülesande näidislahendus."""
from tuum import ytm,bond_price
y=ytm(950)
assert abs(bond_price(y=y)-950)<1e-8
print(f'YTM {y:.4%}')
