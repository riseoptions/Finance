"""20 short executable labs; run e.g. python src/labs.py 13."""
import sys,json,csv,statistics,math
from collections import Counter,defaultdict,deque
from assistant import ROOT,connect,ingest,load_contracts,metrics,retrieve,digest

def run(n):
    c=connect();ingest(c);load_contracts(c)
    if n==1: print(json.dumps({'question':'Kas lepingu hind ületab algset ja muudetud eelarvet?','scope':'SYN-P01 dokumendid','stop':'E01 E02 E03 võrreldud; maksete puudumine märgitud'},ensure_ascii=False))
    elif n==2: print(sys.version, '\nTöökaust:',ROOT,'\nVälisvõrku selles laboris ei kasutata.')
    elif n==3: print((ROOT/'data/manifest.json').read_text(encoding='utf-8'))
    elif n==4:
        for r in c.execute('SELECT * FROM evidence'): print(r['evidence_id'],digest((ROOT/r['path']).read_bytes())==r['sha256'])
    elif n==5:
        from api_demo import main
        old=sys.argv;sys.argv=[old[0]];main();sys.argv=old
    elif n==6: print([dict(r) for r in c.execute('SELECT contract_id,buyer,supplier FROM contracts')])
    elif n==7:
        before=c.execute('SELECT COUNT(*) FROM evidence').fetchone()[0];ingest(c)
        print('Enne/pärast:',before,c.execute('SELECT COUNT(*) FROM evidence').fetchone()[0])
    elif n==8:
        for sql in (ROOT/'sql/queries.sql').read_text().split(';'):
            if sql.strip(): print([dict(r) for r in c.execute(sql)])
    elif n==9: print('E04 -> E06: sama päritoluahel; E05 parandab E04. Kaks avaldamist != kaks sõltumatut tõendit.')
    elif n==10: print(Counter(r['source_id'] for r in c.execute('SELECT source_id FROM evidence')))
    elif n==11:
        print({r['evidence_id']:Counter(r['text'].lower().split()).most_common(5) for r in c.execute('SELECT * FROM evidence WHERE evidence_id IN ("E04","E05","E07")')})
    elif n==12: print([dict(r) for r in c.execute('SELECT evidence_id,published_at,title FROM evidence ORDER BY published_at,evidence_id')])
    elif n==13: print(json.dumps(metrics(c),indent=2))
    elif n==14:
        rs=list(c.execute('SELECT bids,100*(award_eur/base_eur-1) AS growth FROM contracts'))
        print('Pearson r:',statistics.correlation([r['bids'] for r in rs],[r['growth'] for r in rs]),'Põhjuslikkus ei ole tuvastatud.')
    elif n==15:
        g=defaultdict(set)
        for r in csv.DictReader((ROOT/'data/edges.csv').open(encoding='utf-8')):g[r['src']].add(r['dst']);g[r['dst']].add(r['src'])
        queue=deque([['SYN-O02']]);seen={'SYN-O02'}
        while queue:
            path=queue.popleft()
            if path[-1]=='SYN-O03': print('Tee:',path,'Seos on aadressi kasutamine, mitte omand.');break
            for node in sorted(g[path[-1]]-seen):seen.add(node);queue.append(path+[node])
        print('Astmed:',{k:len(v) for k,v in g.items()})
    elif n==16:
        from ml_demo import main
        main()
    elif n==17:
        from rag import main
        old=sys.argv;sys.argv=[old[0]];main();sys.argv=old
    elif n==18:
        tests=json.loads((ROOT/'data/rag_eval.json').read_text(encoding='utf-8'));results=[]
        for t in tests:
            ids=[h['id'] for h in retrieve(c,t['question'])];gold=set(t['gold'])
            results.append({'question':t['question'],'retrieved':ids,'recall_at_3':len(gold&set(ids))/len(gold) if gold else None,'empty_expected':not gold,'empty_actual':not ids})
        (ROOT/'reports/rag_metrics.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(results,ensure_ascii=False,indent=2))
    elif n==19:
        from assistant import report
        print(report(c))
    elif n==20: print('Kontroll: python -m unittest discover -s tests -v; kaitsmine: docs/opetaja.md')
    else: raise ValueError('Moodul 1–20')
    c.close()
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 1)
