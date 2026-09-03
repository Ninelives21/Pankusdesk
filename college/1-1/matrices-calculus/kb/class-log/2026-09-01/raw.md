# MAC Class Log — 1 September 2026

## Source policy

This is the dated notebook record. Wording and class-work order are preserved as far as safely readable; mathematical typography and line wrapping are normalized. Two visible slips are retained and documented rather than silently corrected: on notebook p.14 the common rank 2 is compared with 4 even though there are three unknowns, and on p.16 the written row operation \(R_2-2R_1\) is followed by an incorrect \(-3\) entry where \(-2\) is required. The supplied p.18 ends during the final example, so the dated record does not invent the missing classroom continuation. The original photographs remain in `mac_1stSept(1).zip`.

## Notebook page 13

### Gauss-elimination method (Row-rank method)

**Procedure:** It is used to test if the given system is consistent or not and solve if it is consistent.

In this method, the unknowns are eliminated successively and the system is reduced to echelon form with row transformations, from which unknowns are calculated by back-substitution method.

### 1. Using Gauss-elimination method, solve

\[
x+2y+z=8,\qquad 2x+3y+4z=20,\qquad 4x+3y+2z=16.
\]

The notebook writes the system as \(AX=B\), forms the augmented matrix and reduces it to

\[
\left[\begin{array}{ccc|c}
1&2&1&8\\
0&-1&2&4\\
0&0&-12&-36
\end{array}\right].
\]

## Notebook page 14

The notebook records \(\rho(A)=\rho(A|B)=3=n\), then back-substitutes to obtain

\[
z=3,\qquad y=2,\qquad x=1.
\]

### 2. Test for consistency and solve if it is consistent

\[
x+y+z=6,\qquad x+2y+3z=14,\qquad x+4y+7z=30.
\]

Row reduction gives

\[
\left[\begin{array}{ccc|c}
1&1&1&6\\
0&1&2&8\\
0&0&0&0
\end{array}\right].
\]

The notebook writes \(\rho(A)=\rho(A|B)=2<4\) and concludes that the system is consistent and has infinitely many solutions.

## Notebook page 15

For Example 2, let \(z=k\). Then

\[
y=8-2k,\qquad x=k-2,
\]

so

\[
X=\begin{bmatrix}k-2\\8-2k\\k\end{bmatrix}.
\]

### 3. Test for consistency and solve

\[
x+y+z=4,\qquad 2x+5y-2z=3,\qquad x+7y-7z=5.
\]

The augmented matrix reduces to a row \([0\ 0\ 0\mid11]\), so the notebook concludes that the system is inconsistent.

## Notebook page 16

### 4. Solve

\[
x_1+2x_2+x_3=0,\qquad
2x_1+2x_2+3x_3=0,\qquad
3x_1+2x_2+x_3=0.
\]

The notebook notes \(\rho(A)=n\Rightarrow\) unique/trivial solution and \(\rho(A)<n\Rightarrow\) many solutions. It starts with

\[
A=\begin{bmatrix}1&2&1\\2&2&3\\3&2&1\end{bmatrix}
\]

and records a third pivot, concluding \(\rho(A)=n\) and

\[
X=\begin{bmatrix}0\\0\\0\end{bmatrix}.
\]

### 5. Find values of \(\lambda\) and \(\mu\)

For

\[
2x+3y+5z=9,\qquad
7x+3y-2z=8,\qquad
2x+3y+\lambda z=\mu,
\]

find conditions for (i) unique solution, (ii) many solutions, and (iii) no solution.

## Notebook page 17

The class row reduction reaches

\[
\left[\begin{array}{ccc|c}
2&3&5&9\\
0&-15&-39&-47\\
0&0&\lambda-5&\mu-9
\end{array}\right].
\]

The notebook concludes:

- unique solution: \(\lambda\ne5\), \(\mu\in\mathbb R\);
- many solutions: \(\lambda=5\), \(\mu=9\);
- no solution: \(\lambda=5\), \(\mu\ne9\).

## Notebook page 18

### 6. Find the values of \(\lambda\) for which the system has a non-trivial solution and solve in each case

\[
3x_1+x_2-\lambda x_3=0,
\]
\[
4x_1-2x_2-3x_3=0,
\]
\[
2\lambda x_1+4x_2+\lambda x_3=0.
\]

The notebook forms

\[
A=\begin{bmatrix}
3&1&-\lambda\\
4&-2&-3\\
2\lambda&4&\lambda
\end{bmatrix}
\]

and begins row reduction. The supplied photograph ends during this working; no final values of \(\lambda\) or solution ratios are written on the supplied page.
