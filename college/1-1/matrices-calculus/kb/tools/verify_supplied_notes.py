#!/usr/bin/env python3
"""Check source-packet provenance, schema, links and preserved source-error lines."""
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[5]
SUBJECT = ROOT / 'college/1-1/matrices-calculus'
entry_path = SUBJECT / 'kb/supplied-notes/unit-4.json'
entry = json.loads(entry_path.read_text())
manifest = json.loads((SUBJECT / 'kb/supplied-notes/manifest.json').read_text())
schema = json.loads((ROOT / 'college/schemas/undated-class-notes.schema.json').read_text())
jsonschema.Draft202012Validator(schema).validate(entry)
source = manifest['sources'][0]
assert entry['source_id'] == source['id']
assert source['sha256'] == entry['source']['sha256']
assert source['page_count'] == entry['source']['page_count'] == 66
assert source['bytes'] == entry['source']['bytes'] == 16665505
assert 'date' not in entry, 'Do not invent a calendar date for the supplied packet'
assert (entry_path.parent / source['entry']).resolve() == entry_path.resolve()

ids = []
items = {}
covered = set()
mismatch_count = 0
for section in entry['pages']:
    ids.append(section['id'])
    covered.update(section['source_pages'])
    for block in section['blocks']:
        if block.get('id'):
            ids.append(block['id'])
        mismatch_count += bool(block.get('math_mismatch'))
        for item in block.get('items', []):
            ids.append(item['id'])
            items[item['id']] = item
            assert set(item['source_pages']) <= set(section['source_pages'])
            assert item['question_paragraphs'], 'Keep each complete question visible'
            mismatch_count += bool(item.get('math_mismatch'))
            for index in item.get('source_result_indices', []):
                assert 0 <= index < len(item['paragraphs'])
            if not item['paragraphs']:
                assert item.get('source_note'), 'Label source-only questions honestly'
assert covered == set(range(1, 67))
assert len(ids) == len(set(ids)), 'Source index anchors must be unique'
assert len(entry['pages']) == 7 and len(items) == 55 and mismatch_count == 28

topics = json.loads((SUBJECT / 'kb/data/topics.json').read_text())
topic_ids = {topic['id'] for topic in topics['topics']} if isinstance(topics, dict) else {topic['id'] for topic in topics}
for mapping in entry['mapped_topics']:
    assert mapping['topic_id'] in topic_ids
    assert (ROOT / mapping['href'].split('#')[0]).is_file()

# These intentionally wrong source lines must not be silently replaced by corrections.
inverse = '\n'.join(items['pd-inverse-tangent']['paragraphs'])
assert r'\dfrac{-1}{x^2+y^2}' in inverse
assert r'\dfrac{-2y^2}{(x^2+y^2)^2}' in inverse
last_box = items['box-general-volume']
assert last_box['paragraphs'][-1] == r'\[z=(k)^{1/3}\]'
assert last_box.get('math_mismatch')
assert items['third-partial-exponential']['paragraphs'][-1] == r'\[=\]'
assert items['taylor-square-root']['paragraphs'][-1] == r'\[f_{yy}(1,0)=\]'
assert not items['lagrange-fixed-product-exercise']['paragraphs']

serialized = json.dumps(entry, ensure_ascii=False)
assert r'\\frac' not in serialized, 'Use the shared dfrac typography convention'
assert not any(ord(ch) < 32 and ch not in '\n\r\t' for ch in serialized)
index = json.loads((SUBJECT / 'index-resources.json').read_text())
assert index['noteUnitCards'] and index['notes'][0]['href'] == 'unit-4-supplied-notes.html'
assert (SUBJECT / index['notes'][0]['href']).is_file()
print('MAC SUPPLIED NOTES VERIFY: PASS')
print(' - JSON schema, source manifest and existing topic links')
print(' - all 66 PDF pages, 7 sections, 55 questions/examples, 28 amber checks')
print(' - unique index anchors and source-only/unfinished working preserved')
print(' - original inverse-tangent and final box-error lines remain unchanged')
