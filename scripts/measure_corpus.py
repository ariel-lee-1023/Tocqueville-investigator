#!/usr/bin/env python3
"""Rebuild source measurements from owned local books; never writes into the repository."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--corpus',type=Path,required=True)
p.add_argument('--distiller',type=Path,required=True,help='persona-distiller root containing scripts/')
p.add_argument('--work',type=Path,required=True,help='New or empty scratch directory outside this repository')
a=p.parse_args();w=a.work.resolve()
if w.is_relative_to(ROOT) or (w.exists() and any(w.iterdir())):p.error('--work must be an empty scratch directory outside the repository')
w.mkdir(parents=True,exist_ok=True)
scripts=a.distiller/'scripts'
def run(script,*args):subprocess.run([sys.executable,str(scripts/script),*map(str,args)],check=True)
manifest=json.loads((ROOT/'fidelity-ledger/source-manifest.json').read_text());sources={}
for m in manifest:
 f=a.corpus/m['file']
 if hashlib.sha256(f.read_bytes()).hexdigest()!=m['sha256']:p.error('Source checksum mismatch: '+m['file'])
 sources[m['id']]=f.read_text().splitlines()
prep=w/'prepared';prep.mkdir();rows=[]
spans=json.loads((ROOT/'fidelity-ledger/source-spans.json').read_text())
for c in spans:
 if int(c['id'][1:])>18:continue
 t='\n'.join(sources[c['source']][c['start_line']-1:c['end_line']])
 if c['attribution']=='firsthand':
  t=re.sub(r'\[[^\]]{0,120}\]','',t);t=re.sub(r'<[^>]+>','',t)
  t='\n'.join(l for l in t.splitlines() if not l.startswith('#') and not re.fullmatch(r'\s*\*+\s*',l))
 t=re.sub(r'(\w)[¬\u00ad]\s*\n?\s*(\w)',r'\1\2',t)
 (prep/(c['id']+'.md')).write_text(t)
 kind='dialogue' if c['id']=='c15' else 'decision_record' if c['id'] in ['c10','c11','c12'] else 'monologue'
 rows.append(dict(id=c['id'],label=c['label'],file=c['id']+'.md',kind=kind,attribution=c['attribution']))
spec=w/'segment-spec.json';spec.write_text(json.dumps({'source_root':str(prep),'clusters':rows},indent=2))
run('segment.py',spec,'--out',w)
run('corpus_clean.py',w/'clusters','--fix','--no-backup','--json',w/'cluster-cleaning.json')
units=w/'units';units.mkdir()
for f in (w/'clusters').glob('*.txt'):
 if int(f.name[1:3])>13:continue
 t=re.sub(r'\\?\[[^\]]*\]','',f.read_text(),flags=re.S);t=re.sub(r'\\?\*[a-z]\\?\b','',t)
 if f.name.startswith('c13'):t=re.sub(r'Count Louis de Kergorlay\s+de Kergorlay, Count Louis.{0,180}?Alexis de Tocqueville\s+de Tocqueville, Alexis','',t,flags=re.S)
 t=re.sub(r'(?m)^Count Louis de Kergorlay\s*$','',t);(units/f.name).write_text(t)
run('register_discover.py',units,'--json',w/'registers.json')
families=w/'families';families.mkdir()
for name,ids in [('c91',range(1,10)),('c92',range(10,13)),('c93',[13])]:
 (families/(name+'.txt')).write_text('\n\n'.join(next(units.glob(f'c{i:02}*')).read_text() for i in ids))
run('style_metrics.py',families,'--per-file','--json',w/'style-metrics.json')
run('holdout_split.py',ROOT/'fidelity-ledger/passages.json','--seed',42,'--frac',.12,'--stratify','--out',w/'holdout-split.json')
run('token_count.py',ROOT/'.agents/skills/tocqueville-investigator-perspective','--per-file','--json',w/'token-counts.json')
print('Measurements complete. Editorial inference and blind classification are separate human/agent tasks.')
