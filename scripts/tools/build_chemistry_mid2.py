#!/usr/bin/env python3
"""Render the four supplied Mid II papers, preserving source choices and marks."""
import json
from build_chemistry_collections import S, R, E, PREFIX, shell, handout_figure, anchor


def main():
 data=json.loads((R/'mid-2-papers.json').read_text())
 inventory=json.loads((R/'source-inventory.json').read_text())['sources']
 lookup={x['id']:x for x in inventory}
 lookup.update({x['source_id']:x for x in inventory if x.get('source_id')})
 figures={x['id']:x for x in json.loads((R/'mid-2-source-figures.json').read_text())['figures']}
 def figure(id):
  if id not in figures:return handout_figure(id)
  f=figures[id]
  return f'<figure class="study-figure" data-source-figure="{E(id)}"><a href="{E(f["asset"])}" target="_blank" rel="noopener"><img src="{E(f["asset"])}" alt="{E(f["alt"])}" width="{f["width"]}" height="{f["height"]}" loading="lazy" decoding="async"></a><figcaption><strong>{E(f["title"])}.</strong> {E(f["caption"])} {E(f["source_filename"])} · PDF p.{f["source_pdf_page"]}. Select image for full size.</figcaption></figure><aside class="study-mismatch-note" role="note"><strong>Source diagram correction.</strong><p>{E(f["source_discrepancy"])}</p></aside>'
 def answer(a):
  sources=[]
  for ref in a['source_refs']:
   src=lookup[ref['source_id']]
   assert all(0<n<=src['pages_or_slides'] for n in ref['pages']),ref
   sources.append(f'<a href="{anchor("college-notes.html",src["id"])}">{E(src["filename"])}</a>'+(' · pages '+', '.join(map(str,ref['pages'])) if ref['pages'] else ''))
  return ''.join('<p>'+E(t)+'</p>' for t in a['paragraphs'])+('<p class="source-notes-editorial">'+E(a['clarification'])+'</p>' if a.get('clarification') else '')+''.join(figure(i) for i in a.get('figure_ids',[]))+'<p class="document-source">Answer basis: '+'; '.join(sources)+'.</p>'
 def question(p,q,part):
  label=f'Part {part} · '+('('+q['number']+')' if part=='A' else 'Q'+q['number'])+f' · {q["marks"]} marks'
  prompt=E(q['prompt'])
  for sub in q.get('parts',[]):prompt+=f'<br><strong>({E(sub["label"])})</strong> {E(sub["prompt"])}'+(f' <strong>[{sub["marks"]} marks]</strong>' if sub['marks'] is not None else '')
  body='<div class="study-solution-label">PankusDesk-authored solution</div>'
  if 'parts' in q:
   if any(x['marks'] is None for x in q['parts']):body+='<p class="document-source">The paper gives '+str(q['marks'])+' marks for this question as a whole; no separate subpart marks are printed.</p>'
   for sub in q['parts']:body+=f'<section class="study-solution-part" id="{E(sub["id"])}"><h4>({E(sub["label"])}) {E(sub["prompt"])}</h4>'+answer(sub['answer'])+'</section>'
  else:body+=answer(q['answer'])
  body+=f'<p class="document-source">Scope: {E(q["scope"])}. Question source: {E(p["source_records"][0]["filename"])} · page 1 · {E(p["date"])}.</p>'
  mismatch=' has-math-mismatch' if any(x in figures for x in q.get('answer',{}).get('figure_ids',[])) else ''
  return f'<details class="study-accordion-item study-accordion-item--example collection-question{mismatch}" id="{E(q["id"])}"><summary><span class="study-example-summary-copy"><span class="study-example-title">{E(label)}</span><span class="study-example-question">{prompt}</span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{body}</div></details>'
 nav='';body='<div class="bank-view-intro" id="all-papers"><p id="bank-view-status" role="status">Viewing 30 Dec 2025 · R25</p><p>Actual supplied VNR sessional papers, distinct from the general question bank. Answers are PankusDesk-authored from the supplied notes, not lecturer-approved marking keys. Study both OR alternatives here; in the examination follow the paper’s choice instructions.</p><p>Original unit labels are retained. In R22 papers, Unit IV corrosion maps to R25 Unit II; supplementary older topics are labelled in their answers. The July 2024 paper is Semester II for other branches, not an IT Semester I paper.</p><p><a href="'+PREFIX+'index.html">← Chemistry resources</a> · <a href="'+PREFIX+'question-banks.html">General question bank →</a></p></div>'
 for p in data['papers']:
  title=p['date']+' · '+p['regulation']+(' · Semester II / other branches' if p['semester']=='II' else '')
  default=p['id']==data['default_paper'];current=' aria-current="location"' if default else '';hidden='' if default else ' hidden'
  nav+=f'<a href="{anchor("mid-2.html",p["id"])}" data-bank-unit="{p["id"]}"{current}>{E(title)}</a>'
  block=f'<h2>{E(title)}</h2><p><strong>{E(p["printed_session"])}</strong> · Date of examination: {E(p["date"])}{(' '+E(p['time_of_day'])) if p.get('time_of_day') else ''} · B.Tech I Year, Semester {p["semester"]} · Sessional Examination II.</p><p>Subject code as printed: <strong>{E(p.get("subject_code_printed",p.get("subject_code","")))}</strong>. Common to: {E(", ".join(p["branches"]))}. Duration: 2 hours · Maximum: 30 marks.</p><p><strong>Exam choices:</strong> Part A: all five questions, 5 × 2 = 10 marks. Part B: answer one question from each original unit (III, IV, V), 4 + 8 + 8 = 20 marks. All alternatives are solved below.</p>'
  if p['regulation']=='R22':block+='<aside class="source-notes-editorial">Older R22 paper. Original units and questions are preserved for practice; this is not presented as a paper set under R25.</aside>'
  block+='<h3>Part A · Short answers · 10 marks</h3>'+''.join(question(p,q,'A') for q in p['part_a'])+'<h3>Part B · Original unit choices · 20 marks</h3>'
  for i,u in enumerate([3,4,5]):
   block+=f'<h3>Original Unit {u} · Choose Q{2*i+1} OR Q{2*i+2}</h3>'
   block+=question(p,p['part_b'][2*i],'B')+'<p class="paper-or"><strong>OR</strong> · answer one of this pair in the examination</p>'+question(p,p['part_b'][2*i+1],'B')
  block+='<details><summary>Paper provenance and duplicate captures</summary><p>Supplied in chem_mid_2.zip. Student identifiers are not transcribed; original photographs/PDFs are not published.</p><ul>'+''.join('<li>'+E(x['filename'])+' · page 1 · SHA-256 <code>'+x['sha256']+'</code></li>' for x in p['source_records'])+'</ul><p>Other filename aliases: '+E(', '.join(p['source_files']))+'.</p></details>'
  body+=f'<section class="document-page bank-unit" id="{p["id"]}" data-bank-unit-section="{p["id"]}" data-bank-title="{E(title)}"{hidden}>{block}</section>'
 nav+=f'<a href="{anchor("mid-2.html","all-papers")}" data-bank-unit="all">All four papers</a>'
 page=shell('mid-2.html',data['title'],'Four actual Mid II papers with their original questions, OR choices and worked solutions. The current R25 paper opens first.',nav,body)
 page=page.replace('<body>',f'<body data-question-bank="true" data-bank-default="{data["default_paper"]}" data-bank-all-id="all-papers" data-bank-all-label="Viewing all four papers">')
 for css in ['pages/end-sem-notes','pages/source-notes','pages/practice']:page=page.replace('</head>',f'<link rel="stylesheet" href="styles/new/{css}.css">\n</head>')
 page=page.replace('</head>','<script src="scripts/new/question-bank-navigation.js" defer></script>\n</head>')
 (S/'mid-2.html').write_text(page)
 print('Built 4 Mid II papers / 44 questions, including all OR alternatives.')

if __name__=='__main__':main()
