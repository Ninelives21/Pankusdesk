#!/usr/bin/env python3
"""Validate source identity, question fidelity and links in Chemistry collections."""
from pathlib import Path
import json
import hashlib
import re
from urllib.parse import urlsplit,unquote
from verify_cfe_revision_structure import Document
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'college/1-1/chemistry-engineers';R=S/'revision'
def normal(text):return re.sub(r'\s+',' ',text).strip()
def main():
 inventory=json.loads((R/'source-inventory.json').read_text());sources=inventory['sources'];ids={s['id'] for s in sources};assert len(ids)==len(sources)
 assert len({s['sha256'] for s in sources})==len(sources)
 assert {s['unit'] for s in sources}=={1,2,3,4,5}
 for s in sources:
  assert re.fullmatch(r'[0-9a-f]{64}',s['sha256']);assert s['filename'];assert s['aliases']
  if s.get('equivalent_to'):assert s['equivalent_to'] in ids
  assert '/workspace/' not in json.dumps(s)
 bank=json.loads((R/'question-bank-pending.json').read_text());qdoc=Document((S/'question-banks.html').read_text())
 all_questions=bank['questions']+bank.get('additional_questions',[])
 solutions=json.loads((R/'question-bank-solutions.json').read_text())
 assert len({q['id'] for q in all_questions})==len(all_questions)
 assert set(solutions['answers'])=={q['id'] for q in all_questions}
 for q in all_questions:
  assert q['id'] in qdoc.ids,q['id']
  assert normal(q['original_prompt']) in normal(qdoc.ids[q['id']].text()),q['id']
  node=qdoc.ids[q['id']];assert node.tag=='details',q['id']
  assert any(n.has_class('study-example-solution') for n in node.elements()),q['id']
  answer=solutions['answers'][q['id']]
  assert answer.get('modules') or answer.get('existing_answer_id') or answer.get('existing_answer_ids'),q['id']
  for key in answer.get('modules',[]):
   module=solutions['modules'][key];assert module['source_refs'] and module['paragraphs'],key
   assert all(len(p.strip())>20 for p in module['paragraphs']),key
 intake=json.loads((R/'question-bank-intake.json').read_text())
 relocation=json.loads((R/'question-bank-relocation.json').read_text())
 expected={q['id'] for q in all_questions}|{n.attrs['id'] for x in relocation['units'].values() for n in Document((S/x['source_fragment']).read_text()).nodes if n.tag=='details' and n.has_class('study-accordion-item--example')}|{q['id'] for c in intake['collections'] for q in c['questions']}
 actual={n.attrs['id'] for n in qdoc.nodes if n.has_class('collection-question')}
 assert actual==expected,(actual-expected,expected-actual)
 # Supplied bank prompts have one public home; unique teaching examples remain in notes.
 bank_entries=[n for n in qdoc.nodes if n.tag=='details' and n.has_class('study-accordion-item--example')]
 bank_entry_ids={n.attrs['id'] for n in bank_entries}
 bank_prompts=[normal(n.text()) for n in qdoc.nodes if n.has_class('study-example-question')]
 for u in range(1,6):
  filename='end-sem-notes.html' if u==1 else f'end-sem-unit-{u}.html'
  note=Document((S/filename).read_text());note_text=normal(note.root.text())
  assert not bank_entry_ids.intersection(note.ids),(filename,'bank entry duplicated in notes')
  for prompt in bank_prompts:assert prompt not in note_text,(filename,prompt,'bank prompt duplicated in notes')
  assert ('hidden' in qdoc.ids[f'unit-{u}'].attrs)==(u!=1),('initial unit visibility',u)
 relocation=json.loads((R/'question-bank-relocation.json').read_text())
 nav=next(n for n in qdoc.nodes if n.tag=='nav' and n.attrs.get('aria-label')=='Collection contents')
 assert len([n for n in nav.elements() if n.tag=='a'])==5+len(intake['collections'])
 assert not any(n.attrs.get('data-bank-unit')=='all' for n in nav.elements())
 assert qdoc.root.text().find('Consolidated · All units')==-1
 for unit,record in relocation['units'].items():
  fragment=(S/record['source_fragment']).read_bytes();assert hashlib.sha256(fragment).hexdigest()==record['html_sha256']
  old=Document((S/record['old_page']).read_text())
  for id in record['ids']:
   assert id in qdoc.ids,id
   assert id not in old.ids,(id,'still in notes')
  original=Document(fragment.decode())
  for id in record['ids']:
   old=original.ids[id];new=qdoc.ids[id]
   if old.tag!='details':continue
   prompts=lambda node:[normal(n.text()) for n in node.elements() if n.has_class('study-example-question')]
   assert prompts(old)==prompts(new),(id,'original prompt changed')
   for equation in re.findall(r'\\\(.*?\\\)|\\\[.*?\\\]',old.text(),re.S):assert equation in new.text(),(id,'equation lost')
   assert [n.attrs['src'] for n in old.elements() if n.tag=='img']==[n.attrs['src'] for n in new.elements() if n.tag=='img'],(id,'original drawing changed')
 additions=json.loads((R/'college-notes-additions.json').read_text())['additions']
 for a in additions:
  assert a['source_id'] in ids and a['pages']
  f='end-sem-notes.html' if a['unit']==1 else f'end-sem-unit-{a["unit"]}.html'
  doc=Document((S/f).read_text());assert a['id'] in doc.ids
  assert 'PankusDesk' in doc.ids[a['id']].text()
 for f in ['college-notes.html','question-banks.html']:
  doc=Document((S/f).read_text());allids=[n.attrs['id'] for n in doc.nodes if 'id' in n.attrs];assert len(allids)==len(set(allids)),f
  assert any(n.has_class('document-back-top') for n in doc.nodes)
  for n in doc.nodes:
   if n.tag!='a' or 'href' not in n.attrs:continue
   u=urlsplit(n.attrs['href'])
   if u.scheme or u.netloc:
    assert u.scheme=='https',n.attrs['href']
    continue
   target=ROOT/unquote(u.path)
   assert target.is_file(),(f,n.attrs['href'])
   if u.fragment:assert unquote(u.fragment) in Document(target.read_text()).ids,(f,n.attrs['href'])
  assert not any(n.tag in ['iframe','embed','object'] for n in doc.nodes)
 print(f'CHEMISTRY COLLECTIONS: PASS — {len(sources)} distinct source identities, {len(actual)} retained/intake prompts, {len(additions)} cited explanations, links and Back to top.')
if __name__=='__main__':main()
