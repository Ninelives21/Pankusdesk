#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'data'
errors=[]
manifest=json.loads((D/'source-manifest.json').read_text())
coverage=json.loads((D/'coverage-audit.json').read_text())
lectures=json.loads((D/'lecture-index.json').read_text())
book=json.loads((D/'book-index.json').read_text())
topics=json.loads((D/'topics.json').read_text())

# Counts tied to the approved source corpus
if manifest['accounting']['textbook_capture_count_in_unit_zips'] != 214: errors.append('textbook capture count != 214')
if manifest['accounting']['lecture_transcript_count'] != 35: errors.append('lecture transcript count != 35')
if manifest['accounting']['supplementary_pdf_pages'] != 97: errors.append('supplementary PDF page count != 97')
# Unit-II lecture 08 must remain absent
u2nums=[x['lecture_number'] for x in lectures if x['unit']==2]
if u2nums != [1,2,3,4,5,6,7,9]: errors.append(f'Unit-II lecture numbers changed: {u2nums}')
# page 200 must have multiple captures; p243 must be indexed
by_page={x['printed_page']:x for x in book}
if 200 not in by_page or len(by_page[200]['captures']) < 2: errors.append('page 200 shared capture missing')
if 243 not in by_page: errors.append('page 243 missing')
# every syllabus atom covered, no empty source list
for c in coverage:
    if c['status']=='SOURCE_GAP': errors.append('source gap: '+c['syllabus_atom'])
    if not c['source_refs']: errors.append('no sources: '+c['syllabus_atom'])
# every source ref must resolve through one of the indexes/manifests
valid_refs=set(x['source_id'] for x in book)
valid_refs.update(x['source_id'] for x in lectures)
valid_refs.update(f"SUP-P{n:03d}" for n in range(1,98))
valid_refs.update(x['source_id'] for x in manifest.get('syllabus_refs',[]))
valid_refs.update(x['id'] for x in manifest.get('gap_sources',[]))
# every topic must have provenance
ids=set()
for t in topics:
    if t['id'] in ids: errors.append('duplicate topic id '+t['id'])
    ids.add(t['id'])
    if not t['source_refs']: errors.append('topic has no source refs '+t['id'])
    unresolved=[r for r in t['source_refs'] if r not in valid_refs]
    if unresolved: errors.append('unresolved source refs '+t['id']+': '+','.join(unresolved))
    # recursively validate claim/section-level provenance added to the rich KB
    def walk_refs(obj, path=''):
        if isinstance(obj, dict):
            if 'source_refs' in obj and isinstance(obj['source_refs'], list):
                bad=[r for r in obj['source_refs'] if r not in valid_refs]
                if bad: errors.append('unresolved nested source refs '+t['id']+path+': '+','.join(bad))
            for k,v in obj.items():
                if k != 'source_refs': walk_refs(v, path+'/'+str(k))
        elif isinstance(obj, list):
            for i,v in enumerate(obj): walk_refs(v, path+f'/{i}')
    walk_refs(t)
# explicit four gap topics must stay marked
required_gap={'u3-swinburne','u4-sync-impedance','u4-synchronous-motor','u5-elcb'}
actual_gap={t['id'] for t in topics if t['status']=='core-gap-filled'}
if actual_gap != required_gap: errors.append(f'gap-topic set changed: {sorted(actual_gap)}')

if errors:
    print('BEE KB VERIFY: FAIL')
    for e in errors: print(' -',e)
    sys.exit(1)
print('BEE KB VERIFY: PASS')
print(f" - {manifest['accounting']['textbook_capture_count_in_unit_zips']} textbook captures accounted")
print(f" - {manifest['accounting']['lecture_transcript_count']} lecture transcripts accounted")
print(f" - {len(coverage)} R25 syllabus atoms source-backed")
print(f" - {len(topics)} knowledge topics, all with provenance")
print(' - Unit-II lecture 08 remains explicitly absent')
print(' - 4 audited gap topics remain explicitly gap-filled')
