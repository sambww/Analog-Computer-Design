"""Mode 3 (Sampling) — Langevin sampling from a target distribution.

Maps to ``docs/05-computational-model.md`` (Mode 3) and the thermodynamic-computing lineage
in ``docs/03-analog-substrate.md``: sustained thermal noise turns relaxation into a sampler,
giving native Monte-Carlo / Bayesian inference. The target here is a 2-D Gaussian
``N(mu, Sigma)`` encoded as the energy ``E(x) = 1/2 (x-mu)ᵀ Σ⁻¹ (x-mu)``; samples should
reproduce ``mu`` and ``Sigma`` *in statistics* — reproducibility Class C.

Run:  python demos/demo_sampling.py
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from continuum import Substrate  # noqa: E402


def gaussian_sampler(mu: np.ndarray, Sigma: np.ndarray, seed: int = 0):
    substrate = Substrate(seed=seed)
    Sinv = np.linalg.inv(Sigma)

    def grad_energy(x: np.ndarray) -> np.ndarray:
        return Sinv @ (x - mu)  # ∇E for the Gaussian energy

    samples = substrate.sample(
        grad_energy,
        x0=np.zeros_like(mu),
        temperature=1.0,   # T=1 so exp(-E) matches the target density exactly
        steps=60000,
        dt=0.01,
        burn_in=5000,
        thin=5,
    )
    return samples


def main() -> None:
    mu = np.array([1.5, -0.5])
    Sigma = np.array([[1.0, 0.6], [0.6, 0.8]])
    samples = gaussian_sampler(mu, Sigma, seed=1)

    est_mu = samples.mean(axis=0)
    est_cov = np.cov(samples.T)
    mu_err = float(np.linalg.norm(est_mu - mu))
    cov_err = float(np.linalg.norm(est_cov - Sigma))

    print("Mode 3 — Sampling / Langevin (2-D Gaussian target)")
    print(f"  drew {len(samples)} samples")
    print(f"  target mean {mu}      estimated {np.round(est_mu, 3)}   ‖Δ‖={mu_err:.3e}")
    print(f"  target cov  diag {np.diag(Sigma)}  estimated {np.round(np.diag(est_cov), 3)}")
    print(f"  [C: distributional] mean error={mu_err:.3e}, cov error={cov_err:.3e}")


if __name__ == "__main__":
    main()
