# Unit I Q & A — source/answer review

The fourth navigation group adds all **24 short-answer questions and 12 essays** from `Unit-1 Water and its Treatment QB - Modified.doc.pdf`. Full prompts remain visible before opening the shared answer dropdowns. The printed [BL] labels and multipart wording remain present. Essay 7 has separate (a)/(b) panels; Essay 10 has separate chlorine/bleaching-powder/chloramine panels using shared practice styles.

Answers are labelled **PankusDesk answer**. They are authored from the already incorporated course notes and existing textbook-led `kb/data/topics.json`; they are not claimed to be printed textbook solutions. Existing notes, four hardness numericals, their IDs and original image bytes are preserved. Six figure placements reuse approved ROS assets; no new drawings or substituted diagrams are made.

## Attached textbook is not yet checked

`chem_unit1.zip` exceeds the download tool's **32 MiB** transfer limit. It could not be opened; this PR does not claim to have inspected it. An accessible split of that archive is needed for a new raw-book cross-check.

- **Short Q17:** the available notes call CaSO₄ a hard scale and describe silica/silicates as particularly hard/adherent, but do not identify one unique “hardest”. The answer states the source-supported examples/removal and explicitly marks textbook confirmation pending. It does not invent an exam-key answer.
- **Short Q11:** pH/turbidity/colour values are identified as course-handout values. The existing source table is **IS 10500**, not verified WHO guidance. It is not relabelled.
- Answers avoid silently importing errors from the source transcript; the unchanged transcript remains intact. Only questions, not the newly authored answers, are verbatim source text.

## Numerical verification

All five numerical questions have reproducible working and bold results:

| Question | Temporary ppm | Permanent ppm | Total ppm |
| --- | --- | --- | --- |
| Short 8 | 200 given | 300 given | 500 |
| Short 9 | Not requested | Not requested | 150 |
| Essay 2 | 125 | 75 | 200 |
| Essay 3 | 150 | 200 | 350 |
| Essay 7(b) | 20 | 101 | 121 |

For Essay 3, 10,000 L changes equivalent mass, not ppm: temporary mass = **1.5 kg** and total mass = **3.5 kg** as CaCO₃. For Essay 7(b), the tiny CaSO₄ entry is **1.36 mg/L**, yielding **1 mg/L** equivalent, not 100. Turbidity is excluded. Short 9 uses the supplied ionic atomic masses, not Ca/Mg salt molecular masses. All Clarke conversions use the source's rounded **0.07 °Cl per ppm** consistently.

Source mapping, every original prompt and numerical check are recorded in [the Q & A audit](unit-1-qa-audit.json). `kb:` references in that audit name existing textbook-led topic IDs; the other reference strings are anchors on the end-sem page. No newly verified textbook page numbers are manufactured.
