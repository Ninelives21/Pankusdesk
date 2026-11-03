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
by_id={t['id']:t for t in topics}
for c in coverage:
    complete=all(by_id.get(tid,{}).get('sections') and
                 (c.get('unit') in (1,2) or by_id[tid].get('source_coverage')=='complete-theory')
                 for tid in c.get('topic_ids',[]))
    want='COVERED' if complete else 'SOURCE_GAP'
    if c.get('status')!=want: errors.append('coverage status mismatch: '+c.get('syllabus_atom','?'))
    if want=='SOURCE_GAP' and not c.get('gap_reason'): errors.append('source gap has no explanation')
covered=sum(c.get('status')=='COVERED' for c in coverage)
gaps=sum(c.get('status')=='SOURCE_GAP' for c in coverage)
if status.get('source_gap_count')!=gaps: errors.append('source gap count differs from coverage audit')
if status.get('covered_topic_count')!=covered: errors.append('covered topic count differs from coverage audit')
if covered+gaps!=expected_atoms: errors.append('coverage states do not account for all atoms')
if status.get('ready_units')!=[1,2]: errors.append('ready units must be [1, 2]')
if status.get('supporting_topic_count')!=len(supporting): errors.append('supporting topic count mismatch')
qids=set(); counts={}
for unit_no in qbank.get('units',{}):
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

# Imported notebook/Text pages remain separate, source-resolved and anchored.
import hashlib
subject=json.loads((ROOT.parent/'subject.json').read_text())
if [u['number'] for u in subject['units'] if u['publicationStatus']=='ready']!=status['ready_units']:
    errors.append('ready units disagree with subject metadata')
if any(u['publicationStatus']!='draft' for u in subject['units'] if u['number'] in (3,4,5)):
    errors.append('new units require explicit draft status until all publication gates pass')
examples={}
for t in topics:
    for sec in t.get('sections',[]):
        for item in sec.get('accordions',[]):
            ident=item.get('id')
            if ident:
                if ident in examples: errors.append('duplicate example id '+ident)
                examples[ident]=item
            if t.get('unit') in (3,4):
                if not ident or not item.get('question_paragraphs') or not item.get('final_answer'):
                    errors.append('imported example lacks stable id/full question/final answer')
                parts=item.get('solution_parts',[])
                if not item.get('paragraphs') and not parts: errors.append('imported example has no working '+str(ident))
                for part in parts:
                    if not part.get('label') or not part.get('paragraphs'): errors.append('empty multipart solution '+str(ident))
if sum(k.startswith('tb-example-4-') for k in examples)!=21: errors.append('expected 21 complete Chapter 4 examples')
if sum(k.startswith('tb-example-5-') for k in examples)!=48: errors.append('expected 48 in-scope Chapter 5 examples')
undated=manifest.get('undated_class_sources',[])
if len(undated)!=15: errors.append('expected 15 imported undated lessons')
seen_captures=set()
for record in undated:
    path=ROOT.parent/record['entry']
    entry=json.loads(path.read_text())
    if entry.get('date') or entry.get('date_status')!='undated': errors.append('invented/misclassified class date')
    seen_captures.update(entry.get('source_captures',[]))
    for pg in entry.get('pages',[]):
        for block in pg.get('blocks',[]):
            for item in block.get('items',[]):
                match=item.get('textbook_match',{})
                if match.get('status') not in ('exact','near','none'): errors.append('unreviewed class question')
                href=match.get('href','')
                if match.get('status') in ('exact','near'):
                    anchor=href.partition('#')[2]
                    if not anchor or anchor not in ids|set(examples)|{'question-'+q for q in qids}:
                        errors.append('class textbook link has no canonical target: '+href)
                if match.get('status')=='exact' and (item.get('solution_mode')!='textbook-link' or item.get('paragraphs')):
                    errors.append('exact class match duplicates its canonical solution')
if seen_captures!=set(range(26,74)): errors.append('notebook capture coverage mismatch')
source_captures=json.loads((ROOT/'audits/mac-source-captures.json').read_text())
if {x['capture_number'] for x in source_captures}!=set(range(26,148)):
    errors.append('source capture ledger must account for all 122 supplied images')
for cap in source_captures:
    if not cap.get('sha256') or not cap.get('archive') or not cap.get('image_file'): errors.append('incomplete capture provenance')
figures=json.loads((ROOT/'audits/mac-ros-figures.json').read_text())
if len(figures)!=14: errors.append('expected 14 audited ROS crops')
for fig in figures:
    path=ROOT.parent/fig['output']
    if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=fig['output_sha256']:
        errors.append('ROS output missing or changed: '+fig['id'])
    if fig.get('pixel_comparison')!='identical to original crop' or len(fig.get('crop_xyxy',[]))!=4:
        errors.append('ROS fidelity record missing: '+fig['id'])
if errors:
    print('MAC KB VERIFY: FAIL'); [print(' -',e) for e in errors]; sys.exit(1)
print('MAC KB VERIFY: PASS')
print(' - Units I–II source-backed and ready')
print(f' - {len(supporting)} supporting Unit II/order-preservation topics allowed alongside 43 R25 core topics')
print(f' - {counts.get("1",0)} Unit I textbook practice items published')
print(f' - {counts.get("2",0)} Unit II textbook practice items published with class-match links')
print(f' - {covered} source-backed theory atoms; {gaps} explicit full/partial source gaps')
print(' - Units III–V remain draft; selected III–IV practice is explicitly partial')
