# Lihtne viitajaga järeltest
from math import prod
r=[.02,-.01,.03,-.02,.01]
pos=[0]+[int(x>0) for x in r[:-1]]
eelmine,kasv=0,1
for w,x in zip(pos,r):
    kulu=.001*abs(w-eelmine)
    kasv*=1+w*x-kulu
    eelmine=w
print(f"Strateegia: {kasv-1:.4%}; osta-ja-hoia: {prod(1+x for x in r)-1:.4%}")
