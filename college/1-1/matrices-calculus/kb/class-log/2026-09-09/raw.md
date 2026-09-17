# MAC Class Log — 9 September 2026

Source: seven Unit II notebook photographs, `Mac-class-unit2 - 5.jpg` through `Mac-class-unit2 - 11.jpg`, supplied in `mac_9thSept.zip`.

The top of page 5 still contains the end of the 8 September trace/transpose/inverse example. The new 9 September work begins below the written date with Example 3, so the repeated 8 September material is not duplicated here.

Every class question below was checked against the supplied Grewal Unit II worked examples and in-scope textbook questions before completion. Only exact matches count as textbook matches.

## Example 3 — Find the eigenvalues and corresponding eigenvectors

\[A=\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}.\]

### Aside — exact textbook match

This class matrix is exactly Grewal Problems 2.9 Q3(b), p. 72. The full class-note solution is shown below; the final result is also checked against Appendix 3, p. 1381.

### Complete worked solution

Start with the characteristic equation:
\[|A-\lambda I|=\begin{vmatrix}8-\lambda&-6&2\\-6&7-\lambda&-4\\2&-4&3-\lambda\end{vmatrix}=0.\]
Expand along the first row:
\[(8-\lambda)\begin{vmatrix}7-\lambda&-4\\-4&3-\lambda\end{vmatrix}+6\begin{vmatrix}-6&-4\\2&3-\lambda\end{vmatrix}+2\begin{vmatrix}-6&7-\lambda\\2&-4\end{vmatrix}=0.\]
Evaluate the three minors:
\[(7-\lambda)(3-\lambda)-16=\lambda^2-10\lambda+5,\]
\[(-6)(3-\lambda)+8=6\lambda-10,\]
\[24-2(7-\lambda)=10+2\lambda.\]
Therefore
\[(8-\lambda)(\lambda^2-10\lambda+5)+6(6\lambda-10)+2(10+2\lambda)=0,\]
\[-\lambda^3+18\lambda^2-45\lambda=0,\]
\[-\lambda(\lambda-3)(\lambda-15)=0.\]
Hence the eigenvalues are
\[\boxed{\lambda=0,\ 3,\ 15}.\]
Now find the eigenvector for each eigenvalue.
For \(\lambda=0\), solve \(AX=0\):
\[\begin{bmatrix}8&-6&2\\-6&7&-4\\2&-4&3\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=0.\]
Use \(R_2\to4R_2+3R_1\) and \(R_3\to4R_3-R_1\):
\[\begin{bmatrix}8&-6&2\\0&10&-10\\0&-10&10\end{bmatrix}.\]
Then \(R_3\to R_3+R_2\):
\[\begin{bmatrix}8&-6&2\\0&10&-10\\0&0&0\end{bmatrix}.\]
The second row gives \(y-z=0\Rightarrow y=z\). The first row gives \(8x-6y+2z=0\). Using \(z=y\):
\[8x-4y=0\Rightarrow y=2x.\]
Take \(x=k\). Then \(y=z=2k\), so
\[X_1=k\begin{bmatrix}1\\2\\2\end{bmatrix}.\]
For \(\lambda=3\), solve \((A-3I)X=0\):
\[\begin{bmatrix}5&-6&2\\-6&4&-4\\2&-4&0\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=0.\]
Use \(R_2\to5R_2+6R_1\) and \(R_3\to5R_3-2R_1\):
\[\begin{bmatrix}5&-6&2\\0&-16&-8\\0&-8&-4\end{bmatrix}.\]
Then \(R_3\to2R_3-R_2\):
\[\begin{bmatrix}5&-6&2\\0&-16&-8\\0&0&0\end{bmatrix}.\]
The second row gives \(-16y-8z=0\Rightarrow z=-2y\). Substitute into the first row:
\[5x-6y+2(-2y)=0\Rightarrow5x-10y=0\Rightarrow x=2y.\]
Take \(y=k\). Then
\[X_2=k\begin{bmatrix}2\\1\\-2\end{bmatrix}.\]
For \(\lambda=15\), solve \((A-15I)X=0\):
\[\begin{bmatrix}-7&-6&2\\-6&-8&-4\\2&-4&-12\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=0.\]
Use \(R_2\to7R_2-6R_1\) and \(R_3\to7R_3+2R_1\):
\[\begin{bmatrix}-7&-6&2\\0&-20&-40\\0&-40&-80\end{bmatrix}.\]
Then \(R_3\to R_3-2R_2\):
\[\begin{bmatrix}-7&-6&2\\0&-20&-40\\0&0&0\end{bmatrix}.\]
The second row gives \(y=-2z\). Substitute into the first row:
\[-7x-6(-2z)+2z=0\Rightarrow-7x+14z=0\Rightarrow x=2z.\]
Take \(z=k\). Then
\[X_3=k\begin{bmatrix}2\\-2\\1\end{bmatrix}.\]
Book-answer check: Grewal Appendix 3, p. 1381 prints the roots for Q3(b) as \(0,3,5\), but its own third eigenvector is \([2,-2,1]^T\). Direct multiplication gives \(A[2,-2,1]^T=15[2,-2,1]^T\), and \(\operatorname{tr}(A)=18=0+3+15\). Thus the printed \(5\) is a textbook misprint; the verified third eigenvalue is \(15\).

