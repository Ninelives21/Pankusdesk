# MAC Class Log — 2 September 2026

Source: `mac_2ndSept.zip` · notebook pp. 19–21.

## Page 19

**7. Test for the consistency and solve if it is consistent**

\[
5x+3y+7z=4,\qquad 3x+26y+2z=9,\qquad 7x+2y+10z=5.
\]

The notebook forms the augmented matrix, applies \(R_2\to5R_2-3R_1\) and \(R_3\to5R_3-7R_1\), and reaches a zero third row. It records the system as **consistent**. The page begins back-substitution but stops before a full parameter solution is written.

## Page 20

Homogeneous system:

\[
-x_1+x_2=0,\qquad -x_1-2x_2+3x_3=0,\qquad 2x_1+x_2-3x_3=0.
\]

The notebook row-reduces to two independent rows, writes “∞ solutions”, and obtains \(x_1=x_2=x_3=k\).

## Page 21

Four-variable system:

\[
\begin{aligned}
2u_1+u_2+2u_3+u_4&=6\\
6u_1-6u_2+6u_3+12u_4&=36\\
4u_1+3u_2+3u_3-3u_4&=-1\\
2u_1+2u_2-u_3+u_4&=10.
\end{aligned}
\]

The page contains an augmented-matrix reduction with several overwritten entries. The later handwritten rows contain last-column values 15 and 36. The supplied page does not show a reliable final solution consistent with the original equations.

## Verification notes (not notebook transcription)

- Page 19: \(\rho(A)=\rho(A|B)=2<3\); one parameterisation is \((x,y,z)=(5-16k,k,11k-3)\).
- Page 20: the displayed second row is the negative of the row produced by the annotated operation; this does not change the solution space. The family \(X=k(1,1,1)^T\) is correct.
- Page 21: independent reduction gives \((u_1,u_2,u_3,u_4)=(2,1,-1,3)\).
