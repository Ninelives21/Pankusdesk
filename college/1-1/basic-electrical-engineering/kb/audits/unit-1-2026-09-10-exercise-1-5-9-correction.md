# Unit I — Exercise 1.5.9 printed-figure correction

Exercise 1.5.9 was reworked from the latest workspace supplied as `re.zip`.

## What was preserved

- The original textbook Figure 1.36 remains in the worked example and is not replaced.
- The printed equivalent Figure 1.36(a), KCL steps and final answer remain in place.

## What was added

- A clearly labelled corrected reconstruction, `f1-36-corrected.png`, is shown after the original question figure and before the solution.
- The reconstruction restores the 10 Ω A–B resistor branch required by the question, Figure 1.36(a) and the printed KCL equation.
- The reconstruction also keeps A and B as distinct nodes instead of allowing the B conductor to meet the right-hand A conductor.
- An amber note explains that this is an inferred correction and why it is necessary.
- A reusable explainer dropdown is shown immediately below Figure 1.36(a). It explains the A/B node identification, why all five branches are parallel, why both current-source arrows become B→A in the equivalent drawing, that resistors have no inherent current direction, and how those assumed directions lead to the KCL signs.

## Renderer support

`scripts/new/study-ui.js` now supports optional `notes` and `explainers` inside worked-example accordion items. They may be unanchored or placed at `before-paragraph`, `paragraph` or `end` hooks, matching the existing figure-placement pattern.
