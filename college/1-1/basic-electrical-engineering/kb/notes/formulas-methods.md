# BEE Formula & Method Index

> This is an index, not a new source. Every line below is copied from a source-grounded topic record. If a formula convention varies by source, the unit note carries the caution.

## Unit 1

### Circuit concept, elements, current and voltage
- `i = dq/dt`
- `v = dw/dq`
Sources: `[SYL-R25-U1]` `[TB-P004]` `[TB-P005]` `[LEC-U1-01]` `[LEC-U1-02]` `[LEC-U1-03]` `[LEC-U1-04]` `[LEC-U1-08]` `[LEC-U1-21]` `[SUP-P009]` `[SUP-P012]`

### R, L and C parameters
- `Resistor: v = Ri; p = vi = i²R = v²/R`
- `Inductor: v = L·di/dt; stored energy W = ½Li²`
- `Capacitor: i = C·dv/dt; stored energy W = ½Cv²`
Sources: `[SYL-R25-U1]` `[TB-P005]` `[TB-P006]` `[TB-P007]` `[LEC-U1-05]` `[LEC-U1-06]` `[LEC-U1-07]` `[SUP-P042]` `[SUP-P047]` `[SUP-P052]`

### Source transformation
- `Voltage source Vs in series R ↔ current source Is = Vs/R in parallel R`
Sources: `[TB-P013]` `[TB-P014]` `[TB-P015]` `[SUP-P035]` `[SUP-P036]` `[SUP-P038]`

### Series, parallel and series-parallel reduction
- `Series: Req = ΣR; Leq = ΣL; 1/Ceq = Σ(1/C)`
- `Parallel: 1/Req = Σ(1/R); 1/Leq = Σ(1/L); Ceq = ΣC`
Sources: `[SYL-R25-U1]` `[TB-P031]` `[TB-P032]` `[TB-P033]` `[TB-P034]` `[TB-P035]` `[LEC-U1-17]` `[LEC-U1-18]` `[LEC-U1-19]` `[LEC-U1-20]` `[LEC-U1-22]` `[SUP-P058]` `[SUP-P062]`

### Thevenin’s theorem
- `Vterminal = Vth − Iload·Rth (with the polarity/current convention used in the lecture)`
Sources: `[SYL-R25-U1]` `[TB-P051]` `[TB-P052]` `[TB-P053]` `[TB-P054]` `[TB-P055]` `[TB-P056]` `[TB-P057]` `[TB-P058]` `[TB-P059]` `[TB-P060]` `[TB-P061]` `[TB-P062]` `[LEC-U1-26]` `[LEC-U1-27]` `[SUP-P090]` `[SUP-P091]` `[SUP-P092]` `[SUP-P093]`

## Unit 2

### Sinusoidal waveforms and basic quantities
- `T = 1/f`
- `ω = 2πf`
- `v(t) = Vm sin(ωt + φ)`
Sources: `[SYL-R25-U2]` `[TB-P073]` `[TB-P074]` `[TB-P075]` `[TB-P076]` `[TB-P077]` `[TB-P078]` `[TB-P079]` `[LEC-U2-01]`

### Average, RMS, form factor and peak factor
- `Sine half-cycle average = 0.637·peak`
- `Sine RMS = peak/√2 ≈ 0.707·peak`
- `Form factor = RMS/Average = 1.11 for sine wave`
- `Peak factor = Peak/RMS = √2 ≈ 1.414 for sine wave`
Sources: `[SYL-R25-U2]` `[TB-P080]` `[TB-P081]` `[TB-P082]` `[TB-P083]` `[TB-P084]` `[TB-P085]` `[TB-P086]` `[TB-P087]` `[TB-P088]`

### Single-phase AC through pure R
- `Z = R`
- `φ = 0°; power factor = 1`
- `P = VI for the pure-resistive RMS case`
Sources: `[SYL-R25-U2]` `[TB-P089]` `[TB-P090]`

### Single-phase AC through pure L
- `XL = ωL = 2πfL`
- `Ideal L: current lags voltage by 90°`
Sources: `[SYL-R25-U2]` `[TB-P090]` `[TB-P091]` `[TB-P092]`

