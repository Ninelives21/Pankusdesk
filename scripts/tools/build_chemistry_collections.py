#!/usr/bin/env python3
"""Build Chemistry collection/inventory and question pages from source records.
No source binaries are required; no source solutions are promoted to checked answers.
"""
from collections import defaultdict
from pathlib import Path
import html
import json
import re
ROOT=Path(__file__).resolve().parents[2]
S=ROOT/'college/1-1/chemistry-engineers';R=S/'revision'
E=html.escape
PREFIX='college/1-1/chemistry-engineers/'
TITLES={1:'Water and Its Treatment',2:'Electrochemistry and Corrosion',3:'Energy Sources and Battery Technology',4:'Polymers',5:'Spectroscopic Applications and Advanced Functional Materials'}
def read(name):return json.loads((R/name).read_text())
def notes(unit):return 'end-sem-notes.html' if unit==1 else f'end-sem-unit-{unit}.html'
def anchor(path,id):return E(PREFIX+path+'#'+id)
def shell(path,title,intro,nav,body):
 css=''.join(f'<link rel="stylesheet" href="styles/new/{name}.css">' for name in ['variables','base','layout','navbar','components','study-ui','pages/institutional-documents','pages/notes-collections'])
 return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<base id="site-base" href="/"><script>if(location.hostname.endsWith('github.io')) document.getElementById('site-base').href='/Pankusdesk/';</script><title>{E(title)} · Chemistry · Panku’s Desk</title>{css}
