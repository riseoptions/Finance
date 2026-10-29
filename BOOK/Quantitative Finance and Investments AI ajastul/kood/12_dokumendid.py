"""Muuda enda avalik finantsaruande PDF kohalikuks RAG-korpuseks.
python kood/12_dokumendid.py aruanne.pdf --available-at 2024-02-03 --output andmed/aruanded.json
Kuupäev peab olema info tegelik saadavuspäev, mitte aruandeperioodi lõpp.
Päevasisene andmekasutus vajab täpsemat ajatemplit; siin päevapõhine õppenäide.
"""
import argparse,json,hashlib
from pathlib import Path

def main():
 a=argparse.ArgumentParser();a.add_argument('pdf',type=Path);a.add_argument('--available-at',required=True)
 a.add_argument('--output',type=Path,required=True);args=a.parse_args()
 from datetime import date
 date.fromisoformat(args.available_at)
 import fitz
 digest=hashlib.sha256(args.pdf.read_bytes()).hexdigest()[:12];chunks=[]
 with fitz.open(args.pdf) as pdf:
  for i,page in enumerate(pdf):
   text=page.get_text().strip()
   for start in range(0,len(text),1400):
    chunks.append({'id':f'{digest}_p{i+1}_c{start//1400}', 'available_at':args.available_at,
      'source':f'{args.pdf.name}, PDF page {i+1}', 'text':text[start:start+1800]})
 if not chunks:raise ValueError('PDF-ist ei leitud teksti; skann vajab OCR-i.')
 args.output.parent.mkdir(exist_ok=True,parents=True)
 args.output.write_text(json.dumps(chunks,ensure_ascii=False,indent=2));print('Lõike:',len(chunks))
if __name__=='__main__':main()
