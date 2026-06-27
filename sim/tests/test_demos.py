"""Convergence tests for the Continuum Engine demos.

Each test asserts that a substrate primitive, driven by the agent loop, reaches the
known-correct answer within tolerance. RNG seeds are fixed so the suite is deterministic.
Run:  python -m pytest tests/ -q     (from the sim/ directory)
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from demos import demo_optimization as opt   # noqa: E402
from demos import demo_ode as ode             # noqa: E402
from demos import demo_sampling as smp        # noqa: E402


def test_maxcut_reaches_optimum():
    """Mode 1: annealed relaxation should find the true Max-Cut optimum on a tiny graph."""
    W = opt.make_graph(n=10, seed=7)
    result, optimum = opt.solve_maxcut(W, seed=1)
    assert result.accepted, f"did not reach optimum; residual={result.error}"
    assert result.error < 1e-9


def test_linear_solve_residual_small():
    """Mode 1: gradient-flow linear solve should drive ‖Ax-b‖ under tolerance (Class A)."""
    A = ode.make_spd(n=8, seed=3)
    rng = np.random.default_rng(11)
    x_true = rng.standard_normal(A.shape[0])
    b = A @ x_true
    result = ode.solve_linear(A, b, seed=2)
    assert result.accepted
    assert result.error < 1e-6
    assert np.linalg.norm(result.value - x_true) < 1e-4


def test_oscillator_matches_analytic():
    """Mode 2: integrated trajectory should match the closed-form damped oscillator."""
    _, _, _, max_err = ode.damped_oscillator(seed=1)
    assert max_err < 1e-3, f"trajectory error too large: {max_err}"


def test_sampler_matches_target_statistics():
    """Mode 3: Langevin samples should reproduce the target mean and covariance (Class C)."""
    mu = np.array([1.5, -0.5])
    Sigma = np.array([[1.0, 0.6], [0.6, 0.8]])
    samples = smp.gaussian_sampler(mu, Sigma, seed=1)
    est_mu = samples.mean(axis=0)
    est_cov = np.cov(samples.T)
    assert np.linalg.norm(est_mu - mu) < 0.15
    assert np.linalg.norm(est_cov - Sigma) < 0.25
