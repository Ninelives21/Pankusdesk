#!/usr/bin/env python3
"""Build searchable HTML from supplied PDFs kept outside the repository.

Usage: python3 scripts/tools/build_institutional_documents.py --syllabus PATH
       --regulations PATH --handbook PATH
Requires PyMuPDF only for regeneration; the published site has no PDF/runtime dependency.
"""
import argparse
from collections import defaultdict
from pathlib import Path
import hashlib
import html
import json
import re
import fitz

ROOT = Path(__file__).resolve().parents[2]
E = html.escape
SPECS = {
 'r25': ('R25 Syllabus · First-Year IT', 'I-B.Tech-IT-R25-26-11-2025.pdf', 'college/documents/r25.html', [
 (1,'Department of Information Technology'),(2,'Vision and Mission'),(3,'Programme Identity'),(4,'Programme Educational Objectives'),(5,'Programme Outcomes'),(7,'Programme Specific Outcomes'),(8,'Semester I and II Course Structure'),(9,'I · Matrices and Calculus'),(11,'I · Chemistry for Engineers'),(14,'I · Basic Electrical Engineering'),(16,'I · Programming for Problem Solving'),(18,'I · Engineering Drawing'),(20,'I · Chemistry Laboratory'),(22,'I · PPS Laboratory'),(25,'I · IT Workshop'),(28,'I · BEE Laboratory'),(30,'II · Differential Equations, Laplace Transforms and Vector Calculus'),(32,'II · Advanced Engineering Physics'),(35,'II · English for Skill Enhancement'),(37,'II · Electronic Devices and Circuits'),(39,'II · Data Structures'),(41,'II · Physics Laboratory'),(43,'II · English Language and Communication Skills Laboratory'),(46,'II · Data Structures Laboratory'),(49,'II · Python Programming Laboratory'),(53,'II · Engineering Workshop'),(55,'II · Happiness and Wellbeing')]),
 'regulations': ('R25 Academic Regulations', 'VNR-BTECH-R25-REGULATIONS.pdf', 'college/documents/regulations.html', [
 (1,'Cover'),(2,'Original Table of Contents'),(4,'Part 1 · Introduction and Administrative Framework'),(9,'Part 2 · Admission and Programme Structure'),(19,'Part 3 · Academic Processes'),(24,'Part 4 · Evaluation and Assessment'),(33,'Part 5 · Results, Grading and Promotion'),(39,'Part 6 · Award of Degree'),(41,'Part 7 · Special Programmes'),(44,'Part 8 · Additional Provisions'),(48,'Part 9 · Lateral Entry Scheme'),(50,'Appendix · Malpractice Rules'),(55,'Institute Contact Details')]),
 'exams': ('Exams & Notices · Examination Handbook', 'EXAMINATIONS AND EVALUATION SECTION HANDBOOK 07-11-2026.pdf', 'college/1-1/exams-notices.html', [
 (1,'Handbook Cover'),(2,'Examination Handbook · Guidelines'),(3,'Eligibility and Registration'),(4,'Fees, Hall Ticket and Examination Day'),(6,'Disciplinary Action and Theory Assessment'),(10,'Practical and Other Course Assessment'),(14,'Results and Academic Progression'),(19,'Frequently Asked Questions'),(25,'Examination Lifecycle and Services')]),
}
# Fractions and summation layouts require explicit semantic transcription.
FORMULAS = {
 35: [(fitz.Rect(150,435,445,468),r'\mathrm{SGPA}=\dfrac{\text{Total earned weighted grade points in a semester}}{\text{Total credits in a semester}}'),
      (fitz.Rect(245,478,350,513),r'\mathrm{SGPA}=\dfrac{\sum_{i=1}^{P}C_i G_i}{\sum_{i=1}^{P}C_i}'),
      (fitz.Rect(125,697,470,727),r'\mathrm{CGPA}=\dfrac{\text{Total earned weighted grade points for the entire programme}}{\text{Total credits for the entire programme}}')],
 36: [(fitz.Rect(245,70,350,104),r'\mathrm{CGPA}=\dfrac{\sum_{j=1}^{m}C_j G_j}{\sum_{j=1}^{m}C_j}'),
      (fitz.Rect(230,560,366,586),r'\text{Thus, SGPA}=\dfrac{139}{20}=6.95')],
 37: [(fitz.Rect(230,562,367,586),r'\text{Thus, CGPA}=\dfrac{321}{40}=8.02')],
}

