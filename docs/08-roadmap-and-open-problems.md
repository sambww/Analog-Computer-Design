# 08 — Roadmap and Open Problems

> **Status of this document:** The early phases are `[ESTABLISHED]` and buildable today; later
> phases are `[SPECULATIVE]` and depend on named breakthroughs. This is the design's honesty
> ledger — the explicit list of what would have to be invented.

---

## 1. Phased roadmap (today → the vision)

The Continuum Engine is not a single invention but the endpoint of a path that starts with
hardware that already exists.

### Phase 0 — Today (all `[ESTABLISHED]`)
Existing building blocks, used separately: analog VLSI/neuromorphic chips, memristor crossbars
for in-memory matrix multiply, photonic matrix-multiply meshes, physical reservoir computers,
analog Ising machines/annealers, FPAAs. **What's missing:** they are fixed-function, hard to
reconfigure, and not driven by a unifying agent layer.

### Phase 1 — Agent-driven analog accelerator (near-term, mostly `[ESTABLISHED]`)
Wrap *existing* analog accelerators (e.g., a crossbar or photonic core) in the agent control
plane of Doc 04: agents handle embedding, calibration, and approximate-and-verify. Digital host
does everything else. **Goal:** prove the agent-first programming model on real, imperfect
analog hardware. This phase is buildable now and is the most important to validate the thesis.

### Phase 2 — Reconfigurable analog fabric (mid-term, `[SPECULATIVE]` in degree)
Generalize the fixed accelerator into a **field-programmable analog fabric** (Doc 02-B): one
device that can embody many problem physics by reconfiguring couplings. Extends FPAAs and
photonic meshes far beyond current density and flexibility. **Goal:** one machine, many problem
classes, configured by agents.

### Phase 3 — Programmable Continuous Field (long-term, `[SPECULATIVE]`)
The dense, continuous, locally-programmable medium of Doc 03 — the true substrate. **Goal:** the
full Continuum Engine: co-located state/compute at scale, native ops across all of Doc 05's
modes, room-temperature stability.

### Phase 4 — Self-improving instrument (visionary, `[SPECULATIVE]`)
The agent layer learns across all problems it ever sees — better embeddings, better drift
models, a growing library of known-good configurations (Doc 04 §5). The machine **gets better at
being programmed the more it runs.**

---

## 2. Named open problems (the honesty ledger)

Each is a concrete obstacle, paired with the established principle it must extend. None violate
known physics; all exceed known engineering.

| # | Open problem | Extends `[ESTABLISHED]` | Breakthrough required `[SPECULATIVE]` |
|---|--------------|-------------------------|----------------------------------------|
| **OP-1** | **Dense programmable medium** with locally settable dynamics | FPAAs, photonic phase-shifters | Orders-of-magnitude higher density + addressability |
| **OP-2** | **Fast, fine-grained reconfiguration** without destroying co-located state | Memristor non-volatility | Reconfigure in place without state loss |
| **OP-3** | **Drift & variation control** at room temperature | Self-calibrating instruments | Stable analog behavior at scale, agent-correctable |
| **OP-4** | **High-density, low-noise readout** | Modern ADCs, image sensors | Massively parallel readout that doesn't dominate energy/error |
| **OP-5** | **Scalable connectivity / embedding** | Domain decomposition, Ising embedding | Rich enough coupling to avoid crippling embedding overhead |
| **OP-6** | **Reliable agent compilation** of intent → physics | Learned compilers/controllers | Agents that embed & calibrate robustly across problem classes |
| **OP-7** | **Verification of analog results** at low cost | Numerical error analysis | Cheap, trustworthy residual/confidence estimation (Doc 07) |
| **OP-8** | **Manufacturing & yield** of analog media | Analog VLSI fabs | Economical production of variable analog substrates |

OP-1 through OP-4 are *physics/devices*; OP-5 through OP-7 are *systems/AI*; OP-8 is
*manufacturing*. The design is only as real as the slowest of these.

---

## 3. What would falsify the thesis

Stating the failure conditions plainly keeps the design honest:

- **If** the agent layer cannot reliably compile intent → physics for general problems (OP-6
  fails), the machine is an unprogrammable curiosity.
- **If** embedding/connectivity overhead (OP-5) eats the parallelism advantage, digital wins
  even on native-fit problems.
- **If** drift and readout noise (OP-3, OP-4) can't be controlled, the approximate-and-verify
  loop becomes so expensive it erases the energy advantage.
- **If** verification (OP-7) is unreliable, results can't be trusted and the machine is unsafe
  to use for anything that matters.

Any one of these failing in isolation may be survivable; several failing together is fatal. The
design's bet is that **Phase 1 can be validated now** with today's hardware, de-risking the
agent-first thesis before the harder physics (Phases 2–3) is attempted.

---

## 4. Closing

The Continuum Engine is a *direction*, not a blueprint: take the century-long line of analog
computing (Doc 03), make AI agents its native programmers (Doc 04), pose problems as physics to
be evolved rather than algorithms to be stepped (Doc 05), and you get a machine that — for
large, continuous, energy-bound, native-fit workloads — can far outrun digital (Doc 06), while
honestly leaving everything discrete and exact to the digital shell (Doc 07).

Everything speculative in this repository is tagged, traced to an established principle, and
listed above as a named open problem. That is the boundary between vision and fantasy, drawn on
purpose.

← Back to **[README](../README.md)** · See also **[glossary](./glossary.md)**.
