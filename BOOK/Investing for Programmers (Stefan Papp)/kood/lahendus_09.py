"""Iseseisva ülesande näidislahendus."""
from uurimisagent import invoke
try: invoke({'tool':'kauple'})
except ValueError: print('Lubamatu tööriist blokeeritud')
else: raise AssertionError('Tööriistade piirang puudub')
