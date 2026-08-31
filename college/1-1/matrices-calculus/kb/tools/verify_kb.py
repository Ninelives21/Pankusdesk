#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]; D=ROOT/'data'; errors=[]
manifest=json.loads((D/'source-manifest.json').read_text()); syllabus=json.loads((D/'syllabus.json').read_text()); coverage=json.loads((D/'coverage-audit.json').read_text()); topics=json.loads((D/'topics.json').read_text()); status=json.loads((D/'kb-status.json').read_text()); book=json.loads((D/'book-index.json').read_text()); qbank=json.loads((D/'textbook-questions.json').read_text())
expected_atoms=43
if manifest['course']['code']!='25BS1MT101': errors.append('course code changed')
if len(syllabus.get('units',[]))!=5: errors.append('R25 unit count != 5')
if len(coverage)!=expected_atoms: errors.append('R25 coverage atom count mismatch')
core=[t for t in topics if t.get('status')!='supporting']; supporting=[t for t in topics if t.get('status')=='supporting']
if len(core)!=expected_atoms: errors.append('R25 core topic count mismatch')
valid={x['source_id'] for x in manifest.get('syllabus_refs',[])}|{x['source_id'] for x in book}|{x['id'] for x in manifest.get('class_sources',[])}|{x['id'] for x in manifest.get('gap_sources',[])}
ids=set()
for t in topics:
    if t['id'] in ids: errors.append('duplicate topic '+t['id'])
    ids.add(t['id'])
    bad=[r for r in t.get('source_refs',[]) if r not in valid]
    if bad: errors.append('unresolved refs '+t['id']+': '+','.join(bad))
    if t.get('unit') in (1,2) and not t.get('sections'): errors.append('ready topic has no sections '+t['id'])
    if t.get('unit')==1:
        blob=json.dumps(t,ensure_ascii=False)
        if '\\frac' in blob: errors.append('Unit I authored topic uses \\frac '+t['id'])
for c in coverage:
    want='COVERED' if c.get('unit') in (1,2) else 'SOURCE_GAP'
    if c.get('status')!=want: errors.append('coverage status mismatch: '+c.get('syllabus_atom','?'))
if status.get('source_gap_count')!=27: errors.append('source gap count must be 27 after Units I–II')
if status.get('ready_units')!=[1,2]: errors.append('ready units must be [1, 2]')
if status.get('supporting_topic_count')!=len(supporting): errors.append('supporting topic count mismatch')
unit=qbank.get('units',{}).get('1',{}); qids=set(); count=0
for g in unit.get('groups',[]):
    for q in g.get('questions',[]):
        count+=1
        if q['id'] in qids: errors.append('duplicate question '+q['id'])
        qids.add(q['id'])
        if q.get('topic_id') not in ids: errors.append('unknown question topic '+str(q.get('topic_id')))
        for r in q.get('question_source_refs',[])+q.get('answer_source_refs',[]):
            if r not in valid: errors.append('unresolved question ref '+r)
if count<9: errors.append('Unit I staged textbook-question release must contain at least Problems 2.4 (9 questions)')
if errors:
    print('MAC KB VERIFY: FAIL'); [print(' -',e) for e in errors]; sys.exit(1)
print('MAC KB VERIFY: PASS')
print(' - Units I–II source-backed and ready')
print(f' - {len(supporting)} supporting Unit II/order-preservation topics allowed alongside 43 R25 core topics')
print(f' - {count} Unit I textbook practice items currently published (Unit II questions deferred)')
print(' - Units III–V remain explicit source gaps')
