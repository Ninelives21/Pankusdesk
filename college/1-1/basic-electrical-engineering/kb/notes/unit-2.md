# Unit 2 — Steady State AC Circuits

> **Source-lock:** These notes are consolidated only from the official R25 Unit-II syllabus boundary, the supplied prescribed-textbook captures pp.73–129, and the supplied Unit-II lecture transcripts (01–07 and 09). Lecture 08 was not supplied. The gap package contains no Unit-II gap source and is therefore not used here. Supporting material is retained only when it comes from those supplied sources and is not allowed to expand the R25 core.

## Sinusoidal waveforms and basic quantities

**Status:** Core R25

### Quick recall
- A sinusoidal alternating quantity varies periodically and reverses direction or polarity; one complete cycle corresponds to 360° or 2π radians.
- The basic quantities are peak value, instantaneous value, cycle, time period T, frequency f and angular frequency ω, with f = 1/T and ω = 2πf.
- A phase angle locates a sinusoid relative to a chosen reference; positive and negative angular displacement indicate lead and lag relative to that reference.

### Why sinusoidal waveforms are preferred
- Many alternating quantities can be expressed as sums of sinusoids, so sinusoidal analysis provides a useful basis for more general waveforms.
- Sinusoidal signals are easy to generate and transmit.
- They are convenient mathematically because differentiation and integration of a sinusoid produce another sinusoid.
- In a linear circuit, a sinusoidal excitation produces a sinusoidal forced response at the same frequency. This is another reason sinusoids are especially convenient for analysis and measurement.

**Section provenance:** `[TB-P073]` `[LEC-U2-01]`

### Cycle, period and frequency
A cycle is the complete set of positive and negative values through which an alternating quantity passes before the pattern repeats. If one cycle takes T seconds, T is the time period. Frequency f is the number of cycles completed per second and is measured in hertz.

- One cycle = 360° = 2π rad.
- f = 1/T and T = 1/f.
- For a 50 Hz supply, one cycle lasts 1/50 s = 0.02 s = 20 ms.

**Section provenance:** `[TB-P074]`

### Angular frequency and electrical angle
If a sinusoid completes f cycles each second and each cycle spans 2π radians, its angular frequency is ω = 2πf rad/s. After time t, the corresponding angular displacement is θ = ωt = 2πft.

**Section provenance:** `[TB-P074]`

### Instantaneous value of a sinusoid
For a sine wave starting from zero with positive slope, the instantaneous value is written v(t) = V_m sin(ωt), where V_m is the maximum or peak value. If the waveform has an initial phase angle φ relative to the reference, the general form is v(t) = V_m sin(ωt + φ).

- At ωt = 0°, v = 0.
- At ωt = 90°, v = V_m.
- At ωt = 180°, v = 0.
- At ωt = 270°, v = −V_m.

**Section provenance:** `[TB-P075]` `[TB-P076]`

### Phase, lead and lag
Phase specifies the angular position of a sinusoid relative to a reference waveform. If one sinusoid reaches the same point in its cycle earlier than the reference, it leads; if it reaches it later, it lags. The phase difference is the angular separation between the corresponding phasors or waveforms.

- A waveform written with +φ is advanced by φ relative to the zero-phase reference.
- A waveform written with −φ is delayed by φ relative to the zero-phase reference.
- When comparing two waveforms, first express them in a common sine or cosine form before deciding the phase difference.

**Section provenance:** `[TB-P075]` `[TB-P076]` `[TB-P077]` `[TB-P078]`

### What 'steady state' means in these notes
*Supporting context within the supplied corpus; not a separate R25 syllabus atom.*

Immediately after an excitation is applied, a circuit may contain a natural or transient part as well as the forced response. For a stable circuit, the natural part dies away; the persistent sinusoidal forced response remains.

This unit is concerned with that sinusoidal steady-state behaviour. Transient analysis itself is outside the R25 Unit II scope.

**Section provenance:** `[LEC-U2-01]` `[LEC-U2-02]` `[LEC-U2-04]`

### Formula anchors
- `T = 1/f`
- `ω = 2πf`
- `θ = ωt = 2πft`
- `v(t) = V_m sin(ωt + φ)`

### Problem-solving method
1. Write the waveform in the standard form V_m sin(ωt + φ) or V_m cos(ωt + φ).
2. Read V_m directly as the peak value.
3. Use f = ω/(2π) and T = 1/f.
4. Substitute the required time t into ωt + φ to obtain the instantaneous value.
5. For phase comparison, convert both quantities to the same trigonometric reference before subtracting their phase angles.

### Important notes
- Do not compare a sine angle directly with a cosine angle without first converting them to a common sine/cosine form.
- The natural/transient discussion is explanatory context only; R25 Unit II asks for steady-state AC circuits.

### Check yourself
1. **What is the relation among time period, frequency and angular frequency?**
   - T = 1/f and ω = 2πf. One complete cycle corresponds to 2π radians.
2. **What is the instantaneous value of a sinusoid with peak V_m and phase φ?**
   - v(t) = V_m sin(ωt + φ), where ω = 2πf.
3. **Why are sinusoids especially convenient for steady-state analysis?**
   - Sinusoids are easy to generate and manipulate mathematically; in a linear circuit, a sinusoidal excitation also produces a sinusoidal forced response at the same frequency, so the response can be characterized mainly by magnitude and phase.

### Physical-book reference
- pp. 73–79; source image(s): 73.png–79.png — sinusoidal representation, phase, phasor introduction and worked phase examples

**Topic provenance:** `[SYL-R25-U2]` `[TB-P073]` `[TB-P074]` `[TB-P075]` `[TB-P076]` `[TB-P077]` `[TB-P078]` `[TB-P079]` `[LEC-U2-01]` `[LEC-U2-02]` `[LEC-U2-04]`

## Average, RMS, form factor and peak factor

