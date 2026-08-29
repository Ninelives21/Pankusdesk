# Unit I — Matrices

> Canonical student-facing content is source-backed from the supplied B. S. Grewal scans and filtered to the R25 Unit-I scope. Main textbook prose is retained closely; worked examples are rendered as dropdowns on the web page.

## Rank of a matrix by Echelon form

### 2.7 (1) Rank of a Matrix

If we select any r rows and r columns from any matrix A, deleting all the other rows and columns, then the determinant formed by these r × r elements is called the minor of A of order r. Clearly, there will be a number of different minors of the same order, got by deleting different rows and columns from the same matrix.

Def. A matrix is said to be of rank r when

- (i) it has at least one non-zero minor of order r, and
- (ii) every minor of order higher than r vanishes.
- Briefly, the rank of a matrix is the largest order of any non-vanishing minor of the matrix.
- The rank of a matrix A shall be denoted by \(\rho(A)\).

### Observations

- Obs. 1. Rank of A and its transpose is the same i.e. \(\rho(A)=\rho(A\prime)\).
- Obs. 2. Rank of a null matrix is zero.
- Obs. 3. Rank of a non-singular square matrix of order r is r.
- Obs. 4. If a matrix has a non-zero minor of order r, its rank is \(\ge r\). If all minors of a matrix of order \(r+1\) are zero, its rank is \(\le r\).

### 2.7 (2) Elementary transformation of a matrix

The following operations, three of which refer to rows and three to columns are known as elementary transformations:

- I. The interchange of any two rows (columns).
- II. The multiplication of any row (column) by a non-zero number.
- III. The addition of a constant multiple of the elements of any row (column) to the corresponding elements of any other row (column).
- Notation. The elementary row transformations will be denoted by the following symbols: (i) \(R_{ij}\) for the interchange of the ith and jth rows. (ii) \(kR_i\) for multiplication of the ith row by k. (iii) \(R_i+pR_j\) for addition to the ith row, p times the jth row.
- The corresponding column transformation will be denoted by writing C in place of R.
- Elementary transformations do not change either the order or rank of a matrix. While the value of the minors may get changed by the transformation I and II, their zero or non-zero character remains unaffected.

#### Example 2.24 — Determine the rank of the following matrices (dropdown on web page)

(i) \[\begin{bmatrix}1&2&3\\1&4&2\\2&6&5\end{bmatrix}\]

Solution: (i) Operate \(R_2-R_1\) and \(R_3-2R_1\), so that the given matrix

\[\sim\begin{bmatrix}1&2&3\\0&2&-1\\0&2&-1\end{bmatrix}=A\text{ (say)}\]

Obviously, the 3rd order minor of \(A\) vanishes. Also its 2nd order minors formed by its 2nd and 3rd rows are all zero. But another 2nd order minor is \(\begin{vmatrix}1&3\\0&-1\end{vmatrix}=-1\ne0\).

\[\therefore\ \rho(A)=2.\] Hence the rank of the given matrix is 2.

(ii) \[\begin{bmatrix}0&1&-3&-1\\1&0&1&1\\3&1&0&2\\1&1&-2&0\end{bmatrix}\]

Given matrix

\[\sim\begin{bmatrix}0&1&-3&-1\\1&0&0&0\\3&0&0&0\\1&0&0&0\end{bmatrix}\quad[\text{Operating }C_3-C_1,\ C_4-C_1]\]

\[\sim\begin{bmatrix}0&1&-3&-1\\1&0&0&0\\0&0&0&0\\0&0&0&0\end{bmatrix}\quad[\text{Operating }R_3-3R_2,\ R_4-R_2]\]

\[\sim\begin{bmatrix}0&1&0&0\\1&0&0&0\\0&0&0&0\\0&0&0&0\end{bmatrix}=A\text{ (say)}\quad[\text{Operating }C_3+3C_2,\ C_4+C_2]\]

Obviously, the 4th order minor of \(A\) is zero. Also every 3rd order minor of \(A\) is zero. But, of all the 2nd order minors, only \(\begin{vmatrix}0&1\\1&0\end{vmatrix}=-1\ne0\).

\[\therefore\ \rho(A)=2.\] Hence the rank of the given matrix is 2.

### 2.7 (3) Equivalent matrix

Two matrices A and B are said to be equivalent if one can be obtained from the other by a sequence of elementary transformations. Two equivalent matrices have the same order and the same rank. The symbol ~ is used for equivalence.


## Inverse of non-singular matrices by Gauss-Jordan method

### 2.7 (6) Gauss-Jordan method of finding the inverse

Those elementary row transformations which reduce a given square matrix A to the unit matrix, when applied to unit matrix I give the inverse of A.

Let the successive row transformations which reduce A to I result from pre-multiplication by the elementary matrices \(R_1,R_2,\ldots,R_i\), so that

\[R_iR_{i-1}\cdots R_2R_1A=I\]

\[R_iR_{i-1}\cdots R_2R_1AA^{-1}=IA^{-1}\]

or \[R_iR_{i-1}\cdots R_2R_1I=A^{-1}\qquad[\because\ AA^{-1}=I]\]

Hence the result.

Working rule to evaluate A⁻¹. Write the two matrices A and I side by side. Then perform the same row transformations on both. As soon as A is reduced to I, the other matrix represents A⁻¹.

#### Example 2.25 — Using the Gauss-Jordan method, find the inverse of the matrix (dropdown on web page)

\[A=\begin{bmatrix}1&1&3\\1&3&-3\\-2&-4&-4\end{bmatrix}\]

Solution: Writing the same matrix side by side with the unit matrix of order 3, we have

\[\left[\begin{array}{ccc:ccc}1&1&3&1&0&0\\1&3&-3&0&1&0\\-2&-4&-4&0&0&1\end{array}\right]\quad[\text{Operate }R_2-R_1\text{ and }R_3+2R_1]\]

\[\sim\left[\begin{array}{ccc:ccc}1&1&3&1&0&0\\0&2&-6&-1&1&0\\0&-2&2&2&0&1\end{array}\right]\quad[\text{Operate }\dfrac12R_2\text{ and }\dfrac12R_3]\]

\[\sim\left[\begin{array}{ccc:ccc}1&1&3&1&0&0\\0&1&-3&-\dfrac12&\dfrac12&0\\0&-1&1&1&0&\dfrac12\end{array}\right]\quad[\text{Operate }R_1-R_2\text{ and }R_3+R_2]\]

\[\sim\left[\begin{array}{ccc:ccc}1&0&6&\dfrac32&-\dfrac12&0\\0&1&-3&-\dfrac12&\dfrac12&0\\0&0&-2&\dfrac12&\dfrac12&\dfrac12\end{array}\right]\]

