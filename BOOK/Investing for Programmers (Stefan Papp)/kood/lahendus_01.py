"""Iseseisva ülesande näidislahendus."""
def kogutootlus(p0,p1,d=0):
    if p0<=0: raise ValueError('Ostuhind peab olema positiivne')
    return (p1-p0+d)/p0
assert abs(kogutootlus(50,54,1)-.1)<1e-12
print(kogutootlus(50,54,1))