**Status:** Core R25

### Quick recall
- For a symmetrical sine wave the algebraic average over a full cycle is zero, so its average value is conventionally evaluated over a half cycle.
- The RMS or effective value of an AC quantity is the DC value that would produce the same heating effect in a resistor over the same time.
- For a sine wave, average = 0.637 of peak, RMS = 0.707 of peak, form factor = 1.11 and peak factor = 1.414.

### Average value
The average value of a periodic quantity is its total signed area divided by the interval over which the average is taken. For a symmetrical sine wave, the positive and negative half-cycle areas cancel over a full cycle, so the full-cycle average is zero. The useful average magnitude is therefore taken over one half cycle.

- `I_avg = (1/π)∫₀^π I_m sinθ dθ = 2I_m/π = 0.637 I_m`

**Section provenance:** `[TB-P080]` `[TB-P081]`

### RMS or effective value
The need for RMS value comes from comparing AC and DC by their heating effect in the same resistance. If an alternating current produces the same heat as a certain DC current over the same interval, that DC current is the effective or RMS value of the AC current.

The RMS operation means: square the instantaneous quantity, find the mean of the squared values over the chosen cycle, then take the square root.

**Section provenance:** `[TB-P081]` `[TB-P082]`

### RMS value of a sine wave
For i = I_m sinθ, integrating i² over a half cycle and taking the square root gives I_rms = I_m/√2 = 0.707I_m. The same relation applies to sinusoidal voltage.

**Section provenance:** `[TB-P082]` `[TB-P083]`

### Form factor
Form factor compares the RMS value with the average value of the same alternating quantity. For a sine wave it is 0.707/0.637 ≈ 1.11.

**Section provenance:** `[TB-P083]`

### Peak factor
Peak factor compares the maximum or peak value with the RMS value. For a sine wave, peak factor = 1/0.707 ≈ 1.414 = √2.

**Section provenance:** `[TB-P084]`

### Non-sinusoidal periodic waveforms
The same definitions apply to non-sinusoidal periodic waves. The waveform must first be expressed mathematically over the relevant intervals, after which average and RMS values are obtained by integration. For piecewise waveforms, each interval contributes separately.

- For a saw-tooth wave rising linearly from 0 to V_m over T, V_avg = V_m/2 and V_rms = V_m/√3.
- For a waveform that is zero during part of the cycle and sinusoidal during the remainder, include both intervals explicitly in the average/RMS integral.
- For a triangular waveform, write the line equation for each segment and integrate each piece over the period.

**Section provenance:** `[TB-P084]` `[TB-P085]` `[TB-P086]` `[TB-P087]` `[TB-P088]`

### Formula anchors
- `Sine-wave average over half cycle = 2V_m/π = 0.637V_m`
- `Sine-wave RMS = V_m/√2 = 0.707V_m`
- `Form factor = RMS value / Average value`
- `Peak factor = Peak value / RMS value`
- `Sine-wave form factor ≈ 1.11`
- `Sine-wave peak factor = √2 ≈ 1.414`

### Problem-solving method
1. Choose the correct averaging interval. For a symmetric sine wave, use a half cycle for average magnitude; for a general waveform, use its actual period.
2. Write the waveform equation v(t) or v(θ), piecewise if necessary.
3. For average value, integrate v over the interval and divide by the interval length.
4. For RMS, integrate v² over the interval, divide by the interval length and take the square root.
5. Use the resulting average and RMS values to calculate form factor; use peak/RMS for peak factor.

### Important notes
- For a symmetric sine wave, the full-cycle algebraic average is zero; the quoted 0.637V_m average is the half-cycle average magnitude.

### Check yourself
1. **Why is the average of a sine wave usually quoted over a half cycle?**
   - The positive and negative half-cycle areas cancel over a complete cycle, giving zero algebraic average. Over a half cycle, the average magnitude is 2V_m/π = 0.637V_m.
2. **What physical meaning does RMS value have?**
   - It is the DC value that would produce the same heating effect in a resistor as the alternating quantity over the same time.
3. **What are the sine-wave form factor and peak factor?**
   - Form factor = 0.707/0.637 ≈ 1.11. Peak factor = 1/0.707 = √2 ≈ 1.414.

### Physical-book reference
- pp. 80–88; source image(s): 80.png–88.png — average and RMS derivations plus saw-tooth, rectified and triangular examples

**Topic provenance:** `[SYL-R25-U2]` `[TB-P080]` `[TB-P081]` `[TB-P082]` `[TB-P083]` `[TB-P084]` `[TB-P085]` `[TB-P086]` `[TB-P087]` `[TB-P088]`

## Phasor representation and complex form

**Status:** Core R25

### Quick recall
- A phasor represents a sinusoidal quantity by a rotating vector whose magnitude and angular position encode peak/RMS magnitude and phase.
- Same-frequency sinusoids can be compared and combined through their phasors rather than repeatedly manipulating time-domain sine and cosine expressions.
- The complex-exponential basis of phasors turns the sinusoidal steady-state relations of R, L and C into algebraic impedances.

### From sine wave to rotating phasor
A sinusoid can be represented by a phasor rotating at angular velocity ω. As the phasor completes one revolution, the sinusoid completes one cycle. The projection of the rotating phasor on a chosen axis gives the instantaneous sinusoidal value.

Because all quantities in a single-frequency steady-state circuit rotate at the same angular speed, their relative angular separations remain fixed. Those separations are the phase differences that matter in circuit analysis.

**Section provenance:** `[TB-P075]` `[TB-P076]`

### Reading lead and lag from phasors
A phasor located ahead of another in the direction of rotation leads it by the angular separation; one behind lags. A negative coefficient or a sine/cosine conversion can shift the apparent angle, so expressions should be reduced to a common reference before deciding which quantity leads.

