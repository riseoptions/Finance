# Püsitasu pikaajaline mõju
algus,r,n=10000,.07,20
for f in [.002,.015]:
    lopp=algus*((1+r)*(1-f))**n
    print(f"Tasu {f:.1%}: {lopp:.2f} eurot")
