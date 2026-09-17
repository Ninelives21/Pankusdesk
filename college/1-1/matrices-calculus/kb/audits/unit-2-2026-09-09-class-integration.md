# MAC Unit II — 9 September 2026 class-note integration

## Source

- `mac_9thSept.zip`
- SHA-256: `c905c714238de316ea1a4f1f2c443614af1ddf7b1af89c1fef219e56407fc4d0`
- Seven notebook photographs: `Mac-class-unit2 - 5.jpg` through `Mac-class-unit2 - 11.jpg`

The top of notebook page 5 is the tail end of the 8 September property example. The dated 9 September work begins at the circled Example 3, so the 9 September class contains Examples 3, 4 and 5.

## Final dropdown behaviour

The 17 September correction pass brings all three examples into the established PankusDesk class-question pattern:

1. the complete question is visible in the accordion summary;
2. clicking it opens a full step-by-step solution;
3. each example is checked against the prescribed Grewal Unit II worked examples and in-scope textbook questions before solving;
4. only an exact source match counts as a textbook match;
5. an exact match receives an aside at the start of the dropdown, but the class-note dropdown still contains the full worked solution;
6. textbook answers are checked against Appendix 3 when available;
7. notebook slips remain visible as mismatch notes instead of being silently overwritten.

## Textbook match checks

### Example 3

Class matrix:

\[
A=\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}.
\]

Exact match confirmed: **Grewal Problems 2.9 Q3(b), book p. 72**.

Appendix 3 p. 1381 prints roots `0, 3, 5` with eigenvectors `(1,2,2)`, `(2,1,-2)`, `(2,-2,1)`. The third printed root is inconsistent with both the matrix trace and the printed third eigenvector. Direct verification gives the third root as `15`.

Verified eigenpairs:

- `lambda=0`, eigenspace spanned by `[1,2,2]^T`
- `lambda=3`, eigenspace spanned by `[2,1,-2]^T`
- `lambda=15`, eigenspace spanned by `[2,-2,1]^T`

The notebook's final summary appears to omit the minus sign in the third component for `lambda=3`; the rendered class note preserves this as a notebook mismatch.

### Example 4

Class matrix:

\[
A=\begin{bmatrix}
6&-2&2\\
-2&3&-1\\
2&-1&3
\end{bmatrix}.
\]

Exact match confirmed: **Grewal Problems 2.9 Q3(e), book p. 72**.

Appendix 3 p. 1381 gives roots `8, 2, 2` with eigenvectors `(2,-1,1)`, `(1,0,-2)`, `(1,2,0)`. The full dropdown derives these step by step. Priyanka's `[-1,0,2]^T` is the same eigendirection as the printed `[1,0,-2]^T`.

The notebook briefly lists `8,6,2`; this is retained as a mismatch because `6` is not a root.

### Example 5

Class matrix:

\[
A=\begin{bmatrix}
-2&2&-3\\
2&1&-6\\
-1&2&0
\end{bmatrix}.
\]

No exact match was found in the supplied Grewal Unit II worked examples or in-scope textbook questions. Problems 2.9 Q3(d) differs in entry `(3,2)` and is **not counted as a match**.

The notebook stops during the determinant setup and writes the top-left entry as `-2`; the correct diagonal entry in `A-lambda I` is `-2-lambda`. The dropdown preserves that mismatch and then independently completes the actual class problem.

Verified characteristic equation:

\[
-(\lambda+3)(\lambda^2-2\lambda+9)=0.
\]

Verified eigenvalues/eigenvectors:

- `lambda=-3`, eigenspace spanned by `[3,0,1]^T`
- `lambda=1+2sqrt(2)i`, eigenspace spanned by `[lambda,2lambda,3]^T`
- `lambda=1-2sqrt(2)i`, eigenspace spanned by `[lambda,2lambda,3]^T`

All displayed eigenpairs were checked by direct multiplication.

## Files changed in the correction pass

- `college/1-1/matrices-calculus/kb/class-log/2026-09-09/entry.json`
- `college/1-1/matrices-calculus/kb/class-log/2026-09-09/raw.md`
- this audit file

The Unit II textbook theory, textbook-question bank, calendar, source manifest and other dated class entries are not changed by this correction.
