"""Ajafiltriga retrieval-demo. Generatiivset mudelit ei kutsuta: see pole täielik RAG."""
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from projekt import ROOT

def retrieve(question, as_of):
    docs=json.loads((ROOT/'andmed/dokumendid.json').read_text(encoding='utf-8'))
    allowed=[d for d in docs if d['published'] <= as_of]
    if not allowed:return []
    v=TfidfVectorizer()
    matrix=v.fit_transform([d['text'] for d in allowed])
    scores=cosine_similarity(v.transform([question]),matrix)[0]
    order=scores.argsort()[::-1]
    return [{**allowed[i],'score':float(scores[i])} for i in order if scores[i]>0][:2]

if __name__=='__main__':
    results=retrieve('tulu kasvas','2024-02-29')
    print(json.dumps(results,ensure_ascii=False,indent=2))
    assert all(x['id'] != 'D2' for x in results)
    print('Leitud allikad võib anda LLM-ile; vasta ainult nende põhjal või ütle, et tõend puudub.')
