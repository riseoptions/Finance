"""Iseseisva ülesande näidislahendus."""
def pe(price,eps): return price/eps if eps>0 else None
assert pe(30,2)==15
assert pe(30,-2) is None
print(pe(30,2),pe(30,-2))
