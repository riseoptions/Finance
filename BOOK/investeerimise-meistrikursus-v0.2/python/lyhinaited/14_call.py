# Call-optsiooni kasum tähtajal
S, K, preemia = 110,100,5
valjamakse = max(S-K,0)
kasum = valjamakse-preemia
print(f"Väljamakse: {valjamakse:.2f}; kasum: {kasum:.2f}")
print(f"Preemiatootlus: {kasum/preemia:.2%}")
