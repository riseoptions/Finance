"""Iseseisva ülesande näidislahendus."""
import pandas as pd
from tuum import osta_hoia,tootlused
p=pd.DataFrame({'A':[100,120,120],'B':[100,100,120]})
bh=(1+osta_hoia(p,[.5,.5])).prod()-1
rb=(1+tootlused(p).mean(axis=1)).prod()-1
print('Osta-hoia',round(bh,4),'tasakaalustatud kuludeta',round(rb,4))
assert abs(bh-.2)<1e-12 and abs(rb-.21)<1e-12
