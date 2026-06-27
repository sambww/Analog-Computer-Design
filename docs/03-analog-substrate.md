# 03 — The Analog Substrate

> **Status of this document:** This is the most speculative document in the repository. The
> *lineage* is `[ESTABLISHED]`; the *unified programmable medium* it builds toward is firmly
> `[SPECULATIVE]`. Every leap is paired with the real principle it extends.

---

## 1. The lineage (so the leap is traceable)

The substrate is an extrapolation along a real, century-long line of analog computing. Each
prior art demonstrates one capability the Continuum Engine needs; the speculation is in
*unifying and scaling* them, not in inventing physics from nothing.

| Prior art | What it proves `[ESTABLISHED]` | What it lacks |
|-----------|-------------------------------|---------------|
| **Op-amp analog computers** (1940s–70s) | Continuous integration/differentiation; solving ODEs by direct physical analogy | Hand-patched, fixed-function, drift-prone |
| **Analog VLSI / neuromorphic** (Mead, 1980s–) | Massive parallel analog compute in silicon; physics-as-computation at scale | Limited precision, hard to reconfigure |
| **Memristor crossbars** | In-memory analog matrix–vector multiply; co-located memory+compute | Device variability, endurance |
| **Photonic / optical mesh** | Matrix multiply at light speed, near-zero static energy, huge bandwidth | Bulky modulators, limited nonlinearity |
| **Physical reservoir computing** | *Any* sufficiently rich nonlinear medium can compute if read out cleverly | Not directly programmable; fixed dynamics |
| **Ising machines / analog annealers** | Optimization by physical energy minimization | Embedding overhead, limited connectivity |
| **Thermodynamic / probabilistic computing** | Sampling and inference driven *by* thermal noise | Early-stage, small scale |

The pattern across all of these: **state and computation are co-located, dynamics are
continuous and parallel, and the answer is the medium's natural behavior.** The Continuum
Engine asks: *what if one reconfigurable medium did all of this at once?*

---

## 2. The speculative core: a Programmable Continuous Field (PCF)

`[SPECULATIVE]` The substrate is a **Programmable Continuous Field** — a dense, reconfigurable
physical medium supporting a continuous field of state with locally programmable dynamics.
Think of it as the limit of a memristor crossbar, a photonic mesh, and a neuromorphic array
fused into one substance whose *local rules* can be set by the field fabric.

Three properties define it:

1. **Continuous state.** State is represented by continuous physical quantities (e.g., field
   amplitude/phase, charge density, oscillator phase) across a spatial continuum, not by bits.
   `[ESTABLISHED]` basis: every analog medium above. `[SPECULATIVE]` extension: the density and
   addressability assumed here exceed current devices.

2. **Programmable local dynamics.** At each location, the *law* governing evolution —
   effective stiffness, coupling to neighbors, nonlinearity, gain/loss — is set by the field
   fabric (Doc 02-B). This is what makes one medium able to embody many problems. `[ESTABLISHED]`
   basis: FPAAs and photonic phase-shifters do this in limited form; `[SPECULATIVE]`: doing it
   densely, continuously, and at scale.

3. **Native operations as physics.** The medium does not *execute* operations; it *exhibits*
   them. The primitives below fall out of the physics for free.

---

## 3. Native operations (computation = physics)

These are the substrate's "instruction set," except none of them are instructions — they are
behaviors of the medium under particular configurations.

- **Integration / differentiation over time.** A continuous-state variable that accumulates is
  an integrator; ODE solving is direct, not stepped. `[ESTABLISHED]` (op-amp integrators).
- **Matrix–vector multiply.** A configured coupling array maps an input field to an output
  field in a single physical pass, in O(1) time regardless of matrix size — the cost is paid in
  parallel hardware, not in sequential operations. `[ESTABLISHED]` (crossbars, photonic mesh).
- **Smooth nonlinearity.** Saturation, thresholding, and activation arise from the medium's
  intrinsic nonlinear response. `[ESTABLISHED]` (analog VLSI transfer curves).
- **Energy minimization / relaxation.** Configure the couplings so the problem's cost function
  *is* the medium's energy; release it and it descends to a minimum. `[ESTABLISHED]` (Hopfield,
  Ising machines).
- **Stochastic sampling.** Add calibrated thermal/shot noise and the medium samples from a
  distribution rather than settling to a point — native Monte Carlo / Bayesian inference.
  `[ESTABLISHED]` (Langevin dynamics, thermodynamic computing).
- **Spatiotemporal transformation.** Wave propagation, diffusion, and convolution happen
  intrinsically as the field evolves. `[ESTABLISHED]` (optical convolution, reaction–diffusion).

A "program," then, is a **configuration that composes these behaviors** so the medium's
natural evolution lands on the answer (formalized in Doc 05).

---

## 4. State representation and readout

- **Encoding.** Variables map to continuous physical quantities: amplitude, phase, charge, or
  oscillator frequency. Vectors and matrices map to spatial patterns and coupling arrays.
- **Co-located memory.** There is no separate memory. The medium's present physical state *is*
  the working memory; persistence is achieved by configurable retention (cf. memristor
  non-volatility). `[ESTABLISHED]` framing (in-memory computing); `[SPECULATIVE]` scale.
- **Readout.** Sensors transduce the continuous state back to the digital shell via ADCs
  (Doc 07). Readout is a measurement and therefore has finite precision and adds noise — a
  first-class design constraint, not an afterthought.

---

## 5. The honest gaps — what must be invented

This substrate does not exist. The specific `[SPECULATIVE]` leaps, isolated so they are easy
to attack, are:

1. **A dense medium with programmable local dynamics** at a scale and addressability far beyond
   today's FPAAs or photonic meshes.
2. **Reconfiguration that is both fine-grained and fast** without destroying the co-located
   state.
3. **Stable, calibratable analog behavior** at room temperature with manageable drift — the
   perennial enemy of analog computing.
4. **High-density, low-noise readout** that does not dominate the energy or error budget.

Doc 08 lays these out as named open problems with the breakthroughs each requires. Nothing
here violates known physics; everything here exceeds known engineering. That is the deliberate
boundary of this design.

→ Continue to **[04 — The AI Agent Layer](./04-ai-agent-layer.md)**.
