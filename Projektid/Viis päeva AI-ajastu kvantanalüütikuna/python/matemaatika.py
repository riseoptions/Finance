"""Väikeste arvuliste näidete kontroll; ei vaja internetti."""
import numpy as np
print('Lihttootlus:', 108/100-1)
print('Logtootlus kahe perioodi peale:', 2*np.log(1.1))
print('Geomeetriline keskmine:', np.sqrt(1.2*.8)-1)
print('Sharpe:', np.sqrt(12)*.01/.04)
print('Kahe vara volatiilsus:', np.sqrt(.25*.04+.25*.04+2*.25*(-.5)*.04))
print('Ridge ühe tunnusega:', 2/(4+1))
print('RMSE protsendipunktides:', np.sqrt((1**2+3**2)/2))
print('Precision, recall:', 30/50, 30/40)
x = np.array([-.02,-.01,0,.01,.02])
y = .002+1.2*x
b = np.linalg.lstsq(np.c_[np.ones(len(x)),x],y,rcond=None)[0]
print('OLS vabaliige ja beeta:',b)
assert np.allclose(b,[.002,1.2])
