# MAC Class Log — 29 August 2026

## Source policy

This is the dated notebook record. Wording is preserved as written as far as it is safely readable; line wrapping is normalized. The original notebook photographs remain in `mac_29thAug(1).zip` and are not copied into website assets.

## Notebook page 11

### System of linear equations

System is consistent (at least one solution) if

\[
\rho(A)=\rho(A|B).
\]

- \(\rho(A|B)=n\) → unique solution (when ranks are equal / consistent).
- \(\rho(A|B)<n\) → infinitely many solutions (when ranks are equal / consistent).
- \(\rho(A)\ne\rho(A|B)\) → no solution.

A set of linear equations in 2 or more unknowns is called system of linear equations.

For m linear equations in n unknowns,

\[
\begin{aligned}
a_{11}u_1+a_{12}u_2+\cdots+a_{1n}u_n&=b_1\\
a_{21}u_1+a_{22}u_2+\cdots+a_{2n}u_n&=b_2\\
&\vdots\\
a_{m1}u_1+a_{m2}u_2+\cdots+a_{mn}u_n&=b_m
\end{aligned}
\]

The system can be written in matrix form as \(AX=B\), where A is the coefficient matrix, X is the column of unknowns and B is the column of constants.

## Notebook page 12

A system is said to be consistent if it has at least 1 solution.

For \(AX=B\), the system is consistent iff

\[
\rho(A)=\rho(A|B).
\]

Case (i): \(\rho(A)=\rho(A|B)=n\) (number of unknowns) → unique solution.

Case (ii): \(\rho(A)=\rho(A|B)<n\) → infinite solutions, among which \((n-r)\) are independent parameters when the common rank is r.

If \(\rho(A)\ne\rho(A|B)\) → the system has no solution and is inconsistent.

### NOTE

- System \(AX=B\) is said to be non-homogeneous if \(B\ne0\).
- A non-homogeneous system may or may not be consistent.
- A system of form \(AX=0\) is called homogeneous, where 0 is null vector.
- A homogeneous system is always consistent as it possesses a trivial solution.
- A homogeneous system \(AX=0\) has a non-trivial solution iff \(\rho(A)<n\); for a square coefficient matrix, equivalently \(|A|=0\).
