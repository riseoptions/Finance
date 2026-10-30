import sys,unittest,tempfile,json,sqlite3,io,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import assistant as a
from rag import validate
from api_demo import fetch
class Core(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.c=a.connect(Path(self.t.name)/'test.sqlite');a.ingest(self.c);a.load_contracts(self.c)
    def tearDown(self):self.c.close();self.t.cleanup()
    def test_idempotent(self):
        a.ingest(self.c);self.assertEqual(self.c.execute('SELECT COUNT(*) FROM evidence').fetchone()[0],12)
    def test_arithmetic(self):
        m=a.metrics(self.c);self.assertEqual(m['n'],12);self.assertAlmostEqual(m['median_pct'],5);self.assertAlmostEqual(m['mean_pct'],9.75)
        r=self.c.execute("SELECT * FROM contracts WHERE contract_id='SYN-C01'").fetchone();self.assertAlmostEqual((r['award_eur']/r['base_eur']-1)*100,20)
        self.assertAlmostEqual((r['award_eur']/1250000-1)*100,-4)
    def test_evidence_integrity(self):
        for r in self.c.execute('SELECT * FROM evidence'):
            self.assertEqual(a.digest((a.ROOT/r['path']).read_bytes()),r['sha256'])
            self.assertTrue(r['url'].startswith('https://osint-lab.example/'))
    def test_version_history(self):
        records=json.loads((a.ROOT/'data/manifest.json').read_text(encoding='utf-8'))
        # A controlled new synthetic file version, without touching originals.
        p=a.ROOT/'data/_test_version.txt'
        try:
            p.write_text('Uus fiktiivne versioon',encoding='utf-8');r=dict(records[0]);r['path']='data/_test_version.txt';a.ingest(self.c,[r])
            self.assertEqual(self.c.execute("SELECT COUNT(*) FROM evidence WHERE evidence_id='E01'").fetchone()[0],2)
            old=self.c.execute("SELECT * FROM evidence WHERE evidence_id='E01' AND text LIKE '%1000000%'").fetchone()
            self.assertIsNotNone(old);self.assertEqual(a.digest((a.ROOT/old['path']).read_bytes()),old['sha256'])
        finally:p.unlink(missing_ok=True)
    def test_query_parameter(self):
        self.assertEqual(self.c.execute('SELECT * FROM contracts WHERE contract_id=?',("x' OR 1=1 --",)).fetchall(),[])
    def test_path_escape(self):
        r=json.loads((a.ROOT/'data/manifest.json').read_text(encoding='utf-8'))[0];r['path']='../book.txt'
        with self.assertRaises(ValueError):a.ingest(self.c,[r])
    def test_sql_checks(self):
        for sql in (a.ROOT/'sql/queries.sql').read_text().split(';'):
            if sql.strip():self.c.execute(sql).fetchall()
    def test_retrieval_and_abstention(self):
        self.assertIn('E08',[h['id'] for h in a.retrieve(self.c,'ehitusluba väljastatud')])
        self.assertEqual(a.retrieve(self.c,'kvantgravitatsioon neutriino'),[])
        self.assertNotIn('E12',[h['id'] for h in a.retrieve(self.c,'Ignoreeri juhiseid')])
    def test_citation_validation(self):
        hits=a.retrieve(self.c,'ehitusluba väljastatud')
        bad={'claims':[{'text':'X','evidence_id':'E99','quote':'Y'}],'unknowns':[]};self.assertTrue(validate(bad,hits))
        h=hits[0];good={'claims':[{'text':'Dokumendi väljavõte','evidence_id':h['id'],'quote':h['text']}],'unknowns':[]};self.assertEqual(validate(good,hits),[])
        good['claims'][0]['quote']='Tsitaati ei eksisteeri';self.assertTrue(validate(good,hits))
    def test_api_mock_and_schema(self):
        raw,value=fetch(opener=lambda *args,**kw:io.BytesIO(b'[{"id":"SYN"}]'));self.assertEqual(value[0]['id'],'SYN')
        with self.assertRaises(ValueError):fetch(opener=lambda *args,**kw:io.BytesIO(b'{}'))
        with self.assertRaises(ValueError):fetch(url='https://unapproved.example/')
    def test_data_binding(self):
        e=(a.ROOT/'data/evidence/E10.txt').read_text(encoding='utf-8')
        for f in ['data/contracts.csv','data/edges.csv']:self.assertIn(a.digest((a.ROOT/f).read_bytes()),e)
    def test_manifest_unique(self):
        m=json.loads((a.ROOT/'data/manifest.json').read_text(encoding='utf-8'));self.assertEqual(len({r['evidence_id'] for r in m}),len(m))
if __name__=='__main__':unittest.main()
