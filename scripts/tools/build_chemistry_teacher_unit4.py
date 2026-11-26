#!/usr/bin/env python3
"""Insert/rebuild only Unit 4 in the existing teacher Q&A collection."""
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/chemistry-engineers'
PAGE = 'college/1-1/chemistry-engineers/teacher-notes-unit-wise.html'
LABELS = {'qbank': 'QBank', 'mid2': 'Mid 2', 'endsem': 'End Sem', 'faqs': 'FAQs', 'class-test': 'Class test'}


def source_text(text):
    # Source-labelled subparts remain distinct without changing their wording.
    parts = re.split(r'(?=\([a-d]\)|\((?:i|ii|iii|iv)\)|(?<![\w(])(?:i|ii|iii|iv)\))', text)
    return '<br>'.join(escape(part) for part in parts if part)


def render_block(block):
    kind = block['type']
    if kind == 'paragraph':
        text = source_text(block['text'])
        if block['text'].startswith(('Observed in:', 'Approximate source-topic', 'Teacher notes · PDF')):
            return f'<p class="collection-status">{text}</p>'
        return f'<p>{text}</p>'
    if kind == 'heading':
        return f'<h4 class="teacher-notes-group">{escape(block["text"])}</h4>'
    if kind == 'table':
        headers = ''.join(f'<th scope="col">{escape(cell)}</th>' for cell in block['headers'])
        rows = ''.join('<tr>' + ''.join(f'<td>{escape(cell)}</td>' for cell in row) + '</tr>' for row in block['rows'])
        return f'<div class="source-table-scroll"><table><caption>Supplied comparison · PDF page {block["page"]}</caption><thead><tr>{headers}</tr></thead><tbody>{rows}</tbody></table></div>'
    if kind == 'figure':
        src = escape(block['src'])
        return f'<figure class="study-figure teacher-notes-figure"><a href="{src}" target="_blank" rel="noopener"><img src="{src}" width="{block["width"]}" height="{block["height"]}" alt="{escape(block["alt"])}" loading="lazy" decoding="async"></a><figcaption>{escape(block["caption"])} · Supplied PDF page {block["page"]}; original rendering, select to enlarge.</figcaption></figure>'
    raise ValueError(kind)


def render_question(question):
    answer = []
    # Explicit answer subpart markers receive the existing shared alternating panels.
    open_part = False
    for block in question['answer']:
        if block['type'] == 'paragraph' and re.fullmatch(r'\([a-d]\)', block['text']):
            if open_part:
                answer.append('</div>')
            answer.append(f'<div class="teacher-answer-part"><h5>{escape(block["text"])}</h5>')
            open_part = True
        else:
            answer.append(render_block(block))
    if open_part:
        answer.append('</div>')
    if question.get('source_gap'):
        answer.append(f'<p class="collection-status"><strong>Source gap:</strong> {escape(question["source_gap"])}</p>')
    pages = ', '.join(map(str, question['source_pages']))
    return f'''<details class="study-accordion-item study-accordion-item--example collection-question" id="{question['id']}"><summary><span class="study-example-summary-copy"><span class="study-example-title">Supplied PDF · p. {pages}</span><span class="study-example-question"><strong>{source_text(question['question'])}</strong></span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{''.join(answer)}</div></details>'''


def render(data):
    navigation = f'<details class="source-nav-group" open><summary><a href="{PAGE}#unit-4">Unit 4 · Polymeric Materials</a></summary>'
    navigation += ''.join(f'<a class="document-nav-child" href="{PAGE}#u4-{key}">{label}</a>' for key, label in LABELS.items()) + '</details>'
    content = ['<section class="document-page teacher-notes-unit" id="unit-4"><h2>Unit 4 · Polymeric Materials</h2><p>Questions and supplied answers from the Unit 4 study PDFs and supplied class-test compilation. Teacher-note references and corrections remain as supplied; supplementary topics and historical R22 material are identified in context.</p>']
    for document in data['documents']:
        category = document['category']
        content.append(f'<section class="bank-source-group teacher-note-subsection" id="u4-{category}"><h3>{LABELS[category]}</h3>')
        if category == 'mid2':
            content.append('<p class="collection-status">R25 polymer questions first. The historical R22 corrosion appendix below is outside current R25 Unit 4.</p>')
        if category == 'faqs':
            content.append('<p class="collection-status">The supplied frequencies are approximate topic-mention counts across source entries, not counts of distinct examination sittings.</p>')
        for event in document['events']:
            content.append(render_question(event) if event['type'] == 'question' else render_block(event))
        content.append('</section>')
    content.append('</section>')
    return navigation, '\n'.join(content) + '\n'


def build(text, data):
    nav, body = render(data)
    # Remove a previous generated Unit 4 only; preserve Units 3 and 5 byte-for-byte.
    nav4 = f'<details class="source-nav-group" open><summary><a href="{PAGE}#unit-4">'
    nav5 = f'<details class="source-nav-group" open><summary><a href="{PAGE}#unit-5">'
    if nav4 in text:
        start = text.index(nav4)
        text = text[:start] + text[text.index(nav5, start):]
    section4 = '<section class="document-page teacher-notes-unit" id="unit-4">'
    section5 = '<section class="document-page teacher-notes-unit" id="unit-5">'
    if section4 in text:
        start = text.index(section4)
        text = text[:start] + text[text.index(section5, start):]
    assert text.count(nav5) == text.count(section5) == 1
    return text.replace(nav5, nav + nav5).replace(section5, body + section5)


if __name__ == '__main__':
    data = json.loads((SUBJECT / 'revision/teacher-unit-4.json').read_text())
    page = SUBJECT / 'teacher-notes-unit-wise.html'
    page.write_text(build(page.read_text(), data))
    print('Built Unit 4 teacher Q&A: 44 QBank, 18 Mid 2, 12 End Sem, 19 FAQ and 33 Class test entries.')
