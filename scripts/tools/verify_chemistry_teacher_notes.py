#!/usr/bin/env python3
"""Verify durable source integrity and compare with the uploaded PDF when supplied."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess

from build_chemistry_teacher_notes import build

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/chemistry-engineers'
DATA = SUBJECT / 'kb/supplied-notes'


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


class TranscriptParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.pages = {}
        self.page = None
        self.in_paragraph = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))
        if 'data-source-page' in attrs:
            self.page = int(attrs['data-source-page'])
            self.pages[self.page] = []
        if tag == 'p' and attrs.get('class') == 'teacher-transcript':
            self.in_paragraph = True

    def handle_endtag(self, tag):
        if tag == 'p':
            self.in_paragraph = False
        if tag == 'div':
            self.page = None

    def handle_data(self, data):
        if self.in_paragraph and self.page is not None:
            self.pages[self.page].append(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-pdf', type=Path)
    args = parser.parse_args()
    entry = json.loads((DATA / 'unit-5-teacher.json').read_text())
    manifest = json.loads((DATA / 'manifest.json').read_text())
    source = manifest['sources'][0]
    assert source['id'] == entry['source_id'] == manifest['answer_policy']['primary_source_id']
    assert source['page_count'] == 28
    assert [p['page'] for p in entry['pages']] == list(range(1, 29))
    assert len(manifest['syllabus_mapping']) == 7
    for page in entry['pages']:
        assert digest(page['text']) == page['text_sha256'], page['page']
        assert not any(ord(ch) < 32 and ch not in '\n\t' for ch in page['text'])
        assert page['embedded_image_count'] >= 0
    assert not entry['pages'][-1]['text']
    for mapping in manifest['syllabus_mapping']:
        assert set(mapping['pdf_pages']) <= set(range(1, 29))
    assert manifest['answer_policy']['fallback_url'] == 'https://ninelives21.github.io/Pankusdesk/college/1-1/chemistry-engineers/index.html'
    assert source['id'] in (ROOT / 'AGENTS.md').read_text() or 'unit-5-teacher.json' in (ROOT / 'AGENTS.md').read_text()
    assert 'supplied-notes/manifest.json' in (SUBJECT / 'kb/README.md').read_text()
    rendered = (SUBJECT / 'unit-5-teacher-notes.html').read_text()
    assert rendered == build(), 'Regenerate HTML after data changes'
    html = TranscriptParser()
    html.feed(rendered)
    assert len(html.ids) == len(set(html.ids))
    for page in entry['pages']:
        actual = ' '.join(html.pages[page['page']])
        assert re.sub(r'\s+', '', actual) == re.sub(r'\s+', '', page['text']), page['page']
    for link in html.links:
        if link.startswith(('http:', 'https:')):
            continue
        path, _, anchor = link.partition('#')
        assert (ROOT / path).is_file(), path
        if anchor:
            assert anchor in html.ids, anchor
    resources = json.loads((SUBJECT / 'index-resources.json').read_text())
    assert resources['notes'][0]['href'] == 'unit-5-teacher-notes.html'
    if args.source_pdf:
        pdf = args.source_pdf
        assert hashlib.sha256(pdf.read_bytes()).hexdigest() == source['sha256']
        assert pdf.stat().st_size == source['bytes']
        raw = subprocess.check_output(['pdftotext', '-layout', '-enc', 'UTF-8', str(pdf), '-']).decode()
        pages = raw.split('\f')
        assert not pages.pop().strip()
        assert len(pages) == 28
        for original, saved in zip(pages, entry['pages']):
            normalized = '\n'.join(line.rstrip() for line in original.splitlines()).strip()
            assert normalized == saved['text'], saved['page']
        print('PASS: all 28 page texts match uploaded PDF extraction; binary checksum and size match.')
    else:
        print('Source PDF comparison not run; pass --source-pdf to verify the original upload.')
    print('CHEMISTRY TEACHER NOTES VERIFY: PASS — page integrity, rendered text, anchors, policy, source identity and index link.')


if __name__ == '__main__':
    main()