### Single-phase AC through pure C
- `XC = 1/(ωC) = 1/(2πfC)`
- `Ideal C: current leads voltage by 90°`
Sources: `[SYL-R25-U2]` `[TB-P093]` `[TB-P094]`

### Series RL circuit
- `Z = R + jXL`
- `|Z| = √(R²+XL²)`
- `tanφ = XL/R`
- `P = VI cosφ`
- `Q = VI sinφ`
- `S = VI`
Sources: `[SYL-R25-U2]` `[TB-P095]` `[TB-P096]` `[TB-P097]`

### Series RC circuit
- `Z = R − jXC`
- `|Z| = √(R²+XC²)`
- `P = VI cosφ`
- `Q = VI sinφ (capacitive sign as used in the source treatment)`
- `S = P − jQ for the capacitive case as presented`
Sources: `[SYL-R25-U2]` `[TB-P098]` `[TB-P099]`

### Series RLC circuit
- `Z = R + j(XL − XC)`
- `|Z| = √(R²+(XL−XC)²)`
- `At resonance XL = XC, Z = R and power factor = 1`
- `fr = 1/(2π√(LC))`
Sources: `[SYL-R25-U2]` `[TB-P100]` `[TB-P101]` `[TB-P102]` `[TB-P103]` `[TB-P104]` `[TB-P105]` `[TB-P106]` `[TB-P107]` `[TB-P108]` `[TB-P109]` `[TB-P110]` `[TB-P111]` `[TB-P112]` `[LEC-U2-04]` `[LEC-U2-05]` `[LEC-U2-09]`

### Real, reactive and apparent power; power factor
- `Power factor = cosφ`
- `P = VI cosφ`
- `Q = VI sinφ`
- `S = VI`
Sources: `[SYL-R25-U2]` `[TB-P090]` `[TB-P096]` `[TB-P099]` `[TB-P117]` `[TB-P119]`

### Three-phase balanced circuits
- `Star: VL = √3·Vph, IL = Iph; line voltage leads corresponding phase voltage by 30°`
- `Delta: VL = Vph, IL = √3·Iph; line current lags corresponding phase current by 30°`
- `Balanced 3φ: P = √3 VL IL cosφ; Q = √3 VL IL sinφ; S = √3 VL IL`
Sources: `[SYL-R25-U2]` `[TB-P112]` `[TB-P113]` `[TB-P114]` `[TB-P115]` `[TB-P116]` `[TB-P117]` `[TB-P118]` `[TB-P119]` `[TB-P120]` `[TB-P121]` `[TB-P122]` `[TB-P123]` `[TB-P124]` `[TB-P125]` `[TB-P126]` `[TB-P127]` `[TB-P128]`

## Unit 3

### Transformer EMF equation and transformation ratio
- `E1 = 4.44 f N1 Φm`
- `E2 = 4.44 f N2 Φm`
- `k = N2/N1 = E2/E1 ≈ V2/V1 (ideal/neglected-drop treatment)`
Sources: `[TB-P133]` `[TB-P134]` `[TB-P135]` `[TB-P136]` `[TB-P137]`

### Practical transformer on no-load
- `Im = I0 sinφ0`
- `Iw = I0 cosφ0`
Sources: `[TB-P137]` `[TB-P138]` `[TB-P139]`

### Transformer voltage regulation
- `As printed: %VR = (E2 − V2)/E2 × 100`
- `Approx. lagging drop ∝ I2(R02 cosφ + X02 sinφ)`
- `Approx. leading drop ∝ I2(R02 cosφ − X02 sinφ)`
Sources: `[SYL-R25-U3]` `[TB-P144]` `[TB-P145]` `[TB-P146]` `[TB-P147]` `[TB-P148]`

### Transformer losses and efficiency
- `Copper loss ∝ I²`
- `η = output/input × 100`
- `Maximum efficiency condition (source treatment): copper loss = constant/core loss`
Sources: `[SYL-R25-U3]` `[TB-P149]` `[TB-P150]` `[TB-P151]` `[TB-P152]` `[TB-P153]` `[TB-P154]` `[TB-P155]` `[TB-P156]` `[TB-P157]`

