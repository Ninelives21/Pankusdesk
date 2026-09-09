# MAC Unit II — 9 September 2026 class-note integration

## Source

- `mac_9thSept.zip`
- SHA-256: `c905c714238de316ea1a4f1f2c443614af1ddf7b1af89c1fef219e56407fc4d0`
- Seven notebook photographs: `Mac-class-unit2 - 5.jpg` through `Mac-class-unit2 - 11.jpg`

The newly uploaded `mac_8thSept.zip` was also checked. Its four JPGs are byte-for-byte identical to the four photographs already integrated on 8 September, so no duplicate 8 September entry was created.

## Integrated content

- Example with eigenvalues `0, 3, 15` and corresponding eigenvectors found by row reduction
- Example with a repeated eigenvalue and a two-dimensional eigenspace
- Start of a third eigenvalue/eigenvector example; retained as incomplete because the supplied notebook stops at the determinant setup

## Independent verification

For `A=[[8,-6,2],[-6,7,-4],[2,-4,3]]`, the characteristic polynomial is `lambda(lambda-3)(lambda-15)`. Verified eigenvectors are proportional to `[1,2,2]^T`, `[2,1,-2]^T`, and `[2,-2,1]^T`.

For `A=[[6,-2,2],[-2,3,-1],[2,-1,3]]`, the notebook polynomial is correct but the handwritten root list `8,6,2` is not. The polynomial factors as `(lambda-8)(lambda-2)^2`, so the verified roots are `8,2,2`. The eigenspace for `lambda=2` has dimension 2 and is spanned by `[-1,0,2]^T` and `[1,2,0]^T`.

The final photographed problem is incomplete. Its handwritten determinant also omits `-lambda` from the top-left diagonal term. The student-facing entry shows the corrected determinant setup but does not invent a continuation.

## Publication

- Added the dated 9 September source and entry to the Unit II Class Notes page via the existing shared renderer.
- Added the date to the semester class-log index.
- Unit II textbook theory remains untouched.
- Raw notebook images remain outside website assets.
