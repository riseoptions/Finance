"""Kaheksa optsiooniküsimuse arvutuslabor. Python 3 + numpy. Käivita kogu fail."""
from math import exp, log, sqrt, erf, pi
import numpy as np

def normal_cdf(x):
    a = np.asarray(x)
    return np.vectorize(lambda z: 0.5*(1+erf(float(z)/sqrt(2))), otypes=[float])(a)

def bs(S, K=100., T=1., r=0., sigma=.2):
    """Euroopa call, dividendideta. Tagastab hinna, delta ja gamma."""
    S = np.asarray(S, dtype=float)
    if np.any(S <= 0) or K <= 0 or T < 0 or sigma <= 0:
        raise ValueError('S,K,sigma > 0; T >= 0')
    if T == 0:
        return np.maximum(S-K, 0), np.where(S>K,1.,np.where(S<K,0.,.5)), np.zeros_like(S)
    d1=(np.log(S/K)+(r+.5*sigma*sigma)*T)/(sigma*sqrt(T))
    d2=d1-sigma*sqrt(T)
    return (S*normal_cdf(d1)-K*exp(-r*T)*normal_cdf(d2),
            normal_cdf(d1), np.exp(-.5*d1*d1)/(sqrt(2*pi)*S*sigma*sqrt(T)))

def binomial(S=1., up=2., down=.5, K=1., R=1.):
    if not down < R < up:
        raise ValueError('Arbitraaživabaduseks peab down < R < up')
    Su,Sd=S*up,S*down
    Cu,Cd=max(Su-K,0),max(Sd-K,0)
    delta=(Cu-Cd)/(Su-Sd)
    cash=(Cd-delta*Sd)/R
    q=(R-down)/(up-down)
    return delta*S+cash,delta,cash,q

def hedge_simulation(real_sigma=.3, hedge_sigma=.2, n=5000, steps=252,
                     mu=0., r=0., cost_rate=0., seed=42, sell_sigma=None):
    """Müüdud call: raha + aktsiad - lõppväljamakse. Delta hedge_sigma järgi, hind sell_sigma järgi (vaikimisi hedge_sigma).
    Kulu: cost_rate * tehingu nominaal; arvestab algostu ja lõppmüüki.
    Sama seeme võimaldab sama sammude arvu korral ausat strateegiavõrdlust.
    """
    rng=np.random.default_rng(seed)
    dt=1/steps
    S=np.full(n,100.)
    _,delta,gamma=bs(S,r=r,sigma=hedge_sigma)
    premium=bs(S,r=r,sigma=hedge_sigma if sell_sigma is None else sell_sigma)[0]
    cash=premium-delta*S-cost_rate*np.abs(delta)*S
    integral=np.zeros(n)
    costs=cost_rate*np.abs(delta)*S
    for i in range(steps):
        # Diskonteeritud gamma-integrandi vasakpoolne Riemanni summa.
        integral += exp(-r*i*dt)*.5*gamma*S*S*(hedge_sigma**2-real_sigma**2)*dt
        S *= np.exp((mu-.5*real_sigma**2)*dt+real_sigma*sqrt(dt)*rng.standard_normal(n))
        cash *= exp(r*dt)
        if i < steps-1:
            _,new_delta,gamma=bs(S,T=1-(i+1)*dt,r=r,sigma=hedge_sigma)
            fee=cost_rate*np.abs(new_delta-delta)*S
            cash -= (new_delta-delta)*S+fee
            costs += fee
            delta=new_delta
    fee=cost_rate*np.abs(delta)*S
    cash += delta*S-fee
    costs += fee
    pnl=cash-np.maximum(S-100,0)
    return pnl, integral*exp(r), costs

def main():
    c,d,b,q=binomial()
    assert np.isclose(c,1/3) and np.isclose(d,2/3)
    print('1–2: hind, delta, raha, q:', c,d,b,q)
    for p in [.2,.5,.8]:
        print('p=',p,'P-keskmine=',p,'replikatsioonihind=',c)
    c20,delta,gamma=bs(100)
    c30=bs(100,sigma=.3)[0]
    print('3: BS sigma20/sigma30, delta, gamma:',c20,c30,delta,gamma)
    h=.001
    fd=(bs(100+h)[0]-bs(100-h)[0])/(2*h)
    assert abs(fd-delta)<1e-7
    # 4: ümberpaigutamine ei muuda hetkeportfelli väärtust.
    old_cash=10.; old_delta=.5; new_delta=.6; spot=102.
    new_cash=old_cash-(new_delta-old_delta)*spot
    assert np.isclose(old_cash+old_delta*spot,new_cash+new_delta*spot)
    print('4: uus rahakonto:',new_cash)
    # 5: 3 seisundit, 2 instrumenti; lisame sõltumatu put-väljamakse.
    A=np.array([[80.,1.],[100.,1.],[120.,1.]])
    payoff=np.array([0.,0.,20.])
    beta=np.linalg.lstsq(A,payoff,rcond=None)[0]
    print('5: aktsia+raha kaalud ja jäägid:',beta,payoff-A@beta)
    A3=np.column_stack((A,[20.,0.,0.]))
    weights=np.linalg.solve(A3,payoff)
    assert np.allclose(A3@weights,payoff)
    print('5: aktsia+raha+put kaalud:',weights)
    # 6: delta ei kata hüppest tingitud mittelineaarset muutust.
    jump_residual=bs(80)[0]-c20-delta*(80-100)
    print('6: 100 -> 80 hüppe optsioonimiinus-delta jääk:',jump_residual)
    # 7: lambda märk sõltub Browni liikumise teisenduse kokkuleppest.
    aP,bfactor,lam=.03,.02,.5
    print('7: aQ=aP-b*lambda:',aP-bfactor*lam)
    sigf=.01; tau=5
    print('7: HJM forwardi drift:',sigf**2*tau)
    # 8: võrdleme tehingukuludeta väärvolatiilsuse katet.
    pnl,integ,_=hedge_simulation()
    expected=float(c20-c30)
    print('8: keskmine P&L, standardviga, teooria:',pnl.mean(),pnl.std(ddof=1)/sqrt(len(pnl)),expected)
    print('8: P&L 5/50/95 protsentiil:',np.quantile(pnl,[.05,.5,.95]))
    print('8: gamma-integrali keskmine:',integ.mean())
    assert abs(pnl.mean()-expected)<5*pnl.std(ddof=1)/sqrt(len(pnl))+.05
    for steps in [12,52,252]:
        plain,_,_=hedge_simulation(real_sigma=.2,steps=steps)
        costly,_,fees=hedge_simulation(real_sigma=.2,steps=steps,cost_rate=.001)
        print('sammud / tasuta std / kuludega keskmine / keskmine kulu:',steps,plain.std(),costly.mean(),fees.mean())
    print('Fikseeritud müügihind sigma=20%, tegelik sigma=30%:')
    for hs in [.15,.2,.3]:
        result,_,_=hedge_simulation(hedge_sigma=hs,sell_sigma=.2)
        print('hedge sigma / Q-keskmine / std:',hs,result.mean(),result.std())
    print('Kõik arvulised kontrollid läbitud.')

if __name__=='__main__':
    main()