\[\left[\text{Operate }R_1+3R_3,\ R_2-\dfrac32R_3\text{ and }\left(-\dfrac12\right)R_3\right]\]

\[\sim\left[\begin{array}{ccc:ccc}1&0&0&3&1&\dfrac32\\0&1&0&-\dfrac54&-\dfrac14&-\dfrac34\\0&0&1&-\dfrac14&-\dfrac14&-\dfrac14\end{array}\right]\]

Hence the inverse of the given matrix is

\[A^{-1}=\begin{bmatrix}3&1&\dfrac32\\-\dfrac54&-\dfrac14&-\dfrac34\\-\dfrac14&-\dfrac14&-\dfrac14\end{bmatrix}.\]


## Rank of a matrix by Normal form

### 2.7 (7) Normal form of a matrix

Every non-zero matrix A of rank r, can be reduced by a sequence of elementary transformations, to the form

\[\begin{bmatrix}I_r&0\\0&0\end{bmatrix}\]

called the normal form of A.

- Cor. 1. The rank of a matrix A is r if and only if it can be reduced to the normal form (i).
- Cor. 2. Since each elementary transformation can be effected by pre-multiplication or post-multiplication with a suitable elementary matrix and each elementary matrix is non-singular, therefore, we have the following result:
- Corresponding to every matrix A of rank r, there exist non-singular matrices P and Q such that PAQ equals (i).
- If A be a \(m\times n\) matrix, then P and Q are square matrices of orders m and n respectively.

#### Example 2.26 — Reduce the following matrix into its normal form and hence find its rank (dropdown on web page)

\[A=\begin{bmatrix}2&3&-1&-1\\1&-1&-2&-4\\3&1&3&-2\\6&3&0&-7\end{bmatrix}\]

Solution:

\[A\sim\begin{bmatrix}1&-1&-2&-4\\2&3&-1&-1\\3&1&3&-2\\6&3&0&-7\end{bmatrix}\quad[\text{By }R_{12}]\]

\[\sim\begin{bmatrix}1&-1&-2&-4\\0&5&3&7\\0&4&9&10\\0&9&12&17\end{bmatrix}\quad[\text{By }R_2-2R_1,\ R_3-3R_1,\ R_4-6R_1]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&5&3&7\\0&4&9&10\\0&9&12&17\end{bmatrix}\quad[\text{By }C_2+C_1,\ C_3+2C_1,\ C_4+4C_1]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&5&3&7\\0&4&9&10\\0&0&0&0\end{bmatrix}\quad[\text{By }R_4-R_2-R_3]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&1&-6&-3\\0&4&9&10\\0&0&0&0\end{bmatrix}\quad[\text{By }R_2-R_3]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&1&-6&-3\\0&0&33&22\\0&0&0&0\end{bmatrix}\quad[\text{By }R_3-4R_2]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&33&22\\0&0&0&0\end{bmatrix}\quad[\text{By }C_3+6C_2,\ C_4+3C_2]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&22\\0&0&0&0\end{bmatrix}\quad\left[\text{By }\dfrac1{33}C_3\right]\]

\[\sim\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&0\end{bmatrix}\quad[\text{By }C_4-22C_3]\]

\[\sim\begin{bmatrix}I_3&0\\0&0\end{bmatrix}\]

Hence \(\rho(A)=3\).

#### Example 2.27 — Find non-singular matrices P and Q such that A is reduced to normal form. Also find the rank of A (dropdown on web page)

\[A=\begin{bmatrix}1&2&3&4\\2&1&4&3\\3&0&5&-10\end{bmatrix}\]

Solution: Total number of rows = 3. ∴ Consider unit matrix I₃. Total number of columns = 4. ∴ Consider unit matrix I₄.

\[A_{3\times4}=I_3AI_4\]

