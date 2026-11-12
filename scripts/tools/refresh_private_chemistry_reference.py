#!/usr/bin/env python3
"""Refresh the private Chemistry reference JSON after reviewed public answer changes.
Raw source extraction/review is a separate intake step; this cannot invent missing pages.
Never writes the private corpus inside the public Git checkout.
"""
from pathlib import Path
import argparse,hashlib,json
ROOT=Path(__file__).resolve().parents[2];SUB=ROOT/'college/1-1/chemistry-engineers';REV=SUB/'revision'
def load(p):return json.loads(p.read_text())
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--corpus',type=Path,required=True);args=parser.parse_args();path=args.corpus.resolve()
 if path==ROOT or ROOT in path.parents:parser.error('Private source corpus must remain outside the public Git checkout.')
 data=load(path);inventory=load(REV/'source-inventory.json');known={s['id']:s['sha256'] for s in inventory['sources']}
 assert {s['id']:s['sha256'] for s in data['sources']}==known,'Source intake must be reconciled before refresh.'
 for source in data['sources']:
  original=Path(source['private_path']);assert original.is_file(),source['id'];assert hashlib.sha256(original.read_bytes()).hexdigest()==source['sha256'],source['id']
 data['questions']=load(REV/'question-bank-pending.json');data['authored_answers']=load(REV/'question-bank-solutions.json');data['answer_audit']=load(REV/'consolidation-answer-review.json')
 data['retained_solved_banks']={p.name:p.read_text() for p in sorted((REV/'question-sections').glob('*.html'))}
 data['canonical_existing_notes']={str(p.relative_to(SUB)):load(p) for p in sorted((SUB/'kb/data').glob('*.json'))}
 data['labelled_notes_additions']=load(REV/'college-notes-additions.json')
 data['approved_source_figures']=load(REV/'source-figures.json')
 data['selected_college_notes']={p.name:load(p) for p in sorted(REV.glob('unit-*-senior-notes.json'))}
 data['retrieval_index']={key:{'title':module['title'],'source_refs':module['source_refs'],'question_ids':[id for id,a in data['authored_answers']['answers'].items() if key in a.get('modules',[])]} for key,module in data['authored_answers']['modules'].items()}
 assert set(data['authored_answers']['answers'])=={q['id'] for q in data['questions']['questions']+data['questions']['additional_questions']}
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 audit=load(REV/'reference-corpus-audit.json');audit['private_corpus_sha256']=hashlib.sha256(path.read_bytes()).hexdigest();audit['answer_modules']=len(data['authored_answers']['modules']);audit['new_authored_answers']=len(data['authored_answers']['answers']);audit['additional_embedded_questions']=len(data['questions']['additional_questions']);audit['textbook_captures_extracted']=len(data.get('textbook_captures',[]));(REV/'reference-corpus-audit.json').write_text(json.dumps(audit,indent=2)+'\n')
 print(f'PRIVATE REFERENCE: refreshed {len(known)} source identities and {len(data["authored_answers"]["answers"])} authored answers; private JSON not staged or published.')
if __name__=='__main__':main()
