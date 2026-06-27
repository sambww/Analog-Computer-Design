# 02 — Architecture Overview

> **Status of this document:** The layering and data/control-flow concepts are `[ESTABLISHED]`
> systems-engineering patterns applied to an analog core. The specific substrate they wrap is
> `[SPECULATIVE]` (see Doc 03).

---

## 1. Four layers

The Continuum Engine is organized as four layers. Computation lives at the bottom; intent
enters at the top.

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  (D) DIGITAL I/O SHELL                                                 │
  │      • symbolic in/out, storage, networking, human/agent API          │
  │      • ADC/DAC transduction, result certification                     │
  └───────────────▲───────────────────────────────────┬──────────────────┘
                  │ intent, constraints, data          │ certified answers
  ┌───────────────┴───────────────────────────────────▼──────────────────┐
  │  (C) AGENT CONTROL PLANE   ← the "programmer" / OS / compiler          │
  │      • decompose problem → analog primitives                          │
  │      • synthesize field configuration (boundary conditions, biases)   │
  │      • calibrate, correct drift, schedule, verify, refine             │
  └───────────────▲───────────────────────────────────┬──────────────────┘
                  │ configuration (couplings, biases)   │ measured state, residuals
  ┌───────────────┴───────────────────────────────────▼──────────────────┐
  │  (B) FIELD FABRIC (configurable interconnect)                         │
  │      • programmable couplings between substrate regions               │
  │      • routes/shapes continuous signals; defines the "wiring"         │
  └───────────────▲───────────────────────────────────┬──────────────────┘
                  │ coupling weights                    │ continuous signals
  ┌───────────────┴───────────────────────────────────▼──────────────────┐
  │  (A) CONTINUOUS ANALOG SUBSTRATE   ← computation = physics            │
  │      • the medium whose natural dynamics ARE the computation          │
  │      • co-located state + compute; relaxes toward solutions           │
  └──────────────────────────────────────────────────────────────────────┘
```

### (A) Continuous Analog Substrate — *where computing happens*
The physical medium whose dynamics embody the problem. State and computation are co-located:
the same physical degrees of freedom that *hold* the answer also *compute* it. Detailed in
Doc 03.

### (B) Field Fabric — *the reconfigurable wiring*
A programmable interconnect that sets the couplings between regions of the substrate —
effectively the weights/topology of the physical system. Reconfiguring the fabric is how one
machine embodies many different problem physics. `[ESTABLISHED]` analogues: FPAAs
(field-programmable analog arrays), crossbar interconnects, photonic mesh phase-shifters.

### (C) Agent Control Plane — *the programmer*
The AI layer. It takes intent and constraints from above and produces *configurations* for
the fabric and substrate below; it then reads back measured state, computes residuals, and
iterates: calibrate → run → measure → correct → refine. This layer is the subject of Doc 04.

### (D) Digital I/O Shell — *the boundary with the rest of the world*
Conventional digital silicon doing what digital is best at: exact storage, networking, the
human/agent-facing API, transduction (ADC/DAC), and *certification* of analog results. The
shell is deliberately thin — it serves the analog core. Detailed in Doc 07.

---

## 2. Two distinct flows: signal vs. control

A common confusion with analog machines is conflating *the computation* with *the control of
the computation*. They are separate flows with different speeds and natures.

- **Signal flow (fast, continuous, analog).** Inside layers A–B, continuous physical signals
  evolve in real, physical time. This is the actual computation. It is parallel across the
  whole substrate at once and is not clocked by any instruction counter.

- **Control flow (slower, discrete, agentic).** Layers C–D operate in a configure → observe →
  adjust loop. This loop is comparatively slow and *episodic*: agents set up a problem, let the
  physics run, measure, and decide what to do next. The agents are *not* in the inner loop of
  the computation — they are in the *outer* loop that aims it.

```
   intent ──► [C: agent] ──configure──► [B/A: physics evolves] ──measure──► [C: agent]
                  ▲                                                            │
                  └───────────────── refine / re-aim ──────────────────────────┘
                                  (outer control loop)
```

This separation is what makes the machine programmable without an instruction set: agents
shape the *landscape*; physics rolls the ball downhill.

---

## 3. A worked trace (high level)

To make the layers concrete, here is how a single problem flows through the machine. (Doc 05
formalizes the model; this is just the choreography.)

1. **Pose (D→C).** A request arrives at the digital shell: *"Find the lowest-energy folding of
   this molecule,"* with constraints and a precision target.
2. **Compile (C).** Agents map the problem onto the substrate's native dynamics — here, an
   energy-minimization embedding — and synthesize a fabric configuration (couplings, biases)
   plus a calibration plan.
3. **Configure (C→B→A).** The configuration is written into the field fabric and substrate.
4. **Evolve (A).** The substrate is released and relaxes; its physics descends the energy
   landscape in continuous time, in parallel, with thermal noise providing escape from local
   minima.
5. **Measure (A→C).** The settled state is read out; agents compute residuals and a confidence
   estimate.
6. **Refine (C).** If confidence is low or constraints are violated, agents adjust biases,
   anneal the noise schedule, or re-embed, and re-run (back to step 3). Approximate-and-verify
   in action.
7. **Certify & return (C→D).** When the result meets the target, the shell packages the answer
   *with* its error bounds and reproducibility class and returns it.

---

## 4. Where the speculation lives

Everything in this document is conventional systems engineering *except* the substrate (A)
and the degree of fabric reconfigurability (B). Those are where the `[SPECULATIVE]` leaps
concentrate, and they are the subject of the next document.

→ Continue to **[03 — The Analog Substrate](./03-analog-substrate.md)**.
