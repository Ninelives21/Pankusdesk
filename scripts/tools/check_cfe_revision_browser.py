#!/usr/bin/env python3
"""Browser regression for CFE revision structure, clipping and image placement.

Requires Python Playwright and an installed Chromium browser. Serve the repository
root before running; pass --base-url when the local server uses another port.
"""
import argparse
import shutil
import tempfile
from pathlib import Path
import json,re,urllib.request,hashlib
from playwright.sync_api import sync_playwright
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--base-url',default='http://127.0.0.1:8000')
parser.add_argument('--browser',default=shutil.which('chromium'))
parser.add_argument('--screenshots',type=Path,default=Path(tempfile.gettempdir())/'cfe-revision-review')
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[2];SUB='college/1-1/chemistry-engineers/';OUT=args.screenshots;OUT.mkdir(parents=True,exist_ok=True)
a=json.loads((ROOT/SUB/'revision/unit-2-source-audit.json').read_text());manifest=json.loads((ROOT/SUB/'revision/unit-2-ros-manifest.json').read_text())
assert len(manifest['assets'])==18
assert len({x['image_id'] for x in manifest['assets']})==18
for x in manifest['assets']:
 path=ROOT/SUB/'assets/end-sem/unit-2'/x['output_filename'];assert hashlib.sha256(path.read_bytes()).hexdigest()==x['output_sha256']
