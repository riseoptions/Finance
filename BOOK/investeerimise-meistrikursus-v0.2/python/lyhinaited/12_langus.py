# Maksimaalne langus
vaartused = [100, 120, 90, 110, 130]
tipp, suurim = vaartused[0], 0
for v in vaartused:
    tipp = max(tipp,v)
    suurim = min(suurim,v/tipp-1)
print(f"Maksimaalne langus: {suurim:.2%}")
