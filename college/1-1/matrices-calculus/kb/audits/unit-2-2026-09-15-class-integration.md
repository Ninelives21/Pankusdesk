# MAC Unit II — 15 September 2026 class-note integration (corrected full-solution pass)

## Source workspace

Latest user-supplied `re.zip` from the correction task. This workspace already contained the earlier 15 September integration; that entry was inspected and replaced rather than applying the change to an older delta.

## Source material

Four notebook photographs supplied directly in chat:

- `Mac-class-unit2 - 16.jpg` — linearly independent/dependent vectors
- `Mac-class-unit2 - 17.jpg` — algebraic/geometric multiplicity example
- `Mac-class-unit2 - 18.jpg` — similarity and diagonalization theory
- `Mac-class-unit2 - 19.jpg` — triangular-matrix eigenvalue/eigenvector question

The source hashes remain those already stored in `source-manifest.json`.

## What was corrected in this pass

The earlier 15 September integration was too summary-like. It did not satisfy the established class-example pattern.

This pass changes that behaviour so that:

1. every class example/question appears as a clickable accordion/dropdown;
2. opening the question reveals a complete worked solution;
3. intermediate equations, substitutions and row-reduction logic are shown rather than jumping to final answers;
4. every class example was checked against both the prescribed Unit II worked examples and the in-scope textbook question bank before solving;
5. when an exact textbook match exists, a textbook-match aside appears at the beginning of the dropdown;
6. the class-note answer is checked against the printed textbook answer where one exists.

## Textbook match check

### Linear-independence vector examples

No exact match was found in the current Grewal Unit II worked examples or the in-scope textbook question sets. Both examples are therefore solved directly from the class data.

### Algebraic/geometric multiplicity matrix

Class matrix:

\[
A=\begin{bmatrix}
6&-2&2\\
-2&3&-1\\
2&-1&3
\end{bmatrix}.
\]

Exact source match:

- Grewal Problems 2.9 Q3(e), book p. 72.
- Printed Appendix 3 answer, p. 1381: roots `8, 2, 2` with eigenvectors `(2,-1,1)`, `(1,0,-2)`, `(1,2,0)`.

The new dropdown derives the characteristic equation and all eigenvector relations step by step. Priyanka's `[-1,0,2]^T` vector is explicitly recognized as the same eigendirection as the printed `[1,0,-2]^T` vector.

Verified result:

\[
AM(8)=GM(8)=1,\qquad AM(2)=GM(2)=2.
\]

### Triangular-matrix class question

\[
A=\begin{bmatrix}
2&3&4\\
0&2&-1\\
0&0&1
\end{bmatrix}.
\]

No exact match was found in the current Unit II worked examples or in-scope textbook question bank.

The notebook writes `lambda = 1,1,1` and `AM(lambda=1)=3`; this is incorrect for the written matrix. The dropdown preserves that as a notebook discrepancy, then independently completes the problem at the user's explicit request.

Verified result:

- eigenvalues: `2,2,1`;
- for `lambda=2`: eigenspace `span{[1,0,0]^T}`, so `GM(2)=1`;
- for `lambda=1`: eigenspace `span{[-7,1,1]^T}`, so `GM(1)=1`;
- therefore the matrix is not diagonalizable because `AM(2)=2` but `GM(2)=1`.

## UI behaviour

The existing generic class-log/study accordion renderer is reused. No MAC-specific UI mechanism was introduced.

The 15 September page now uses `accordions` blocks for all examples/questions so the visible question is clickable and the worked solution is revealed in the dropdown.

## Calendar

The existing 15 September MAC calendar entry is retained and its summary is updated to reflect the completed worked examples.

## Files modified

- `college/1-1/matrices-calculus/kb/class-log/2026-09-15/entry.json`
- `college/1-1/matrices-calculus/kb/class-log/2026-09-15/raw.md`
- `college/1-1/matrices-calculus/kb/data/source-manifest.json`
- `college/1-1/matrices-calculus/kb/audits/unit-2-2026-09-15-class-integration.md`
- `college/1-1/data/class-log.json`

## Verification performed

- JSON parse validation: PASS for the modified entry, source manifest and semester class-log files.
- MAC KB verifier: PASS.
- College verifier: PASS.
- Direct mathematical checks: PASS. The AM/GM example characteristic polynomial is `-(lambda-8)(lambda-2)^2`; all three displayed eigenvectors satisfy `Av=lambda v`. The triangular example characteristic polynomial is `-(lambda-2)^2(lambda-1)`; `[1,0,0]^T` and `[-7,1,1]^T` satisfy the corresponding eigenvector equations.
- Linear-independence checks: the first pair has rank 1 and the second pair has rank 2.
- Malformed control-character/backslash scan: PASS; no control characters or malformed `\frac` tokens were found in the revised entry.
- Source check against Grewal: Problems 2.9 Q3(e) confirmed on book p. 72; Appendix 3 p. 1381 confirmed the printed roots/eigenvectors used for the answer check.
- Local browser visual QA was attempted, but the sandbox blocked loopback HTTP navigation (`ERR_BLOCKED_BY_ADMINISTRATOR`), so no browser-render claim is made for this pass. The generic accordion renderer itself was not changed.
- Delta ZIP: created with one top-level folder and test-unzipped successfully.
