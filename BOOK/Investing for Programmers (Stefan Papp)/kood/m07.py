"""[NÄIDE] Risk, optsioonid ja futuurid — vt mooduli selgitust."""
from tuum import moodikud
import numpy as np
for s in [90,100,105,120]: print('Hind',s,'call kasum',max(s-100,0)-5,'put kasum',max(100-s,0)-4)
print('Maksimaalne langus',moodikud(np.array([.2,-.25,110/90-1]))['max_langus'])
