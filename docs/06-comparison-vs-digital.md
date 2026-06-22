# 06 — Comparison vs. Digital

> **Status of this document:** The digital-side facts are `[ESTABLISHED]`. The analog-side
> figures are *targets* implied by the lineage in Doc 03 and are `[SPECULATIVE]` until the
> substrate exists. This document deliberately bounds the superiority claims rather than
> stating them absolutely.

---

## 1. The core structural difference

A digital computer separates memory from compute and processes one (or a few) instructions per
clock. Its dominant cost today is **moving data** across that separation — the von Neumann
bottleneck — and the **energy per operation** floor. `[ESTABLISHED]`.

The Continuum Engine **co-locates state and compute** and lets an entire problem evolve as a
single physical event. There is no instruction stream and no fetch–decode–execute loop. For
problems that fit its substrate, this removes the two costs digital is most limited by.

That is the whole thesis in one sentence: **digital simulates the problem; the Continuum
Engine becomes it.**

---

## 2. Head-to-head table

| Dimension | Digital computer `[ESTABLISHED]` | Continuum Engine (target) `[SPECULATIVE]` |
|-----------|----------------------------------|-------------------------------------------|
| **Compute model** | Sequential instructions over discrete state | Continuous physical dynamics; relax/evolve/sample |
| **Memory ↔ compute** | Separated (von Neumann bottleneck) | Co-located in the medium — no fetch |
| **Parallelism** | Cores × SIMD lanes (thousands) | The whole field at once (problem-wide, physical) |
| **Clocking** | Fixed clock; perf ∝ clock × IPC | No instruction clock; perf ∝ physical settling time |
| **Energy/op** | Bounded by switching + data movement | Potentially orders lower for native ops (passive evolution) |
| **Native fit** | Discrete logic, exact arithmetic, control flow | Optimization, ODE/PDE, inference, sampling, search |
| **Precision** | Arbitrary, exact, reproducible (bit-perfect) | Limited by noise/readout; approximate-and-verify |
| **Reproducibility** | Deterministic, bit-identical | Statistical; same answer within an error class |
| **Programming model** | Humans write code; deterministic compiler | AI agents shape physics; learned, calibrated |
| **Drift / aging** | Negligible at logic level | Real; managed by the agent calibration loop |
| **Best at** | Everything discrete, exact, branchy | Continuous, parallel, physics-shaped problems |

---

## 3. Where the Continuum Engine genuinely wins

Bounded, specific claims — each tied to a native mode from Doc 05:

- **Physical simulation (PDE/ODE).** Digital pays for discretizing space and time and iterating;
  the substrate embodies the dynamics directly (Mode 2). Largest expected advantage.
- **Large-scale optimization & constraint satisfaction.** Physical energy minimization explores
  the whole landscape in parallel (Mode 1) instead of iterating a solver.
- **Neural inference at the edge of energy budgets.** Matrix–vector multiply + nonlinearity as
  one physical pass, at a fraction of the energy of digital MACs. `[ESTABLISHED]` direction
  (analog in-memory compute already shows large energy wins).
- **Probabilistic inference / sampling.** Thermal noise *is* the sampler (Mode 3); digital
  spends enormous effort emulating randomness and mixing.

For these, the plausible target is **orders-of-magnitude** improvement in energy-per-solution
and in latency — *if* the problem fits the substrate.

---

## 4. Where digital wins — permanently and by design

This is not hedging; it is the architecture's explicit division of labor (Doc 01 tenet 3,
Doc 05 §5):

- **Exact arithmetic, integers, cryptography.** Need bit-perfect, reproducible results → digital.
- **Control-flow-heavy / branchy logic.** No natural landscape → digital.
- **Unbounded precision.** Analog precision is noise-limited; you only buy more via verify loops.
- **Determinism / auditability requirements.** When the answer must be bit-identical every time
  → digital.

The Continuum Engine **keeps a digital shell precisely so these stay digital** (Doc 07). It is a
*better core for the right problems*, not a universal replacement. Any claim that it "beats
digital at everything" would be false and is explicitly disclaimed here.

---

## 5. The fair accounting (advantage minus overheads)

A real comparison must subtract the costs that are easy to ignore:

- **Embedding overhead** — fitting a problem onto the fabric's connectivity (Doc 04 §5).
- **Calibration & drift correction** — the outer agent loop (Doc 04 §4).
- **Readout precision tax** — ADC noise and the approximate-and-verify refinement (Doc 07).
- **Agent compile time** — the slow control flow before physics even runs (Doc 02 §2).

Net advantage = (huge native speed/energy win) − (these overheads). For small or ill-fitting
problems the overheads dominate and **digital wins outright**. The Continuum Engine pays off on
**large, native-fit, energy-bound workloads** — which, not coincidentally, is where computing
is increasingly bottlenecked.

→ Continue to **[07 — I/O and Interfacing](./07-io-and-interfacing.md)**.
