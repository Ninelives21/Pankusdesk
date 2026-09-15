# BEE Class Log — 9 September 2026

## Page 1 — Network theorems and superposition theorem

Network theorems are useful to find the voltage or current of one specific branch. This simplifies mesh/nodal analysis when only one response is required.

### Superposition theorem

In a linear network containing two or more sources, the response in any element is equal to the algebraic sum of the responses caused by the individual sources acting alone.

- Voltage source: replace with a short circuit when made non-operative.
- Current source: replace with an open circuit when made non-operative.
- Ideal current source internal resistance: \(\infty\).
- Ideal voltage source internal resistance: \(0\).

The first redraw shows the original two-source circuit. The second redraw shows the case when only the 15 V source acts.

Note: In the notebook sequence, the right-hand source in the original sketch is unlabeled, but the next sketch clearly says “When 20 V is acting alone”. To keep the three Superposition sketches consistent with each other and with the theorem, the redraw treats the original second source as 20 V. In the source-isolation sketches, only one source remains active at a time and the other voltage source is suppressed by a short circuit.

\[
15-V=\dfrac{V}{3.3}+\dfrac{V}{2.2}
\]

## Page 2 — Superposition example continued and Thevenin’s theorem

### When 20 V is acting alone

\[
\dfrac{20-V}{2.2}=V+\dfrac{V}{3.3}
\]

\[
V=5.17\text{ V},\qquad I'=1.56\text{ mA}
\]

### Superposition example — explanation

- Superposition theorem is used when a linear circuit has more than one independent source.
- Original circuit: keep both sources active.
- 15 V acting alone: keep the 15 V source and suppress the 20 V source by a short circuit.
- 20 V acting alone: keep the 20 V source and suppress the 15 V source by a short circuit.
- Final response: add the separate contributions algebraically with the correct sign.

The corrected redraws are meant to make the class-note working internally consistent. The equations match the source-isolation sketches:

- For 15 V acting alone: \((15-V)/1 = V/3.3 + V/2.2\), written in the notebook as \(15-V=V/3.3+V/2.2\).
- For 20 V acting alone: \((20-V)/2.2 = V/1 + V/3.3\), written in the notebook as \((20-V)/2.2 = V + V/3.3\).

### Thevenin’s theorem

Any two-terminal linear bilateral network can be replaced by an equivalent circuit consisting of an equivalent source \(V_{th}\) (or \(V_{oc}\)) in series with resistance \(R_{th}\).

- \(V_{th}\) or \(V_{oc}\): open-circuit voltage measured between the load terminals.
- \(R_{th}\): Thevenin resistance seen from the load terminals with the independent sources replaced by their internal resistances.

The class example is shown first as the original loaded network, followed by the open-circuit arrangement used for \(V_{th}\) or \(V_{oc}\).

## Page 3 — Thevenin resistance, equivalent circuit and worked network

The next sketch suppresses the source and shows the network used to obtain \(R_{th}\). The following sketch is the Thevenin equivalent circuit with the 3.3 kΩ load reconnected and the load current \(I_L\) marked downward.

A later worked network uses the same resistor pattern as the earlier Superposition example — \(1\,\text{k}\Omega\), \(2.2\,\text{k}\Omega\) and \(3.3\,\text{k}\Omega\) — but changes the source values to \(18\,\text{V}\) and \(22\,\text{V}\).

**Source-model clarification (PankusDesk):** the source symbol alone does not prove that either source is ideal, and the absence of a drawn internal resistance is not proof by itself. The ideal-source treatment comes from the class-note superposition method stated earlier: an ideal voltage source has zero internal resistance and a voltage source made non-operative is replaced by a short circuit. Therefore this worked example is interpreted using the same ideal-source model for both independent sources. If a practical source had a stated non-zero internal resistance, that resistance would remain when the source voltage was set to zero.

With both sources active, the complete-circuit node equation is

\[
\dfrac{18-V}{1}+\dfrac{22-V}{2.2}=\dfrac{V}{3.3}.
\]

This complete-circuit equation is retained as an independent check. The source-by-source calculations on the following notebook page use superposition.

## Page 4 — Teacher-corrected source-by-source working

Priyanka’s working is in black ink. The teacher’s review/correction is in red ink. Red ticks, circles, arrows and crosses are therefore feedback marks, not additional circuit symbols or values.

### 18 V source acting alone

Keep the \(18\,\text{V}\) source active. In the ideal-source model used by the class notes, set the \(22\,\text{V}\) source to zero volts, so it becomes a short circuit; the \(2.2\,\text{k}\Omega\) resistor remains connected from node \(V\) to the common return. At node \(V\), \((18-V)/1\) enters from the left, while \(V/3.3\) and \(V/2.2\) leave:

\[
\dfrac{18-V}{1}=\dfrac{V}{3.3}+\dfrac{V}{2.2}.
\]

The notebook result

\[
V=10.24\text{ V},\qquad I=3.10\text{ mA}
\]

is marked with a red teacher tick and is consistent with the circuit.

### 22 V source acting alone

Keep the \(22\,\text{V}\) source active. Set the \(18\,\text{V}\) source to zero volts, so it becomes a short circuit; the \(1\,\text{k}\Omega\) resistor then connects node \(V\) to the common return. At node \(V\), \((22-V)/2.2\) enters from the right, while \(V/1\) and \(V/3.3\) leave:

\[
\dfrac{22-V}{2.2}=\dfrac{V}{1}+\dfrac{V}{3.3}.
\]

Priyanka’s lower black-ink result near the red cross is approximately

\[
V=9.55\text{ V},\qquad I=2.89\text{ mA},
\]

but these values are not consistent with the shown circuit.

Verified correction:

\[
V\approx5.69\text{ V},\qquad I_{22}\approx1.72\text{ mA}.
\]

### Superposition total and direct check

Both source-isolation cases drive the current through the \(3.3\,\text{k}\Omega\) branch downward relative to the same reference direction, so the two contributions have the same sign and are added. If one contribution had been upward, it would enter the algebraic sum with the opposite sign.

\[
V_{\text{total}}\approx10.24+5.69=15.93\text{ V}
\]

\[
I_{\text{total}}\approx3.10+1.72=4.82\text{ mA}.
\]

Solving the complete circuit directly gives

\[
V\approx15.93\text{ V},\qquad I\approx4.83\text{ mA},
\]

with the small current difference due only to rounding the individual source contributions before adding them.

Some other red circles/arrows on the notebook are clearly teacher emphasis or correction marks, but their exact intended wording is not legible enough to transcribe safely; they are therefore not assigned invented meanings.
