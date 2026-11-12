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
 for q in bank['questions']:
  assert q['id'] in qdoc.ids,q['id']
  assert normal(q['original_prompt']) in normal(qdoc.ids[q['id']].text()),q['id']
 assert len([n for n in qdoc.nodes if n.has_class('collection-question')])==len(bank['questions'])
 relocation=json.loads((R/'question-bank-relocation.json').read_text())
 nav=next(n for n in qdoc.nodes if n.tag=='nav' and n.attrs.get('aria-label')=='Collection contents')
 assert len([n for n in nav.elements() if n.tag=='a'])==6
 for unit,record in relocation['units'].items():
  fragment=(S/record['source_fragment']).read_bytes();assert hashlib.sha256(fragment).hexdigest()==record['html_sha256']
  old=Document((S/record['old_page']).read_text())
  for id in record['ids']:
   assert id in qdoc.ids,id
   assert id not in old.ids,(id,'still in notes')
  original=Document(fragment.decode())
  for id in record['ids']:assert normal(original.ids[id].text())==normal(qdoc.ids[id].text()),(id,'relocation changed content')
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
 print(f'CHEMISTRY COLLECTIONS: PASS — {len(sources)} distinct source identities, {len(bank["questions"])} original prompts, {len(additions)} cited explanations, links and Back to top.')
if __name__=='__main__':main()
