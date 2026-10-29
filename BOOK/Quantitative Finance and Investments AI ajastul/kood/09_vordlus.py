from projekt import OUT
import pandas as pd
if __name__=='__main__':
 for name in ['vordlus.csv','test_mse.csv','portfell.csv']:
  print('\n'+name);print(pd.read_csv(OUT/name).to_string(index=False))
 print('LLM/agent: mõõda faktitäpsust, aega ja kulu eraldi; need pole strateegiatootlused.')