\[\begin{bmatrix}1&2&3&4\\2&1&4&3\\3&0&5&-10\end{bmatrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}A\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

Our aim is to reduce A to normal form by using elementary transformations.

\[R_2-2R_1,\ R_3-3R_1\]

\[\begin{bmatrix}1&2&3&4\\0&-3&-2&-5\\0&-6&-4&-22\end{bmatrix}=\begin{bmatrix}1&0&0\\-2&1&0\\-3&0&1\end{bmatrix}A\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

\[C_2-2C_1,\ C_3-3C_1,\ C_4-4C_1\]

\[\begin{bmatrix}1&0&0&0\\0&-3&-2&-5\\0&-6&-4&-22\end{bmatrix}=\begin{bmatrix}1&0&0\\-2&1&0\\-3&0&1\end{bmatrix}A\begin{bmatrix}1&-2&-3&-4\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(R_3-2R_2\),

\[\begin{bmatrix}1&0&0&0\\0&-3&-2&-5\\0&0&0&-12\end{bmatrix}=\begin{bmatrix}1&0&0\\-2&1&0\\1&-2&1\end{bmatrix}A\begin{bmatrix}1&-2&-3&-4\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(-R_2,-R_3\),

\[\begin{bmatrix}1&0&0&0\\0&3&2&5\\0&0&0&12\end{bmatrix}=\begin{bmatrix}1&0&0\\2&-1&0\\-1&2&-1\end{bmatrix}A\begin{bmatrix}1&-2&-3&-4\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(C_2-C_3\),

\[\begin{bmatrix}1&0&0&0\\0&1&2&5\\0&0&0&12\end{bmatrix}=\begin{bmatrix}1&0&0\\2&-1&0\\-1&2&-1\end{bmatrix}A\begin{bmatrix}1&1&-3&-4\\0&1&0&0\\0&-1&1&0\\0&0&0&1\end{bmatrix}\]

By \(C_3-2C_2,\ C_4-5C_2\),

\[\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&12\end{bmatrix}=\begin{bmatrix}1&0&0\\2&-1&0\\-1&2&-1\end{bmatrix}A\begin{bmatrix}1&1&-5&-9\\0&1&-2&-5\\0&-1&3&5\\0&0&0&1\end{bmatrix}\]

By \(\dfrac1{12}R_3\),

\[\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\end{bmatrix}=\begin{bmatrix}1&0&0\\2&-1&0\\-\dfrac1{12}&\dfrac16&-\dfrac1{12}\end{bmatrix}A\begin{bmatrix}1&1&-5&-9\\0&1&-2&-5\\0&-1&3&5\\0&0&0&1\end{bmatrix}\]

By \(C_{34}\),

\[\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\end{bmatrix}=\begin{bmatrix}1&0&0\\2&-1&0\\-\dfrac1{12}&\dfrac16&-\dfrac1{12}\end{bmatrix}A\begin{bmatrix}1&1&-9&-5\\0&1&-5&-2\\0&-1&5&3\\0&0&1&0\end{bmatrix}\]

\[[I_3:0]=PAQ\]

Here PAQ is in normal form \(\rho(A)=3\).

\[P=\begin{bmatrix}1&0&0\\2&-1&0\\-\dfrac1{12}&\dfrac16&-\dfrac1{12}\end{bmatrix},\qquad Q=\begin{bmatrix}1&1&-9&-5\\0&1&-5&-2\\0&-1&5&3\\0&0&1&0\end{bmatrix}\]

Here P and Q are non-singular matrices.

#### Example 2.28 — For the matrix A, find non-singular matrices P and Q in the normal form (dropdown on web page)

\[A=\begin{bmatrix}2&1&-3&-6\\3&-3&1&2\\-1&1&1&2\end{bmatrix}\]

Solution: Order of A = 3 × 4. Total number of rows in A = 3. ∴ Consider unit matrix I₃. Total number of columns in A = 4. ∴ Consider unit matrix I₄.

\[A_{3\times4}=I_3AI_4\]

By \(R_{13}\),

PankusDesk source note: the printed question has −1 as the first entry of the third row, but the book’s first displayed step after R₁₃ uses +1. The remaining printed working is reproduced as printed, following that +1 entry.

\[\begin{bmatrix}1&1&1&2\\3&-3&1&2\\2&1&-3&-6\end{bmatrix}=\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}A\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(R_2-3R_1,\ R_3-2R_1\),

\[\begin{bmatrix}1&1&1&2\\0&-6&-2&-4\\0&-1&-5&-10\end{bmatrix}=\begin{bmatrix}0&0&1\\0&1&-3\\1&0&-2\end{bmatrix}A\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(C_2-C_1,\ C_3-C_1,\ C_4-2C_1\),

\[\begin{bmatrix}1&0&0&0\\0&-6&-2&-4\\0&-1&-5&-10\end{bmatrix}=\begin{bmatrix}0&0&1\\0&1&-3\\1&0&-2\end{bmatrix}A\begin{bmatrix}1&-1&-1&-2\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(-R_2,-R_3\) and then followed by \(R_{23}\),

\[\begin{bmatrix}1&0&0&0\\0&1&5&10\\0&6&2&4\end{bmatrix}=\begin{bmatrix}0&0&1\\-1&0&2\\0&-1&3\end{bmatrix}A\begin{bmatrix}1&-1&-1&-2\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(R_3-6R_2\),

\[\begin{bmatrix}1&0&0&0\\0&1&5&10\\0&0&-28&-56\end{bmatrix}=\begin{bmatrix}0&0&1\\-1&0&2\\6&-1&-9\end{bmatrix}A\begin{bmatrix}1&-1&-1&-2\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(C_3-5C_2,\ C_4-10C_2\),

\[\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&-28&-56\end{bmatrix}=\begin{bmatrix}0&0&1\\-1&0&2\\6&-1&-9\end{bmatrix}A\begin{bmatrix}1&-1&4&8\\0&1&-5&-10\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(-\dfrac1{28}R_3\),

\[\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&2\end{bmatrix}=\begin{bmatrix}0&0&1\\-1&0&2\\-\dfrac6{28}&\dfrac1{28}&\dfrac9{28}\end{bmatrix}A\begin{bmatrix}1&-1&4&8\\0&1&-5&-10\\0&0&1&0\\0&0&0&1\end{bmatrix}\]

By \(C_4-2C_3\),

\[\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\end{bmatrix}=\begin{bmatrix}0&0&1\\-1&0&2\\-\dfrac6{28}&\dfrac1{28}&\dfrac9{28}\end{bmatrix}A\begin{bmatrix}1&-1&4&0\\0&1&-5&0\\0&0&1&-2\\0&0&0&1\end{bmatrix}\]

\[[I_3:0]=PAQ\]

PAQ is in normal form. P, Q are non-singular matrices.

\[\rho(A)=3.\]


## System of linear equations

### 2.9 Solution of Linear System of Equations

Consider the equations \[\begin{aligned}a_1x+b_1y+c_1z&=d_1\\a_2x+b_2y+c_2z&=d_2\\a_3x+b_3y+c_3z&=d_3\end{aligned}\]

### (1) Method of determinants — Cramer’s rule

If the determinant of coefficient be \[\Delta=\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix},\]

then \[x=\dfrac{\begin{vmatrix}d_1&b_1&c_1\\d_2&b_2&c_2\\d_3&b_3&c_3\end{vmatrix}}{\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}},\qquad \Delta\ne0,\]

Similarly, \[y=\dfrac{\begin{vmatrix}a_1&d_1&c_1\\a_2&d_2&c_2\\a_3&d_3&c_3\end{vmatrix}}{\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}},\]

and \[z=\dfrac{\begin{vmatrix}a_1&b_1&d_1\\a_2&b_2&d_2\\a_3&b_3&d_3\end{vmatrix}}{\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}}.\]

Equations (ii), (iii) and (iv) giving the values of x, y, z constitute the Cramer’s rule, which reduces the solution of the linear Eqn. (i) to a problem in evaluation of determinants.

#### Example 2.31 — Solve the equations by (i) determinants (ii) matrices (dropdown on web page)

Solve the equations \(3x+y+2z=3,\ 2x-3y-z=-3,\ x+2y+z=4\) by (i) determinants (ii) matrices.

Solution: (i) By determinants:

\[\Delta=\begin{vmatrix}3&1&2\\2&-3&-1\\1&2&1\end{vmatrix}=3(-3+2)-2(1-4)+(-1+6)=8\quad[\text{Expanding by }C_1]\]

\[x=\dfrac1\Delta\begin{vmatrix}3&1&2\\-3&-3&-1\\4&2&1\end{vmatrix}=\dfrac18[3(-3+2)+3(1-4)+4(-1+6)]=1\]

Similarly, \(y=\dfrac1\Delta\begin{vmatrix}3&3&2\\2&-3&-1\\1&4&1\end{vmatrix}=2\) and \(z=\dfrac1\Delta\begin{vmatrix}3&1&3\\2&-3&-3\\1&2&4\end{vmatrix}=-1\).

Hence \(x=1,\ y=2,\ z=-1\).

Note. The use of Cramer’s rule involves a lot of labour when the number of equations exceeds four. In such and other cases, the numerical methods given in § 28.4 to 28.6 are preferable.

(ii) By matrices:

Here \[\Delta=\begin{vmatrix}3&1&2\\2&-3&-1\\1&2&1\end{vmatrix}=\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}\text{ (say)}.\]

Then \(A_1=-1,A_2=3,A_3=5;\ B_1=-3,B_2=1,B_3=7;\ C_1=7,C_2=-5,C_3=-11\). Also \(\Delta=a_1A_1+a_2A_2+a_3A_3=8\).

\[\begin{bmatrix}x\\y\\z\end{bmatrix}=\dfrac1\Delta\begin{bmatrix}A_1&A_2&A_3\\B_1&B_2&B_3\\C_1&C_2&C_3\end{bmatrix}\begin{bmatrix}d_1\\d_2\\d_3\end{bmatrix}\]

\[=\dfrac18\begin{bmatrix}-1&3&5\\-3&1&7\\7&-5&-11\end{bmatrix}\begin{bmatrix}3\\-3\\4\end{bmatrix}=\dfrac18\begin{bmatrix}-3-9+20\\-9-3+28\\21+15-44\end{bmatrix}=\begin{bmatrix}1\\2\\-1\end{bmatrix}.\]

Hence \(x=1,y=2,z=-1\).

### (2) Matrix inversion method

If \[A=\begin{bmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{bmatrix},\quad X=\begin{bmatrix}x\\y\\z\end{bmatrix}\quad\text{and}\quad D=\begin{bmatrix}d_1\\d_2\\d_3\end{bmatrix},\]

then the Eqn. (i) are equivalent to the matrix equation \(AX=D\), where A is the coefficient matrix.

Multiplying both sides of Eqn. (v) by the reciprocal matrix \(A^{-1}\), we get \[A^{-1}AX=A^{-1}D\quad\text{or}\quad IX=A^{-1}D\qquad[\because\ A^{-1}A=I]\]

or \[X=A^{-1}D\quad\text{i.e.,}\quad\begin{bmatrix}x\\y\\z\end{bmatrix}=\dfrac1\Delta\begin{bmatrix}A_1&A_2&A_3\\B_1&B_2&B_3\\C_1&C_2&C_3\end{bmatrix}\begin{bmatrix}d_1\\d_2\\d_3\end{bmatrix},\]

where \(A_1,B_1\) etc. are the cofactors of \(a_1,b_1\) etc. in the determinant \(\Delta=\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}\) \((\Delta\ne0)\).

Hence equating the values of x, y, z to the corresponding elements in the product on the right side of (vi), we get the desired solutions.

Obs. When A is a singular matrix, i.e., Δ = 0, the above methods fail. These also fail when the number of equations and the number of unknowns are unequal. Matrices can, however, be usefully applied to deal with such equations as will be seen in § 2.10(2).

#### Example 2.32 — Solve by finding the inverse by elementary row operations (dropdown on web page)

Solve the equations \(x_1-x_2+x_3+x_4=2;\ x_1+x_2-x_3+x_4=-4;\ x_1+x_2+x_3-x_4=4;\ x_1+x_2+x_3+x_4=0\), by finding the inverse by elementary row operations.

Solution: Given system can be written as AX = B, where

\[A=\begin{bmatrix}1&-1&1&1\\1&1&-1&1\\1&1&1&-1\\1&1&1&1\end{bmatrix},\quad X=\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix},\quad B=\begin{bmatrix}2\\-4\\4\\0\end{bmatrix}.\]

To find A⁻¹, we write

\[\left[A:I\right]=\left[\begin{array}{cccc:cccc}1&-1&1&1&1&0&0&0\\1&1&-1&1&0&1&0&0\\1&1&1&-1&0&0&1&0\\1&1&1&1&0&0&0&1\end{array}\right]\]

\[\sim\left[\begin{array}{cccc:cccc}1&-1&1&1&1&0&0&0\\0&2&-2&0&-1&1&0&0\\2&0&2&0&1&0&1&0\\2&0&2&2&1&0&0&1\end{array}\right]\quad\left[\begin{array}{l}R_2-R_1\\R_3+R_1\\R_4+R_1\end{array}\right]\]

\[\sim\left[\begin{array}{cccc:cccc}1&-1&1&1&1&0&0&0\\0&1&-1&0&-\dfrac12&\dfrac12&0&0\\1&0&1&0&\dfrac12&0&\dfrac12&0\\1&0&1&1&\dfrac12&0&0&\dfrac12\end{array}\right]\quad\left[\begin{array}{l}\dfrac12R_2\\\dfrac12R_3\\\dfrac12R_4\end{array}\right]\]

\[\sim\left[\begin{array}{cccc:cccc}1&0&0&1&\dfrac12&\dfrac12&0&0\\0&1&-1&0&-\dfrac12&\dfrac12&0&0\\1&0&1&0&\dfrac12&0&\dfrac12&0\\0&0&0&1&0&0&-\dfrac12&\dfrac12\end{array}\right]\quad\left[\begin{array}{l}R_1+R_2\\R_4-R_3\end{array}\right]\]

\[\sim\left[\begin{array}{cccc:cccc}1&0&0&0&\dfrac12&\dfrac12&\dfrac12&-\dfrac12\\1&1&0&0&0&\dfrac12&\dfrac12&0\\1&0&1&0&\dfrac12&0&\dfrac12&0\\0&0&0&1&0&0&-\dfrac12&\dfrac12\end{array}\right]\quad\left[\begin{array}{l}R_1-R_4\\R_2+R_3\end{array}\right]\]

\[\sim\left[\begin{array}{cccc:cccc}1&0&0&0&\dfrac12&\dfrac12&\dfrac12&-\dfrac12\\0&1&0&0&-\dfrac12&0&0&\dfrac12\\0&0&1&0&0&-\dfrac12&0&\dfrac12\\0&0&0&1&0&0&-\dfrac12&\dfrac12\end{array}\right]\quad\left[\begin{array}{l}R_2-R_1\\R_3-R_1\end{array}\right]\]

Thus,

\[A^{-1}=\begin{bmatrix}\dfrac12&\dfrac12&\dfrac12&-\dfrac12\\-\dfrac12&0&0&\dfrac12\\0&-\dfrac12&0&\dfrac12\\0&0&-\dfrac12&\dfrac12\end{bmatrix}.\]

Hence,

\[X=A^{-1}B=\begin{bmatrix}\dfrac12&\dfrac12&\dfrac12&-\dfrac12\\-\dfrac12&0&0&\dfrac12\\0&-\dfrac12&0&\dfrac12\\0&0&-\dfrac12&\dfrac12\end{bmatrix}\begin{bmatrix}2\\-4\\4\\0\end{bmatrix}=\begin{bmatrix}1\\-1\\2\\-2\end{bmatrix}.\]

i.e., \(x_1=1,x_2=-1,x_3=2,x_4=-2\).


## Solving systems of non-homogeneous equations

### 2.10 (1) Consistency of Linear System of Equations

Consider the system of m linear equations

\[\begin{aligned}a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=k_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=k_2\\&\vdots\\a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=k_m\end{aligned}\]

containing the n unknowns x₁, x₂, …, xₙ. To determine whether the Eqn. (i) are consistent (i.e., possess a solution) or not, we consider the ranks of the matrices

\[A=\begin{bmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{bmatrix}\quad\text{and}\quad K=\begin{bmatrix}a_{11}&a_{12}&\cdots&a_{1n}&k_1\\a_{21}&a_{22}&\cdots&a_{2n}&k_2\\\vdots&\vdots&&\vdots&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}&k_m\end{bmatrix}.\]

A is the co-efficient matrix and K is called the augmented matrix of the Eqn. (i).

### (2) Rouche’s theorem

The system of Eqn. (i) is consistent if and only if the coefficient matrix A and the augmented matrix K are of the same rank otherwise the system is inconsistent.

Proof. We consider the following two possible cases:

I. Rank of A = rank of K = r (r ≤ the smaller of the numbers m and n). The Eqn. (i) can, be suitable row operations, be reduced to

\[\begin{aligned}b_{11}x_1+b_{12}x_2+\cdots+b_{1n}x_n&=l_1\\0x_1+b_{22}x_2+\cdots+b_{2n}x_n&=l_2\\&\vdots\\0x_1+0x_2+\cdots+b_{rn}x_n&=l_r\end{aligned}\]

and the remaining m − r equations being all of the form 0x₁ + 0x₂ + …… + 0xₙ = 0.

The Eqn. (ii) will have a solution, though n − r of the unknowns may be chosen arbitrarily. The solution, will be unique only when r = n. Hence the Eqn. (i) are consistent.

II. Rank of A (i.e., r) < rank of K. In particular, let the rank of K be r + 1. In this case, the Eqn. (i) will reduce, by suitable row operations, to

\[\begin{aligned}b_{11}x_1+b_{12}x_2+\cdots+b_{1n}x_n&=l_1\\0x_1+b_{22}x_2+\cdots+b_{2n}x_n&=l_2\\&\vdots\\0x_1+0x_2+\cdots+b_{rn}x_n&=l_r\\0x_1+0x_2+\cdots+0x_n&=l_{r+1}\end{aligned}\]

and the remaining m − (r + 1) equations are of the form 0x₁ + 0x₂ + … + 0xₙ = 0.

Clearly, the (r + 1)th equation cannot be satisfied by any set of values for the unknowns. Hence the Eqn. (i) are inconsistent.

### Procedure to test the consistency of a system of equations in n unknowns

Find the ranks of the coefficient matrix A and the augmented matrix K, by reducing A to the triangular form by elementary row operations. Let the rank of A be r and that of K be r′.

- If r ≠ r′, the equations are inconsistent, i.e., there is no solution.
- If r = r′ = n, the equations are consistent and there is a unique solution.
- If r = r′ < n, the equations are consistent and there are infinite number of solutions. Giving arbitrary values to n − r of the unknowns, we may express the other r unknowns in terms of these.

#### Example 2.33 — Test for consistency and solve (dropdown on web page)

Test for consistency and solve \(5x+3y+7z=4,\ 3x+26y+2z=9,\ 7x+2y+10z=5\).

Solution: We have

\[\begin{bmatrix}5&3&7\\3&26&2\\7&2&10\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}4\\9\\5\end{bmatrix}.\]

Operate \(3R_1,5R_2\): \[\begin{bmatrix}15&9&21\\15&130&10\\7&2&10\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}12\\45\\5\end{bmatrix}.\]

Operate \(R_2-R_1\): \[\begin{bmatrix}15&9&21\\0&121&-11\\7&2&10\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}12\\33\\5\end{bmatrix}.\]

Operate \(\dfrac73R_1,5R_3,\dfrac1{11}R_2\): \[\begin{bmatrix}35&21&49\\0&11&-1\\35&10&50\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}28\\3\\25\end{bmatrix}.\]