### Notebook mismatch

In the handwritten final summary for \(\lambda=3\), the third entry of the eigenvector appears without the minus sign. Direct substitution shows that \([2,1,2]^T\) is not an eigenvector for \(\lambda=3\); the verified vector is \([2,1,-2]^T\) (or any non-zero scalar multiple).

### Final answer

\(\lambda=0:[1,2,2]^T;\quad \lambda=3:[2,1,-2]^T;\quad \lambda=15:[2,-2,1]^T\), up to non-zero scalar multiples.

## Example 4 — Find the eigenvalues and eigenvectors

\[A=\begin{bmatrix}6&-2&2\\-2&3&-1\\2&-1&3\end{bmatrix}.\]

### Aside — exact textbook match

This class matrix is exactly Grewal Problems 2.9 Q3(e), p. 72. The full solution is worked below and the final roots/eigenvectors are checked against Appendix 3, p. 1381.

### Complete worked solution

Start with the characteristic equation:
\[|A-\lambda I|=\begin{vmatrix}6-\lambda&-2&2\\-2&3-\lambda&-1\\2&-1&3-\lambda\end{vmatrix}=0.\]
Expand along the first row:
\[(6-\lambda)\begin{vmatrix}3-\lambda&-1\\-1&3-\lambda\end{vmatrix}+2\begin{vmatrix}-2&-1\\2&3-\lambda\end{vmatrix}+2\begin{vmatrix}-2&3-\lambda\\2&-1\end{vmatrix}=0.\]
Now simplify the minors:
\[(3-\lambda)^2-1=\lambda^2-6\lambda+8,\]
\[-2(3-\lambda)+2=2\lambda-4,\]
\[2-2(3-\lambda)=2\lambda-4.\]
Therefore
\[(6-\lambda)(\lambda^2-6\lambda+8)+2(2\lambda-4)+2(2\lambda-4)=0,\]
\[-\lambda^3+12\lambda^2-36\lambda+32=0,\]
\[-(\lambda-8)(\lambda-2)^2=0.\]
Hence the eigenvalues are
\[\boxed{\lambda=8,\ 2,\ 2}.\]
For \(\lambda=8\), solve \((A-8I)X=0\):
\[\begin{bmatrix}-2&-2&2\\-2&-5&-1\\2&-1&-5\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=0.\]
Use \(R_2\to R_2-R_1\) and \(R_3\to R_3+R_1\):
\[\begin{bmatrix}-2&-2&2\\0&-3&-3\\0&-3&-3\end{bmatrix}.\]
Then \(R_3\to R_3-R_2\):
\[\begin{bmatrix}-2&-2&2\\0&-3&-3\\0&0&0\end{bmatrix}.\]
The second row gives \(y+z=0\Rightarrow y=-z\). The first row gives \(-2x-2y+2z=0\Rightarrow x+y-z=0\). Hence
\[x-z-z=0\Rightarrow x=2z.\]
Take \(z=k\). Then
\[X_1=k\begin{bmatrix}2\\-1\\1\end{bmatrix}.\]
For the repeated eigenvalue \(\lambda=2\), solve \((A-2I)X=0\):
\[\begin{bmatrix}4&-2&2\\-2&1&-1\\2&-1&1\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=0.\]
Here \(R_1=-2R_2\) and \(R_3=-R_2\), so there is only one independent equation:
\[-2x+y-z=0\Rightarrow y=2x+z.\]
There are two free variables, so two independent eigenvectors can be chosen.
Choose \(x=1,z=0\). Then \(y=2\), giving
\[X_2=\begin{bmatrix}1\\2\\0\end{bmatrix}.\]
Choose \(x=1,z=-2\). Then \(y=0\), giving
\[X_3=\begin{bmatrix}1\\0\\-2\end{bmatrix}.\]
Priyanka writes the second \(\lambda=2\) direction as \([-1,0,2]^T\). This is \(-1\) times \([1,0,-2]^T\), so it is the same eigenvector direction.
Book-answer check: Grewal Appendix 3, p. 1381 gives roots \(8,2,2\) with eigenvectors \((2,-1,1)\), \((1,0,-2)\), and \((1,2,0)\). The result above matches the printed answer up to ordering/sign of eigenvectors.

### Notebook mismatch

The notebook briefly lists the roots as \(8,6,2\) and starts a \(\lambda=6\) case. But its own characteristic polynomial factors as \(-(\lambda-8)(\lambda-2)^2\). Therefore \(6\) is not an eigenvalue; the correct eigenvalues are \(8,2,2\).

### Final answer

