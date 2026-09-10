# BEE Class Log — 9 September 2026

## Page 1 — Network theorems and superposition theorem

Network theorems are useful to find the voltage or current of one specific branch. This simplifies mesh/nodal analysis when only one response is required.

### Superposition theorem

In a linear network containing two or more sources, the response in any element is equal to the algebraic sum of the responses caused by the individual sources acting alone.

- Voltage source: replace with a short circuit when made non-operative.
- Current source: replace with an open circuit when made non-operative.
- Ideal current source internal resistance: \(\infty\).
- Ideal voltage source internal resistance: \(0\).

The page contains the original two-source example and a second sketch headed “When 15 V is acting alone”.

\[
15-V=\frac{V}{3.3}+\frac{V}{2.2}
\]

## Page 2 — Superposition example continued and Thevenin’s theorem

### When 20 V is acting alone

\[
\frac{20-V}{2.2}=V+\frac{V}{3.3}
\]

\[
V=5.17\text{ V},\qquad I'=1.56\text{ mA}
\]

### Thevenin’s theorem

Any two-terminal linear bilateral network can be replaced by an equivalent circuit consisting of an equivalent source \(V_{th}\) (or \(V_{oc}\)) in series with resistance \(R_{th}\).

The page then sketches an example network and the open-circuit-voltage arrangement for \(V_{th}\) or \(V_{oc}\).

## Page 3 — Thevenin resistance, equivalent circuit and worked network

The page sketches the circuit used to obtain \(R_{th}\), followed by the Thevenin equivalent circuit with the load reconnected.

A further two-source circuit is written with node voltage \(V\):

\[
\frac{18-V}{1}+\frac{22-V}{2.2}=\frac{V}{3.3}
\]

## Page 4 — Corrected copy and source-reduction sketch

The corrected copy of the two-source circuit repeats:

\[
\frac{18-V}{1}+\frac{22-V}{2.2}=\frac{V}{3.3}
\]

The written results are:

\[
V=10.24\text{ V},\qquad I=3.10\text{ mA}
\]

The lower part of the page contains another source-reduction/checking sketch. The calculations underneath are crossed through and are not transcribed as final working.
