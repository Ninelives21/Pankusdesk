# Chemistry college/senior notes consolidation

This review covers all five units and the latest supplied archives. It is an inventory and selected-content consolidation, not certification that every slide, scan, figure or historical solution is complete.

## What is published

- One College & Senior Notes collection links all five existing notes pages, with per-unit source inventories and printing guidance. The separate Unit-wise Question Bank & Solutions page has exactly six contents choices: Units I–V and Consolidated · All units. Its Back to top control stays above Contents. Selecting a unit filters the same single copy of the content; Consolidated reveals all five units.
- The inventory has 71 distinct byte identities and 110 recorded archive/filename appearances. Exact duplicates share a record; confirmed re-exports have explicit equivalence links rather than another teaching copy. Different formats without proven visual identity remain separate records.
- Original Unit I–V topic prose, existing answers, figures, source anchors and correction panels are retained. Standalone Unit I/II question banks and the hardness problem sheet now live in question-banks.html; integral source teaching examples remain in Notes. Four labelled, source-linked PankusDesk explanations are additive: membrane selection, anodic area effect, catalyst contact/heat transfer, and FRP fibre/matrix roles.
- The question collection displays all 244 already-recorded typed prompts in nine source groups. Original numbering, old-syllabus classifications and both Unit V variants remain separate. The 80 existing Unit I/II question-bank entries and four hardness problems are moved intact into question-banks.html. Their original IDs remain there; old notes-page fragment URLs redirect to the matching bank entry.
- Additional embedded question collections are listed with source pages and pending transcription status. The two OCR pages explicitly marked not-for-display are not published as verified question wording. Unverified source model answers are not promoted to solutions.
- Textbook notes, unit publication states, existing approved figure assets and textbook/class-note data are unchanged.

## Unit-by-unit selections and remaining work

1. **Water:** retain the original two source transcripts, numericals and question answers. Add qualitative membrane selection from the 70-page source, without copying numeric ranges affected by source/encoding differences. The WIL student report and unusable one-page file remain excluded. Mixed Unit I/II slides are described by their real page ranges. Legacy PPTs, many slide images and additional embedded question pages still need full visual/source review.
2. **Electrochemistry and corrosion:** retain all existing corrections and figures. The additional 14-page corrosion handout supports the area-effect explanation, which agrees with the existing answer. Supporting corrosion decks and older coating lessons are not silently promoted to core requirements. Their full visual transcription remains pending.
3. **Energy and batteries:** retain the two typed primary packets and add the selected cracking explanation. Moving-bed/fluidised-bed wording is explicitly source-specific. Coal analysis, knocking and methanol-cell sources remain supplementary/outside the explicit R25 core. Existing required process/battery figures remain pending. Handwritten/image-heavy notes are not certified as a full transcription.
4. **Polymers:** retain the R25 packet and add source-linked fibre/matrix roles. Older PET/PMMA/polycarbonate/Bakelite, manufacturing and extended thermal-property sources remain separately inventoried. The 27-page scan and legacy conducting-polymer PPT are not yet fully visually ingested. Required polymer reaction/figure checks remain pending.
5. **Spectroscopy and materials:** all latest files reconcile to existing sources. Retain all existing qualifications; no duplicate source is independent confirmation. Supporting STM/AFM/biosensor image pages, multimedia and required source figures remain pending. Detailed nano-synthesis and lubricant files are outside the explicit core.

## Answer-impact review

`consolidation-answer-review.json` records the checked relationships between the selected additions and existing/pending questions. Existing Unit I/II answers are unchanged. The MF pore-size range discrepancy is preserved for follow-up; it is not silently corrected. This limited impact check does not renew verification of all historical answers.

## Source/storage boundary

No PDF, PPT, scan, private student report or new drawing is committed. Originals remain in the private intake workspace. No figure is generated, redrawn, recoloured or replaced under this consolidation. The current figure-production freeze remains in force. Existing pending drawing work is visible on the notes pages and must not be hidden by a ready-status promotion.

## Rebuild and verification

- `python3 scripts/tools/build_chemistry_collections.py` rebuilds the collection/question pages and additive unit panels from the committed inventory and additions JSON.
- `python3 scripts/tools/verify_chemistry_collections.py` checks source identities, all typed prompts, cited additions and local links/anchors.
- Run the three baseline college/BEE/MAC validators and the existing Chemistry structure/browser checks. Screenshots, HTML character accounting and link checks do not by themselves establish academic or figure correctness.
