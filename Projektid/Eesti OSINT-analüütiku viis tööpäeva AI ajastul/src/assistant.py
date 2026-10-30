"""Estonian OSINT Research Assistant: offline, standard-library baseline."""
from pathlib import Path
import csv,sqlite3,json,hashlib,datetime,argparse,statistics,re
ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'reports/research.sqlite'
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def digest(data): return hashlib.sha256(data).hexdigest()
def connect(db=DB):
    c=sqlite3.connect(db);c.row_factory=sqlite3.Row
    c.executescript((ROOT/'sql/schema.sql').read_text(encoding='utf-8'));return c
def ingest(c,manifest=None):
    records=manifest if manifest is not None else json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8'))
    with c:
        for r in records:
            p=(ROOT/r['path']).resolve()
            if not p.is_relative_to(ROOT/'data'): raise ValueError('Tõend peab asuma data kaustas')
            raw=p.read_bytes();sha=digest(raw)
            snapshot=ROOT/'reports/snapshots'/f'{sha}{p.suffix}'
            snapshot.parent.mkdir(parents=True,exist_ok=True)
            if snapshot.exists() and snapshot.read_bytes()!=raw: raise ValueError('Räsikonflikt')
            if not snapshot.exists(): snapshot.write_bytes(raw)
            c.execute('INSERT OR IGNORE INTO sources VALUES(?,?,?)',(r['source_id'],r['url'],r['rights']))
            # Per-evidence URL retained in manifest; source URL is only a source entry point.
            c.execute('INSERT OR IGNORE INTO evidence VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                (r['evidence_id'],sha,r['source_id'],r['title'],r['published_at'],r['captured_at'],now(),str(snapshot.relative_to(ROOT)),r['url'],raw.decode('utf-8'),int(r['synthetic'])))
        c.execute('INSERT INTO audit VALUES(?,?,?)',(now(),'ingest',str(len(records))))
    return len(records)
def load_contracts(c):
    with c, (ROOT/'data/contracts.csv').open(encoding='utf-8',newline='') as f:
        for r in csv.DictReader(f):
            if not c.execute('SELECT 1 FROM evidence WHERE evidence_id=?',(r['evidence_id'],)).fetchone():
                raise ValueError('Puuduv tõend')
            c.execute('INSERT OR REPLACE INTO contracts VALUES(?,?,?,?,?,?,?)',
                (r['contract_id'],r['buyer'],r['supplier'],float(r['base_eur']),float(r['award_eur']),int(r['bids']),r['evidence_id']))
def metrics(c):
    rows=list(c.execute('SELECT * FROM contracts ORDER BY contract_id'))
    rates=[100*(r['award_eur']/r['base_eur']-1) for r in rows]
    return dict(n=len(rows),mean_pct=statistics.mean(rates),median_pct=statistics.median(rates),
                min_pct=min(rates),max_pct=max(rates),rates=rates)
def tokens(s): return set(re.findall(r'[a-zõäöüšž0-9]+',s.lower()))
def retrieve(c,question,k=3):
    q=tokens(question)
    rows=list(c.execute('SELECT * FROM evidence WHERE source_id != ? ORDER BY evidence_id,ingested_at DESC',('SYN-test',)))
    seen=set();hits=[]
    for r in rows:
        if r['evidence_id'] in seen: continue
        seen.add(r['evidence_id']);t=tokens(r['text']);score=len(q&t)/max(1,len(q))
        if score>0: hits.append(dict(id=r['evidence_id'],score=score,text=r['text'],sha256=r['sha256'],path=r['path']))
    return sorted(hits,key=lambda x:(-x['score'],x['id']))[:k]
def report(c):
    m=metrics(c)
    lines=['# OSINT analüüsiaruanne — FIKTIIVNE ÕPPEJUHTUM','',
      'Kuupäev: 30.10.2026. Ulatus: SYN-P01 avaliku arendusprojekti dokumendid. Koostaja: õppelabor.',
      '', '## Otsustajale',
      'Algne ehituseelarve oli 1 000 000 eurot [E01]. Leping sõlmiti 1 200 000 eurole käibemaksuta [E02]. '
      'Seega ületab leping algset eelarvet 20%. Hilisem eelarve on 1 250 000 eurot [E03]; leping on sellest 4% väiksem. '
      'Need arvud ei näita tegelikke väljamakseid.',
      '1 500 000 euro väide esineb algses uudises [E04], kuid paranduses lükatakse see tagasi [E05]. '
      'Sama väite kordamine avalikul lehel [E06] ei ole sõltumatu kinnitus.',
      '', '## Hinnangud ja piirangud',
      'Kõrge kindlus õppekorpuse piires: lepingu summa, eelarveotsuste ajaline järjestus ja loa väljavõtte olemasolu [E01–E03, E08]. '
      'Teadmata: tegelikud maksed, tööde alustamise kuupäev ja kõigi loatingimuste täitmine. '
      'Sama ärimaja aadress ei tõenda ettevõtete ühist kontrolli [E09]. Korruptsioonijärelduseks tõendid puuduvad.',
      'Keskkonnaalane tingimus puudutab sademeveelahendust, mitte üldist keeldu [E11]. '
      'Soovitus: küsida ametlik maksete koond, lepingu lisad ning loa tingimuste täitmise dokument; säilitada küsimused uurimislogis.',
      '', '## Meetod ja võrdlusvalim',
      f"12 fiktiivse lepingu eelarvest kõrvalekalde mediaan on {m['median_pct']:.2f}% ja keskmine {m['mean_pct']:.2f}% [E10; contracts.csv]. "
      'Valim on koostatud õpetamiseks; sellest ei hinnata Eesti korruptsiooniriski ega tegelikku hinnataset.',
      'Arvutus: 100 × (lepingu hind / esialgne eelarve − 1). Kõik summad ilma käibemaksuta. '
      'Võrdlus ei korrigeeri töömahtu, perioodi ega keerukust.',
      '', '## Tõendiregister',
      '| ID | Avaldamine | Säilitatud fail | SHA-256 |','|---|---|---|---|']
    for r in c.execute('SELECT * FROM evidence ORDER BY evidence_id'):
        lines.append(f"| {r['evidence_id']} | {r['published_at']} | [{r['title']}](../{r['path']}) | `{r['sha256']}` |")
    lines+=['','Algallika URL, päritolu ja fiktiivne kogumisaeg: [manifest](../data/manifest.json). '
      'Räsid tõendavad muutumatust võrreldes säilitatud versiooniga, mitte dokumendi tõesust. '
      'SQLite audit on õppelogi, mitte võltsimiskindel tõendiahel. Välisallikaid selle juhtumi kohta ei päringuta.']
    out=ROOT/'reports/raport.md';out.write_text('\n'.join(lines)+'\n',encoding='utf-8');return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--question');args=ap.parse_args()
    c=connect();ingest(c);load_contracts(c)
    print(report(c))
    if args.question: print(json.dumps(retrieve(c,args.question),ensure_ascii=False,indent=2))
    else: print(json.dumps(metrics(c),ensure_ascii=False,indent=2))
    c.close()
if __name__=='__main__': main()