def contains(rect, word):
 return rect.contains(fitz.Point((word[0]+word[2])/2,(word[1]+word[3])/2))

def line_text(words):
 return ' '.join(w[4] for w in sorted(words,key=lambda w:w[0]))

def build_page(page, key, number):
 words=page.get_text('words');used=set();elements=[];headings=[];table_count=0
 def take(rect):
  ids=[i for i,w in enumerate(words) if i not in used and contains(rect,w)]
  used.update(ids);return [words[i] for i in ids]
 if key=='regulations':
  for rect,formula in FORMULAS.get(number,[]):
   if take(rect):elements.append((rect.y0,0,f'<div class="document-equation">\\[{E(formula)}\\]</div>'))
 for ti,table in enumerate(page.find_tables().tables):
  # Use source words within detected cells rather than OCR/rewording cell text.
  rows=[]
  for row in table.rows:
   cells=[]
   for cell in row.cells:
    if cell is None:cells.append('<td></td>');continue
    selected=take(fitz.Rect(cell));lines=defaultdict(list)
    for w in selected:lines[(w[5],w[6])].append(w)
    text='<br>'.join(E(line_text(ws)) for _,ws in sorted(lines.items(),key=lambda kv:min(w[1] for w in kv[1])))
    cells.append(f'<td>{text}</td>')
   rows.append('<tr>'+''.join(cells)+'</tr>')
  elements.append((table.bbox[1],table.bbox[0],f'<div class="document-table"><table><caption>Source table · PDF page {number}</caption><tbody>'+''.join(rows)+'</tbody></table></div>'));table_count+=1
 blocks=defaultdict(list)
 for i,w in enumerate(words):
  if i not in used:blocks[w[5]].append((i,w))
 for entries in blocks.values():
  for i,_ in entries:used.add(i)
  ws=[w for _,w in entries];lines=defaultdict(list)
  for w in ws:lines[w[6]].append(w)
  texts=[line_text(v) for _,v in sorted(lines.items())]
  text=' '.join(texts)
  if not text.strip():continue
  y=min(w[1] for w in ws);x=min(w[0] for w in ws)
  if re.fullmatch(r'[ivx\d]+',text.strip(),re.I) and (y<65 or y>page.rect.height-65):continue
  if set(text.replace(' ','')) <= set('─_-'):continue
  heading=(len(text)<180 and (re.match(r'^(?:UNIT[-– ]*[IVX]+|(?:A?\d+\.0)\s+[A-Z]|PART\s+\d|WEEK\s+\d)',text) or (text.isupper() and len(text)>5 and not re.search(r'\d{3}',text))))
  if heading:
   anchor=f'{key}-p{number}-h{len(headings)+1}';headings.append((anchor,text));content=f'<h3 id="{anchor}">{E(text)}</h3>'
  else:
   # Keep source clauses/list lines separate while reflowing ordinary wrapped prose.
   chunks=[];current=[]
   for t in texts:
    if re.match(r'^(?:[•➢⮚▪]|\d+(?:\.\d+)*\.?(?:\s|$)|[a-zivx]+[.)]\s|Q\d+[.)]|[A-Z][A-Z &/–-]+:)',t) and current:
     chunks.append(' '.join(current));current=[]
    current.append(t)
   if current:chunks.append(' '.join(current))
   content=''.join(f'<p>{E(t)}</p>' for t in chunks)
  elements.append((y,x,content))
 assert len(used)==len(words),(key,number,'unassigned source words')
 body=''.join(item[2] for item in sorted(elements,key=lambda e:(round(e[0],1),e[1])))
 # Rejoin PDF text-block continuations without combining numbered clauses or lists.
 def continuation_group(match):
  paragraphs=re.findall(r'<p>([^<]*)</p>',match.group(0));joined=[]
  for paragraph in paragraphs:
   next_clause=re.match(r'^(?:\d+(?:\.\d+)*[.)]?(?:\s|$)|[A-Za-z][.)]\s|[•➢⮚▪]|UNIT|WEEK|Where:|Table\s|Q\d|[A-Z][A-Z &/–-]+:)',paragraph)
   if joined and not joined[-1].rstrip().endswith(('.', '!', '?', ';', ':')) and not next_clause:
    joined[-1]+=' '+paragraph
   else: joined.append(paragraph)
  return ''.join('<p>'+paragraph+'</p>' for paragraph in joined)
 body=re.sub(r'(?:<p>[^<]*</p>\s*)+',continuation_group,body)
 if key=='r25':
  headings=[entry for entry in headings if not entry[1].startswith('UNIT')]
  def unit_anchor(match):
   label=match.group(0);anchor=f'r25-p{number}-unit-{len(headings)+1}'
   headings.append((anchor,label))
   return f'<span class="document-unit-title" id="{anchor}">{label}</span>'
  body=re.sub(r'\bUNIT\s*[-–]?\s*[IVX]+\s*:',unit_anchor,body)
 return body,headings,{'pdf_page':number,'source_words':len(words),'assigned_words':len(used),'tables':table_count}

