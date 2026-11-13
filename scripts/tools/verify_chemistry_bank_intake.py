#!/usr/bin/env python3
"""Verify all 17 uploaded supporting files, questions, calculations and diagrams."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib,re
from lxml import html
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'college/1-1/chemistry-engineers';R=S/'revision'
def read(name):return json.loads((R/name).read_text())
def main():
 data=read('question-bank-intake.json');page=html.fromstring((S/'question-banks.html').read_text())
 ids=page.xpath('//@id');assert len(ids)==len(set(ids))
 collections=data['collections'];assert len(collections)==17
 assert Counter(c['kind'] for c in collections)=={'question_bank':12,'numerical_practice':2,'notes_with_questions':1,'reference':2}
 assert len(data['deferred_exam_papers'])==4
 assert page.xpath('//body/@data-bank-allow-all')==['false']
 assert not page.xpath('//a[@data-bank-unit="all"]')
 assert 'Consolidated' not in page.text_content()
 assert page.xpath('//*[@id="unit-1" and not(@hidden)]')
 assert len(page.xpath('//*[@data-bank-unit-section and not(@hidden)]'))==1
 assert len(page.xpath('//details[contains(@class,"collection-question")]'))==622
 bank=read('question-bank-pending.json');oldids={q['id'] for q in bank['questions']+bank['additional_questions']}
 oldids.update(n.get('id') for u in [1,2] for n in html.fromstring((R/f'question-sections/unit-{u}.html').read_text()).xpath('//details[contains(@class,"study-accordion-item--example")]'))
 for id in oldids:assert page.get_element_by_id(id).tag=='details'
 count=0
 for c in collections:
  assert len(c['sha256'])==64 and c['pages']>0
  section=page.get_element_by_id(c['id']);assert c['title'] in section.text_content()
  assert page.xpath('//a[@data-bank-unit=$unit and contains(@href,$id)]',unit=str(c['unit']),id='#'+c['id'])
  assert len(section.xpath('.//details[contains(@class,"collection-question")]'))==len(c['questions'])
  if c['kind']=='reference':assert c['exercise_count']==0 and c['reviewed_pages']==list(range(1,c['pages']+1))
  for q in c['questions']:
   count+=1;node=page.get_element_by_id(q['id']);summary=node.find('summary').text_content()
   plain=lambda t:re.sub(r'\s+',' ',t).strip()
   if q['id'].startswith('intake-'):assert plain(q['prompt']) in plain(summary)
   if q.get('blocks'):
    for b in q['blocks']:
     if b['type']=='paragraph':assert b['text'] in node.text_content()
     elif b['type']=='equation':assert b['latex'] in node.text_content() and r'\frac' not in b['latex']
     elif b['type']=='figure':assert node.xpath('.//figure[@data-source-figure=$id]',id=b['id'])
   if q.get('check'):
    salts=q['check']['salts'];temporary=sum(Fraction(str(v))*100/m for _,v,m,t in salts if t);permanent=sum(Fraction(str(v))*100/m for _,v,m,t in salts if not t)
    assert temporary==Fraction(q['check']['temporary']);assert permanent==Fraction(q['check']['permanent'])
    assert f'{float(temporary):.2f}' in node.text_content() and f'{float(permanent):.2f}' in node.text_content()
   if q.get('correction'):assert node.xpath('.//aside[contains(@class,"study-mismatch-note")]')
 assert count==428
 extra=next(q for c in collections for q in c['questions'] if q['number']=='Additional (a)')
 assert extra['answer_ref']=='u2-qa-extra-0'
 assert 'Liquid metal corrosion' in page.get_element_by_id(extra['id']).text_content()
 # Independent checks of new numerical answers, including the printed-error case.
 new={q['number']:q for c in collections for q in c['questions'] if q['id'].startswith('intake-numerical-')}
 assert Fraction(new[1]['check']['temporary'])==100 and Fraction(new[1]['check']['permanent'])==Fraction(700,3)
 assert Fraction(new[2]['check']['temporary'])==Fraction(840,73)
 assert Fraction(new[2]['check']['permanent'])==Fraction(2126,57)
 assert Fraction(new[3]['check']['temporary'])==20 and Fraction(new[3]['check']['permanent'])==15
 assert Fraction(new[4]['check']['temporary'])==155 and Fraction(new[4]['check']['permanent'])==Fraction(3017,19)
 for node in page.xpath('//div[contains(@class,"study-example-solution")]'):
  assert not node.xpath('.//*[contains(@class,"document-source") or contains(@class,"study-solution-label")]')
  assert not any(t in node.text_content() for t in ['Answer basis:','Question source:','PankusDesk-authored'])
 figures={f['id']:f for name in ['source-figures.json','mid-2-source-figures.json','question-bank-intake-figures.json'] for f in read(name)['figures']}
 for node in page.xpath('//figure[@data-source-figure]'):
  f=figures[node.get('data-source-figure')];img=node.find('.//img');assert img.get('src')==f['asset'];assert img.get('alt')==f['alt']
  assert hashlib.sha256((ROOT/f['asset']).read_bytes()).hexdigest()==f.get('sha256',f.get('asset_sha256'))
 for f in read('question-bank-intake-figures.json')['figures']:assert page.xpath('//figure[@data-source-figure=$id]',id=f['id'])
 # No question or supplied figure disappears when sheets are regrouped.
 for u in [1,2]:
  source=html.fromstring((R/f'question-sections/unit-{u}.html').read_text())
  for src in source.xpath('//img/@src'):assert page.xpath('//img[@src=$src]',src=src)
 assert page.xpath('//*[contains(@class,"document-back-top")]/following-sibling::details[contains(@class,"document-contents")]')
 for href in page.xpath('//@href | //@src'):
  if href.startswith(('https:','http:')):continue
  path,_,id=href.partition('#');target=ROOT/path if path else S/'question-banks.html';assert target.exists(),href
  if id:assert html.fromstring(target.read_text()).xpath('//*[@id=$id]',id=id),href
 print('CHEMISTRY BANK INTAKE: PASS — 17 files, 428 supplied occurrences / 622 total questions, 4 independent numerical checks, complete set links and figure identities; four exam papers deferred.')
if __name__=='__main__':main()
