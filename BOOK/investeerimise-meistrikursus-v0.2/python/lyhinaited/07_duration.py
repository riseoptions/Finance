# Duration ja intressitundlikkus
F, c, y, n = 1000, 0.05, 0.06, 3
cf = [F*c] * n
cf[-1] += F
pv = [v/(1+y)**t for t,v in enumerate(cf,1)]
P = sum(pv)
d_mac = sum(t*v for t,v in enumerate(pv,1))/P
d_mod = d_mac/(1+y)
print(f"Macaulay: {d_mac:.4f}; modified: {d_mod:.4f}")
print(f"Ligikaudne hinnamuutus +0.01 šokiga: {-d_mod*.01:.4%}")
