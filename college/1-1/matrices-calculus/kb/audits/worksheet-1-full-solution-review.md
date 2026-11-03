# Worksheet & Solutions 1 — complete independent review

This review supersedes the earlier selective-check description in PR #25. All **272 numbered entries** were reviewed against the supplied, unchanged 15-page college PDF: Unit I 44, Unit II 24, Unit III 52, Unit IV 67, Unit V 85. The source has no supplied answer key. These remain PankusDesk-authored solutions, not college-approved answers.

The per-question evidence is in `worksheet-1-solution-audit.json`: each entry records the source pages, review status, independent mathematical method, corrections/qualifications, and a hash of the reviewed question and displayed solution. `verify_mac_worksheet.py` checks complete evidence coverage and those hashes; this integrity check is not itself a proof of mathematical correctness.

## Review procedure and evidence

Each unit was independently reviewed from the PDF rather than by rerunning the original answer-generation program. The review considered source transcription, mathematical correctness, complete requested subparts, reproducible intermediate working, domain and theorem hypotheses, local versus global extrema, all parameter cases and singularities. Explanations and conditional source interpretations were reviewed analytically as well as by symbolic checks.

- **Unit I, 44/44:** elementary-matrix certificates for row operations; exact minors/ranks and exceptional parameter cases; both inverse products; substitution of complete solution families; exact Gauss–Seidel updates, diagonal dominance and residual/change stopping checks. 105 independent assertions.
- **Unit II, 24/24:** independent source matrix/polynomial transcription; direct determinants, eigenspaces and multiplicities; AP=PD, inverse products and direct powers; polynomial quotient/remainder identities and direct matrix evaluation; orthonormal quadratic-form reductions and inertia. All exact checks passed.
- **Unit III, 52/52:** source intervals and expressions; every mean-value hypothesis and real-domain restriction; explicit derivatives and sequence counterexamples; Taylor coefficients and numerical remainder; analytical Cartesian and polar traces, tangents, asymptotes and stationary points. 98 recorded independent checks/review grounds.
- **Unit IV, 67/67:** source/domain review for every entry; direct derivatives/Jacobians and dependence relations; stationary equations, Hessian tests and degenerate cases; constrained stationary candidates and global certificates; Euler identities on their differentiable domains. 170 symbolic assertions plus per-entry analytical review.
- **Unit V, 85/85:** source bounds/differentials compared visually; independently evaluated iterated integrals and alternate-order/substitution checks; radial/angular Jacobians, geometric area/volume checks, crossed bounds and improper convergence. The first 37 entries have 40 exact equality checks; all remaining 48 have separate exact or analytical records, including conditional and divergent cases.

## Errors corrected in the earlier draft

- **Unit I · Short Q7:** the displayed determinant was −x(x−3)², but the answer incorrectly listed 1,2,3. Rank 2 occurs at **x=0 or x=3**. Nonzero minors establish the rank at both values. The source's k/x parameter-name mismatch is still labelled.
- **Unit III · Rolle Q3:** the source interval starts at **positive π/4**, not negative π/4. The prompt, endpoint values and derivative discussion are corrected. Rolle remains inapplicable.
- **Unit III · Rolle Q9:** the claimed explicit interior root 1+1/√2 was wrong. The root is **(1+√5)/2**. The original existence argument was valid.
- **Unit III · LMVT Q3:** restored a corrupted absolute-value inequality and supplied explicit sequences demonstrating nondifferentiability at zero.
- **Unit IV · Short Q9:** corrected an overbroad saddle definition that would also include ordinary nonstationary points.
- **Unit V · Cartesian Area Q3:** under the explicitly proposed line 2x−3y+4=0, the earlier area was too large by a factor of two. The correct area is **(9a²−8a)^(3/2)/(3a)** for a>8/9. The source's missing equals sign remains labelled.

Working was also expanded where a correct answer lacked enough steps: specific normal-form column operations and parameter cases, all multi-part matrix calculations, curve-trace details, the requested Lagrange method and global optimality certificates, and successive integral antiderivatives/region bounds. The duplicate curve question retains a complete answer, not just a pointer.

## Source limitations remain explicit

No official correction is presumed for missing operators or bounds. In particular: Unit II Long Q3/Q4 lack visible polynomial operators before the terms interpreted as +8A⁶/+15A⁶; Unit I Gauss–Seidel Q3 has a malformed chain; Unit III Rolle Q10 lacks an operator; Unit IV has an undefined evaluation point, missing piecewise value, sign-domain omissions and a false mixed-derivative claim; Unit V has incompatible differential orders, ambiguous region wording, a missing bottom bound and divergent cases. The answers distinguish literal validity from a labelled conditional interpretation. They must not be read as an invented college answer key.

Curve traces are analytical. No new drawings, private notebook photographs or textbook scans were added. Canonical topic publication states, class notes and existing figures remain unchanged.

## Navigation revision

The MAC index card is **Worksheet & Solutions 1** with no WS 1 badge. It opens this worksheet directly. The former horizontal section-link block is now the left **Contents** navigation, grouped under Units I–V; the WS 1 selector is removed. Contents collapses on phones. Existing question/group anchors are preserved. Future worksheets can receive separate index cards and registry entries.

Before merging, use the refreshed PR checklist to inspect desktop and phone navigation, the corrected answers, amber question-number-only styling and source-PDF link. Agent browser checks and CI results are reported separately from the user's unchecked acceptance items.
