# 07 — I/O and Interfacing

> **Status of this document:** Almost entirely `[ESTABLISHED]` engineering — transduction,
> data converters, error budgeting, noise. This is the most buildable part of the design, and
> deliberately so: the boundary is where the speculative core meets real silicon.

---

## 1. The digital shell's job

The analog core cannot, by itself, talk to the world, store results durably, or guarantee
exactness. The **digital I/O shell** (Doc 02-D) is the thin layer of conventional silicon that
wraps it and handles everything analog is bad at:

- **Symbolic I/O** — receive problems and emit answers as exact digital data.
- **Durable storage & networking** — bit-perfect persistence and communication.
- **Transduction** — convert between digital values and continuous physical state (DAC in,
  ADC out).
- **Certification** — attach error bounds, confidence, and reproducibility class to every
  result (Doc 04 §6).
- **Hosting the agents** — the agent control plane (Doc 04) runs here.

The shell *serves* the core; it never becomes the main compute path (Doc 01, tenet 3).

---

## 2. The transduction boundary (DAC in, ADC out)

```
  digital problem ──► [DAC / field writer] ──► continuous config & inputs ──► SUBSTRATE
                                                                                  │
                                                                              evolves
                                                                                  │
  certified answer ◄── [Verifier + ADC / field reader] ◄── continuous settled state
```

- **Writing in (DAC / field writer).** Inputs, boundary conditions, couplings, and biases are
  written as continuous physical quantities. Write precision sets a floor on how accurately a
  problem can be posed. `[ESTABLISHED]`.
- **Reading out (ADC / field reader).** Settled or sampled state is measured back to digital.
  Readout is a *measurement*: it has finite resolution and **adds noise**. This is usually the
  dominant precision limit of the whole machine. `[ESTABLISHED]`.

Design consequence: I/O is co-designed with the substrate, not bolted on. Readout density,
speed, and noise are first-class budget items (Doc 03 §5, gap 4).

---

## 3. Noise: resource and adversary

Noise is treated with two faces, consistent with Doc 01 tenet 4:

**As a resource `[ESTABLISHED]`:**
- *Sampling* — thermal noise drives native Monte Carlo / Bayesian inference (Doc 05, Mode 3).
- *Escaping local minima* — annealed noise lets relaxation reach better optima (Mode 1).
- *Regularization* — noise smooths landscapes and improves generalization in inference.
- *Stochastic resonance* — small noise can enhance detection of weak signals.

**As an adversary `[ESTABLISHED]`:**
- Readout noise limits precision; device noise causes run-to-run variation; drift biases
  results over time.

The agent layer's job (Doc 04 §4) is to **schedule and budget** noise: inject it where it
helps, suppress and average it where it hurts.

---

## 4. Precision and the error budget

Because analog precision is finite, every result carries an explicit **error budget**, summed
across sources:

| Source | Nature | Mitigation |
|--------|--------|------------|
| Write/DAC error | How accurately the problem was posed | Calibrated converters; agent compensation |
| Device variation | Region-to-region mismatch | Calibrator models and corrects it (Doc 04) |
| Drift / aging | Slow change over time | Periodic recalibration; drift model |
| Thermal/shot noise | Random fluctuation | Averaging; choose noise schedule deliberately |
| Readout/ADC error | Measurement resolution + noise | Higher-resolution readout; repeated reads |

**Approximate-and-verify (Doc 01 tenet 5).** The core produces a fast approximate answer; the
Verifier checks it (e.g., plug a candidate solution back into the objective `J` and measure the
residual — cheap and digital) and either accepts it or triggers refinement. Precision is thus
*bought only where the problem needs it*, not paid uniformly.

---

## 5. Reproducibility classes

Analog results are not bit-identical run to run, so every answer is labeled with a
**reproducibility class** so downstream consumers know what they are getting:

- **Class A — Verified-exact.** Approximate analog answer refined/checked digitally until it
  meets a hard tolerance. Reproducible within that tolerance. (e.g., a linear solve with a
  digitally checked residual.)
- **Class B — Bounded-approximate.** Answer with a stated error bound; reproducible within the
  bound but not bit-identical. (e.g., a PDE field, an optimization result.)
- **Class C — Distributional.** A sample or a distribution; reproducible only in its statistics.
  (e.g., Bayesian posterior samples.)

This labeling is the concrete mechanism behind tenet 8 ("honest about limits"): the machine
**never presents a Class B or C result as if it were digital-exact.**

---

## 6. Why the boundary is small but critical

The shell is intentionally thin — most of the machine's value is in the analog core — but it is
where the design becomes *trustworthy*. Transduction sets the precision floor; certification
makes results safe to use; the reproducibility class makes the machine's honesty machine-
readable. Get the boundary right and the speculative core becomes usable; get it wrong and even
a perfect substrate is untrustworthy.

→ Continue to **[08 — Roadmap and Open Problems](./08-roadmap-and-open-problems.md)**.