**Section provenance:** `[TB-P076]` `[TB-P077]` `[TB-P078]` `[TB-P079]`

### Rectangular, polar and exponential forms
The same phasor can be written in rectangular form x + jy, polar form M∠φ and exponential form Me^{jφ}. These are equivalent descriptions of the same complex quantity.

- Rectangular form separates horizontal and quadrature components.
- Polar form shows magnitude and phase directly.
- Exponential form expresses the same magnitude and phase using e^{jφ}.

**Section provenance:** `[TB-P079]`

### Why phasors simplify sinusoidal steady-state calculations
*Supporting context within the supplied corpus; not a separate R25 syllabus atom.*

A deeper phasor interpretation is to represent a sinusoid through a complex exponential, solve the linear circuit for the corresponding complex amplitude, and take the appropriate real sinusoidal result at the end. The common time factor e^{jωt} is suppressed, leaving only complex amplitudes to manipulate.

Under this representation differentiation corresponds to multiplication by jω. Consequently the element voltage/current ratios become algebraic impedances: R for a resistor, jωL for an inductor and 1/(jωC) for a capacitor.

**Section provenance:** `[LEC-U2-02]` `[LEC-U2-03]` `[LEC-U2-05]` `[LEC-U2-06]` `[LEC-U2-07]`

### Limits of the phasor method
*Supporting context within the supplied corpus; not a separate R25 syllabus atom.*

Phasor analysis gives the sinusoidal steady-state response, not the natural/transient response. It treats one frequency at a time. If independent excitations have different frequencies, each frequency is analysed separately and the time-domain responses can then be superposed.

**Section provenance:** `[LEC-U2-03]`

### Formula anchors
- `Rectangular: V = x + jy`
- `Polar: V = |V|∠φ`
- `Exponential: V = |V|e^{jφ}`
- `Z_R = R`
- `Z_L = jωL`
- `Z_C = 1/(jωC) = −j/(ωC)`

### Problem-solving method
1. Express all same-frequency quantities using a common sine or cosine convention.
2. Convert each phasor to a convenient complex form.
3. Use ordinary complex-number addition, subtraction, multiplication or division as required.
4. Convert the final phasor back to magnitude-angle form and then to the corresponding sinusoidal time expression if needed.

### Important notes
- Phasor analysis here is a steady-state method. It does not include the transient/natural response.

### Check yourself
1. **What information does a phasor retain from a sinusoid?**
   - Its magnitude and phase. In a fixed-frequency steady-state analysis the common time variation is suppressed, so relative magnitudes and angles can be manipulated directly.
2. **What are the sinusoidal steady-state impedances of R, L and C?**
   - Z_R = R, Z_L = jωL and Z_C = 1/(jωC) = −j/(ωC).
3. **Does a phasor solution include the natural/transient response?**
   - No. The phasor method here gives the sinusoidal steady-state response only.

### Physical-book reference
- pp. 75–79; source image(s): 75.png–79.png — rotating phasor, phase relations and rectangular/polar/exponential forms

**Topic provenance:** `[SYL-R25-U2]` `[TB-P075]` `[TB-P076]` `[TB-P077]` `[TB-P078]` `[TB-P079]` `[LEC-U2-02]` `[LEC-U2-03]` `[LEC-U2-05]` `[LEC-U2-06]` `[LEC-U2-07]`

## Single-phase AC through pure resistance

**Status:** Core R25

### Quick recall
- In a pure resistive AC circuit, voltage and current are in phase, so the impedance is R and the power factor is unity.
- Instantaneous power remains non-negative; the resistor continuously absorbs energy and the average power is real or active power.

### Voltage-current relation
For a resistance R connected across v = V_m sinωt, Ohm's law gives i = v/R = I_m sinωt. Voltage and current therefore pass through zero and reach their positive and negative maxima together: their phase difference is zero.

**Section provenance:** `[TB-P089]`

### Phasor and impedance
The voltage and current phasors lie on the same line because their phase angle is 0°. The impedance is the ratio of the voltage phasor to the current phasor and is purely real: Z = R.

**Section provenance:** `[TB-P089]` `[TB-P090]`

### Power in a pure resistor
Instantaneous power is p = vi = V_mI_m sin²ωt. Using the double-angle identity, it consists of a constant term plus a term at twice the supply frequency. The instantaneous power never reverses sign, so power flows from source to load throughout the cycle.

The average value is P = V_rms I_rms. The resistor therefore consumes active or real power.

**Section provenance:** `[TB-P090]`

### Formula anchors
- `Z = R`
- `φ = 0°`
- `Power factor = cosφ = 1`
- `p = V_mI_m sin²ωt`
- `P = V_rms I_rms`

### Check yourself
1. **What is the phase relation between voltage and current in a pure resistance?**
   - They are in phase, so φ = 0° and power factor = 1.
2. **Why is the average power in a pure resistor non-zero?**
   - Its instantaneous power p = vi remains non-negative over the cycle, so energy flows continuously from the source into the resistor and is dissipated as real/active power.

### Physical-book reference
- pp. 89–90; source image(s): 89.png–90.png

**Topic provenance:** `[SYL-R25-U2]` `[TB-P089]` `[TB-P090]`

## Single-phase AC through pure inductance

**Status:** Core R25

### Quick recall
- For an ideal pure inductor, current lags voltage by 90° and the inductive reactance is X_L = ωL.
- Its impedance is jX_L and its power factor is zero.
- An ideal inductor consumes no average active power; energy is alternately stored in and returned from the magnetic field, producing reactive power exchange.

### Deriving the current phase
With v = V_m sinωt applied to an ideal inductor, the voltage-current relation leads to an integrated current proportional to −cosωt. Rewriting −cosωt as sin(ωt − 90°) shows that current lags the applied voltage by 90°.

**Section provenance:** `[TB-P090]` `[TB-P091]`

