# MAC Class Log — 15 September 2026

Source: four Unit II notebook photographs, `Mac-class-unit2 - 16.jpg` through `Mac-class-unit2 - 19.jpg`, supplied directly in chat. The first page is dated `15/9/26`.

## Linearly independent vectors

The class definition is cleaned to:

\[
\alpha_1X_1+\alpha_2X_2+\cdots+\alpha_nX_n=0
\]

implies

\[
\alpha_1=\alpha_2=\cdots=\alpha_n=0.
\]

Otherwise the vectors are linearly dependent.

### Example 1 — dependent vectors

\[
X_1=\begin{bmatrix}1\\2\\3\end{bmatrix},\qquad
X_2=\begin{bmatrix}2\\4\\6\end{bmatrix}.
\]

Since \(X_2=2X_1\),

\[
2X_1-X_2=0,
\]

with non-zero coefficients. Hence the vectors are linearly dependent.

### Example 2 — independent vectors

\[
X_3=\begin{bmatrix}2\\5\\6\end{bmatrix},\qquad
X_4=\begin{bmatrix}1\\5\\3\end{bmatrix}.
\]

Assume

\[
\alpha_1X_3+\alpha_2X_4=0.
\]

Then

\[
2\alpha_1+\alpha_2=0,\qquad
5\alpha_1+5\alpha_2=0,\qquad
6\alpha_1+3\alpha_2=0.
\]

From the first equation \(\alpha_2=-2\alpha_1\). Substitution in the second gives \(\alpha_1=0\), hence \(\alpha_2=0\). Therefore \(X_3,X_4\) are linearly independent.

## Algebraic multiplicity and geometric multiplicity

- **Algebraic multiplicity (AM):** the number of times an eigenvalue occurs as a root of the characteristic equation.
- **Geometric multiplicity (GM):** the number of linearly independent eigenvectors corresponding to that eigenvalue.

The class reuses

\[
A=\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix},
\]

with verified eigenvalues \(8,2,2\). Therefore

\[
AM(8)=1,\qquad AM(2)=2.
\]

The notebook lists

\[
X_1=\begin{bmatrix}2\\-1\\1\end{bmatrix}\quad(\lambda=8),
\]

and for \(\lambda=2\),

\[
X_2=\begin{bmatrix}-1\\0\\2\end{bmatrix},\qquad
X_3=\begin{bmatrix}1\\2\\0\end{bmatrix}.
\]

Thus

\[
GM(8)=1,\qquad GM(2)=2.
\]

This matrix is an exact match to Grewal Problems 2.9 Q3(e) and is also the matrix from the 9 September class-note Example 4. The canonical textbook solution is linked rather than duplicated.

## Similarity of matrices

A matrix \(A\) is similar to a matrix \(B\) if there exists a non-singular matrix \(P\) such that

\[
P^{-1}AP=B.
\]

## Diagonalization

If \(A\) is similar to a diagonal matrix \(D\), then \(A\) is diagonalizable and

\[
P^{-1}AP=D.
\]

Class notes record:

1. \(A\) is diagonalizable iff the algebraic multiplicity of each eigenvalue equals its geometric multiplicity.
2. If \(A\) has distinct eigenvalues, it is diagonalizable; the converse need not be true.
3. An \(n\times n\) matrix is diagonalizable iff it has \(n\) linearly independent eigenvectors.
4. The matrix formed from eigenvectors as columns, e.g. \(P=[X_1\ X_2\ X_3]\), is the **modal matrix**.
5. The diagonal matrix \(D\) is the **spectral matrix**, whose diagonal entries are the eigenvalues of \(A\).
6. \(P^{-1}AP=D\) is called a **similarity transformation**.

## Unfinished class question

\[
A=\begin{bmatrix}2&3&4\\0&2&-1\\0&0&1\end{bmatrix}.
\]

The notebook asks for the eigenvalues and eigenvectors, but the supplied page stops after writing \(\lambda=1,1,1\) and \(AM(\lambda=1)=3\).

This is a notebook mismatch. Because the matrix is upper triangular, its eigenvalues are its diagonal entries:

\[
2,2,1.
\]

Therefore

\[
AM(2)=2,\qquad AM(1)=1.
\]

No independent eigenvector solution is added because the photographed class work stops at this point.
