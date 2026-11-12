# Chemistry notes and answer consolidation

The bank now contains **458 solved entries**: 374 newly authored entries (244 previously typed prompts plus 130 additional embedded question occurrences), and 84 retained entries (80 Unit I/II questions and four hardness problems). Repeated sheets retain their own numbering and source identity; common answers use shared modules to prevent divergent versions. These are supplied question banks, not authenticated PYQs or lecturer-approved answer keys.

## Private reference corpus

The private `chemistry-reference.json` is kept outside the public Git checkout. It holds source identities, page/record text, low-text-page OCR, existing knowledge JSON, retained solutions, source conflicts, authored answers and a topic/question retrieval index. It is a retrievable reference file, not permanent model training. `reference-corpus-audit.json` contains a checksum and non-private accounting only. Source PDFs/PPTs, textbook photographs and the administrative student report are not committed.

All 71 inventoried identities have been resolved; the student report and unusable one-page export remain excluded from scientific evidence. Duplicate exports remain identifiable. Native/OCR text extraction does **not** certify every raster equation, embedded image, slide layout or diagram. Legacy PPT text is extracted from binary text records; it is not misreported as a rendered slide-by-slide visual transcription. Textbook captures are retained privately as a separate OCR collection; deferred chapter-end exercise publication is unchanged.

## Answers and source qualifications

Supplied notes are the first source. General chemistry is used only for source gaps/contradictions and is explicitly qualified in answer metadata and displayed explanations. Older-syllabus questions are still answered and labelled supplementary; original prompts are not silently filtered away. Long answers include process/construction/working/equations/applications as relevant; short answers use focused selections, and labelled subparts use separate panels.

Checks address PTFE classification, Kevlar acid versus acid-chloride routes, hydrogen production, lithium-ion charge/direction, fluidized-bed terminology, STM gap/current, active CO sensing versus passive thermal detection, glucose atom balance, coal analysis and conditional material-performance claims. No unprovided numerical measurements, exam limits or teacher approval are invented. Two retained Unit I answers were updated with explicit comparison records: hard scale/EDTA (textbook pp.7–8) and the newer MF range (handout PDF pp.61–62). Original questions, IDs and figure binaries are preserved; the original relocation hash remains in the revision record.

## Pages and navigation

Question banks live in `question-banks.html`, with exactly six left-nav choices (five units plus Consolidated) and Back to top above Contents, including on phones. Notes remain separate. New source qualifications are additive labelled explanations on the relevant Unit IV/V notes. Stale “future bank / answers pending” messages are removed. Existing notes-question fragment redirects continue working.

## Approved source diagrams and remaining source gaps

The user authorised unchanged extraction/publication of supplied handout diagrams. Eleven selected embedded images (386,325 bytes total) accompany the related long answers and notes. Their PDF identities, pages, embedded object numbers, byte/pixel checksums, dimensions and semantic comparisons are recorded in `source-figures.json`. Existing approved assets remain unchanged. No diagram is redrawn, relabelled, recoloured or recompressed. The PEMFC diagram is on PDF p.12, correcting the earlier proposed p.13 reference.

Two explicit drawing requests remain source gaps: Nitinol’s transformation cycle and an IR CO-analyser apparatus. The supplied relevant packets contain prose but no suitable image; the DOCX has no embedded media. These answers retain precise gap notices. A polymer shape-memory illustration is not substituted for an alloy transformation, nor a passive motion sensor for an active absorption analyser. The existing breakpoint graph fulfils the duplicated Unit I illustration request. Other explicit diagram requests now have their original source illustrations. The PR is not declared fully diagram-complete or lecturer-approved; textbook publication states remain unchanged.

## Rebuild and verification

- `python3 scripts/tools/build_chemistry_collections.py`
- `python3 scripts/tools/verify_chemistry_collections.py`
- `python3 scripts/tools/verify_chemistry_answers.py`
- `python3 scripts/tools/verify_cfe_revision_structure.py`
- Three baseline college/BEE/MAC verifiers and detailed Chemistry browser regression.

The answers verifier checks coverage, real source IDs/page bounds, paragraph selections and subpart labels, independently recomputes repeated hardness cases, and checks selected atom/charge balances. Browser verification covers desktop/tablet/phone, filtered/consolidated views, answer deep links, old redirects, Back to top, figures and the GitHub Pages base path. Passing structural tests is not proof of teacher approval or every source drawing’s correctness.
