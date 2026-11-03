# MAC supplied-notes integration audit

## Scope and preserved content

The supplied material previously supported Worksheet & Solutions 1. This change integrates it into the canonical Text and separate Class Notes pages. Existing Units I–II textbook content, dated records, worksheet content and figures are preserved. Chemistry PR #24 and unrelated ED/PPS work are untouched.

| Source | Content and treatment |
|---|---|
| `ww_MAC_class_notes.zip` · 48 photos (26–73) | 4 Unit II supplement pages, 35 Unit III pages, 9 introductory Unit IV pages; transcribed into 15 undated lessons. |
| `01_MAC_01.zip` + `01_MAC_02.zip` · 55 photos (74–128) | Printed pp. 217–271, complete Chapter 5 source packet. R25 theory and Examples 5.1–5.34 / 5.46–5.59 imported; unrelated sections omitted. |
| `2_3-MAC.zip` · 19 photos (129–147) | Printed pp. 1357–1360 and 157–171. Unit III Examples 4.14–4.34 imported; curve appendix and Unit V area/volume formulas are partial references. |
| `mac_book_toc_index.zip` | Contents/index used to identify remaining sections; no invented textbook page citations. |
| `01_MAC.zip` | Initial Chapter 5 upload replaced by the complete two-part capture set above; not counted as additional unique pages. |
| `MAC WORK SHEET.pdf` | Existing audited worksheet retained unchanged. |

`mac-source-captures.json` accounts for all 122 unique note/chapter/appendix photo captures (the seven TOC/index photos have a separate supplemental archive record) with archive/file identities and SHA-256. Full photographs stay outside the public repository. `mac-ros-figures.json` records 14 unchanged crops with native coordinates and source/output hashes. Each lossless WebP was compared pixel-for-pixel with its original crop and visually inspected. No redraw, enhancement, recolouring or replacement of prior figures.

## Publication and source limits

- Units I–II retain their existing ready status. The new undated Unit II supplement is separate from the existing dated chronology.
- Units III–IV are draft. Unit III still lacks full introductory limit/continuity and full Cartesian/polar tracing pages. Unit IV has its theory source packet, but the complete exercise-bank release and final publication review remain pending.
- Unit V is draft/reference only: the supplied appendix has area/volume formulas, not a chapter treatment. All nine Unit V atoms remain source gaps.
- The source coverage ledger now has 30 theory-backed atoms and 13 full/partial source gaps. Coverage is not a claim that a unit is ready.
- The new book pages contain later exam references than the historical 36th-edition/2010 citation. The new packet’s exact edition is unconfirmed. Existing source records are preserved, and the new selected-question pages have their own source label.
- Notebook dates are absent or cropped (one ends `/10/26`). No dates were inferred from file order; no calendar entries were manufactured.

## Textbook/class matching and solutions

All new class questions were compared with the supplied worked examples and visible section-end sets. Matching is limited to those supplied pages, not a claim about unavailable chapters. Exact matches link to stable canonical textbook anchors; the new question bank contains six selected Unit III questions/parts and one Unit IV question to prevent duplicate solutions. The remaining section-end/chapter-end questions are not yet transcribed, and the pages explicitly say so. Near matches state the changed data/sign/condition. Additional class working is labelled PankusDesk verification.

Textbook Examples 4.14–4.34 (21) and 5.1–5.34 / 5.46–5.59 (48), plus the unnumbered path-limit illustration, have full visible prompts, worked dropdowns and bold final answers. Multipart examples use separate labelled solution panels. The record does not imply that all Chapter 5 examples are in R25: tangent planes, multivariable Taylor/error applications and Leibniz integral differentiation are omitted.

## Verified source discrepancies

These are visible amber notes in the study pages. Transcription errors caught during preparation were corrected against the photos; they are not misrepresented as source errors.

