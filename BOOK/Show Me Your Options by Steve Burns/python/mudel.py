"""Euroopa optsiooni Black–Scholesi õppemudel; pole turuhinna ennustus."""
from math import erf, exp, log, sqrt

def N(x):
    return (1 + erf(x / sqrt(2))) / 2

def hind(S, K, T, sigma, r=0.0, q=0.0, liik='C'):
    if S <= 0 or K <= 0 or T < 0 or sigma <= 0:
        raise ValueError('Vaja S>0, K>0, T>=0, sigma>0')
    if liik not in ('C','P'):
        raise ValueError('liik peab olema C või P')
    if T == 0:
        return max(S-K,0) if liik=='C' else max(K-S,0)
    d1=(log(S/K)+(r-q+sigma*sigma/2)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    if liik=='C':
        return S*exp(-q*T)*N(d1)-K*exp(-r*T)*N(d2)
    return K*exp(-r*T)*N(-d2)-S*exp(-q*T)*N(-d1)
