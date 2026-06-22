# The Continuum Engine

### An AI-Agent-First Analog Computer

> A design for a machine where **computation is physics**, **programming is done by AI
> agents**, and the digital computer is reduced to a peripheral at the edges.

This repository is a **design study**, not a product. It describes an architecture for a
class of analog computer that is *native to artificial intelligence* — where AI agents,
not human programmers, are the primary "users" of the machine — and argues where and why
such a machine could outperform digital computers by orders of magnitude.

---

## The one-paragraph pitch

A digital computer spends almost all of its energy and time *simulating* the physics of a
problem one discrete step at a time, shuttling numbers between memory and a processor. The
**Continuum Engine** inverts this: instead of simulating dynamics, it *is* the dynamics.
Problems are posed as continuous physical fields whose natural evolution **settles into the
answer**. There is no instruction stream, no clock-bound fetch–decode–execute loop, and no
von Neumann bottleneck. Because the machine has no fixed instruction set and its behavior is
shaped by continuous configuration rather than discrete code, **AI agents are its native
programmers** — they translate intent into physical boundary conditions, calibrate the
substrate, correct for drift and noise, and verify results. The result is a system that, for
the workloads AI actually runs (optimization, inference, simulation of physical systems,
search), can be far faster and far more energy-efficient than any digital machine — while
honestly remaining *worse* at the things digital computers are perfect for, like exact
discrete arithmetic and bit-perfect reproducibility.

---

## How to read this repository

This is **grounded extrapolation**. Every claim is tagged so you always know whether you are
reading established engineering or speculation:

- **`[ESTABLISHED]`** — real, demonstrated science or engineering (op-amps, analog VLSI,
  memristor crossbars, photonic matrix multiply, reservoir computing, etc.).
- **`[SPECULATIVE]`** — a deliberate leap beyond current technology. Every speculative claim
  is paired with the established principle it extends, so the leap is traceable, not magical.

Recommended reading order:

| # | Document | What it covers |
|---|----------|----------------|
| — | **[README.md](./README.md)** | You are here: vision, pitch, doc map |
| 1 | **[docs/01-vision-and-principles.md](./docs/01-vision-and-principles.md)** | The thesis and the design tenets |
| 2 | **[docs/02-architecture-overview.md](./docs/02-architecture-overview.md)** | The four layers and how signal/control flow |
| 3 | **[docs/03-analog-substrate.md](./docs/03-analog-substrate.md)** | The physical compute medium |
| 4 | **[docs/04-ai-agent-layer.md](./docs/04-ai-agent-layer.md)** | How AI agents "program" physics |
| 5 | **[docs/05-computational-model.md](./docs/05-computational-model.md)** | What a "program" actually is |
| 6 | **[docs/06-comparison-vs-digital.md](./docs/06-comparison-vs-digital.md)** | Head-to-head with digital, honestly |
| 7 | **[docs/07-io-and-interfacing.md](./docs/07-io-and-interfacing.md)** | The digital boundary, noise, precision |
| 8 | **[docs/08-roadmap-and-open-problems.md](./docs/08-roadmap-and-open-problems.md)** | The path there and what's unsolved |
| — | **[docs/glossary.md](./docs/glossary.md)** | Terms, each tagged established/speculative |

---

## What this is *not*

- It is **not** a claim that analog beats digital at everything. Section 6 is explicit about
  where digital wins and always will.
- It is **not** a buildable spec. Sections 3 and 8 flag exactly which breakthroughs are still
  missing.
- It is **not** quantum computing. The Continuum Engine is a classical, continuous-state
  machine; the relationship to quantum hardware is discussed in the glossary.

---

## License & status

Design study, work in progress. See [docs/08-roadmap-and-open-problems.md](./docs/08-roadmap-and-open-problems.md)
for the honest list of what would have to be invented to make this real.
