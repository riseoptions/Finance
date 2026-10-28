# Portfelli oodatav tootlus
kaalud, ootused = [0.6,0.4], [0.08,0.03]
assert abs(sum(kaalud)-1) < 1e-12
vastus = sum(w*r for w,r in zip(kaalud,ootused))
print(f"Portfelli oodatav tootlus: {vastus:.2%}")
