# Unit I three-page refactor audit — 2 September 2026

## New student-facing contract

Unit I has three separate study destinations:

1. `unit-1.html` — textbook-led Text/theory.
2. `unit-1-questions.html` — prescribed textbook questions.
3. `unit-1-class-notes.html` — Priyanka's class notes with date-based left navigation.

The shared `unit-resource-nav.js` renderer exposes these destinations consistently.

## Theory purge

All Unit-I `kind: "class-note"` sections, `CLASS-U1-*` topic-level source references, class-history rows, and class-note-only formula-summary entries were removed from `kb/data/topics.json`. The Unit-I Text page is therefore no longer a mixed textbook/class-note page.

## Class-note de-duplication rule

The class-notes page is date-navigated, but continuation material is assimilated into the date on which that lesson was first introduced instead of being repeated as a second near-duplicate lesson. Provenance is retained in each dated entry's `source_notes`.

Final Unit-I class-note organization:

- **24 Aug 2026** — circuit concept, basic quantities, and one consolidated network-element classification section. The updated NRS tree replaces the older incomplete tree. Explanation dropdowns consolidate the later definitions for active/passive, voltage/current sources, independent/dependent sources, linear/non-linear, bilateral/unilateral, time-invariant/time-variant, and lumped/distributed elements.
- **27 Aug 2026** — detailed ideal/practical voltage and current source models and characteristics.
- **31 Aug 2026** — dependent sources and R/L/C. Later power/energy annotations written onto those same notebook pages are assimilated into this entry.
- **1 Sep 2026** — only the genuinely new nodes, branches and closed-loops lesson.

## Redraw use

`assets/class/2026-09-01/figures/`

- `c1.png` — updated network-element classification tree; displayed under 24 Aug as the consolidated replacement diagram.
- `c2.png` — standalone resistor symbol; displayed with the 31 Aug resistance notes.
- `c3.png` — standalone inductor symbol; displayed with the 31 Aug inductance notes.
- `c4.png` — nodes, branches and loops circuit; displayed under 1 Sep.

Existing 31 Aug dependent-source and capacitor NRS assets remain in their original asset folder.

## Calendar

BEE calendar links continue to target date anchors on `unit-1-class-notes.html`. The 1 Sep calendar description now names only nodes, branches and closed loops; consolidated continuation material remains discoverable under 24 Aug and 31 Aug.

## Verification expectations

- Unit-I Text contains no embedded class-note sections.
- The 24 Aug class-note entry references the updated classification tree exactly once.
- The 1 Sep entry references only the nodes/branches/loops redraw.
- 31 Aug includes the later R/L/C energy annotations.
- Calendar date anchors resolve to real dated entries.
- All referenced class redraw assets exist.
- Subject and generic college verifiers pass.
