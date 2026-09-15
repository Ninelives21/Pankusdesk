# BEE Unit I — Kirchhoff SIMPLER hand-holding pass

Date: 2026-09-15

## Source workspace

Latest user-supplied `/mnt/data/re.zip`, extracted as the working workspace for this task. No older delta/workspace was used as the implementation base.

## Scope

Updated the existing SIMPLER explainers on the Unit I Kirchhoff's-laws page to follow a stronger hand-holding rule: do not merely state a classification or sign; explain how the student can know it from the visible circuit symbol, arrowhead, polarity mark, node connection, or branch topology.

No textbook question, compact source solution, figure asset, source provenance, or printed answer was replaced by this pass.

## Content changes

Updated all 10 existing Kirchhoff SIMPLER explainers in `kb/data/topics.json`:

1. General Kirchhoff problem-solving SIMPLER guide.
2. Exercise 1.5.4.
3. Exercise 1.5.6.
4. Exercise 1.5.7.
5. Exercise 1.5.8.
6. Exercise 1.5.9.
7. Exercise 1.5.10.
8. Exercise 1.5.11.
9. Exercise 1.5.13.
10. Exercise 1.5.14.

Examples of the new hand-holding treatment include:

- diamond shape -> dependent/controlled source;
- `+/-` on a source -> voltage-source polarity;
- arrow inside a source -> current source and source-current direction;
- circle + arrow -> independent current source;
- diamond + arrow -> dependent current source;
- `V_x` in Exercise 1.5.11 explicitly identified as the controlling voltage across the 5 ohm resistor, not as the dependent source itself;
- uninterrupted wire / labelled junctions -> node identity;
- same two end nodes -> parallel;
- end-to-end elements with no branching junction -> series/same current;
- visible current arrowheads -> entering/leaving status for KCL;
- dashed `V_ab` reference in Exercise 1.5.8 explicitly distinguished from a conducting wire;
- negative current/voltage results reconnected to the originally drawn reference arrow/polarity.

For Exercise 1.5.11 the wording now explicitly states that **we know the `2V_x` source is dependent because it is drawn as a diamond**, while `V_x` itself is only the controlling voltage.

## Global rule added

Updated the shared college standard and checklist so future SIMPLER content across subjects follows the same rule:

- SIMPLER is hand-holding, not merely shorter;
- assume the student may return with little remembered context;
- re-establish the visual/semantic clue before using it;
- explain "how we know" an important classification/sign from the visible figure;
- avoid unexplained "obvious", "clearly", or "by inspection" jumps.

Files updated for this rule:

- `college/COLLEGE_BUILD_STANDARD.md`
- `college/UNIT_BUILD_CHECKLIST.md`

No shared renderer/CSS change was required because this is a content-quality rule, not a component behaviour or visual-style change.

## Verification performed

- JSON parse: PASS.
- Targeted Kirchhoff SIMPLER assertion: PASS — 10 existing explainers found.
- Exercise 1.5.11 assertion: PASS — diamond shape explicitly tied to the dependent `2V_x` source; `V_x` explicitly distinguished as the controlling voltage.
- Decoded JSON control-character scan: PASS.
- Kirchhoff MathJax delimiter-balance scan: PASS.
- Relevant circuit figures visually reviewed from the current workspace before wording the visual-cue explanations.
- BEE KB verifier: PASS.
- Global College verifier: PASS.

A headless Chromium page screenshot was attempted in the container but did not complete before timeout, so no browser-render visual check is claimed for this handoff.
