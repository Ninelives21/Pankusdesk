"""Check PDF-transcribed FAQ coverage and retained C11 reference examples.

Optional --source-text compares every numbered question with the local intake text;
private intake files are not required or published by the normal verifier.
"""
import hashlib
import argparse
import json
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/programming-problem-solving'


def verify(source_text=None):
    bank = json.loads((SUBJECT / 'exam-prep/frequently-asked-questions.json').read_text())
    snapshot = bank['snapshot']
    assert snapshot['pages'] == 20
    assert snapshot['sha256'] == 'f8099c249ecc5333b68e59c51203579874d84d493b103ee3ce86059b7b41967c'
    numbered = [q for section in bank['sections'][:4] for q in section['questions']]
    extras = bank['sections'][4].get('nav_items', bank['sections'][4]['questions'])
    expected = [(3, 'A', 7), (3, 'Q', 11), (4, 'A', 5), (4, 'Q', 8)]
    assert [(q['unit'], q['number']) for q in numbered] == [
        (unit, f'{prefix}{n}') for unit, prefix, count in expected for n in range(1, count + 1)
    ]
    assert len(numbered) == snapshot['numbered_questions'] == 31
    assert len(extras) == snapshot['additional_topics'] == 8
    assert [q['number'] for q in extras] == [f'T{i}' for i in range(1, 9)]
    anchors = [section['id'] for section in bank['sections']]
    for q in numbered:
        anchors.append(q['id'])
        assert q['answer'] in bank['answers'] and q['nav_label']
        assert q['source_pages'][0] == q['page']
        assert all(3 <= page <= 20 for page in q['source_pages'])
    anchors.extend(q['id'] for q in extras)
    assert len(anchors) == len(set(anchors))
    def check_blocks(blocks):
        for block in blocks:
            assert block['type'] in {'paragraph', 'heading', 'code', 'list', 'table', 'part'}
            if block['type'] == 'table':
                assert block['headers'] and block['rows']
                assert all(len(row) == len(block['headers']) for row in block['rows'])
            elif block['type'] == 'part':
                assert block['label'] and block['blocks']
                check_blocks(block['blocks'])
            elif block['type'] == 'list':
                assert block['items'] and all(item['text'] for item in block['items'])
            elif block['type'] == 'code':
                assert block['code']
            else:
                assert block['text']

    def flat(blocks):
        parts = []
        for block in blocks:
            kind = block['type']
            if kind in {'paragraph', 'heading'}:
                parts.append(block['text'])
            elif kind == 'code':
                parts.append(block['code'])
            elif kind == 'list':
                parts.extend(item['text'] for item in block['items'])
            elif kind == 'table':
                parts.extend(block['headers'])
                parts.extend(cell for row in block['rows'] for cell in row)
            elif kind == 'part':
                parts.extend([block['label'], flat(block['blocks'])])
        return '\n'.join(parts)

    assert bank['kind'] == 'source-transcription'
    assert len(bank['answers']) == 31 and not bank['programs']
    final_table = bank['sections'][4]['blocks'][-1]
    assert len(final_table['rows']) == 8
    assert final_table['row_ids'] == [q['id'] for q in extras]
    for section in bank['sections']:
        check_blocks(section.get('blocks', []))
        check_blocks(section.get('after_blocks', []))
    for answer in bank['answers'].values():
        assert answer['basis'] == 'supplied-pdf' and not answer['programs']
        assert answer['source_metadata'] and answer['blocks']
        check_blocks(answer['blocks'])
        digest = hashlib.sha256(re.sub(r'\s+', '', flat(answer['blocks'])).encode()).hexdigest()
        assert digest == answer['source_text_sha256'], 'Source answer text changed'
    # These records are not rendered. Keep the existing authored-C regression checks
    # independent of transcription; original Turbo C listings are not claimed C11.
    reference = bank['authored_reference']
    used_programs = set()
    for answer in reference['answers'].values():
        assert answer['paragraphs'] and answer['authority'].startswith('PankusDesk-authored')
        assert answer['basis'] in {'priyanka', 'priyanka+senior', 'senior', 'general'}
        assert answer['basis_label'] and isinstance(answer['note_refs'], list)
        used_programs.update(answer['programs'])
        used_programs.update(answer.get('supplementary_programs', []))
        assert answer['blocks'] and 'research_topic_ids' in answer
        check_blocks(answer['blocks'])
    assert used_programs == set(reference['programs'])
    card = next(c for c in json.loads((SUBJECT / 'index-resources.json').read_text())['questions']
                if c.get('id') == 'frequently-asked-questions')
    assert (SUBJECT / card['href']).is_file()
    if source_text:
        original = []
        for match in re.finditer(r'--- PAGE (\d+) ---\n(.*?)(?=\n--- PAGE |\Z)',
                                 Path(source_text).read_text(), re.S):
            page = int(match[1])
            if page < 3:
                continue
            for question in re.finditer(r'^([AQ]\d+)\. (.*?)(?=\n(?:Asked in:|Teacher’s notes:))',
                                         match[2], re.M | re.S):
                original.append((3 if page < 14 else 4, question[1], ' '.join(question[2].split()), page))
        assert original == [(q['unit'], q['number'], q['question'], q['page']) for q in numbered]
        source = Path(source_text).read_text()
        source = source[source.index('--- PAGE 3 ---'):]
        source = re.sub(r'^--- PAGE \d+ ---\n|^PPS R25 •.*\n|^Page \d+\n', '', source, flags=re.M)
        source = re.sub(r'^(?:Unit III \(Second Half\) – Functions, Recursion, Storage Classes|Unit IV – Structures and Pointers|Part [AB] – .*?)\n', '', source, flags=re.M)
        source = source.split('\nUnit IV topics not in the teacher’s notes')[0]
        matches = list(re.finditer(r'^([AQ]\d+)\. (.*?)(?=\n(?:Asked in:|Teacher’s notes:))', source, re.M | re.S))

        def normalize(text):
            for before, after in bank['transcription_policy']['typography_repairs'].items():
                text = text.replace(before, after)
            text = re.sub(r'^\s*(?:\d+\.|•)\s*', '', text, flags=re.M)
            return re.sub(r'\s+', '', text)

        indexed = [(q, section) for section in bank['sections'][:4] for q in section['questions']]
        assert len(matches) == len(indexed) == 31
        for index, (match, (question, section)) in enumerate(zip(matches, indexed)):
            start = source.index('\n', match.end()) + 1
            end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
            lines = source[start:end].splitlines()
            while lines and (lines[0].startswith(('Asked in:', 'Teacher’s notes:'))
                             or re.fullmatch(r'[\d, –—−-]+', lines[0].strip())):
                lines.pop(0)
            expected_text = '\n'.join(lines)
            rendered_text = flat(bank['answers'][question['answer']]['blocks'])
            if question == section['questions'][-1]:
                rendered_text += '\n' + flat(section.get('after_blocks', []))
            assert normalize(expected_text) == normalize(rendered_text), question['id']
        print('PASS: all 31 complete supplied answers, including code, outputs and unit-end notices, match the source text.')
        print('PASS: all 31 question wordings, numbers, order and starting pages match the supplied text.')
    print('PASS: 31 numbered questions + 8 final topics, source snapshot, anchors, answer/program references and card.')
    # Exercise meaningful boundaries beyond the displayed examples.
    cases = {
        'source-categories': [('3 4\n1001 2\n', None), ('3\n', None)],
        'function-factorial': [('0\n', '1\n'), ('20\n', '2432902008176640000\n'), ('21\n', None)],
        'factorial': [('0\n', '1\n'), ('21\n', None)],
        'fibonacci': [('0\n', '\n'), ('1\n', '0\n'), ('21\n', None)],
        'sum-recursion': [('0\n', '0\n'), ('100\n', '5050\n'), ('101\n', None)],
        'ackermann': [('0 1\n', '2\n'), ('1 1\n', '3\n'), ('4 7\n', None)],
        'student-average': [('1 1\n1 A 75\n', '1 A average=75.00\n'),
                            ('0 3\n', None), ('1 0\n', None), ('1 11\n', None),
                            ('1 1\n1 A 101\n', None)],
        'array-sum': [('0\n', '0\n'), ('21\n', None)],
        'array-pointer-io': [('0\n', '\n'), ('21\n', None)],
        'student-details': [('101\n', None)],
    }
    for key, program in reference['programs'].items():
        assert program['note']
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            code, exe = folder / 'example.c', folder / 'example'
            code.write_text(program['code'])
            build = subprocess.run(['cc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-pedantic',
                                    str(code), '-o', str(exe)], capture_output=True, text=True)
            assert build.returncode == 0, (key, build.stderr)
            for sample, expected in [(program['input'], program['expected'])] + cases.get(key, []):
                result = subprocess.run([str(exe)], input=sample, capture_output=True, text=True,
                                        cwd=folder, timeout=10)
                if expected is None:
                    assert result.returncode != 0, (key, sample, 'invalid input accepted')
                else:
                    assert result.returncode == 0 and result.stdout == expected, (
                        key, sample, result.returncode, result.stdout, expected, result.stderr)
    print(f'PASS: {len(reference["programs"])} retained reference C11 programs compile warning-free; all samples and boundary cases match. Source Turbo C listings are preserved, not certified C11.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-text')
    verify(parser.parse_args().source_text)
