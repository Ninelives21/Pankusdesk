#!/usr/bin/env python3
"""Verify original-image identities, source locations and required-diagram accounting.
Use --corpus to compare the public extracted bytes with the private supplied PDFs.
"""
from pathlib import Path
import argparse,hashlib,json
from verify_cfe_revision_structure import Document
ROOT=Path(__file__).resolve().parents[2];SUB=ROOT/'college/1-1/chemistry-engineers';REV=SUB/'revision'
def load(p):return json.loads(p.read_text())
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--corpus',type=Path);args=parser.parse_args()
 manifest=load(REV/'source-figures.json');inventory=load(REV/'source-inventory.json');bank=load(REV/'question-bank-pending.json');solutions=load(REV/'question-bank-solutions.json');sources={s['id']:s for s in inventory['sources']};figures={f['id']:f for f in manifest['figures']}
 assert len(figures)==len(manifest['figures'])==11
 assert sum(f['bytes'] for f in figures.values())==manifest['total_asset_bytes']
 qdoc=Document((SUB/'question-banks.html').read_text());private={}
 if args.corpus:
  import fitz
  private={s['id']:s for s in load(args.corpus)['sources']}
 for id,f in figures.items():
  original=sources[f['source_id']];assert original['sha256']==f['source_sha256'];assert 0<f['source_pdf_page']<=original['pages_or_slides'];assert f['semantic_comparison'];assert f['review_state']=='compared_with_supplied_source_page'
  path=ROOT/f['asset'];assert path.parent==SUB/'assets/handout-figures';binary=path.read_bytes();assert len(binary)==f['bytes'];assert hashlib.sha256(binary).hexdigest()==f['asset_sha256'],id
  if private:
   source=Path(private[f['source_id']]['private_path']);assert hashlib.sha256(source.read_bytes()).hexdigest()==f['source_sha256'];doc=fitz.open(source);page=doc[f['source_pdf_page']-1]
   assert any(i['xref']==f['embedded_xref'] for i in page.get_image_info(xrefs=True)),id
   image=doc.extract_image(f['embedded_xref']);assert image['image']==binary,(id,'embedded image changed')
   assert (image['width'],image['height'])==(f['width'],f['height']);assert hashlib.sha256(fitz.Pixmap(doc,f['embedded_xref']).samples).hexdigest()==f['decoded_pixel_sha256']
  if f['notes_anchor']:
   unit=original['unit'];notes=Document((SUB/f'end-sem-unit-{unit}.html').read_text());topic=notes.ids[f['notes_anchor']]
   assert any(n.tag=='figure' and n.attrs.get('data-source-figure')==id for n in topic.elements()),(id,'missing from relevant notes topic')
 gap_questions={qid:g for g in manifest['source_gaps'] for qid in g['question_ids']};assert len(gap_questions)==2
 accounted=0
 for q in bank['questions']+bank['additional_questions']:
  if not solutions['answers'][q['id']].get('diagram_required'):continue
  node=qdoc.ids[q['id']];images=[n for n in node.elements() if n.tag=='img']
  if q['id'] in gap_questions:
   assert not images and 'Diagram unavailable:' in node.text(),q['id']
   assert solutions['answers'][q['id']]['figure_status']=='source_drawing_unavailable_in_supplied_handouts'
  else:assert images,(q['id'],'required diagram not supplied or gap not recorded')
  accounted+=1
 for node in qdoc.nodes:
  if node.tag!='figure' or 'data-source-figure' not in node.attrs:continue
  id=node.attrs['data-source-figure']
  if id not in figures:
   extra={f['id'] for filename in ['mid-2-source-figures.json','question-bank-intake-figures.json'] for f in load(REV/filename)['figures']}
   assert id in extra,id
   continue  # Extra identities/placements are checked by verify_chemistry_bank_intake.py.
  f=figures[id];imgs=[n for n in node.elements() if n.tag=='img'];assert len(imgs)==1
  img=imgs[0];assert img.attrs['src']==f['asset'];assert img.attrs['alt']==f['alt'];assert img.attrs['width']==str(f['width']);assert img.attrs['height']==str(f['height'])
  assert f['title'] in node.text()
 print(f'CHEMISTRY SOURCE FIGURES: PASS — 11 image identities, {accounted} explicit drawing requests accounted, two precise source gaps'+('; private PDF image bytes and pixels match' if private else '')+'.')
if __name__=='__main__':main()
