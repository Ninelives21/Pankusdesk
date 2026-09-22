# Chemistry Unit II — Electrode Potential SIMPLER integration

## Source workspace
Latest user-supplied `redo.zip` in the 2026-09-22 task, extracted and inspected before editing.

## Change
Added a PankusDesk `SIMPLER` explainer to the opening **Development of electrode potential** section of Unit II. It follows the formal opening material and textbook Fig. 1 placement, before the next formal subsection.

The explainer clarifies:
- the zinc electrode material is oxidised, specifically surface Zn atoms;
- `Zn(s) → Zn²⁺(aq) + 2e⁻`;
- Zn²⁺ enters the solution while the electrons remain on the metal;
- why this leaves the zinc electrode negative relative to the nearby solution;
- why forward/reverse processes approach dynamic equilibrium;
- how charge separation produces electrode potential;
- the contrast with Cu²⁺ electronation/reduction shown in the textbook figure.

This is a PankusDesk teaching aid and is not represented as prescribed-textbook prose. Existing formal textbook-derived material was not rewritten.

## Files modified / added
- `college/1-1/chemistry-engineers/kb/data/topics.json`
- `college/1-1/chemistry-engineers/kb/audits/unit-2-2026-09-22-electrode-potential-simpler.md`

## Verification
- `topics.json` parses successfully as JSON.
- Confirmed the explainer is attached only to `u2-electrode-potential` → `Development of electrode potential`.
- Checked LaTeX strings after JSON parsing for the intended backslashes and formulas.
- Scanned the modified JSON for unexpected ASCII control characters.
- Ran the repository college verifier; result recorded in handoff.
