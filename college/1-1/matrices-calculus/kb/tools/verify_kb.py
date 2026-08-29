#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parents[1]
D = ROOT / 'data'
errors = []
manifest = json.loads((D/'source-manifest.json').read_text(encoding='utf-8'))
syllabus = json.loads((D/'syllabus.json').read_text(encoding='utf-8'))
coverage = json.loads((D/'coverage-audit.json').read_text(encoding='utf-8'))
topics = json.loads((D/'topics.json').read_text(encoding='utf-8'))
status = json.loads((D/'kb-status.json').read_text(encoding='utf-8'))
expected_atoms = 43
if manifest['course']['code'] != '25BS1MT101': errors.append('course code changed')
if len(syllabus.get('units', [])) != 5: errors.append('R25 unit count != 5')
if len(coverage) != expected_atoms: errors.append(f'coverage atom count != {expected_atoms}')
if len(topics) != expected_atoms: errors.append(f'topic count != {expected_atoms}')
valid_refs = {x['source_id'] for x in manifest.get('syllabus_refs', [])}
ids = set()
for t in topics:
    if t['id'] in ids: errors.append('duplicate topic id '+t['id'])
    ids.add(t['id'])
    if not t.get('source_refs'): errors.append('topic has no source refs '+t['id'])
    bad = [r for r in t.get('source_refs', []) if r not in valid_refs]
    if bad: errors.append('unresolved source refs '+t['id']+': '+','.join(bad))
for c in coverage:
    if c.get('status') != 'SOURCE_GAP': errors.append('initial scaffold coverage must remain SOURCE_GAP: '+c.get('syllabus_atom','?'))
    if not c.get('source_refs'): errors.append('coverage row has no source refs: '+c.get('syllabus_atom','?'))
if status.get('r25_atom_count') != expected_atoms: errors.append('kb-status R25 atom count mismatch')
if status.get('source_gap_count') != expected_atoms: errors.append('kb-status source gap count mismatch')
if status.get('gap_filled_topic_ids') != []: errors.append('unexpected gap-filled topic in initial scaffold')
if errors:
    print('MAC KB VERIFY: FAIL')
    for e in errors: print(' -', e)
    sys.exit(1)
print('MAC KB VERIFY: PASS')
print(f' - 5 official R25 units mapped')
print(f' - {expected_atoms} syllabus atoms have stable topic IDs')
print(f' - {expected_atoms} detailed-theory source gaps remain explicit')
print(' - no unsupported gap filling introduced')
