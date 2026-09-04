# MAC Class Log — 4 September 2026

Source: six notebook photographs, `mac_class_notes - 22.jpg` through `mac_class_notes - 27.jpg`.

## Notebook p. 22 — Gauss–Seidel idea

The class introduces the Gauss–Seidel iterative method for a three-variable system \(AX=B\), starting with initial guesses for the unknowns. It notes that convergence is rapid when the system is diagonally dominant and defines the diagonal-dominance check.

## Notebook p. 23 — procedure

1. Check diagonal dominance.
2. Rearrange each equation to isolate its diagonal unknown.
3. Start from \([x_1^{(0)},x_2^{(0)},x_3^{(0)}]=[0,0,0]\) and, during an iteration, use each newly computed value immediately in the next equation.

## Notebook pp. 24–26 — Example 1

Solve by Gauss–Seidel:

\[
5x_1-x_2=9,\qquad -x_1+5x_2-x_3=4,\qquad -x_2+5x_3=-6.
\]

The class iterates from \((0,0,0)\) and approaches \((2,1,-1)\). PankusDesk recomputed the complete iteration chain and presents it as one solved accordion.

## Notebook p. 27 — Q2 and Q3

Q2:

\[
5x_1-x_2+x_3=10,\qquad 2x_1+4x_2=12,\qquad x_1+x_2+5x_3=-1.
\]

Q3:

\[
8x_1+x_2-x_3=8,\qquad 2x_1+x_2+9x_3=12,\qquad x_1-7x_2+2x_3=-4.
\]

The supplied notebook page marks these for diagonal-dominance work but does not contain solutions. PankusDesk therefore supplies complete Gauss–Seidel solutions. Q3 is first reordered as equations 1, 3, 2 so that the diagonal entries are \(8,-7,9\).

## Verification notes

- Example 1 converges to \((2,1,-1)\).
- Q2 converges to approximately \((2.5556,1.7222,-1.0556)\), with exact solution \((23/9,31/18,-19/18)\).
- Q3 converges to \((1,1,1)\).
- A few handwritten iteration superscripts/signs on p.26 are inconsistent with the recurrence; the verified recurrence values are used in the study copy.
