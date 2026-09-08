# BEE Class Log — 7 September 2026

## Source policy

The four supplied notebook photographs are the authoritative source for this dated class record. Wording and notebook order are preserved as far as safely readable, with grammar lightly cleaned on the student-facing page. Seven circuit sketches are represented by the approved notebook-style redraws.

Where a handwritten intermediate sign conflicts with the equation immediately before and after it, the source discrepancy is stated explicitly. The final A–B network problem is incomplete in the supplied page, so no missing steps or final resistance are invented.

## Page 1 — Three-mesh KVL problem

Question: find the current and power supplied by the source.

Loop 1:

\[10-6I_1-(I_1-I_2)=0\]

\[-7I_1+I_2=-10\qquad (1)\]

Loop 2:

\[-2I_2-3(I_2-I_3)-(I_2-I_1)=0\]

\[I_1-6I_2+3I_3=0\qquad (2)\]

Loop 3:

\[-10I_3-20-3(I_3-I_2)=0\]

\[3I_2-13I_3=20\qquad (3)\]

Notebook results:

- \(I_1=1.34\,A\)
- \(I_2=-0.62\,A\)
- \(I_3=-1.68\,A\)

The handwritten power line ends at \(VI_1=10\times1.34\), which evaluates to 13.4 W.

One intermediate expansion line appears to use the wrong sign for the \(3I_2\) term. The original loop equation and numbered equation (3) agree with each other and are retained.

## Page 2 — KCL nodal-analysis problem

Question: find currents in each resistor by applying KCL.

Node 1:

\[5=\dfrac{V_1}{10}+\dfrac{V_1-V_2}{3}\]

\[13V_1-10V_2=150\]

Node 2:

\[\dfrac{V_2-V_1}{3}+\dfrac{V_2}{5}+\dfrac{V_2-10}{1}=0\]

\[-5V_1+23V_2=150\]

Notebook values:

- \(V_1=19.88\,V\)
- \(V_2=10.84\,V\)
- \(I_{10\Omega}\approx1.98\,A\)
- \(I_{3\Omega}\approx3.01\,A\)
- \(I_{5\Omega}\approx2.16\,A\)
- \(I_{1\Omega}\approx0.84\,A\)

## Page 3 — Network reduction technique

Class list:

1. Series connection
2. Parallel connection
3. Series-parallel connection

### Series connection

\[V_s=IR_1+IR_2\]

\[R_{eq}=R_1+R_2\]

### Parallel connection

\[I=I_1+I_2\]

\[\dfrac1{R_{eq}}=\dfrac1{R_1}+\dfrac1{R_2}\]

\[R_{eq}=\dfrac{R_1R_2}{R_1+R_2}\]

Current-divider wording: current in one parallel branch is total current multiplied by the other branch resistance, divided by the sum of the two branch resistances.

- Inductors in series: \(L_{eq}=L_1+L_2\)
- Inductors in parallel: \(L_{eq}=\dfrac{L_1L_2}{L_1+L_2}\)
- Capacitors in series: \(C_{eq}=\dfrac{C_1C_2}{C_1+C_2}\)

## Page 4 — Series-parallel examples

Capacitors in parallel:

\[C_{eq}=C_1+C_2\]

### X–Y network

Three 6-ohm branches reduce to 2 ohms; the two 2-ohm branches reduce to 1 ohm. The upper path therefore becomes 5 ohms, in parallel with the lower 5-ohm branch:

\[R_{XY}=2.5\,\Omega\]

### A–B network

The class page draws the original A–B circuit and then a first simplified/redrawn form. The supplied page does not include a completed final equivalent-resistance answer, so this dated record stops at the visible reduction step.
