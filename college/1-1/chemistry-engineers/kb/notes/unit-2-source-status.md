# Chemistry Unit II — Source Pipeline Status

## Current checkpoint

**Stage 0 — Mechanical source inventory: COMPLETE**

No Chemistry theory, examples, questions, figures, or answers were transcribed or interpreted in this stage. Stage 0 only establishes a resumable source ledger.

## Locked inputs

- Workspace source: `redo.zip`
  - SHA-256: `69e1e138d2d436c85552f3d7ac682d11df3ac24efd9092f65ba0920f88ec7446`
- Textbook photo archive: `chem_unit2.zip`
  - SHA-256: `7c0c9e0fac7b8e2e801e4786a1267cbb74e2a165e8bcfb7226e3cdb986174535`
- Prescribed textbook identity used for the ledger: *Engineering Chemistry*, P. C. Jain and M. Jain, Dhanpat Rai and Company, 2010.
- Photo sequence: `Chem_unit2 - 1.jpg` through `Chem_unit2 - 84.jpg`.
- Mechanical textbook mapping: sequence 1 → p. 279, …, sequence 84 → p. 362.
- Expected/actual textbook pages: 84 / 84.
- Missing sequence numbers: none.
- Duplicate sequence numbers: none.
- All 84 extracted JPEGs opened successfully for mechanical metadata inspection.

## Persistent checkpoint files

- `kb/data/unit-2-source-index.json` — immutable mechanical inventory for this supplied source set: source/archive hashes, page mapping, per-image hashes, dimensions and file sizes.
- `kb/data/unit-2-source-lock.json` — resumable Stage 1 ledger. Each micro-batch has its own status and empty `entries` array until academically inspected.
- `kb/notes/unit-2-source-status.md` — this human-readable resume point.

## Stage 1 micro-batches

| Batch | Textbook pages | Status |
|---|---:|---|
| U2-SL-01 | 279–288 | pending |
| U2-SL-02 | 289–298 | pending |
| U2-SL-03 | 299–308 | pending |
| U2-SL-04 | 309–318 | pending |
| U2-SL-05 | 319–328 | pending |
| U2-SL-06 | 329–338 | pending |
| U2-SL-07 | 339–348 | pending |
| U2-SL-08 | 349–358 | pending |
| U2-SL-09 | 359–362 | pending |

## Resume rule

On the next run, read this status file plus `unit-2-source-index.json` and `unit-2-source-lock.json`. Process **only the first pending batch**. Do not reread or reinterpret completed batches. After completing a batch, write its extracted source entries into the ledger and update the counters/status before stopping.

No student-facing Unit II page content should be generated until the source-lock stage is complete and the R25 mapping has been made from the locked entries.