### Inductive reactance
The current amplitude is I_m = V_m/(ωL). The quantity ωL therefore plays the role of AC opposition and is called inductive reactance X_L. Since X_L = 2πfL, inductive reactance increases directly with frequency.

- At f = 0 (steady DC), X_L = 0.
- An ideal inductor therefore behaves as a short circuit in DC steady state.

**Section provenance:** `[TB-P091]` `[TB-P092]`

### Impedance and power factor
The impedance of the pure inductor is Z = jX_L, corresponding to a +90° impedance angle. Voltage leads current by 90°, so cos90° = 0 and the power factor is zero.

**Section provenance:** `[TB-P092]`

### Power exchange in a pure inductor
The instantaneous power changes sign twice in each cycle. During one part of the cycle energy flows from the source into the magnetic field; during another part it returns to the source. Positive and negative areas cancel, so the average active power is zero.

This exchanged, non-working component is reactive or imaginary power.

**Section provenance:** `[TB-P092]` `[TB-P093]`

### Formula anchors
- `X_L = ωL = 2πfL`
- `Z_L = jX_L`
- `I_m = V_m/X_L`
- `Ideal L: current lags voltage by 90°`
- `Power factor = 0`
- `Average active power = 0`

### Important notes
- The zero active-power statement applies to the ideal pure inductance used in this section; a practical coil may also contain resistance.

### Check yourself
1. **How does inductive reactance vary with frequency?**
   - X_L = 2πfL, so it increases directly with frequency.
2. **What is the phase relation in a pure inductor?**
   - Current lags voltage by 90°.
3. **Why does an ideal pure inductor consume no average active power?**
   - Instantaneous power alternates positive and negative as energy is stored in the magnetic field and then returned to the source, so the average over a complete cycle is zero.

### Physical-book reference
- pp. 90–93; source image(s): 90.png–93.png

**Topic provenance:** `[SYL-R25-U2]` `[TB-P090]` `[TB-P091]` `[TB-P092]` `[TB-P093]`

## Single-phase AC through pure capacitance

**Status:** Core R25

### Quick recall
- For an ideal pure capacitor, current leads voltage by 90° and the capacitive reactance is X_C = 1/(ωC).
- Its impedance is −jX_C and its power factor is zero.
- An ideal capacitor consumes no average active power; it alternately stores and returns electric-field energy.

### Deriving the current phase
For a capacitor, q = Cv and i = dq/dt = C dv/dt. With v = V_m sinωt, differentiation gives i = ωCV_m cosωt = I_m sin(ωt + 90°). Hence current leads voltage by 90°.

**Section provenance:** `[TB-P093]` `[TB-P094]`

### Capacitive reactance
Since I_m = ωCV_m, the ratio V_m/I_m is 1/(ωC). This quantity is capacitive reactance X_C. Because X_C = 1/(2πfC), capacitive reactance decreases as frequency increases.

- At f = 0 (steady DC), X_C tends to infinity.
- An ideal capacitor therefore behaves as an open circuit in DC steady state.

**Section provenance:** `[TB-P094]` `[TB-P095]`

### Impedance and power factor
The impedance is Z = −jX_C, corresponding to a −90° impedance angle. Current leads voltage by 90°, so the ideal capacitive power factor is zero.

**Section provenance:** `[TB-P095]`

### Power exchange in a pure capacitor
As in the pure inductor, instantaneous power alternates sign and its average over a full cycle is zero. Energy is exchanged between the source and the capacitor's electric field rather than being continuously consumed as active power.

**Section provenance:** `[TB-P094]` `[TB-P095]`

### Formula anchors
- `i = C·dv/dt`
- `X_C = 1/(ωC) = 1/(2πfC)`
- `Z_C = −jX_C`
- `I_m = V_m/X_C`
- `Ideal C: current leads voltage by 90°`
- `Power factor = 0`
- `Average active power = 0`

### Check yourself
1. **How does capacitive reactance vary with frequency?**
   - X_C = 1/(2πfC), so it decreases as frequency increases.
2. **What is the phase relation in a pure capacitor?**
   - Current leads voltage by 90°.
3. **What does an ideal capacitor look like at steady DC?**
   - Since f = 0 makes X_C infinite, it behaves as an open circuit in DC steady state.

### Physical-book reference
- pp. 93–95; source image(s): 93.png–95.png

**Topic provenance:** `[SYL-R25-U2]` `[TB-P093]` `[TB-P094]` `[TB-P095]`

## Series RL circuit

**Status:** Core R25

### Quick recall
- In a series RL circuit the same current flows through R and L; V_R is in phase with current and V_L leads current by 90°.
- The supply voltage is the phasor sum V_R + jV_L, giving Z = R + jX_L and |Z| = √(R² + X_L²).
- Current lags the supply voltage by φ, with cosφ = R/|Z|; the circuit therefore has a lagging power factor.

### Building the phasor diagram
Because R and L are in series, current is common to both elements and is chosen as the reference phasor. The resistor drop V_R = IR lies along the current axis. The inductor drop V_L = IX_L is 90° ahead of current. Their vector sum is the applied voltage.

**Section provenance:** `[TB-P096]` `[TB-P097]`

### Impedance triangle
From V = V_R + jV_L and division by the common current, Z = R + jX_L. Geometrically R is the horizontal side, X_L the positive quadrature side and |Z| the hypotenuse.

- |Z| = √(R² + X_L²).
- cosφ = R/|Z|.
- tanφ = X_L/R.
- Since φ is positive for the inductive reactance, current lags voltage by φ.

**Section provenance:** `[TB-P097]` `[TB-P098]`

### Power in a series RL circuit
The applied voltage can be resolved into an in-phase component associated with R and a quadrature component associated with L. Accordingly, AC power separates into active power P, reactive power Q and apparent power S.