- **Example 4.31**: The final printed line on p. 170 drops the minus sign in the leading denominator term and reports +2/3. The denominator is −x³/2+O(x⁴), whereas the numerator is x³/3+O(x⁴). Their ratio is −2/3.
- **Example 4.16**: The printed example states 0<a<b<1 but then substitutes a=1, b=4/3. The proof only needs 0<a<b; with that condition both the inequality and the numerical deduction are valid.
- **Example 4.19**: The printed odd-order remainder uses cos(θx). An odd derivative of cos x is a signed sine, so with polynomial degree 2n the order-(2n+1) remainder is (−1)ⁿ⁺¹ x²ⁿ⁺¹ sin(θx)/(2n+1)!. The even-order remainder displayed here is an equivalent valid Taylor form.
- **Example 4.25**: The numerical-substitution line starts with 1.1 instead of x−1=0.1, although the next line uses 0.1 and obtains the correct 0.0953. The fourth-derivative value −6 is also labelled at 0 instead of at the expansion point 1. The calculation here evaluates all derivatives at 1 and substitutes h=0.1.
- **Example 5.7**: Some intermediate lines on pp. 221–222 repeat y² where the third numerator must be z², and a z-differentiation line uses b²+u instead of c²+u. The original constraint requires z²/(c²+u)² in v and 2z/(c²+u) in that derivative; the working here makes those corrections explicit.
- **Example 5.9**: One line on p. 224 prints ∂r/∂y=y/x. Differentiating r²=x²+y² while holding x constant gives ∂r/∂y=y/r. The subsequent displayed result uses the latter value.
- **Example 5.10**: The question and last printed line give −1/(x logₑ x). The preceding differentiation instead yields −1/[x(1+logₑ x)]. The step replacing logₑ e+logₑ x by logₑ x loses the 1. The verified result below is −1/[x logₑ(ex)], not the printed target.
- **Example 5.13**: The intermediate multiplied equations on p. 227 interchange some xx/xy/yy subscripts and put uₓ where uᵧ is required in the y-differentiated equation. Differentiating xuₓ+yuᵧ=nu gives the two equations shown here; their sum establishes the stated final theorem.
- **Example 5.14**: The question on p. 227 prints ∂/∂x outside the radial bracket, although its variables and the entire solution use r and t. The radial heat equation (the same as Example 5.4) requires ∂/∂r there. This working explicitly follows that radial version.
- **Example 5.20**: The printed simplification cancels 1−4t² without an absolute value. For the principal arcsine, the displayed positive derivative holds on |t|<1/2. The square-root identity gives a negative derivative on 1/2<|t|<1; the joining points require separate consideration.
- **Example 5.23**: The second identity’s right-hand bracket prints (∂u/∂v)² rather than (∂z/∂v)², and an intermediate chain-rule term labels ∂z/∂y as ∂x/∂y. The dependent variable throughout is z; squaring the two correct z-derivative equations gives the stated gradient-norm identity.
- **Example 5.24**: The final formula on p. 236 omits the overall minus sign present in the preceding quotient differentiation. Differentiating fₓ+fᵧ y′=0 again gives y″=−(fₓₓ fᵧ²−2fₓᵧ fₓ fᵧ+fᵧᵧ fₓ²)/fᵧ³, as shown here.
- **Example 5.26**: The printed question on p. 237 (and repeated line on p. 238) loses the factor 1/r² on the angular second derivative and prints a difference of Cartesian second derivatives. The preceding Example 5.25 and the worked derivation require vᵣᵣ+vᵣ/r+vθθ/r²=vₓₓ+vᵧᵧ. The working here follows that verified identity; some intermediate printed lines also omit mixed derivatives.
- **Example 5.27**: The question header on p. 238 prints y=eᵘ sin u, but the following coordinate line and working use y=eᵘ sin v. The identity here follows that latter transformation. Several intermediate derivative labels also interchange u and v. The correct coordinate derivatives are x_u=x, y_u=y, x_v=−y, y_v=x. The final identity printed in the question agrees with the working shown here.
- **Example 5.29**: The derivative list for part (i) prints yθ=−r cos θ, but differentiating y=r sin θ gives +r cos θ, as its following determinant uses. In the spherical determinant a yφ entry is printed with a minus sign; differentiating y=r sin θ sin φ gives +r sin θ cos φ. The matrices here use the derivatives of the stated coordinate maps.
- **Example 5.31**: The question prints x=r sin θ cos θ, while the intended spherical transformation (Example 5.29 and the subsequent first row) is x=r sin θ cos φ. The following derivative matrix also loses sin φ in yᵣ and gives the wrong sign for yφ. The solution here explicitly uses x=r sin θ cos φ, y=r sin θ sin φ, z=r cos θ, for which the Jacobian is r² sin θ.
- **Example 5.32**: An early line on p. 242 labels xᵣ=cos θ as xθ. The forward determinant on p. 243 then contains inverse-coordinate entries in its second row. The correct forward rows are (cos θ,−r sin θ) and (sin θ,r cos θ), giving r; the inverse determinant gives 1/r.
- **Example 5.34**: The intermediate assertion v=sin⁻¹(u) need not hold on the full stated square because v=sin⁻¹x+sin⁻¹y may leave the principal arcsine interval. The final relation u=sin v is valid and follows directly from the sine addition formula, which is the route used here.
- **Example 5.47**: The printed solution lists only (1/2,1/3) and (0,0). Both derivatives actually vanish on the entire two coordinate axes. It also prints D=1/14 at the nonzero point; direct substitution gives D=1/144. The isolated maximum value 1/432 is correct; the additional stationary-line classification is PankusDesk verification.
- **Example 5.52**: The question and initial constraint on pp. 259–260 give x²+y²+z²=4 (radius 2). The printed working later substitutes 1 instead of 4 and concludes 12 and 14, which are the distances for a radius-one sphere. For the question as printed, the correct distances are 11 and 15.
- **Example 5.57**: The printed rearrangement for z on p. 263 loses the minus sign: its multiplier equation gives z=−λ₁nc⁴/[2(1−c²u)], consistent with the x and y rearrangements. The common-sign expressions shown here yield the indicated stationary-value condition.
- **Example 5.58**: The first Lagrange-function display on p. 264 uses x²/y² where the stated ellipsoid requires x²/a². A later line prints 3V+2λ−1=0, but multiplication and addition of the derivative equations gives 3V+2λ=0; its following λ=−3V/2 is consistent with that corrected equation.
- **Example 5.59**: The printed candidate list uses z=±2 with the same sign notation as x=±2, but its derivative equations require z=−x. The stationary points are (2,4,−2) and (−2,−4,2). They give the book’s final distances √6 and 3√6.
- **Class · Concavity and inflection**: The concave-down line writes y″=0. The required sign condition is y″<0; the unchanged source sketch illustrates concave downwards. The earlier “change of direction” wording for inflection is incomplete: the relevant change is concavity.
- **Class · Differentiate the preceding series**: The initial prompt has +x³/48. Differentiating the preceding series gives −x³/48, as the final handwritten working and Problems 4.5 Q19 both show. The linked canonical solution follows that verified negative sign.
- **Class · Question and working use different denominators**: The header writes x²+y², whereas the solution repeatedly uses x²+y⁴ and the curved path x=my². These are different functions with different answers. Both have been kept explicitly; the squeeze argument for the written question is PankusDesk verification.
- **Class · Equality of mixed partials**: The notebook states this for “any continuous function”. Continuity of the function alone is insufficient; the usual sufficient hypothesis concerns its mixed second partial derivatives.
- **Class · Square root and reciprocal square root**: The theorem list writes g′(x)=0, but the quotient formulation requires g′(x)≠0 on the open interval. The same page’s verification below correctly checks that g′ is nonzero. The statement here uses the required nonzero condition.
- **Class · Logarithm and reciprocal**: The prompt asks for f(x)=ln x and f′(x)=1/x. Its working substitutes endpoint differences of f′ and f″ instead, so it is checking a different pair of functions. For the stated pair the canonical textbook solution uses (ln e−ln 1)/(1/e−1)=−e/(e−1), giving c=e/(e−1).
- **Class · Logarithmic inequality**: One intermediate handwritten line uses 1/a<1/c<1/b after a<c<b. For positive numbers reciprocals reverse order: 1/b<1/c<1/a. The notebook’s final logarithmic bounds agree with the corrected order used in the canonical solution.
- **Class · Exercise: bound an inverse cosine**: The handwritten upper comparison uses an equality sign. LMVT gives a strict inequality because the intermediate c is strictly between 1/2 and 3/5; the two endpoint bounds are not attained.

