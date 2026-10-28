"""[NÄIDE] Erakapital ja iduettevõtete hindamine — vt mooduli selgitust."""
pre,investment=4_000_000,1_000_000
print(f"Uue investori osalus {investment/(pre+investment):.1%}")
print(f"Vana 10% osalus pärast vooru {.1*(1-.2):.1%}")
print('Runway kuudes',600_000/50_000)
print(f"Kümne aasta CAGR {(15000/10000)**.1-1:.2%}")