def build(key,path):
 title,filename,out,groups=SPECS[key];doc=fitz.open(path);pages=[];nav=[];audit=[]
 for number,page in enumerate(doc,1):
  if not page.get_text().strip():
   if key=='exams' and number in (1,25):
    cover = ('<h3>Examinations and Evaluation Section Handbook</h3><p>VNR Vignana Jyothi Institute of Engineering and Technology (Autonomous Institute) · B.Tech. CBCS R25.</p><p>Let’s ensure fairness, integrity and excellence in every assessment we do. Together, we uphold quality education!</p>' if number==1 else '<h3>Examination Lifecycle</h3><p>Registration → Question Paper Management → Examination → Digital Evaluation → Scrutiny → Results → Academic Records.</p><h3>Digital Examination Services</h3><p>Examination Registration · Hall Tickets · Examination Fee Payment · Question Paper Management · Barcode-enabled Answer Booklets · Digital Evaluation · Scrutiny · Result Processing · Academic Records.</p><p>Website: www.vnrvjiet.ac.in · Email: postbox@vnrvjiet.ac.in.</p>')
    pages.append((number,cover,[]));audit.append({'pdf_page':number,'image_cover_text':'Manually transcribed title/lifecycle/services; decorative branding omitted.'})
   else: audit.append({'pdf_page':number,'blank_text_layer':True})
   continue
  body,headings,record=build_page(page,key,number);audit.append(record)
  pages.append((number,body,headings))
 for gi,(start,label) in enumerate(groups):
  end=groups[gi+1][0] if gi+1<len(groups) else len(doc)+1
  entries=[p for p in pages if start<=p[0]<end]
  if not entries:continue
  target=f'{key}-page-{entries[0][0]}'
  children=[]
  for n,_,heads in entries:
   children.append(f'<a href="{out}#{key}-page-{n}">PDF page {n}</a>')
   children.extend(f'<a class="document-nav-child" href="{out}#{anchor}">{E(text)}</a>' for anchor,text in heads)
  nav.append(f'<details open><summary><a href="{out}#{target}">{E(label)}</a></summary>'+''.join(children)+'</details>')
 if key=='regulations':
  toc_lines=[line.strip() for page in list(doc)[1:3] for line in page.get_text().splitlines() if line.strip()]
  clauses=[]
  for i,line in enumerate(toc_lines):
   if not re.fullmatch(r'A?\d+\.0',line):continue
   title_lines=[]
   for following in toc_lines[i+1:]:
    if re.fullmatch(r'\d+(?:[-–]\d+)?',following):
     pdf_page=int(re.split('[-–]',following)[0])+3
     clauses.append(f'<a href="{out}#regulations-page-{pdf_page}">{E(line+" "+" ".join(title_lines))}</a>')
     break
    title_lines.append(following)
  nav.insert(1,'<details open><summary>Numbered Regulations</summary>'+''.join(clauses)+'</details>')
 body=''.join(f'<section class="document-page" id="{key}-page-{n}"><h2>PDF page {n}</h2>{content}</section>' for n,content,_ in pages)
 intro={
 'r25':'Complete first-year Information Technology syllabus, including Semesters I and II, course structures, outcomes, units, laboratory exercises and references.',
 'regulations':'B.Tech. CBCS R25 Academic Regulations, including academic processes, assessment, promotion, lateral entry and the malpractice appendix.',
 'exams':'Examinations & Evaluation Section · B.Tech. CBCS R25 · Academic Year 2026–27. The handbook is a simplified guide; the R25 Academic Regulations remain the governing document.'}[key]
 extras='<p><a href="college/calendar.html?semester=1-1&amp;date=2026-11-30">Chemistry lab examination schedule → Calendar</a></p>' if key=='exams' else ''
 css=''.join(f'<link rel="stylesheet" href="styles/new/{f}.css">' for f in ['variables','base','layout','navbar','components','study-ui','pages/institutional-documents'])
 htmltext=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<base id="site-base" href="/"><script>if(location.hostname.endsWith('github.io')) document.getElementById('site-base').href='/Pankusdesk/';</script>
