#!/usr/bin/env python3
"""Validate the package and audit contracts; stdlib only. No literary-fidelity claims."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT

def runtime_hash():
    h=hashlib.sha256()
    for p in sorted([SKILL/'SKILL.md', *(SKILL/'references').rglob('*.md')]):
        h.update(p.relative_to(SKILL).as_posix().encode()+b'\0'+p.read_bytes()+b'\0')
    return 'sha256:'+h.hexdigest()

def main():
    errors=[]
    def require(ok,msg):
        if not ok:errors.append(msg)
    def load(name):return json.loads((ROOT/'fidelity-ledger'/name).read_text())
    try:
        core=(SKILL/'SKILL.md').read_text()
        require(re.search(r'^name: tocqueville-investigator-perspective$',core,re.M),'Unexpected skill name')
        require((ROOT/'SKILL.md').is_file() and not (ROOT/'SKILL.md').is_symlink(),'Root SKILL.md must be a regular file')
        require((ROOT/'references').is_dir() and not (ROOT/'references').is_symlink(),'Root references must be a real directory')
        require(not (ROOT/'.agents/skills').exists(),'Unexpected nested runtime package')
        for p in ROOT.rglob('*'):
            if '.git' not in p.parts:require(not p.is_symlink(),'Unexpected symlink: '+str(p.relative_to(ROOT)))
        for heading in ['The axis','How I read a question','What I will not concede','How I move in an exchange','How I sound','What my vocabulary is for','When I stop','Loading depth (host-agent note)']:
            require('## '+heading in core,'Missing core section: '+heading)
        for p in sorted(ROOT.rglob('*.md')):
            if '.git' in p.parts:continue
            text=p.read_text()
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
                target=target.strip('<>').split('#')[0]
                if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target):continue
                path=p.parent/target
                require(path.exists(),f'{p.relative_to(ROOT)}: missing link {target}')
                if p==ROOT/'README.md':
                    relative=path.relative_to(ROOT)
                    require(not any((ROOT/Path(*relative.parts[:i])).is_symlink() for i in range(1,len(relative.parts)+1)),f'README link traverses a symlink instead of a GitHub file path: {target}')
            if p==SKILL/'SKILL.md' or p.is_relative_to(SKILL/'references'):
                require(not p.name.startswith(('provenance','fidelity','scores')),'Audit file in runtime: '+str(p))
        for target in re.findall(r'`(references/[^`]+\.md)`',core):
            require((SKILL/target).is_file(),'Missing runtime route: '+target)
        spans=load('source-spans.json');source_ids={x['id'] for x in load('source-manifest.json')};cluster_ids={x['id'] for x in spans}
        for x in spans:require(x['source'] in source_ids and x['start_line']<=x['end_line'],'Invalid source span: '+x['id'])
        elements=load('extractions.json');ids={x['id'] for x in elements};require(len(ids)==len(elements),'Duplicate element IDs')
        scores=load('scores.json');require(abs(sum(scores['weights'].values())-1)<1e-8,'Weights do not sum to one')
        decisions={x['id']:x for x in scores['decisions']};require(ids==set(decisions),'Extraction/decision IDs differ')
        for e in elements:
            require(set(e['clusters'])<=cluster_ids,'Unresolved source IDs for '+e['id'])
            require(bool(e['evidence']),'No evidence for '+e['id'])
            if e['type'] in ['regularity','verdict']:require(len(set(e['clusters']))>=2,'Insufficient distinct source units: '+e['id'])
            if e['type']=='procedure':require(all(k in e for k in ['order','precondition','on_fail']),'Incomplete procedure '+e['id'])
            if e['type']=='cost_refusal':require(bool(e.get('convenient_move')),'Missing divergence '+e['id'])
            d=decisions[e['id']];expected=sum(scores['weights'][k]*v for k,v in d['scores'].items())
            require(abs(expected-d['composite'])<1e-6,'Incorrect composite: '+e['id'])
            require(d['decision']=='cut' or d['composite']>=.55,'Unlogged below-threshold retention: '+e['id'])
        counts=scores['core_budget']['counts'];formula=2200+250*min(counts['cost_refusal'],6)+180*min(counts['projectible'],7)+200*min(counts['procedure'],5)+150*min(counts['verdict'],8)+140*min(counts['interactional'],5)+120*min(counts['variation'],4)
        require(formula==scores['core_budget']['supply'],'Incorrect core budget supply')
        fidelity=load('fidelity.json')
        if fidelity['stale']:
            require(fidelity['stale']==['runtime_package'] and bool(fidelity.get('maintenance_note')),'Unexplained historical fidelity results')
            require(fidelity.get('current_runtime_hash')==runtime_hash(),'Runtime changed since maintenance review')
        else:
            require(fidelity['content_hash']==runtime_hash(),'Runtime changed: fidelity results are stale')
        hashes=load('test-hashes.json')
        for name,expected in hashes['samples'].items():
            require(hashlib.sha256((ROOT/'fidelity-ledger/samples'/name).read_bytes()).hexdigest()==expected,'Sample changed: '+name)
        key=load('discrimination-key.json')['labels'];answers=load('gate-results.json')['discrimination']['answers']
        require(len(answers)==len(key),'Discrimination denominator mismatch')
        measured=sum(a==key[str(i+1)] for i,a in enumerate(answers))/len(answers)
        require(measured==fidelity['discrimination']['score'],'Discrimination score/key mismatch')
        require(fidelity['cost']['presence_assertion']=='pass','Cost-presence assertion failed')
        for anchor in ['departmental council','oath','Gobineau','administrator','freedom only']:
            require(anchor in core,'Missing cost/commitment anchor: '+anchor)
        items=load('projection-items.json');overall=sum(x['score'] for x in items)/(2*len(items))
        require(abs(overall-fidelity['projection']['gate']['overall'])<1e-8,'Projection score/denominator mismatch')
        finals=load('projection-final.json');require(len(finals)==len(items),'Incomplete final projection review')
        require(abs(sum(x['score'] for x in finals)/(2*len(finals))-fidelity['projection']['final']['overall'])<1e-8,'Final projection arithmetic mismatch')
        require(load('holdout-split.json')['n_masked']==fidelity['projection']['n_masked'],'Mask count mismatch')
        for p in (ROOT/'fidelity-ledger/samples').glob('*.md'):
            for phrase in ['win-win','actionable insights','game changer','as an ai']:
                require(phrase not in p.read_text().lower(),'Avoid-list violation in '+p.name)
        require(max(len(p.read_text().split()) for p in (ROOT/'fidelity-ledger/samples').glob('*.md'))>=400,'No sustained-prose sample')
        # Prevent accidental publishing of the local source corpus or workstation paths.
        for p in ROOT.rglob('*'):
            if '.git' in p.parts or not p.is_file() or p.is_symlink():continue
            require(p.stat().st_size<350000,'Unexpectedly large tracked artifact: '+str(p.relative_to(ROOT)))
            if p.suffix in {'.md','.json','.py'}:
                require(('/Users/'+'Extracurriculars/') not in p.read_text(),'Private corpus path in '+str(p.relative_to(ROOT)))
    except (OSError,KeyError,ValueError) as ex:
        errors.append(str(ex))
    if errors:
        print('\n'.join('ERROR: '+s for s in errors));return 1
    print('PASS: package, links, source IDs, scoring, sample coverage, and current runtime hash.')
    if fidelity['stale']:print('NOTE: fidelity results are historical; runtime fidelity has not been rerun after maintenance.')
    return 0
if __name__=='__main__':sys.exit(main())
