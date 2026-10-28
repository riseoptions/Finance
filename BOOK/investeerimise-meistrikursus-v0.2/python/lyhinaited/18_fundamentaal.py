# P/E ja vaba rahavoog
hind, aktsiaid, kasum = 20,10,25
cfo, capex = 18,15
pe = hind*aktsiaid/kasum
fcf = cfo-capex
print(f"P/E: {pe:.2f}; lihtsustatud FCF: {fcf:.2f}")
