#!/usr/bin/env python3
"""Browser regression checks for the central scroll tracker and shared adapters.

Requires the existing Playwright Python package and Chromium. Serves this checkout
on an automatically assigned loopback port; no persistent server or dependencies.
"""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
from urllib.parse import unquote, urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = '''<!doctype html><html><head><style>
html{scroll-behavior:auto;overflow-anchor:none}body{margin:0;font:16px sans-serif}
aside{position:fixed;left:0;top:0;width:230px}nav{max-height:260px;overflow-y:auto}
nav a{display:block;padding:10px}main{margin-left:250px}main section{border-top:1px solid #ccc}
#one,#two,#hidden-section{min-height:1100px}#growth[open] div{height:1400px}
#end{height:50px}#hidden-section{display:none}.concealed{visibility:hidden}
</style><script src="/scripts/new/navbar.js" defer></script></head><body>
<header><nav><a id="global-link" href="#two" aria-current="page">Site navigation</a></nav></header>
<aside><details class="document-contents" open><summary>Contents</summary><nav id="contents">
<a href="#document-top" class="document-back-top">Back to top</a>
<details id="nested" open><summary><a href="#outer">Unit A</a></summary>
<a id="one-link" href="#one">First</a><a id="two-link" href="#two">Second</a></details>
<a href="#hidden-section">Hidden</a><a id="end-link" href="#end">Last</a>
<a href="?other=1#two">Other query</a><a href="other.html#two">Other page</a>
<a href="https://other.example/#two">External</a><a href="#%E0%A4%A">Malformed fragment</a>
</nav></details></aside><main id="document-top"><section id="outer">
<section id="one"><h1>First</h1><details id="growth"><summary>Long answer</summary><div>Expanded answer</div></details></section>
<section id="two"><h2>Second</h2><p>Long section</p></section></section>
<section id="hidden-section">Hidden content</section><section id="end">Short last section</section></main></body></html>'''


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


def scroll_to(page, identifier, offset=130):
    page.evaluate('''([id,offset]) => {
        const target=document.getElementById(id);
        scrollTo({top:scrollY+target.getBoundingClientRect().top-offset,behavior:'instant'});
    }''', [identifier, offset])


def wait_active(page, identifier):
    page.wait_for_function('''id => [...document.querySelectorAll('[data-section-nav] a.is-current-section')]
        .some(a=>decodeURIComponent(a.hash.slice(1))===id)''', arg=identifier)


def core_checks(browser, origin, width):
    context = browser.new_context(viewport={'width': width, 'height': 900}, ignore_https_errors=True)
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.route('**/__section_nav_fixture.html', lambda route: route.fulfill(body=FIXTURE, content_type='text/html'))
    page.goto(origin + '/__section_nav_fixture.html', wait_until='networkidle')
    page.wait_for_function('Boolean(window.PankuSectionNav)')
    initial_url = page.url
    scroll_to(page, 'one', -450)
    wait_active(page, 'one')
    assert page.url == initial_url, 'Reading must not rewrite URL/history'
    assert page.locator('#global-link').get_attribute('aria-current') == 'page'
    page.locator('#nested').evaluate('(el)=>el.open=false')
    page.locator('.document-contents').evaluate('(el)=>el.open=false')
    scroll_to(page, 'two')
    wait_active(page, 'two')
    assert page.locator('#nested').evaluate('(el)=>el.open'), 'Expand nested navigation group'
    assert not page.locator('.document-contents').evaluate('(el)=>el.open'), 'Do not open mobile Contents'
    expected_scroll = page.evaluate('scrollY')
    page.wait_for_timeout(100)
    assert abs(page.evaluate('scrollY') - expected_scroll) < 1, 'Highlight must not move the reading viewport'
    # Expansion above the reading line changes the current section without user scroll.
    page.locator('#growth').evaluate('(el)=>el.open=true')
    wait_active(page, 'one')
    page.locator('#growth').evaluate('(el)=>el.open=false')
    wait_active(page, 'two')
    # Dynamic renderer output: discover both new links and targets automatically.
    page.evaluate('''() => {
        const target=document.createElement('section');target.id='dynamic';target.style.height='1000px';
        target.textContent='Loaded later';document.querySelector('main').append(target);
        const link=document.createElement('a');link.href='#dynamic';link.textContent='Dynamic';
        document.getElementById('contents').append(link);
    }''')
    scroll_to(page, 'dynamic')
    wait_active(page, 'dynamic')
    assert page.locator('a[href="#hidden-section"]').get_attribute('aria-current') is None
    # A class/style visibility change must remove the old active target.
    page.evaluate("document.getElementById('dynamic').className='concealed'")
    page.wait_for_function("!document.querySelector('a[href=\"#dynamic\"]').hasAttribute('aria-current')")
    page.evaluate("scrollTo({top:document.documentElement.scrollHeight,behavior:'instant'})")
    wait_active(page, 'end')
    # Normal clicks, Back and Forward still navigate. No scroll-driven hash changes.
    page.locator('.document-contents').evaluate('(el)=>el.open=true')
    page.locator('#one-link').click()
    page.wait_for_url('**#one')
    wait_active(page, 'one')
    page.locator('#two-link').click()
    page.wait_for_url('**#two')
    wait_active(page, 'two')
    page.go_back()
    page.wait_for_url('**#one')
    wait_active(page, 'one')
    page.go_forward()
    page.wait_for_url('**#two')
    wait_active(page, 'two')
    assert not errors, errors
    context.close()
    print(f'PASS core {width}px: long/nested/hidden/dynamic sections, resize after expansion, short final section, mobile Contents, URL/history and excluded links', flush=True)


