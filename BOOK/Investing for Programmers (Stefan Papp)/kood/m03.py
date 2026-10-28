"""[NÄIDE] Andmed ja korratav uurimistöö — vt mooduli selgitust."""
import pandas as pd
from tuum import tootlused
p=pd.DataFrame({'hind':[100.,102.,101.]},index=pd.date_range('2024-01-01',periods=3))
print(tootlused(p).round(6).to_string())
