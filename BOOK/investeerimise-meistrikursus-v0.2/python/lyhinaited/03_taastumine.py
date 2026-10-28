# Kahjumist taastumine
for kahjum in (0.10, 0.25, 0.50, 0.80):
    vajalik = kahjum / (1 - kahjum)
    print(f"Kahjum {kahjum:.0%}: taastumiseks {vajalik:.2%}")
