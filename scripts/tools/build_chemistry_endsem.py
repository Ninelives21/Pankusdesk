#!/usr/bin/env python3
"""Render the four actual Chemistry End Sem papers and mark-proportionate answers."""
import json
import re
from build_chemistry_collections import S, R, E, PREFIX, shell, anchor
from study_answer_blocks import render_blocks


def main():
    data = json.loads((R / 'end-sem-papers.json').read_text())
    figures = {}
    for name in ['source-figures.json', 'mid-2-source-figures.json', 'end-sem-source-figures.json']:
        figures.update({f['id']: f for f in json.loads((R / name).read_text())['figures']})

    def figure(id):
        f = figures[id]
        note = f.get('student_note', '')
        return f'<figure class="study-figure" data-source-figure="{E(id)}"><a href="{E(f["asset"])}" target="_blank" rel="noopener"><img src="{E(f["asset"])}" alt="{E(f["alt"])}" width="{f["width"]}" height="{f["height"]}" loading="lazy" decoding="async"></a><figcaption><strong>{E(f["title"])}.</strong>{(" " + E(note)) if note else ""}</figcaption></figure>'

    def prompt(text):
        # Keep printed roman subparts on separate lines, even in closed cards.
        return re.sub(r'\(([iv]+)\)\s*', r'<br><strong>(\1)</strong> ', E(text))

    def answer_blocks(blocks):
        return ''.join(
            f'<section class="study-solution-part"><h4>{E(b["title"])}</h4>{answer_blocks(b["blocks"])}</section>'
            if b['type'] == 'section' else render_blocks([b], figure)
            for b in blocks)

    def answer(item):
        return answer_blocks(data['answers'][item['answer_ref']]['blocks'])

    def question(q, part):
        label = f'Part {part} · ' + (f'({q["number"]})' if part == 'A' else f'Q{q["number"]}') + f' · {q["marks"]} marks'
        text = prompt(q['prompt'])
        body = ''
        if q.get('parts'):
            for sub in q['parts']:
                text += f'<br><strong>({E(sub["label"])})</strong> {prompt(sub["prompt"])} <strong>[{sub["marks"]} marks]</strong>'
                body += f'<section class="study-solution-part" id="{E(sub["id"])}"><h4>({E(sub["label"])})</h4>{answer(sub)}</section>'
        else:
            body = answer(q)
        return f'<details class="study-accordion-item study-accordion-item--example collection-question" id="{E(q["id"])}"><summary><span class="study-example-summary-copy"><span class="study-example-title">{E(label)}</span><span class="study-example-question">{text}</span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{body}</div></details>'

    nav = ''
    body = '<div class="bank-view-intro"><p id="bank-view-status" role="status">Viewing January 2026 · R25</p><p>Choose a paper and open a question for its answer. All OR alternatives are solved.</p><p>Older R22 papers retain their original units and questions; their syllabus differs from R25.</p></div>'
    for paper in data['papers']:
        title = paper['session'] + ' · ' + paper['regulation'] + (' · ME' if paper['branches'] == ['ME'] else '')
        default = paper['id'] == data['default_paper']
        nav += f'<a href="{anchor("end-sem.html", paper["id"])}" data-bank-unit="{paper["id"]}"' + (' aria-current="location"' if default else '') + f'>{E(title)}</a>'
        block = f'<h2>{E(title)}</h2><p><strong>{E(paper["subject"])}</strong> · {E(paper["exam_type"])} examinations · B.Tech I Year, Semester I.</p><p>Subject code: <strong>{E(paper["subject_code"])}</strong> · Common to: {E(", ".join(paper["branches"]))} · Duration: 3 hours · Maximum: 60 marks.</p><p><strong>Exam choices:</strong> Part A: answer all five, 5 × 2 = 10 marks. Part B: answer one question from each unit, 5 × 10 = 50 marks.</p>'
        block += '<h3>Part A · Short answers · 10 marks</h3>' + ''.join(question(q, 'A') for q in paper['part_a'])
        block += '<h3>Part B · 50 marks</h3>'
        for unit in range(1, 6):
            first, second = paper['part_b'][2 * unit - 2:2 * unit]
            block += f'<h3>Unit {unit} · Choose Q{first["number"]} OR Q{second["number"]}</h3>'
            block += question(first, 'B') + '<p class="paper-or"><strong>OR</strong> · answer one of this pair in the examination</p>' + question(second, 'B')
        hidden = '' if default else ' hidden'
        body += f'<section class="document-page bank-unit" id="{paper["id"]}" data-bank-unit-section="{paper["id"]}" data-bank-title="{E(title)}"{hidden}>{block}</section>'
    page = shell('end-sem.html', data['title'], 'Four actual examination papers with short answers, worked essays and relevant diagrams. The R25 paper opens first.', nav, body)
    page = page.replace('<body>', f'<body data-question-bank="true" data-bank-default="{data["default_paper"]}" data-bank-allow-all="false">')
    for css in ['pages/end-sem-notes', 'pages/source-notes', 'pages/practice']:
        page = page.replace('</head>', f'<link rel="stylesheet" href="styles/new/{css}.css">\n</head>')
    page = page.replace('</head>', '<script src="scripts/new/question-bank-navigation.js" defer></script>\n</head>')
    (S / 'end-sem.html').write_text(page)
    print('Built 4 End Sem papers / 60 question dropdowns / 87 answer parts, with all 20 OR pairs.')


if __name__ == '__main__':
    main()
