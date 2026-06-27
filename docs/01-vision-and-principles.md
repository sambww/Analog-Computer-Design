# 01 — Vision and Principles

> **Status of this document:** Mostly conceptual framing. The *principles* are grounded in
> `[ESTABLISHED]` analog-computing history; the *machine* they point toward is
> `[SPECULATIVE]`.

---

## 1. The thesis: computation as physics, programming as agency

Two ideas sit at the center of this design.

**Thesis A — Computation is physics, not arithmetic.**
A digital computer represents a physical system (a fluid, a market, a neural network, a
protein) as numbers, then runs an *algorithm* that approximates the system's evolution one
discrete time-step at a time. Every step costs energy and latency, and the approximation is
never the thing itself. An analog computer takes the opposite stance: build a physical system
whose governing equations are *the same* as the problem's, let it evolve, and **read the
answer off the physics**. The computation has no algorithmic overhead because there is no
algorithm — only nature taking its course. `[ESTABLISHED]` This is exactly how 20th-century
analog computers solved differential equations with op-amp integrators, and how modern
photonic chips perform matrix multiplication at the speed of light through a passive mesh.

**Thesis B — AI agents are the native programmers.**
A machine with no instruction set cannot be programmed the way a CPU is. You do not write
`MOV` and `ADD`; you *shape a physical field* — set boundary conditions, bias a medium,
configure couplings — so that the system's natural relaxation lands on the answer. Choosing
those configurations is a high-dimensional, noisy, continuous inverse problem. That is
precisely the kind of problem modern AI is good at and humans are bad at. So in this design,
**AI agents are not an application running on the computer — they are the operating system,
the compiler, and the calibration loop.** The human states intent; agents translate it into
physics.

Put together: **the Continuum Engine is a physical medium that computes by evolving, driven
and interpreted by AI agents.**

---

## 2. Why bother? What digital does badly

Digital computers are miraculous at exact, discrete, reproducible symbol manipulation. But
the workloads that now dominate computing — and especially the workloads AI itself runs —
are a poor fit for that strength:

- **Simulating continuous physics.** Weather, fluids, plasmas, molecules, materials. Digital
  spends exponential effort discretizing space and time to approximate something an analog
  medium can embody directly. `[ESTABLISHED]` problem framing.
- **Optimization and constraint satisfaction.** Routing, scheduling, layout, inference. Many
  map naturally onto *energy minimization* — and physical systems minimize energy for free.
  `[ESTABLISHED]` (Hopfield networks, Ising machines, analog optimization).
- **Neural inference.** A neural network is mostly matrix–vector multiply plus a smooth
  nonlinearity — the two things analog crossbars and physical media do natively and cheaply.
  `[ESTABLISHED]` (analog in-memory compute, memristor crossbars).
- **The energy wall.** Digital is hitting hard limits on energy-per-operation and on moving
  data between memory and compute. The von Neumann bottleneck is now the dominant cost.
  `[ESTABLISHED]`.

The bet of this design: a machine built for *these* workloads, programmed by agents that can
tolerate and exploit its messiness, can deliver order-of-magnitude gains where it counts —
without pretending to replace digital for the things digital already does perfectly.

---

## 3. Design tenets

These tenets govern every later document. Each is something the architecture must honor.

1. **Compute by evolving, not by stepping.** The default mode of operation is to let a
   continuous physical system relax toward a solution, not to iterate discrete instructions.

2. **Agents over instructions.** There is no human-facing instruction set. The programming
   interface is *intent + constraints*; AI agents compile that into physical configuration.

3. **Analog core, digital shell.** Continuous dynamics in the center; digital only at the
   boundary for symbolic I/O, storage, and orchestration. Digital serves analog, not the
   reverse.

4. **Noise is a resource, not only a flaw.** Thermal and shot noise enable stochastic search,
   sampling, and regularization. The design *uses* noise where helpful and *budgets* it where
   harmful. `[ESTABLISHED]` (stochastic resonance, Langevin sampling, noisy optimization).

5. **Approximate-and-verify.** The analog core produces fast approximate answers; a
   lightweight digital/agent layer verifies, refines, and certifies them. Precision is bought
   only where it is needed.

6. **Reconfigurable, not fixed-function.** The substrate is continuously reconfigurable so a
   single machine can embody many different problem physics over time — otherwise it is just
   an ASIC.

7. **Co-located memory and compute.** State lives *in* the physical medium that computes on
   it. There is no separate memory to fetch from. This is the structural answer to the von
   Neumann bottleneck. `[ESTABLISHED]` framing (in-memory computing).

8. **Honest about limits.** The machine must never silently pretend to digital precision.
   Error bounds, reproducibility class, and confidence travel with every result.

---

## 4. The shape of the machine (preview)

The rest of the repository fills this in, but in one breath: a **reconfigurable continuous
analog substrate** (Doc 03) is shaped by an **AI agent control plane** (Doc 04) according to
a **field/energy computational model** (Doc 05), wrapped in a thin **digital I/O shell**
(Doc 07), and is — for the right workloads — dramatically better than digital (Doc 06), if a
handful of named breakthroughs land (Doc 08).

→ Continue to **[02 — Architecture Overview](./02-architecture-overview.md)**.
