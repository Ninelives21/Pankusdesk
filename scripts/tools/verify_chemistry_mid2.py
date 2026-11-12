#!/usr/bin/env python3
"""Check Mid II source structure, complete answer parts, citations and asset identity."""
import hashlib,json
from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'college/1-1/chemistry-engineers';R=S/'revision'
d=json.loads((R/'mid-2-papers.json').read_text());page=html.fromstring((S/'mid-2.html').read_text())
ids=page.xpath('//@id');assert len(ids)==len(set(ids))
assert len(d['papers'])==4 and d['papers'][0]['regulation']=='R25'
assert page.xpath('//body/@data-bank-default')==[d['default_paper']]
assert len(page.xpath('//*[@data-bank-unit-section and not(@hidden)]'))==1
assert len(page.xpath('//details[contains(@class,"collection-question")]'))==44
sources=json.loads((R/'source-inventory.json').read_text())['sources'];lookup={x['id']:x for x in sources};lookup.update({x['source_id']:x for x in sources if x.get('source_id')})
parts=0
for p in d['papers']:
 assert len(p['part_a'])==5 and len(p['part_b'])==6
 assert [q['number'] for q in p['part_a']]==list('abcde')
 assert [q['marks'] for q in p['part_a']]==[2]*5
 assert [q['marks'] for q in p['part_b']]==[4,4,8,8,8,8]
 assert p['maximum_marks']==30 and p['source_records']
 for q in p['part_a']+p['part_b']:
  panel=page.get_element_by_id(q['id']);summary=panel.find('summary').text_content()
  assert q['prompt'] in summary
  blocks=q.get('parts',[q]);parts+=len(blocks)
  if 'parts' in q and all(x['marks'] is not None for x in blocks):assert sum(x['marks'] for x in blocks)==q['marks']
  for sub in blocks:
   assert sub['prompt'] in summary
   assert sub['answer']['paragraphs'] and sub['answer']['source_refs']
   for t in sub['answer']['paragraphs']:assert t in panel.text_content()
   for ref in sub['answer']['source_refs']:assert ref['source_id'] in lookup
 for record in p['source_records']:assert len(record['sha256'])==64 and record['page']==1
for f in json.loads((R/'mid-2-source-figures.json').read_text())['figures']:
 assert hashlib.sha256((ROOT/f['asset']).read_bytes()).hexdigest()==f['sha256']
 assert f['source_discrepancy'] in page.text_content()
 assert f['source_sha256']==lookup[f['source_id']]['sha256']
# Internal and asset URLs resolve, including cited source IDs.
for url in page.xpath('//@href | //@src'):
 if url.startswith(('http:','https:')):continue
 path,_,frag=url.partition('#');target=ROOT/path if path else S/'mid-2.html';assert target.exists(),url
 if frag:assert html.fromstring(target.read_text()).xpath('//*[@id=$id]',id=frag),url
assert page.xpath('//*[contains(@class,"document-back-top")]/following-sibling::details[contains(@class,"document-contents")]')
assert len(page.xpath('//p[contains(@class,"paper-or")]'))==12
cards=json.loads((S/'index-resources.json').read_text())['questions'];assert sum(x['href']=='mid-2.html' for x in cards)==1
print(f'CHEMISTRY MID II: PASS — 4 papers, 44 questions / {parts} answer parts, 12 OR pairs, original marks, source citations/anchors and unchanged diagram hash.')
