# R25 Chemistry — senior-shared notes intake

This change integrates a **selected supplementary revision layer** for Units III, IV and V. It does not complete the prescribed-textbook Text pages, introduce a Question Bank card, solve the saved questions, or change any unit to `ready`. Site reorganisation and chapter-end textbook exercises remain deferred.

## Sources and file decisions

The source is the user's five ZIP uploads from VJNOTES, not an inferred lecturer record. `senior-notes-intake.json` records the original 24 PDF/PPTX files and three additional source variants (a revised bank, DOCX and screenshot). `additional-notes-intake.json` reconciles all 17 files in the latest five ZIPs, including aliases and duplicate evidence. Originals remain in the private intake workspace; no original was deleted and no source scans were uploaded to the public repository.

| File | Decision |
| --- | --- |
| `07 Energy Sources.pdf` — 9 pages | Select the R25 fuel/refining/cracking/Fischer–Tropsch material. |
| `08 Gaseous Fuels & Battery Tchnology.pdf` — 13 pages | Select gaseous fuels, water electrolysis, battery classification, Zn-air, Li-ion, Na-ion comparison and PEMFC. Retain its four embedded Q&As separately for answer review. |
| `09 Polymers.pdf` — 17 pages | Select R25 polymer topics, explicitly flag discrepancies and qualify unsupported claims. |
| `Unit 3.pdf` — 2 pages | Save current Unit III question sheet: 24 short and 11 essays. |
| `Unit 4.pdf` — 1 page | Save Polymers questions: 11 short and 9 essays. Its `UNIT-II` heading is inconsistent with CO-4 and R25; map by contents to Unit IV. |
| `UNIT-3 Questions.pdf` — 2 pages | Older-syllabus question sheet: 24 short and 12 essays. Select current overlap; separate coal analysis, knocking, TEL, methanol cells and solar cells. Retain mixed subparts without deleting the original prompt. |
| `Unit-4 Questions.pdf` — 2 pages | Corrosion questions: 25 short and 8 essays. Reassign to R25 Unit II; separate coatings/tinning content outside explicit syllabus scope. |
| `Unit_3_Notes.pdf` — 23 scanned pages | Older-syllabus overlap. No native text. Pages 1, 5, 10, 15, 20 and 23 were visually sampled; this is not a full transcription. Questions on pp.22–23 are OCR-staged, explicitly unverified. Prefer current typed notes for this release. |
| `1 UNIT III Part 1 Energy Sources [Autosaved].pptx` — 39 slides | Older-syllabus overlap; current selected note supplies the relevant material. Do not import coal-analysis/knocking content as a new R25 requirement. |
| `battery_tech_fuel_cell.pptx` — 27 slides | Battery overlap plus methanol-cell content. Image-heavy content not fully transcribed; prefer the selected current packet. |
| `reserve_n_zinc_air.pptx` — 11 slides | Supporting overlap, largely images; not claimed fully ingested. |
| `Factors Influencing Corrosion.pptx` — 10 slides | Supporting source for R25 Unit II, not Polymers. |
| `Unit 4CORROSION AND ITS CONTROL PPT.pptx` — 66 slides | Supporting source for R25 Unit II, with older-syllabus extras. |
| `unit_4_Notes.pdf` — 16 pages | Supporting corrosion source for R25 Unit II. Existing revision notes remain intact. |
| `unit _4_TextBook.pdf` — 21 pages | Corrosion excerpt. Its book/edition is unidentified; it is not relabelled as the prescribed Jain textbook. |

The initially oversized `chem_unit_6.zip` was confirmed by the user to be a misnamed Unit V archive. It has now been replaced by `chem_unit_5_01.zip`, `chem_unit_5_02.zip` and `chem_unit_5_03.zip`. All three download and pass ZIP integrity checks. The nine distinct PDFs are inventoried as follows:

| Unit V file | Decision |
| --- | --- |
| `10 Spectroscopy and Smart Materials.pdf` — 30 pages | Primary R25 revision selection; all native text read. Formula/classification images sampled. Viewer p.21 is visually blank, not invented missing content. |
| `Unit 5.pdf` — 2 pages | Save 15 short and 10 essay prompts. CO instrument source conflict flagged. |
| `unit_5_Notes.pdf` — 27 pages | Older mixed-topic source. Select self-healing mechanisms pp.8–9; save/filter questions pp.26–27. Lubricants, biochips and synthesis requirements set aside. |
| `1_Nano material.pdf` — 12 pages | Select introductory nanoscale context pp.5/7 only; other analytical techniques and synthesis not imported as current requirements. |
| `2_Nano synthesis.pdf` — 64 pages | Outside explicit R25 Unit V scope; preserve privately. |
| `3_Unit V AFM.pdf` — 16 pages | Supporting overlap; prefer current typed notes. Not a full image transcription. Final video/Screen annotation not imported. |
| `4_Unit V STM.pdf` — 13 pages | Supporting overlap; prefer current typed notes. Not a full image transcription. Final video/Screen annotation not imported. |
| `5_Biosensors.pdf` — 49 pages | Image-heavy supporting overlap; current typed packet supplies core glucose treatment. Last three pages visually sampled; no complete transcription claimed. |
| `7_unit 5  Lubricant.pdf` — 36 pages | Outside explicit current R25 scope; preserve privately, exclude from revision page. |

