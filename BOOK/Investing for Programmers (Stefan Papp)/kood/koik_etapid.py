"""Üks offline käivitus: projekt, fundamentaalnäide, indikaatorid, RAG-demo ja lisapraktikumid."""
from pathlib import Path
import subprocess,sys
from tuum import OUT
HERE=Path(__file__).resolve().parent
for name in ['projekt.py','m02.py','m10.py','uurimisagent.py','lisapraktikumid.py','ml_lisad.py']:
    result=subprocess.run([sys.executable,str(HERE/name)],check=True,capture_output=True,text=True)
    (OUT/(Path(name).stem+'_jooks.txt')).write_text(result.stdout,encoding='utf-8')
parts=['# Ühine õppeprojekti raport\n\nKõik käesoleva koondjooksu turu- ja ettevõtteandmed on simuleeritud või fiktiivsed.\n']
for name in ['raport.md','agent_raport.md']:
    parts.append((OUT/name).read_text(encoding='utf-8'))
parts.append('## Fundamentaalnäite arvutus\n\n```text\n'+(OUT/'m02_jooks.txt').read_text(encoding='utf-8')+'\n```')
(OUT/'koondraport.md').write_text('\n\n'.join(parts),encoding='utf-8')
print(OUT/'koondraport.md')
