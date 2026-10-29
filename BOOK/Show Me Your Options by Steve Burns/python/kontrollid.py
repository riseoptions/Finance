"""Õppemudelite kontrollid: käivita Python 3-ga."""
import json
from pathlib import Path
from math import exp,isclose
from mudel import hind

def close(a,b,tol=1e-7):
    assert abs(a-b)<tol,(a,b)

C=lambda s,k:max(s-k,0)
P=lambda s,k:max(k-s,0)
# Iga alusvara hinna korral on samade jalgade payoff-id identsed.
for s in range(0,501):
    close(C(s,100)-P(s,100),s-100)
    close(s+P(s,100),C(s,100)+100)
    close(s-C(s,100),100-P(s,100))
    close((C(s,105)-3)+(3-C(s,105)),0)
    close((P(s,95)-3)+(3-P(s,95)),0)
# Sõltumatud tuntud referentsid BSM-ile.
close(hind(100,100,1,.2,.05),10.450583572185565)
close(hind(100,100,1,.2,.05,liik='P'),5.573526022256971)
for s in (50,90,100,110,150):
    for T in (.01,.25,1):
        call=hind(s,100,T,.3,.04,.02)
        put=hind(s,100,T,.3,.04,.02,'P')
        close(call-put,s*exp(-.02*T)-100*exp(-.04*T))
        assert hind(s,100,T,.4,.04,.02)>=call-1e-10  # Ümardus sügaval OTM/ITM-is
        h=.01
        gamma=(hind(s+h,100,T,.3)-2*hind(s,100,T,.3)+hind(s-h,100,T,.3))/h**2
        assert gamma>-1e-7
assert hind(100,100,.25,.4)>hind(100,100,.25,.3)
close(hind(110,100,0,.2),10)
close(hind(90,100,0,.2,liik='P'),10)
# Atlase 21 strateegiat: sõltumatult ette antud piirid, nullpunktid ja sabad.
data=json.loads(Path(__file__).with_name('strateegiate_andmed.json').read_text())
expected=[(3,None,[108],1),(3,92,[92],0),(None,3,[108],-1),(92,3,[92],0),
(97,8,[97],0),(92,3,[92],0),(8,None,[103],1),(4,6,[104],0),(6,4,[104],0),
(6,4,[96],0),(6,4,[104],0),(12,None,[88,112],1),(6,None,[89,111],1),
(2,8,[92,108],0),(3,2,[93,107],0),(5,5,[100],0),(100,None,[100],1),
(None,8,[102,118],-1),(2,8,[92,108],0),(2,3,[92,108],0),(8,2,[92,108],0)]
for d,(loss,gain,roots,slope) in zip(data,expected):
    stock=d[3];legs=d[2]
    initial=stock*100+sum(q*p for typ,k,q,p in legs)
    def value(s):return stock*s+sum(q*(C(s,k) if typ=='C' else P(s,k)) for typ,k,q,p in legs)-initial
    ks=[0]+[x[1] for x in legs]
    vals=[value(s) for s in ks]
    if loss is not None:close(min(vals),-loss)
    if gain is not None:close(max(vals),gain)
    for root in roots:close(value(root),0)
    close(value(10001)-value(10000),slope)
# Ülesannete aritmeetika sõltumatud vastused.
close((C(110,105)-3)*100,200)
close((P(80,95)-3)*100,1200)
close((3-C(130,105))*100,-2200)
close((3-P(0,95))*100,-9200)
close(2.4*100*2+2,482)
close((2.8-3.2)*100-2,-42)
close((.5*2+.5*.04*2**2-.03)*100,105)
close(.9*10-.1*120-2,-5)
close((120+2)/130*100,93.84615384615384)
close(10000*.9**10,3486.784401)
close((70-95+3+2)*100,-2000)
assert int(500/160)==3
# Kalendri ja diagonaali kaitstud teoreetiline väärtus esimesel tähtajal.
for kl,ks in [(100,100),(95,105)]:
    for s in range(1,301):
        for iv in (.1,.2,.4):
            assert hind(s,kl,30/365,iv)-C(s,ks)>=-1e-8
print('KÕIK KONTROLLID LÄBITUD: payoff, 21 strateegiat, BSM, ülesanded, eri tähtajad.')
