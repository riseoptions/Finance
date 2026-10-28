# Kelly panuse osakaal
from math import log
p,b=.55,1
f=(b*p-(1-p))/b
g=p*log(1+b*f)+(1-p)*log(1-f)
print(f"Kelly osakaal: {f:.2%}; oodatav logkasv: {g:.6f}")
