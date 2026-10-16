# Unit III Short Notes — Swinburne notation alignment

Date: 2026-10-16

## Scope
Aligned the Swinburne's Test note text with the accepted NRS circuit redraw at:
`college/1-1/basic-electrical-engineering/assets/pankusdesk/u3/short-notes/swinburne-test-circuit.png`

## Changes
- Explained the drawing notation explicitly:
  - `I_0` = no-load line current measured by A1.
  - `I_sh` = shunt-field current measured by A2.
  - `I_a` = armature current.
- Bridged drawing notation to calculation notation:
  - `I_0 ≡ I_L0`
  - `I_sh ≡ I_f`
  - at no load `I_a ≡ I_a0`
- Added the current-split relation `I_0 = I_a + I_sh` before the calculation form `I_a0 = I_L0 - I_f`.
- Updated diagram title, caption, alt text and teaching note to match the accepted redraw.
- Removed search-query / AI-generation / placeholder metadata from the active diagram entry now that the real redraw is available.
- Preserved backend source_refs and all subsequent loss/efficiency calculations.

## Verification
- `short-notes.json` parsed successfully.
- `node --check scripts/new/unit-short-notes.js` passed.
- BEE KB verifier passed: `BEE KB VERIFY: PASS`.
- The verifier emitted an unrelated artifact_tool spreadsheet warm-up traceback on stderr, but exited 0 and completed the BEE KB verification successfully.
