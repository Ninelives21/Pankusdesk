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
qids=set(); counts={}
for unit_no in ('1','2'):
    unit=qbank.get('units',{}).get(unit_no,{})
    count=0
    for g in unit.get('groups',[]):
        if not g.get('id'): errors.append(f'Unit {unit_no} question group missing id')
        for q in g.get('questions',[]):
            count+=1
            if q['id'] in qids: errors.append('duplicate question '+q['id'])
            qids.add(q['id'])
            if q.get('topic_id') not in ids: errors.append('unknown question topic '+str(q.get('topic_id')))
            for r in q.get('question_source_refs',[])+q.get('answer_source_refs',[]):
                if r not in valid: errors.append('unresolved question ref '+r)
            if unit_no == '2':
                for p in q.get('question_parts',[]):
                    if not p.get('id'): errors.append('multipart Unit II question part missing stable id '+q['id']+' '+str(p.get('label')))
    counts[unit_no]=count
if counts.get('1',0)<9: errors.append('Unit I staged textbook-question release must contain at least Problems 2.4 (9 questions)')
if counts.get('2')!=70: errors.append(f'Unit II textbook-question count must be 70, found {counts.get("2",0)}')

# Unit II worked examples must have stable deep-link ids.
for t in topics:
    if t.get('unit')!=2: continue
    for sec in t.get('sections',[]):
        for item in sec.get('accordions',[]):
            if str(item.get('title','')).startswith('Example 2.') and not item.get('id'):
                errors.append('Unit II textbook worked example missing stable id: '+str(item.get('title')))

# Class-question textbook-match gate for Unit II supplied class notes.
for class_source in manifest.get('class_sources',[]):
    if class_source.get('unit')!=2: continue
    entry_path=ROOT.parent/class_source.get('entry','')
    if not entry_path.exists():
        errors.append('missing Unit II class entry '+str(entry_path)); continue
    entry=json.loads(entry_path.read_text())
    for pg in entry.get('pages',[]):
        for block in pg.get('blocks',[]):
            if block.get('type')!='accordions': continue
            for item in block.get('items',[]):
                if not (item.get('question_paragraphs') or str(item.get('title','')).lower().startswith('example')): continue
                match=item.get('textbook_match')
                if not isinstance(match,dict) or match.get('status') not in ('exact','near','none'):
                    errors.append(f'class question lacks textbook-match audit {entry.get("date")} {item.get("title")}')
                if isinstance(match,dict) and match.get('status') in ('exact','near') and not match.get('href'):
                    errors.append(f'class textbook match lacks href {entry.get("date")} {item.get("title")}')
                if item.get('solution_mode')=='textbook-link' and item.get('paragraphs'):
                    errors.append(f'link-only class question still duplicates solution {entry.get("date")} {item.get("title")}')
if errors:
    print('MAC KB VERIFY: FAIL'); [print(' -',e) for e in errors]; sys.exit(1)
print('MAC KB VERIFY: PASS')
print(' - Units I–II source-backed and ready')
print(f' - {len(supporting)} supporting Unit II/order-preservation topics allowed alongside 43 R25 core topics')
print(f' - {counts.get("1",0)} Unit I textbook practice items published')
print(f' - {counts.get("2",0)} Unit II textbook practice items published with class-match links')
print(' - Units III–V remain explicit source gaps')
