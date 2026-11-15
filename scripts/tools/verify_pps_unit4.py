"""Verify Unit 4 source selection, question coverage, provenance and displayed C programs."""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/programming-problem-solving'


def walk(blocks):
    for block in blocks:
        yield block
        if block['type'] == 'part':
            yield from walk(block['blocks'])


def verify(source_root=None, kb_root=None):
    bank = json.loads((SUBJECT / 'exam-prep/unit-4-question-bank.json').read_text())
    assert bank['navigation_mode'] == 'papers-only'
    assert [p['id'] for p in bank['papers']] == ['u4-important', 'u4-additional']
    groups = [g for p in bank['papers'] for g in p['groups']]
    assert [len(g['parts']) for g in groups] == [15, 10, 8, 8]
    questions = [q for g in groups for q in g['parts']]
    assert len(questions) == len({q['id'] for q in questions}) == 41
    assert {q['answer'] for q in questions} == set(bank['answers'])
    for g in groups:
        assert [q['number'] for q in g['parts']] == [str(i) for i in range(1, len(g['parts']) + 1)]
    for q in groups[0]['parts'] + groups[1]['parts']:
        assert q['marks'] == (3 if '-short-' in q['id'] else 8)
        assert q['companion_ref']['source'] == 'u4-answers'
        assert q['companion_ref']['number'] == int(q['number'])
        assert q['marks_basis']
    assert all('marks' not in q for g in groups[2:] for q in g['parts'])
    assert [(x['section'], x['short'], x['long']) for x in bank['scope']['exclusions']] == [
        ('Unit 3', 8, 7), ('Unit 5', 15, 7)]
    assert next(s for s in bank['sources'] if s['id'] == 'u4-bank')['printed_heading'] == 'UNIT-5 Question Bank'
    assert bank['scope']['companion_duplicate_questions'] == 25
    used = set()
    for a in bank['answers'].values():
        assert a['paragraphs'] and a['authority'] and a['source_fidelity']
        assert a['source_trace']['priority'] == 'Priyanka → senior KB → general PPS knowledge'
        if 'general' in a['basis']:
            assert a['source_trace']['general_supplement']
        for x in walk(a['blocks']):
            if x['type'] == 'program':
                used.add(x['id'])
            if x['type'] == 'table':
                assert all(len(row) == len(x['headers']) for row in x['rows'])
    assert used == set(bank['programs'])
    # Actual source defects, rather than stylistic rewrites.
    assert 'char s[3][20]' in bank['programs']['u4-pointer-strings']['code']
    assert 'int arr[2][3][2]' not in bank['programs']['u4-pointer-strings']['code']
    assert 'no universally best' in json.dumps(bank['answers']['structure-passing'])
    assert 'undefined behavior' in json.dumps(bank['answers']['pointer-analysis'])
    assert len(groups[3]['parts'][-1]['question_parts']) == 2
    assert 'printf(“%d”,c);' in groups[3]['parts'][-1]['question_parts'][1]['code']
    card = next(c for c in json.loads((SUBJECT / 'index-resources.json').read_text())['questions']
                if c.get('id') == 'unit-4-question-bank')
    assert (SUBJECT / card['href']).is_file()
    assert sum(c.get('id') == 'unit-4-question-bank' for c in json.loads((SUBJECT / 'index-resources.json').read_text())['questions']) == 1
    if source_root:
        texts = {}
        for s in bank['sources']:
            p = next(Path(source_root).glob(s['sha256'][:12] + '*.pdf'))
            assert hashlib.sha256(p.read_bytes()).hexdigest() == s['sha256']
            texts[s['id']] = p.with_suffix('.txt').read_text()
        mixed = texts['u4-mixed']
        selected = mixed.split('UNIT- 4', 1)[1].split('UNIT- 5', 1)[0]
        compact = lambda text: re.sub(r'\s+', '', text)
        for g in groups[:2]:
            for q in g['parts']:
                assert compact(q['question']) in compact(selected), q['id']
        for g in groups[2:]:
            for q in g['parts']:
                assert compact(q['question']) in compact(texts['u4-bank']), q['id']
        assert '3 Marks' in texts['u4-answers'] and '8 Marks Each' in texts['u4-answers']
        assert compact(groups[-1]['parts'][-1]['question_parts'][1]['code']) in compact(texts['u4-bank'])
        print('PASS: all41 question wordings, mixed-unit selection, companion marks and source checksums.')
    if kb_root:
        folder = Path(kb_root)
        pri = {x['id']: x for x in json.loads((folder / 'priyanka/topics.json').read_text())['topics']}
        senior = {x['id']: x for x in json.loads((folder / 'kb.json').read_text())['topics']}
        for a in bank['answers'].values():
            t = a['source_trace']
            assert set(t['priyanka_topic_ids']) <= set(pri)
            assert set(t['senior_topic_ids']) <= set(senior)
            pages = {p for id in t['priyanka_topic_ids'] for p in pri[id]['images']}
            spages = {p for id in t['senior_topic_ids'] for p in senior[id]['pages']}
            assert set(a['note_refs']) <= (pages if a['basis'].startswith('priyanka') else spages)
            assert set(a.get('senior_pages', [])) <= spages
        print('PASS: every primary note image/topic and senior page reference resolves.')
    extra = {
        'u4-five-students': [('1 A City 101 0 0\n', None)],
        'u4-structure-pointer': [('7 sita\n', 'Roll: 7\nName: sita\n')],
        'extra-students': [('0 3\n', None)],
    }
    for key, p in bank['programs'].items():
        with tempfile.TemporaryDirectory() as tmp:
            source, exe = Path(tmp) / 'example.c', Path(tmp) / 'example'
            source.write_text(p['code'])
            result = subprocess.run(['cc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-pedantic',
                                     str(source), '-o', str(exe)], capture_output=True, text=True)
            assert result.returncode == 0, (key, result.stderr)
            for data, expected in [(p['input'], p['expected'])] + extra.get(key, []):
                r = subprocess.run([str(exe)], input=data, capture_output=True, text=True, timeout=5)
                assert (r.returncode != 0 if expected is None else
                        r.returncode == 0 and r.stdout == expected), (key, r.stdout, expected, r.stderr)
    print(f'PASS: 41 dropdowns,2 navigation sets,source priority and {len(bank["programs"])} warning-free C11 programs with matching output.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root')
    p.add_argument('--kb-root')
    args = p.parse_args()
    verify(args.source_root, args.kb_root)
