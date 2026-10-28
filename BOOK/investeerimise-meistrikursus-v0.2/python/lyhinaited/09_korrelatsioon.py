# Korrelatsioon tootlustest
from statistics import mean
from math import sqrt
a, b = [.01,-.02,.03,.00], [.02,-.01,.04,.01]
da, db = [x-mean(a) for x in a], [x-mean(b) for x in b]
rho = sum(x*y for x,y in zip(da,db))/sqrt(
    sum(x*x for x in da)*sum(y*y for y in db))
print(f"Korrelatsioon: {rho:.4f}")
