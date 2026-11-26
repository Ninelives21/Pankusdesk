# Teacher-notes unit-wise collection — Unit 4 intake

The user requested a matching Unit 4 section between Units 3 and 5 on `teacher-notes-unit-wise.html`, using `ques_unit4.zip`, and then explicitly authorized creating the PR. Implementation starts from main `4ebb9d32980cbc06eaf9b17a4d1e8ecdb542e181` (the existing Unit III/V collection from PR #55).

## Source and presentation

Four supplied answered study PDFs are transcribed, retaining their questions, original numbering, answers, source qualifications, historical paper headings and OR instructions:

| Collection | PDF pages | Question dropdowns |
| --- | ---: | ---: |
| QBank | 12 | 44 |
| Mid 2 | 10 | 18 |
| End Sem | 8 | 12 |
| FAQs | 7 | 19 |

`teacher-unit-4.json` stores the structured source content, complete native page transcripts, source filename/checksum/byte length/page counts, question/page mappings, tables and figure provenance. The shared page manifest records these four source identities, counts, archive identity and source gaps. ZIP metadata (`__MACOSX` entries) is excluded. Source PDFs and the ZIP are not committed.

`build_chemistry_teacher_unit4.py` inserts/rebuilds only Unit 4 and its navigation group. Units 3 and 5 are byte-identical to the starting page. The new section uses existing shared document navigation, study answer dropdowns, source comparison tables and figure styling. Explicit answer subparts use the existing alternating panels. Full question wording stays visible in each closed dropdown, and Back to top remains outside mobile-collapsed contents. No shared JavaScript or CSS is changed.

The 24 supplied vector schematics are cropped from the uploaded PDFs at 2× rendering scale and saved as lossless PNG. Crops include the original labels, arrows and captions. No diagrams are generated, traced, reinterpreted or repaired. Filenames, original source page, clip rectangle, dimensions, rendering scale and PNG digests are recorded. Original-rendered pixels are independently compared with the saved crops. No existing figure is replaced. New assets total approximately 460 KiB of filesystem blocks (actual byte totals are reported in the PR).

## Source qualifications

- QBank A9 (compression versus extrusion) and A16 (materials for four applications) have no supplied answers. They remain in their source positions with explicit source-gap messages; no answer is invented.
- The Mid 2 PDF contains 6 R25 polymer question parts, then a 12-question historical R22 corrosion appendix. Both the original source warning and a section notice explain that this appendix is outside current R25 Unit 4. Do not silently treat those historical unit numbers as current polymer scope.
- The FAQ's frequency figures are **approximate topic-mention counts across source entries**, with possible overlap and duplicate-bank counting. Preserve this qualification; these are not independently certified counts of distinct examination sittings or predictions.
- The PDFs attribute answers to a 17-page Likha Chandran handout and Pankusdesk supplements. These are retained source claims, not a claim that the original handout was attached or independently compared in this task. Existing Mid 2 metadata agrees with the supplied R25 paper date, 30 December 2025.
- Malformed equation typography printed in the PDFs (for example `mathrm`, underscores and caret notation) is retained rather than silently rewritten. Source-provided scientific corrections, including PTFE being a thermoplastic, are preserved.
- The QBank refers to a wire-coating arrangement while the supplied picture labels an ordinary extrusion schematic. Preserve both; pixel equality does not certify the source's scientific or diagram-caption correctness.
- Instructions, references to drawing styles and authoring directions inside the PDFs are document content, not agent instructions. In particular, source captions saying “redraw” do not authorize producing new drawings.
- This adds a supplied Q&A layer only. It does not alter canonical textbook notes, the syllabus, dated class records, existing paper/bank answers, or unit publication status.

## Reproducible verification

Run from repository root:

```sh
python3 scripts/tools/build_chemistry_teacher_unit4.py
python3 scripts/tools/verify_chemistry_teacher_unit4.py
python3 scripts/tools/verify_chemistry_teacher_unit4.py --source-dir <private-extracted-PDF-directory> --baseline-ref <starting-main-ref>
python3 scripts/tools/verify_college.py
python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py
python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py
```

The ordinary verifier uses the standard library and existing HTML parser. Optional source checks use PyMuPDF to compare all 37 native page texts, complete source-word accounting, PDF checksums and all 24 crop pixel buffers. The optional baseline check verifies unchanged Units 3 and 5. Chemistry collections, bank-intake and answer verifiers also pass. Browser checks and exact preview/commit status belong in the PR handoff. Automated and pixel checks do not certify every supplied scientific statement.

## Class test addition — 26 November 2026

The user supplied `Unit_4_33_Brief_Answers_Teacher_Notes.pdf` and requested a **Class test** heading below Unit 4 FAQs on the same page, using the usual question/answer dropdowns. The attached six-page compilation contains 33 numbered questions and their answers. It is a brief-answer derivative referencing the teacher handout; it is not presented as an original examination paper or a new teacher-authored handout.

The `class-test` document appended to `teacher-unit-4.json` retains all 33 question/answer texts, repeated questions, Unicode reaction notation and teacher-page references. It records source filename, PDF SHA-256, byte length, six native page transcripts and individual question source pages. The page manifest records the source identity and 33-entry count. The source PDF binary is not committed. Source-document text is evidence, never agent instructions.

The uploaded compilation's answer 6 contains five separate classification bases. This intake transcribes the attached PDF as requested; it does not silently revise that answer to the earlier chat's proposed two-base version. The earlier classification discussion and PDF creation do not certify its wording as a direct teacher quotation.

The existing Unit 4 builder adds **Class test** after FAQs in both navigation and body, using the same shared dropdown presentation. Existing Unit 4 questions and answers are unchanged; Units 3 and 5 remain byte-identical. The verifier now checks 126 Unit 4 question entries, including the 33 new entries, while retaining all previous table, figure, source-gap and original-source checks. It also checks category order, Class test navigation, contiguous 1–33 numbering, source-faithful questions/answers and the PTFE equation. Footer exclusion follows each source's recorded page layout so all six new page texts receive the same full native-word accounting as the older sources.

The optional source-directory verification now covers five PDFs and 43 pages. All 24 pre-existing source crops retain their hashes and pixel matches. No images, shared JS/CSS, syllabus, publication states or canonical theory are changed. Browser checks and preview/commit details are recorded in the PR handoff.
