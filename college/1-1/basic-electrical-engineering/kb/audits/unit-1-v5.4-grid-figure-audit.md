# Unit I v5.4 — CSS Grid figure-placement audit

All 35 prescribed-textbook figures currently used on the Unit I notes page were checked against the supplied `unit_1(9)` page images and assigned an explicit inline position. The two Priyanka class-note redraws are also explicitly positioned. No Unit I figure is left with an `end` or unanchored fallback placement.

Layout policy: figures that occupy their own line in the textbook are rendered as a one-column CSS Grid row at the matching text boundary; figures that sit beside text in the textbook are rendered as a two-column CSS Grid row with the corresponding paragraph range. On narrow screens the grid collapses to one column.

## Textbook figures

| Figure asset | Book page | Section | Placement |
|---|---:|---|---|
| `f1-1.png` | 3 | 1.2 Overview of electrical-energy generation, transmission and utilization | full-width grid after paragraph 0 |
| `f1-2.png` | 3 | 1.2 Overview of electrical-energy generation, transmission and utilization | full-width grid after paragraph 2 |
| `f1-3.png` | 4 | 1.3 Electric Circuit | full-width grid after paragraph 1 |
| `f1-4.png` | 4 | Analogy between electrical, magnetic and mechanical systems | full-width grid after paragraph 1 |
| `f1-5.png` | 5 | (a) Resistance | side-by-side grid with paragraphs 1–3 (right) |
| `f1-6.png` | 5 | (a) Resistance | side-by-side grid with paragraphs 4–6 (right) |
| `f1-7.png` | 6 | (b) Inductance | full-width grid after paragraph 0 |
| `f1-8.png` | 6 | (b) Inductance | full-width grid after paragraph 3 |
| `f1-9.png` | 6 | (b) Inductance | side-by-side grid with paragraphs 10–14 (right) |
| `f1-10.png` | 7 | (c) Capacitance | side-by-side grid with paragraphs 0–3 (right) |
| `f1-11.png` | 9 | (a) Independent Voltage Source | full-width grid after paragraph 1 |
| `f1-12.png` | 9 | (b) Independent Current Source | full-width grid after paragraph 1 |
| `f1-13.png` | 10 | 2. Dependent Sources | full-width grid after paragraph 0 |
| `f1-14.png` | 10 | (a) Voltage-Controlled Voltage Source (VCVS) | full-width grid after paragraph 2 |
| `f1-15.png` | 11 | (b) Current-Controlled Voltage Source (CCVS) | full-width grid after paragraph 2 |
| `f1-16.png` | 11 | (c) Voltage-Controlled Current Source (VCCS) | full-width grid after paragraph 2 |
| `f1-17.png` | 12 | (d) Current-Controlled Current Source (CCCS) | full-width grid after paragraph 2 |
| `f1-18.png` | 12 | Practical Voltage Sources | full-width grid after paragraph 3 |
| `f1-19.png` | 13 | Practical Current Sources | full-width grid after paragraph 1 |
| `f1-20.png` | 13 | 1.4 Source Transformation | full-width grid after paragraph 1 |
| `f1-21.png` | 14 | 1.4 Source Transformation | full-width grid after paragraph 7 |
| `f1-22.png` | 15 | 1.4 Source Transformation | full-width grid after paragraph 25 |
| `f1-23.png` | 15 | Current source to voltage source | full-width grid after paragraph 2 |
| `f1-26.png` | 16 | (a) Kirchhoff’s Current Law (KCL) | side-by-side grid with paragraphs 2–3 (right) |
| `f1-27.png` | 17 | (b) Kirchhoff’s Voltage Law (KVL) | full-width grid before paragraph 3 |
| `f1-45.png` | 36 | 1.7 Star/Delta Transformations | full-width grid after paragraph 0 |
| `f1-50.png` | 48 | Exercise 1.8.1 — response due to 10-V source alone | full-width grid before paragraph 0 |
| `f1-50a.png` | 49 | Exercise 1.8.1 — response due to 10-V source alone | full-width grid after paragraph 0 |
| `f1-50b.png` | 49 | Exercise 1.8.1 — response due to 2-A source alone | full-width grid after paragraph 0 |
| `f1-50c.png` | 50 | Exercise 1.8.1 — response due to 20-V source alone and total response | full-width grid after paragraph 0 |
| `f1-51.png` | 51 | 1.9 Thevenin’s Theorem | full-width grid after paragraph 1 |
| `f1-52.png` | 51 | Step 1 — finding Thevenin resistance \(R_{th}\) | full-width grid after paragraph 0 |
| `f1-53.png` | 52 | Step 2 — finding Thevenin voltage \(V_{th}\) | full-width grid after paragraph 0 |
| `f1-54.png` | 52 | Steps 3 and 4 — obtain the equivalent and reconnect the load | full-width grid after paragraph 0 |
| `f1-55.png` | 53 | Steps 3 and 4 — obtain the equivalent and reconnect the load | full-width grid after paragraph 1 |

## Priyanka class-note redraws

| Figure asset | Section | Placement |
|---|---|---|
| `c2.png` | Types of network elements | full-width grid after paragraph 0 |
| `c1.png` | Voltage source and constant-voltage characteristic | full-width grid after paragraph 0 |

## Resistivity correction

The resistance section now uses the correct resistivity symbol `\(\rho\)` in both `topics.json` and `kb/notes/unit-1.md`.
