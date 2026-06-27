"""Mode 2 (Evolution) + a Mode 1 linear solve.

Two native behaviors from ``docs/05-computational-model.md``:

1. **Evolution (Mode 2)** — integrate a damped harmonic oscillator on the substrate and
   verify the trajectory against the closed-form analytic solution. This is the op-amp
   ODE-solver lineage of ``docs/03-analog-substrate.md``.

2. **Linear solve (Mode 1)** — solve ``A x = b`` (A symmetric positive-definite) by gradient
   flow on ``f(x) = 1/2 xᵀA x - bᵀx``, whose minimum is ``x* = A⁻¹b``. The agent verifies by
   the residual ``‖A x - b‖`` and certifies it Class A (verified-exact) — the
   approximate-and-verify pattern of ``docs/07-io-and-interfacing.md``.

Run:  python demos/demo_ode.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from continuum import Agent, ReproClass, Substrate  # noqa: E402


# --------------------------------------------------------------------------- #
# 1. Mode 2 — damped harmonic oscillator   y'' + 2ζω y' + ω² y = 0
# --------------------------------------------------------------------------- #
def damped_oscillator(zeta: float = 0.2, omega: float = 2.0, seed: int = 0):
    substrate = Substrate(seed=seed)
    y0 = np.array([1.0, 0.0])  # [position, velocity]

    def dynamics(t: float, y: np.ndarray) -> np.ndarray:
        pos, vel = y
        return np.array([vel, -2 * zeta * omega * vel - omega ** 2 * pos])

    ts, ys = substrate.evolve(dynamics, y0, t_span=(0.0, 10.0), steps=4000)

    # Closed-form reference (underdamped) for verification.
    wd = omega * np.sqrt(1 - zeta ** 2)
    analytic = np.exp(-zeta * omega * ts) * (
        np.cos(wd * ts) + (zeta * omega / wd) * np.sin(wd * ts)
    )
    max_err = float(np.max(np.abs(ys[:, 0] - analytic)))
    return ts, ys[:, 0], analytic, max_err


# --------------------------------------------------------------------------- #
# 2. Mode 1 — linear solve  A x = b  via gradient flow
# --------------------------------------------------------------------------- #
def make_spd(n: int = 8, seed: int = 3) -> np.ndarray:
    rng = np.random.default_rng(seed)
    M = rng.standard_normal((n, n))
    return M @ M.T + n * np.eye(n)  # symmetric positive-definite, well-conditioned


def solve_linear(A: np.ndarray, b: np.ndarray, seed: int = 0):
    substrate = Substrate(seed=seed)
    agent = Agent(max_attempts=5)
    n = A.shape[0]
    # Stable explicit-Euler step requires dt < 2 / max-eigenvalue of A.
    dt = 1.0 / float(np.max(np.linalg.eigvalsh(A)))

    def grad_energy(x: np.ndarray) -> np.ndarray:
        return A @ x - b  # ∇(1/2 xᵀA x - bᵀx)

    def run(attempt: int) -> np.ndarray:
        x0 = np.zeros(n)
        trace = substrate.relax(grad_energy, x0, steps=2000 + 2000 * attempt, dt=dt)
        return trace.x

    def residual(x: np.ndarray) -> float:
        return float(np.linalg.norm(A @ x - b))

    result = agent.solve(
        run, residual, tol=1e-6, repro_class=ReproClass.A,
        note=f"linear solve, n={n}",
    )
    return result


def main() -> None:
    print("Mode 2 — Evolution / damped harmonic oscillator")
    _, _, _, max_err = damped_oscillator(seed=1)
    print(f"  max |substrate - analytic| over trajectory: {max_err:.3e}")
    print(f"  [B: bounded-approximate] trajectory error bound = {max_err:.3e}\n")

    print("Mode 1 — Relaxation / linear solve A x = b")
    A = make_spd()
    rng = np.random.default_rng(11)
    x_true = rng.standard_normal(A.shape[0])
    b = A @ x_true
    result = solve_linear(A, b, seed=2)
    err_vs_true = float(np.linalg.norm(result.value - x_true))
    print(f"  ‖x_found - x_true‖: {err_vs_true:.3e}")
    print(f"  {result}")


if __name__ == "__main__":
    main()
