"""Validate the Mid-II collection and compile/run its standalone C11 examples."""
import json,subprocess,tempfile
from pathlib import Path
p=Path(__file__).resolve().parents[2]/'college/1-1/programming-problem-solving/exam-prep/mid-2.json';d=json.loads(p.read_text());results=[]
assert len(d['questions'])==60 and len(d['occurrences'])==111
assert len(d['papers'])==3
sources={s['id'] for s in d['sources']}; occurrences={o['id'] for o in d['occurrences']}
assert len(sources)==len(d['sources']) and len(occurrences)==len(d['occurrences'])
assert all(len(s['sha256'])==64 for s in d['sources'])
seen=set(); covered=[]
for q in d['questions']:
 assert q['id'] not in seen and q['unit'] in [3,4,5] and q['answer'] in d['answers']; seen.add(q['id'])
 assert set(q['occurrences'])<=occurrences; covered+=q['occurrences']
assert sorted(covered)==sorted(occurrences), 'Each source occurrence must map exactly once'
for o in d['occurrences']: assert o['source'] in sources and o['page']>=1
for paper in d['papers']:
 assert set(paper['sources'])<=sources and paper['max_marks']==30
 assert sum(q['marks'] for q in paper['groups'][0]['parts'])==10
 for unit in [3,4,5]:
  choices=[g for g in paper['groups'] if g['unit']==unit]
  assert len(choices)==2 and not choices[0]['or_before'] and choices[1]['or_before']
  assert all(sum(q['marks'] for q in g['parts'])==(4 if unit==3 else 8) for g in choices)
 for group in paper['groups']:
  for q in group['parts']:
   assert q['id'] not in seen and q['answer'] in d['answers'];seen.add(q['id'])
for a in d['answers'].values(): assert all(pid in d['programs'] for pid in a['programs'])
print('PASS:60revision entries,111source occurrences, paper choice/mark integrity, unique anchors and all answer/program references.')
for key,program in d['programs'].items():
 with tempfile.TemporaryDirectory() as tmp:
  r=Path(tmp);c=r/'program.c';c.write_text(program['code']);exe=r/'program';compile=subprocess.run(['cc','-std=c11','-Wall','-Wextra','-Werror','-pedantic',str(c),'-o',str(exe)],capture_output=True,text=True)
  assert compile.returncode==0,(key,compile.stderr)
  (r/'input.txt').write_text('Hello C\n');args=[str(exe)]+(['hello'] if key=='command-line' else [])
  run=subprocess.run(args,input=program['input'],capture_output=True,text=True,cwd=r,timeout=10)
  assert run.returncode==0 and run.stdout==program['expected'],(key,run.returncode,run.stdout,program['expected'],run.stderr)
  if key=='copy-file':assert (r/'input.txt').read_bytes()==(r/'copy.txt').read_bytes()
  if key=='even-odd-files':assert (r/'even.txt').read_text()=='2\n4\n' and (r/'odd.txt').read_text()=='1\n3\n'
  if key in ['factorial','fibonacci','array-sum','gcd','ackermann']:
   bad={'factorial':'21','fibonacci':'21','array-sum':'21','gcd':'0 0','ackermann':'4 7'}[key];rr=subprocess.run(args,input=bad,capture_output=True,text=True,cwd=r,timeout=3);assert rr.returncode!=0,key
  results.append(key)
print('PASS:',len(results),'C11 programs compile warning-free; expected outputs/files match; selected invalid bounds rejected.')
