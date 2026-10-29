from projekt import load_prices,dataset,walk_forward,OUT
if __name__=='__main__':
 pred,winner=walk_forward(dataset(load_prices().iloc[:,0]));pred.to_csv(OUT/'prognoosid.csv');print('Valik:',winner)
