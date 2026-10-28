"""[NÄIDE] Tootlus, portfell ja võrdlusindeks — vt mooduli selgitust."""
import pandas as pd
from tuum import osta_hoia
p=pd.DataFrame({'A':[100,120],'B':[100,100]})
print(f"Portfelli tootlus {osta_hoia(p,[.5,.5]).iloc[0]:.2%}")
print(f"A lõppkaal {120/220:.2%}")