Operate \(R_3-R_1+R_2,\dfrac17R_1\): \[\begin{bmatrix}5&3&7\\0&11&-1\\0&0&0\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}4\\3\\0\end{bmatrix}.\]

The ranks of coefficient matrix and augmented matrix for the last set of equations, are both 2. Hence the equations are consistent. Also the given system is equivalent to

\[5x+3y+7z=4,\qquad 11y-z=3,\qquad \therefore\ y=\dfrac3{11}+\dfrac z{11}\quad\text{and}\quad x=\dfrac7{11}-\dfrac{16}{11}z,\]

where z is a parameter.

Hence \(x=\dfrac7{11},y=\dfrac3{11}\) and \(z=0\), is a particular solution.

Obs. In the above solution, the coefficient matrix is reduced to an upper triangular matrix by row-transformations.

#### Example 2.34 — Investigate λ and μ for no, unique and infinitely many solutions (dropdown on web page)

Investigate the values of \(\lambda\) and \(\mu\) so that the equations \(2x+3y+5z=9,\ 7x+3y-2z=8,\ 2x+3y+\lambda z=\mu\), have (i) no solution, (ii) a unique solution and (iii) an infinite number of solutions.

Solution: We have

\[\begin{bmatrix}2&3&5\\7&3&-2\\2&3&\lambda\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}9\\8\\\mu\end{bmatrix}.\]

