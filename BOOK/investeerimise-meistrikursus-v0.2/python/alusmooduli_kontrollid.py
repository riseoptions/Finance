"""Sõltumatud seosed ja piirjuhud alusmooduli arvutuste kontrollimiseks."""
from math import isclose, sqrt, prod


def price(y):
    return 50/(1+y)+50/(1+y)**2+1050/(1+y)**3

assert isclose(price(.05),1000)
y=.06
P=price(y)
duration=(50/1.06+2*50/1.06**2+3*1050/1.06**3)/P
modified=duration/(1+y)
h=1e-5
finite_difference=-(price(y+h)-price(y-h))/(2*h)/P
assert isclose(modified,finite_difference,rel_tol=1e-8)
# IRR kontroll tagasi algsesse rahavoovõrrandisse asendamisega.
irr=(-1+sqrt(9.4))/2-1
assert isclose(100*(1+irr)**2+100*(1+irr),210)
# Kahe perioodi võimenduse täpne erinevus erinevate märkidega tootlustel.
for r1,r2 in [(.1,.1),(.1,-.1),(-.1,-.2)]:
    for leverage in [2,-1]:
        leveraged=(1+leverage*r1)*(1+leverage*r2)-1
        benchmark=leverage*((1+r1)*(1+r2)-1)
        assert isclose(leveraged-benchmark,leverage*(leverage-1)*r1*r2,abs_tol=1e-12)
# Rahavoogude võrdlus: annuiteedi suletud valem vs iga makse eraldi kasvatamine.
assert isclose(100*(1.05**5-1)/.05,sum(100*1.05**t for t in range(5)))
# Tegurite järjekord ei muuda konstantse võimendusega kuludeta lõpptulemust.
r=[.10,-.05,.03]
assert isclose(prod(1+2*x for x in r),prod(1+2*x for x in reversed(r)))
# Täpne inflatsiooni korrigeerimine taastab nominaaltootluse.
real=1.08/1.05-1
assert isclose((1+real)*1.05,1.08)
print('Alusmooduli finantsmatemaatika piirjuhud ja sõltumatud seosed läbitud.')
