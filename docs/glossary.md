# Glossary

Each term is tagged **`[ESTABLISHED]`** (real, demonstrated science/engineering) or
**`[SPECULATIVE]`** (a deliberate leap beyond current technology). Terms specific to this
design are marked **`[THIS DESIGN]`**.

---

### Agent control plane `[THIS DESIGN]`
The layer of AI agents that programs, calibrates, schedules, and verifies the analog core. See
[Doc 04](./04-ai-agent-layer.md).

### Analog VLSI / Neuromorphic computing `[ESTABLISHED]`
Building computation directly from the physics of analog circuits (Carver Mead, 1980s–).
Demonstrates massive parallel analog compute and physics-as-computation at scale.

### Approximate-and-verify `[THIS DESIGN]` (pattern is `[ESTABLISHED]`)
Produce a fast approximate analog answer, then cheaply check/refine it digitally (e.g., measure
the residual of a candidate solution). Buys precision only where needed. See
[Doc 07](./07-io-and-interfacing.md).

### Co-located memory and compute / In-memory computing `[ESTABLISHED]`
Architectures where data is processed where it is stored, eliminating data movement between
memory and processor. The structural answer to the von Neumann bottleneck.

### Continuum Engine `[THIS DESIGN]`
The name of the AI-agent-first analog computer designed in this repository.

### Drift `[ESTABLISHED]`
Slow change in an analog device's behavior over time/temperature. A perennial enemy of analog
computing; here it is managed by the agent calibration loop ([Doc 04 §4](./04-ai-agent-layer.md)).

### Energy minimization / Relaxation `[ESTABLISHED]`
Solving a problem by encoding its cost as a physical system's energy and letting the system
settle to a minimum. Basis of Hopfield networks and Ising machines. Execution Mode 1 in
[Doc 05](./05-computational-model.md).

### Field Fabric `[THIS DESIGN]`
The reconfigurable interconnect that sets couplings between substrate regions — the "wiring."
See [Doc 02-B](./02-architecture-overview.md). Extends `[ESTABLISHED]` FPAAs / photonic meshes.

### FPAA (Field-Programmable Analog Array) `[ESTABLISHED]`
A reconfigurable analog IC — the analog cousin of an FPGA. Prior art for the Field Fabric.

### Ising machine / Analog annealer `[ESTABLISHED]`
Hardware that solves combinatorial optimization by physically minimizing an Ising energy
function, often with annealed noise.

### Memristor crossbar `[ESTABLISHED]`
A grid of resistive memory devices that performs analog matrix–vector multiplication in place,
co-locating memory and compute.

### Objective functional (J) `[THIS DESIGN]` (math is `[ESTABLISHED]`)
The function of substrate state whose minimum (or equilibrium distribution) encodes the
solution. Part of what constitutes a "program" here. See [Doc 05](./05-computational-model.md).

### Photonic / Optical computing `[ESTABLISHED]`
Using light propagating through a passive mesh to perform operations (notably matrix multiply)
at the speed of light with very low static energy.

### Programmable Continuous Field (PCF) `[SPECULATIVE]`
The speculative core substrate of this design: a dense, reconfigurable medium with continuous
state and programmable local dynamics. The unification of the Doc 03 lineage. The biggest leap
in the repository.

### Quantum computing `[ESTABLISHED]` (distinct from this design)
Computation using quantum superposition/entanglement. The Continuum Engine is **not** a quantum
computer — it is a *classical, continuous-state* machine. They are different paradigms; the PCF
exploits classical continuous physics, not quantum amplitudes.

### Reproducibility class `[THIS DESIGN]`
A label (A: verified-exact, B: bounded-approximate, C: distributional) attached to every result
so consumers know its precision/reproducibility guarantee. See [Doc 07 §5](./07-io-and-interfacing.md).

### Reservoir computing (Physical) `[ESTABLISHED]`
Using a fixed, rich nonlinear physical medium as a "reservoir" and training only a simple
readout. Shows that many physical media can compute if read out cleverly.

### Sampling (thermodynamic / Langevin) `[ESTABLISHED]`
Using calibrated thermal noise so a physical system visits states with probability
`∝ exp(−J/T)`, giving native Monte Carlo / Bayesian inference. Execution Mode 3 in
[Doc 05](./05-computational-model.md).

### Stochastic resonance `[ESTABLISHED]`
A phenomenon where adding noise can *improve* detection of weak signals — one reason noise is
treated as a resource here.

### Substrate (Continuous Analog Substrate) `[THIS DESIGN]`
Layer A of the architecture: the physical medium whose dynamics are the computation. Realized
by the PCF. See [Doc 02-A](./02-architecture-overview.md) and [Doc 03](./03-analog-substrate.md).

### Von Neumann bottleneck `[ESTABLISHED]`
The throughput/energy limit caused by separating memory from compute and shuttling data between
them. The dominant cost in modern digital computing and a central motivation for this design.

← Back to **[README](../README.md)**.
