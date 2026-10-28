# Sharpe’i suhtarv
from statistics import mean, stdev
uletootlused = [.04, .08, -.02, .06]
s = mean(uletootlused)/stdev(uletootlused)
print(f"Aastaste ületootluste Sharpe: {s:.4f}")
