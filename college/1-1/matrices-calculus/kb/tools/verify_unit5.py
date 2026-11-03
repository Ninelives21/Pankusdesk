#!/usr/bin/env python3
"""Unit V intake, scope, anchor and preservation checks (no runtime dependency)."""
from pathlib import Path
import hashlib,json,re,subprocess
S=Path(__file__).resolve().parents[2]; D=S/'kb/data'
def read(path):return json.loads(path.read_text())
topics=read(D/'topics.json');bank=read(D/'textbook-questions.json');manifest=read(D/'source-manifest.json');book=read(D/'book-index.json')
unit=[t for t in topics if t['unit']==5];core=[t for t in unit if t['status']=='core']
assert len(core)==9 and all(t['sections'] and t['source_coverage']=='complete-theory' for t in core)
cap=read(S/'kb/audits/mac-unit5-source-captures.json')
assert sorted(c['capture_number'] for c in cap)==list(range(1,51))
assert sorted(c['printed_page'] for c in cap)==list(range(315,365))
refs={r['source_id'] for r in book}|{r['source_id'] for r in manifest['syllabus_refs']}
q=bank['units']['5'];expected={1:set(range(1,19)),2:set(range(1,9)),3:set(range(1,12)),4:set(range(1,29))-{27},9:{5,*range(9,19)},10:{1,2,3,7,8,11,12,*range(13,30),32,33,41,42,43}}
ids=set();count=0
for g in q['groups']:
 n=int(g['id'].split('-')[-1]);assert {a['number'] for a in g['questions']}==expected[n]
 for a in g['questions']:
  assert a['id'] not in ids;ids.add(a['id']);count+=1
  assert a['question_source_refs'] and set(a['question_source_refs']+a['answer_source_refs'])<=refs
  assert a['answer'].get('paragraphs') or a['answer'].get('parts')
  assert a['answer'].get('result')
  for part in a.get('question_parts',[]):assert part.get('id')
assert count==104
ex=[a for t in unit for s in t['sections'] for a in s.get('accordions',[])]
assert len(ex)==38 and len({a['id'] for a in ex})==38
for a in ex:
 assert a['question_paragraphs'] and a['final_answer'] and (a.get('paragraphs') or a.get('solution_parts'))
for t in unit:
 assert set(t['source_refs'])<=refs
 for sec in t['sections']:assert set(sec['source_refs'])<=refs
figs=read(S/'kb/audits/mac-unit5-ros-figures.json');assert len(figs)==37
for f in figs:
 assert hashlib.sha256((S/f['output']).read_bytes()).hexdigest()==f['output_sha256']
 assert f['pixel_comparison']=='identical to original crop' and len(f['crop_xyxy'])==4
# Keep all pre-existing theory, practice, dated/undated class data and binaries intact.
root=S.parents[2];base='3498dd4167f9ab282f2dbba92f81bc038a415c18'
for filename,key in [('topics.json',None),('textbook-questions.json','units')]:
 rel=(D/filename).relative_to(root);old=json.loads(subprocess.check_output(['git','show',base+':'+str(rel)],cwd=root));now=read(D/filename)
 if key:
  for n in ['1','2','3','4']:assert old[key][n]==now[key][n]
 else:
  for t in old:
   if t['unit']!=5:assert t==next(a for a in now if a['id']==t['id'])
print('UNIT V VERIFY: PASS — 50 captures, 9 core topics, 38 examples, 104 questions, 37 ROS assets; I–IV preserved')