- P = VI cosφ is the real/active power consumed.
- Q = VI sinφ is the inductive reactive power.
- S = VI is the apparent-power magnitude.
- The power triangle has P on the horizontal axis, +Q vertically and S as the hypotenuse.

**Section provenance:** `[TB-P098]`

### Standard RL numerical workflow
The book's worked problems repeatedly follow the same sequence: obtain ω from the supply frequency, calculate X_L, form Z, find |Z| and φ, calculate current, then calculate element voltages and powers. This is the safest order for exam problems because each result feeds the next.

**Section provenance:** `[TB-P102]` `[TB-P103]` `[TB-P106]` `[TB-P107]`

### Formula anchors
- `X_L = 2πfL`
- `Z = R + jX_L`
- `|Z| = √(R² + X_L²)`
- `tanφ = X_L/R`
- `Power factor = cosφ = R/|Z| (lagging)`
- `I = V/|Z|`
- `V_R = IR`
- `V_L = IX_L`
- `P = VI cosφ`
- `Q = VI sinφ`
- `S = VI = √(P²+Q²)`

### Problem-solving method
1. Calculate X_L = 2πfL.
2. Write Z = R + jX_L and calculate |Z|.
3. Find φ from tanφ = X_L/R or cosφ = R/|Z|.
4. Calculate I = V/|Z| using RMS values unless the problem explicitly gives peaks.
5. Find V_R = IR and V_L = IX_L.
6. Calculate P, Q and S if required and state that the power factor is lagging.

### Important notes
- Do not add V_R and V_L arithmetically; they are 90° apart and must be combined as phasors.

### Check yourself
1. **Why is current used as the reference in a series RL phasor diagram?**
   - The same current flows through both series elements. V_R is in phase with that current and V_L leads it by 90°, making the voltage phasors easy to construct.
2. **What makes the RL power factor lagging?**
   - The net impedance has positive inductive reactance, so the supply voltage leads the common current by φ; equivalently, current lags voltage.
3. **How are R, X_L and |Z| related?**
   - They form a right-angled impedance triangle: |Z| = √(R² + X_L²), with cosφ = R/|Z| and tanφ = X_L/R.

### Physical-book reference
- pp. 96–98, 102–103, 106–107; source image(s): 96.png–98.png, 102.png–103.png, 106.png–107.png — RL derivation, power triangle and worked examples

**Topic provenance:** `[SYL-R25-U2]` `[TB-P096]` `[TB-P097]` `[TB-P098]` `[TB-P102]` `[TB-P103]` `[TB-P106]` `[TB-P107]`

## Series RC circuit

**Status:** Core R25

### Quick recall
- In a series RC circuit the common current is in phase with V_R and leads V_C by 90°; equivalently V_C lags current by 90°.
- The supply impedance is Z = R − jX_C and |Z| = √(R² + X_C²).
- Current leads the supply voltage, so the circuit has a leading power factor.

### Building the RC phasor diagram
Current is common to the series elements and is taken as the reference. V_R lies along the current axis. The capacitive voltage V_C is 90° behind current, so it is drawn on the negative quadrature axis. The supply voltage is the vector sum V_R − jV_C.

**Section provenance:** `[TB-P098]` `[TB-P099]`

### Impedance and phase
Dividing the supply-voltage phasor by current gives Z = R − jX_C. Its magnitude is √(R² + X_C²). The negative reactive component places the supply voltage behind current, so current leads the supply by angle φ.

- cosφ = R/|Z|.
- |tanφ| = X_C/R.
- The power factor is described as leading.

**Section provenance:** `[TB-P099]` `[TB-P100]`

### Power in a series RC circuit
Real power is associated with the resistor and remains P = VI cosφ. The capacitive reactive component has the opposite sign to the inductive case, so complex power is written S = P − jQ for the capacitive circuit.

**Section provenance:** `[TB-P100]`

### Using time displacement to find phase
One worked example gives the time by which voltage lags current. Since one complete period represents 360°, a measured time displacement Δt corresponds to φ = (Δt/T)×360°. This provides an alternative route to the phase angle before calculating power factor and impedance.

**Section provenance:** `[TB-P109]` `[TB-P110]`

### Formula anchors
- `X_C = 1/(2πfC)`
- `Z = R − jX_C`
- `|Z| = √(R² + X_C²)`
- `Power factor = cosφ = R/|Z| (leading)`
- `I = V/|Z|`
- `V_R = IR`
- `V_C = IX_C`
- `P = VI cosφ`
- `Capacitive complex power shown as S = P − jQ`

### Problem-solving method
1. Calculate X_C = 1/(2πfC).
2. Write Z = R − jX_C and calculate |Z|.
3. Find the magnitude of φ using R and X_C; state that current leads voltage.
4. Calculate I = V/|Z|.
5. Find V_R = IR and V_C = IX_C.
6. If the phase is given as a time displacement, first calculate T = 1/f and convert the time shift into degrees.

### Important notes
- The capacitive reactive component has the opposite sign to the inductive one; do not label a series RC power factor as lagging.

### Check yourself
1. **In a series RC circuit, which quantity leads: current or supply voltage?**
   - Current leads the supply voltage. V_R is in phase with current while V_C is 90° behind current.
2. **Why does Z contain −jX_C?**
   - The capacitive voltage is on the negative quadrature axis relative to the current reference, so the reactive part of the impedance is negative.
3. **How can a time lead/lag be converted to phase angle?**
   - Find T = 1/f, then φ = (Δt/T)×360° for a complete cycle of 360°.

### Physical-book reference
- pp. 98–100, 108–110; source image(s): 98.png–100.png, 108.png–110.png — RC phasor/impedance triangles and numerical examples

**Topic provenance:** `[SYL-R25-U2]` `[TB-P098]` `[TB-P099]` `[TB-P100]` `[TB-P108]` `[TB-P109]` `[TB-P110]`

## Series RLC circuit and resonance

