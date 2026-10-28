"""Sisulised matemaatiliste omaduste kontrollid, mitte turu empiiriline test."""
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from math import isclose, sqrt
import numpy as np


def lae(nimi):
    p = Path(__file__).parent / nimi
    spec = spec_from_file_location(p.stem, p)
    m = module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

h = lae('02_hajutamine.py')
v = lae('03_varjatud_risk.py')
f = lae('01_fondivoitjad.py')
assert isclose(h.portfelli_sigma(10,.2,0), .2/sqrt(10))
assert isclose(h.portfelli_sigma(10,.2,1), .2)
assert isclose(h.portfelli_sigma(10,.2,-1/9), 0, abs_tol=1e-8)
assert h.portfelli_sigma(100,.2,.8) > h.portfelli_sigma(10,.2,.1)
a, b = v.risk([-.005,.2],[.96,.04]), v.risk([-.005,.8],[.96,.04])
assert isclose(a['VaR'],b['VaR'])
assert isclose(a['ES'],.159) and isclose(b['ES'],.639)
assert isclose(v.risk([-.005,.2],[.96,.04],.99)['VaR'],.2)
assert isclose(v.risk([-.005,.2],[.96,.04],.99)['ES'],.2)
# Sama atomaarse jaotuse teisest järjekorrast ja osadeks jagamisest tulemus ei muutu.
c=v.risk([.2,-.005,.2],[.02,.96,.02])
assert all(isclose(c[k],a[k]) for k in a)
# ES on nihke suhtes ekvivariantne.
d=v.risk([.095,.3],[.96,.04])
assert isclose(d['ES'], a['ES']+.1)
# Nulloskusega mudeli teoreetiline tulevane eelis on 0; kontrollime MC vea suurusjärku.
z=f.katse(0)
assert z['monte_carlo_95_vahemik'][0] < 0 < z['monte_carlo_95_vahemik'][1]
assert f.katse(.04)['jargmise_cagr_vahe_fondide_keskmisega'] > .04
print('Kõik matemaatilised kontrollid läbitud. Empiirilisi turuväiteid need ei valideeri.')
