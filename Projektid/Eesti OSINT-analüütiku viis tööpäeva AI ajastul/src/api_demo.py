"""Official PxWeb discovery GET; default is offline fixture, live opt-in."""
from pathlib import Path
import argparse,json,urllib.request,urllib.error,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1]
URL='https://andmed.stat.ee/api/v1/et/stat'
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs): return None

def fetch(url=URL,opener=None):
    if url!=URL: raise ValueError('Lubatud ainult dokumenteeritud metaandmete URL')
    req=urllib.request.Request(url,headers={'User-Agent':'EstonianOSINTLearning/1.0','Accept':'application/json'})
    open_=opener or urllib.request.build_opener(NoRedirect()).open
    with open_(req,timeout=20) as r:
        raw=r.read(2_000_001)
    if len(raw)>2_000_000: raise ValueError('Vastus liiga suur')
    value=json.loads(raw)
    if not isinstance(value,list): raise ValueError('Oodati PxWeb kataloogi loendit')
    return raw,value

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--live',action='store_true');a=ap.parse_args()
    if not a.live:
        print('VÕRGUTA SÜNTEETILINE API NÄIDIS:',json.dumps([{'id':'SYN-TABLE','type':'t','text':'Õppetabel'}],ensure_ascii=False));return
    try: raw,value=fetch()
    except (urllib.error.URLError,ValueError,TimeoutError) as exc:
        raise SystemExit(f'Päring ebaõnnestus; ei proovita piirangust mööda: {exc}')
    sha=hashlib.sha256(raw).hexdigest();p=ROOT/'reports'/f'pxweb_{sha}.json';p.write_bytes(raw)
    p.with_suffix('.meta.json').write_text(json.dumps({'url':URL,'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':sha,'purpose':'statistikakataloogi metaandmed','live':True},indent=2),encoding='utf-8')
    print('Kataloogikirjeid:',len(value),'fail:',p)
if __name__=='__main__': main()