**Status:** Core R25

### Quick recall
- For a series RLC circuit, the net reactance is X_L − X_C and Z = R + j(X_L − X_C).
- If X_L > X_C the circuit is inductive and current lags; if X_L < X_C it is capacitive and current leads; if X_L = X_C the circuit is purely resistive with unity power factor.
- The unity-power-factor condition X_L = X_C is series resonance, with f_r = 1/(2π√LC).

### Phasor construction
The same current flows through R, L and C and is used as the reference. V_R is in phase with current, V_L is +90° and V_C is −90°. Because V_L and V_C are opposite, the net quadrature voltage is V_L − V_C.

**Section provenance:** `[TB-P100]` `[TB-P101]`

### Impedance of the series RLC circuit
The supply voltage is V = V_R + j(V_L − V_C). Dividing by the common current gives Z = R + j(X_L − X_C). The magnitude is √[R² + (X_L − X_C)²].

**Section provenance:** `[TB-P101]` `[TB-P102]`

### Three possible operating cases
- If X_L > X_C: net reactance is inductive, current lags voltage and power factor is lagging.
- If X_L < X_C: net reactance is capacitive, current leads voltage and power factor is leading.
- If X_L = X_C: net reactance is zero, Z = R, current and voltage are in phase and power factor is unity.

**Section provenance:** `[TB-P101]` `[TB-P102]`

### Series resonance
*Supporting context within the supplied corpus; not a separate R25 syllabus atom.*

The condition X_L = X_C is called series resonance, and the corresponding frequency is the resonant frequency. R25 names series RLC analysis but does not separately list resonance, so this is retained as a useful extension within the RLC topic rather than as a separate syllabus topic.

- At resonance, 2πfL = 1/(2πfC).
- Therefore f_r = 1/(2π√LC).
- At resonance, Z = R and the current magnitude is V/R.
- Power factor is unity because the net reactance is zero.

**Section provenance:** `[TB-P111]` `[TB-P112]`

### Worked-problem pattern
A reliable RLC problem sequence is to calculate X_L and X_C separately, take their difference, then calculate impedance magnitude, current, power factor and the individual element voltages. Even when V_L and V_C are individually large, only their phasor difference contributes to the supply's reactive voltage.

**Section provenance:** `[TB-P104]` `[TB-P105]` `[TB-P111]` `[TB-P112]`

### Steady-state RLC response through phasors
*Supporting context within the supplied corpus; not a separate R25 syllabus atom.*

Once the transient part has died away, each sinusoidal steady-state branch quantity can be represented by a complex amplitude at the excitation frequency and solved algebraically with phasors.

Second-order transient classification is outside the R25 Unit II scope; only the steady-state/forced-response viewpoint is retained here.

**Section provenance:** `[LEC-U2-02]` `[LEC-U2-05]` `[LEC-U2-06]` `[LEC-U2-07]` `[LEC-U2-09]`

### Formula anchors
- `Z = R + j(X_L − X_C)`
- `|Z| = √[R² + (X_L − X_C)²]`
- `Power factor = R/|Z|`
- `At resonance: X_L = X_C`
- `f_r = 1/(2π√LC)`
- `At resonance: Z = R, I = V/R, power factor = 1`

### Problem-solving method
1. Calculate X_L = 2πfL and X_C = 1/(2πfC).
2. Form the net reactance X = X_L − X_C.
3. Write Z = R + jX and calculate |Z|.
4. Use the sign of X to decide whether the circuit is inductive (lagging) or capacitive (leading).
5. Calculate I = V/|Z| and then V_R = IR, V_L = IX_L and V_C = IX_C.
6. For unity-power-factor/resonance questions, set X_L = X_C and solve for the unknown frequency, L or C.

### Important notes
- V_L and V_C are 180° opposed on the reactive axis. The supply voltage is based on V_L − V_C, not V_L + V_C.
- Resonance is present in the prescribed chapter but is not separately named as an R25 Unit-II syllabus atom.

### Check yourself
1. **How do you decide whether a series RLC circuit is inductive or capacitive?**
   - Compare X_L and X_C. If X_L > X_C, net reactance is positive and the circuit is inductive; if X_L < X_C, net reactance is negative and the circuit is capacitive.
2. **What happens at series resonance?**
   - X_L = X_C, so the reactive parts cancel, Z = R, current and voltage are in phase, and the power factor is unity.
3. **Why can V_L and V_C each exceed the supply voltage in an RLC circuit without being added directly?**
   - Their phasors point in opposite quadrature directions. Only their difference V_L − V_C contributes to the net reactive part of the supply voltage.

### Physical-book reference
- pp. 100–112; source image(s): 100.png–112.png — RLC analysis, worked examples and series resonance

**Topic provenance:** `[SYL-R25-U2]` `[TB-P100]` `[TB-P101]` `[TB-P102]` `[TB-P103]` `[TB-P104]` `[TB-P105]` `[TB-P106]` `[TB-P107]` `[TB-P108]` `[TB-P109]` `[TB-P110]` `[TB-P111]` `[TB-P112]` `[LEC-U2-02]` `[LEC-U2-05]` `[LEC-U2-06]` `[LEC-U2-07]` `[LEC-U2-09]`

## Real, reactive and apparent power; power factor

**Status:** Core R25

### Quick recall
- Power factor is the cosine of the phase angle between voltage and current.
- Real or active power P is the in-phase power that is actually consumed; reactive power Q represents the quadrature exchange associated with ideal inductive/capacitive behaviour; apparent power S is the product of RMS voltage and current.
- For a sinusoidal single-phase circuit, P = VI cosφ, Q = VI sinφ and |S| = VI = √(P² + Q²), with the sign/direction of reactive power distinguishing inductive and capacitive cases.

