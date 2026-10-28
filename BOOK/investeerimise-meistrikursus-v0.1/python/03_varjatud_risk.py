"""Diskreetse kahjujaotuse VaR ja ES; null ajaloolist kahju ei välista riski."""
import json
import numpy as np


def risk(kaod, toenaosused, alpha=.95):
    x, p = np.asarray(kaod, float), np.asarray(toenaosused, float)
    if x.ndim != 1 or p.shape != x.shape or len(x) == 0:
        raise ValueError('Vaja on sama pikkusega mittetühje ühemõõtmelisi massiive.')
    if not np.isfinite(x).all() or not np.isfinite(p).all():
        raise ValueError('Sisend peab olema lõplik.')
    if np.any(p <= 0) or not np.isclose(p.sum(), 1) or not 0 < alpha < 1:
        raise ValueError('Tõenäosused peavad olema positiivsed ja summa 1; 0 < alpha < 1.')
    order = np.argsort(x)
    x, p = x[order], p[order]
    cdf = p.cumsum()
    var = x[np.searchsorted(cdf, alpha, side='left')]
    # Kvantiiliintegraal: piiripealsest tõenäosusmassist kaasatakse vaid vajalik osa.
    masses = np.maximum(0, cdf - np.maximum(cdf-p, alpha))
    es = np.dot(x, masses) / (1-alpha)
    return {'VaR': float(var), 'ES': float(es)}

if __name__ == '__main__':
    # 96% kuudest kasum 0.5%; 4% kuudest kahjum 20% või 80%.
    a = risk([-.005, .20], [.96, .04])
    b = risk([-.005, .80], [.96, .04])
    vaikne = risk([-.005], [1.0])
    print(json.dumps({'A': a, 'B': b, 'vaikse_ajaloo_hinnang': vaikne,
        'toenaosus_60_kuud_ilma_krahhita': .96**60,
        'A_oodatav_kuutootlus': .96*.005-.04*.20,
        'B_oodatav_kuutootlus': .96*.005-.04*.80}, ensure_ascii=False, indent=2))
