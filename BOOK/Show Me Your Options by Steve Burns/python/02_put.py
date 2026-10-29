# Put’i P/L
# Õppenäide; hinnad ei ole turuandmed.
K=95;preemia=3;kordaja=100
for S in [0,80,95,100,120]:
    payoff=max(K-S,0)
    print(S, (payoff-preemia)*kordaja)
