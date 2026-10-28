"""Iseseisva ülesande näidislahendus."""
from tuum import demo_hinnad,backtest
s=demo_hinnad().iloc[:,0]
a=(1+backtest(s,0).neto).prod();b=(1+backtest(s,.003).neto).prod()
assert b<=a+1e-12
print('Kuludeta',a,'kuludega',b)
