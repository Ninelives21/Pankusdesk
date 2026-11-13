#!/usr/bin/env python3
"""Render the four supplied Mid II papers, preserving source choices and marks."""
import json
from build_chemistry_collections import S, R, E, PREFIX, shell, anchor
from study_answer_blocks import render_blocks


def main():
 data=json.loads((R/'mid-2-papers.json').read_text())
 faq=json.loads((R/'mid-2-faq.json').read_text())
 questions={};paper_for={}
 for paper in data['papers']:
  for q in paper['part_a']+paper['part_b']:
   for item in [q]+q.get('parts',[]):questions[item['id']]=item;paper_for[item['id']]=paper['id']
 inventory=json.loads((R/'source-inventory.json').read_text())['sources']
 lookup={x['id']:x for x in inventory}
 lookup.update({x['source_id']:x for x in inventory if x.get('source_id')})
 figures={x['id']:x for x in json.loads((R/'source-figures.json').read_text())['figures']}
 figures.update({x['id']:x for x in json.loads((R/'mid-2-source-figures.json').read_text())['figures']})
 def figure(id):
  f=figures[id];note=f.get('student_note','')
  return f'<figure class="study-figure" data-source-figure="{E(id)}"><a href="{E(f["asset"])}" target="_blank" rel="noopener"><img src="{E(f["asset"])}" alt="{E(f["alt"])}" width="{f["width"]}" height="{f["height"]}" loading="lazy" decoding="async"></a><figcaption><strong>{E(f["title"])}.</strong>{(" "+E(note)) if note else ""}</figcaption></figure>'
 def answer(a):
  # Preserve source checks in data; exam answers contain only teaching content.
  for ref in a['source_refs']:
   src=lookup[ref['source_id']]
   assert all(0<n<=src['pages_or_slides'] for n in ref['pages']),ref
  return render_blocks(a['blocks'],figure)
 def question(p,q,part):
  label=f'Part {part} · '+('('+q['number']+')' if part=='A' else 'Q'+q['number'])+f' · {q["marks"]} marks'
  prompt=E(q['prompt'])
  for sub in q.get('parts',[]):prompt+=f'<br><strong>({E(sub["label"])})</strong> {E(sub["prompt"])}'+(f' <strong>[{sub["marks"]} marks]</strong>' if sub['marks'] is not None else '')
  body=''
  if 'parts' in q:
   for sub in q['parts']:body+=f'<section class="study-solution-part" id="{E(sub["id"])}"><h4>({E(sub["label"])}) {E(sub.get("answer_title",sub["prompt"]))}</h4>'+answer(sub['answer'])+'</section>'
  else:body+=answer(q['answer'])
  return f'<details class="study-accordion-item study-accordion-item--example collection-question" id="{E(q["id"])}"><summary><span class="study-example-summary-copy"><span class="study-example-title">{E(label)}</span><span class="study-example-question">{prompt}</span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{body}</div></details>'
 nav='';body='<div class="bank-view-intro" id="paper-intro"><p id="bank-view-status" role="status">Viewing 30 Dec 2025 · R25</p><p>Choose a paper. Open a question to read its answer.</p><p><a href="'+PREFIX+'index.html">← Chemistry</a></p></div>'
 for p in data['papers']:
  title=p['date']+' · '+p['regulation']+(' · Semester II / other branches' if p['semester']=='II' else '')
  default=p['id']==data['default_paper'];current=' aria-current="location"' if default else '';hidden='' if default else ' hidden'
  nav+=f'<a href="{anchor("mid-2.html",p["id"])}" data-bank-unit="{p["id"]}"{current}>{E(title)}</a>'
  block=f'<h2>{E(title)}</h2><p><strong>{E(p["printed_session"])}</strong> · Date of examination: {E(p["date"])}{(' '+E(p['time_of_day'])) if p.get('time_of_day') else ''} · B.Tech I Year, Semester {p["semester"]} · Sessional Examination II.</p><p>Subject code: <strong>{E(p.get("subject_code_printed",p.get("subject_code","")))}</strong>. Common to: {E(", ".join(p["branches"]))}. Duration: 2 hours · Maximum: 30 marks.</p><p><strong>Exam choices:</strong> Part A: all five questions, 5 × 2 = 10 marks. Part B: answer one question from each original unit (III, IV, V), 4 + 8 + 8 = 20 marks. All alternatives are solved below.</p>'
  block+='<h3>Part A · Short answers · 10 marks</h3>'+''.join(question(p,q,'A') for q in p['part_a'])+'<h3>Part B · 20 marks</h3>'
  for i,u in enumerate([3,4,5]):
   block+=f'<h3>Unit {u} · Choose Q{2*i+1} OR Q{2*i+2}</h3>'
   block+=question(p,p['part_b'][2*i],'B')+'<p class="paper-or"><strong>OR</strong> · answer one of this pair in the examination</p>'+question(p,p['part_b'][2*i+1],'B')
  body+=f'<section class="document-page bank-unit" id="{p["id"]}" data-bank-unit-section="{p["id"]}" data-bank-title="{E(title)}"{hidden}>{block}</section>'
 # A focused revision view replaces the combined paper dump. Answers are reused
 # from their canonical paper records rather than independently authored copies.
 faqbody='<span id="all-papers"></span><h2>'+E(faq['title'])+'</h2><p>'+E(faq['intro'])+'</p>'
 for kind,heading in [('short','Short-answer questions'),('essay','Essay questions')]:
  faqbody+='<h3>'+heading+'</h3>'
  for entry in [x for x in faq['entries'] if x['kind']==kind]:
   count=len({paper_for[id] for id in entry['topic_matches']})
   label=f'Unit {entry["r25_unit"]} · Related questions in {count} of {faq["paper_count"]} papers'
   content=''
   for ref in entry['answer_refs']:
    rendered=answer(questions[ref['id']]['answer'])
    content+=('<section class="study-solution-part"><h4>'+E(ref['heading'])+'</h4>'+rendered+'</section>') if ref.get('heading') else rendered
   note='<p>'+E(entry['frequency_note'])+'</p>' if entry.get('frequency_note') else ''
   faqbody+=f'<div class="bank-source-group">{note}<details class="study-accordion-item study-accordion-item--example collection-question" id="{E(entry["id"])}"><summary><span class="study-example-summary-copy"><span class="study-example-title">{E(label)}</span><span class="study-example-question">{E(entry["title"])}</span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{content}</div></details></div>'
 body+=f'<section class="document-page bank-unit" id="{faq["id"]}" data-bank-unit-section="faq" data-bank-title="{E(faq["title"])}" hidden>{faqbody}</section>'
 nav+=f'<a href="{anchor("mid-2.html",faq["id"])}" data-bank-unit="faq">Frequently Asked Questions · R25</a>'
 page=shell('mid-2.html',data['title'],'Short answers, essay answers and diagrams. The R25 paper opens first.',nav,body)
 page=page.replace('<body>',f'<body data-question-bank="true" data-bank-default="{data["default_paper"]}" data-bank-allow-all="false">')
 for css in ['pages/end-sem-notes','pages/source-notes','pages/practice']:page=page.replace('</head>',f'<link rel="stylesheet" href="styles/new/{css}.css">\n</head>')
 page=page.replace('</head>','<script src="scripts/new/question-bank-navigation.js" defer></script>\n</head>')
 (S/'mid-2.html').write_text(page)
 print('Built 4 Mid II papers / 44 questions, including all OR alternatives.')

if __name__=='__main__':main()
