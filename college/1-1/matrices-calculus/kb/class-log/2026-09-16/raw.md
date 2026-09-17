# MAC Class Log — 16 September 2026

Source: six Unit II notebook photographs, `Mac-class-unit2 - 20.jpg` through `Mac-class-unit2 - 25.jpg`, supplied directly in chat.

This cleaned record preserves Priyanka's matrices, class order and intended method. Every class problem is a question/solution dropdown in the rendered page. The working is completed step by step. Notebook slips are identified rather than silently copied.

## Question 1 — not diagonalizable

\[
A=\begin{bmatrix}0&1\\0&0\end{bmatrix}.
\]

The characteristic equation is \(\lambda^2=0\), so \(\lambda=0\) has algebraic multiplicity 2. Solving \(AX=0\) gives \(x_2=0\) and \(x_1\) free, so the eigenspace is spanned by \([1,0]^T\). Hence \(GM(0)=1\ne AM(0)=2\), so the matrix is not diagonalizable.

No exact match was found in the current Unit II Grewal worked examples or in-scope question sets.

## Question 2 — diagonalize

\[
A=\begin{bmatrix}5&-4&4\\12&-11&12\\4&-4&5\end{bmatrix}.
\]

The characteristic equation factors as

\[
-(\lambda+3)(\lambda-1)^2=0,
\]

so the eigenvalues are \(1,1,-3\).

For \(\lambda=1\), two independent eigenvectors are

\[
X_1=\begin{bmatrix}1\\1\\0\end{bmatrix},\qquad
X_2=\begin{bmatrix}-1\\0\\1\end{bmatrix}.
\]

For \(\lambda=-3\), one eigenvector is

\[
X_3=\begin{bmatrix}1\\3\\1\end{bmatrix}.
\]

Thus

\[
P=\begin{bmatrix}1&-1&1\\1&0&3\\0&1&1\end{bmatrix},\qquad
P^{-1}=\begin{bmatrix}3&-2&3\\1&-1&2\\-1&1&-1\end{bmatrix},
\]

and

\[
P^{-1}AP=\operatorname{diag}(1,1,-3).
\]

No exact textbook match was found in the current Unit II worked examples or in-scope question sets.

## Question 3 — diagonalize and hence find \(A^4\)

\[
A=\begin{bmatrix}1&0&0\\0&3&-1\\0&-1&3\end{bmatrix}.
\]

The eigenvalues are \(1,2,4\), with convenient eigenvectors

\[
X_1=\begin{bmatrix}1\\0\\0\end{bmatrix},\quad
X_2=\begin{bmatrix}0\\1\\1\end{bmatrix},\quad
X_3=\begin{bmatrix}0\\-1\\1\end{bmatrix}.
\]

Therefore

\[
P=\begin{bmatrix}1&0&0\\0&1&-1\\0&1&1\end{bmatrix},\qquad
D=\operatorname{diag}(1,2,4),
\]

and

\[
P^{-1}=\begin{bmatrix}1&0&0\\0&\frac12&\frac12\\0&-\frac12&\frac12\end{bmatrix}.
\]

Using \(A^4=PD^4P^{-1}\),

\[
A^4=\begin{bmatrix}1&0&0\\0&136&-120\\0&-120&136\end{bmatrix}.
\]

The identical matrix appears in Grewal Problems 2.10 Q9(a), but that textbook part asks only for the eigenvalues, eigenvectors and modal matrix. Because the class question additionally asks for diagonalization and \(A^4\), this is a partial overlap, not an exact problem match. The class problem is therefore solved independently in full.