### Power factor
Power factor is cosφ, where φ is the phase angle between the voltage and current phasors. It is unity for a pure resistance and zero for ideal pure L or C. In mixed circuits, the sign of the reactive part determines whether the power factor is described as lagging or leading.

**Section provenance:** `[TB-P090]` `[TB-P092]` `[TB-P095]` `[TB-P098]` `[TB-P100]`

### Real or active power P
Real power is associated with the component of current in phase with voltage. It represents net energy transferred from the source and consumed by the load. For a sinusoidal single-phase circuit using RMS values, P = VI cosφ.

**Section provenance:** `[TB-P090]` `[TB-P098]` `[TB-P100]`

### Reactive power Q
Reactive power corresponds to the quadrature component and represents periodic energy exchange rather than net consumption over a full cycle. The inductive case uses the positive reactive direction; the capacitive case uses the opposite sign.

**Section provenance:** `[TB-P093]` `[TB-P095]` `[TB-P098]` `[TB-P100]`

### Apparent power S and the power triangle
Apparent power is the product of RMS voltage and RMS current. In the power triangle, P and Q are perpendicular components and S is the hypotenuse, so |S| = √(P² + Q²).

- Active power is expressed in W or kW.
- Reactive power is expressed in VAR or kVAR.
- Apparent power is expressed in VA or kVA.

**Section provenance:** `[TB-P098]` `[TB-P100]`

### How R, L and C affect power
- Pure R: voltage and current in phase, power factor 1, active power consumed.
- Pure L: current lags 90°, power factor 0, zero average active power, reactive exchange.
- Pure C: current leads 90°, power factor 0, zero average active power, reactive exchange in the opposite sense.
- Series RL: lagging power factor.
- Series RC: leading power factor.
- Series RLC: lagging, leading or unity depending on X_L − X_C.

**Section provenance:** `[TB-P090]` `[TB-P092]` `[TB-P093]` `[TB-P095]` `[TB-P098]` `[TB-P100]` `[TB-P102]`

### Formula anchors
- `Power factor = cosφ`
- `P = VI cosφ`
- `Q = VI sinφ`
- `|S| = VI`
- `|S| = √(P² + Q²)`

### Problem-solving method
1. Find the phase angle or power factor from the circuit impedance.
2. Use RMS voltage and current in the power formulas.
3. Calculate P = VI cosφ.
4. Calculate Q = VI sinφ, keeping the inductive/capacitive sign convention clear.
5. Calculate apparent power S = VI and verify |S|² = P² + Q².

### Important notes
- Power factor is not the same thing as efficiency; in these notes it is specifically cosφ, the phase relation between voltage and current.

### Check yourself
1. **What is the difference between real, reactive and apparent power?**
   - Real power P = VI cosφ is the net consumed component; reactive power Q = VI sinφ is the quadrature exchange; apparent power |S| = VI is the RMS volt-ampere product and is the hypotenuse of the power triangle.
2. **Which circuits have lagging and leading power factor?**
   - Inductive circuits such as series RL are lagging; capacitive circuits such as series RC are leading. A pure resistance and a series RLC circuit at resonance have unity power factor.
3. **What units are used for P, Q and S?**
   - W (or kW) for active power, VAR (or kVAR) for reactive power, and VA (or kVA) for apparent power.

### Physical-book reference
- pp. 90, 92–93, 95, 98, 100, 102, 106, 117, 119; source image(s): 90.png, 92.png–93.png, 95.png, 98.png, 100.png, 102.png, 106.png, 117.png, 119.png

**Topic provenance:** `[SYL-R25-U2]` `[TB-P090]` `[TB-P092]` `[TB-P093]` `[TB-P095]` `[TB-P098]` `[TB-P100]` `[TB-P102]` `[TB-P106]` `[TB-P117]` `[TB-P119]`

## Three-phase balanced circuits: star and delta

**Status:** Core R25

### Quick recall
- A balanced three-phase set consists of three equal-magnitude, equal-frequency sinusoidal phase quantities displaced by 120°.
- In star connection, V_L = √3V_ph and I_L = I_ph; the line voltage leads the corresponding phase voltage by 30°.
- In delta connection, V_L = V_ph and I_L = √3I_ph; the line current lags the corresponding phase current by 30°.
- For a balanced three-phase load, P = √3V_LI_L cosφ, Q = √3V_LI_L sinφ and S = √3V_LI_L.

### Why three-phase systems are used
Three-phase systems are widely used for generating and transmitting large amounts of power because they offer economic and operational advantages and allow compact, efficient equipment for a given power rating.

**Section provenance:** `[TB-P112]`

### Balanced three-phase set
A three-phase system contains three sinusoidal phase voltages or currents having the same frequency and, in the balanced case, the same magnitude, with successive phases displaced by 120°. Taking phase a as the reference, the three phase voltages may be represented at 0°, −120° and −240°.

**Section provenance:** `[TB-P112]` `[TB-P113]`

### Phase sequence
Phase sequence is the order in which the phase quantities reach corresponding positions such as their positive maxima. For the sequence abc, phase a reaches the reference position first, followed by b and then c. Reversing the order changes the phase sequence.

**Section provenance:** `[TB-P113]`

### Star connection: physical arrangement
In star connection, similar-polarity ends of the three phase windings are joined to a common neutral or star point. The other three ends form the line terminals. With the neutral brought out, the arrangement forms a four-wire three-phase system.

- Phase voltage V_ph is the voltage from a line to the neutral point.
- Line voltage V_L is the voltage between two line conductors.
- Line current equals phase current because each line is in series with its phase: I_L = I_ph.

**Section provenance:** `[TB-P114]` `[TB-P115]` `[TB-P116]`

### Star connection: derivation of line voltage
For example, V_ab = V_a − V_b. The two phase-voltage phasors have equal magnitude and are 120° apart. A phasor/parallelogram construction gives the magnitude of their difference.

