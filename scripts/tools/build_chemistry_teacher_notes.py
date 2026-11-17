#!/usr/bin/env python3
"""Render the permanent teacher transcript; no PDF or private corpus is needed."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SUBJECT = ROOT / 'college/1-1/chemistry-engineers'
DATA = SUBJECT / 'kb/supplied-notes'
PAGE = 'college/1-1/chemistry-engineers/unit-5-teacher-notes.html'


def build():
    entry = json.loads((DATA / 'unit-5-teacher.json').read_text())
    manifest = json.loads((DATA / 'manifest.json').read_text())
    esc = html.escape
    links = '\n'.join(f'<a href="{PAGE}#{p["id"]}">p.{p["page"]} · {esc(p["title"])}</a>' for p in entry['pages'])
    def render_block(block):
        # Reflow PDF line wraps, retaining separate source list items.
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        output = []
        for line in lines:
            if output and re.match(r'^(?:[•➢❖✓]|[0-9]+[.)])\s', line):
                output.append('<br>')
            elif output:
                output.append(' ')
            output.append(esc(line))
        return ''.join(output)

    sections = []
    for page in entry['pages']:
        notice = ''
        if page['embedded_image_count']:
            notice = '<p class="document-source"><strong>Diagram gap:</strong> This PDF page includes embedded images. Their contents are not transcribed here; captions below are source text.</p>'
        text = page['text']
        body = ''.join(f'<p class="teacher-transcript">{render_block(block)}</p>' for block in text.split('\n\n') if block.strip())
        if not body:
            body = '<p class="document-source">Blank final source page.</p>'
        sections.append(f'<section class="document-page" id="{page["id"]}"><h2>PDF page {page["page"]} · {esc(page["title"])}</h2>{notice}<div data-source-page="{page["page"]}">{body}</div></section>')
    styles = ['variables.css', 'base.css', 'layout.css', 'navbar.css', 'components.css', 'study-ui.css', 'pages/institutional-documents.css', 'pages/teacher-transcript.css']
    css = '\n'.join(f'<link rel="stylesheet" href="styles/new/{s}">' for s in styles)
    source = manifest['sources'][0]
    output = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<base id="site-base" href="/"><script>if(location.hostname.endsWith('github.io')) document.getElementById('site-base').href='/Pankusdesk/';</script>
<title>Unit 5 Teacher Notes · Chemistry · Panku’s Desk</title>
{css}
<script src="scripts/new/navbar.js" defer></script><script src="scripts/new/study-ui.js" defer></script><script src="scripts/new/institutional-documents.js" defer></script>
</head><body><div id="navbar-new"></div>
<main class="page-shell institutional-document" id="document-top">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Panku’s Desk</a> › <a href="college/1-1/chemistry-engineers/index.html">Chemistry</a> › Unit 5 Teacher Notes</nav>
<header><h1>Unit 5 · Teacher Notes</h1><p>Spectroscopic Applications and Advanced Functional Materials</p>
<p>Primary source for Unit 5 answers. Existing Chemistry notes supply information missing from this packet.</p>
<p class="document-source">Native-text transcription. Diagrams and original superscript/subscript layout remain untranscribed. Source claims are preserved and are not automatically verified scientific statements.</p>
<details><summary>Source identity and review notes</summary><p>{esc(source['filename'])} · {source['page_count']} PDF pages</p><p>SHA-256: <code>{source['sha256']}</code></p>
<p>Check source wording carefully for STM constant-height mode (p.3), the deformation/phase statement (pp.13–14), and passive-IR terminology alongside a powered emitter (pp.24–25). The full policy and gaps are recorded in <a href="college/1-1/chemistry-engineers/kb/supplied-notes/manifest.json">the source manifest</a>.</p></details></header>
<div class="document-layout"><aside class="document-sidebar" aria-label="Teacher notes navigation">
<a class="document-back-top" href="{PAGE}#document-top">↑ Back to top</a>
<details class="document-contents" open><summary>Contents · PDF pages</summary><nav aria-label="Teacher packet contents">{links}</nav></details></aside>
<article class="document-body" aria-label="Teacher source transcription">{''.join(sections)}</article></div></main></body></html>
'''
    return output


if __name__ == '__main__':
    (SUBJECT / 'unit-5-teacher-notes.html').write_text(build())
    print('Built Chemistry Unit 5 teacher notes from permanent repository data.')
