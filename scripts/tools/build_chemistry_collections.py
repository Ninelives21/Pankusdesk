#!/usr/bin/env python3
"""Build Chemistry collection/inventory and question pages from source records.
Build labelled authored answers; retain source wording, provenance and existing figures.
"""
from collections import defaultdict
from pathlib import Path
import html
import json
import re
from html.parser import HTMLParser
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[2]
S=ROOT/'college/1-1/chemistry-engineers';R=S/'revision'
E=html.escape
PREFIX='college/1-1/chemistry-engineers/'
TITLES={1:'Water and Its Treatment',2:'Electrochemistry and Corrosion',3:'Energy Sources and Battery Technology',4:'Polymers',5:'Spectroscopic Applications and Advanced Functional Materials'}
@lru_cache(maxsize=None)
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

@lru_cache(maxsize=None)
def existing_solution(id):
 # Parse the retained answer boundary without duplicating stable IDs.
 raw=(R/'question-sections/unit-1.html').read_text()
 class AnswerParser(HTMLParser):
  def __init__(self):super().__init__(convert_charrefs=False);self.active=False;self.depth=0;self.done=False;self.out=[];self.target=False
  def handle_starttag(self,tag,attrs):
   if tag=='details' and dict(attrs).get('id')==id:self.target=True
   if self.target and not self.done:
    if self.active:
     self.depth+=tag=='div';self.out.append('<'+tag+''.join(' '+k+'="'+E(v or '')+'"' for k,v in attrs if k!='id')+'>')
    elif tag=='div' and 'study-example-solution' in dict(attrs).get('class',''):self.active=True;self.depth=1
  def handle_endtag(self,tag):
   if self.active and not self.done:
    if tag=='div':self.depth-=1
    if self.depth==0:self.done=True;self.active=False
    else:self.out.append('</'+tag+'>')
  def handle_data(self,data):
   if self.active and not self.done:self.out.append(E(data))
  def handle_entityref(self,name):
   if self.active and not self.done:self.out.append('&'+name+';')
  def handle_charref(self,name):
   if self.active and not self.done:self.out.append('&#'+name+';')
 parser=AnswerParser();parser.feed(raw);assert parser.done,id;return ''.join(parser.out)

def answer_html(q,solutions):
 a=solutions['answers'][q['id']];parts=[]
 if a.get('source_discrepancy'):parts.append('<aside class="study-mismatch-note" role="note"><div class="study-mismatch-note-label">Source discrepancy</div><p>'+E(a['source_discrepancy'])+'</p></aside>')
 for id in ([a['existing_answer_id']] if a.get('existing_answer_id') else a.get('existing_answer_ids',[])):parts.append(existing_solution(id))
 for part in a.get('subpart_answers',[]):parts.append(f'<section class="study-solution-part"><h4>({E(part["label"])}) {E(part["title"])}</h4><p>{E(part["text"])}</p></section>')
 for i,key in enumerate([] if a.get('subpart_answers') else a.get('modules',[])):
  m=solutions['modules'][key];selected=a.get('paragraph_selection',{}).get(key);paras=[m['paragraphs'][n] for n in selected] if selected is not None else m['paragraphs'];paragraphs='<p>'+E(a['direct_answer'])+'</p>' if a.get('direct_answer') else ''.join('<p>'+E(p)+'</p>' for p in paras)
  ref=m.get('notes_ref');source=''
  if ref:source=f'<p class="document-source"><a href="{anchor(notes(ref["unit"]),ref["anchor"])}">Related college notes: {E(m["title"])}</a></p>'
  inventory=read('source-inventory.json')['sources'];lookup={x['id']:x for x in inventory};lookup.update({x['source_id']:x for x in inventory if x.get('source_id')})
  citations=[]
  for citation in m['source_refs']:
   record=lookup[citation['source_id']];pages=citation.get('pages',[]);citations.append('<a href="'+anchor('college-notes.html',record['id'])+'">'+E(record['filename'])+'</a>'+(' · pages '+', '.join(map(str,pages)) if pages else ''))
  for citation in m.get('textbook_refs',[]):citations.append(E(citation['filename'])+' · printed page '+str(citation['printed_page'])+' (private supplied textbook capture)')
  source+='<p class="document-source">Answer basis: '+'; '.join(citations)+'.</p>'
  fallback='<p class="source-notes-editorial">'+E(m['fallback_note'])+'</p>' if m.get('fallback_note') else ''
  partlabel=f'({chr(97+i)}) ' if len(a.get('modules',[]))>1 and re.search(r'(?<!\w)[ab]\)',q['original_prompt']) else ''
  parts.append(f'<section class="study-solution-part"><h4>{partlabel}{E(m["title"])}</h4>{paragraphs}{fallback}{source}</section>')
 if a.get('diagram_required') and not any('<img ' in p for p in parts):parts.append('<p class="source-notes-editorial"><strong>Diagram requirement:</strong> the question requests a drawing. Text and equations are supplied here; any existing linked drawing is retained. A new checked drawing has not been produced under the current figure-production freeze.</p>')
 return '<div class="study-solution-label">PankusDesk-authored answer</div>'+''.join(parts)