The system admits of unique solution if, and only if, the coefficient matrix is of rank 3. This requires that

\[\begin{vmatrix}2&3&5\\7&3&-2\\2&3&\lambda\end{vmatrix}=15(5-\lambda)\ne0.\]

Thus for a unique solution \(\lambda\ne5\) and \(\mu\) may have any value. If \(\lambda=5\), the system will have no solution for those values of \(\mu\) for which the matrices

\[A=\begin{bmatrix}2&3&5\\7&3&-2\\2&3&5\end{bmatrix}\quad\text{and}\quad K=\begin{bmatrix}2&3&5&9\\7&3&-2&8\\2&3&5&\mu\end{bmatrix}\]

are not of the same rank. But A is of rank 2 and K is not of rank 2 unless μ = 9. Thus if λ = 5 and μ ≠ 9, the system will have no solution.

If λ = 5 and μ = 9, the system will have an infinite number of solutions.

#### Example 2.35 — Test for consistency and solve if consistent (dropdown on web page)

Test for consistency the following equations and solve them if consistent: \(x-2y+3t=2,\ 2x+y+z+t=-4,\ 4x-3y+z+7t=8\).

Solution: Given equation can be written as

\[\begin{bmatrix}1&-2&0&3\\2&1&1&1\\4&-3&1&7\end{bmatrix}\begin{bmatrix}x\\y\\z\\t\end{bmatrix}=\begin{bmatrix}2\\-4\\8\end{bmatrix}.\]

