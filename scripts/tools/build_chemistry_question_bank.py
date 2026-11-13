#!/usr/bin/env python3
"""Build the unit bank with individual supplied sets and answer-only presentation."""
import json,re,copy
from collections import defaultdict
from lxml import html
from build_chemistry_collections import S,R,E,PREFIX,TITLES,shell,read,answer_html
from study_answer_blocks import render_blocks
from chemistry_short_answers import short_answer_blocks

def build_question_bank():
 bank=read('question-bank-pending.json');solutions=read('question-bank-solutions.json');intake=read('question-bank-intake.json')
 question_data={q['id']:q for q in bank['questions']+bank['additional_questions']}
 figures={f['id']:f for name in ['source-figures.json','mid-2-source-figures.json','question-bank-intake-figures.json'] for f in read(name)['figures']}
 mid=read('mid-2-papers.json');midanswers={}
 for paper in mid['papers']:
  for q in paper['part_b']:
   for sub in q.get('parts',[q]):midanswers[sub['id']]=sub['answer']['blocks']
 prefix='cfe-mid2-2025-12-30-r25-b-'
 modules={'lithium':prefix+'2','conducting':prefix+'3-a','smp':prefix+'3-b','kevlar':prefix+'4-a','pla':prefix+'4-b','dye':prefix+'5-b','healing':prefix+'6-a','batteryclasses':'cfe-mid2-2023-03-06-r22-b-1','methanol':'cfe-mid2-2023-03-06-r22-b-2','nano':'cfe-mid2-2023-03-06-r22-b-5-b','stm':prefix+'5-a'}
 def figure(id):
  f=figures[id];note=f.get('student_note','')
  return f'<figure class="study-figure" data-source-figure="{E(id)}"><a href="{E(f["asset"])}" target="_blank" rel="noopener"><img src="{E(f["asset"])}" alt="{E(f["alt"])}" width="{f["width"]}" height="{f["height"]}" loading="lazy" decoding="async"></a><figcaption><strong>{E(f["title"])}.</strong>{(" "+E(note)) if note else ""}</figcaption></figure>'
 def clean(raw):
  root=html.fragment_fromstring(raw,create_parent='div')
  for n in list(root.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," document-source ") or contains(concat(" ",normalize-space(@class)," ")," study-solution-label ")]')):
   if n.getparent() is not None:n.drop_tree()
  for n in root.xpath('.//figure[@data-source-figure]'):
   new=html.fragment_fromstring(figure(n.get('data-source-figure')));
   if n.get('id'):new.set('id',n.get('id'))
   n.getparent().replace(n,new)
  # Remove authoring chatter, retaining mathematical/scientific corrections.
  for n in list(root.xpath('.//p | .//h4')):
   if n.getparent() is None:continue
   text=n.text_content().strip()
   if text.startswith('Source drawing gap:'):
    n.clear();n.text='Diagram unavailable: a Nitinol transformation-cycle drawing is still needed.' if 'Nitinol' in text else 'Diagram unavailable: a CO-analyser apparatus drawing is still needed.';continue
   if text.startswith(('General chemistry clarification is used only','Based on ','Answer basis:','Question source:','PankusDesk-completed working. The supplied','The supplied bank asks about galvanization')):n.drop_tree();continue
   if n.get('class')=='numerical-authored-label':n.text='Working'
   if text.startswith('Supplied table'):n.text='Given values'
  for n in root.iter():
   if n.text:
    for a,b in [('PankusDesk-completed working','Working'),('PankusDesk-authored explanation','Explanation'),('Source qualification: ','Note: '),('Source correction: ','Correction: '),('The supplied example','The example'),('in the supplied example','in this example'),('The notes specify','A typical catalyst contains'),('The supplied historical example','One example'),('the course notes call this','also called')]:n.text=n.text.replace(a,b)
  replacements={'The source transcript’s wording is preserved above. ': '',
   'Working. The source table begins on PDF p.1 and continues on p.2; its header and all rows are reunited above.': '',
   'PankusDesk solution — using the question’s printed data, including ': 'Using the given data, '
                                                                          'including ',
   'The supplied course material discusses': 'Methods include',
   'In the supplied comparison': 'In this comparison',
   'The supplied textbook, printed p.7, explicitly calls it very adherent and difficult to remove; printed p.8 prescribes EDTA treatment, which forms soluble calcium complexes.': 'It '
                                                                                                                                                                                   'is '
                                                                                                                                                                                   'adherent '
                                                                                                                                                                                   'and '
                                                                                                                                                                                   'difficult '
                                                                                                                                                                                   'to '
                                                                                                                                                                                   'remove. '
                                                                                                                                                                                   'EDTA '
                                                                                                                                                                                   'treatment '
                                                                                                                                                                                   'forms '
                                                                                                                                                                                   'soluble '
                                                                                                                                                                                   'calcium '
                                                                                                                                                                                   'complexes.',
   'discussed in the supplied notes': 'formed in boilers',
   'The supplied notation gives:': 'Reaction:',
   'Read the supplied graph': 'Read the graph',
   'the supplied course explains its action in terms of': 'its action involves',
   'The supplied diagram shows': 'The diagram shows',
   'Prevention in the supplied textbook (printed p.10):': 'Prevention:',
   'This is the course explanation for why': 'This explains why',
   'The text gives historical': 'Typical historical',
   'Using the supplied conversion chart, ': 'Using ',
   'using the supplied rounded conversion': 'using the rounded conversion',
   'Using the source chart’s rounded ': 'Using ',
   'in the supplied table': 'in the table',
   'its supplied atomic mass': 'its atomic mass',
   'The notes state 25°C, 1 bar gas pressure and 1 M ion concentration.': 'Use 25°C, 1 bar gas '
                                                                          'pressure and unit ion '
                                                                          'activity (approximately 1 '
                                                                          'M).',
   'represented approximately by 1 M in the notes': 'represented approximately by 1 M',
   'The SHE construction description elsewhere uses 1 atm; retain that source convention when quoting it rather than silently equating bar and atm.': 'Do '
                                                                                                                                                      'not '
                                                                                                                                                      'silently '
                                                                                                                                                      'equate '
                                                                                                                                                      '1 '
                                                                                                                                                      'bar '
                                                                                                                                                      'with '
                                                                                                                                                      '1 '
                                                                                                                                                      'atm.',
   'The balanced product is neutral Hg(l), following the comparison handout and charge balance. The original Hg⁺ typo is recorded in the correction ledger.': 'The '
                                                                                                                                                              'balanced '
                                                                                                                                                              'product '
                                                                                                                                                              'is '
                                                                                                                                                              'neutral '
                                                                                                                                                              'Hg(l), '
                                                                                                                                                              'not '
                                                                                                                                                              'Hg⁺.',
   'The handout groups glass with the reference-electrode choices. ': '',
   'The simplified course rule is useful for the supplied exercise, but': 'The simple volume-ratio '
                                                                          'rule is a guideline, but',
   'Using the supplied handout’s simplified rule,': 'Using the simplified volume-ratio rule,',
   'This is the intended course-model answer to these given data.': 'Actual protection also depends '
                                                                    'on film integrity and '
                                                                    'environment.',
   'The supplied simplified scheme': 'The simplified scheme',
   'The supplied slide names the Statue of Liberty:': 'For the Statue of Liberty,',
   'This is the example given by the source; it does not mean': 'This does not mean',
   '; the DOCX omits it': '',
   'No source product lifetime is a universal guarantee.': 'Recovery is not guaranteed for every '
                                                           'damage condition.',
   'Source clarification: unsupported direct COD claims in the DOCX are not adopted.': 'Dye '
                                                                                       'absorbance '
                                                                                       'alone does '
                                                                                       'not '
                                                                                       'determine '
                                                                                       'COD.',
   '; the packet’s repeated lung example labelled as prostate is not treated as prostate-specific evidence': '',
   'Correction: the DOCX’s direct current–distance proportionality is wrong.': 'Tunnelling current '
                                                                               'is not directly '
                                                                               'proportional to tip '
                                                                               'distance.',
   'Conflicting numerical scan limits in the notes are not universal specifications.': 'Scan limits '
                                                                                       'depend on '
                                                                                       'the '
                                                                                       'instrument.',
   'the source’s MoS₂ example should be stated as an example, not an industry-wide recipe': 'MoS₂ is '
                                                                                            'one '
                                                                                            'example '
                                                                                            'rather '
                                                                                            'than a '
                                                                                            'universal '
                                                                                            'formulation',
   'The supplied course examples classify watches, clocks and sewing machines under fluid-film lubrication; use that stated course classification while recognising that': 'Examples '
                                                                                                                                                                           'include '
                                                                                                                                                                           'watches, '
                                                                                                                                                                           'clocks '
                                                                                                                                                                           'and '
                                                                                                                                                                           'sewing '
                                                                                                                                                                           'machines, '
                                                                                                                                                                           'though',
   'described in these notes': 'used here',
   'The supplied DOCX states tunnelling current is proportional to tip distance.': 'Tunnelling '
                                                                                   'current is not '
                                                                                   'directly '
                                                                                   'proportional to '
                                                                                   'tip distance.',
   'The supplied model equation omits water when writing gluconic acid as product.': 'Water is '
                                                                                     'required when '
                                                                                     'writing '
                                                                                     'gluconic acid '
                                                                                     'as the '
                                                                                     'product.',
   'Source drawing gap: The supplied notes explain the Nitinol cycle but do not include a transformation drawing to extract. Text is complete; this question’s requested drawing remains a source gap.': 'Diagram '
                                                                                                                                                                                                         'unavailable: '
                                                                                                                                                                                                         'a '
                                                                                                                                                                                                         'Nitinol '
                                                                                                                                                                                                         'transformation-cycle '
                                                                                                                                                                                                         'drawing '
                                                                                                                                                                                                         'is '
                                                                                                                                                                                                         'still '
                                                                                                                                                                                                         'needed '
                                                                                                                                                                                                         'for '
                                                                                                                                                                                                         'this '
                                                                                                                                                                                                         'question.',
   'Source drawing gap: The supplied notes describe CO absorption but contain no analyser drawing to extract. The active/NDIR explanation is provided; this question’s requested apparatus drawing remains a source gap.': 'Diagram '
                                                                                                                                                                                                                           'unavailable: '
                                                                                                                                                                                                                           'a '
                                                                                                                                                                                                                           'CO-analyser '
                                                                                                                                                                                                                           'apparatus '
                                                                                                                                                                                                                           'drawing '
                                                                                                                                                                                                                           'is '
                                                                                                                                                                                                                           'still '
                                                                                                                                                                                                                           'needed '
                                                                                                                                                                                                                           'for '
                                                                                                                                                                                                                           'this '
                                                                                                                                                                                                                           'question.'}
  for node in root.iter():
   for field in ["text","tail"]:
    value=getattr(node,field)
    if value:
     for old,new in replacements.items():value=value.replace(old,new)
     setattr(node,field,value)
  return ''.join(html.tostring(n,encoding='unicode') for n in root)
 retained={};retained_prompts={};retained_units={}
 for u in [1,2]:
  doc=html.fromstring((R/f'question-sections/unit-{u}.html').read_text())
  for card in doc.xpath('//details[contains(@class,"study-accordion-item--example")]'):
   id=card.get('id');retained[id]=clean(html.tostring(card.xpath('.//*[contains(@class,"study-example-solution")]')[0],encoding='unicode'));promptnode=card.xpath('.//*[contains(@class,"study-example-question")]')[0];retained_prompts[id]=(promptnode.text or '')+''.join(html.tostring(n,encoding='unicode') for n in promptnode);retained_units[id]=u
 cache={}
 def existing(id):
  if id in cache:return cache[id]
  if id in retained:cache[id]=retained[id];return cache[id]
  q=question_data[id];a=solutions['answers'][id];keys=a.get('modules',[])
  short=short_answer_blocks(q,a)
  if short:
   cache[id]=render_blocks(short,figure);return cache[id]
  if q['source_set'] in ['essay','long'] and len(keys)==1 and not a.get('subpart_answers') and not a.get('source_discrepancy'):
   key=keys[0];target=modules.get(key)
   if key=='biosensor':target=prefix+'6-b' if re.search('glucose|amperometric',q['original_prompt'],re.I) else 'cfe-mid2-2024-07-04-r22-b-5-a'
   if target:
    blocks=copy.deepcopy(midanswers[target])
    if key=='stm' and 'nanomaterial' not in q['original_prompt'].lower():blocks=blocks[1:]
    cache[id]=render_blocks(blocks,figure);return cache[id]
  cache[id]=clean(answer_html(q,solutions));return cache[id]
 def answer(record):
  if record.get('blocks'):body=render_blocks(record['blocks'],figure)
  elif record.get('answer_refs'):body=''.join(existing(id) for id in record['answer_refs'])
  else:body=existing(record['answer_ref'])
  if record.get('answer_refs') or (record.get('answer_ref') and record['id']!=record['answer_ref']):
   root=html.fragment_fromstring(body,create_parent='div');aliases={n.get('id'):record['id']+'--'+n.get('id') for n in root.xpath('.//*[@id]')}
   for n in root.xpath('.//*[@id]'):n.set('id',aliases[n.get('id')])
   for n in root.xpath('.//a[starts-with(@href,"#")]'):
    if n.get('href')[1:] in aliases:n.set('href','#'+aliases[n.get('href')[1:]])
   body=''.join(html.tostring(n,encoding='unicode') for n in root)
  if record.get('correction'):body='<aside class="study-mismatch-note"><strong>Calculation correction</strong><p>'+E(record['correction'])+'</p></aside>'+body
  return body
 def strip_bl(s):return re.sub(r'\[?BL\s*[-–]?\s*\d\]?\.?','',s,flags=re.I).strip()
 def question(record):
  id=record['id'];label=('Short answer' if record['kind']=='short' else 'Problem' if record['kind']=='numerical' else 'Essay')+(' · '+str(record['number']) if record.get('number') is not None else '')
  if id in retained_prompts:prompt=retained_prompts[id]
  else:
   prompt=E(record['prompt']);prompt=re.sub(r'(?<!\w)([a-h]\)|[iv]{1,3}\))(?=\s)',r'<br><strong>\1</strong>',prompt)
  mismatch=' has-math-mismatch' if record.get('correction') or (id in solutions['answers'] and solutions['answers'][id].get('source_discrepancy')) else ''
  return f'<details class="study-accordion-item study-accordion-item--example collection-question{mismatch}" id="{E(id)}"><summary><span class="study-example-summary-copy"><span class="study-example-title">{E(label)}</span><span class="study-example-question">{prompt}</span></span><span class="study-accordion-toggle" aria-hidden="true">+</span></summary><div class="study-accordion-content study-example-solution">{answer(record)}</div></details>'
 units=defaultdict(list);navs=defaultdict(list);used=set()
 for c in intake['collections']:
  content='<h3>'+E(c['title'])+'</h3>'
  if c['kind']=='reference':
   content+='<p>'+E(c['reference_note'])+'</p>'
   module=solutions['modules'][c['reference_module']];content+='<details class="study-tip"><summary>Reference summary</summary><div class="study-tip-content">'+''.join('<p>'+E(p)+'</p>' for p in module['paragraphs'][:2])+'</div></details>'
  for record in c['questions']:
   assert record['id'] not in used,record['id'];used.add(record['id']);content+=question(record)
  if c['filename']=='Problems on hardness .docx.pdf':
   original=html.fromstring((R/'question-sections/unit-1.html').read_text())
   for reference_id,title in [('numericals-opening-example','Opening worked example'),('numericals-conversions','Hardness conversion chart')]:
    original_panel=original.get_element_by_id(reference_id)
    images=''.join(html.tostring(n,encoding='unicode') for n in original_panel.xpath('./div[contains(@class,"source-visual")]'))
    content+=f'<section id="{reference_id}"><h4>{title}</h4>{images}</section>'
  units[c['unit']].append(f'<section class="bank-source-group" id="{c["id"]}">{content}</section>')
  navs[c['unit']].append(f'<a href="{PREFIX}question-banks.html#{c["id"]}" data-bank-unit="{c["unit"]}">{E(c["title"])}</a>')
 # All pre-existing question IDs remain public, including older distinct sheets.
 leftovers=defaultdict(list)
 for id,q in question_data.items():
  if id in used:continue
  leftovers[(q['r25_unit'],q['source_id'],q['source_filename'])].append({'id':id,'prompt':q['original_prompt'],'kind':q['source_set'],'number':q.get('source_question_number',''),'answer_ref':id})
 for id in retained:
  if id not in used:leftovers[(retained_units[id],'retained-unit-'+str(retained_units[id]),'Additional supplied questions')].append({'id':id,'prompt':'','kind':'short' if 'short' in id else 'essay','number':id.rsplit('-',1)[-1],'answer_ref':id})
 for (u,sid,name),qs in leftovers.items():
  group='bank-'+sid.lower();content='<h3>'+E(name)+'</h3>'+''.join(question(q) for q in qs)
  units[u].append(f'<section class="bank-source-group" id="{group}">{content}</section>')
 # Preserve source-group anchors consumed by the individually named collections.
 old_sets=defaultdict(list)
 for q in question_data.values():old_sets[q['source_id']].append(q['id'])
 available={re.search(r'id="([^"]+)"',x).group(1) for xs in units.values() for x in xs}
 for sid,ids in old_sets.items():
  old='bank-'+sid.lower()
  if old not in available:
   u=question_data[ids[0]]['r25_unit'];units[u].insert(0,f'<span id="{old}"></span>')
 # Preserve historical section anchors as unit landing points after regrouping.
 ids={n.get('id') for xs in units.values() for fragment in xs for n in html.fragment_fromstring(fragment,create_parent='div').xpath('.//*[@id]')}
 for unit,record in read('question-bank-relocation.json')['units'].items():
  for old in record['ids']:
   if old not in ids:units[int(unit)].insert(0,f'<span id="{E(old)}"></span>');ids.add(old)
 nav='';body='<div class="bank-view-intro"><p id="bank-view-status" role="status">Viewing Unit 1</p><p>Select a unit or an individual question set. Open a question for its answer.</p></div>'
 for u,title in TITLES.items():
  current=' aria-current="location"' if u==1 else ''
  nav+=f'<details class="source-nav-group" open><summary><a href="{PREFIX}question-banks.html#unit-{u}" data-bank-unit="{u}"{current}>Unit {u} · {E(title)}</a></summary>'+''.join(navs[u])+'</details>'
  aliases='<span id="all-units"></span><span id="existing-answers"></span><span id="source-questions-pending"></span>' if u==1 else ''
  body+=f'<section class="document-page bank-unit" id="unit-{u}" data-bank-unit-section="{u}"'+(' hidden' if u!=1 else '')+'><h2>Unit '+str(u)+' · '+E(title)+'</h2>'+aliases+''.join(units[u])+'</section>'
 page=shell('question-banks.html','Unit-wise Question Bank & Solutions','Question sets, numerical practice and supporting handouts. Unit I opens first.',nav,body)
 for css in ['pages/end-sem-notes','pages/source-notes','pages/practice']:page=page.replace('</head>',f'<link rel="stylesheet" href="styles/new/{css}.css">\n</head>')
 page=page.replace('<body>','<body data-question-bank="true" data-bank-allow-all="false">').replace('</head>','<script src="scripts/new/question-bank-navigation.js" defer></script>\n</head>')
 (S/'question-banks.html').write_text('\n'.join(line.rstrip() for line in page.splitlines())+'\n')
 print('Built 17 individually named handouts; preserved all existing questions and added missing occurrences.')

if __name__=='__main__':build_question_bank()
