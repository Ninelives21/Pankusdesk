"""Check Unit 3 source selection, card order, provenance, traces and executable C examples."""
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
    bank = json.loads((SUBJECT / 'exam-prep/unit-3-question-bank.json').read_text())
    assert bank['navigation_mode'] == 'papers-only'
    assert [p['id'] for p in bank['papers']] == ['u3-part1', 'u3-part2', 'u3-important']
    assert [len(g['parts']) for p in bank['papers'] for g in p['groups']] == [2, 5, 8, 6, 8, 7]
    questions = [q for p in bank['papers'] for g in p['groups'] for q in g['parts']]
    assert len(questions) == len({q['id'] for q in questions}) == 36
    assert {q['answer'] for q in questions} == set(bank['answers'])
    assert all('marks' not in q for q in questions)
    for p in bank['papers']:
        assert p['entry_kind'] == 'question-bank'
        for g in p['groups']:
            assert [q['number'] for q in g['parts']] == list(map(str, range(1, len(g['parts']) + 1)))
    cards = json.loads((SUBJECT / 'index-resources.json').read_text())['questions']
    ids = [c.get('id') for c in cards]
    assert ids.count('unit-3-question-bank') == 1
    assert ids.index('unit-3-question-bank') + 1 == ids.index('unit-4-question-bank')
    assert (SUBJECT / next(c['href'] for c in cards if c.get('id') == 'unit-3-question-bank')).is_file()
    used, tested = set(), set()
    for a in bank['answers'].values():
        assert a['paragraphs'] and a['authority'] and a['source_fidelity']
        assert a['source_trace']['priority'] == 'Priyanka → senior KB → general PPS knowledge'
        if 'general' in a['basis']:
            assert a['source_trace']['general_supplement']
        codes = []
        for block in walk(a['blocks']):
            if block['type'] == 'program':
                used.add(block['id'])
            if block['type'] == 'code':
                codes.append(block['code'])
            if block['type'] == 'table':
                assert all(len(row) == len(block['headers']) for row in block['rows'])
        for id in a.get('snippet_tests', []):
            tested.add(id)
            display = bank['snippet_fixtures'][id]['displayed_code']
            assert all(c in codes for c in ([display] if isinstance(display, str) else display))
    assert used == set(bank['programs']) and tested == set(bank['snippet_fixtures'])
    assert len(bank['answers']['recursive-tasks']['blocks']) == 4
    assert 'Factorial/ Akerman' in next(q['question'] for q in questions if q['answer'] == 'recursive-tasks')
    assert 'return ack(m - 1, ack(m, n - 1));' in bank['programs']['u3-ackermann']['code']
    assert 'return gcd(b, a % b);' in bank['programs']['u3-recursive-gcd']['code']
    assert 'multiply(a, b, c);' in bank['programs']['u3-matrix-functions']['code']
    assert 'sort(a, n);' in bank['programs']['u3-bubble']['code']
    assert bank['answers']['binary-algorithm']['source_fidelity']['corrections']
    assert bank['answers']['selection-complexity']['source_trace']['general_supplement']
    if source_root:
        texts = {}
        for src in bank['sources']:
            pdf = next(Path(source_root).glob(src['sha256'][:12] + '*.pdf'))
            assert hashlib.sha256(pdf.read_bytes()).hexdigest() == src['sha256']
            texts[src['id']] = pdf.with_suffix('.txt').read_text()
        compact = lambda t: re.sub(r'\s+', '', t)
        texts['u3-mixed'] = texts['u3-mixed'].split('UNIT-3', 1)[1].split('UNIT- 4', 1)[0]
        for p in bank['papers']:
            text = compact(texts[p['sources'][0]])
            for g in p['groups']:
                for q in g['parts']:
                    assert compact(q['question']) in text, q['id']
        print('PASS: all36 question wordings/checksums and exclusive Unit 3 extraction match supplied sources.')
    if kb_root:
        folder = Path(kb_root)
        pri = {x['id']: x for x in json.loads((folder / 'priyanka/topics.json').read_text())['topics']}
        problems = {x['id']: x for x in json.loads((folder / 'priyanka/problems.json').read_text())['problems']}
        senior = {x['id']: x for x in json.loads((folder / 'kb.json').read_text())['topics']}
        for a in bank['answers'].values():
            trace = a['source_trace']
            assert set(trace['priyanka_topic_ids']) <= set(pri)
            assert set(trace['senior_topic_ids']) <= set(senior)
            pages = {p for id in trace['priyanka_topic_ids'] for p in pri[id]['images']}
            assert set(trace.get('priyanka_problem_ids', [])) <= set(problems)
            pages.update(p for id in trace.get('priyanka_problem_ids', []) for p in problems[id]['images'])
            spages = {p for id in trace['senior_topic_ids'] for p in senior[id]['pages']}
            assert set(a['note_refs']) <= (pages if a['basis'].startswith('priyanka') else spages)
            assert set(a.get('senior_pages', [])) <= spages
        print('PASS: primary topic/image and senior page references resolve to the ingested KB.')
    extra = {
        'extra-factorial-recursive': [('0\n', '0! = 1\n'), ('21\n', None)],
        'extra-fibonacci': [('0\n', ''), ('1\n', '0\n'), ('-1\n', None)],
        'extra-array-sum': [('1\n-8\n', 'Sum: -8\n'), ('0\n', None)],
        'u3-value-pointer': [('8 8\n', 'Before: 8 8\nAfter value: 8 8\nAfter pointer: 8 8\n')],
        'u3-ackermann': [('0 1\n', 'A(0,1) = 2\n'), ('1 1\n', 'A(1,1) = 3\n'),
                          ('3 6\n', 'A(3,6) = 509\n'), ('4 0\n', None)],
        'u3-recursive-gcd': [('0 8\n', 'GCD: 8\n'), ('0 0\n', None)],
        'u3-bubble': [('4\n4 -1 4 0\n', 'Before: 4 -1 4 0\nAfter: -1 0 4 4\n'), ('0\n', None)],
        'u3-insertion': [('4\n4 -1 4 0\n', '-1 0 4 4\n'), ('1\n7\n', '7\n')],
        'selection-sort': [('4\n4 -1 4 0\n', '-1 0 4 4\n')],
        'u3-matrix-functions': [('10 20 1 5 6 13 15 4 8\n1 1 1 1 1 1 1 1 1\n', '31 31 31\n24 24 24\n27 27 27\n')],
    }
    for key, example in {**bank['programs'], **bank['snippet_fixtures']}.items():
        with tempfile.TemporaryDirectory() as tmp:
            src, exe = Path(tmp) / 'example.c', Path(tmp) / 'example'
            src.write_text(example['code'])
            c = subprocess.run(['cc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-pedantic', str(src), '-o', str(exe)], capture_output=True, text=True)
            assert c.returncode == 0, (key, c.stderr)
            for data, expected in [(example['input'], example['expected'])] + extra.get(key, []):
                r = subprocess.run([str(exe)], input=data, capture_output=True, text=True, timeout=5)
                assert (r.returncode != 0 if expected is None else r.returncode == 0 and r.stdout == expected), (key, r.stdout, expected, r.stderr)
    print(f'PASS: card before Unit4,36 Q&As,3 set links,12 full C11 programs and4 displayed fixtures; samples/boundaries match.')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root')
    p.add_argument('--kb-root')
    args = p.parse_args()
    verify(args.source_root, args.kb_root)