<title>{E(title)} · Panku’s Desk</title>{css}<script src="scripts/new/navbar.js" defer></script><script src="scripts/new/study-ui.js" defer></script><script src="scripts/new/institutional-documents.js" defer></script></head>
<body><div id="navbar-new"></div><main class="page-shell institutional-document" id="document-top">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="index.html">Panku’s Desk</a> › <a href="index.html#important-documents">Important Documents</a> › {E(title)}</nav>
<header><h1>{E(title)}</h1><p>{E(intro)}</p><p class="document-source">Source: {E(filename)} · {len(doc)} PDF pages. HTML edition; original wording and source page references retained. Decorative covers and logos are omitted.</p>{extras}</header>
<div class="document-layout"><aside class="document-sidebar" aria-label="Document navigation"><a class="document-back-top" href="{out}#document-top">↑ Back to top</a><details class="document-contents" open><summary>Contents</summary><nav aria-label="Document contents">{''.join(nav)}</nav></details></aside><article class="document-body">{body}</article></div>
</main></body></html>\n'''
 htmltext=htmltext.replace('</p>', '</p>\n').replace('</h3>', '</h3>\n').replace('</tr>', '</tr>\n').replace('</section>', '</section>\n')
 (ROOT/out).write_text(htmltext)
 return {'id':key,'title':title,'source_filename':filename,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_bytes':path.stat().st_size,'pdf_pages':len(doc),'html_path':out,'html_bytes':len(htmltext.encode()),'page_audit':audit,'formula_transcriptions':list(FORMULAS) if key=='regulations' else []}

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 for arg in ['syllabus','regulations','handbook']:parser.add_argument('--'+arg,type=Path,required=True)
 args=parser.parse_args()
 records=[build('r25',args.syllabus),build('regulations',args.regulations),build('exams',args.handbook)]
 manifest={'storage_policy':'HTML only; supplied PDF binaries remain outside the public repository. Regeneration accepts external source paths. Original wording retained; no changes to rules or syllabus authority.','documents':records}
 (ROOT/'college/documents/source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps([{k:r[k] for k in ['id','pdf_pages','html_bytes']} for r in records]))
if __name__=='__main__':main()
