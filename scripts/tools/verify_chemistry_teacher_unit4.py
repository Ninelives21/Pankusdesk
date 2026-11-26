#!/usr/bin/env python3
"""Check source-preserving Unit 4 Q&A, tables, figures and unchanged neighbours."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

from build_chemistry_teacher_unit4 import build
from verify_cfe_revision_structure import Document

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/chemistry-engineers'
RELATIVE_PAGE = 'college/1-1/chemistry-engineers/teacher-notes-unit-wise.html'


def normal(text):
    return re.sub(r'\s+', ' ', text).strip()


def flattened(blocks):
    words = []
    for block in blocks:
        if block['type'] in ('paragraph', 'heading'):
            words.extend(block['text'].split())
        elif block['type'] == 'question':
            words.extend(block['question'].split())
            words.extend(flattened(block['answer']))
        elif block['type'] == 'figure':
            words.extend(' '.join(block['source_text']).split())
        elif block['type'] == 'table':
            words.extend(' '.join(block['headers'] + sum(block['rows'], [])).split())
    return words


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path)
    parser.add_argument('--baseline-ref', help='Compare Units 3 and 5 with an inspected Git ref')
    args = parser.parse_args()
    data = json.loads((SUBJECT / 'revision/teacher-unit-4.json').read_text())
    manifest = json.loads((SUBJECT / 'teacher-notes-unit-wise-manifest.json').read_text())
    text = (ROOT / RELATIVE_PAGE).read_text()
    doc = Document(text)
    ids = [n.attrs['id'] for n in doc.nodes if 'id' in n.attrs]
    assert len(ids) == len(set(ids)), 'Duplicate anchors'
    assert text.index('id="unit-3"') < text.index('id="unit-4"') < text.index('id="unit-5"')
    assert text.index('#unit-3') < text.index('#unit-4') < text.index('#unit-5')
    assert build(text, data) == text, 'Generated Unit 4 must be reproducible'
    questions = [e for d in data['documents'] for e in d['events'] if e['type'] == 'question']
    assert len(questions) == 126
    assert [d['question_count'] for d in data['documents']] == [44, 18, 12, 19, 33]
    assert [d['page_count'] for d in data['documents']] == [12, 10, 8, 7, 6]
    for document in data['documents']:
        assert manifest['question_counts'][f'unit-4-{document["category"]}'] == document['question_count']
        for page in document['page_transcripts']:
            assert hashlib.sha256(page['text'].encode()).hexdigest() == page['text_sha256']
        for event in document['events']:
            if event['type'] != 'question':
                continue
            question = doc.ids[event['id']]
            visible = next(n for n in question.elements() if n.has_class('study-example-question'))
            assert normal(visible.text()) == normal(event['question']), event['id']
            solution = next(n for n in question.elements() if n.has_class('study-example-solution'))
            # Compare every supplied prose block, not just titles or answer length.
            rendered = normal(solution.text())
            for block in event['answer']:
                if block['type'] == 'paragraph':
                    assert normal(block['text']) in rendered, (event['id'], block['text'])
                elif block['type'] == 'table':
                    for cell in block['headers'] + sum(block['rows'], []):
                        assert normal(cell) in rendered, (event['id'], cell)
            assert solution.text().strip(), event['id']
    class_test = doc.ids['u4-class-test']
    class_questions = [n for n in class_test.elements() if n.has_class('collection-question')]
    assert [n.attrs['id'] for n in class_questions] == [f'u4-class-test-q{i}' for i in range(1, 34)]
    unit_sections = [n.attrs['id'] for n in doc.ids['unit-4'].children
                     if getattr(n, 'tag', None) == 'section']
    assert unit_sections == ['u4-qbank', 'u4-mid2', 'u4-endsem', 'u4-faqs', 'u4-class-test']
    assert '#u4-class-test' in text.split('</aside>', 1)[0]
    assert 'CF₂=CF₂ → [–CF₂–CF₂–]ₙ' in doc.ids['u4-class-test-q30'].text()
    gaps = [q['id'] for q in questions if q.get('source_gap')]
    assert gaps == ['u4-qbank-q9', 'u4-qbank-q16']
    assert all('Source gap:' in doc.ids[q].text() for q in gaps)
    assert 'not counts of distinct examination sittings' in doc.ids['u4-faqs'].text()
    assert 'NOT included' in doc.ids['u4-mid2'].text()
    unit = list(doc.ids['unit-4'].elements())
    assert sum(n.tag == 'table' for n in unit) == 10
    assert sum(n.tag == 'figure' for n in unit) == 24
    figures = manifest['unit_4_intake']['figures']
    assert len(figures) == 24
    for figure in figures:
        assert hashlib.sha256((ROOT / figure['src']).read_bytes()).hexdigest() == figure['sha256']
    for node in unit:
        for key in ('href', 'src'):
            value = node.attrs.get(key)
            if value:
                path, _, anchor = value.partition('#')
                assert (ROOT / path).is_file(), value
                if anchor:
                    assert anchor in doc.ids
    if args.baseline_ref:
        baseline = subprocess.check_output(['git', 'show', f'{args.baseline_ref}:{RELATIVE_PAGE}'], cwd=ROOT).decode()
        for number, end in [(3, '<section class="document-page teacher-notes-unit" id="unit-5">'), (5, '</article>')]:
            start = f'<section class="document-page teacher-notes-unit" id="unit-{number}">'
            old = baseline.split(start, 1)[1].split(end, 1)[0]
            if number == 3:
                old = old.split('<section class="document-page teacher-notes-unit" id="unit-4">', 1)[0]
            new = text.split(start, 1)[1]
            if number == 3:
                new = new.split('<section class="document-page teacher-notes-unit" id="unit-4">', 1)[0]
            else:
                new = new.split(end, 1)[0]
            assert old == new, f'Unit {number} changed'
        previous = Document(baseline)
        for identifier, node in previous.ids.items():
            if re.fullmatch(r'u4-(?:qbank|mid2|endsem|faqs)-q\d+', identifier):
                assert node.text() == doc.ids[identifier].text(), identifier
        print('PASS: existing Unit 4 question/answer text remains unchanged')
        print('PASS: Units 3 and 5 remain byte-for-byte unchanged against', args.baseline_ref)
    if args.source_dir:
        import fitz  # optional original-source audit; ordinary checkout checks are stdlib-only
        for document in data['documents']:
            pdf = args.source_dir / document['source_filename']
            assert hashlib.sha256(pdf.read_bytes()).hexdigest() == document['sha256']
            original = fitz.open(pdf)
            words = []
            for index, page in enumerate(original):
                assert page.get_text() == document['page_transcripts'][index]['text']
                for block in page.get_text('dict')['blocks']:
                    if block['type'] != 0 or block['bbox'][1] > document.get('footer_top', 740):
                        continue
                    spans = [span for line in block['lines'] for span in line['spans']]
                    if spans[0]['size'] >= 15:
                        continue  # source title, represented by the Unit 4 shell
                    words.extend(' '.join(span['text'] for span in spans).split())
            assert Counter(words) == Counter(flattened(document['events'])), document['source_filename']
            for figure in figures:
                if f'-{document["category"]}-' not in figure['src']:
                    continue
                pix = original[figure['page'] - 1].get_pixmap(matrix=fitz.Matrix(2, 2), clip=fitz.Rect(figure['bbox']))
                saved = fitz.Pixmap(str(ROOT / figure['src']))
                assert pix.width == saved.width and pix.height == saved.height and pix.samples == saved.samples, figure['src']
        print('PASS: 5 PDF identities, all 43 page texts, complete native-word accounting and all 24 source-rendered crops')
    else:
        print('Original-PDF comparison not run; supply --source-dir to repeat source and pixel checks.')
    print('CHEMISTRY TEACHER UNIT 4 VERIFY: PASS — 126 questions (33 Class test), 10 tables, 24 supplied figures, 2 explicit source gaps, navigation and source metadata.')


if __name__ == '__main__':
    main()