Operate \(R_2-2R_1,R_3-4R_1\): \[\begin{bmatrix}1&-2&0&3\\0&5&1&-5\\0&5&1&-5\end{bmatrix}\begin{bmatrix}x\\y\\z\\t\end{bmatrix}=\begin{bmatrix}2\\0\\0\end{bmatrix}.\]

Operate \(R_3-R_2\): \[\begin{bmatrix}1&-2&0&3\\0&5&1&-5\\0&0&0&0\end{bmatrix}\begin{bmatrix}x\\y\\z\\t\end{bmatrix}=\begin{bmatrix}2\\0\\0\end{bmatrix}.\]

Clearly, rank of the coefficient matrix is 2 and the rank of augmented matrix is also 2. Hence the given equations are consistent. But the rank 2 < 4, the number of unknowns.

∴ The number of parameters is 4 − 2 = 2. Thus the equations have doubly infinite solutions. Now putting t = k₁ and z = k₂ in

\[x-2y+3t=2\qquad\text{and}\qquad 5y+z-5t=0,\]

we get \(x-2y+3k_1=2\) and \(5y+k_2-5k_1=0\). Hence \(y=k_1-\dfrac{k_2}{5}\) and

\[x=2+2y-3k_1=2+2\left(k_1-\dfrac{k_2}{5}\right)-3k_1=2-k_1-\dfrac25k_2.\]

#### Example 2.37 — Parameter μ: unique solution, inconsistency and general solution (dropdown on web page)

Show that if \(\mu\ne0\), the system of equations \(2x+y=a,\ x+\mu y-z=b,\ y+2z=c\) has unique solution for every choice of a, b, c. If \(\mu=0\), determine the relation satisfied by a, b, c such that the system is inconsistent. Find the general solution by taking \(\mu=0,a=1,b=1,c=-1\).

Solution: Part 1. The above system of equations in matrix form can be written as

\[\begin{bmatrix}2&1&0\\1&\mu&-1\\0&1&2\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}a\\b\\c\end{bmatrix}.\]

Here 3 equations in 3 unknowns are there, hence we will apply another method.

\[|A|=\begin{vmatrix}2&1&0\\1&\mu&-1\\0&1&2\end{vmatrix}=2(2\mu+1)-1(2)=4\mu.\]

If \(\mu\ne0\), \(|A|\ne0\), the system \(AX=B\) always possesses a unique solution for every choice of a, b, c.

Part 2: If μ = 0 then,

\[\begin{bmatrix}2&1&0\\1&0&-1\\0&1&2\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}a\\b\\c\end{bmatrix}.\]

Perform \(R_{12}\): \[(A,B)\sim\begin{bmatrix}1&0&-1&|&b\\2&1&0&|&a\\0&1&2&|&c\end{bmatrix}.\]

Perform \(R_2-2R_1\): \[\sim\begin{bmatrix}1&0&-1&|&b\\0&1&2&|&a-2b\\0&1&2&|&c\end{bmatrix}.\]

Perform \(R_3-R_2\): \[\sim\begin{bmatrix}1&0&-1&|&b\\0&1&2&|&a-2b\\0&0&0&|&c-a+2b\end{bmatrix}.\]

If \(\mu=0\) and \(c-a+2b\ne0\) then \(\rho(A)=2,\ \rho(A,B)=3\). Hence if \(\mu=0\) and \(c-a+2b\ne0\) then system possesses no solution.

Part 3: If \(\mu=0,\ c-a+2b=0\) then \(\rho(A)=\rho(A,B)=2<3\). System possesses an infinite number of solutions. Hence, system is consistent if \(\mu=0\) and \(c-a+2b=0\).

Part 4: Take \(\mu=0,a=1,b=1,c=-1\), substituting in equation (i), we get \[(A,B)\sim\begin{bmatrix}1&0&-1&|&1\\0&1&2&|&-1\\0&0&0&|&0\end{bmatrix}.\]

\(\rho(A)=\rho(A,B)=2<3\), system possesses an infinite no. of solutions.

By \(R_2\), \(y+2z=-1\). Let \(z=t\), \(y=-1-2t\). By \(R_1\), \(x-z=1\), \(x=1+t\). Hence, if \(\mu=0,a=1,b=1,c=-1\), then solution set is \(x=1+t,\ y=-1-2t,\ z=t\).

#### Example 2.38 — Examine for consistency by considering the rank of relevant matrices (dropdown on web page)

By considering the rank of relevant matrices, examine for consistency the system of equations \(2x-y-z=2,\ x+2y+z=2,\ 4x-7y-5z=2\) and solve if found consistent.

Solution: Given system of equations in matrix form can be written as

\[\begin{bmatrix}2&-1&-1\\1&2&1\\4&-7&-5\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=\begin{bmatrix}2\\2\\2\end{bmatrix},\quad i.e.,\ AX=B.\]

Consider an augmented matrix

\[(A,B)=\begin{bmatrix}2&-1&-1&|&2\\1&2&1&|&2\\4&-7&-5&|&2\end{bmatrix}.\]

Perform \(R_{12}\): \[\sim\begin{bmatrix}1&2&1&|&2\\2&-1&-1&|&2\\4&-7&-5&|&2\end{bmatrix}.\]

Perform \(R_2-2R_1,R_3-4R_1\): \[\sim\begin{bmatrix}1&2&1&|&2\\0&-5&-3&|&-2\\0&15&-9&|&-6\end{bmatrix}.\]

Perform \(R_3-3R_2\): \[\sim\begin{bmatrix}1&2&1&|&2\\0&-5&-3&|&-2\\0&0&0&|&0\end{bmatrix}.\]

Here, \(\rho(A)=2,\ \rho(A,B)=2\). \(\rho(A)=\rho(A,B)\). ∴ System is Consistent. \(\rho(A)=\rho(A,B)=2<3\), number of Variables.

System possesses an infinite number of solutions given as follows.

By \(R_2\), \(-5y-3z=-2\). Let \(z=t\), \(y=\dfrac{2-3t}{5}\).

By \(R_1\), \(x+2y+z=2\), hence \(x=\dfrac{6+t}{5}\).

Solution set is \(x=\dfrac{6+t}{5},\ y=\dfrac{2-3t}{5},\ z=t\).

#### Example 2.39 — Examine for consistency and obtain the solution if consistent (dropdown on web page)

Examine for consistency the following set of equations and obtain the solution if consistent: \(2x_1+x_2-x_3+3x_4=11,\ x_1-2x_2+x_3+x_4=8,\ 4x_1+7x_2+2x_3-x_4=0,\ 3x_1+5x_2+4x_3+4x_4=17\).

Solution: Given system of equation in matrix form can be written as

\[\begin{bmatrix}2&1&-1&3\\1&-2&1&1\\4&7&2&-1\\3&5&4&4\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\\x_4\end{bmatrix}=\begin{bmatrix}11\\8\\0\\17\end{bmatrix},\quad AX=B.\]

