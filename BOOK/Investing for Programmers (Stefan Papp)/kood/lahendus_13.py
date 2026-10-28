"""Iseseisva ülesande näidislahendus."""
from math import ceil
def tasuvus(arendus_tunnid,saast_min):
    if saast_min<=0: raise ValueError('Sääst peab olema positiivne')
    return ceil(arendus_tunnid*60/saast_min)
assert tasuvus(7,16)==27
print(tasuvus(7,16))
