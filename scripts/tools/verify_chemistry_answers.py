#!/usr/bin/env python3
"""Check answer/source coverage, declared corrections and reproducible numerical cases.
This does not certify lecturer approval or diagram fidelity.
"""
from pathlib import Path
from fractions import Fraction
import json,re
ROOT=Path(__file__).resolve().parents[2];R=ROOT/'college/1-1/chemistry-engineers/revision'
def load(n):return json.loads((R/n).read_text())
def main():
 bank=load('question-bank-pending.json');sol=load('question-bank-solutions.json');sources=load('source-inventory.json')['sources'];lookup={s['id']:s for s in sources};lookup.update({s['source_id']:s for s in sources if s.get('source_id')})
 questions=bank['questions']+bank['additional_questions'];assert len(bank['questions'])==244;assert len(bank['additional_questions'])==130;assert len(questions)==len({q['id'] for q in questions})==374
 assert set(sol['answers'])=={q['id'] for q in questions}
 for key,module in sol['modules'].items():
  assert module['paragraphs'] and module['source_refs'],key
  for ref in module['source_refs']:
   source=lookup[ref['source_id']]
   for page in ref['pages']:assert 0<page<=source['pages_or_slides'],(key,page)
 for q in questions:
  a=sol['answers'][q['id']];assert a['review_state']=='text_authored_source_qualified',q['id']
  if re.search('diagram|illustration|labelled|labeled',q['original_prompt'],re.I):assert a['diagram_required'] and a['figure_status'],q['id']
  for key,indices in a.get('paragraph_selection',{}).items():
   assert key in a['modules'];assert indices and all(0<=i<len(sol['modules'][key]['paragraphs']) for i in indices),q['id']
  if a.get('subpart_answers'):assert len(a['subpart_answers'])==len({p['label'] for p in a['subpart_answers']}),q['id']
 # Independent recomputation of repeated water-bank numerical data.
 def eq(c,m):return Fraction(str(c))*100/Fraction(str(m))
 assert eq(146,146)+eq(40.5,162)==125
 assert eq(34,136)+eq(60,120)==75
 assert eq(73,146)+eq(162,162)==150
 assert eq(136,136)+eq(95,95)+150==350
 assert eq(16.2,162)+eq(14.6,146)==20
 assert eq(111,111)+eq(1.36,136)==101
 # Atom/charge bookkeeping for the corrected glucose and principal cell reactions.
 # Vector order: C,H,O,Zn,Na,Cl,N,S,charge. Coefficients include electrons explicitly.
 species={'glucose':(6,12,6,0,0,0,0,0,0),'O2':(0,0,2,0,0,0,0,0,0),'H2O':(0,2,1,0,0,0,0,0,0),'acid':(6,12,7,0,0,0,0,0,0),'peroxide':(0,2,2,0,0,0,0,0,0),'lactone':(6,10,6,0,0,0,0,0,0),'Zn':(0,0,0,1,0,0,0,0,0),'ZnO':(0,0,1,1,0,0,0,0,0),'OH':(0,1,1,0,0,0,0,0,-1),'H+':(0,1,0,0,0,0,0,0,1),'e':(0,0,0,0,0,0,0,0,-1),'H2':(0,2,0,0,0,0,0,0,0)}
 def balanced(left,right):
  def total(side):return tuple(sum(n*species[k][i] for k,n in side.items()) for i in range(9))
  assert total(left)==total(right),(left,right)
 balanced({'glucose':1,'O2':1},{'lactone':1,'peroxide':1})
 balanced({'lactone':1,'H2O':1},{'acid':1})
 balanced({'glucose':1,'O2':1,'H2O':1},{'acid':1,'peroxide':1})
 balanced({'peroxide':1},{'O2':1,'H+':2,'e':2})
 balanced({'Zn':1,'OH':2},{'ZnO':1,'H2O':1,'e':2})
 balanced({'O2':1,'H2O':2,'e':4},{'OH':4})
 balanced({'H2':2},{'H+':4,'e':4})
 balanced({'O2':1,'H+':4,'e':4},{'H2O':2})
 assert 'thermoplastic' in sol['answers']['cfe-senior-u4-q-r25-short-5']['source_discrepancy']
 assert 'exponentially' in ' '.join(sol['modules']['stm']['paragraphs'])
 assert 'active' in ' '.join(sol['modules']['ir']['paragraphs'])
 print('CHEMISTRY ANSWERS: PASS — 374/374 authored entries, source/page bounds, answer selections, subparts, six independent numerical checks and eight atom/charge checks. Diagram/lecturer validation separate.')
if __name__=='__main__':main()
