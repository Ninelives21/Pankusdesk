# PankusDesk feedback loop — 10 Sep 2026

## Scope

Base: `redo(20260910-023323)` plus handoff `pankusdesk-mac-u2-textbook-questions-class-linking-2026-09-10`.

This pass addresses three user-reported issues:

1. unusually many amber discrepancy markers on MAC Unit II textbook questions;
2. textbook-question typography still feeling too small;
3. no previous/next-unit navigation from the three pages of a unit.

## Amber discrepancy re-audit

The Unit II textbook bank originally carried 18 `math_mismatch` records. Each computational discrepancy was rechecked independently. Seventeen remain genuine meaning-bearing source/appendix conflicts. Problems 2.12 Q42 was demoted from amber to an ordinary wording/logic caveat because its problem is the wording “only if”, not a concrete numerical/matrix source disagreement.

Remaining amber items:

- Problems 2.8: Q6
- Problems 2.9: Q3, Q5, Q6, Q9, Q12, Q15, Q18
- Problems 2.10: Q3, Q4, Q5, Q7, Q8
- Problems 2.12: Q15, Q20, Q29, Q33

No amber item was removed merely to reduce the count.

## Textbook-question typography

Readability changes are global in `styles/new/pages/practice.css`, not MAC-specific:

- question text 17px → 18px desktop; 16px → 17px mobile;
- answer text 16px → 17px;
- question metadata 12px → 13px;
- group/source/quick-link supporting text increased by 1px;
- discrepancy explanation text 14px → 15px.

This applies to all subjects using the shared textbook-question renderer.

## Previous/next-unit navigation

`scripts/new/unit-resource-nav.js` now derives adjacent units from `subject.units` and renders Previous unit / Next unit links beneath the existing Text · Textbook Questions · Class Notes tabs.

Rules:

- the link always targets `unit-N.html`, the adjacent unit's Text/index page;
- it appears identically on Text, Textbook Questions and Class Notes pages because all three call the same shared renderer;
- no subject- or semester-specific navigation data is added;
- Unit I has only Next, the last unit has only Previous, middle units have both.

The global build standard, checklist and generic college verifier were updated so future subject builds preserve the shared navigation contract.
