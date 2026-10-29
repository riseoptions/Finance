# Kolme strateegia võrdlus
# Õppenäide; hinnad ei ole turuandmed.
M=100
print("S, long call, bull call spread, covered call")
for S in [0,80,95,100,105,110,120,150]:
    call=(max(S-105,0)-3)*M
    bull=(max(S-100,0)-max(S-110,0)-4)*M
    covered=(S-100+3-max(S-105,0))*M
    print(S,call,bull,covered)
