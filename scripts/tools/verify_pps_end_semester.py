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


def verify(source_text=None, kb_root=None, source_root=None):
    bank = json.loads((SUBJECT / 'exam-prep/end-semester.json').read_text())
    paper = bank['paper']
    assert (paper['regulation'], paper['subject_code'], paper['minutes'], paper['max_marks']) == (
        'R25', '25ES1CS101', 180, 60)
    assert bank['sources'][0]['sha256'] == '1928b6abafcffcd0fa18fd88d570e6fc31847e888d54d6542c27981d7beba704'
    assert bank['sources'][0]['printed_exam'] == 'January 2026'
    questions = [q for section in bank['sections'] for q in section['questions']]
    ids = [q['id'] for q in questions]
    assert len(ids) == len(set(ids)) == 19
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
    # Preserve the existing R25 gates, then check the complete added papers.
    new_questions = [q for p in bank['papers'] for g in p['groups'] for q in g['parts']]
    assert [len([q for g in p['groups'] for q in g['parts']]) for p in bank['papers']] == [24, 25]
    assert bank['navigation_mode'] == 'papers-only'
    assert [p['id'] for p in bank['papers']] == ['endsem-2025', 'endsem-2024']
    assert len(set(ids + [q['id'] for q in new_questions])) == 68
    for p in bank['papers']:
        assert p['regulation'] == 'R22' and p['subject_code'] == '22ES1CS101'
        assert p['minutes'] == 180 and p['max_marks'] == 60
        assert sum(q['marks'] for q in p['groups'][0]['parts']) == 10
        assert len(p['groups']) == 11
        assert sum(bool(g.get('or_before')) for g in p['groups']) == 5
        for i in range(1, 11):
            g = p['groups'][i]
            assert sum(q['marks'] for q in g['parts']) == 10
            assert bool(g.get('or_before')) == (i % 2 == 0)
            assert g['unit'] == ['I', 'II', 'III', 'IV', 'V'][(i - 1) // 2]
        for g in p['groups']:
            for q in g['parts']:
                assert q['page'] in [1, 2]
                q = dict(q, source_label='Verified paper source')
                questions.append(q)
    assert {q['answer'] for q in questions} == set(bank['answers'])
    program_ids = set()
    snippet_ids = set()
    for q in questions:
        answer = bank['answers'][q['answer']]
        assert q['page'] in [1, 2] and q['source_label']
        if q['id'] in ids:
            assert q['page'] == 1 and q['nav_label']
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
    # These source-specific checks protect reviewed notebook details, not just
    # equivalent C semantics. The original photographs still require human review.
    answers = bank['answers']
    nested, ladder = answers['endsem-2026-a']['blocks']
    assert nested['blocks'][1]['code'].count('if (condition)') == 3
    assert nested['blocks'][1]['code'].count('else {') == 3
    assert ladder['blocks'][0]['text'] == 'Multi-way decision-making statement.'
    assert ladder['blocks'][1]['code'].count('else if') == 2
    array_code = '\n'.join(x['code'] for x in blocks_in(answers['endsem-2026-3']['blocks']) if x['type'] == 'code')
    assert 'int m[5] = {20, 10, 5, 40, 35};' in array_code
    assert '{10, 20, 1}, {5, 6, 13}, {15, 4, 8}' in array_code
    assert 'a[i][j]' in array_code
    categories = answers['endsem-2026-5-b']['blocks'][:4]
    assert [x['blocks'][0]['code'].split('{')[0].strip() for x in categories] == [
        'int sum(int x, int y)', 'void sum(int n, int y)', 'void sum(void)', 'int sum(void)']
    assert bank['snippet_fixtures']['conversion-implicit']['expected'] == '3\n'
    assert 'float f = 3.5f;' in bank['snippet_fixtures']['conversion-implicit']['displayed_code']
    assert 'fun(&x)' in bank['programs']['indirection']['code']
    assert '*y = *y * 10;' in bank['programs']['indirection']['code']
    assert all('source_fidelity' in a for a in answers.values())
    if source_text:
        original = re.sub(r'\s+', '', Path(source_text).read_text())
        assert all(re.sub(r'\s+', '', q['question']) in original for q in questions if q['id'] in ids)
        assert '#include' in original and '#define' in original
        print('PASS: all 19 question wordings match the supplied paper text.')
    if source_root:
        folder = Path(source_root)
        for p in bank['papers']:
            # Compare the two different typesettings independently; ignore only
            # whitespace, page furniture and assessment columns interrupting text.
            source = next(s for s in bank['sources'] if s['id'] == p['sources'][0])
            file = next(folder.glob(source['sha256'][:12] + '*.txt'))
            text = re.sub(r'--- PAGE \d+ ---|Page \d+ of \d+|\b\d+M\b|CO-\d+|BL-\d+', '', file.read_text())
            text = re.sub(r'\s+', '', text)
            for g in p['groups']:
                for q in g['parts']:
                    assert re.sub(r'\s+', '', q['question']) in text, (p['id'], q['number'])
            pdf = next(folder.glob(source['sha256'][:12] + '*.pdf'))
            import hashlib
            assert hashlib.sha256(pdf.read_bytes()).hexdigest() == source['sha256']
        print('PASS: all 49 added question wordings and original paper checksums match supplied sources.')
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
    print('PASS: three unique PPS papers, 68 question occurrences, 15 OR choices and paper-only navigation data.')

    extra = {
        'more-prime': [('1\n', 'Not prime\n'), ('2\n', 'Prime\n'), ('12\n', 'Not prime\n')],
        'more-linear': [('3\n8 8 1\n8\n', 'The element is found at 1 position\n'),
                        ('3\n8 8 1\n7\n', 'The element not found\n'), ('0\n', None)],
        'more-min-position': [('3\n5 -2 -2\n', 'Smallest: -2\nPosition: 2\n'),
                              ('1\n9\n', 'Smallest: 9\nPosition: 1\n'), ('0\n', None)],
        'more-insertion': [('5\n4 4 -1 0 -1\n', '-1 -1 0 4 4\n'), ('1\n9\n', '9\n')],
        'more-armstrong': [('0 9\n', '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'),
                           ('9474 9474\n', '9474\n'), ('500 100\n', None)],
        'more-upper': [('aZ 19!\n', 'AZ 19!\n')],
        'more-pointer-array': [('1\n-8\n', '-8\n'), ('31\n', None)],
        'more-dma': [('1\n-8\n', 'Sum: -8\n'), ('0\n', None)],
        'more-digit': [('0\n', 'Zero\n'), ('10\n', None)],
        'branch-if': [('0\n', 'simple if program\n'), ('-2\n', 'simple if program\n')],
        'branch-if-else': [('-3\n', '-3 is odd\n')],
        'branch-ladder': [('8 8 2\n', '8 is greatest\n'), ('2 8 8\n', '8 is greatest\n'),
                          ('8 8 8\n', '8 is greatest\n')],
        'branch-nested': [('9 2 3\n', '9 is the greatest\n'), ('2 9 3\n', '9 is the greatest\n'),
                          ('2 3 9\n', '9 is the greatest\n'), ('9 9 9\n', '9 is the greatest\n')],
        'branch-switch': [('8 2 1\n', 'The addition value is 10\n'),
                          ('8 2 2\n', 'The subtraction value is 6\n'),
                          ('8 2 3\n', 'The multiplication value is 16\n'),
                          ('8 2 4\n', 'The division value is 4\n'), ('8 0 4\n', None)],
        'loop-for': [('0\n', 'The factorial of 0 is 1\n'), ('21\n', None)],
        'indirection': [('-3\n', 'Value before calling function: -3\ny value is -30\nValue after calling function: -30\n'),
                        ('1001\n', None)],
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
            for name, expected in example.get('output_files', {}).items():
                assert (folder / name).read_text() == expected, (key, name)
            if key == 'more-cli-factorial':
                for arg, expected in [('0', '0! = 1\n'), ('21', None), ('oops', None)]:
                    result = subprocess.run([str(exe), arg], capture_output=True, text=True, timeout=5)
                    assert (result.returncode != 0 if expected is None else
                            result.returncode == 0 and result.stdout == expected)
            if key == 'more-copy':
                for args in [[], ['missing.txt', 'target2.txt'], ['source.txt', 'source.txt']]:
                    result = subprocess.run([str(exe)] + args, capture_output=True, cwd=folder, timeout=5)
                    assert result.returncode != 0
                assert (folder / 'source.txt').read_text() == example['files']['source.txt']
            if key == 'more-file-count':
                (folder / 'blank.txt').write_text('')
                result = subprocess.run([str(exe), 'blank.txt'], capture_output=True, text=True, cwd=folder, timeout=5)
                assert result.returncode == 0 and result.stdout == 'Words: 0\nWhitespace: 0\nTabs: 0\nSpaces: 0\n'
    print(f'PASS: {len(bank["programs"])} full C11 programs and {len(bank["snippet_fixtures"])} displayed-code fixtures compile warning-free; sample and boundary outputs match.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-text')
    parser.add_argument('--kb-root')
    parser.add_argument('--source-root')
    args = parser.parse_args()
    verify(args.source_text, args.kb_root, args.source_root)
