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

A further two-source circuit is written with node voltage \(V\):

\[
\dfrac{18-V}{1}+\dfrac{22-V}{2.2}=\dfrac{V}{3.3}
\]

## Page 4 — Corrected copy and source-reduction sketch

The corrected copy of the two-source circuit repeats:

\[
\dfrac{18-V}{1}+\dfrac{22-V}{2.2}=\dfrac{V}{3.3}
\]

The written results are:

\[
V=10.24\text{ V},\qquad I=3.10\text{ mA}
\]

The lower part of the page contains another source-reduction/checking sketch. The calculations underneath are crossed through and are not transcribed as final working.
