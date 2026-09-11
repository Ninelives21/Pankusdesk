# Unit 1 — Exercise 1.5.13 integration

- Workspace baseline: user-supplied `re(1).zip` (latest WS for this task).
- Moved Exercise 1.5.13 into the Unit 1 **Worked examples** accordion sequence immediately after Exercise 1.5.12.
- Added approved NRS redraw of textbook Figure 1.40 as `assets/book/u1/examples/f1-40.png`.
- Preserved the textbook solution sequence and equations from pp. 29–30.
- Added a nested **SIMPLER** explainer inside the Exercise 1.5.13 solution after the two loop-current calculations. The explainer covers:
  - why the diagonal C–D 12 V branch carries no current despite maintaining a 12 V potential difference;
  - how resistor polarity follows the assumed current direction (passive sign convention);
  - why B→D is a rise and C→A is a drop;
  - the B→D→C→A potential walk giving `V_AB = 13 V`;
  - concise sign rules for resistors and voltage sources.
- Removed the former standalone Exercise 1.5.13 section to avoid duplicate rendering.
- Expanded the Worked examples source coverage through TB-P030 / pp. 18–30.

Verification:
- `python3 scripts/tools/verify_college.py` — PASS
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py` — PASS
- all JavaScript `node --check` — PASS
- custom Exercise 1.5.13 placement/asset/nested-explainer checks — PASS
