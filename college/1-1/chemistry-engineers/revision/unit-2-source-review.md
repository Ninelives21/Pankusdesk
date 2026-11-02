# Unit 2 end-sem notes — source review

Status: **draft**. This is a separate semester-end source layer; textbook-led topics, syllabus metadata, dated class notes and their publication states are unchanged. No new textbook-page verification is claimed.

## Source discrepancies and qualifications

### Nernst notation and explanation
Source `e`, PDF viewer page 5.
The source uses both reaction quotient Q and equilibrium constant K in a non-standard-potential equation. It also says (RT/nF) ln(Q) decreases while E decreases; with E° fixed, subtracting a decreasing term would instead increase E. The transcript is retained; these source statements require review. R25 requires the equation and significance, with no derivation.

### SHE potential convention
Source `e`, PDF viewer page 7.
The source calls the potential developed during oxidation positive and then “comparatively very small”. The reference potential assigned to SHE is exactly zero by convention under its specified reference conditions; this is not a measurement of a small residual voltage. Source wording is retained.

### SHE source claims conflict
Source `e`, PDF viewer page 8.
This page claims SHE is not affected by liquid-junction potential, while its own limitations describe impurity poisoning. The comparison sheet additionally says it is not affected by impurities. Do not treat either immunity claim as established; the supplied statements are retained separately.

### Calomel reaction and Nernst discrepancy
Source `e`, PDF viewer page 10.
The printed reduction reaction gives 2 Hg⁺ as product. This fails charge balance: the left side has charge −2 and the right side 0. The comparison sheet prints Hg₂Cl₂(s) + 2e⁻ ⇌ 2Hg(l) + 2Cl⁻. The raster Nernst expression on this page has RT/F multiplying ln[Cl⁻]²; the comparison sheet has the 1/2 coefficient appropriate to the two-electron reaction. Both printed versions are preserved.

### Calomel potential values conflict
Source `e`, PDF viewer page 11.
Page 10 gives +0.2422 V for saturated KCl, but the worked substitution continued here uses +0.2442 V. These are different printed values; neither has silently replaced the other. The accompanying electrolyte concentration and temperature must be specified when selecting a value.

### Glass-electrode expressions conflict
Source `e`, PDF viewer page 16.
This page sets E° to zero and obtains E = +0.0592 pH. The comparison handout instead prints E = constant − 0.0592 pH at 25°C. Measurement polarity and the reference-system offset matter; a combined glass electrode does not inherit SHE’s zero-potential convention. These source expressions remain distinct pending textbook verification.

### Printed oxidation mechanism
Source `c`, PDF viewer page 3.
The raster mechanism ends with the general product “MO” while using variable valency n. That shorthand is not a balanced general oxide formula for arbitrary n. The expression has been transcribed as printed, not presented as a verified general stoichiometric equation.

### Pilling–Bedworth example — textbook check pending
Source `c`, PDF viewer page 4.
The handout says that a larger specific volume ratio always gives less oxidation corrosion, and selects W (3.6) over Cr (2.0) and Ni (1.6). It does not discuss cracking or spalling of high-volume oxide films. A unique independently verified exam answer to Short Q17 is pending; the source’s W answer is retained and explicitly attributed.

### General anodic equation
Source `c`, PDF viewer page 8.
The supplied general expression is M → M⁺ + ne⁻. Its charges balance only for n = 1. The later iron example, Fe → Fe²⁺ + 2e⁻, is balanced. The general source expression is retained without silently changing its superscript.

### Sacrificial-anode limitations — source check pending
Source `c`, PDF viewer page 17.
The handout lists “High starting current is required” and “Uncoated parts cannot be protected” under sacrificial-anode limitations. These claims need textbook checking; they should not be generalized as verified limitations. The source list remains intact.

## Question bank numbering

The PDF has 34 short questions and 9 numbered essays. Between Essay 7 and Essay 8 it prints a separate `a)` prompt about dry corrosion without an essay number. It is retained as an **unnumbered source prompt**, with its position recorded, rather than relabelled Essay 10 or silently merged with Essay 7.

## Integration and verification

Native PDF wording/subscripts/superscripts are reflowed. Raster-only text panels were transcribed after viewing the source; equations are MathJax and comparison panels are semantic tables. Source errors are preserved with shared amber discrepancy notes. Ordinary editorial and pending-figure notes use the existing blue source-note style. All answer content is labelled PankusDesk-authored, separate from the source transcript.

ROS assets remain pending under the repository figure-production freeze. The text draft is reviewable without adding raw scans or broken image links. See [the proposed figure register](unit-2-ros-register.md) and [the provenance audit](unit-2-source-audit.json).

The Chemistry index has five revision cards. Unit 1 retains its existing URL and anchors; Units 3–5 have pending cards without fake working links. No PR, remote push, merge or publication is part of this local draft.


## R25 scope mapping

The provenance audit maps 13 detailed requirements from the uploaded R25 p.12 to supplied PDF pages. All named headings have supplied material; this does not declare academic verification or figure completion. Nernst derivation is excluded as required by R25. Both methods of cathodic protection are included.

## Local validation

- PASS: `python3 scripts/tools/verify_college.py`
- PASS: `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`
- PASS: `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`
- PASS: `python3 scripts/tools/build_vercel.py`
- PASS: `node --check scripts/new/subject-home.js`, modified JSON parsing, `git diff --check`.
- Chromium at 1440px and 390px: five end-sem cards; original textbook unit grid retained; all 44 source prompts and answer dropdowns; five navigation groups; keyboard controls; separate answer subparts; equations; no page-wide overflow. Screenshots inspected. BEE's existing resource cards still render.
- All eight native source tables checked for non-whitespace character preservation; column headers checked visually. Raster-panel transcription remains subject to final independent fidelity review.
- PASS: GitHub Pages `/Pankusdesk/` base-path browser simulation at 390px for cards, Unit 2 links, hash navigation, equations and horizontal table scrolling.
- Unit 1 source page is exactly unchanged after removing its one new “All end-sem units” navigation link. No image assets changed.

## Files changed

- `college/1-1/chemistry-engineers/index.html`
- `college/1-1/chemistry-engineers/subject.json`
- `college/1-1/chemistry-engineers/end-sem-notes.html` — all-units return link only
- `college/1-1/chemistry-engineers/end-sem-unit-2.html`
- `college/1-1/chemistry-engineers/revision/unit-2-source-audit.json`
- `college/1-1/chemistry-engineers/revision/unit-2-source-review.md`
- `college/1-1/chemistry-engineers/revision/unit-2-ros-register.md`
- `scripts/new/subject-home.js` — generic optional unit-resource groups
- `styles/new/pages/subject.css` — responsive unit-resource grid
- `styles/new/pages/source-notes.css` — optional wide source-table cells

## Local review steps

Serve the repository root with `python3 -m http.server 8006 --bind 127.0.0.1`, then open `http://127.0.0.1:8006/college/1-1/chemistry-engineers/index.html#end-sem-units`.

- [ ] On desktop and phone, inspect the five End-Sem Notes cards. Expect Units 1–2 to open separate revision pages and Units 3–5 to be marked not integrated, without dead links.
- [ ] Open Unit 2; expand the five sidebar groups. Expect clear boundaries and only one group expanded at a time. Open Essay 7 and expect four separate answer parts, with the full question visible before opening.
- [ ] Inspect Short Q17 and the calomel/glass source notes. Expect explicit source qualifications rather than silent corrections. On a phone, swipe the comparison table to reach the Glass electrode column.

No hosted preview has been created. Figure placeholders are intentional; see the ROS register for the 18 proposed assets.
