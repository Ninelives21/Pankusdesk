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


def handout_figure(id):
 figures={f['id']:f for f in read('source-figures.json')['figures']};f=figures[id]
 return f'<figure class="study-figure" data-source-figure="{E(id)}"><a href="{E(f["asset"])}" target="_blank" rel="noopener"><img src="{E(f["asset"])}" alt="{E(f["alt"])}" width="{f["width"]}" height="{f["height"]}" loading="lazy" decoding="async"></a><figcaption><strong>{E(f["title"])}.</strong> {E(f["caption"])} <span class="document-source">{E(f["source_filename"])} · PDF p.{f["source_pdf_page"]}. Select image to view full size.</span></figcaption></figure>'

def answer_figure_ids(q,a,key):
 # Short definitions keep their focused answer. Long questions use the relevant module figures.
 if q.get('source_set') not in ['essay','long','model']:return []
 return [f['id'] for f in read('source-figures.json')['figures'] if key in f['modules']]

def answer_html(q,solutions):
 a=solutions['answers'][q['id']];parts=[]
 if a.get('source_discrepancy'):parts.append('<aside class="study-mismatch-note" role="note"><div class="study-mismatch-note-label">Source discrepancy</div><p>'+E(a['source_discrepancy'])+'</p></aside>')
 for id in ([a['existing_answer_id']] if a.get('existing_answer_id') else a.get('existing_answer_ids',[])):parts.append(existing_solution(id))
 for part in a.get('subpart_answers',[]):
  illustrations=''.join(handout_figure(id) for id in part.get('figure_ids',[]))
  parts.append(f'<section class="study-solution-part"><h4>({E(part["label"])}) {E(part["title"])}</h4><p>{E(part["text"])}</p>{illustrations}</section>')
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
  illustrations=''.join(handout_figure(id) for id in answer_figure_ids(q,a,key))
  parts.append(f'<section class="study-solution-part"><h4>{partlabel}{E(m["title"])}</h4>{paragraphs}{illustrations}{fallback}{source}</section>')
 if a.get('diagram_required') and not any('<img ' in p for p in parts):
  gap=next((g for g in read('source-figures.json')['source_gaps'] if q['id'] in g['question_ids']),None)
  assert gap,('Unaccounted required diagram',q['id'])
  parts.append('<p class="source-notes-editorial"><strong>Source drawing gap:</strong> '+E(gap['student_note'])+'</p>')

 return '<div class="study-solution-label">PankusDesk-authored answer</div>'+''.join(parts)

