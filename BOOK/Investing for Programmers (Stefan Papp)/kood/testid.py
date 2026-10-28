"""Finantsilise tähendusega regressioonitestid: python kood/testid.py."""
import unittest
import numpy as np
import pandas as pd
from tuum import moodikud,osta_hoia,bond_price,ytm,kontrolli_hindu,backtest,ml_andmed,demo_hinnad
from uurimisagent import invoke,otsi
class TestKursus(unittest.TestCase):
    def test_liittootlus(self): self.assertAlmostEqual(moodikud([.2,-.2])['kogutootlus'],-.04)
    def test_esimese_paeva_langus(self): self.assertAlmostEqual(moodikud([-.2,0])['max_langus'],-.2)
    def test_tipust_langus(self): self.assertAlmostEqual(moodikud([.2,-.25,110/90-1])['max_langus'],-.25)
    def test_osta_hoia(self):
        p=pd.DataFrame({'a':[100,120,120],'b':[100,100,120]})
        self.assertAlmostEqual((1+osta_hoia(p,[.5,.5])).prod()-1,.2)
    def test_bond_par(self): self.assertAlmostEqual(bond_price(y=.05),1000)
    def test_bond_ytm(self): self.assertAlmostEqual(bond_price(y=ytm(950)),950)
    def test_vigane_hind(self):
        with self.assertRaises(ValueError): kontrolli_hindu(pd.DataFrame({'a':[100,0]}))
    def test_duplikaat(self):
        with self.assertRaises(ValueError): kontrolli_hindu(pd.DataFrame({'a':[100,101]},index=[1,1]))
    def test_tulevik_ei_muuda_minevikku(self):
        s=demo_hinnad().iloc[:,0];a=backtest(s);s2=s.copy();s2.iloc[400:]*=2;b=backtest(s2)
        pd.testing.assert_frame_equal(a.iloc[:398],b.iloc[:398])
    def test_tehingu_viivitus(self):
        s=pd.Series(np.arange(1.,102.));bt=backtest(s)
        # Esimene SMA60 signaal indeksil 59, täitmine 60, esimene tootlus 61.
        self.assertEqual(bt.loc[59,'signaal'],1)
        self.assertEqual(bt.loc[60,'positsioon'],0)
        self.assertEqual(bt.loc[61,'positsioon'],1)
        self.assertAlmostEqual(bt.loc[60,'neto'],-.001)
    def test_kulud(self):
        s=demo_hinnad().iloc[:,0]
        self.assertLessEqual((1+backtest(s,.003).neto).prod(),(1+backtest(s,0).neto).prod())
    def test_siht_ja_tunnused(self):
        s=demo_hinnad().iloc[:,0];d=ml_andmed(s);t=d.index[10];i=s.index.get_loc(t)
        self.assertAlmostEqual(d.loc[t,'target'],s.iloc[i+1]/s.iloc[i]-1)
        s2=s.copy();s2.iloc[i+1:]*=2
        pd.testing.assert_series_equal(d.drop(columns='target').loc[t],ml_andmed(s2).drop(columns='target').loc[t])
    def test_tool_whitelist(self):
        with self.assertRaises(ValueError):invoke({'tool':'kauple'})
    def test_allikaleid(self): self.assertEqual(otsi('müügitulu')[0]['id'],'D1')
if __name__=='__main__': unittest.main(verbosity=2)
