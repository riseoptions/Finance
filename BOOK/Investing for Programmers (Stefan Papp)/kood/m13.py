"""[NÄIDE] Otsustusprotsess, lõpp-projekt ja õpetamine — vt mooduli selgitust."""
entry={'eesmark':'Õppida riskimõõdikuid','allikas':'SIMULATSIOON',
       'eeldused':['Väliseid rahavooge pole'],'risk':'Reaalne turg võib erineda',
       'kontroll':'Võrdlen käsitsi arvutatud näitega'}
required={'eesmark','allikas','eeldused','risk','kontroll'}
assert required<=entry.keys()
print('Päeviku struktuur korras; sisuline kvaliteet vajab inimese kontrolli.')
