# BEE Class Log — 3 September 2026

## Source policy

The three supplied notebook photographs are the authoritative source for this dated class record. Wording is preserved as far as it is safely readable, with grammar and awkward English lightly cleaned on the student-facing Class Notes page. Circuit sketches are redrawn in the shared notebook-redraw style.

Where handwritten arithmetic conflicts with the setup equations on the same page, the website keeps the setup and explicitly labels a separate arithmetic check rather than silently changing the source.

## Page 1 — Kirchhoff’s Voltage Law

Kirchhoff’s Voltage Law states that the algebraic sum of all voltages around a closed loop is zero.

Equivalent class wording: in a closed loop, sum of voltage sources = sum of voltage drops across resistors.

\[\sum V=0\]

### Example 1 — apply KVL and find voltage across each element

\[10-I(10^6)-I(3.1\times10^6)-I(400\times10^3)-I(500\times10^3)=0\]

\[I=2\,\mu A\]

- 1 MΩ → 2 V
- 3.1 MΩ → 6.2 V
- 400 kΩ → 0.8 V
- 500 kΩ → 1 V

### Problem 2 — find mesh currents I1 and I2

Loop 1:

\[5-2I_1-2(I_1-I_2)=0\]

\[-4I_1+2I_2=-5\]

Loop 2:

\[-4I_2-6I_2+10-2(I_2-I_1)=0\]

\[2I_1-12I_2=-10\]

The handwritten final numerical labels are inconsistent with these boxed equations; this is called out on the web page.

## Page 2 — Kirchhoff’s Current Law

Kirchhoff’s Current Law states that the algebraic sum of currents meeting at a node or junction is zero.

Sum of currents entering a node = sum of currents leaving a node.

\[\sum I=0\]

## Page 3 — KCL examples

### Find current through 3.3 kΩ

\[\frac{15-V}{1}+\frac{20-V}{2.2}=\frac{V}{3.3}\]

Notebook result: V ≈ 13.75 V and current through 3.3 kΩ ≈ 4.1 mA.

### Practice 2

\[\frac{15-V}{1}=\frac{V}{3.3}+\frac{V}{2.2}\]

The notebook page ends after the node-voltage working.
