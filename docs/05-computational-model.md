# 05 — The Computational Model

> **Status of this document:** The mathematical framing (variational/energy methods, dynamical
> systems) is `[ESTABLISHED]`. Its realization on the PCF substrate is `[SPECULATIVE]`.

---

## 1. What is a "program" here?

On a digital computer, a program is a *sequence of instructions*. On the Continuum Engine, a
program is a **physical setup whose natural evolution produces the answer**. Concretely, a
program is the triple:

```
  PROGRAM  =  ( objective functional J ,  constraints C ,  readout map R )
```

- **Objective functional `J`** — a function of the substrate's continuous state whose minimum
  (or whose equilibrium distribution) encodes the solution. The agent layer configures the
  fabric so that the medium's physical energy *is* `J`.
- **Constraints `C`** — boundary conditions, fixed inputs, and feasibility regions, imposed by
  clamping parts of the field or biasing couplings.
- **Readout map `R`** — how settled physical state is interpreted back into the answer.

"Running the program" means: impose `C`, release the medium so it descends `J` (or samples
`exp(−J/T)`), then apply `R`. There is no instruction counter. **The dynamics are the
execution.**

---

## 2. The two fundamental execution modes

Almost everything the machine does is one of two physical behaviors:

### Mode 1 — Relaxation (find the minimum)
Configure couplings so that `J` is the medium's energy; release; the system descends to a
(local or global) minimum. With a noise/anneal schedule, it escapes local minima and
approaches the global optimum. `[ESTABLISHED]`: gradient flows, Hopfield networks, Ising
machines, analog annealing.

```
   J(state)
     \                   release → physics descends J
      \    .-.          ───────────────────────────────►   settled state = argmin J
       \  /   \   ___
        \/     \_/   \____•   ← global minimum (the answer)
```

Used for: optimization, constraint satisfaction, equilibrium problems, MAP inference.

### Mode 2 — Evolution (follow the dynamics)
Configure the medium so its governing equation *is* the problem's dynamics; let it run forward
in continuous time and read the trajectory or final state. `[ESTABLISHED]`: op-amp ODE solvers,
wave/diffusion media, reservoir computing.

Used for: simulating physical systems, solving ODEs/PDEs, time-series transformation.

A third mode, **Sampling**, is Mode 1 run *with* sustained calibrated noise so the medium
visits states with probability `∝ exp(−J/T)` instead of settling — giving native Monte Carlo /
Bayesian inference. `[ESTABLISHED]`: Langevin/thermodynamic sampling.

---

## 3. Mapping problem classes onto the model

| Problem class | Native mode | How it maps |
|---------------|-------------|-------------|
| **Continuous optimization** | Relaxation | Cost → energy; minimum → solution |
| **Combinatorial optimization** | Relaxation + anneal | Embed as Ising/QUBO energy; anneal noise down |
| **ODE / PDE simulation** | Evolution | Substrate dynamics ≡ problem dynamics; read trajectory |
| **Linear algebra (Ax=b, eigen)** | Relaxation / Evolution | Solution as energy minimum or steady state of a configured network |
| **Neural inference** | Evolution | Matrix–vector multiply + nonlinearity as a single physical pass |
| **Probabilistic inference / sampling** | Sampling | Posterior → energy; thermal noise → samples |
| **Search / association** | Relaxation | Content-addressable energy landscape (attractor = match) |

The common thread: each class reduces to *building a landscape* or *matching dynamics*, both
of which the substrate does in parallel, in physical time, with no per-operation overhead.

---

## 4. The performance intuition (why it can be so much faster)

For a problem with `N` interacting variables:

- **Digital** evaluates interactions essentially sequentially (modulo cores); a single
  relaxation step can cost on the order of `N` to `N²` operations, repeated over many
  iterations. Energy and time scale with that operation count.
- **Continuum Engine** lets all `N` variables interact *simultaneously* as one physical event.
  The "step" is paid in parallel hardware and physical settling time, not in a growing
  operation count. For the right problems this is the difference between *computing* the
  interaction and *being* the interaction.

This is an intuition, not a universal speedup theorem — it holds for problems that *fit the
substrate and its connectivity*. Embedding cost, readout precision, and the outer control loop
all eat into the advantage; Doc 06 accounts for them honestly.

---

## 5. What this model does **badly** (on purpose, stated plainly)

The model is powerful exactly where digital is weak, and weak exactly where digital is strong:

- **Exact discrete arithmetic.** Continuous media give approximate, noisy values. Bit-exact
  integer math, cryptographic operations, and anything requiring perfect reproducibility belong
  on the digital shell. `[ESTABLISHED]` limitation.
- **Long deterministic instruction sequences.** Control-flow-heavy, branchy logic has no
  natural "landscape." Keep it digital.
- **Unbounded precision.** Analog precision is limited by noise and readout (Doc 07). You buy
  precision through the approximate-and-verify loop, and it is never free.
- **Problems that don't fit the connectivity.** If a problem's interaction graph can't be
  embedded in the fabric without huge overhead, the advantage evaporates.

The design's stance (tenet 5 and 8): **use the analog core for what it is uniquely good at,
hand the rest to digital, and never disguise one as the other.**

→ Continue to **[06 — Comparison vs. Digital](./06-comparison-vs-digital.md)**.
