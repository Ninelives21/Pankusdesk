# Hardness numericals — source and solution review

Source: `Problems on hardness .docx.pdf`, three PDF viewer pages. Four numbered questions and their CaCO₃-equivalent tables are retained verbatim, apart from reflow and chemical subscript presentation. The Problem 2 table header from p.1 and rows from p.2 are reunited. Both raster panels are retained through ROS. The previously merged two main notes PDFs and their eleven images are unchanged.

## Authored working

The user explicitly requested the final problem be solved despite the absent solution. All four numbered questions now have complete, separately labelled PankusDesk working and bold final answers. These are not represented as printed textbook solutions.

Problem 4 uses **14.6 mg/L**, exactly as the question prints. The supplied table is left unchanged at **146 mg/L** / **100 mg/L equivalent**, and is marked as discrepant. The worked calculation uses **10 mg/L equivalent** for the question's value.

The source says “dissolved salts”. The solution therefore assumes the listed CaCO₃ contributes dissolved carbonate hardness and that no Ca/Mg is removed by precipitation. HCl = 36 mg/L is retained, using M(HCl) = 36.5 g/mol. Its CaCO₃-equivalent acidity is 36 × 50/36.5 = 49.315068… mg/L. This converts an equivalent amount of temporary to permanent hardness; it is neither ignored nor added to total Ca/Mg hardness.

- Total hardness: 100 + 10 + 10 + 10 = **130 ppm**.
- Temporary hardness: 110 − 49.315068… = **60.684931… ppm**.
- Permanent hardness: 20 + 49.315068… = **69.315068… ppm**.

An independent charge/alkalinity balance reproduces these values exactly with rational arithmetic. If 146 mg/L was intended, temporary hardness becomes 150.684931… ppm and total hardness 220 ppm; permanent hardness remains 69.315068… ppm. This alternative is explicitly distinguished from the primary answer.

No claim is made that the paper specifies a unique real-water equilibrium model. If its CaCO₃ is undissolved solid, dissolution/CO₂ conditions would be needed; that is not the printed dissolved-salt interpretation used here.

For Problem 3, total hardness follows the supplied Ca/Mg salt inventory; NaOH and KOH are not hardness contributions. This does not simulate subsequent precipitation equilibria. All degree-Clarke answers consistently use the source's rounded **0.07 °Cl per ppm**, not a mixture with its separately rounded reciprocal **14.3 ppm per °Cl**.

## ROS panels

| Stable ID | PDF page | Panel | Processing |
| --- | --- | --- | --- |
| CFE-U1-N-P001-V01 | 1 | Opening worked example and its complete table/solution | Crop original screenshot to the visible complete example; exclude browser/desktop and off-page unrelated problem; lossless WebP |
| CFE-U1-N-P003-V01 | 3 | Degree of Hardness formula, conversion box and ten-salt molecular-weight table | Complete original embedded asset; lossless WebP |

The original page-3 chart has **ten rows**, including Al₂(SO₄)₃ and FeSO₄. Those rows are retained, even though the four questions use Ca/Mg salts. See [contact sheet](unit-1-numericals-contact.jpg) and [source/solution audit](unit-1-numericals-audit.json). Both outputs decode pixel-identically to the retained original pixels; no redraw, enhancement, resampling or label changes.