Consider an augmented matrix

\[(A,B)=\begin{bmatrix}2&1&-1&3&|&11\\1&-2&1&1&|&8\\4&7&2&-1&|&0\\3&5&4&4&|&17\end{bmatrix}.\]

By \(R_{12}\): \[\sim\begin{bmatrix}1&-2&1&1&|&8\\2&1&-1&3&|&11\\4&7&2&-1&|&0\\3&5&4&4&|&17\end{bmatrix}.\]

By \(R_2-2R_1,R_3-4R_1,R_4-3R_1\): \[\sim\begin{bmatrix}1&-2&1&1&|&8\\0&5&-3&1&|&-5\\0&15&-2&-5&|&-32\\0&11&1&1&|&-7\end{bmatrix}.\]

By \(R_3-3R_2,\ R_4-\dfrac{11}{5}R_2\): \[\sim\begin{bmatrix}1&-2&1&1&|&8\\0&5&-3&1&|&-5\\0&0&7&-8&|&-17\\0&0&\dfrac{38}{5}&-\dfrac65&|&4\end{bmatrix}.\]



By \(R_4-\dfrac{38}{35}R_3\): \[\sim\begin{bmatrix}1&-2&1&1&|&8\\0&5&-3&1&|&-5\\0&0&7&-8&|&-17\\0&0&0&\dfrac{262}{35}&|&\dfrac{786}{35}\end{bmatrix}.\]

Here \(\rho(A)=4,\ \rho(A,B)=4\). The system is consistent and possesses a unique solution.

By \(R_4\), \(\dfrac{262}{35}x_4=\dfrac{786}{35}\), \(x_4=3\). By \(R_3\), \(7x_3-8x_4=-17\), hence \(x_3=1\). By \(R_2\), \(5x_2-3x_3+x_4=-5\), hence \(x_2=-1\). Finally \(x_1=2\).

Required solution set is \(x_1=2,x_2=-1,x_3=1,x_4=3\).


## Solving systems of homogeneous equations

### 2.10 (3) System of linear homogeneous equations

Consider the homogeneous linear equations

\[\begin{aligned}a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=0\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=0\\&\vdots\\a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=0\end{aligned}\]

Find the rank r of the coefficient matrix A by reducing it to the triangular form by elementary row operations.

I. If r = n, the equations (iii) have only a trivial zero solution \(x_1=x_2=\cdots=x_n=0\).

If r < n, the equation (iii) have (n − r) linearly independent solutions. The number of linearly independent solutions is (n − r) means, if arbitrary values are assigned to (n − r) of the variables, the values of the remaining r variables can be uniquely found. Thus the equations (iii) will have an infinite number of solutions.

II. When m < n (i.e., the number of equations is less than the number of variables), the solution is always other than \(x_1=x_2=\cdots=x_n=0\). The number of solutions is infinite.

III. When m = n (i.e., the number of equations = the number of variables), the necessary and sufficient condition for solutions other than \(x_1=x_2=\cdots=x_n=0\), is that the determinant of the coefficient matrix is zero. In this case the equations are said to be consistent and such a solution is called non-trivial solution. The determinant is called the eliminant of the equations.

#### Example 2.36 — Solve the homogeneous equations (dropdown on web page)

(i) \(x+2y+3z=0,\ 3x+4y+4z=0,\ 7x+10y+12z=0\).

(ii) \(4x+2y+z+3w=0,\ 6x+3y+4z+7w=0,\ 2x+y+w=0\).

Solution: (i) Rank of the coefficient matrix

\[\begin{bmatrix}1&2&3\\3&4&4\\7&10&12\end{bmatrix}\sim\begin{bmatrix}1&2&3\\0&-2&-5\\7&10&12\end{bmatrix}\quad[\text{Operating }R_2-3R_1]\]

\[\sim\begin{bmatrix}1&2&3\\0&-2&-5\\0&0&1\end{bmatrix}\quad[\text{Operating }R_3-7R_1-2R_2]\]

is 3 which = the number of variables (i.e., r = n). ∴ The equations have only a trivial solution: x = y = z = 0.

(ii) Rank of the coefficient matrix

\[\begin{bmatrix}4&2&1&3\\6&3&4&7\\2&1&0&1\end{bmatrix}\sim\begin{bmatrix}4&2&1&3\\0&0&\dfrac52&\dfrac52\\0&0&-\dfrac12&-\dfrac12\end{bmatrix}\quad\left[\text{Operating }R_2-\dfrac32R_1,\ R_3-\dfrac12R_1\right]\]

\[\sim\begin{bmatrix}4&2&1&3\\0&0&\dfrac52&\dfrac52\\0&0&0&0\end{bmatrix}\quad\left[\text{Operating }R_3+\dfrac15R_2\right]\]

is 2 which < the number of variable (i.e., r < n). ∴ Number of independent solutions = 4 − 2 = 2. Given system is equivalent to

\[4x+2y+z+3w=0,\qquad z+w=0.\]

∴ We have \(z=-w\) and \(y=-2x-w\), which give an infinite number of non-trivial solutions, x and w being the parameters.

#### Example 2.40 — Find λ for consistency and the ratios x : y : z (dropdown on web page)

Find the values of \(\lambda\) for which the equations \((\lambda-1)x+(3\lambda+1)y+2\lambda z=0,\ (\lambda-1)x+(4\lambda-2)y+(\lambda+3)z=0,\ 2x+(3\lambda+1)y+3(\lambda-1)z=0\) are consistent, and find the ratios of x : y : z when λ has the smallest of these values. What happens when λ has the greatest of these values.

Solution: The given equations will be consistent, if

\[\begin{vmatrix}\lambda-1&3\lambda+1&2\lambda\\\lambda-1&4\lambda-2&\lambda+3\\2&3\lambda+1&3(\lambda-1)\end{vmatrix}=0.\]

Operate \(R_2-R_1\): \[\begin{vmatrix}\lambda-1&3\lambda+1&2\lambda\\0&\lambda-3&3-\lambda\\2&3\lambda+1&3(\lambda-1)\end{vmatrix}=0.\]

Operate \(C_3+C_2\): \[\begin{vmatrix}\lambda-1&3\lambda+1&5\lambda+1\\0&\lambda-3&0\\2&3\lambda+1&6\lambda-2\end{vmatrix}=0.\]

Expand by \(R_2\): \[(\lambda-3)\begin{vmatrix}\lambda-1&5\lambda+1\\2&2(3\lambda-1)\end{vmatrix}=0\]

or, \(2(\lambda-3)[(\lambda-1)(3\lambda-1)-(5\lambda+1)]=0\), or, \(6\lambda(\lambda-3)^2=0\), or, \(\lambda=0\) or 3.

