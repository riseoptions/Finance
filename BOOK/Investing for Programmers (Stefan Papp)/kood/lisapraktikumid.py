"""Stress, VaR/ES, portfelli kaalud, sentiment ja optsioonigraafik. Kõik simuleeritud."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tuum import demo_hinnad,tootlused,OUT

def main():
    r=tootlused(demo_hinnad()); loss=-r.iloc[:,0]*10000
    var=np.quantile(loss,.95); es=loss[loss>=var].mean()
    print('Ajaloolise meetodi VaR95/ES95 demo:',round(var,2),round(es,2))
    rng=np.random.default_rng(17);weights=rng.dirichlet(np.ones(3),2000)
    cov=r.cov().to_numpy()*252;mu=r.mean().to_numpy()*252
    risk=np.sqrt(np.einsum('ij,jk,ik->i',weights,cov,weights))
    i=np.argmin(risk)
    print('Valimi vähima riskiga kaalud:',weights[i].round(3),'risk',round(risk[i],4))
    print('Stress: aktsiad -40%, võlakiri -10%; võrdsed kaalud:',np.mean([-.4,-.4,-.1]))
    fig,ax=plt.subplots();ax.scatter(risk,weights@mu,s=4,alpha=.3)
    ax.set(xlabel='Aastane volatiilsus',ylabel='Aritmeetiline aastastatud keskmine',title='SIMULEERITUD kaalude pilv; mitte täpne efektiivsuspiir')
    fig.tight_layout();fig.savefig(OUT/'kaalud.png');plt.close(fig)
    s=np.linspace(50,150,201);fig,ax=plt.subplots()
    ax.plot(s,np.maximum(s-100,0)-5,label='Call ost, K=100, preemia=5')
    ax.plot(s,np.maximum(100-s,0)-4,label='Put ost, K=100, preemia=4')
    ax.axhline(0,color='black',linewidth=.5);ax.legend();ax.set(xlabel='Alusvara hind tähtajal',ylabel='Kasum ühiku kohta',title='Hüpoteetiline optsioonikasum')
    fig.tight_layout();fig.savefig(OUT/'optsioonid.png');plt.close(fig)
    positive={'kasv','kasvas','paranes'};negative={'kahjum','langes','risk'}
    for text in ['Müügitulu kasvas','Kahjum vähenes oodatust rohkem']:
        tokens=set(text.lower().split());score=len(tokens&positive)-len(tokens&negative)
        print('NAIIVNE sentiment:',repr(text),score)
    print('Negatiivne sõna ei pruugi tähendada negatiivset uudist; käsitsi märgendamine on vajalik.')
if __name__=='__main__':main()
