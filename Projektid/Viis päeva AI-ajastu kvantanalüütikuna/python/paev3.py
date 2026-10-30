import pandas as pd
from projekt import ROOT
m = pd.read_csv(ROOT/'raportid/prognoosimootdikud.csv')
r = pd.read_csv(ROOT/'raportid/mootdikud.csv')
print('Prognoos:')
print(m[m.period == 'valideerimine'].to_string(index=False))
print('Portfell:')
print(r[r.period == 'valideerimine'].to_string(index=False))
print('55% tabamus, 1 euro võit, 1.5 euro kaotus:', .55*1-.45*1.5)
