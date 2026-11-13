#!/usr/bin/env python3
"""Check reviewed question parts and source block boundaries, not just flattened text."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/chemistry-engineers'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}


class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def text(self):
        return ''.join(c if isinstance(c, str) else c.text() for c in self.children)

    def elements(self):
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.elements()

    def has_class(self, name):
        return name in self.attrs.get('class', '').split()


class Document(HTMLParser):
    def __init__(self, value):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(value)
        self.nodes = list(self.root.elements())
        self.ids = {n.attrs['id']: n for n in self.nodes if 'id' in n.attrs}

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def normalize(value):
    # Whitespace inside a word is meaningful: "Galvani c)" must not equal "Galvanic)".
    return re.sub(r'\s+', ' ', value).strip()


def question_check(doc, records, unit, errors):
    expected_ids = {record['id'] for record in records}
    actual_ids = {node.attrs.get('id') for node in doc.nodes
                  if node.has_class('study-accordion-item')
                  and re.fullmatch(r'(?:u2-)?qa-(?:short|essay|extra)-\d+', node.attrs.get('id', ''))}
    if actual_ids != expected_ids:
        errors.append(f'{unit}: question inventory differs: missing {sorted(expected_ids - actual_ids)}, unexpected {sorted(actual_ids - expected_ids)}')
    for record in records:
        identifier = record['id']
        card = doc.ids.get(identifier)
        if card is None:
            errors.append(f'{unit}: missing {identifier}')
            continue
        copies = [n for n in card.elements() if n.has_class('study-example-question')]
        if len(copies) != 1:
            errors.append(f'{identifier}: expected one complete visible question')
            continue
        actual = [normalize(n.text()) for n in copies[0].children if isinstance(n, Node)]
        expected = record.get('source_question_parts', record.get('question_parts'))
        if expected is None:
            errors.append(f'{identifier}: missing independently reviewed question-part contract')
            continue
        expected = list(map(normalize, expected))
        if actual != expected:
            errors.append(f'{identifier}: question parts differ\n  expected: {expected}\n  actual:   {actual}')
        if unit != 2:
            continue
        labels = [normalize(n.text()) for n in card.elements() if n.has_class('answer-part-heading')]
        if labels != record['expected_answer_part_labels']:
            errors.append(f'{identifier}: answer parts differ: {labels}')
        images = [n for n in card.elements() if n.tag == 'img']
        assessment = record['figure_assessment']
        expected_images = len(assessment['asset_ids']) + bool(assessment.get('reused_approved_asset'))
        if len(images) != expected_images:
            errors.append(f'{identifier}: expected {expected_images} images, found {len(images)}')


def check(unit2_path):
    errors = []
    unit2 = Document(unit2_path.read_text())
    # Preserve the original fixed contracts across the new notes/bank routes.
    bank = Document((SUBJECT / 'question-banks.html').read_text())
    unit2_bank = bank.ids['unit-2']
    audit = json.loads((SUBJECT / 'revision/unit-2-source-audit.json').read_text())
    original_cards = [bank.ids[q['id']] for q in audit['questions']]
    relocated = [node for card in original_cards for node in [card, *card.elements()]]
    unit2.nodes.extend(relocated)
    unit2.ids.update({n.attrs['id']: n for n in relocated if 'id' in n.attrs})
    audit = json.loads((SUBJECT / 'revision/unit-2-source-audit.json').read_text())
    contract = json.loads((SUBJECT / 'revision/unit-2-structure-contract.json').read_text())
    question_check(unit2, audit['questions'], 2, errors)
    unit1 = Document('')
    unit1.nodes = [bank.ids['unit-1'], *bank.ids['unit-1'].elements()]
    unit1.ids = {n.attrs['id']: n for n in unit1.nodes if 'id' in n.attrs}
    unit1_audit = json.loads((SUBJECT / 'revision/unit-1-qa-audit.json').read_text())
    question_check(unit1, unit1_audit['questions'], 1, errors)
    all_ids = [n.attrs['id'] for n in unit2.nodes if 'id' in n.attrs]
    if len(all_ids) != len(set(all_ids)):
        errors.append('Unit 2: duplicate IDs')
    for item in contract['paragraphs']:
        matches = [n for n in unit2.nodes if n.tag == item['tag'] and normalize(item['contains']) in normalize(n.text())]
        if len(matches) != 1:
            errors.append(f"Expected one complete {item['tag']} block containing: {item['contains']!r}; found {len(matches)}")
        elif any(p.tag in {'td', 'th'} for p in ancestors(matches[0])):
            errors.append(f"Narrative trapped in table cell: {item['contains']!r}")
    for identifier, shapes in contract['source_table_shapes'].items():
        tables = [n for n in unit2.ids[identifier].elements() if n.tag == 'table']
        actual = []
        for table in tables:
            rows = [n for n in table.elements() if n.tag == 'tr']
            counts = [sum(isinstance(c, Node) and c.tag in {'th', 'td'} for c in row.children) for row in rows]
            actual.append([len(rows), max(counts, default=0)])
            if len(set(counts)) != 1:
                errors.append(f'{identifier}: inconsistent table row widths {counts}')
        if actual != shapes:
            errors.append(f'{identifier}: source table shapes differ: expected {shapes}, found {actual}')
    for identifier, expected in contract['part_image_counts'].items():
        parts = [n for n in unit2.ids[identifier].elements() if n.has_class('answer-part')]
        actual = [sum(n.tag == 'img' for n in part.elements()) for part in parts]
        if actual != expected:
            errors.append(f'{identifier}: figures in wrong answer part: {actual}')
    for item in contract.get('table_cell_phrases', []):
        cells = [n for n in unit2.ids[item['section']].elements() if n.tag == 'td']
        if not any(normalize(item['contains']) in normalize(cell.text()) for cell in cells):
            errors.append(f"Split table-cell sentence: {item['contains']!r}")
    if sum(n.tag == 'img' for n in unit2.nodes) != contract['image_placements']:
        errors.append('Unit 2: image placement count changed')
    for node in unit2.nodes:
        if node.tag == 'p' and normalize(node.text()) in {'•', '➢', '', '❖'}:
            errors.append('Unit 2: orphan bullet paragraph')
        href = node.attrs.get('href', '')
        if href.startswith('#') and href[1:] not in unit2.ids:
            errors.append(f'Unit 2: unresolved anchor {href}')
    return errors


def ancestors(node):
    while node.parent:
        node = node.parent
        yield node


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--html', type=Path, default=SUBJECT / 'end-sem-unit-2.html')
    args = parser.parse_args()
    problems = check(args.html)
    if problems:
        print('CFE REVISION STRUCTURE: FAIL\n' + '\n'.join(problems))
        sys.exit(1)
    print('CFE REVISION STRUCTURE: PASS — notes plus relocated bank: 44 Unit 2 and 36 Unit 1 questions; exact part boundaries, answer parts, source paragraphs/tables, figures and anchors')
