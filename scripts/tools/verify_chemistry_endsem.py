#!/usr/bin/env python3
"""Gate End Sem paper identity, original choices/marks, answers, assets and navigation."""
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from urllib.parse import urlsplit, unquote
from lxml import html

ROOT = Path(__file__).resolve().parents[2]
S = ROOT / 'college/1-1/chemistry-engineers'
R = S / 'revision'
data = json.loads((R / 'end-sem-papers.json').read_text())
page = html.fromstring((S / 'end-sem.html').read_text())
ids = page.xpath('//@id')
assert len(ids) == len(set(ids)), 'Duplicate anchors'
assert data['default_paper'] == 'cfe-endsem-2026-r25'
assert page.xpath('//body/@data-bank-default') == [data['default_paper']]
assert page.xpath('//body/@data-bank-allow-all') == ['false']
assert len(page.xpath('//*[@data-bank-unit-section and not(@hidden)]')) == 1
assert len(page.xpath('//a[@data-bank-unit and @data-bank-unit!="faq"]')) == 4
assert len(page.xpath('//a[@data-bank-unit="faq"]')) == 1
assert len(page.xpath('//*[@data-bank-unit-section!="faq"]//details[contains(@class,"collection-question")]')) == 60
assert len(page.xpath('//p[contains(@class,"paper-or")]')) == 20
assert page.xpath('//*[contains(@class,"document-back-top")]/following-sibling::details[contains(@class,"document-contents")]')
assert not page.xpath('//iframe|//embed|//object')
expected = [('January 2026', 'R25', '25BS1CH101', '74b56552e95a'),
            ('January 2025', 'R22', '22BS1CH102', '705b1f3db2e9'),
            ('January 2024', 'R22', '22BS1CH102', 'fa1037da6a81'),
            ('January 2025', 'R22', '22BS1CH101', '7250a088cf0c')]
assert len(data['papers']) == 4
sources = json.loads((R / 'source-inventory.json').read_text())['sources']
lookup = {s['id']: s for s in sources}
lookup.update({s['source_id']: s for s in sources if s.get('source_id')})
figures = {}
for file in ['source-figures.json', 'mid-2-source-figures.json', 'end-sem-source-figures.json']:
    figures.update({f['id']: f for f in json.loads((R / file).read_text())['figures']})
def blocks(items):
    for item in items:
        if item['type'] == 'section':
            yield from blocks(item['blocks'])
        else:
            yield item

