# Reference Drawings — source and ROS audit

## Source inventory

The supplied `drawings_converted_to_pdf.zip` contains **26 single-page PDFs**. The intake excludes only macOS metadata (`__MACOSX`, AppleDouble `._*` files and `.DS_Store`); no PDF is skipped. Original PDF filenames and bytes are preserved under `../notes/reference-drawings/`.

Every PDF page is one registered drawing sheet/composite. Multiple constructions and related orthographic views on a sheet remain together, including borders, dimensions, annotations and title blocks. Archive order establishes the initial stable IDs `ed-ref-001-p001-v01` through `ed-ref-026-p001-v01`. No earlier register existed; the [initial register](reference-drawings-ros-register.md) freezes these identities. Similar filenames, dated variants and overlapping material remain separate. Dates in navigation identify filenames, not inferred class-log dates. No syllabus unit or publication state is invented.

The source archive SHA-256 is recorded in `../notes/reference-drawings.json`; each PDF hash and output hash is recorded in the [manifest](reference-drawings-ros-manifest.json).

## ROS processing

The PDFs contain native vector paths and no embedded raster pictures or extractable text. Each complete page is directly rendered at **300 dpi**, then encoded as **lossless WebP** without cropping, resizing, sharpening, recolouring, OCR reconstruction, watermark removal, diagram repair or redraw. Rendering vector content at this resolution is not enlargement of a low-resolution bitmap.

All 26 WebPs decode and their RGB pixels equal the corresponding complete-page PDF render exactly. Original PDFs are available on each drawing section for unlimited vector zoom. A separate full-size WebP link is supplied by the existing shared source-notes renderer. Production drawings use `PankuStudyUI.renderFigure()` and the existing responsive notes layout.

The package `../notes/reference-drawings-ros.zip` contains individually named WebPs, all 26 unmodified original PDFs, register, manifest, audit and two review contact sheets. ZIP integrity is tested; names reconcile with the register without missing, duplicate or unexpected WebPs. [Contact sheet 1](reference-drawings-contact-1.jpg) and [contact sheet 2](reference-drawings-contact-2.jpg) are reduced review previews, never production assets.

## Source limitations and naming

- `pentagon & heptagon.pdf` visibly contains ellipse constructions (its title block says “ELLIPSE BY DIFFERENT METHODS”). Navigation therefore reads “Ellipse — different construction methods”; the original filename and content remain unchanged. This is a filename discrepancy, not a mathematical correction or an invented polygon drawing.
- `Drawing1.pdf` is unusually wide and partly empty; some other sheets contain substantial blank paper. Whole sheets are retained to preserve their framing and avoid clipping faint lines or title blocks. Original vector PDFs permit closer inspection.
- Source strokes vary in thickness and some labels are small. The native vector PDF is the best option for extreme zoom; lossless encoding does not add academic content.
- These are reference sheets, not newly authored solutions or an independent audit of every construction's geometry. No academic values, lines, labels or source defects are changed.

## Website change

- `../index.html`: adds a second resource card, “Reference Drawings”, preserving the existing Projection of Solids card.
- `../reference-drawings.html`: resource shell with a left navigation reference to each of the 26 sheets.
- `../notes/reference-drawings.json`: sheet titles, stable anchors, figure dimensions and original PDF links.
- `scripts/new/source-notes.js`: small generic extension for optional section resource links; existing figure rendering, navigation and example behavior retained.
- `../assets/class/reference-drawings/`, `../notes/reference-drawings/`, ROS ZIP and these audit files: source-faithful assets/provenance.

## Verification

- All original PDF SHA-256 checks, 26 IDs/anchors, figure/source links and 26 decoded-pixel comparisons against direct PDF renders: PASS.
- JSON parsing; `node --check scripts/new/source-notes.js`; `git diff --check`: PASS.
- `python3 scripts/tools/verify_college.py`: PASS.
- `python3 college/1-1/basic-electrical-engineering/kb/tools/verify_kb.py`: PASS.
- `python3 college/1-1/matrices-calculus/kb/tools/verify_kb.py`: PASS.
- Chromium 1440px/390px: card, 26 nav entries, every image decoded, every original PDF fetched (including spaces, ampersands and parentheses in filenames), direct anchors, full-size links, ZIP integrity, mobile menu collapse and no horizontal page overflow: PASS.
- Simulated GitHub Pages `/Pankusdesk/`: image/PDF URLs, direct anchor and in-page navigation: PASS.
- Existing Projection of Solids page: 32 figures and direct-open example regression: PASS.
- `python3 scripts/tools/build_vercel.py`: PASS.

User acceptance remains separate and unchecked in the PR description.
