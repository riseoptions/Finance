"""[NÄIDE] Investeerimise loogika ja finantsinstrumendid — vt mooduli selgitust."""
p0,p1,d,inf=100,108,2,0.04
r=(p1-p0+d)/p0
print(f"Kogutootlus {r:.2%}; reaaltootlus {(1+r)/(1+inf)-1:.2%}")
