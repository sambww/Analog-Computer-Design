# 04 — The AI Agent Layer

> **Status of this document:** The agent *roles and loop* are `[ESTABLISHED]` practice
> (modern AI agents, control theory, automated calibration). Applying them as the *sole*
> programming model for a continuous substrate is the `[SPECULATIVE]` move — and the heart of
> the "AI-agent-first" claim.

---

## 1. Why agents, and why *first*

A CPU has an instruction set; you compile a language down to it. The Continuum Engine has no
instruction set — only a continuous configuration space (Doc 03). Configuring it to solve a
problem is a high-dimensional, noisy, nonlinear **inverse problem**: *given the answer I want,
find the physical setup whose natural evolution produces it.* Humans cannot do this by hand at
scale; it is the analog-machine equivalent of asking someone to write a billion floating-point
constants by intuition.

This is exactly the kind of problem AI is built for. So the design makes AI agents the
**primary, native** programming interface — not an application that runs *on* the machine, but
the layer that *operates* it. Hence "AI-agent-first": **the machine is unusable without
agents, and designed assuming agents from the start.**

---

## 2. The agent stack

The control plane (Doc 02-C) is a small society of specialized agents. Each owns one part of
turning intent into settled physics.

| Agent role | Responsibility | Established analogue `[ESTABLISHED]` |
|------------|----------------|--------------------------------------|
| **Intent compiler** | Turn a human/agent request + constraints into a formal problem (objective + boundary conditions) | Compiler front-end / spec synthesis |
| **Embedder** | Map the formal problem onto the substrate's native dynamics (which primitives, what topology) | Hardware mapping / place-and-route |
| **Configurator** | Synthesize concrete fabric couplings, biases, and noise schedule | FPGA bitstream generation |
| **Calibrator** | Characterize the physical medium, correct drift and device variation | Instrument auto-calibration |
| **Conductor** | Schedule runs, set anneal/relaxation schedules, manage the outer control loop | Control-systems supervisor |
| **Verifier** | Estimate residuals, error bounds, and confidence; decide accept/refine | Approximate-and-verify / numerical error analysis |
| **Librarian** | Cache known-good configurations and calibration models for reuse | Build cache / model registry |

These agents are themselves *digital* (they run in the shell, Doc 07-D). The machine is a
hybrid: **digital intelligence aiming analog physics.**

---

## 3. How agents "program" physics — the compile pipeline

```
  intent + constraints
        │
        ▼
  [Intent compiler]  ──►  formal problem  (objective functional J, constraints, precision target)
        │
        ▼
  [Embedder]         ──►  embedding plan   (which native ops; substrate topology)
        │
        ▼
  [Configurator]     ──►  physical config  (couplings, biases, noise schedule)
        │
        ▼
  [Calibrator] ⇄ substrate  ──►  corrected config (drift/variation compensated)
        │
        ▼
  RUN: substrate relaxes ──► measured state
        │
        ▼
  [Verifier]  ──► residuals + confidence ──► accept ▸ return   /   refine ▸ loop back
```

The crucial inversion from digital: the agent does **not** specify *how* to compute the answer
step by step. It specifies *what landscape to build*, and physics does the descending. The
agent's skill is in **shaping landscapes and reading results**, not in sequencing operations.

---

## 4. The outer control loop (calibrate → run → measure → correct)

Analog machines drift, vary device-to-device, and are noisy. The agent layer turns these from
fatal flaws into managed quantities via a continuous outer loop (the slow control flow of
Doc 02-§2):

1. **Calibrate.** Probe the substrate with known stimuli; fit a model of its current behavior
   (gains, offsets, coupling errors). `[ESTABLISHED]` (self-calibrating instruments).
2. **Run.** Configure and release the physics; let it evolve in real time.
3. **Measure.** Read out settled (or sampled) state and compute residuals against the
   objective.
4. **Correct & refine.** Compensate for measured drift, adjust biases/noise schedule, or
   re-embed; re-run. Over many problems, the **Librarian** learns reusable configurations and
   the **Calibrator** learns a drift model, so the loop shortens over time.

This loop is also the source of the machine's robustness: correctness is enforced by the
*agents verifying physics*, not by the physics being perfect.

---

## 5. Multi-agent orchestration

For large problems, agents **decompose and compose**:

- **Decomposition.** The Embedder splits a problem too big for the substrate into subproblems
  that fit, schedules them across substrate regions or across time, and stitches partial
  results. `[ESTABLISHED]` (domain decomposition, tiling).
- **Specialization.** Different agents (or fine-tuned variants) specialize by problem class —
  PDEs, combinatorial optimization, inference — and the Conductor routes work to the right
  one.
- **Learning across runs.** Because the same agents see many problems, they improve their
  embeddings and calibration models over time. The machine *gets better at being programmed*
  the more it is used. `[SPECULATIVE]` at full strength, but `[ESTABLISHED]` in spirit (learned
  compilers, learned controllers).

---

## 6. Trust boundary and safety

Two honesty constraints the agent layer must enforce (tying back to tenet 8 in Doc 01):

- **Never launder uncertainty.** The Verifier must attach error bounds and a reproducibility
  class to every result. An analog answer presented as if it were bit-exact is a defect.
- **Keep agents in the *outer* loop.** Agents aim and verify; they are not in the inner
  physical loop. This bounds their failure modes to *mis-aiming* (caught by the Verifier)
  rather than corrupting the computation mid-flight.

→ Continue to **[05 — The Computational Model](./05-computational-model.md)**.