### DC machine construction, generator principle and EMF equation
- `Eg = Φ Z N P / (60 A)`
- `For wave winding A = 2; for lap winding A = P (as presented)`
Sources: `[SYL-R25-U3]` `[TB-P158]` `[TB-P159]` `[TB-P160]` `[TB-P161]` `[TB-P162]` `[TB-P163]` `[TB-P164]` `[TB-P165]` `[TB-P166]` `[TB-P167]` `[TB-P168]` `[TB-P169]` `[TB-P170]`

### DC motor principle and back EMF
- `Force relation shown: F = BIl`
- `Motor voltage balance: V = Eb + IaRa (with brush drop added where considered)`
- `Generated/back-emf form uses Eg = ΦZNP/(60A)`
Sources: `[SYL-R25-U3]` `[TB-P171]` `[TB-P172]` `[TB-P173]` `[TB-P174]` `[TB-P175]` `[TB-P176]` `[TB-P177]`

### Load characteristics and speed control of separately excited DC motor
- `T ∝ ΦIa; with constant Φ, T ∝ Ia`
- `N ∝ (V − IaRa)/Φ`
Sources: `[SYL-R25-U3]` `[TB-P178]` `[TB-P179]` `[TB-P180]` `[TB-P181]` `[TB-P182]` `[TB-P183]` `[TB-P184]`

### Swinburne’s test
- `Iao = IL0 − If`
- `No-load armature copper loss = Iao²Ra`
- `Constant loss = no-load input − no-load armature copper loss`
- `Motor efficiency = (input − total losses)/input`
- `Generator efficiency = output/(output + total losses)`
Sources: `[SYL-R25-U3]` `[GAP-U3-SWINBURNE-NPTEL]` `[GAP-U3-SWINBURNE-IARE-BEE-LAB]`

## Unit 4

### Three-phase induction motor principle, slip and rotor frequency
- `Ns = 120f/P`
- `s = (Ns − N)/Ns`
- `fr = s f`
Sources: `[SYL-R25-U4]` `[TB-P188]` `[TB-P189]` `[TB-P190]` `[TB-P191]` `[TB-P192]` `[TB-P193]` `[TB-P194]`

### Torque-slip characteristics
- `T ∝ sR2 / (R2² + (sX2)²) (source proportional form)`
- `Low slip: T ∝ s`
- `High slip: T ∝ 1/s`
- `Maximum torque condition: s = R2/X2`
Sources: `[SYL-R25-U4]` `[TB-P195]` `[TB-P196]` `[TB-P197]`

### Working principle of synchronous generator
- `f = PNs/120`
- `Per-phase induced emf shown: E = 4.44 Φ f N`
Sources: `[SYL-R25-U4]` `[TB-P197]` `[TB-P198]` `[TB-P199]`

### Synchronous-generator voltage regulation by synchronous impedance method
- `Zs = Voc/Isc (for the same field excitation, per the BIET source)`
- `Xs = √(Zs² − Ra²)`
- `Regulation = (E0 − V)/V × 100 (conceptual EMF-method form; use the source’s phasor/sign convention for a numerical problem)`
Sources: `[SYL-R25-U4]` `[GAP-U4-SYNC-REACTANCE-NPTEL]` `[GAP-U4-OCSC-NPTEL]` `[GAP-U4-SYNC-IMPEDANCE-BIET]` `[GAP-U4-SYNC-IMPEDANCE-IARE]`

## Unit 5

### Lead-acid battery: construction, working and electrical characteristics
- `Discharge reaction as printed: Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O`
- `Capacity unit: ampere-hour (Ah)`
- `Ah efficiency = Ah discharged / Ah charged × 100`
Sources: `[SYL-R25-U5]` `[TB-P211]` `[TB-P212]` `[TB-P213]` `[TB-P214]`

### Energy-use calculations and electrical safety
- `Energy = Power × Time`
- `1 unit = 1 kWh`
Sources: `[TB-P214]` `[TB-P215]` `[TB-P216]` `[TB-P217]`
