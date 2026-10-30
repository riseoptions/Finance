"""Synthetic topic triage. No credibility or person scoring."""
import csv,json
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import f1_score,confusion_matrix
from assistant import ROOT

def main():
    rows=list(csv.DictReader((ROOT/'data/nlp.csv').open(encoding='utf-8')))
    sets={s:[r for r in rows if r['split']==s] for s in ['train','dev','test']}
    assert not ({r['group'] for r in sets['train']} & {r['group'] for r in sets['test']})
    assert not ({r['group'] for r in sets['dev']} & {r['group'] for r in sets['test']})
    x=lambda s:[r['text'] for r in sets[s]];y=lambda s:[r['label'] for r in sets[s]]
    models={'majority':make_pipeline(TfidfVectorizer(),DummyClassifier(strategy='most_frequent')),
      'tfidf_logreg':make_pipeline(TfidfVectorizer(ngram_range=(1,2)),LogisticRegression(max_iter=1000,random_state=42))}
    scores={}
    for name,m in models.items():
        m.fit(x('train'),y('train'))
        scores[name]={s:{'macro_f1':f1_score(y(s),m.predict(x(s)),average='macro'),
            'confusion_matrix':confusion_matrix(y(s),m.predict(x(s)),labels=['arvamus','hange','keskkond']).tolist()} for s in ['dev','test']}
    out={'synthetic':True,'labels':['arvamus','hange','keskkond'],'n':{s:len(v) for s,v in sets.items()},'scores':scores,
         'deployment':'Ei rakendata pärisandmetele ilma sõltumatu eestikeelse hindamiskoguta. Testiga ei häälestatud.'}
    (ROOT/'reports/ml_metrics.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
