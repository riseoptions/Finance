"""Iseseisva ülesande näidislahendus."""
import pandas as pd
s=pd.Series([10,12,14,16]).rolling(3).mean()
assert s.iloc[:2].isna().all() and list(s.iloc[2:])==[12,14]
print(s.to_string())
