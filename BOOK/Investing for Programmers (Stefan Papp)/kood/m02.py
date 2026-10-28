"""[NÄIDE] Aruanded, suhtarvud ja kasvutees — vt mooduli selgitust."""
revenue,profit,shares,price=1000,100,50,30
print('EPS',profit/shares,'P/E',price/(profit/shares),'FCF',140-60)
print('Kahe rahavoo PV',round(100/1.1+110/1.1**2,2))
