# MAC Class Log — 9 September 2026

Source: seven Unit II notebook photographs, `Mac-class-unit2 - 5.jpg` through `Mac-class-unit2 - 11.jpg`, supplied in `mac_9thSept.zip`.

The top of page 5 still contains the end of the 8 September trace/transpose/inverse example. The new 9 September work begins below the written date with the next eigenvalue/eigenvector problem, so the repeated 8 September material is not duplicated here.

## Example 3 — eigenvalues and corresponding eigenvectors

\[
A=\begin{bmatrix}
8&-6&2\\
-6&7&-4\\
2&-4&3
\end{bmatrix}.
\]

The characteristic equation is

\[
|A-\lambda I|=0
\]

and simplifies to

\[
-\lambda^3+18\lambda^2-45\lambda=0
=-\lambda(\lambda-3)(\lambda-15).
\]

Hence

\[
\lambda=0,\ 3,\ 15.
\]

For \(\lambda=0\), the class row reduction gives

\[
\begin{bmatrix}
8&-6&2\\
0&10&-10\\
0&0&0
\end{bmatrix}X=0,
\]

so a corresponding eigenvector is

\[
X_1=\begin{bmatrix}1\\2\\2\end{bmatrix}.
\]

For \(\lambda=3\), the reduced system is

\[
\begin{bmatrix}
5&-6&2\\
0&-16&-8\\
0&0&0
\end{bmatrix}X=0,
\]

which gives an eigenvector proportional to

\[
X_2=\begin{bmatrix}2\\1\\-2\end{bmatrix}.
\]

For \(\lambda=15\), the reduced system is

\[
\begin{bmatrix}
-7&-6&2\\
0&-20&-40\\
0&0&0
\end{bmatrix}X=0,
\]

which gives

\[
X_3=\begin{bmatrix}2\\-2\\1\end{bmatrix}.
\]

### Independent verification

All three vectors satisfy \(AX=\lambda X\) for the stated eigenvalue.

## Example 4 — repeated eigenvalue

\[
A=\begin{bmatrix}
6&-2&2\\
-2&3&-1\\
2&-1&3
\end{bmatrix}.
\]

The characteristic polynomial written in class is

\[
-\lambda^3+12\lambda^2-36\lambda+32=0.
\]

It factors as

\[
-(\lambda-8)(\lambda-2)^2=0.
\]

Therefore the verified eigenvalues are

\[
8,\ 2,\ 2.
\]

For \(\lambda=8\), a corresponding eigenvector is

\[
\begin{bmatrix}2\\-1\\1\end{bmatrix}.
\]

For the repeated eigenvalue \(\lambda=2\), the eigenspace is two-dimensional. The notebook writes the general vector as a combination equivalent to

\[
X=\frac{k_1}{2}\begin{bmatrix}-1\\0\\2\end{bmatrix}
+\frac{k_2}{2}\begin{bmatrix}1\\2\\0\end{bmatrix}.
\]

Thus two independent eigenvectors for \(\lambda=2\) are

\[
\begin{bmatrix}-1\\0\\2\end{bmatrix},
\qquad
\begin{bmatrix}1\\2\\0\end{bmatrix}.
\]

### Verification note

The notebook briefly lists the roots as \(8,6,2\) and starts a \(\lambda=6\) line. That is a mathematical slip: \(6\) is not a root of the characteristic polynomial. The correct roots are \(8,2,2\).

## Example 5 — new problem begins

The last photograph begins

\[
A=\begin{bmatrix}
-2&2&-3\\
2&1&-6\\
-1&2&0
\end{bmatrix},
\qquad |A-\lambda I|=0.
\]

The photographed work stops while setting up the determinant.

### Verification note

The handwritten determinant writes the top-left diagonal term as \(-2\). The correct characteristic determinant must subtract \(\lambda\) from every diagonal entry:

\[
|A-\lambda I|=
\begin{vmatrix}
-2-\lambda&2&-3\\
2&1-\lambda&-6\\
-1&2&-\lambda
\end{vmatrix}=0.
\]

No further solution is added because the supplied 9 September notes do not continue the example.
