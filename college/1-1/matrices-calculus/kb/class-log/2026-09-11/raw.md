# MAC Class Log — 11 September 2026

Source: four Unit II notebook photographs, `Mac-class-unit2 - 12.jpg` through `Mac-class-unit2 - 15.jpg`, supplied directly in chat.

Both class questions were compared against the prescribed Grewal Unit II worked examples and the in-scope Problems 2.8, 2.9, 2.10 and 2.12 sets. No exact textbook match was found, so these remain separate class-note solutions.

## Example 6 — characteristic roots and corresponding eigenvectors

\[
A=\begin{bmatrix}
5&-2&0\\
-2&6&2\\
0&2&7
\end{bmatrix}.
\]

The class starts with

\[
|A-\lambda I|=0.
\]

Thus

\[
\begin{vmatrix}
5-\lambda&-2&0\\
-2&6-\lambda&2\\
0&2&7-\lambda
\end{vmatrix}=0.
\]

Expanding along the first row,

\[
(5-\lambda)\big[(6-\lambda)(7-\lambda)-4\big]
+2\big[-2(7-\lambda)\big]=0,
\]

so

\[
(5-\lambda)(\lambda^2-13\lambda+38)-28+4\lambda=0.
\]

Hence

\[
-\lambda^3+18\lambda^2-99\lambda+162=0
=-(\lambda-3)(\lambda-6)(\lambda-9).
\]

Therefore

\[
\lambda=3,\ 6,\ 9.
\]

### For \(\lambda=3\)

\[
\begin{bmatrix}
2&-2&0\\
-2&3&2\\
0&2&4
\end{bmatrix}X=0.
\]

Using the notebook row operations \(R_2\to R_2+R_1\) and \(R_3\to R_3-2R_2\),

\[
\begin{bmatrix}
2&-2&0\\
0&1&2\\
0&0&0
\end{bmatrix}X=0.
\]

Hence

\[
2x_1-2x_2=0,\qquad x_2+2x_3=0.
\]

Taking \(x_3=k\) gives \(x_1=x_2=-2k\). Therefore one eigenvector is

\[
X_1=k\begin{bmatrix}-2\\-2\\1\end{bmatrix}.
\]

### For \(\lambda=6\)

\[
\begin{bmatrix}
-1&-2&0\\
-2&0&2\\
0&2&1
\end{bmatrix}X=0.
\]

The notebook reduction gives

\[
\begin{bmatrix}
-1&-2&0\\
0&2&1\\
0&0&0
\end{bmatrix}X=0.
\]

Thus

\[
-x_1-2x_2=0,\qquad 2x_2+x_3=0.
\]

Taking \(x_2=-k\) gives

\[
X_2=k\begin{bmatrix}2\\-1\\2\end{bmatrix}.
\]

### For \(\lambda=9\)

\[
\begin{bmatrix}
-4&-2&0\\
-2&-3&2\\
0&2&-2
\end{bmatrix}X=0.
\]

Following the notebook reduction,

\[
\begin{bmatrix}
-4&-2&0\\
0&-2&2\\
0&0&0
\end{bmatrix}X=0.
\]

Therefore

\[
-2x_1-x_2=0,\qquad -x_2+x_3=0.
\]

Taking \(x_2=2k\) gives

\[
X_3=k\begin{bmatrix}-1\\2\\2\end{bmatrix}.
\]

The three eigenpairs have been independently checked by direct multiplication.

## Next class question — eigenvalues and eigenvectors

\[
A=\begin{bmatrix}
-3&-7&-5\\
2&4&3\\
1&2&2
\end{bmatrix}.
\]

The characteristic equation is

\[
\begin{vmatrix}
-3-\lambda&-7&-5\\
2&4-\lambda&3\\
1&2&2-\lambda
\end{vmatrix}=0.
\]

Cleaning the crossed-out arithmetic while retaining the notebook expansion,

\[
(-3-\lambda)\big[(4-\lambda)(2-\lambda)-6\big]
+7\big[2(2-\lambda)-3\big]
-5\big[4-(4-\lambda)\big]=0.
\]

Hence

\[
-\lambda^3+3\lambda^2-3\lambda+1=0
=-(\lambda-1)^3.
\]

Therefore

\[
\lambda=1,1,1.
\]

For \(\lambda=1\),

\[
\begin{bmatrix}
-4&-7&-5\\
2&3&3\\
1&2&1
\end{bmatrix}X=0.
\]

The notebook uses

\[
R_2\to2R_2+R_1,\qquad R_3\to4R_3+R_1,
\]

giving

\[
\begin{bmatrix}
-4&-7&-5\\
0&-1&1\\
0&1&-1
\end{bmatrix}X=0.
\]

Then \(R_3\to R_3+R_2\):

\[
\begin{bmatrix}
-4&-7&-5\\
0&-1&1\\
0&0&0
\end{bmatrix}X=0.
\]

Thus

\[
-x_2+x_3=0\quad\Rightarrow\quad x_3=x_2.
\]

Substituting into the first equation,

\[
-4x_1-7x_2-5x_3=0
\quad\Rightarrow\quad
-4x_1-12x_2=0.
\]

Taking \(x_2=k\),

\[
x_1=-3k,\qquad x_3=k,
\]

so a corresponding eigenvector is

\[
X=k\begin{bmatrix}-3\\1\\1\end{bmatrix}.
\]

The notes list the root three times, \(1,1,1\), and obtain a corresponding eigenvector \([-3,1,1]^T\).
