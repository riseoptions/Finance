"""Originaalne simulatsioon: sama oskus vs püsiv oskuste erinevus."""
import json
import numpy as np


def katse(oskuse_hajuvus=0.0, seeme=20261028, kordusi=1000):
    rng = np.random.default_rng(seeme)
    enne, parast, vahed = [], [], []
    for _ in range(kordusi):
        # 500 fondi; kummaski sõltumatus ajavahemikus 5 aastat.
        oskus = rng.normal(0, oskuse_hajuvus, 500)
        mu = 0.06 + oskus  # aastase logtootluse ootus
        treening = rng.normal(mu, 0.18 / np.sqrt(5))
        kontroll = rng.normal(mu, 0.18 / np.sqrt(5))
        valitud = np.argmax(treening)
        enne.append(np.expm1(treening[valitud]))
        parast.append(np.expm1(kontroll[valitud]))
        vahed.append(np.expm1(kontroll[valitud]) - np.expm1(kontroll).mean())
    se = np.std(vahed, ddof=1) / np.sqrt(kordusi)
    keskmine = float(np.mean(vahed))
    return {'oskuse_hajuvus': oskuse_hajuvus, 'kordusi': kordusi,
            'voitja_varasem_cagr': float(np.mean(enne)),
            'voitja_jargmine_cagr': float(np.mean(parast)),
            'jargmise_cagr_vahe_fondide_keskmisega': keskmine,
            'monte_carlo_95_vahemik': [keskmine-1.96*se, keskmine+1.96*se]}

if __name__ == '__main__':
    print(json.dumps([katse(0.0), katse(0.04)], indent=2, ensure_ascii=False))