MuPDF reports unsupported appearance generation for Screen annotations in the AFM/STM decks. Static pages can be read, but this is not a claim that the original video playback was recovered.

## Coverage and limits

- Unit III: 12 revision sections mapped to the 10 syllabus atoms in the existing syllabus record.
- Unit IV: 10 revision sections mapped to the 8 syllabus atoms.
- Unit V: 17 revision sections mapped to the 7 syllabus atoms; the CO instrument conflict remains open.
- Every section records source ID and viewer pages in `unit-3-senior-notes.json` / `unit-4-senior-notes.json` / `unit-5-senior-notes.json`. The intake manifest resolves those IDs to actual supplied files and hashes.
- This is an R25 selection/paraphrase, not a verbatim transcript of every source page. Source files, exclusions and still-unreviewed slide/scan content remain traceable.
- Required drawings remain pending under the figure-production freeze in `AGENTS.md`. Existing approved figures are unchanged. The draft pages have a visible warning and per-topic limits; they do not pretend that prose replaces the required diagrams.
- Na-ion coverage is a characteristics/comparison treatment. It is not presented as a complete construction-and-reaction account absent from this source.
- Kevlar's displayed acid-based condensation scheme is recorded as a simplified scheme; industrial synthesis details require prescribed-book verification.
- Source numerical operating ranges, broad environmental/safety rankings, and universal polymer classifications are not automatically promoted to verified facts.
- Canonical `kb/data/topics.json`, textbook questions, Unit I/II content and publication states remain unchanged.

## Meaning-bearing discrepancies

The original claims are quoted/identified in gold notes in the affected revision topics. Corrected topic headings use the existing shared gold treatment.

| Source | Discrepancy and verification |
| --- | --- |
| Energy p.3 | “Cycloparaffins or naphthalene” confuses a saturated-ring class with a particular aromatic compound. The class is naphthenes; flag the original wording. |
| Energy p.6 | “Coal embedded in the catalyst” conflicts with the same process description identifying carbon deposited during cracking. Regeneration burns deposited coke. |
| Batteries p.3 | “Only green and blue hydrogen are reliably zero-carbon” conflicts with the description of carbon-containing feedstocks and incomplete carbon capture. Do not teach blue hydrogen as automatically zero-carbon. |
| Batteries p.9 | Electrons said to travel in the opposite direction to Li ions. The half-reactions on the same page show both moving from negative-electrode side to positive-electrode side on discharge, along different paths. The printed `Li` in `LiC6 → C6 + Li + e−` also lacks the positive charge required by charge balance. |
| Polymers pp.4–6 | The tables equate condensation with thermosetting and classify nylon as a thermoset. The linear nylon-6,6 structure in the same packet is a counterexample to that equivalence. Polymerisation route and thermal response are distinct classifications; nylon is thermoplastic. |
| Polymers question sheet, short Q5 | The prompt says Teflon behaves as a thermoset; the note's own thermoplastic list includes PTFE. Preserve and flag the false premise; do not author a justification for it. |

Other claims are **pending/withheld**, not advertised as verified corrections: the universal DP=600 boundary; pendant methyl groups as proof of chain branching; electrolyser temperature disagreements; the 10⁻⁷ mol/L electrolysis claim; PTFE's quoted 350°C as an unspecified service limit; broad SMP/PLA safety and biodegradability claims; battery lifecycle, cost, emissions and safety absolutes. Their treatment is visible under “Limits and pending checks”. No external source was silently used to fill missing theory.

## Question staging

`question-bank-pending.json` saves **244 typed question occurrences**, including source duplicates, plus two unverified OCR page blocks. These are not 244 unique, approved or solved questions. Unit V adds 25 current-sheet questions and 40 older-packet questions.

- 170 retained candidates;
- 3 questions requiring premise review;
- 46 out-of-scope records, preserved rather than deleted;
- 6 mixed-part records;
- 3 supporting records;
- 11 source answers requiring review (four embedded Q&As and seven DOCX model answers);
- 5 question occurrences requiring CO instrument source clarification.

Thirty-nine exact-normalised repeated occurrences link to their earlier record. Near-duplicates are not declared identical. Each record has source filename/ID, starting viewer page, original set/number, R25 unit, prompt, selection reason and solution status. Labelled letter subparts are retained structurally where present. No marks, dates, solutions or PYQ identities were invented. These data must be filtered and academically reviewed before any future question-bank UI.

## Additional Unit V discrepancies and open checks

