# Continuum Engine — runnable conceptual simulation

This is a small, **numpy-only** behavioral model of the AI-agent-first analog computer
described in [`../docs`](../docs). It does **not** simulate the speculative hardware. It makes
the design's *core ideas* runnable so you can watch them converge to known-correct answers and
see the error bounds / reproducibility classes the docs promise.

> Status: this code is `[ESTABLISHED]` numerics standing in for the `[SPECULATIVE]` substrate.
> The point is fidelity to the **computational model** (docs/05), not to the physics.

## What it demonstrates

The simulation mirrors the architecture of [docs/02](../docs/02-architecture-overview.md):

- **`continuum/substrate.py`** — the analog substrate's three native execution modes from
  [docs/05](../docs/05-computational-model.md):
  - `relax`  → **Mode 1 (Relaxation)** — descend an energy landscape (Hopfield/Ising lineage)
  - `evolve` → **Mode 2 (Evolution)** — integrate continuous-time dynamics (op-amp ODE lineage)
  - `sample` → **Mode 3 (Sampling)** — Langevin sampling (thermodynamic-computing lineage)
- **`continuum/agent.py`** — the agent control plane from
  [docs/04](../docs/04-ai-agent-layer.md): configure → run → measure → refine → **certify**,
  attaching an error bound and a reproducibility class (A/B/C) per
  [docs/07 §5](../docs/07-io-and-interfacing.md).

## The demos

| Demo | Mode | Problem | Verified against | Repro class |
|------|------|---------|------------------|-------------|
| `demos/demo_optimization.py` | 1 | Max-Cut as Ising energy minimization | brute-force optimum | B |
| `demos/demo_ode.py` | 2 + 1 | Damped oscillator; linear solve `Ax=b` | analytic solution; residual `‖Ax-b‖` | B; A |
| `demos/demo_sampling.py` | 3 | Sample a 2-D Gaussian | target mean & covariance | C |

Each demo prints its result **with** an error bound and a reproducibility class — the design's
rule that the machine never presents an approximate answer as if it were exact
([docs/01](../docs/01-vision-and-principles.md) tenet 8).

## Run it

```bash
cd sim
pip install -r requirements.txt        # numpy (and pytest to run the tests)

python demos/demo_optimization.py
python demos/demo_ode.py
python demos/demo_sampling.py

pip install pytest
python -m pytest tests/ -q             # deterministic convergence tests (seeded RNG)
```

## How to read the mapping back to the design

The `relax` / `evolve` / `sample` primitives are the "instruction set that isn't an
instruction set" of [docs/03](../docs/03-analog-substrate.md): you don't sequence operations,
you *shape a landscape or specify dynamics* and read off the settled state. The `Agent.solve`
loop is the outer control flow of [docs/02 §2](../docs/02-architecture-overview.md) — agents
aim the physics and verify it; they are not in the inner computational loop.
