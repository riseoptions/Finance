"""Iseseisva ülesande näidislahendus."""
import pandas as pd
from tuum import kontrolli_hindu
bad=pd.DataFrame({'x':[10,11]},index=['2024-01-01','2024-01-01'])
try: kontrolli_hindu(bad)
except ValueError: print('Duplikaat tuvastati')
else: raise AssertionError('Kontroll puudub')