assert len(a['questions'])==44 and all('figure_assessment' in q for q in a['questions'])
clean=lambda t:re.sub(r'\s+',' ',t).strip()
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path=args.browser,args=['--no-sandbox']);page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 def cdn(route):
  with urllib.request.urlopen(route.request.url,timeout=30) as r:route.fulfill(status=r.status,body=r.read(),content_type=r.headers.get('Content-Type'))
 page.route('https://cdn.jsdelivr.net/**',cdn)
 for width in [1440,390]:
  page.set_viewport_size(dict(width=width,height=1000));page.goto(args.base_url.rstrip('/')+'/'+SUB+'end-sem-unit-2.html',wait_until='domcontentloaded');page.wait_for_function('document.querySelectorAll("mjx-container").length>0');page.evaluate('async()=>{await MathJax.startup.promise;await MathJax.typesetPromise([]);await document.fonts.ready;await new Promise(requestAnimationFrame)}')
  assert page.locator('.source-nav-group').count()==4  # The question-bank group moved out of Notes.
  note_math_count=page.locator('mjx-container').count()
  note_image_count=page.locator('.source-visual img').count();assert note_image_count==18
  assert page.locator('mjx-merror').count()==0
  for img in page.locator('.source-visual img').all():
   img.evaluate('(i)=>{i.loading="eager";return i.decode()}')
  note_text=page.locator('.end-sem-content').inner_text()
  assert 'Figure pending' not in note_text and 'checks remain pending' not in note_text
  assert 'E(SCE) = +0.2422 V' in note_text
  assert page.locator('img[alt*="Hg/Mercury"],img[alt*="Hg/Mercury" i]').count()>=1 or page.locator('img[alt*="source label error"]').count()>=2
  for img in page.locator('img[src*="e-p007"],img[src*="r-p001-v02"]').all():
   assert 'platinized platinum' in img.locator('xpath=ancestor::figure').text_content()
  for section in page.locator('section[data-source]').all():
   if section.bounding_box()['height']>40:section.screenshot(path=str(OUT/f'{width}-notes-{section.get_attribute("id")}.png'))
  page.goto(args.base_url.rstrip('/')+'/'+SUB+'question-banks.html#unit-2',wait_until='networkidle');page.wait_for_selector('[data-document-ready="true"]');page.wait_for_selector('body[data-bank-ready="true"]')
  assert page.locator('#unit-2').is_visible()
  assert page.locator('#unit-1').is_hidden()
  assert note_math_count+page.locator('#unit-2 mjx-container').count()>20 and page.locator('mjx-merror').count()==0  # Same original math gate, across both routes.
  bank_images=page.locator('#unit-2 .source-visual img');assert note_image_count+bank_images.count()==39
  for img in bank_images.all():img.evaluate('(i)=>{i.loading="eager";return i.decode()}')
  for q in a['questions']:
   card=page.locator('#'+q['id']);assert [clean(x) for x in card.locator('.study-example-question > span').all_inner_texts()]==[clean(x) for x in q['source_question_parts']],q['id']
   card.locator('summary').click();page.evaluate('async()=>{await document.fonts.ready;await new Promise(requestAnimationFrame)}');assert card.locator('.study-solution-label').inner_text().lower()=='pankusdesk answer'
   assess=q['figure_assessment'];expected=len(assess['asset_ids'])+(1 if assess.get('reused_approved_asset') else 0)
   assert card.locator('img').count()==expected,(q['id'],expected)
   if re.search(r'\bpending\b',card.inner_text().lower()):raise AssertionError((q['id'],'stale pending wording'))
   assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),q['id']
   bad=card.locator('p,.answer-part,.answer-part-list,.source-table-scroll,.source-equation,mjx-container').evaluate_all('(xs)=>xs.filter(x=>{if(x.closest("mjx-assistive-mml") || ((x.closest(".source-table-scroll,.source-equation"))&&!x.matches(".source-table-scroll,.source-equation")))return false;const a=x.getBoundingClientRect(),b=x.closest("details").getBoundingClientRect();return a.right>b.right+1||a.left<b.left-1}).map(x=>x.tagName+":"+x.className)')
   assert not bad,(q['id'],bad)
   for horizontal in card.locator('.source-equation,.source-table-scroll').all():
    assert horizontal.evaluate('(x)=>getComputedStyle(x).overflowX==="auto"&&getComputedStyle(x).overflowY==="hidden"'),(q['id'],'wide content must scroll horizontally only')
    if horizontal.evaluate('(x)=>x.scrollWidth>x.clientWidth+1'):
     horizontal.evaluate('(x)=>x.scrollLeft=x.scrollWidth')
     assert horizontal.evaluate('(x)=>x.scrollLeft>0'),(q['id'],'wide content cannot be reached')
     horizontal.evaluate('(x)=>x.scrollLeft=0')
   text_bad=card.evaluate('''x=>{const box=x.getBoundingClientRect(),walker=document.createTreeWalker(x,NodeFilter.SHOW_TEXT),bad=[];let t;while(t=walker.nextNode()){if(!t.textContent.trim()||t.parentElement.closest("mjx-container,.source-table-scroll,.source-equation"))continue;const r=document.createRange();r.selectNodeContents(t);if([...r.getClientRects()].some(a=>a.right>box.right+1||a.left<box.left-1))bad.push(t.textContent)}return bad}''')
   assert not text_bad,(q['id'],text_bad)
   card.screenshot(path=str(OUT/f'{width}-all-{q["id"]}.png'));card.locator('summary').click()
  for key,counts in [('essay-6',[0,1]),('essay-8',[1,1]),('essay-9',[1,1])]:
   card=page.locator('#u2-qa-'+key)
   assert card.locator('.answer-part').evaluate_all('(xs)=>xs.map(x=>x.querySelectorAll("img").length)')==counts
  for id in ['u2-qa-essay-6','u2-qa-essay-7','u2-qa-essay-8','u2-qa-essay-9']:
   card=page.locator('#'+id);card.locator('summary').click();card.screenshot(path=str(OUT/f'{width}-{id}.png'));card.locator('summary').click()
  # Caption is present at every placement of either erroneous source SHE drawing.
  for img in page.locator('#unit-2 img[src*="e-p007"],#unit-2 img[src*="r-p001-v02"]').all():
   assert 'platinized platinum' in img.locator('xpath=ancestor::figure').text_content()
  page.locator('#u2-qa-essay-1 summary').click()
  with page.expect_popup() as popup:page.locator('#u2-qa-essay-1 .source-visual a').click()
  pp=popup.value;pp.wait_for_load_state();assert pp.url.endswith('cfe-u2-e-p002-v01.webp');pp.close()
  page.goto(args.base_url.rstrip('/')+'/'+SUB+'index.html#end-sem-units',wait_until='networkidle');assert page.locator('#end-sem-units .subject-resource-links a').count()==5
  assert 'notes and ros figures' in page.locator('#end-sem-units').inner_text().lower()
  print(width,'PASS: 39 images decoded, 44 original prompts/answers, per-question figure map, correct multipart placement, full-size link, math, source captions and no page overflow')
 assert not errors,errors
 b.close()
print('PASS: 18 asset identities; exact source-part arrays, visible text/panel/math bounds and figure placement for all 44 questions')
