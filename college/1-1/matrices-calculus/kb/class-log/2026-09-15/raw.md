# MAC Class Log — 15 September 2026

Source: four Unit II notebook photographs, `Mac-class-unit2 - 16.jpg` through `Mac-class-unit2 - 19.jpg`, supplied directly in chat. The first page is dated `15/9/26`.

This cleaned record preserves Priyanka's matrices, definitions and class order. All examples are presented as question/solution dropdowns in the rendered page. Where the notebook contains a slip or stops before completing a question, that is explicitly identified; the independently completed working is not presented as if it appeared in the notebook.

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

Assume

\[
\alpha_1X_1+\alpha_2X_2=0.
\]

Then

\[
\alpha_1+2\alpha_2=0,\qquad
2\alpha_1+4\alpha_2=0,\qquad
3\alpha_1+6\alpha_2=0.
\]

The equations are all the same relation. For example, choosing
\(\alpha_1=2,\alpha_2=-1\) gives

\[
2X_1-X_2=0.
\]

The coefficients are not both zero, so the vectors are linearly dependent. This agrees with the notebook observation \(X_2=2X_1\).

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

From the first equation,

\[
\alpha_2=-2\alpha_1.
\]

Substitute in the second:

\[
5\alpha_1+5(-2\alpha_1)=0
\Rightarrow -5\alpha_1=0
\Rightarrow \alpha_1=0.
\]

Hence \(\alpha_2=0\). Therefore the vectors are linearly independent.

Neither vector-pair example has an exact match in the current prescribed Unit II worked examples or in-scope textbook question sets.

## Algebraic multiplicity and geometric multiplicity

- **Algebraic multiplicity (AM):** the number of times an eigenvalue occurs as a root of the characteristic equation.
- **Geometric multiplicity (GM):** the number of linearly independent eigenvectors corresponding to that eigenvalue.

The class uses

\[
A=\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix}.
\]

This is an **exact match to Grewal Problems 2.9 Q3(e), book p. 72**. Appendix 3 p. 1381 prints the roots/eigenvectors as

\[
8,2,2;
\qquad
(2,-1,1),\ (1,0,-2),\ (1,2,0).
\]

The full class-note solution is worked stepwise in the rendered dropdown. Its characteristic equation reduces to

\[
-(\lambda-8)(\lambda-2)^2=0,
\]

so

\[
AM(8)=1,\qquad AM(2)=2.
\]

For \(\lambda=8\), row reduction gives

\[
X=k\begin{bmatrix}2\\-1\\1\end{bmatrix},
\]

hence \(GM(8)=1\).

For \(\lambda=2\), the eigenspace is two-dimensional and may be represented by

\[
X_2=\begin{bmatrix}1\\2\\0\end{bmatrix},\qquad
X_3=\begin{bmatrix}1\\0\\-2\end{bmatrix}.
\]

Thus \(GM(2)=2\). Priyanka writes one of these as \([-1,0,2]^T\), which is the same eigendirection as the textbook's \([1,0,-2]^T\).

Therefore

\[
AM(8)=GM(8)=1,\qquad AM(2)=GM(2)=2.
\]

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

## Class question — completed after the notebook stopping point

\[
A=\begin{bmatrix}2&3&4\\0&2&-1\\0&0&1\end{bmatrix}.
\]

The notebook writes \(\lambda=1,1,1\) and \(AM(1)=3\), but this is inconsistent with the matrix actually written.

Because \(A\) is upper triangular,

\[
|A-\lambda I|
=(2-\lambda)^2(1-\lambda)=0.
\]

Therefore the verified eigenvalues are

\[
2,2,1,
\]

and

\[
AM(2)=2,\qquad AM(1)=1.
\]

For \(\lambda=2\),

\[
(A-2I)X=0
\]

gives \(z=0\), then \(y=0\), with \(x\) free. Hence

\[
X=k\begin{bmatrix}1\\0\\0\end{bmatrix},
\qquad GM(2)=1.
\]

For \(\lambda=1\),

\[
(A-I)X=0
\]

gives \(y=z\) and \(x=-7z\). Hence

\[
X=k\begin{bmatrix}-7\\1\\1\end{bmatrix},
\qquad GM(1)=1.
\]

Thus the matrix has only two independent eigenvector directions in total and is **not diagonalizable**.

No exact match for this matrix was found in the current Grewal Unit II worked examples or in-scope textbook question sets. The eigenvector calculation above is an independent PankusDesk completion made because the user explicitly requested every class example to be worked through fully.
