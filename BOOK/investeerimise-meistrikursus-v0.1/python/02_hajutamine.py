"""Võrdsete kaalude ja võrdsete standardhälvete täpne portfellivalem."""
import json
from math import sqrt


def portfelli_sigma(n, sigma, rho):
    if n < 2 or not isinstance(n, int):
        raise ValueError('Varade arv peab olema täisarv vähemalt 2.')
    if sigma < 0 or not -1/(n-1) <= rho <= 1:
        raise ValueError('Lubamatu standardhälve või korrelatsioonimaatriks.')
    return sigma * sqrt(rho + (1-rho)/n)

if __name__ == '__main__':
    tulemused = []
    for nimi, sigma, rho in [('Rahulik', .20, .10),
                             ('Ainult korrelatsiooni stress', .20, .80),
                             ('Korrelatsiooni ja volatiilsuse stress', .40, .80)]:
        tulemused.append({'stsenaarium': nimi, 'n': 10, 'vara_sigma': sigma,
                         'rho': rho, 'portfelli_sigma': portfelli_sigma(10, sigma, rho)})
    print(json.dumps(tulemused, ensure_ascii=False, indent=2))
