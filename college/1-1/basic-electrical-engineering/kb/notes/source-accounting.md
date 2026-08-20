# Source Accounting Audit

## Required corpus

| Source | Count | Status |
|---|---:|---|
| Prescribed book Unit-I PNG capture | 65 | PASS |
| Prescribed book Unit-II PNG capture | 57 | PASS |
| Prescribed book Unit-III PNG capture | 56 | PASS |
| Prescribed book Unit-IV PNG capture | 15 | PASS |
| Prescribed book Unit-V PNG capture | 21 | PASS |
| **Book captures total** | **214** | **PASS** |
| Unit-I lecture transcripts | 27 | PASS |
| Unit-II lecture transcripts | 8 | PASS |
| **Lecture transcripts total** | **35** | **PASS** |
| Extra Dr. G. Ramesh PDF | 97 PDF pages | PASS |
| Official VNR R25 specification | supplied | PASS |
| Textbook p.243 UPS | supplied; also present in Unit-V capture | PASS |
| Approved gap package | supplied | PASS |

### Explicit guardrails
- Unit-II transcript numbers supplied are `01,02,03,04,05,06,07,09`. **08 does not exist in the supplied source set.**
- Page 200 has two captures because it straddles Unit IV and Unit V; this is intentional, not a duplicate-source error.
- The standalone `243.png` duplicates the Unit-V p.243 capture and is retained as corroborating capture, not counted as a new textbook page.
- Raw textbook PNGs are **not copied into this public workspace**. `data/book-index.json` proves every captured image is accounted for.

## Hashes
See `data/source-manifest.json`. The archive/file SHA-256 values bind this KB build to the exact inputs used.
