# Unit Build Checklist — Design Lock v2

Use this checklist for every college unit. A unit is not `ready` until the applicable items pass.

---

## A. Design lock and workspace

- [ ] Read `college/COLLEGE_BUILD_STANDARD.md`.
- [ ] Read `college/REFERENCE_IMPLEMENTATION.md`.
- [ ] Read `college/NOTEBOOK_REDRAW_STYLE.md` before any redraw work.
- [ ] Inspect the latest workspace, not an old delta/chat reconstruction.
- [ ] Inspect target `subject.json`, current schemas and shared renderers.
- [ ] Confirm whether the unit is currently `scaffold` or `ready`.

## B. Source intake and lock

- [ ] Inventory the official syllabus/regulation source.
- [ ] Inventory prescribed textbook pages, figures and chapter questions.
- [ ] Inventory supplied lectures/transcripts.
- [ ] Inventory dated class notes.
- [ ] Inventory supplementary documents.
- [ ] Record missing lecture numbers/pages/files and known source anomalies exactly.
- [ ] Do not use model memory to fill a source gap silently.

## C. Syllabus coverage and gaps

- [ ] Atomise the official unit syllabus.
- [ ] Map every syllabus atom to real source references.
- [ ] Mark unsupported required material as `SOURCE_GAP`.
- [ ] Obtain explicit approval before using an outside gap source.
- [ ] Record approved gap-source provenance.
- [ ] Do not promote useful extra material to official/core scope.

## D. Textbook-faithful cumulative theory

- [ ] Treat the prescribed textbook as the primary notes source.
- [ ] Preserve textbook sequence and terminology.
- [ ] Preserve definitions and explanatory detail; do not over-summarise.
- [ ] Keep equations/derivations in situ.
- [ ] Keep useful worked-example calculation lines where they teach the method.
- [ ] Put every example in a dropdown and include the full step-by-step solution; never leave an example as question + final answer only.
- [ ] Keep the full example question visible while the dropdown is closed; clicking `+` must reveal the solution/working only.
- [ ] For every labelled multi-part question/example/answer, put each subpart on its own line; in solutions, give each subpart its own clearly separated labelled panel rather than one continuous block.
- [ ] Show every substantive transformation/row operation/substitution/iteration required to reproduce the result.
- [ ] Correct only grammar/punctuation/obvious typos unless a larger correction is explicitly approved.
- [ ] Preserve/flag source inconsistencies rather than silently reconciling them.
- [ ] Build/update stable topic IDs.
- [ ] Set `core`, `supporting`, `core-gap-filled` correctly.
- [ ] De-duplicate overlapping textbook/lecture/class material.
- [ ] Write theory directly; remove source/workflow narration from student-facing prose.
- [ ] Add topic + section `source_refs`.
- [ ] Add `book_refs` where useful for internal/page reference.
- [ ] Synchronize `kb/notes/unit-N.md` where used.

## E. Mathematics

- [ ] Use MathJax/LaTeX delimiters for mathematical content.
- [ ] Use `\dfrac` for every authored fraction; no `\frac` in ready-unit topic content.
- [ ] Verify subscripts/symbols (`\rho`, `\varphi`, etc.) were not corrupted by code escapes.
- [ ] Check equations against the source after programmatic edits.

## F. Quick recall, self-checks and teaching aids

- [ ] Add concise `learn` points where useful.
- [ ] Keep generated `self_checks` separate from official textbook/PYQ material.
- [ ] Add formulas/methods/cautions only when useful and source-safe.
- [ ] If source notes are too terse or symbol-heavy, add a blue explanation accordion rather than rewriting the source material.
- [ ] Give each explanation dropdown a meaningful title.
- [ ] Keep explanation language simple enough to teach the confusing step.
- [ ] Use `accordion_recap` only when it adds real revision value.

## G. Figures — selection and asset role

- [ ] Audit which figures are actually needed.
- [ ] Put textbook theory figures in `assets/book/uN/theory/`.
- [ ] Put textbook question/example figures in `assets/book/uN/examples/`.
- [ ] Put derived dated class visuals in `assets/class/YYYY-MM-DD/figures/`.
- [ ] Do not commit raw notebook photographs under website asset `raw` folders.
- [ ] Give every embedded figure descriptive alt text.
- [ ] Record intrinsic `width`/`height` when available.
- [ ] Do not expose capture filenames as student-facing descriptions.

## H. NRS technical redraw gate

For **every technical redraw**:

- [ ] Identify what the drawing actually is (circuit, graph, field diagram, classification, etc.).
- [ ] State meaning-bearing details before generation.
- [ ] Confirm ambiguous details with the user.
- [ ] Verify arrow directions individually, not just “clockwise/anticlockwise” as a label.
- [ ] Verify polarity.
- [ ] Verify dot/cross / into-page/out-of-page conventions.
- [ ] Verify source orientation and graph axes.
- [ ] Verify circuit connectivity/topology.
- [ ] Verify around/through/front/behind spatial relationships.
- [ ] Verify meaningful counts (loops, turns, arrows, terminals, panels).
- [ ] Generate only after the semantic audit is understood.
- [ ] Inspect the actual output against the audit.
- [ ] Reject/regenerate any technically wrong output.
- [ ] Do not let a textbook cue override the actual class-note source.

