# BEE Unit I — Exercise 1.5.10 SIMPLER integration

Date: 2026-09-13

## Source workspace

Latest user-supplied `/mnt/data/re.zip`, extracted to the working workspace for this task. This workspace already contains the cumulative Kirchhoff problem-solving guide, SIMPLER integrations for Exercises 1.5.4, 1.5.6, 1.5.7, 1.5.8 and 1.5.9, and the global JSON cache-refresh fix.

## Source/resource check

No additional resource was required. The workspace contains both Figure 1.37 and Figure 1.37(a), including all resistor values, node labels, current-reference arrows, source polarity and the preserved compact textbook working.

The visual source was checked before writing the explainer:

- nodes: `a`, `b`, `c`, `d`;
- source: 12 V, positive on the `a` side and negative on the `d` side;
- resistors: 2 Ω (`a-b`), 1 Ω (`a-c`), 1 Ω (`b-c`), 4 Ω (`b-d`), 3 Ω (`c-d`);
- reference currents in Figure 1.37(a): `i1` total supply current, `i2` from `a→b`, `i3` from `b→c`;
- remaining branch-current labels: `i1-i2`, `i2-i3`, `i1-i2+i3`.

## Verified printed discrepancy

The compact source working contains a sign error during elimination of equations (1) and (2).

From

`3i1 - 9i2 - 3i3 = 0`

and

`-3i1 + 7i2 - 8i3 = 0`,

the correct sum is

`-2i2 - 11i3 = 0`,

not `-2i2 + 11i3 = 0`.

Solving the original KVL equations (1)–(3) gives:

- `i1 = 186/37 A ≈ 5.027 A`;
- `i2 = 66/37 A ≈ 1.784 A`;
- `i3 = -12/37 A ≈ -0.324 A`.

The negative `i3` means the actual current in the central 1 Ω resistor flows from `c→b` with magnitude about `0.324 A`.

The source compact solution and its printed final values remain preserved for source fidelity. An amber `Printed discrepancy` notice was added, and the SIMPLER walkthrough uses the verified corrected algebra.

## Change made

Added a detailed `SIMPLER` explainer to Exercise 1.5.10 in `kb/data/topics.json`. It follows the established Kirchhoff problem-solving sequence:

1. read the circuit before writing equations;
2. identify node and source information;
3. use KCL to derive the branch-current expressions;
4. write KVL for loop `abca`;
5. write KVL for loop `cbdc`;
6. write KVL for source loop `acda`;
7. solve the three equations carefully and expose the printed sign error;
8. interpret the negative central-branch current;
9. calculate the actual current through each of the five resistors;
10. check both KCL and the 12 V source drop using independent paths.

Correct resistor currents used in the SIMPLER:

- 2 Ω (`a→b`): `66/37 A ≈ 1.784 A`;
- central 1 Ω: `12/37 A ≈ 0.324 A`, actual direction `c→b`;
- 4 Ω (`b→d`): `78/37 A ≈ 2.108 A`;
- lower-left 1 Ω (`a→c`): `120/37 A ≈ 3.243 A`;
- 3 Ω (`c→d`): `108/37 A ≈ 2.919 A`.

## Verification performed

- `topics.json` JSON parse: PASS
- Figure 1.37 / Figure 1.37(a) semantic inspection: PASS
- independent exact solution of equations (1)–(3): PASS
- KCL branch-current checks: PASS
- 12 V upper-path and lower-path voltage checks: PASS
- BEE `verify_kb.py`: PASS
- global `verify_college.py`: PASS
- malformed-control-character scan of new explainer: PASS

No browser visual-render PASS is claimed unless separately recorded after execution.
