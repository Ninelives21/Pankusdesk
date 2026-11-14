"""Check the frozen FAQ's source coverage and execute its standalone C11 examples.

Optional --source-text compares every numbered question with the local intake text;
private intake files are not required or published by the normal verifier.
"""
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
    extras = bank['sections'][4]['questions']
    expected = [(3, 'A', 7), (3, 'Q', 11), (4, 'A', 5), (4, 'Q', 8)]
    assert [(q['unit'], q['number']) for q in numbered] == [
        (unit, f'{prefix}{n}') for unit, prefix, count in expected for n in range(1, count + 1)
    ]
    assert len(numbered) == snapshot['numbered_questions'] == 31
    assert len(extras) == snapshot['additional_topics'] == 8
    assert [q['number'] for q in extras] == [f'T{i}' for i in range(1, 9)]
    anchors = [section['id'] for section in bank['sections']]
    for q in numbered + extras:
        anchors.append(q['id'])
        assert q['answer'] in bank['answers'] and q['nav_label']
        assert q['source_pages'][0] == q['page']
        assert all(3 <= page <= 20 for page in q['source_pages'])
    assert len(anchors) == len(set(anchors))
    used_programs = set()
    for answer in bank['answers'].values():
        assert answer['paragraphs'] and answer['authority'].startswith('PankusDesk-authored')
        assert answer['basis'] in {'priyanka', 'priyanka+senior', 'senior', 'general'}
        assert answer['basis_label'] and isinstance(answer['note_refs'], list)
        used_programs.update(answer['programs'])
    assert used_programs == set(bank['programs'])
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
        print('PASS: all 31 question wordings, numbers, order and starting pages match the supplied text.')
    print('PASS: 31 numbered questions + 8 final topics, source snapshot, anchors, answer/program references and card.')
    # Exercise meaningful boundaries beyond the displayed examples.
    cases = {
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
    for key, program in bank['programs'].items():
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
    print(f'PASS: {len(bank["programs"])} C11 programs compile warning-free; all samples and boundary cases match.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-text')
    verify(parser.parse_args().source_text)
