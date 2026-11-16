"""Check Unit 5 intake coverage, citations, C examples and real file results."""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/programming-problem-solving'


def blocks(items):
    for item in items:
        yield item
        if item['type'] == 'part':
            yield from blocks(item['blocks'])


def verify(source_root=None, kb_root=None):
    bank = json.loads((SUBJECT / 'exam-prep/unit-5-question-bank.json').read_text())
    assert bank['kind'] == 'authored-question-bank'
    assert bank['navigation_mode'] == 'papers-only'
    groups = [g for p in bank['papers'] for g in p['groups']]
    assert [len(g['parts']) for g in groups] == [15, 7, 4, 11, 7]
    questions = [q for g in groups for q in g['parts']]
    assert len(questions) == len({q['id'] for q in questions}) == 44
    assert {q['answer'] for q in questions} == set(bank['answers'])
    for i, group in enumerate(groups):
        assert [q['number'] for q in group['parts']] == [str(n) for n in range(1, len(group['parts']) + 1)]
        for q in group['parts']:
            if i < 2:
                assert q['marks'] == (2 if i == 0 else 8) and q['marks_basis']
            else:
                assert 'marks' not in q
    used = set()
    for answer in bank['answers'].values():
        trace = answer['source_trace']
        assert trace['priority'] == 'Priyanka → senior KB → general PPS knowledge'
        assert answer['paragraphs'] and answer['source_fidelity']
        if 'general' in answer['basis']:
            assert trace['general_supplement']
        for item in blocks(answer['blocks']):
            if item['type'] == 'program':
                used.add(item['id'])
            if item['type'] == 'table':
                assert all(len(row) == len(item['headers']) for row in item['rows'])
        assert set(answer.get('snippet_tests', [])) <= set(bank['snippet_fixtures'])
    assert used == set(bank['programs'])
    assert '16th byte' in json.dumps(bank['answers']['offsets'])
    assert 'not a mandatory character' in json.dumps(bank['answers']['text-binary'])
    assert len(groups[3]['parts'][4]['question_parts']) == 2
    cards = json.loads((SUBJECT / 'index-resources.json').read_text())['questions']
    ids = [c.get('id') for c in cards]
    assert ids.count('unit-5-question-bank') == 1
    assert ids[ids.index('unit-3-question-bank'):][:3] == [f'unit-{n}-question-bank' for n in (3, 4, 5)]
    assert (SUBJECT / 'unit-5-question-bank.html').is_file()
    if source_root:
        texts = {}
        for source in bank['sources']:
            path = next(Path(source_root).glob(source['sha256'][:12] + '*.pdf'))
            assert hashlib.sha256(path.read_bytes()).hexdigest() == source['sha256']
            texts[source['id']] = path.with_suffix('.txt').read_text()
        compact = lambda s: re.sub(r'\s+', '', s).replace('–', '-').replace('—', '-')
        for paper in bank['papers']:
            text = texts[paper['sources'][0]]
            for group in paper['groups']:
                for q in group['parts']:
                    assert compact(q['question']) in compact(text), q['id']
        assert '2 Marks' in texts['u5-answers'] and '8 Marks Each' in texts['u5-answers']
        print('PASS: 44 source wordings, source checksums and printed marks.')
    if kb_root:
        folder = Path(kb_root)
        pri = {t['id']: t for t in json.loads((folder / 'priyanka/topics.json').read_text())['topics']}
        sen = {t['id']: t for t in json.loads((folder / 'kb.json').read_text())['topics']}
        for answer in bank['answers'].values():
            trace = answer['source_trace']
            assert set(trace['priyanka_topic_ids']) <= set(pri)
            assert set(trace['senior_topic_ids']) <= set(sen)
            pages = {n for id in trace['priyanka_topic_ids'] for n in pri[id]['images']}
            spages = {n for id in trace['senior_topic_ids'] for n in sen[id]['pages']}
            assert set(answer['note_refs']) <= (pages if answer['basis'].startswith('priyanka') else spages)
        print('PASS: note citations resolve; general completion disclosed.')
    tests = {
        'u5-count': [('\n', [], {}, 0, 'Characters: 1\nLetters: 0\nDigits: 0\nSpecial symbols: 0\nWhitespace: 1\n'), ('', [], {}, 1, None)],
        'u5-cli': [('', [], {}, 0, 'Argument count: 1\n'), ('', ['one argument'], {}, 0, 'Argument count: 2\nArgument 1: one argument\n')],
        'u5-copy': [('', [], {'input.txt': ''}, 0, ''), ('', [], {}, 1, None)],
        'u5-errors': [('', ['absent.txt'], {}, 1, None), ('', ['empty.txt'], {'empty.txt': ''}, 0, 'EOF reached: 1\nAfter clearerr: 0\n')],
        'u5-inventory': [('1 Pen nan\n', [], {}, 1, None), ('bad\n', [], {}, 1, None)],
    }
    runs = 0
    for name, record in {**bank['programs'], **bank['snippet_fixtures']}.items():
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            source = folder / 'program.c'
            exe = folder / 'program'
            source.write_text(record['code'])
            subprocess.run(['cc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-pedantic', str(source), '-o', str(exe)], check=True, capture_output=True, text=True)
            cases = [(record.get('input', ''), record.get('args', []), record.get('files', {}), 0, record['expected'])] + tests.get(name, [])
            for index, (stdin, args, files, status, expected) in enumerate(cases):
                case = folder / str(index)
                case.mkdir()
                for filename, content in files.items():
                    (case / filename).write_text(content)
                result = subprocess.run([str(exe), *args], input=stdin, text=True, capture_output=True, cwd=case, timeout=5)
                assert result.returncode == status, (name, index, result.stderr)
                if expected is not None:
                    assert result.stdout == expected, (name, index, result.stdout, expected)
                if index == 0:
                    for filename, content in record.get('output_files', {}).items():
                        assert (case / filename).read_text() == content
                    if name == 'u5-binary':
                        import struct
                        assert (case / 'data.bin').read_bytes() == struct.pack('@i', 123)
                runs += 1
    print(f'PASS: {len(bank["programs"])} C11 programs, {len(bank["snippet_fixtures"])} snippets, {runs} runs including file contents and failure cases.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root')
    parser.add_argument('--kb-root')
    args = parser.parse_args()
    verify(args.source_root, args.kb_root)