## I. Figure placement

- [ ] Compare each used textbook figure with the actual source page.
- [ ] Place every ready-unit figure explicitly with `after` or `grid` metadata.
- [ ] Do not leave unanchored fallback figures.
- [ ] Use CSS Grid, not floats, for side-by-side textbook placement.
- [ ] Use the source-faithful paragraph range (`grid.start`–`grid.end`).
- [ ] Default side-by-side desktop layout to 50/50 text/image.
- [ ] Keep genuine full-width figures full-width.
- [ ] Verify mobile one-column behaviour.
- [ ] Verify labels/arrows remain readable at normal page size.

## J. Daily class notes

- [ ] Create/maintain `kb/class-log/YYYY-MM-DD/entry.json`.
- [ ] Keep `raw.md` where the workflow retains it.
- [ ] Preserve page sequence and notebook meaning faithfully.
- [ ] Record user-confirmed ambiguous readings where useful.
- [ ] Map the dated entry to stable topic IDs.
- [ ] Add/update the class source in provenance/source manifest.
- [ ] Add the date to `college/<semester>/data/class-log.json`.
- [ ] Verify calendar → dated log link.
- [ ] Integrate useful material into the correct point in the cumulative topic.
- [ ] Use visibly labelled class-note sections, not source-management prose.
- [ ] Add quiet `class_history` links where useful.
- [ ] Combine adjacent class sketches only when they clearly form one concept and the interpretation is confirmed.
- [ ] Preserve contradictions; do not silently reconcile them.

## K. Prescribed textbook questions

- [ ] Audit all chapter-end questions belonging to the unit.
- [ ] Preserve official wording.
- [ ] Give every question a stable ID/anchor.
- [ ] Link theory practice rows to exact anchors.
- [ ] Keep PankusDesk answers distinct from official textbook solutions.
- [ ] Use source-backed steps/equations/tables/figures only.
- [ ] Store printed final answers as `book_check` where appropriate.
- [ ] Flag printed/source discrepancies.
- [ ] Store/render labelled question subparts structurally so `(i)`, `(ii)`, `(iii)` / `(a)`, `(b)`, `(c)` each begin on a new line.
- [ ] Render multi-part solutions as separate labelled panels with a visible boundary/background change between parts.
- [ ] Use `status: source-gap` when sources cannot support an answer.

## L. PYQs

- [ ] Keep PYQs subject-wide by default.
- [ ] Do not invent wording, year, marks or exam metadata.
- [ ] Add unit/topic mappings only when confident.

## M. UI and generic architecture

- [ ] Reuse `scripts/new/subject-unit.js`.
- [ ] Reuse `scripts/new/unit-questions.js`.
- [ ] Reuse `scripts/new/class-log.js`.
- [ ] Reuse `scripts/new/calendar.js` and semester data architecture.
- [ ] Keep unit/question/class-log HTML as lightweight shells.
- [ ] Do not create a subject-specific duplicate renderer without an approved architectural reason.
- [ ] Preserve topic-nav independent scroll and active tracking.
- [ ] Preserve Quick recall / Check yourself / practice navigation.
- [ ] Preserve visibly separate class-note and explanation treatments.
- [ ] Verify desktop/tablet/mobile behaviour.

## N. Verification

- [ ] Parse all changed JSON.
- [ ] Syntax-check changed JavaScript/Python.
- [ ] Validate changed data against current schemas where tooling is available.
- [ ] Run subject-specific verifier.
- [ ] Run `python3 scripts/tools/verify_college.py`.
- [ ] Confirm configured source references resolve.
- [ ] Confirm ready-unit figures exist, have useful alt text and explicit placement.
- [ ] Confirm class-note sections have source labels + class source refs.
- [ ] Confirm explanation accordions are structurally valid.
- [ ] Confirm practice anchors resolve.
- [ ] Confirm class-log mappings and calendar links resolve.
- [ ] Confirm no raw notebook binaries are inside website class `raw` folders.
- [ ] Confirm no `\frac` remains in ready-unit topic content.
- [ ] Confirm student-facing theory/accordion prose contains no build/source meta-commentary.
- [ ] Fix underlying errors; do not weaken verification to obtain PASS.

## O. Ready gate

Set `publicationStatus: "ready"` only when:

- [ ] official scope is fully covered or explicitly gap-resolved;
- [ ] textbook-faithful theory is complete;
- [ ] all required figures are source-checked and correctly placed;
- [ ] class material supplied to date has been integrated/logged;
- [ ] questions/practice links are complete for the intended unit release;
- [ ] visual QA passes;
- [ ] subject verifier passes;
- [ ] generic college verifier passes for the unit's changes.

## P. Handoff

- [ ] Create a **minimal delta** unless a full workspace is explicitly requested.
- [ ] Package the delta with one top-level folder.
- [ ] List changed/added files.
- [ ] Provide an extraction command that works from the stated directory.
- [ ] Provide `rsync -avhn` dry-run first.
- [ ] Provide real `rsync -avh` second.
- [ ] Never use `--delete` for a normal delta.
- [ ] Do not guess the user's Pankusdesk path.
- [ ] Provide `git status` and verifier command(s).