| Source pages (primary 30-page packet) | Treatment |
| --- | --- |
| 3/5 | Loss of UV absorbance does not alone establish complete mineralisation or a unique molecular structure. The packet's own limitations conflict with those stronger claims. |
| 5–7 | Separate thermal imaging from wavelength-resolved molecular absorption spectroscopy. Do not equate every IR image with a molecular spectrum. |
| 8–10 | Passive/source-free CO detector description conflicts with an explicit IR source in its chamber steps. Record the source-driven absorption example, preserve the original question wording, and leave the intended passive apparatus unresolved. Do not change the official syllabus or guess the lecturer's intended design. |
| 13 | The prostate-cancer example repeats lung/sputum wording. Exclude the purported prostate-specific method; tumour spectra are illustrative research examples, not universal diagnostic rules. |
| 16/22 | Constant-height scanning fixes tip height relative to a reference plane, not the local gap over uneven terrain. Current varies with gap. |
| 17/19/20/22 | STM/AFM resolution ranking, AFM scan-size units and environment claims contradict one another. No guessed universal ranking or limit substituted. |
| 24 | The opening autonomous-only definition conflicts with the same page's non-autonomic category. Retain the broader intrinsic/extrinsic and autonomic/non-autonomic distinctions. |
| 30 | Glucose-sensor numerical performance is not identified with a specific device; do not turn it into universal specifications or a claim about every commercial sensor. |

The main remaining source request is **lecturer/prescribed-reference clarification of the intended passive-IR CO setup**. Other uncertain specifics are withheld or qualified; canonical textbook verification and source-based figures remain pending.


## Latest five-unit packets: duplicate reconciliation and integration

The additional upload contains 17 files. Ten are exact byte matches to earlier supplied originals (including the Units I/II banks and the four-problem hardness sheet); three note PDFs have identical extracted text and **identical rendered pixels on all 60 pages compared** despite different PDF bytes; the Polymers bank has identical normalised wording. These 14 files reuse the existing teaching flow and answers, without creating repeated topics or solutions.

The three remaining files are a revised Unit V sheet (12 short + 10 essays), a new undated spectroscopy DOCX, and a screenshot of a nanomaterials definition/classification. Their origin is user-supplied notes; no author, lecturer approval or lecture date is inferred.

- Keep the fuller earlier Unit V bank (15 short + 10 essays) and retain the revised sheet as 22 source occurrences with explicit variant links; do not discard the earlier three short questions.
- The DOCX supplies 22 final-bank prompts and seven model-answer occurrences. Its final heading says “WITH ANSWERS” but that final section has no paired answers. The model prose is saved as source-authored, **unverified**, not a VNR answer key.
- Merge a nanoscale definition into the existing nanomaterials section, and reversible hydrogen-bonding/Diels–Alder examples into the existing intrinsic-healing section. No separate packet dump.
- The DOCX's `tunnelling current ∝ distance` conflicts with the existing approach/retraction account. Flag it in the existing STM topic.
- The DOCX's acid-forming glucose reaction omits water. Retain the main source's lactone-forming reaction, then show lactone hydrolysis and the atom-balanced acid net reaction as a PankusDesk equation check. C₆H₁₄O₉ is present on both sides of the combined reaction.
- Its passive-IR CO description repeats the existing source conflict; repetition is not independent verification. Lecturer/prescribed-reference clarification remains pending.
- Do not import unsupported direct COD estimation or the screenshot's dimensional-classification convention as extra R25 requirements. The original screenshot is not published; figure assets remain frozen.

The existing Units I/II answered banks are referenced from the staged bank, rather than copied with second answers. Source authorship and PankusDesk answer authorship remain distinct. See `additional-notes-intake.json` for every filename, hash and reuse decision.

## Validation

The three required repository checks pass:

- `python3 scripts/tools/verify_college.py`
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`

These checks do not certify academic completeness. Browser results and preview acceptance checks are reported in the PR handoff.

The standalone subject JSON Schema has a **pre-existing** incompatibility with the existing grouped revision card: `studyResources[0].id` and `unitResources` are rejected. Comparing validation errors with `origin/main` gives the identical error and no new errors. The generic college validator understands this existing card pattern and passes. No shared schema was changed for this intake.

Chromium browser checks passed at 1440px and 390px: Unit III/IV revision links, all local anchors, expandable limit panels, source-discrepancy notes, 21/3 MathJax expressions with no MathJax errors, and no page-wide horizontal overflow. The updated Unit V page was separately checked at both widths: 19 local anchors, 5 MathJax expressions, no JavaScript/MathJax errors, working CO-discrepancy deep link/dropdowns and no page-wide overflow. All three revision links and draft states appear on the subject card. The `/Pankusdesk/` base-path route was checked with a simulated `github.io` hostname. Screenshots were inspected. Browser CDN requests were served through Python's configured CA trust because Chromium does not trust the managed proxy certificate; TLS verification was preserved. This is local browser verification, not a claim that the Vercel deployment was visually checked.

The user requested a separate PR because #33 is unmerged. The new `feat/chemistry-r25-units3-5` branch includes the Units III/IV work plus Unit V, based on main; it does not require merging #33 first. PR #33 remains unchanged and unmerged. Review the new combined PR instead of merging both overlapping PRs.