- |V_ab| = √(V_ph² + V_ph² + 2V_ph² cos60°) = √3V_ph.
- The other line voltages have the same magnitude: V_bc = V_ca = √3V_ph.
- The line voltages remain mutually displaced by 120°.
- Each line voltage leads its corresponding phase voltage by 30°.

**Section provenance:** `[TB-P115]` `[TB-P116]`

### Power in a balanced star-connected load
Power per phase is V_ph I_ph cosφ. For three equal phases, total active power is 3V_phI_ph cosφ. Using V_L = √3V_ph and I_L = I_ph gives the line-value form P = √3V_LI_L cosφ. The same substitution gives the corresponding Q and S relations.

**Section provenance:** `[TB-P116]` `[TB-P117]`

### Delta connection: physical arrangement
In delta connection, dissimilar-polarity ends of the three phases are joined to form a closed loop. The three junctions become the line terminals, and the basic delta connection has no neutral point.

- Each phase is connected directly between two lines.
- Therefore phase voltage equals line voltage: V_ph = V_L.

**Section provenance:** `[TB-P117]`

### Delta connection: derivation of line current
The line current at a junction is the phasor difference of the two phase currents meeting there. Relations such as I_A(line) = I_A − I_C lead, by the parallelogram law, to the line/phase-current magnitude relation.

- For equal phase currents separated by 120°, the magnitude of the difference is √3I_ph.
- Thus I_L = √3I_ph.
- The line currents remain mutually displaced by 120°.
- Each line current lags its corresponding phase current by 30°.

**Section provenance:** `[TB-P118]` `[TB-P119]`

### Power in a balanced delta-connected load
Total power is again three times the per-phase power. Substituting V_L = V_ph and I_L = √3I_ph produces the same line-value formula used for star connection.

- P = √3V_LI_L cosφ.
- Q = √3V_LI_L sinφ.
- S = √3V_LI_L.

**Section provenance:** `[TB-P119]`

### Star versus delta: quick comparison
- Star: V_L = √3V_ph; I_L = I_ph; a neutral point is available.
- Delta: V_L = V_ph; I_L = √3I_ph; the three phases form a closed loop with no neutral in the basic connection.
- Star line voltage leads corresponding phase voltage by 30°.
- Delta line current lags corresponding phase current by 30°.
- Balanced three-phase active/reactive/apparent-power formulas in line quantities have the same √3V_LI_L form for both connections.

**Section provenance:** `[TB-P114]` `[TB-P116]` `[TB-P117]` `[TB-P119]`

### Balanced-load problem strategy
The worked examples from pp.119–128 repeatedly convert line quantities to phase quantities, solve one phase using its impedance, convert back to line current where necessary and then calculate total three-phase power.

- For star: first obtain V_ph = V_L/√3 and use I_L = I_ph.
- For delta: use V_ph = V_L and then I_L = √3I_ph.
- For a per-phase impedance R + jX, find |Z| and cosφ = R/|Z| before calculating current and total power.

**Section provenance:** `[TB-P119]` `[TB-P120]` `[TB-P121]` `[TB-P122]` `[TB-P123]` `[TB-P124]` `[TB-P125]` `[TB-P126]` `[TB-P127]` `[TB-P128]`

### Formula anchors
- `Balanced phases: equal magnitude and frequency, 120° apart`
- `Star: V_L = √3V_ph`
- `Star: I_L = I_ph`
- `Delta: V_L = V_ph`
- `Delta: I_L = √3I_ph`
- `Balanced 3φ active power: P = √3V_LI_L cosφ`
- `Balanced 3φ reactive power: Q = √3V_LI_L sinφ`
- `Balanced 3φ apparent power: S = √3V_LI_L`

### Problem-solving method
1. Identify whether the load is star or delta.
2. Convert the given line voltage to phase voltage: star V_ph = V_L/√3; delta V_ph = V_L.
3. Calculate the per-phase impedance and phase current.
4. Convert phase current to line current: star I_L = I_ph; delta I_L = √3I_ph.
5. Find cosφ from the per-phase impedance.
6. Use P = √3V_LI_L cosφ and the analogous Q and S formulas for total balanced three-phase power.

### Important notes
- R25 explicitly asks for the voltage/current relations in star and delta as derivations. Do not reduce these to formulas alone when preparing a six-mark answer.
- Keep line and phase quantities distinct; using V_L directly as V_ph in a star problem or using I_L directly as I_ph in a delta problem gives the wrong result.

### Check yourself
1. **What makes a three-phase system balanced?**
   - The three phase quantities have equal magnitude and frequency and are displaced from one another by 120°.
2. **What are the star line/phase relations?**
   - V_L = √3V_ph and I_L = I_ph. The line voltage leads the corresponding phase voltage by 30°.
3. **What are the delta line/phase relations?**
   - V_L = V_ph and I_L = √3I_ph. The line current lags the corresponding phase current by 30°.
4. **What is the total active power of a balanced three-phase load in line quantities?**
   - P = √3V_LI_L cosφ, for either star or delta once the correct line quantities are used.

### Physical-book reference
- pp. 112–128; source image(s): 112.png–128.png — balanced three-phase system, phase sequence, star/delta derivations and worked problems

**Topic provenance:** `[SYL-R25-U2]` `[TB-P112]` `[TB-P113]` `[TB-P114]` `[TB-P115]` `[TB-P116]` `[TB-P117]` `[TB-P118]` `[TB-P119]` `[TB-P120]` `[TB-P121]` `[TB-P122]` `[TB-P123]` `[TB-P124]` `[TB-P125]` `[TB-P126]` `[TB-P127]` `[TB-P128]`

## Chapter-end review

- Prescribed textbook review page: p.129 (`129.png`).
- 11 short-answer (two-mark) questions.
- 6 essay (six-mark) questions.
- Structured answer bank: `kb/data/textbook-questions.json`.