def main():
 inventory=read('source-inventory.json');byid={s['id']:s for s in inventory['sources']};additions=read('college-notes-additions.json')['additions'];bank=read('question-bank-pending.json');solutions=read('question-bank-solutions.json')
 # Unit-oriented entry point; original pages and their figures stay at their stable URLs.
 nav='';body=''
 for u,title in TITLES.items():
  nav+=f'<a href="{anchor("college-notes.html",f"unit-{u}")}">Unit {u} · {E(title)}</a>'
  count=sum(s['unit']==u for s in inventory['sources']);extra=[a for a in additions if a['unit']==u]
  text=f'<p><a class="primary-button" href="{PREFIX}{notes(u)}">Read Unit {u} notes →</a></p><p>{count} distinct source files inventoried. Existing notes, source transcripts, figures and corrections are retained.</p>'
  text+='<p><strong>Review status:</strong> '+('Existing notes retained; worked answers are available separately in the question bank.' if u<3 else 'Selected R25 notes remain draft. Approved source diagrams accompany the relevant topics; other figure gaps and textbook verification remain explicit.')+'</p>'
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
 from build_chemistry_question_bank import build_question_bank
 build_question_bank()
 # Integrate labelled explanations immediately after their relevant topic heading.
 for u in TITLES:
  p=S/notes(u);text=p.read_text();text=re.sub(r'<!-- COLLEGE-ADDITION-START -->.*?<!-- COLLEGE-ADDITION-END -->','',text,flags=re.S)
  text=re.sub(r'<!-- COLLEGE-COLLECTION-START -->.*?<!-- COLLEGE-COLLECTION-END -->','',text,flags=re.S)
  text=re.sub(r'<!-- HANDOUT-FIGURES-START -->.*?<!-- HANDOUT-FIGURES-END -->','',text,flags=re.S)
  figures_by_anchor=defaultdict(list)
  for figure in read('source-figures.json')['figures']:
   if figure.get('notes_anchor') and byid[figure['source_id']]['unit']==u:figures_by_anchor[figure['notes_anchor']].append(figure['id'])
  for target,figure_ids in figures_by_anchor.items():
   block='<!-- HANDOUT-FIGURES-START -->'+''.join(handout_figure(id) for id in figure_ids)+'<!-- HANDOUT-FIGURES-END -->'
   start=text.index('id="'+target+'"');end=text.index('</section>',start);text=text[:end]+block+text[end:]
  for a in [a for a in additions if a['unit']==u]:
   s=byid[a['source_id']];block='<!-- COLLEGE-ADDITION-START -->'+f'<details class="study-tip" id="{a["id"]}"><summary><span class="study-tip-summary-copy"><span class="study-tip-label">Additional explanation · PankusDesk</span><span class="study-tip-summary-title">{E(a["title"])}</span></span><span class="study-tip-toggle" aria-hidden="true">+</span></summary><div class="study-tip-content">'+''.join(f'<p>{E(p)}</p>' for p in a['paragraphs'])+f'<p class="document-source">Based on {E(s["filename"])} · PDF pages {", ".join(map(str,a["pages"]))}. <a href="{anchor("college-notes.html",s["id"])}">Source and remaining checks</a>. Existing answers and figures are unchanged.</p></div></details>'+'<!-- COLLEGE-ADDITION-END -->'
   start=text.index(f'id="{a["anchor"]}"');match=re.search(r'</h[23]>',text[start:]);assert match,(u,a['anchor']);at=start+match.end();text=text[:at]+block+text[at:]
  banner='<!-- COLLEGE-COLLECTION-START -->'+f'<aside class="source-notes-editorial"><strong>College &amp; Senior Notes · R25 Unit {u}.</strong> <a href="{PREFIX}college-notes.html#unit-{u}">All units, source inventory and printing guide</a> · <a href="{PREFIX}question-banks.html">Question collections</a>. Existing source text, figures and documented corrections are preserved. Additional explanations and authored question-bank answers are labelled separately. Text extraction and drawing verification have separate audit records.</aside>'+'<!-- COLLEGE-COLLECTION-END -->'
  marker=re.search(r'<(?:div|article) class="end-sem-content">',text);assert marker;text=text[:marker.end()]+banner+text[marker.end():];text=text.replace('Questions are saved separately for a future question bank.','Question collections are listed separately; worked answers are available in the question bank.').replace('worked solutions remain pending.','worked answers are available in the question bank.').replace('The supplied questions have been retained for a future question bank. They have not been presented as textbook exercises, PYQs or verified solutions.','The supplied questions and PankusDesk-authored answers are in the Unit-wise Question Bank &amp; Solutions collection. They are not authenticated PYQs or lecturer-approved answers.').replace('Questions are saved for a future question bank; they are not presented here as textbook exercises, PYQs or verified solutions.','Questions and PankusDesk-authored answers are available in the separate question bank; they are not authenticated PYQs or lecturer-approved solutions.');p.write_text(text)
 groups={q['source_id'] for q in bank['questions']+bank.get('additional_questions',[])}
 print(f'Built collection for {len(inventory["sources"])} files, {len(groups)} question collections / {len(bank['questions'])+len(bank.get('additional_questions',[]))} answered prompts and {len(additions)} labelled explanations.')
if __name__=='__main__':main()