(a) When \(\lambda=0\), the equations become \(-x+y=0\), \(-x-2y+3z=0\), \(2x+y-3z=0\).

Solving (ii) and (iii), we get \(\dfrac{x}{6-3}=\dfrac{y}{6-3}=\dfrac{z}{-1+4}\). Hence \(x=y=z\).

(b) When \(\lambda=3\), equations becomes identical.


## Gauss Seidel Iteration Methods

> **PankusDesk context.** Gauss–Seidel is an iterative method for solving simultaneous linear equations. Instead of obtaining the solution through one finite elimination process, we begin with approximate values and repeatedly improve them. The unknowns are calculated one after another, and each newly calculated value is used immediately in the next calculation. This is the key idea behind the textbook’s statement that Gauss–Seidel is a modification of Jacobi’s method.

### (2) Gauss-Seidel iteration method

This is a modification of the Jacobi’s iteration method. As before, we start with initial approximations x₀, y₀, z₀ (each = 0) for x, y, z respectively. Substituting y = y₀, z = z₀ in the first of the Eqn. (2) on page 956, we get

\[x_1=k_1.\]

Then putting x = x₁, z = z₀ in the second of the Eqn. (2) on page 956, we have

\[y_1=k_2-l_2x_1-m_2z_0.\]

Next substituting x = x₁, y = y₁ in the third of the Eqn. (2) on page 956, we obtain

\[z_1=k_3-l_3x_1-m_3y_1\]

and so on, i.e., as soon as new approximation for an unknown is found, it is immediately used in the next step. This process of iteration is continued till convergence to the desired degree of accuracy is obtained.

- Obs. 1. Since the most recent approximation of the unknowns are used while proceeding to the next step, the convergence in the Gauss-Seidel method is faster than in Jacobi’s method.
- Obs. 2. Gauss-Seidel method converges if in each equation, the absolute value of the largest coefficient is greater than the sum of the absolute values of the remaining coefficients.

#### Example 28.22 — Apply Gauss-Seidel iteration method to solve the equations of Ex. 28.21 (dropdown on web page)

Solution. We write the given equation in the form

\[x=\dfrac1{20}(17-y+2z);\qquad y=\dfrac1{20}(-18-3x+z);\qquad z=\dfrac1{20}(25-2x+3y).\]

We start from the approximation x₀ = y₀ = z₀ = 0. Substituting y = y₀, z = z₀ in the right side of the first of equations (i), we get

\[x_1=\dfrac1{20}(17-y_0+2z_0)=0.8500.\]

Putting x = x₁, z = z₀ in the second of the Eqn. (i), we have

\[y_1=\dfrac1{20}(-18-3x_1+z_0)=-1.0275.\]

Putting x = x₁, y = y₁ in the last of the Eqn. (i), we obtain

\[z_1=\dfrac1{20}(25-2x_1+3y_1)=1.0109.\]

For the second iteration, we have

\[x_2=\dfrac1{20}(17-y_1+2z_1)=1.0025,\]

\[y_2=\dfrac1{20}(-18-3x_2+z_1)=-0.9998,\]

\[z_2=\dfrac1{20}(25-2x_2+3y_2)=0.9998.\]

For the third iteration, we get

\[x_3=\dfrac1{20}(17-y_2+2z_2)=1.0000,\]

\[y_3=\dfrac1{20}(-18-3x_3+z_2)=-1.0000,\]

\[z_3=\dfrac1{20}(25-2x_3+3y_3)=1.0000.\]

The values in the 2nd and 3rd iterations being practically the same, we can stop. Hence the solution is x = 1, y = −1, z = 1.

#### Example 28.23 — Solve the equations by Gauss-Seidel iteration method (dropdown on web page)

Solve the equations \(10x_1-2x_2-x_3-x_4=3\), \(-2x_1+10x_2-x_3-x_4=15\), \(-x_1-x_2+10x_3-2x_4=27\), \(-x_1-x_2-2x_3+10x_4=-9\) by Gauss-Seidel iteration method.

Solution. Rewriting the given equations as

\[x_1=0.3+0.2x_2+0.1x_3+0.1x_4\]

\[x_2=1.5+0.2x_1+0.1x_3+0.1x_4\]

\[x_3=2.7+0.1x_1+0.1x_2+0.2x_4\]

\[x_4=-0.9+0.1x_1+0.1x_2+0.2x_3.\]

First iteration

Putting x₂ = 0, x₃ = 0, x₄ = 0 in Eqn.(i), we get x₁ = 0.3.

Putting x₁ = 0.3, x₃ = 0, x₄ = 0 in Eqn.(ii), we obtain x₂ = 1.56.

Putting x₁ = 0.3, x₂ = 1.56, x₄ = 0 in Eqn.(iii), we obtain x₃ = 2.886.

Putting x₁ = 0.3, x₂ = 1.56, x₃ = 2.886 in Eqn.(iv), we get x₄ = −0.1368.

Second iteration

Putting x₂ = 1.56, x₃ = 2.886, x₄ = −0.1368 in Eqn.(i), we obtain x₁ = 0.8869.

Putting x₁ = 0.8869, x₃ = 2.886, x₄ = −0.1368 in Eqn.(ii), we obtain x₂ = 1.9523.

Putting x₁ = 0.8869, x₂ = 1.9523, x₄ = −0.1368 in Eqn.(iii), we have x₃ = 2.9566.

Putting x₁ = 0.8869, x₂ = 1.9523, x₃ = 2.9566 in Eqn.(iv), we get x₄ = −0.0248.

Third iteration

Putting x₂ = 1.9523, x₃ = 2.9566, x₄ = −0.0248 in Eqn.(i), we obtain x₁ = 0.9836.

Putting x₁ = 0.9836, x₃ = 2.9566, x₄ = −0.0248 in Eqn.(ii), we obtain x₂ = 1.9899.

Putting x₁ = 0.9836, x₂ = 1.9899, x₄ = −0.0248 in Eqn.(iii), we get x₃ = 2.9924.

Putting x₁ = 0.9836, x₂ = 1.9899, x₃ = 2.9924 in Eqn.(iv), we get x₄ = −0.0042.

Fourth iteration. Proceeding as above x₁ = 0.9968, x₂ = 1.9982, x₃ = 2.9987, x₄ = −0.0008.

Fifth iteration is x₁ = 0.9994, x₂ = 1.9997, x₃ = 2.9997, x₄ = −0.0001.

Sixth iteration is x₁ = 0.9999, x₂ = 1.9999, x₃ = 2.9999, x₄ = −0.0001.

Hence the solution is x₁ = 1, x₂ = 2, x₃ = 3, x₄ = 0.
