# Unit III Short Notes — AI redraw note integration

Date: 2026-10-16

Scope: Unit III AI-generated Short Notes only.

The four newly supplied/redrawn Unit III images corresponding internally to textbook Figures 3.31, 3.26, 3.29 and 3.35 were integrated into the surrounding revision-note prose without changing their source mapping. Student-facing captions now describe the electrical idea shown rather than exposing implementation/source commentary. The explanatory text below each image was rewritten as teaching content rather than instructions such as “Use this figure…”.

Changes made:
- DC machine construction: added a transition into the drawing and explained the stationary field system versus rotating armature system.
- Simple-loop generator: clarified that the drawing is the alternating-emf stage with continuous slip rings.
- Commutator action: connected split-ring switching directly to unidirectional external current.
- Pole pitch: connected the drawing directly to the EMF-derivation step \(t=60/(NP)\).
- Renderer: added optional `caption` support so backend figure/page provenance can remain available without forcing metadata-style labels into the visible notes.

No textbook figure numbers, source pages, source references, or formulas were removed from backend data.
