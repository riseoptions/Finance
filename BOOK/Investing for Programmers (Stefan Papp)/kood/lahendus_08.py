"""Iseseisva ülesande näidislahendus."""
import numpy as np
y=np.array([.01,-.02,.01]);rmse=np.sqrt(np.mean(y*y))
assert abs(rmse-np.sqrt(.0002))<1e-12
print(f'RMSE {rmse:.6f}')
