# MAC Class Log — 8 September 2026

Source: four Unit II notebook photographs, `Mac-class-unit2 - 1.jpg` through `Mac-class-unit2 - 4.jpg`, supplied in `mac-classnotes-unit2.zip`.

## Eigenvalues and eigenvectors

The class starts Unit II with the definition

\[
AX=\lambda X,
\]

where \(\lambda\) is an eigenvalue and the non-zero vector \(X\) is a corresponding eigenvector. The class example uses

\[
A=\begin{bmatrix}5&4\\1&2\end{bmatrix},\qquad
X=\begin{bmatrix}4\\1\end{bmatrix},
\]

and obtains

\[
AX=\begin{bmatrix}24\\6\end{bmatrix}=6X,
\]

so \(\lambda=6\).

The notes then rewrite the eigenvector equation as

\[
(A-\lambda I)X=0
\]

and use the non-trivial-solution condition

\[
|A-\lambda I|=0,
\]

calling this the characteristic equation. Its roots are the eigenvalues / characteristic roots / latent roots.

## Properties listed in class

1. If \(\lambda\) is an eigenvalue of non-singular \(A\), then \(1/\lambda\) is an eigenvalue of \(A^{-1}\), with a short proof from \(AX=\lambda X\).
2. \(A\) and \(A^T\) have the same eigenvalues.
3. For non-zero \(\lambda\), \(|A|/\lambda\) is an eigenvalue of \(\operatorname{adj}A\).
4. If \(\lambda\) is an eigenvalue of \(A\), then \(\lambda^m\) is an eigenvalue of \(A^m\).
5. If \(\lambda\) is an eigenvalue of \(A\), then \(a\lambda^2+b\lambda+c\) is an eigenvalue of \(aA^2+bA+cI\).
6. One eigenvector cannot correspond to more than one eigenvalue of the same matrix.
7. The sum of eigenvalues equals the trace; their product equals the determinant.
8. The eigenvalues of a triangular or diagonal matrix are its diagonal entries.
9. Similar matrices \(A\) and \(P^{-1}AP\) have the same eigenvalues.

## Class example 1

For

\[
A=\begin{bmatrix}1&2&3\\0&2&-7\\0&0&3\end{bmatrix},
\]

the eigenvalues are \(1,2,3\) because \(A\) is triangular. Therefore the eigenvalues of \(A^{-1}\) are \(1,1/2,1/3\), and those of \(A^2\) are \(1,4,9\).

## Class example 2

The photographed exercise gives two eigenvalues, 3 and 6, and asks for the eigenvalues of \(A^T\) and \(A^{-1}\). Using the trace \(=11\), the third eigenvalue is 2. Hence \(A^T\) has eigenvalues \(2,3,6\) and \(A^{-1}\) has eigenvalues \(1/2,1/3,1/6\).

### Verification note

The photographed matrix appears to omit the minus sign at entry (3,2). With +1, the stated eigenvalues 3 and 6 are not eigenvalues of the matrix. Restoring (3,2) to -1 gives eigenvalues 2, 3 and 6 and makes the class working internally consistent. The dated study entry uses this corrected intended sign.
