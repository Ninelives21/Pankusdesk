# Unit 1 — Exercise 1.5.14 integration

- Workspace baseline: user-supplied `re(1).zip` (latest WS for this task).
- Added approved NRS redraw of textbook Figure 1.41 as `assets/book/u1/examples/f1-41.png`.
- Added approved NRS redraw of textbook Figure 1.41(a) as `assets/book/u1/examples/f1-41a.png`.
- Updated the Unit 1 **Kirchhoff’s laws** topic so Exercise 1.5.14 now includes both figures at the correct logical points in the solution.
- Preserved the textbook solution sequence and equations.
- Added a **Textbook unit mismatch** note to flag that the printed `i_2 = 1.175 A` conflicts with the following power calculation, which uses `1.175 × 10^{-3} A`.
- Added a **SIMPLER** explainer covering:
  - why the original circuit can be redrawn as a parallel network between nodes `x` and `y`;
  - how current directions are assumed and why they could have been chosen the other way round;
  - how resistor polarity follows the assumed current direction;
  - why the sign relation effectively becomes `-1000 i_1 = 4000 i_2`;
  - how KCL is written at node `x`;
  - what the negative value of `i_1` means physically;
  - how the power values are obtained and why the textbook’s printed `i_2` line is inconsistent.
- Updated `kb/notes/unit-1.md` so the raw knowledge-base notes match the published section.

Verification:
- `python3 scripts/tools/verify_college.py` — PASS
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py` — PASS
- `node --check` on edited frontend scripts — not needed (no JS changed)