CASES = [
    ('teacher', 'college/1-1/chemistry-engineers/teacher-notes-unit-wise.html', '[data-document-ready="true"]', 'u4-class-test'),
    ('textbook', 'college/1-1/basic-electrical-engineering/unit-1.html', '.unit-toc-link', None),
    ('class notes', 'college/1-1/matrices-calculus/unit-1-class-notes.html', '.class-notes-date-link', None),
    ('supplied notes', 'college/1-1/matrices-calculus/unit-4-supplied-notes.html', '[data-supplied-toc] a', None),
    ('MAC worksheet', 'college/1-1/matrices-calculus/worksheets.html', '[data-worksheet-nav] a', None),
    ('PPS exam', 'college/1-1/programming-problem-solving/unit-4-question-bank.html', '[data-exam-ready="true"]', None),
    ('PPS worksheet', 'college/1-1/programming-problem-solving/worksheet-1.html', '[data-worksheet-ready="true"]', None),
    ('source notes', 'college/1-1/engineering-drawing/projection-of-solids.html', '[data-notes-ready]', None),
    ('Chemistry bank', 'college/1-1/chemistry-engineers/question-banks.html', '[data-bank-ready="true"]', None),
    ('institutional document', 'college/documents/regulations.html', '[data-document-ready="true"]', None),
]


def page_checks(browser, origin, width, screenshots):
    for name, path, ready, target in CASES:
        context = browser.new_context(viewport={'width': width, 'height': 900}, ignore_https_errors=True)
        page = context.new_page()
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(origin + '/' + path, wait_until='networkidle')
        page.wait_for_selector(ready, state="attached")
        page.wait_for_function('Boolean(window.PankuSectionNav)')
        page.wait_for_function("document.querySelector('[data-section-nav]')")
        if not target:
            target = page.evaluate('''() => {
                const ids=[...document.querySelectorAll('[data-section-nav] a')].map(a=>{
                    let url;try{url=new URL(a.getAttribute('href'),location.href)}catch{return ''}
                    const id=a.dataset.indexTarget||decodeURIComponent(url.hash.slice(1));
                    const t=document.getElementById(id);
                    return t&&t.getClientRects().length&&t.offsetHeight>0&&!t.closest('[hidden]')?id:'';
                }).filter(Boolean);return ids[Math.floor(ids.length/2)];
            }''')
        before = page.url
        scroll_to(page, target)
        wait_active(page, target)
        assert page.url == before, name
        assert not errors, (name, errors)
        # Overflow may already exist in a legacy page; the synthetic checks and
        # teacher-page checks gate the shared component's own layout.
        if name == 'teacher':
            assert page.evaluate('document.documentElement.scrollWidth<=innerWidth+1')
            if screenshots:
                screenshots.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(screenshots / f'scroll-nav-teacher-{width}.png'))
        print(f'PASS {name} {width}px: manual scroll selects {target}', flush=True)
        context.close()


def prefix_check(browser):
    context = browser.new_context(viewport={'width': 390, 'height': 900}, ignore_https_errors=True)
    def local(route):
        path = unquote(urlparse(route.request.url).path)
        file = ROOT / path.removeprefix('/Pankusdesk/')
        if path.startswith('/Pankusdesk/') and file.is_file():
            route.fulfill(path=str(file))
        else:
            route.fulfill(status=404, body='Not a local resource')
    context.route('https://ninelives21.github.io/**', local)
    page = context.new_page()
    path = 'college/1-1/chemistry-engineers/teacher-notes-unit-wise.html'
    page.goto('https://ninelives21.github.io/Pankusdesk/' + path, wait_until='networkidle')
    page.wait_for_function('Boolean(window.PankuSectionNav)')
    scroll_to(page, 'u4-class-test')
    wait_active(page, 'u4-class-test')
    assert page.locator('base').get_attribute('href') == '/Pankusdesk/'
    print('PASS: GitHub Pages /Pankusdesk/ bootstrap and same-document matching', flush=True)
    context.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', default='/usr/bin/chromium')
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    pages = []
    for path in ROOT.rglob('*.html'):
        if '.git' in path.parts or '_vercel_site' in path.parts:
            continue
        text = path.read_text(errors='replace')
        if '<html' not in text.lower() or 'http-equiv="refresh"' in text.lower():
            continue
        assert 'scripts/new/navbar.js' in text, f'Missing shared bootstrap: {path}'
        assert 'styles/new/navbar.css' in text, f'Missing shared current-section style: {path}'
        pages.append(path)
    print(f'PASS: all {len(pages)} full browsing pages load the central bootstrap and stylesheet', flush=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(executable_path=args.browser, headless=True, args=['--no-sandbox'])
            for width in (1440, 390):
                core_checks(browser, f'http://127.0.0.1:{server.server_port}', width)
                page_checks(browser, f'http://127.0.0.1:{server.server_port}', width, args.screenshots)
            prefix_check(browser)
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    main()
