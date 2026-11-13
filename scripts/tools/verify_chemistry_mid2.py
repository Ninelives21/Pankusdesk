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
assert len(page.xpath('//*[@data-bank-unit-section!="faq"]//details[contains(@class,"collection-question")]'))==44
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
   assert sub['answer']['blocks'] and sub['answer']['source_refs']
   for block in sub['answer']['blocks']:
    kind=block['type'];assert kind in ['paragraph','list','table','equation','figure']
    if kind=='paragraph':assert block['text'] in panel.text_content()
    elif kind=='list':
     assert block['items']
     for item in block['items']:assert item in panel.text_content()
    elif kind=='table':
     assert block['headers'] and block['rows']
     for row in block['rows']:
      assert len(row)==len(block['headers'])
      for cell in row:assert cell in panel.text_content()
    elif kind=='equation':
     assert block['latex'] in panel.text_content()
     assert r'\frac' not in block['latex']
    elif kind=='figure':assert panel.xpath('.//figure[@data-source-figure=$id]',id=block['id'])
   for ref in sub['answer']['source_refs']:assert ref['source_id'] in lookup
 for record in p['source_records']:assert len(record['sha256'])==64 and record['page']==1
for f in json.loads((R/'mid-2-source-figures.json').read_text())['figures']:
 assert hashlib.sha256((ROOT/f['asset']).read_bytes()).hexdigest()==f['sha256']
 assert page.xpath('//figure[@data-source-figure=$id]',id=f['id'])
 if f.get('student_note'):assert f['student_note'] in page.text_content()
 assert f['source_sha256']==lookup[f['source_id']]['sha256']
# Required drawings stay with the exact essay/subpart they explain.
required_figures={
 'cfe-mid2-2025-12-30-r25-b-1':['mid2-pem-electrolysis'],
 'cfe-mid2-2025-12-30-r25-b-2':['mid2-lithium'],
 'cfe-mid2-2025-12-30-r25-b-5-a':['handout-stm-apparatus'],
 'cfe-mid2-2025-12-30-r25-b-6-b':['handout-biosensor-chain'],
 'cfe-mid2-2024-07-04-r22-b-2':['mid2-lithium'],
 'cfe-mid2-2024-07-04-r22-b-3-a':['mid2-impressed'],
 'cfe-mid2-2024-07-04-r22-b-4':['mid2-hydrogen-corrosion','mid2-oxygen-corrosion'],
 'cfe-mid2-2024-07-04-r22-b-5-a':['handout-biosensor-chain'],
 'cfe-mid2-2024-01-04-r22-b-1':['mid2-lithium'],
 'cfe-mid2-2024-01-04-r22-b-3':['mid2-hydrogen-corrosion','mid2-oxygen-corrosion'],
 'cfe-mid2-2024-01-04-r22-b-4-a':['mid2-waterline'],
 'cfe-mid2-2024-01-04-r22-b-4-b':['mid2-pitting'],
 'cfe-mid2-2024-01-04-r22-b-6':['handout-stm-apparatus','handout-afm-apparatus'],
 'cfe-mid2-2023-03-06-r22-b-2':['mid2-methanol'],
 'cfe-mid2-2023-03-06-r22-b-3':['mid2-hydrogen-corrosion','mid2-oxygen-corrosion'],
 'cfe-mid2-2023-03-06-r22-b-4-b':['mid2-sacrificial'],
 'cfe-mid2-2023-03-06-r22-b-6-a':['mid2-thick-film'],
 'cfe-mid2-2023-03-06-r22-b-6-b':['handout-boundary-lubrication']}
for id,figures in required_figures.items():
 panel=page.get_element_by_id(id)
 for figure in figures:assert panel.xpath('.//figure[@data-source-figure=$id]',id=figure),(id,figure)
# Source references remain valid in metadata; none are shown inside answers.
for panel in page.xpath('//div[contains(@class,"study-example-solution")]'):
 assert not panel.xpath('.//*[contains(@class,"document-source") or contains(@class,"study-solution-label")]')
 assert not any(x in panel.text_content() for x in ['Answer basis:','Question source:','SHA-256','Scope:'])
assert 'Paper provenance and duplicate captures' not in page.text_content()
# FAQ is limited to R25 Mid II units and uses verifiable paper references.
faq=json.loads((R/'mid-2-faq.json').read_text())
assert faq['paper_count']==len(d['papers'])==4
records={};kinds={};paper_ids={}
for paper in d['papers']:
 for kind in ['part_a','part_b']:
  for q in paper[kind]:
   for item in [q]+q.get('parts',[]):records[item['id']]=item;kinds[item['id']]='short' if kind=='part_a' else 'essay';paper_ids[item['id']]=paper['id']
assert len(faq['entries'])==5
assert page.xpath('//body/@data-bank-allow-all')==['false']
assert not page.xpath('//a[@data-bank-unit="all"]')
assert 'All four papers' not in page.text_content()
assert page.xpath('//a[@data-bank-unit="faq"]')
expected={'mid2-faq-self-healing':3,'mid2-faq-lithium-ion':3,'mid2-faq-stm-afm':4,'mid2-faq-battery-classification':2,'mid2-faq-biosensors':2}
for entry in faq['entries']:
 assert entry['r25_unit'] in [3,4,5]
 assert all(id in records and kinds[id]==entry['kind'] for id in entry['topic_matches'])
 count=len({paper_ids[id] for id in entry['topic_matches']});assert count==expected[entry['id']]
 panel=page.get_element_by_id(entry['id']);assert f'{count} of 4 papers' in panel.find('summary').text_content()
 for ref in entry['answer_refs']:
  assert ref['id'] in records
  for block in records[ref['id']]['answer']['blocks']:
   if block['type']=='paragraph':assert block['text'] in panel.text_content()
   if block['type']=='figure':assert panel.xpath('.//figure[@data-source-figure=$id]',id=block['id'])
lithium=next(x for x in faq['entries'] if x['id']=='mid2-faq-lithium-ion')
assert len({paper_ids[id] for id in lithium['topic_matches']+lithium['related_matches']})==4
assert all(kinds[id]=='short' for id in lithium['related_matches'])
stm=next(x for x in faq['entries'] if x['id']=='mid2-faq-stm-afm')
assert sum(any(word in records[id]['prompt'] for word in ['AFM','Atomic Force Microscope']) for id in stm['topic_matches'])==3
biosensors=next(x for x in faq['entries'] if x['id']=='mid2-faq-biosensors')
assert sum('glucose' in records[id]['prompt'].lower() for id in biosensors['topic_matches'])==1
# Legacy combined-view links now land inside FAQ, not an all-paper view.
assert page.get_element_by_id('all-papers').getparent().get('id')==faq['id']
# Internal and asset URLs resolve.
for url in page.xpath('//@href | //@src'):
 if url.startswith(('http:','https:')):continue
 path,_,frag=url.partition('#');target=ROOT/path if path else S/'mid-2.html';assert target.exists(),url
 if frag:assert html.fromstring(target.read_text()).xpath('//*[@id=$id]',id=frag),url
assert page.xpath('//*[contains(@class,"document-back-top")]/following-sibling::details[contains(@class,"document-contents")]')
assert len(page.xpath('//p[contains(@class,"paper-or")]'))==12
cards=json.loads((S/'index-resources.json').read_text())['questions'];assert sum(x['href']=='mid-2.html' for x in cards)==1
print(f'CHEMISTRY MID II: PASS — 4 papers, 44 questions / {parts} answer parts, 12 OR pairs, original marks, source citations/anchors and unchanged image identities; answer-only display; five checked R25 FAQ groups.')
