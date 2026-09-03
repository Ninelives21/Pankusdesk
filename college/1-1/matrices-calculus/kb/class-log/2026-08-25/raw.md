# MAC Class Log — 25 August 2026

## Source policy

This is the dated notebook record. Wording is preserved as written as far as it is safely readable; line wrapping is normalized. Several matrix entries in the worked reductions are overwritten in the notebook. The record keeps the safely readable sequence and explicitly notes where a later step is clearer than an overwritten intermediate value. The original notebook photographs remain in the supplied `mac_25thAug(1).zip` source archive and are not copied into website assets.

## Notebook page 1

Rank gives no. of independent rows.

### Normal form (canonical form)

- Consists of an identity matrix.
- Row and column operations can be used.
- Only row transformations can be used in echelon.

Matrices of the form \([I_r\ 0]\), \(\begin{bmatrix}I_r\\0\end{bmatrix}\), and \(\begin{bmatrix}I_r&0\\0&0\end{bmatrix}\) are said to be in normal form where \(I_r\) is an identity.

**NOTE:** To reduce a given matrix into normal form, use both row and column transformations. After reducing into normal form, \(\rho(A)\) is given by order of identity matrix in it.

## Notebook pages 2–3

### Example 1 — Find rank of matrix using Normal form

\[
A=\begin{bmatrix}
2&3&-1&1\\
1&-1&-2&-4\\
3&1&3&-2\\
6&3&0&-7
\end{bmatrix}
\]

The notebook applies row and column transformations, ending in the unit matrix \(I_4\).

\[\rho(A)=4.\]

## Notebook pages 4–5

### Example 2

\[
A=\begin{bmatrix}
0&1&-3&-1\\
1&0&1&1\\
3&1&0&2\\
1&1&-2&0
\end{bmatrix}
\]

The notebook reduces the matrix to

\[
\begin{bmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&0&0\\
0&0&0&0
\end{bmatrix}.
\]

Hence the identity block is \(I_2\), so the rank is 2.
