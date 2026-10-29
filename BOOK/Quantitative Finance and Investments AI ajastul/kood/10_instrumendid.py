"""Oma arvulised õppenäited, mitte turuhinnad."""
from math import erf,log,sqrt,exp

def bs_call(s,k,t,r,sigma):
 n=lambda x:(1+erf(x/sqrt(2)))/2
 d1=(log(s/k)+(r+sigma*sigma/2)*t)/(sigma*sqrt(t));d2=d1-sigma*sqrt(t)
 return s*n(d1)-k*exp(-r*t)*n(d2)

def main():
 print('Euroopa call, dividendideta:',round(bs_call(100,100,1,.05,.2),4))
 print('Call kasum tähtajal S=115, K=100, preemia=8:',max(115-100,0)-8)
 print('Futuuri P&L, kordaja 50, hinnamuutus -10:',50*(-10))
 print('ETF preemia %, hind 101, NAV 100:',(101/100-1)*100)
 print('Nullkupongvõlakirja YTM, hind 900, lunastus 1000, 2a:',(1000/900)**.5-1)
if __name__=='__main__':main()
