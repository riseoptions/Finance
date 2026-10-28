# Võlakirja hind
nimivaartus, kupong, tootlus, aastad = 1000, 0.05, 0.06, 3
hind = sum(nimivaartus * kupong / (1+tootlus)**t
           for t in range(1, aastad+1))
hind += nimivaartus / (1+tootlus)**aastad
print(f"Hind: {hind:.4f}")
