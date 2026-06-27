"""Mode 1 (Relaxation) — Max-Cut as Ising energy minimization.

Maps directly to ``docs/05-computational-model.md`` (Mode 1) and the Ising-machine lineage
in ``docs/03-analog-substrate.md``. We pose Max-Cut as an Ising energy whose *minimum* is
the best cut, let the substrate descend it with an annealed-noise schedule, and have the
agent verify the result against the true optimum (brute force, since the graph is tiny).

Run:  python demos/demo_optimization.py
"""

from __future__ import annotations

import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from continuum import Agent, ReproClass, Substrate  # noqa: E402


def make_graph(n: int = 12, seed: int = 7) -> np.ndarray:
    """A random symmetric weight matrix W (zero diagonal) for a Max-Cut instance."""
    rng = np.random.default_rng(seed)
    W = rng.uniform(0.2, 1.0, size=(n, n)) * (rng.random((n, n)) < 0.5)
    W = np.triu(W, 1)
    return W + W.T


def cut_value(W: np.ndarray, s: np.ndarray) -> float:
    """Total weight of edges crossing the cut defined by spins s in {-1,+1}."""
    return 0.25 * np.sum(W * (1.0 - np.outer(s, s)))


def brute_force_maxcut(W: np.ndarray) -> float:
    """True optimum by enumeration (fixing s[0]=+1 by symmetry). Tiny graphs only."""
    n = W.shape[0]
    best = -np.inf
    for bits in itertools.product([1, -1], repeat=n - 1):
        s = np.array((1,) + bits, dtype=float)
        best = max(best, cut_value(W, s))
    return best


def solve_maxcut(W: np.ndarray, seed: int = 0):
    """Agent-driven solve: configure energy, relax with annealed noise, verify vs optimum.

    Ising energy for Max-Cut is E(s) = (1/2) sᵀ W s  (minimizing it maximizes the cut).
    We relax a *continuous* spin x in [-1, 1] (the analog medium's saturating state), then
    read out discrete spins by sign. The agent retries with a hotter/longer anneal until the
    cut matches the known optimum.
    """
    n = W.shape[0]
    optimum = brute_force_maxcut(W)
    substrate = Substrate(seed=seed)
    agent = Agent(max_attempts=6)

    def grad_energy(x: np.ndarray) -> np.ndarray:
        # ∇E for E = 1/2 xᵀ W x is W x; a soft restoring term keeps x in range.
        return W @ x + 0.5 * (x ** 3 - x)

    def run(attempt: int) -> np.ndarray:
        x0 = substrate.rng.uniform(-0.1, 0.1, size=n)
        trace = substrate.relax(
            grad_energy,
            x0,
            steps=3000 + 1500 * attempt,
            dt=0.01,
            noise0=0.5 + 0.3 * attempt,   # hotter start on retries
            anneal=4.0,
            clip=1.0,
        )
        return np.sign(trace.x)

    def residual(s: np.ndarray) -> float:
        # How far below the true optimum is this cut? (0.0 == optimal)
        return float(optimum - cut_value(W, s))

    result = agent.solve(
        run, residual, tol=1e-9, repro_class=ReproClass.B,
        note=f"max-cut on {n} nodes; optimum={optimum:.3f}",
    )
    return result, optimum


def main() -> None:
    W = make_graph()
    result, optimum = solve_maxcut(W, seed=1)
    achieved = optimum - result.error
    print("Mode 1 — Relaxation / Ising Max-Cut")
    print(f"  optimum cut (brute force): {optimum:.4f}")
    print(f"  cut found by substrate:    {achieved:.4f}")
    print(f"  {result}")


if __name__ == "__main__":
    main()
