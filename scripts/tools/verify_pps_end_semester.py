"""Validate R25 end-semester identity/marks/source coverage and run its C examples."""
import argparse
import re
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/programming-problem-solving'


def blocks_in(blocks):
    for block in blocks:
        yield block
        if block['type'] == 'part':
            yield from blocks_in(block['blocks'])


def verify(source_text=None, kb_root=None):
    bank = json.loads((SUBJECT / 'exam-prep/end-semester.json').read_text())
    paper = bank['paper']
    assert (paper['regulation'], paper['subject_code'], paper['minutes'], paper['max_marks']) == (
        'R25', '25ES1CS101', 180, 60)
    assert bank['sources'][0]['sha256'] == '1928b6abafcffcd0fa18fd88d570e6fc31847e888d54d6542c27981d7beba704'
    assert bank['sources'][0]['printed_exam'] == 'January 2026'
    questions = [q for section in bank['sections'] for q in section['questions']]
    ids = [q['id'] for q in questions]
    assert len(ids) == len(set(ids)) == len(bank['answers']) == 19
    assert sum(q['marks'] for q in bank['sections'][0]['questions']) == 10
    assert [q['number'] for q in questions] == [
        'a', 'b', 'c', 'd', 'e', '1(a)', '1(b)', '2', '3', '4',
        '5(a)', '5(b)', '6', '7(a)', '7(b)', '8', '9(a)', '9(b)', '10']
    lookup = {q['id']: q for q in questions}
    assert sum(q.get('or_before', False) for q in questions) == 5
    for choice in paper['choices']:
        assert len(choice['alternatives']) == 2
        for option in choice['alternatives']:
            assert all(lookup[id]['unit'] == choice['unit'] for id in option)
            assert sum(lookup[id]['marks'] for id in option) == 10
        assert lookup[choice['alternatives'][1][0]]['or_before']
    program_ids = set()
    snippet_ids = set()
    for q in questions:
        answer = bank['answers'][q['answer']]
        assert q['page'] == 1 and q['nav_label'] and q['source_label']
        assert answer['paragraphs'] and answer['blocks'] and answer['authority']
        assert answer['source_trace']['priority'] == 'Priyanka → senior KB → general PPS knowledge'
        if answer['basis'] == 'general' or 'general' in answer['basis']:
            assert answer['source_trace'].get('general_supplement')
        for block in blocks_in(answer['blocks']):
            assert block['type'] in {'paragraph', 'heading', 'code', 'list', 'table', 'part', 'program'}
            if block['type'] == 'program':
                assert block['id'] in bank['programs']
                program_ids.add(block['id'])
            elif block['type'] == 'table':
                assert all(len(row) == len(block['headers']) for row in block['rows'])
        for fixture_id in answer.get('snippet_tests', []):
            snippet_ids.add(fixture_id)
            fixture = bank['snippet_fixtures'][fixture_id]
            displayed = fixture['displayed_code']
            if isinstance(displayed, str):
                displayed = [displayed]
            code_blocks = [b['code'] for b in blocks_in(answer['blocks']) if b['type'] == 'code']
            assert all(code in code_blocks for code in displayed), fixture_id
    assert program_ids == set(bank['programs'])
    assert snippet_ids == set(bank['snippet_fixtures'])
    card = next(c for c in json.loads((SUBJECT / 'index-resources.json').read_text())['questions']
                if c.get('id') == 'end-semester-papers')
    assert (SUBJECT / card['href']).is_file()
    # Explicit source-priority regressions: do not call these familiar topics note gaps.
    assert bank['answers']['endsem-2026-c']['note_refs'] == [70, 71, 72]
    assert bank['answers']['endsem-2026-9-a']['source_trace']['priyanka_topic_ids']
    assert bank['answers']['endsem-2026-8']['source_trace']['priyanka_topic_ids'] == ['pri-structures-function-values']
    assert bank['answers']['endsem-2026-6']['source_trace']['general_supplement']
    if source_text:
        original = re.sub(r'\s+', '', Path(source_text).read_text())
        assert all(re.sub(r'\s+', '', q['question']) in original for q in questions)
        assert '#include' in original and '#define' in original
        print('PASS: all 19 question wordings match the supplied paper text.')
    if kb_root:
        folder = Path(kb_root)
        pri = {t['id']: t for t in json.loads((folder / 'priyanka/topics.json').read_text())['topics']}
        senior = {t['id']: t for t in json.loads((folder / 'kb.json').read_text())['topics']}
        problems = {t['id']: t for t in json.loads((folder / 'priyanka/problems.json').read_text())['problems']}
        for answer in bank['answers'].values():
            trace = answer['source_trace']
            assert set(trace['priyanka_topic_ids']) <= set(pri)
            assert set(trace['senior_topic_ids']) <= set(senior)
            assert set(trace.get('priyanka_problem_ids', [])) <= set(problems)
            primary_images = {image for id in trace['priyanka_topic_ids'] for image in pri[id]['images']}
            primary_images.update(image for id in trace.get('priyanka_problem_ids', []) for image in problems[id]['images'])
            senior_pages = {page for id in trace['senior_topic_ids'] for page in senior[id]['pages']}
            if answer['basis'].startswith('priyanka'):
                assert set(answer['note_refs']) <= primary_images
                assert set(answer.get('senior_pages', [])) <= senior_pages
            elif answer['basis'].startswith('senior'):
                assert set(answer['note_refs']) <= senior_pages
        print('PASS: every cited primary topic, image, senior page and source prompt resolves to the ingested KB.')
    print('PASS: January 2026 PPS/R25 identity, 19 answers, exact numbering, 60-mark choice scheme, OR placement, source traces and card.')

    extra = {
        'swap': [('0 0\n', 'Before: 0 0\nAfter: 0 0\n'),
                 ('-5 8\n', 'Before: -5 8\nAfter: 8 -5\n'), ('3\n', None)],
        'selection-sort': [('1\n7\n', '7\n'), ('5\n4 4 -1 0 -1\n', '-1 -1 0 4 4\n'),
                           ('5\n1 2 3 4 5\n', '1 2 3 4 5\n'), ('0\n', None), ('101\n', None)],
        'time-seconds': [('0 0 0\n', 'By value: 0\nBy pointer: 0\n'),
                         ('100000 59 59\n', 'By value: 360003599\nBy pointer: 360003599\n'),
                         ('-1 2 3\n', None), ('1 60 0\n', None), ('1 0 60\n', None)],
        'display-file': [('missing.txt\n', None), ('file with spaces.txt\n', 'Spaces work.\n'),
                         ('empty.txt\n', '')],
    }
    for key, example in {**bank['programs'], **bank['snippet_fixtures']}.items():
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            source, exe = folder / 'example.c', folder / 'example'
            source.write_text(example['code'])
            compiled = subprocess.run(['cc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-pedantic',
                                       str(source), '-o', str(exe)], capture_output=True, text=True)
            assert compiled.returncode == 0, (key, compiled.stderr)
            for name, contents in example.get('files', {}).items():
                (folder / name).write_text(contents)
            (folder / 'file with spaces.txt').write_text('Spaces work.\n')
            (folder / 'empty.txt').write_text('')
            for sample, expected in [(example['input'], example['expected'])] + extra.get(key, []):
                result = subprocess.run([str(exe)] + example.get('args', []), input=sample,
                                        capture_output=True, text=True, cwd=folder, timeout=5)
                if expected is None:
                    assert result.returncode != 0, (key, sample, 'invalid input accepted')
                else:
                    assert result.returncode == 0 and result.stdout == expected, (
                        key, sample, result.returncode, result.stdout, expected, result.stderr)
            if key == 'cli':
                result = subprocess.run([str(exe)], capture_output=True, cwd=folder, timeout=5)
                assert result.returncode != 0
    print(f'PASS: {len(bank["programs"])} full C11 programs and {len(bank["snippet_fixtures"])} displayed-code fixtures compile warning-free; sample and boundary outputs match.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-text')
    parser.add_argument('--kb-root')
    args = parser.parse_args()
    verify(args.source_text, args.kb_root)