\(\lambda=8:[2,-1,1]^T;\quad \lambda=2:\operatorname{span}\{[1,2,0]^T,[1,0,-2]^T\}\).

## Example 5 — Find the eigenvalues and eigenvectors

\[A=\begin{bmatrix}-2&2&-3\\2&1&-6\\-1&2&0\end{bmatrix}.\]

### Textbook match check

Checked against the supplied Grewal Unit II worked examples and in-scope textbook questions. No exact match was found. Problems 2.9 Q3(d) differs in entry (3,2), so it is not counted as a textbook match.

### Complete worked solution

Priyanka begins with \(|A-\lambda I|=0\). The photographed notebook stops during the determinant setup, so the calculation below completes the actual class matrix step by step.
\[|A-\lambda I|=\begin{vmatrix}-2-\lambda&2&-3\\2&1-\lambda&-6\\-1&2&-\lambda\end{vmatrix}=0.\]
Expand along the first row:
\[(-2-\lambda)\begin{vmatrix}1-\lambda&-6\\2&-\lambda\end{vmatrix}-2\begin{vmatrix}2&-6\\-1&-\lambda\end{vmatrix}-3\begin{vmatrix}2&1-\lambda\\-1&2\end{vmatrix}=0.\]
Evaluate the minors:
\[(1-\lambda)(-\lambda)+12=\lambda^2-\lambda+12,\]
\[2(-\lambda)-6=-2\lambda-6,\]
\[4+(1-\lambda)=5-\lambda.\]
Therefore
\[(-2-\lambda)(\lambda^2-\lambda+12)-2(-2\lambda-6)-3(5-\lambda)=0,\]
\[-\lambda^3-\lambda^2-3\lambda-27=0,\]
\[-(\lambda+3)(\lambda^2-2\lambda+9)=0.\]
Hence one eigenvalue is
\[\lambda_1=-3.\]
For the quadratic factor,
\[\lambda^2-2\lambda+9=0\Rightarrow\lambda=\dfrac{2\pm\sqrt{4-36}}{2}=1\pm2\sqrt2\,i.\]
Thus
\[\boxed{\lambda=-3,\quad1+2\sqrt2\,i,\quad1-2\sqrt2\,i}.\]
For \(\lambda=-3\), solve \((A+3I)X=0\):
\[\begin{bmatrix}1&2&-3\\2&4&-6\\-1&2&3\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix}=0.\]
Use \(R_2\to R_2-2R_1\) and \(R_3\to R_3+R_1\):
\[\begin{bmatrix}1&2&-3\\0&0&0\\0&4&0\end{bmatrix}.\]
The third row gives \(y=0\). The first row then gives \(x-3z=0\Rightarrow x=3z\). Taking \(z=k\):
\[X_1=k\begin{bmatrix}3\\0\\1\end{bmatrix}.\]
Now let \(\mu\) denote either complex eigenvalue, so \(\mu^2-2\mu+9=0\). Solve \((A-\mu I)X=0\):
\[\begin{cases}(-2-\mu)x+2y-3z=0,\\2x+(1-\mu)y-6z=0,\\-x+2y-\mu z=0.\end{cases}\]
From the third equation,
\[x=2y-\mu z.\]
Substitute this into the second equation:
\[2(2y-\mu z)+(1-\mu)y-6z=0,\]
\[(5-\mu)y-(2\mu+6)z=0.\]
Using \(\mu^2-2\mu+9=0\), we have \((5-\mu)(2\mu)=3(2\mu+6)\). Hence
\[y=\dfrac{2\mu}{3}z.\]
Then
\[x=2\left(\dfrac{2\mu}{3}z\right)-\mu z=\dfrac{\mu}{3}z.\]
Take \(z=3k\). Then an eigenvector for either complex root \(\mu\) is
\[X=k\begin{bmatrix}\mu\\2\mu\\3\end{bmatrix}.\]
Therefore, for \(\lambda=1+2\sqrt2\,i\):
\[X_2=k\begin{bmatrix}1+2\sqrt2\,i\\2+4\sqrt2\,i\\3\end{bmatrix},\]
and for \(\lambda=1-2\sqrt2\,i\):
\[X_3=k\begin{bmatrix}1-2\sqrt2\,i\\2-4\sqrt2\,i\\3\end{bmatrix}.\]
Each displayed vector was checked by direct multiplication with the class matrix.

### Notebook mismatch

In the handwritten determinant setup, the top-left entry is written as \(-2\). In \(A-\lambda I\), \(\lambda\) must be subtracted from every diagonal entry, so the correct entry is \(-2-\lambda\). The photographed notes stop during this setup; the remaining working in this dropdown is an independent PankusDesk completion of the class question.

### Final answer

\(\lambda=-3\) with eigenvector \([3,0,1]^T\); \(\lambda=1\pm2\sqrt2\,i\) with eigenvectors \([\lambda,2\lambda,3]^T\), up to non-zero scalar multiples.
