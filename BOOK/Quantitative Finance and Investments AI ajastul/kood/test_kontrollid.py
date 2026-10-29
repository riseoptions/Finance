"""Sisulised kontrollid ajastusele, tulevikuandmetele, kuludele ja agendi piiridele."""
import importlib.util, unittest
import numpy as np
import pandas as pd
from projekt import synthetic,dataset,net_returns,metrics
from pathlib import Path
spec=importlib.util.spec_from_file_location('rag',Path(__file__).with_name('07_rag_agent.py'))
rag=importlib.util.module_from_spec(spec);spec.loader.exec_module(rag)
class Checks(unittest.TestCase):
 def test_target_timing(self):
  p=synthetic().iloc[:,0];d=dataset(p);t=d.index[50];i=p.index.get_loc(t)
  self.assertAlmostEqual(d.loc[t,'target'],p.iloc[i+2]/p.iloc[i+1]-1)
 def test_features_do_not_see_future(self):
  p=synthetic().iloc[:,0];q=p.copy();q.iloc[900:]*=7
  pd.testing.assert_frame_equal(dataset(p).loc[:p.index[899]].drop(columns='target'),
                                dataset(q).loc[:p.index[899]].drop(columns='target'))
 def test_cost_round_trip(self):
  idx=pd.date_range('2020-01-01',periods=3)
  r=pd.Series(0.,index=idx);w=pd.Series([1.,1.,0.],index=idx)
  net,_=net_returns(r,w,10);self.assertAlmostEqual(net.sum(),-.002)
 def test_terminal_exit(self):
  idx=pd.date_range('2020-01-01',periods=3)
  net,_=net_returns(pd.Series(0.,index=idx),pd.Series(1.,index=idx),10)
  self.assertAlmostEqual(net.sum(),-.002)
 def test_initial_drawdown(self):self.assertAlmostEqual(metrics(pd.Series([-.2,0.]))['max_drawdown'],-.2)
 def test_cutoff(self):
  self.assertNotIn('future_2024_p1',[d['id'] for d in rag.retrieve('revenue')])
 def test_invalid_tool(self):
  with self.assertRaises(ValueError):rag.dispatch({'tool':'buy'},'2024-03-01')
 def test_fake_citation(self):
  with self.assertRaises(ValueError):rag.check_answer({'claims':[{'text':'x','source_ids':['fake']}]},[])
 def test_agent_loop_mock(self):
  seq=iter(['{"tool":"search","query":"revenue"}',
    '{"tool":"finish","answer":{"claims":[{"text":"Kasv 20%","source_ids":["demo_2023_p1"]}],"missing":[]}}'])
  result=rag.agent(lambda p:(next(seq),{}));self.assertEqual(len(result['trace']),1)
 def test_agent_step_limit(self):
  result=rag.agent(lambda p:('{"tool":"search","query":"revenue"}',{}))
  self.assertIsNone(result['answer']);self.assertEqual(len(result['trace']),3)
if __name__=='__main__':unittest.main()
