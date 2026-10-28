"""Valikulised read-only HTTP päringud. Võrgus katsetamata; offline õpe ei vaja neid."""
import json,os,urllib.request,urllib.parse
from datetime import datetime,timezone
from tuum import ROOT

def fetch(url, headers=None):
    req=urllib.request.Request(url,headers=headers or {})
    with urllib.request.urlopen(req,timeout=30) as response:return json.load(response)

def sec(cik):
    agent=os.environ.get('SEC_USER_AGENT')
    if not agent: raise RuntimeError('Määra SEC_USER_AGENT kujul nimi kontakt-email.')
    if not cik.isdigit() or len(cik)>10: raise ValueError('CIK peab olema kuni 10 numbrit.')
    return fetch(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik.zfill(10)}.json',{'User-Agent':agent})

def fred(series):
    key=os.environ.get('FRED_API_KEY')
    if not key: raise RuntimeError('Määra FRED_API_KEY keskkonnamuutuja.')
    query=urllib.parse.urlencode({'series_id':series,'api_key':key,'file_type':'json',
        'observation_start':'2020-01-01','observation_end':'2024-12-31'})
    return fetch('https://api.stlouisfed.org/fred/series/observations?'+query)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('service',choices=['sec','fred']);p.add_argument('identifier')
    a=p.parse_args();data=sec(a.identifier) if a.service=='sec' else fred(a.identifier)
    # Võtmeid ega võtmega päringu-URL-i ei salvestata.
    dest=ROOT/'andmed'/f'{a.service}_toorandmed.json'
    dest.write_text(json.dumps({'loaded_utc':datetime.now(timezone.utc).isoformat(),
       'service':a.service,'identifier':a.identifier,'data':data},ensure_ascii=False),encoding='utf-8')
    print(dest)