<script src="scripts/new/navbar.js" defer></script><script src="scripts/new/study-ui.js" defer></script><script src="scripts/new/institutional-documents.js" defer></script></head><body><div id="navbar-new"></div>
<main class="page-shell institutional-document notes-collection" id="document-top"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Panku’s Desk</a> › <a href="{PREFIX}index.html">Chemistry</a> › {E(title)}</nav><header><h1>{E(title)}</h1><p>{E(intro)}</p></header>
<div class="document-layout"><aside class="document-sidebar" aria-label="Collection navigation"><a class="document-back-top" href="{PREFIX}{path}#document-top">↑ Back to top</a><details class="document-contents" open><summary>Contents</summary><nav aria-label="Collection contents">{nav}</nav></details></aside><article class="document-body">{body}</article></div></main></body></html>\n'''
def section(id,title,body):return f'<section class="document-page" id="{E(id)}"><h2>{E(title)}</h2>{body}</section>\n'
def main():
 inventory=read('source-inventory.json');byid={s['id']:s for s in inventory['sources']};additions=read('college-notes-additions.json')['additions'];bank=read('question-bank-pending.json')
 # Unit-oriented entry point; original pages and their figures stay at their stable URLs.
 nav='';body=''
 for u,title in TITLES.items():
  nav+=f'<a href="{anchor("college-notes.html",f"unit-{u}")}">Unit {u} · {E(title)}</a>'
  count=sum(s['unit']==u for s in inventory['sources']);extra=[a for a in additions if a['unit']==u]
  text=f'<p><a class="primary-button" href="{PREFIX}{notes(u)}">Read Unit {u} notes →</a></p><p>{count} distinct source files inventoried. Existing notes, source transcripts, figures and corrections are retained.</p>'
  text+='<p><strong>Review status:</strong> '+('Existing notes and worked-answer pages retained; new selections are labelled separately.' if u<3 else 'Selected R25 notes remain draft. Required figures and textbook verification are still pending.')+'</p>'
  if extra:text+='<p>Selected additions:</p><ul>'+''.join(f'<li><a href="{anchor(notes(u),a["id"])}">{E(a["title"])}</a></li>' for a in extra)+'</ul>'
  else:text+='<p>Re-uploaded sources reconcile to existing selections. No unsupported extra prose is added just to create another version.</p>'
  text+=f'<p><a href="{anchor("college-notes.html",f"sources-{u}")}">Inspect source inventory and remaining work →</a> · <a href="{PREFIX}question-banks.html">Question collections →</a></p>'
  body+=section(f'unit-{u}',f'Unit {u} · {title}',text)
 nav+=f'<a href="{anchor("college-notes.html","printing")}">Printing and scope</a>'
 body+=section('printing','Printing and scope','<p>Start with the R25 unit notes linked above and use your browser’s Print command. Source inventories and older-syllabus extras are not additional compulsory reading. Select topics before printing a lengthy reference collection.</p><p>Supporting sources contribute only the selections explicitly cited. “Held” means inventoried, not fully transcribed or academically verified. Raw PDFs, PPTs and private photographs are not published. No new technical drawings are produced in this consolidation.</p><p>Authoring and source qualifications remain visible on the notes pages. These are supplied senior/college materials; lecturer approval is not inferred. Textbook Notes remain a separate collection on the Chemistry index.</p>')
 for u in TITLES:
  nav+=f'<a href="{anchor("college-notes.html",f"sources-{u}")}">Unit {u} source inventory</a>'
  rows=[]
  for s in inventory['sources']:
   if s['unit']!=u:continue
   aliases='<ul>'+''.join(f'<li>{E(a["filename"])}'+(f' · {E(a["archive"])}' if a['archive'] else '')+'</li>' for a in s['aliases'])+'</ul>'
   used=s.get('used_pages');detail=f'<p>Selected pages: {", ".join(map(str,used))}.</p>' if used else ''
   for at in s.get('incorporated_at',[]):detail+=f'<p><a href="{anchor(at["page"],at["anchor"])}">Read selected explanation</a></p>'
   rows.append(f'<tr id="{E(s["id"])}"><td><strong>{E(s["filename"])}</strong><br>{s["pages_or_slides"] or "—"} pages/slides<details><summary>Aliases and source identity</summary>{aliases}<p>SHA-256: <code>{E(s["sha256"])}</code></p></details></td><td>{E(s["status"].replace("_"," "))}<p>{E(s.get("review_state",""))}</p></td><td>{E(s.get("note",""))}{detail}</td></tr>')
  body+=section(f'sources-{u}',f'Unit {u} · source inventory',f'<div class="document-table collection-inventory"><table><caption>Source identities are retained even when their teaching content is duplicated or held for review.</caption><thead><tr><th scope="col">Source</th><th scope="col">Treatment</th><th scope="col">Selection / remaining work</th></tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>')
 (S/'college-notes.html').write_text(shell('college-notes.html','College & Senior Notes','R25 notes for all five units, selected additions, source inventory and printing guidance.',nav,body))
 # Question sheets remain independent collections; do not render unverified source answers.
 groups=defaultdict(list)
 for q in bank['questions']:groups[q['source_id']].append(q)
 sources={s['source_id']:s for s in bank['source_question_sets']}
 qnav=f'<a href="{anchor("question-banks.html","existing-answers")}">Existing answers · Units I–II</a>';qbody=section('existing-answers','Existing worked-answer collections',f'<ul><li><a href="{PREFIX}end-sem-notes.html#qa-short-questions">Unit I · 24 short and 12 essay questions</a></li><li><a href="{PREFIX}end-sem-notes.html#water-numericals">Unit I · four hardness problems</a></li><li><a href="{PREFIX}end-sem-unit-2.html#u2-qa-short">Unit II · 34 short, 9 essay and one unnumbered prompt</a></li></ul><p>Existing PankusDesk-authored answers, source corrections and figures remain on their original pages. No lecturer-approved answer key has been supplied.</p>')
 for sid,qs in groups.items():
  source=sources.get(sid,{});name=source.get('file',qs[0]['source_filename']);unit=source.get('unit',qs[0].get('r25_unit'));id='bank-'+sid.lower();qnav+=f'<a href="{anchor("question-banks.html",id)}">Unit {unit} · {E(name)}</a>'
  content=f'<p>{len(qs)} recorded question occurrences. Original numbering restarts within each source set. Overlapping sheets remain separate; the 25-question and 22-question Unit V variants both remain available.</p><p><strong>Questions only:</strong> worked solutions are not yet checked for these collections. Printed model answers are not being presented as verified solutions.</p>'
  for q in qs:
   number=q.get('source_question_number');label=f'{q.get("source_set","Question").replace("_"," ")} · '+(f'Q{number}' if number is not None else 'Unnumbered prompt')
   prompt=E(q['original_prompt'])
   # Keep explicit source subpart labels on separate lines; do not alter wording.
   prompt=re.sub(r'(?<!\w)(\([a-h]\)|\([iv]{1,3}\))(?=\s)',r'<br><strong>\1</strong>',prompt)
   page=q.get('source_page_start');scope=q.get('selection','pending').replace('_',' ')
   content+=f'<article class="collection-question" id="{E(q["id"])}"><h3>{E(label)}</h3><p class="collection-prompt">{prompt}</p><p class="collection-status">Scope: {E(scope)}. {E(q.get("selection_reason",""))}</p><p class="document-source">{E(name)}'+(f' · PDF page {page}' if page else '')+'</p></article>'
  qbody+=section(id,f'Unit {unit} · {name}',content)
 # Keep untranscribed embedded sheets visible as source collections, without exposing OCR marked not-for-display.
 pending=[(1,'Water and its Treatment_notes.pdf','23–24'),(1,'Water and Its Treatment (class on 07-02-2026) (1).pdf','35–37'),(1,'02 Boiler Troubles & Electro Chemistry.pdf','64–69'),(3,'Unit_3_Notes.pdf','22–23'),(4,'3  Polymer Examples.pdf','33–34')]
 qnav+=f'<a href="{anchor("question-banks.html","source-questions-pending")}">Additional embedded question collections</a>'
 text='<p>These source collections have been identified but are not certified as a complete question transcription. Unverified OCR is not displayed as checked question wording. No collection is silently discarded.</p><ul>'
 for u,name,pages in pending:
  source=next((s for s in inventory['sources'] if s['unit']==u and s['filename']==name),None)
  text+=f'<li>Unit {u} · {E(name)} · source pages {E(pages)} · transcription/duplicate reconciliation pending'+(f' · <a href="{anchor("college-notes.html",source["id"])}">Source record</a>' if source else '')+'</li>'
 qbody+=section('source-questions-pending','Additional embedded question collections',text+'</ul>')
 (S/'question-banks.html').write_text(shell('question-banks.html','College Question Banks','Each supplied collection retains its source identity, numbering and R25 scope. Existing answers and pending solutions are distinguished.',qnav,qbody))
 # Integrate labelled explanations immediately after their relevant topic heading.
 for u in TITLES:
  p=S/notes(u);text=p.read_text();text=re.sub(r'<!-- COLLEGE-ADDITION-START -->.*?<!-- COLLEGE-ADDITION-END -->','',text,flags=re.S)
  text=re.sub(r'<!-- COLLEGE-COLLECTION-START -->.*?<!-- COLLEGE-COLLECTION-END -->','',text,flags=re.S)
  for a in [a for a in additions if a['unit']==u]:
   s=byid[a['source_id']];block='<!-- COLLEGE-ADDITION-START -->'+f'<details class="study-tip" id="{a["id"]}"><summary><span class="study-tip-summary-copy"><span class="study-tip-label">Additional explanation · PankusDesk</span><span class="study-tip-summary-title">{E(a["title"])}</span></span><span class="study-tip-toggle" aria-hidden="true">+</span></summary><div class="study-tip-content">'+''.join(f'<p>{E(p)}</p>' for p in a['paragraphs'])+f'<p class="document-source">Based on {E(s["filename"])} · PDF pages {", ".join(map(str,a["pages"]))}. <a href="{anchor("college-notes.html",s["id"])}">Source and remaining checks</a>. Existing answers and figures are unchanged.</p></div></details>'+'<!-- COLLEGE-ADDITION-END -->'
   start=text.index(f'id="{a["anchor"]}"');match=re.search(r'</h[23]>',text[start:]);assert match,(u,a['anchor']);at=start+match.end();text=text[:at]+block+text[at:]
  banner='<!-- COLLEGE-COLLECTION-START -->'+f'<aside class="source-notes-editorial"><strong>College &amp; Senior Notes · R25 Unit {u}.</strong> <a href="{PREFIX}college-notes.html#unit-{u}">All units, source inventory and printing guide</a> · <a href="{PREFIX}question-banks.html">Question collections</a>. Existing source text, figures and documented corrections are preserved. Additional explanations are labelled separately; pending source reviews do not imply completed ingestion.</aside>'+'<!-- COLLEGE-COLLECTION-END -->'
  marker=re.search(r'<(?:div|article) class="end-sem-content">',text);assert marker;text=text[:marker.end()]+banner+text[marker.end():];text=text.replace('Questions are saved separately for a future question bank.','Question collections are listed separately; worked solutions remain pending.');p.write_text(text)
 print(f'Built collection for {len(inventory["sources"])} files, {len(groups)} question collections / {len(bank["questions"])} recorded prompts and {len(additions)} labelled explanations.')
if __name__=='__main__':main()
