#!/usr/bin/env python3
"""Check WS 1 source integrity and the complete, section-numbered question inventory."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / 'college/1-1/matrices-calculus/worksheets'
EXPECTED = {1: [10, 5, 5, 4, 8, 6, 6], 2: [10, 14],
            3: [10, 10, 12, 6, 6, 8], 4: [10, 6, 18, 6, 20, 7],
            5: [10, 9, 5, 13, 5, 10, 7, 14, 4, 8]}
SOURCE_SHA = 'ad5bfc80fcb54ac48318d7c9b8c680e5b7bb65462f232e24d002d9938172d044'

def verify():
    data = json.loads((FOLDER / 'ws-1.json').read_text())
    assert data['id'] == 'ws-1' and data['label'] == 'WS 1'
    assert hashlib.sha256((FOLDER / data['source']['href']).read_bytes()).hexdigest() == SOURCE_SHA
    assert data['source']['sha256'] == SOURCE_SHA
    ids = set()
    for unit, counts in EXPECTED.items():
        groups = [group for group in data['groups'] if group['unit'] == unit]
        assert [len(group['questions']) for group in groups] == counts, f'Unit {unit}: omitted/extra question set'
        for group in groups:
            assert group['id'] not in ids
            ids.add(group['id'])
            assert group['source_pages'] and all(1 <= page <= 15 for page in group['source_pages'])
            assert [q['number'] for q in group['questions']] == list(range(1, len(group['questions']) + 1))
            for question in group['questions']:
                assert question['id'] not in ids
                ids.add(question['id'])
                for key in ['question_paragraphs', 'paragraphs']:
                    assert question[key] and all(isinstance(p, str) and p.strip() for p in question[key])
                assert question['final_answer'].strip()
    assert len(data['groups']) == sum(len(counts) for counts in EXPECTED.values())
    index = json.loads((FOLDER / 'index.json').read_text())
    assert any(item['id'] == 'ws-1' and item['href'] == 'ws-1.json' for item in index['worksheets'])
    audit = json.loads((ROOT / 'college/1-1/matrices-calculus/kb/audits/worksheet-1-solution-audit.json').read_text())
    questions = {q['id']: q for g in data['groups'] for q in g['questions']}
    assert audit['source_pdf_sha256'] == SOURCE_SHA
    assert len(audit['records']) == len(questions)
    assert {r['id'] for r in audit['records']} == set(questions)
    for record in audit['records']:
        payload = json.dumps(questions[record['id']], ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(payload).hexdigest() == record['question_sha256'], 'Solution changed after audit: ' + record['id']
        assert record['source_transcription_reviewed'] and record['independent_method']
    print('Full audit coverage and reviewed-answer hashes: PASS')
    print('MAC WORKSHEET VERIFY: PASS — 272 entries, original section numbering, unique anchors, unchanged source PDF')

if __name__ == '__main__':
    verify()
