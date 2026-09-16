# MAC Unit II — 11 September 2026 class-note integration

## Source

Four notebook photographs supplied directly in chat:

- `Mac-class-unit2 - 12.jpg` — SHA-256 `ee3a602138178cec058926e51c5784bfc5bf4eec686f3dd17a5c34c1995216bc`
- `Mac-class-unit2 - 13.jpg` — SHA-256 `d8ef1334b7a831ee2fe0e591bc583b6b5a09d000548b256eb680a2594161e67a`
- `Mac-class-unit2 - 14.jpg` — SHA-256 `ab66c0dd233edd0ce63e2a19523d293a023b9a0fd744bd0b51a52c5b80b202f1`
- `Mac-class-unit2 - 15.jpg` — SHA-256 `3c79fd8d93679ded25d6793fd66efe0b635cf5c052b2edb9bb765f374bcb4fa8`

## Textbook-match check

Before retaining independent class solutions, both 11 September questions were compared against:

- the published Unit II Grewal worked-example set in `topics.json`; and
- the in-scope Problems 2.8, 2.9, 2.10 and 2.12 entries in `textbook-questions.json`.

No exact match was found for either matrix. Therefore no textbook-match aside/link is rendered and the class solutions remain separate.

## Class material integrated

### Example 6

\[
A=\begin{bmatrix}5&-2&0\\-2&6&2\\0&2&7\end{bmatrix}
\]

The notebook finds characteristic roots `3, 6, 9` and then obtains corresponding eigenvectors by row reduction. The cleaned study copy preserves the notebook row-operation route while removing crossed-out arithmetic. Verified eigenvectors are proportional to:

- `lambda=3`: `[-2,-2,1]^T`
- `lambda=6`: `[2,-1,2]^T`
- `lambda=9`: `[-1,2,2]^T`

Each was checked by direct multiplication.

### Second class question

\[
A=\begin{bmatrix}-3&-7&-5\\2&4&3\\1&2&2\end{bmatrix}
\]

The cleaned determinant expansion gives

\[
-(\lambda-1)^3=0,
\]

so the eigenvalue is `1` with algebraic multiplicity 3. The class row reduction yields the eigenspace spanned by `[-3,1,1]^T`. This was checked directly.

## Cleanup policy

- No raw notebook image is copied into website assets.
- Crossed-out or overwritten arithmetic is not reproduced as clutter when the intended calculation is unambiguous.
- The class matrices, roots, row-operation method and resulting vectors are kept faithful to the notes.
- No additional theory is inserted into the textbook Text page.
- No textbook-match aside is shown because neither problem is an exact textbook match.

## Calendar

Added the MAC Unit II 11 September entry to `college/1-1/data/class-log.json`, linking directly to `unit-2-class-notes.html#2026-09-11`.
