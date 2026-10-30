from projekt import load_data, panel, backtest, metrics
p = load_data()
d = panel(p)
d['reegel'] = d.mom63 / 3
validation = d[(d.signal >= '2019') & (d.signal < '2022')]
for name in ['baas', 'reegel']:
    result, weights = backtest(validation, name, p)
    print(name, metrics(result.net))
    print(result[['entry','exit','gross','cost','net']].head(2))
print('Üks käsitsi kontroll:', 1.2*.8-1)
