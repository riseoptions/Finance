# Kahe vara standardhälve
from math import sqrt
w, s1, s2, rho = .5, .2, .2, 0
var = w*w*s1*s1 + (1-w)**2*s2*s2 + 2*w*(1-w)*rho*s1*s2
print(f"Portfelli standardhälve: {sqrt(var):.4%}")
