# Unit 2 — completed ROS integration and discrepancy decisions

The user explicitly authorized ROS production for the Unit 2 notes and answers and resolution of the flagged statements. This lifts the figure-production freeze for this task only. Unit 1 and existing approved images remain unchanged. Canonical textbook topic data and unit publication states remain unchanged.

## Images and answer completeness

- All 18 original-source assets are integrated in the notes.
- Relevant answers contain their figures inside the dropdown; multipart answers put the figure in the corresponding part.
- Every one of the 44 question-bank entries has a recorded required/useful/not-needed figure assessment. Essay 1 explicitly requires a diagram. Essay 4 reuses the existing approved Zn/SHE measurement diagram unchanged.
- Original prompts, given values and numbering are retained. All answers remain labelled PankusDesk-authored.

## Resolved review items

### Nernst notation and explanation — correction
Use Q, the reaction quotient: E = E° − (RT/nF) ln Q. At equilibrium Q = K and the complete-cell EMF is zero. For a forward spontaneous cell approaching equilibrium at fixed temperature, ln Q increases and the cell EMF falls towards zero. No derivation is required.
Evidence: `kb/data/topics.json#u2-emf-electrochemical-cell`, [https://goldbook.iupac.org/terms/view/09068](https://goldbook.iupac.org/terms/view/09068)

### SHE potential convention — convention
SHE has zero standard potential by definition; it is not a small measured positive potential. The sign of a different half-cell is assigned relative to SHE and the reduction-potential convention.
Evidence: `kb/data/topics.json#u2-reference-electrodes-she`, `kb/data/topics.json#u2-electrode-potential`

### SHE source claims conflict — convention
Impurity poisoning and liquid-junction potentials are different effects, not mutually contradictory claims. Platinum can be poisoned by impurities; a suitable salt bridge reduces junction-potential errors. Being a primary reference does not remove either issue. The earlier combined “conflict” flag was too broad.
Evidence: `kb/data/topics.json#u2-reference-electrodes-she`

### Calomel reaction and Nernst discrepancy — correction
Hg₂Cl₂(s) + 2e⁻ ⇌ 2Hg(l) + 2Cl⁻. Both sides have charge −2. Hence E = E° − (RT/2F) ln(aCl⁻²) = E° − (RT/F) ln aCl⁻. The original Hg⁺ product and the missing factor 1/2 in front of ln(aCl⁻²) were errors.
Evidence: `comparison table-reference electrodes.pdf p.1`, `charge balance and Nernst substitution`

### Calomel potential values conflict — correction
Use +0.2422 V versus SHE for saturated KCl at 25°C, consistent with the supplied table and existing Jain & Jain record pp.292–293. The isolated +0.2442 V substitution is not used for that stated condition. For 0.1 N KCl the handout says +0.3338 V and the existing book record +0.3335 V; do not mix values from different tables. These concentration-specific potentials are not all the thermodynamic E° of the same reaction.
Evidence: `kb/data/topics.json#u2-calomel-electrode`

### Glass-electrode expressions conflict — convention
Under the existing book convention EG = EG° + 0.0592 pH at 25°C. For glass on the left and saturated calomel on the right, Ecell = Eright − Eleft = 0.2422 − EG° − 0.0592 pH. The positive and negative slopes refer to different measured potentials; reversing the leads also reverses the sign. EG° is a calibration offset, not SHE’s assigned zero.
Evidence: `kb/data/topics.json#u2-ion-selective-glass-electrode`

### Printed oxidation mechanism — correction
For valency n, write 2M + (n/2)O₂ → M₂Oₙ, then reduce subscripts to the empirical oxide formula where appropriate. The source figure’s “MO” is only schematic shorthand; it is balanced as MO only for a divalent metal. Original figure pixels remain unchanged.
Evidence: `kb/data/topics.json#u2-chemical-corrosion`, `atom and charge balance`

### Pilling–Bedworth example — textbook check pending — qualification
For the supplied exercise use the handout’s intended answer W: 3.6 > 2.0 > 1.6 under its simplified larger-ratio rule. This is a conditional course-model answer, not a universal oxidation-rate ranking. In real oxide systems, high volume expansion can cause stress and buckling; ratio alone does not determine corrosion resistance. No different exam-key answer is inferred.
Evidence: `Corrosion.pdf p.4`, `kb/data/topics.json#u2-chemical-corrosion`, [https://pmc.ncbi.nlm.nih.gov/articles/PMC9842761/](https://pmc.ncbi.nlm.nih.gov/articles/PMC9842761/)

### General anodic equation — correction
M → Mⁿ⁺ + ne⁻. The product-ion charge must equal the number of electrons released. For iron, Fe → Fe²⁺ + 2e⁻. The original general M⁺ + ne⁻ was valid only for n = 1.
Evidence: `kb/data/topics.json#u2-chemical-corrosion`, `charge balance`

### Sacrificial-anode limitations — source check pending — correction
A sacrificial system supplies galvanic current without an external DC source. Limited driving voltage can make it unsuitable where current demand or electrolyte resistance is high; consumption requires replacement and monitoring. Bare metal can be protected, but a larger exposed area generally needs more current/anode capacity. Thus “uncoated parts cannot be protected” and “high starting current is required” are not general limitations.
Evidence: `Corrosion.pdf pp.16–18`, `the supplied bare-metal protection composite and galvanic-current mechanism`

## Additional ISE consistency correction

The existing textbook-led ISE record explicitly includes interfering ions, selectivity coefficients and indirect CO₂ sensing. Absolute “ignores other ions” and “cannot measure neutral molecules” claims were corrected accordingly; original wording remains in the ledger.

## Evidence limits and source fidelity

The local textbook-led records in `kb/data/topics.json` were available and checked against the study notes; this is not a claim of a new raw-book screenshot inspection. The calomel reaction is independently balanced and supported by the supplied comparison sheet. The existing textbook-led calomel record itself has a different formula typo; it was not used as the authority for reaction stoichiometry and was not silently modified.

The Pilling–Bedworth course exercise is resolved as **W under the supplied simplified course model**. It is not asserted to establish a universal real-world ranking; the physical caveat is supported by [Yankova et al., Nature Communications 14, 250 (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9842761/), introduction. The discussion is a verification note, not a replacement for prescribed theory. The Nernst definition is also supported by [IUPAC](https://goldbook.iupac.org/terms/view/09068).

Some original images are low-resolution/faint, the illustrated summary has source clipping, and the SHE pictures contain a source label error. ROS intentionally retains these original limitations; captions teach the correct interpretation. See [the register](unit-2-ros-register.md).

## Review checks

- [ ] Open the Unit 2 notes and Essay 1: expect the same original Daniell diagram, with electron path and terminal labels visible; click for full size.
- [ ] Open Essays 8 and 9 on a phone: expect each answer subpart to contain its matching figure, with no page-wide horizontal scrolling.
- [ ] Open Short Q17, calomel and glass-electrode notes: expect a complete conditional W answer, balanced calomel equations and explicit glass-potential polarity/offset, with no unresolved-check placeholders.
- [ ] Inspect a SHE picture: expect its original pixels and a visible caption correcting the original Hg/Mercury label.

## Changed files

- `end-sem-unit-2.html` — figures in notes/answers and documented corrections
- `subject.json` — revision-card progress wording
- `assets/end-sem/unit-2/*.webp` — 18 original-source ROS assets
- `revision/unit-2-source-audit.json` — per-question figure decisions
- `revision/unit-2-source-review.md`, `revision/unit-2-ros-register.md`
- `revision/unit-2-corrections.json`, `revision/unit-2-ros-manifest.json`, `revision/unit-2-ros-contact.jpg`

## Question, paragraph and rendering audit

Essay 6 was incorrectly split into `b) ... (Galvani` and `c) corrosion ...`: the scratch importer treated the final `c)` in `Galvanic)` as a part marker. The previous flattened check removed whitespace and block boundaries, so the concatenated characters still matched. That check was insufficient.

The corrected page now uses source-reviewed question-part arrays for all 44 questions. Essay 6 has exactly `(a)` and `(b)`; Essays 7 and 8 retain four and two labelled parts. A permanent verifier checks each part independently, the corresponding answer labels and figure placement. It also checks all 36 Unit 1 question structures without changing that unit.

The full source-layout pass additionally repaired wrapped SHE/glass/calomel/pH sentences and headings, merged labels with their explanations, separated merged list entries and removed an orphan bullet. Electrode-handout narrative and source Q1 are outside their table. The detailed electrode comparison and stability comparison are joined across source PDF page breaks, including incomplete cell sentences. Repeated continuation headers are removed; every source cell's non-whitespace content is retained. Stable source anchors remain available. The Pilling–Bedworth carryover bullet is placed before the next topic.

The shared multipart grid now constrains a wide table to its own horizontal-scroll container. The following answer part's prose wraps at phone width. Long inline chemical equations retain their sentence context and punctuation in the existing bounded equation component. Browser checks inspect visible text and panel bounds inside each card, not only document-level overflow. Deliberately hidden assistive MathML is excluded from visual geometry checks.

Permanent checks:

```sh
python3 scripts/tools/verify_cfe_revision_structure.py
python3 scripts/tools/check_cfe_revision_browser.py --base-url http://127.0.0.1:8000
```

The browser command requires Playwright and Chromium, with the repository served at the given URL. It checks all 44 questions at 1440px and 390px, screenshots the questions/notes, tests table/equation scrolling, image decoding and full-size opening, and catches clipped visible text or panels. The structural verifier was also run against the original PR24 HTML and correctly rejected it.

[Detailed layout change record](unit-2-layout-review.json) · [Reviewed block/table contract](unit-2-structure-contract.json)

## Validation

PASS:
- `python3 scripts/tools/verify_college.py`
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`
- `python3 scripts/tools/build_vercel.py`; JSON parsing; `git diff --check`.
- Chromium 1440px/390px: all 39 image placements decode, all 44 original prompts and answers, figure mapping, correct multipart placement, full-size image opening, error captions, MathJax without errors and no page overflow. Screenshots inspected.
- GitHub Pages `/Pankusdesk/` base-path browser simulation: answer-part figures decode and equations render at phone width.
- Charge/atom balance, calomel logarithm coefficient and glass sign/offset algebra independently checked.
- Lossless RGB equality against every retained original/crop; stable-ID reconciliation; source/output SHA-256 hashes; ZIP integrity.

Unit 1, canonical topic data and previously approved image binaries are unchanged. Original source defects remain explicitly documented, not repaired or hidden in raster pixels.

Additional PASS checks for this structural audit:
- Exact part boundaries and content for all 44 Unit 2 and 36 Unit 1 questions; all corresponding answer parts and figure placements.
- Complete source paragraphs/headings, table row/column shapes and a glass-limitation sentence retained in one table cell.
- The original PR24 snapshot fails the new regression verifier; the corrected snapshot passes.
- Desktop/phone browser checks include visible text-range and panel geometry inside every answer, along with reachable horizontally scrollable tables/equations. Focused screenshots reviewed, including the reported Essay 6.
- Shared-CSS smoke checks: Chemistry Unit 1 and MAC multipart panels fit at phone width; BEE Unit 1 questions load (no multipart sample present).
- Image binaries, Unit 1 HTML and scientific corrections are unchanged in this audit. Formatting-only changes are recorded separately from chemical corrections.
