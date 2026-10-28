"""Iseseisva ülesande näidislahendus."""
share=.1
for new in [.2,.25]: share*=1-new
assert abs(share-.06)<1e-12
print(f'Lõpposalus {share:.1%}')
