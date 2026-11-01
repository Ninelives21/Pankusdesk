# Unit I source transcript — review notes

This change incorporates the two main notes PDFs in full, in source order:

- `11.09.2025.pdf`: 13 PDF viewer pages.
- `Part II-water - its treatment 01.10.2025.pdf`: 13 PDF viewer pages.

The user explicitly requested word-for-word incorporation. Grammar, spelling, terminology, numerical values and source errors have therefore not been corrected or paraphrased. PDF line wrapping is reflowed; source subscripts/superscripts, native tables, fractions and vector reaction arrows are rendered as HTML/MathJax. All eleven embedded visuals remain source-derived ROS images. The standalone questions/problems PDFs, FAQ and lab are outside this replacement PR.

## Source observations — outside the teaching transcript

These are editorial observations, not changes to the source text:

- Part I p.3: the printed magnesium-bicarbonate/hydrated-lime reaction is not atom-balanced. It is retained as printed.
- Part I p.5: the worked example is an original raster panel. Its printed intermediate rounding (33.3) and total (333.3) are retained; no alternate calculation has replaced the supplied solution.
- Part I p.5: the source makes broad health claims about hard water. These are retained source statements, not independently verified health guidance.
- Part I p.8: the embedded table is labelled **INDIAN STANDARD SPECIFICATIONS FOR DRINKING WATER IS 10500**, not WHO. It has not been relabelled or updated to a newer standard. Several printed entries and remarks may require comparison with the original standard before independent use.
- Part I p.10: the sodium-aluminate equation prints `2Al(OH)3` on the product side; it is not atom-balanced. It is retained as printed.
- Part I pp.11–12: chlorination reactions, dosage values, the stated chlorine/ammonia volume ratio and comparative claims are retained as supplied, without technical correction.
- Part II p.1: the third chloramine reaction prints `NHCl2 + H2O → NCl3 + H2O`. The left reagent is retained as **H2O**, not silently changed to HOCl.
- Part II p.6: the printed Calgon complex reaction is retained without balancing or rewriting its species.
- Part II pp.8–9: unusual resin notation, charges and reaction coefficients are retained.

## ROS inventory and source limitations

See [the complete ROS register](unit-1-ros-register.md): nine drawings/diagram groups plus two raster-only text panels. The paired sand filters and boiler cross-sections stay grouped. Embedded raster labels may be small or blurry; lossless encoding does not recover missing detail. Readers can open images at native size.

The PDF display orientation of two stored sideways images is restored losslessly, matching their horizontal presentation in the supplied PDF. Only blank top/bottom margins of the specifications panel are trimmed. No redrawing, resampling, sharpening, recolouring, watermark removal or scientific correction is performed.

Source hashes, viewer-page mapping, image dimensions, treatment and per-page native-character accounting are in [the source audit](unit-1-source-audit.json). Automated accounting establishes coverage of native PDF text, not academic correctness or recovery of text inside raster panels. Visual QA must compare the actual pages/panels separately.
