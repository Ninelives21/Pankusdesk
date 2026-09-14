# BEE Class Log — 11 September 2026

## Assessment questions

### Question 1

Explain the role of electrical energy in modern life and various engineering branches.

A short answer is integrated in the class-note entry. It covers domestic use, industrial use and the importance of electrical energy across electrical, mechanical, civil, electronics, computer/IT, chemical, biomedical and agricultural engineering applications.

### Question 2

Find the current flowing through the 2-ohm resistor connected between the points \(a\) and \(b\) using Thevenin’s theorem.

This question matches prescribed-textbook **Example 1.9.3**. The class-note entry retains the canonical textbook link and shows the requested solution as six separate NRS step images so each step fits the page cleanly. Final verified result:

\[
I=47.8\,\text{mA}
\]

flowing from \(b\) to \(a\). If current is referenced from \(a\) to \(b\), then \(I_{ab}=-47.8\,\text{mA}\).

### Question 3

Find the current and power supplied by the source. Apply mesh analysis.

Priyanka’s notebook appears to show the upper-left bridge resistor as \(1\,k\Omega\). A matching published problem confirms that the intended value is \(1\,\Omega\): P. Ramana, M. Suryakalavathi and G. T. Chandra Sekhar, *Basic Electrical Engineering*, S. Chand, 2018, Chapter 1, Solved Problem 23, p. 41; solution p. 42.

Using \(1\,\Omega\), the mesh equations are

\[
8I_1-I_2-4I_3=4,
\]

\[
-I_1+8I_2-5I_3=0,
\]

\[
-4I_1-5I_2+15I_3=0.
\]

Solving,

\[
I_1=\frac{380}{577}\approx0.66\,\text{A},\qquad
I_2=\frac{140}{577}\approx0.24\,\text{A},\qquad
I_3=\frac{148}{577}\approx0.26\,\text{A}.
\]

Hence

\[
I_{source}=I_1\approx0.66\,\text{A}
\]

and

\[
P_{supplied}=4I_1\approx2.64\,\text{W}.
\]
