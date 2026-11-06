# R25 Chemistry — senior-shared notes intake

This change integrates a **selected supplementary revision layer** for Units III and IV. It does not complete the prescribed-textbook Text pages, introduce a Question Bank card, solve the saved questions, or change any unit to `ready`. Site reorganisation and chapter-end textbook exercises remain deferred.

## Sources and file decisions

The source is the user's two ZIP uploads from VJNOTES, not an inferred lecturer record. `senior-notes-intake.json` inventories all 15 PDF/PPTX files with hashes, sizes, actual page/slide counts, classification and reasons. Originals remain in the private intake workspace; no original was deleted and no source scans were uploaded to the public repository.

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

`chem_unit_6.zip` exceeded the 32 MiB transfer limit and was not downloaded or inspected. The user subsequently confirmed that it was misnamed and is intended as **Unit V**, and will resend it in smaller parts. No Unit V coverage is inferred from its filename.

## Coverage and limits

- Unit III: 12 revision sections mapped to the 10 syllabus atoms in the existing syllabus record.
- Unit IV: 10 revision sections mapped to the 8 syllabus atoms.
- Every section records source ID and viewer pages in `unit-3-senior-notes.json` / `unit-4-senior-notes.json`. The intake manifest resolves those IDs to actual supplied files and hashes.
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

`question-bank-pending.json` saves **128 typed question occurrences**, including source duplicates, plus two unverified OCR page blocks. These are not 128 unique, approved or solved questions.

- 94 retained candidates;
- 3 questions requiring premise review;
- 20 out-of-scope records, preserved rather than deleted;
- 4 mixed-part records;
- 3 supporting records;
- 4 embedded source Q&As requiring answer review.

Eleven exact-normalised repeated occurrences link to their earlier record. Near-duplicates are not declared identical. Each record has source filename/ID, starting viewer page, original set/number, R25 unit, prompt, selection reason and solution status. Labelled letter subparts are retained structurally where present. No marks, dates, solutions or PYQ identities were invented. These data must be filtered and academically reviewed before any future question-bank UI.

## Validation

The three required repository checks pass:

- `python3 scripts/tools/verify_college.py`
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`

These checks do not certify academic completeness. Browser results and preview acceptance checks are reported in the PR handoff.

The standalone subject JSON Schema has a **pre-existing** incompatibility with the existing grouped revision card: `studyResources[0].id` and `unitResources` are rejected. Comparing validation errors with `origin/main` gives the identical error and no new errors. The generic college validator understands this existing card pattern and passes. No shared schema was changed for this intake.

Chromium browser checks passed at 1440px and 390px: Unit III/IV revision links, all local anchors, expandable limit panels, source-discrepancy notes, 21/3 MathJax expressions with no MathJax errors, and no page-wide horizontal overflow. The `/Pankusdesk/` base-path route was checked with a simulated `github.io` hostname. Screenshots were inspected. Browser CDN requests were served through Python's configured CA trust because Chromium does not trust the managed proxy certificate; TLS verification was preserved. This is local browser verification, not a claim that the Vercel deployment was visually checked.
