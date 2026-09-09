# MAC Unit II — 9 September 2026 class-note integration

## Source

- `mac_9thSept.zip`
- SHA-256: `c905c714238de316ea1a4f1f2c443614af1ddf7b1af89c1fef219e56407fc4d0`
- Seven notebook photographs: `Mac-class-unit2 - 5.jpg` through `Mac-class-unit2 - 11.jpg`

The top of notebook page 5 is the tail end of the 8 September property example. The dated 9 September work begins at the circled Example 3, so the 9 September class contains three questions: Examples 3, 4 and 5.

## Dropdown refactor

All three 9 September class questions are now complete dropdowns on the Unit II Priyanka's Class Notes page. The complete question remains visible in the dropdown summary and the full verified solution is inside.

- Example 3: matrix `[[8,-6,2],[-6,7,-4],[2,-4,3]]`
- Example 4: matrix `[[6,-2,2],[-2,3,-1],[2,-1,3]]`
- Example 5: matrix `[[-2,2,-3],[2,1,-6],[-1,2,0]]`

## Independent verification

### Example 3

The characteristic polynomial is `lambda(lambda-3)(lambda-15)`. The verified eigenpairs are:

- `lambda=0`, eigenspace spanned by `[1,2,2]^T`
- `lambda=3`, eigenspace spanned by `[2,1,-2]^T`
- `lambda=15`, eigenspace spanned by `[2,-2,1]^T`

The handwritten final summary appears to omit the minus sign on the third component of the `lambda=3` eigenvector. The dropdown flags this rather than silently copying it.

### Example 4

The characteristic polynomial factors as `-(lambda-8)(lambda-2)^2`. The notebook's brief root list `8,6,2` is therefore incorrect; `6` is not an eigenvalue.

- `lambda=8`, eigenspace spanned by `[2,-1,1]^T`
- `lambda=2` with algebraic multiplicity 2, eigenspace spanned by `[1,2,0]^T` and `[-1,0,2]^T`

The repeated eigenvalue therefore has two independent eigenvectors.

### Example 5

The notebook stops during the determinant setup and omits `-lambda` from the top-left diagonal term. The dropdown shows the corrected setup and explicitly labels the rest as an independent completion.

The verified characteristic polynomial is

`-(lambda+3)(lambda^2-2lambda+9)`.

Hence the eigenvalues are `-3` and `1 ± 2sqrt(2)i`.

- `lambda=-3`, eigenspace spanned by `[3,0,1]^T`
- for either complex eigenvalue `mu=1 ± 2sqrt(2)i`, an eigenvector is `[mu,2mu,3]^T`

All three eigenpairs were checked by direct multiplication.

## Publication

- Unit II textbook theory remains untouched.
- The 8 September class-note entry remains untouched and is not duplicated.
- No notebook photograph is copied into website assets.
- Existing three-resource Unit II navigation remains untouched.
