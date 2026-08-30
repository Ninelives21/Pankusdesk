# MAC multi-part question/solution layout fix

This delta implements the global PankusDesk rule that labelled subparts are never run together inline.

Changes:
- `scripts/new/unit-questions.js`: structured rendering of question subparts and solution subparts.
- `styles/new/pages/practice.css`: stacked question parts and clearly separated alternating solution panels.
- `college/1-1/matrices-calculus/kb/data/textbook-questions.json`: Problems 2.4 Q2, Q6, Q7 and Q9 structured into explicit subparts.
- `college/schemas/textbook-questions.schema.json`: schema support for structured question/answer parts.
- `college/COLLEGE_BUILD_STANDARD.md` and `college/UNIT_BUILD_CHECKLIST.md`: global rule recorded for all subjects/practice layers.

Apply from the parent folder containing both this delta and `Pankusdesk/`.
