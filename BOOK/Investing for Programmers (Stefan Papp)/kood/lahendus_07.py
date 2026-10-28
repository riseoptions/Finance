"""Iseseisva ülesande näidislahendus."""
def kaitstud(s): return s-100+max(95-s,0)-3
assert kaitstud(70)==-8 and kaitstud(120)==17
print(kaitstud(70),kaitstud(120))
