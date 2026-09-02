# Unit I three-page refactor audit — 2 September 2026

## New student-facing contract

Unit I now has three separate study destinations:

1. `unit-1.html` — textbook-led Text/theory.
2. `unit-1-questions.html` — prescribed textbook questions.
3. `unit-1-class-notes.html` — Priyanka's chronological class notes with date-based left navigation.

The shared `unit-resource-nav.js` renderer exposes these destinations consistently.

## Theory purge

All Unit-I `kind: "class-note"` sections, `CLASS-U1-*` topic-level source references, class-history rows, and `Class-note ...` formula-summary entries were removed from `kb/data/topics.json`.

The remaining Unit-I visible topic/section source references resolve only to the prescribed textbook and official syllabus. The human-readable `kb/notes/unit-1.md` companion was regenerated from the cleaned theory data so it no longer carries embedded class-note panels.

## Chronological class notes

The dedicated Unit-I Class Notes page renders dated entries from the `class_sources` collection in `kb/data/source-manifest.json`.

Working dates after this refactor:

- 24 Aug 2026 — circuit concept & basic quantities.
- 27 Aug 2026 — ideal/practical voltage and current sources.
- 31 Aug 2026 — dependent sources; R, L and C.
- 1 Sep 2026 — expanded network-element classifications; R/L/C energy additions; nodes, branches and closed loops.

The 1 September source pack contains older pages with later annotations. The 1 September dated entry records only the genuinely new additions rather than duplicating the full 31 August lesson.

## 1 September redraws

`assets/class/2026-09-01/figures/`

- `c1.png` — updated network-element classification tree.
- `c2.png` — standalone resistor symbol.
- `c3.png` — standalone inductor symbol.
- `c4.png` — nodes, branches and loops circuit.

The standalone resistor/inductor symbols are used with the R/L class-note material; the updated classification and network circuit belong to the 1 September dated entry.

## Calendar

BEE calendar entries now link directly to date anchors on `unit-1-class-notes.html`. A BEE entry was added for 1 September alongside the existing Matrices & Calculus entry.

## Verification expectations

- Unit-I theory contains no embedded class-note sections.
- Unit-I class-note shell exists and all dated entries resolve.
- Calendar date anchors resolve to real dated class entries.
- All referenced class redraw assets exist.
- Subject and generic college verifiers pass.
