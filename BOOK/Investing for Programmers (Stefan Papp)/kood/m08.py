"""[NÄIDE] Masinõpe: baasmeetodist ausa hindamiseni — vt mooduli selgitust."""
from tuum import demo_hinnad,ml_vordlus
result,split=ml_vordlus(demo_hinnad().iloc[:,0])
print(result.round(6).to_string(index=False));print(split)
