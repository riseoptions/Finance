# Beeta ja alfa
from statistics import mean
x=[-.02,.00,.02,.04]
y=[-.02,.01,.04,.07]
beta=sum((a-mean(x))*(b-mean(y)) for a,b in zip(x,y))/sum((a-mean(x))**2 for a in x)
alfa=mean(y)-beta*mean(x)
print(f"Beeta: {beta:.4f}; perioodi alfa: {alfa:.4%}")
