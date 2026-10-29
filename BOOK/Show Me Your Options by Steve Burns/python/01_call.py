# Call’i P/L
# Õppenäide; hinnad ei ole turuandmed.
K=105;preemia=3;kordaja=100
for S in [90,100,105,110,120]:
    payoff=max(S-K,0)
    print(S, (payoff-preemia)*kordaja)
