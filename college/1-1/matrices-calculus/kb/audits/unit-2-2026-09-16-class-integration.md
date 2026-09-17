# Unit II — 16 September 2026 class-note integration audit

## Source workspace

`re.zip` supplied in the 17 September 2026 task. This workspace already contains the cumulative 9, 11 and 15 September Unit II class-note work and is treated as code source of truth.

## Source material

Six chat-supplied notebook photographs: `Mac-class-unit2 - 20.jpg` through `Mac-class-unit2 - 25.jpg`. SHA-256 hashes are stored in `kb/data/source-manifest.json`.

## Integrated material

1. Show that `[[0,1],[0,0]]` is not diagonalizable — complete AM/GM proof.
2. Diagonalize `[[5,-4,4],[12,-11,12],[4,-4,5]]` — full characteristic polynomial, eigenspaces, modal matrix, inverse and diagonal form.
3. Diagonalize `[[1,0,0],[0,3,-1],[0,-1,3]]` and hence find `A^4` — full eigenvalue/eigenvector calculation, `P`, `P^{-1}`, `D`, and `PD^4P^{-1}` multiplication.

All three are clickable dropdown questions in the generic class-note renderer.

## Textbook comparison

- Q1: no exact match found in the current Unit II worked examples or in-scope question bank.
- Q2: no exact match found.
- Q3: the identical matrix occurs in Grewal Problems 2.10 Q9(a), but Q9(a) asks only for eigenvalues/eigenvectors/modal matrix; the class problem extends this to diagonalization and `A^4`. Per the established rule, partial overlap is **not** counted as an exact match. The class problem is independently solved in full.

## Verified correction

The notebook's lambda=1 work in Q3 briefly suggests a nonzero vector in the final two components. Solving both equations gives `x2=x3=0`; the verified eigenvector is `[1,0,0]^T`. This is displayed as a notebook mismatch rather than silently changed.

## Files added/modified

Added:
- `kb/class-log/2026-09-16/entry.json`
- `kb/class-log/2026-09-16/raw.md`
- `kb/audits/unit-2-2026-09-16-class-integration.md`

Modified:
- `kb/data/source-manifest.json`
- `college/1-1/data/class-log.json`

## Verification actually performed

- `python college/1-1/matrices-calculus/kb/tools/verify_kb.py` → **MAC KB VERIFY: PASS**.
- `python scripts/tools/verify_college.py` → **COLLEGE VERIFY: PASS**.
- Q2 independently checked: `P^{-1}AP = diag(1,1,-3)` and the stored `P^{-1}` is exact.
- Q3 independently checked: `P^{-1}AP = diag(1,2,4)` and direct matrix powering gives `A^4 = [[1,0,0],[0,136,-120],[0,-120,136]]`.
- JSON files parse successfully through the verifiers.
- No NRS redraw was needed: the source pages contain mathematics/text only and the class-note renderer presents them semantically in HTML/MathJax.
- A deployed-browser visual check was not performed; this package is a local delta awaiting sync/deploy.

## Follow-up cross-reference update — 17 September 2026

Q3 now includes a visible textbook cross-reference aside linking directly to **Problems 2.10 Q9(a)** at `unit-2-questions.html#question-u2-p210-09-a`. The aside explicitly states that only the matrix/shared eigenvalue-eigenvector work overlaps; the class problem continues to diagonalization and `A^4`, so the class solution remains complete and independent.

## Textbook cross-reference path fix — 17 September 2026

The class-note textbook links were stored as `unit-2-questions.html#...`. Because the site uses a root `<base>` element, that resolves outside the MAC subject directory.

The affected Unit II class-note links now use `college/1-1/matrices-calculus/unit-2-questions.html#...`, which resolves correctly with both the localhost `/` base and the GitHub Pages `/Pankusdesk/` base. The 16 September Q3 link targets `#question-u2-p210-09-a`. The same defective path form was corrected in the existing 9 September and 15 September textbook cross-references for consistency.