def main():
 inventory=read('source-inventory.json');byid={s['id']:s for s in inventory['sources']};additions=read('college-notes-additions.json')['additions'];bank=read('question-bank-pending.json');solutions=read('question-bank-solutions.json')
 # Unit-oriented entry point; original pages and their figures stay at their stable URLs.
 nav='';body=''
 for u,title in TITLES.items():
  nav+=f'<a href="{anchor("college-notes.html",f"unit-{u}")}">Unit {u} · {E(title)}</a>'
  count=sum(s['unit']==u for s in inventory['sources']);extra=[a for a in additions if a['unit']==u]
  text=f'<p><a class="primary-button" href="{PREFIX}{notes(u)}">Read Unit {u} notes →</a></p><p>{count} distinct source files inventoried. Existing notes, source transcripts, figures and corrections are retained.</p>'
  text+='<p><strong>Review status:</strong> '+('Existing notes retained; worked answers are available separately in the question bank.' if u<3 else 'Selected R25 notes remain draft. Required figures and textbook verification are still pending.')+'</p>'
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
 # One rendered copy of every bank, with five unit filters and one consolidated view.
 groups=defaultdict(list)
 for q in bank['questions']+bank.get('additional_questions',[]):groups[q['source_id']].append(q)
 source_sets={s['source_id']:s for s in bank['source_question_sets']}
 units={u:[] for u in TITLES}
 for u in [1,2]:
  fragment=(R/f'question-sections/unit-{u}.html').read_text()
  units[u].append('<div class="relocated-question-sections">'+fragment+'</div>')
 for sid,qs in groups.items():
  source=source_sets.get(sid,{});name=source.get('file',qs[0]['source_filename']);unit=int(source.get('unit',qs[0].get('r25_unit')));id='bank-'+sid.lower()
  content=f'<p>{len(qs)} recorded question occurrences. Numbering restarts within each source set; overlapping sheets remain separate.</p><p>Open a question to read its PankusDesk-authored answer. Source wording and numbering are retained; older-syllabus material is labelled separately.</p>'
  for q in qs:
   number=q.get('source_question_number');label=f'{q.get("source_set","Question").replace("_"," ").title()} · '+(f'Q{number}' if number is not None else 'Unnumbered prompt')
   prompt=E(q['original_prompt']);prompt=re.sub(r'(?<!\w)(\([a-h]\)|[a-h]\)|\([iv]{1,3}\)|[iv]{1,3}\))(?=\s)',r'<br><strong>\1</strong>',prompt)
   prompt=re.sub(r'(?<![\w(])([1-3]\))(?=\s)',r'<br><strong>\1</strong>',prompt)
   page=q.get('source_page_start');scope=q.get('selection','pending').replace('_',' ')
   scope_note='<p class="document-source">Older-syllabus / supporting question; retained from the supplied collection.</p>' if q.get('selection') in ['out_of_scope','supporting','mixed_parts'] else ''
   mismatch=' has-math-mismatch' if solutions['answers'][q['id']].get('source_discrepancy') else ''
   content+=f'<details class="study-accordion-item study-accordion-item--example collection-question{mismatch}" id="{E(q["id"])}"><summary><span class="study-example-summary-copy"><span class="study-example-title">{E(label)}</span><span class="study-example-question">{prompt}</span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{answer_html(q,solutions)}{scope_note}<p class="document-source">Question source: {E(name)}'+(f' · PDF page {page}' if page else '')+'</p></div></details>'

  units[unit].append(f'<section class="bank-source-group" id="{E(id)}"><h3>{E(name)}</h3>{content}</section>')
 qnav=''.join(f'<a href="{anchor("question-banks.html",f"unit-{u}")}" data-bank-unit="{u}">Unit {u} · {E(title)}</a>' for u,title in TITLES.items())+f'<a href="{anchor("question-banks.html","all-units")}" data-bank-unit="all">Consolidated · All units</a>'
 qbody='<div id="all-units" class="bank-view-intro"><span id="existing-answers"></span><span id="source-questions-pending"></span><p id="bank-view-status" role="status">Consolidated view · all five units</p><p>College question banks and standalone practice sheets, not authenticated previous-year papers. PankusDesk answers follow the supplied notes and are not lecturer-approved keys. Source discrepancies and any outstanding drawing requirements are explicit. Original numbering and both Unit V source variants are retained.</p></div>'
 for u,title in TITLES.items():qbody+=f'<section class="document-page bank-unit" id="unit-{u}" data-bank-unit-section="{u}"><h2>Unit {u} · {E(title)}</h2><p><a href="{PREFIX}{notes(u)}">Read Unit {u} notes →</a></p>'+''.join(units[u])+'</section>'
 question_html=shell('question-banks.html','Unit-wise Question Bank & Solutions','Choose one unit or the consolidated view. Supplied questions and worked answers, grouped by unit and original source.',qnav,qbody)
 for css in ['pages/end-sem-notes','pages/source-notes','pages/practice']:question_html=question_html.replace('</head>',f'<link rel="stylesheet" href="styles/new/{css}.css">\n</head>')
 question_html=question_html.replace('<body>','<body data-question-bank="true">').replace('</head>','<script src="scripts/new/question-bank-navigation.js" defer></script>\n</head>')
 (S/'question-banks.html').write_text(question_html)
 # Integrate labelled explanations immediately after their relevant topic heading.
 for u in TITLES:
  p=S/notes(u);text=p.read_text();text=re.sub(r'<!-- COLLEGE-ADDITION-START -->.*?<!-- COLLEGE-ADDITION-END -->','',text,flags=re.S)
  text=re.sub(r'<!-- COLLEGE-COLLECTION-START -->.*?<!-- COLLEGE-COLLECTION-END -->','',text,flags=re.S)
  for a in [a for a in additions if a['unit']==u]:
   s=byid[a['source_id']];block='<!-- COLLEGE-ADDITION-START -->'+f'<details class="study-tip" id="{a["id"]}"><summary><span class="study-tip-summary-copy"><span class="study-tip-label">Additional explanation · PankusDesk</span><span class="study-tip-summary-title">{E(a["title"])}</span></span><span class="study-tip-toggle" aria-hidden="true">+</span></summary><div class="study-tip-content">'+''.join(f'<p>{E(p)}</p>' for p in a['paragraphs'])+f'<p class="document-source">Based on {E(s["filename"])} · PDF pages {", ".join(map(str,a["pages"]))}. <a href="{anchor("college-notes.html",s["id"])}">Source and remaining checks</a>. Existing answers and figures are unchanged.</p></div></details>'+'<!-- COLLEGE-ADDITION-END -->'
   start=text.index(f'id="{a["anchor"]}"');match=re.search(r'</h[23]>',text[start:]);assert match,(u,a['anchor']);at=start+match.end();text=text[:at]+block+text[at:]
  banner='<!-- COLLEGE-COLLECTION-START -->'+f'<aside class="source-notes-editorial"><strong>College &amp; Senior Notes · R25 Unit {u}.</strong> <a href="{PREFIX}college-notes.html#unit-{u}">All units, source inventory and printing guide</a> · <a href="{PREFIX}question-banks.html">Question collections</a>. Existing source text, figures and documented corrections are preserved. Additional explanations and authored question-bank answers are labelled separately. Text extraction and drawing verification have separate audit records.</aside>'+'<!-- COLLEGE-COLLECTION-END -->'
  marker=re.search(r'<(?:div|article) class="end-sem-content">',text);assert marker;text=text[:marker.end()]+banner+text[marker.end():];text=text.replace('Questions are saved separately for a future question bank.','Question collections are listed separately; worked answers are available in the question bank.').replace('worked solutions remain pending.','worked answers are available in the question bank.').replace('The supplied questions have been retained for a future question bank. They have not been presented as textbook exercises, PYQs or verified solutions.','The supplied questions and PankusDesk-authored answers are in the Unit-wise Question Bank &amp; Solutions collection. They are not authenticated PYQs or lecturer-approved answers.').replace('Questions are saved for a future question bank; they are not presented here as textbook exercises, PYQs or verified solutions.','Questions and PankusDesk-authored answers are available in the separate question bank; they are not authenticated PYQs or lecturer-approved solutions.');p.write_text(text)
 print(f'Built collection for {len(inventory["sources"])} files, {len(groups)} question collections / {len(bank['questions'])+len(bank.get('additional_questions',[]))} answered prompts and {len(additions)} labelled explanations.')
if __name__=='__main__':main()
