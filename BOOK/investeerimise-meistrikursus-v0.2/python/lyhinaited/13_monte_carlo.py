# Monte Carlo keskmise kontroll
from random import Random
from math import exp
from statistics import mean
rng = Random(42)
mu, sigma, algus = .06, .20, 1000
vaartused = [algus*exp(rng.gauss(mu,sigma)) for _ in range(20000)]
print(f"Simulatsiooni keskmine: {mean(vaartused):.2f}")
print(f"Teoreetiline ootus: {algus*exp(mu+sigma*sigma/2):.2f}")