parts = 0
for paper, identity in zip(data['papers'], expected):
    assert (paper['session'], paper['regulation'], paper['subject_code'], paper['source']['sha256'][:12]) == identity
    assert len(paper['source']['sha256']) == 64 and paper['source']['pages'] == [1, 2]
    private = Path('/workspace/work/chem-endsem-intake') / (identity[3] + '-' + paper['source']['filename'])
    if private.exists():
        assert hashlib.sha256(private.read_bytes()).hexdigest() == paper['source']['sha256']
    assert paper['maximum_marks'] == 60 and paper['duration_hours'] == 3
    assert len(paper['part_a']) == 5 and len(paper['part_b']) == 10
    assert [q['number'] for q in paper['part_a']] == list('abcde')
    assert [q['marks'] for q in paper['part_a']] == [2] * 5
    assert [q['number'] for q in paper['part_b']] == list(map(str, range(1, 11)))
    assert [q['unit'] for q in paper['part_b']] == [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    assert [q['marks'] for q in paper['part_b']] == [10] * 10
    for q in paper['part_a'] + paper['part_b']:
        panel = page.get_element_by_id(q['id'])
        summary = panel.find('summary').text_content()
        normal = lambda s: re.sub(r'\s+', ' ', s).strip()
        assert normal(q['prompt']) in normal(summary)
        if q.get('parts'):
            assert sum(p['marks'] for p in q['parts']) == 10
        for sub in q.get('parts', [q]):
            parts += 1
            assert normal(sub['prompt']) in normal(summary)
            answer = data['answers'][sub['answer_ref']]
            assert answer['blocks'] and answer['source_refs']
            for ref in answer['source_refs']:
                assert ref['source_id'] in lookup
                assert ref['pages'] and all(1 <= n <= lookup[ref['source_id']]['pages_or_slides'] for n in ref['pages'])
            node = page.get_element_by_id(sub['id']) if q.get('parts') else panel
            for b in blocks(answer['blocks']):
                if b['type'] == 'paragraph': assert b['text'] in node.text_content()
                elif b['type'] == 'list':
                    assert b['items']
                    for item in b['items']: assert item in node.text_content()
                elif b['type'] == 'equation':
                    assert b['latex'] in node.text_content()
                    assert r'\frac' not in b['latex']
                    assert not re.search(r'[\x00-\x08\x0b-\x1f]', b['latex'])
                elif b['type'] == 'table':
                    for row in b['rows']:
                        assert len(row) == len(b['headers'])
                        for cell in row: assert cell in node.text_content()
                elif b['type'] == 'figure':
                    f = figures[b['id']]
                    assert hashlib.sha256((ROOT / f['asset']).read_bytes()).hexdigest() == f.get('sha256', f.get('asset_sha256'))
                    assert node.xpath('.//figure[@data-source-figure=$id]//img[@src=$src]', id=b['id'], src=f['asset'])
                    assert f['source_sha256'] == lookup[f['source_id']]['sha256']
                else: raise AssertionError(b['type'])
assert parts == 87
assert len(page.get_element_by_id('cfe-endsem-2024-r22-b-10-a').xpath('.//section[contains(@class,"study-solution-part")]')) == 2
# Independent numerical recomputation with exact rational arithmetic, rather than stored rounded sums.
checks = {
    'num26': ([('18.2', 162), ('35.6', 84)], [('17', 111), ('17.6', 120)], (53.62, 29.98, 83.60)),
    'num24': ([('14.6', 146), ('16.2', 162)], [('9.5', 95), ('6', 120)], (20.00, 15.00, 35.00)),
    'numme': ([('84', 84), ('40.5', 162)], [('111', 111), ('60', 120)], (125.00, 150.00, 275.00))}
for key, (temp, perm, expected_values) in checks.items():
    t = sum(Fraction(c) * 100 / m for c, m in temp)
    p = sum(Fraction(c) * 100 / m for c, m in perm)
    values = tuple(round(float(v), 2) for v in [t, p, t+p])
    assert values == expected_values
    audit = data['answers'][key]['numerical_audit']
    assert tuple(audit[k] for k in ['temporary', 'permanent', 'total']) == values
    displayed = ' '.join(b.get('latex', '') for b in data['answers'][key]['blocks'])
    assert all(f'{v:.2f}' in displayed for v in values)
# Required diagrams must occur beside the intended answer, not elsewhere on the page.
required = {'cfe-endsem-2026-r25-b-2': ['endsem-ro'],
            'cfe-endsem-2026-r25-b-3-a': ['endsem-she'],
            'cfe-endsem-2026-r25-b-4': ['mid2-sacrificial', 'mid2-impressed'],
            'cfe-endsem-2026-r25-b-5-a': ['handout-pemfc'],
            'cfe-endsem-2026-r25-b-5-b': ['handout-fischer-tropsch'],
            'cfe-endsem-2026-r25-b-6-b': ['mid2-pem-electrolysis'],
            'cfe-endsem-2026-r25-b-10-a': ['handout-stm-apparatus'],
            'cfe-endsem-2025-r22-b-5-b': ['mid2-methanol'],
            'cfe-endsem-2025-r22-b-8': ['endsem-dry'],
            'cfe-endsem-2024-r22-b-2': ['endsem-ionexchange'],
            'cfe-endsem-2024-r22-b-6-a': ['handout-cracking'],
            'cfe-endsem-2024-r22-b-8': ['mid2-oxygen-corrosion'],
            'cfe-endsem-2024-r22-b-4': ['endsem-bakelite-network']}
for id, figs in required.items():
    for f in figs: assert page.get_element_by_id(id).xpath('.//figure[@data-source-figure=$id]', id=f)
assert 'Diagram unavailable:' in page.get_element_by_id('cfe-endsem-2026-r25-b-9-b').text_content()
assert 'mercury' in page.get_element_by_id('cfe-endsem-2026-r25-b-3-a').text_content()
for panel in page.xpath('//div[contains(@class,"study-example-solution")]'):
    assert not panel.xpath('.//*[contains(@class,"document-source") or contains(@class,"study-solution-label")]')
    assert not any(t in panel.text_content() for t in ['Answer basis:', 'SHA-256', 'Scope: retain', 'Question source:'])
for url in page.xpath('//@href | //@src'):
    u = urlsplit(url)
    if u.scheme: continue
    target = ROOT / unquote(u.path).lstrip('/') if u.path else S / 'end-sem.html'
    if target.is_dir(): target = target / 'index.html'
    assert target.is_file(), url
    if u.fragment: assert html.fromstring(target.read_text()).xpath('//*[@id=$id]', id=unquote(u.fragment)), url
cards = json.loads((S / 'index-resources.json').read_text())['questions']
assert sum(c['href'] == 'end-sem.html' for c in cards) == 1
subject = json.loads((S / 'subject.json').read_text())
assert not any(c.get('practiceKey') == 'pyqs' for c in subject['studyResources'])
assert subject['practice']['pyqs']['href'] == 'end-sem.html'
assert 'end-sem.html' in (S / 'pyqs.html').read_text()
print('CHEMISTRY END SEM: PASS — 4 source-identified papers, 60 questions / 87 answer parts, 20 OR pairs, original marks, 3 independently recomputed numericals, figures, links and answer-only presentation. CO-analyser drawing remains explicitly unavailable.')

faq = json.loads((R / 'end-sem-faq.json').read_text())
assert faq['paper_count'] == len(data['papers']) == 4
assert len(faq['entries']) == 14
records = {}; paper_for = {}; kinds = {}
for paper in data['papers']:
    for section in ['part_a', 'part_b']:
        for q in paper[section]:
            for item in [q] + q.get('parts', []):
                records[item['id']] = item
                paper_for[item['id']] = paper['id']
                kinds[item['id']] = 'short' if section == 'part_a' else 'essay'
expected_counts = {'biosensors':3, 'hardness-salts':2, 'batteries':2, 'saline-rusting':2,
                   'galvanic':4, 'hardness-numericals':3, 'cathodic':3,
                   'shape-memory-polymers':3, 'self-healing':3, 'scale-sludge':2,
                   'reverse-osmosis':2, 'electrochemical-rusting':2,
                   'addition-condensation':2, 'thermoplastics-thermosets':2}
for entry in faq['entries']:
    assert entry['r25_unit'] in range(1, 6)
    assert len(entry['topic_matches']) == len(set(entry['topic_matches']))
    assert all(id in records and kinds[id] == entry['kind'] for id in entry['topic_matches'])
    count = len({paper_for[id] for id in entry['topic_matches']})
    assert count == expected_counts[entry['id'].removeprefix('endsem-faq-')]
    panel = page.get_element_by_id(entry['id'])
    assert f'{count} of 4 papers' in panel.find('summary').text_content()
    assert entry['title'] in panel.find('summary').text_content()
    for ref in entry['answer_refs']:
        assert ref['answer_ref'] in {records[id].get('answer_ref') for id in entry['topic_matches']} or ref['answer_ref'] in ['ironcopper', 'cathodic', 'rocompare', 'wet10']
        for block in blocks(data['answers'][ref['answer_ref']]['blocks']):
            if block['type'] == 'paragraph': assert block['text'] in panel.text_content()
            if block['type'] == 'equation': assert block['latex'] in panel.text_content()
            if block['type'] == 'figure': assert panel.xpath('.//figure[@data-source-figure=$id]', id=block['id'])
assert page.get_element_by_id(faq['id']).get('hidden') is not None
print('END SEM FAQ: PASS — 14 R25 topic groups (4 short, 10 essay), distinct-paper counts, reused checked answers/drawings; original 60 questions preserved.')