## Additional photographs needed

| Needed | Why |
|---|---|
| Single-variable limits/continuity definitions and properties | The supplied Chapter 4 sequence starts at p. 157 with mean-value theorems. Please include the relevant introductory section and its opening heading. |
| Printed p. 172 | Example 4.35 starts at the bottom of p. 171; its continuation is not supplied, so it is not published as a solved example. |
| Full Cartesian and polar curve-tracing textbook section | The supplied p. 1357 is an appendix checklist, not the full tracing chapter or its worked curves. Chapter 6 is titled Integral Calculus and Its Curve Tracing (pp. 272–314). Its curve-tracing subsection opening will establish the exact needed range; the supplied index points only to the appendix. |
| Unit V multiple-integral chapter (Chapter 7 begins p. 315) | Need double/triple integrals, order changes, coordinate substitutions, areas and volumes. The chapter runs to p. 364 but also includes out-of-scope Beta/Gamma material; the section contents/opening will delimit the required pages. |
| Book title/copyright page | Confirm which edition the new Chapter 4/5 packet uses. |

No further replacement screenshots are required for the 14 ROS drawings already integrated. No notebook drawing was supplied for the astroid/catenary prompts, so no substitute figure was generated.

## Validation

- All three required validators PASS: `verify_college.py`, BEE `verify_kb.py`, MAC `verify_kb.py`. JavaScript syntax and Python compilation checks PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/check_imported_calculus.py`: 88 independent SymPy/numerical checks of series, derivatives, limits, Hessians, coordinate Jacobians and multiplier conditions. This checks algebra, not source completeness.
- Source-by-source checks include the notebook rational-limit denominators/signs, CMVT endpoint substitutions and logistic cubic sign; textbook stationary axes, arcsine branch and implicit logarithm discrepancy.
- Strict JSON Schema comparison: new subject, question-bank and undated entries pass; the topic corpus retains the same 32 pre-existing schema violations (missing optional-looking fields in older records and a historical string page range). New/changed Unit III–V records add no schema errors. These legacy records were not normalized.
- Local Chromium PASS at 1440 px and 390 px on eight affected pages: Text III/IV/V, Class Notes II/III/IV and selected Questions III/IV. Zero MathJax errors or document overflow; all 14 ROS images decode. Canonical class-to-textbook links open the intended solution; textbook example and lesson deep links and the `/Pankusdesk/` base prefix pass. Existing Unit I/II Text and Unit I Class Notes render. Desktop/phone screenshots inspected. Hosted preview browser access is not counted as a local browser test.
- Vercel static build PASS: 285,451,983 output bytes, below the existing 350 MiB budget.
