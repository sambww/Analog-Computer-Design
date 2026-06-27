"""The analog substrate's native operations.

These functions model — at the level of *behavior*, not physics — what the
Programmable Continuous Field of ``docs/03-analog-substrate.md`` does natively. Each
corresponds to one execution mode in ``docs/05-computational-model.md``:

- :func:`relax`  — Mode 1 (Relaxation):   descend an energy landscape to a minimum.
- :func:`evolve` — Mode 2 (Evolution):    integrate continuous-time dynamics forward.
- :func:`sample` — Mode 3 (Sampling):     visit states with probability ``∝ exp(-E/T)``.

On real hardware these are *physical events*, not algorithms; here we step them on a
digital host so they can be inspected and verified. The forward-Euler stepping stands in
for the substrate's continuous-time settling — fidelity, not speed, is the point.

Noise is a first-class input, mirroring the design tenet "noise is a resource, not only a
flaw" (``docs/01`` tenet 4): an annealed-noise schedule in :func:`relax` lets the descent
escape local minima, and sustained noise in :func:`sample` *is* the sampler.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np


@dataclass
class RelaxTrace:
    """What the substrate reports back after a relaxation run."""

    x: np.ndarray            # settled continuous state
    energy: float            # final energy E(x)
    energy_history: list = field(default_factory=list)


def relax(
    grad_energy: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    *,
    energy: Callable[[np.ndarray], float] | None = None,
    steps: int = 4000,
    dt: float = 0.01,
    noise0: float = 0.0,
    anneal: float = 0.0,
    clip: float | None = None,
    rng: np.random.Generator | None = None,
) -> RelaxTrace:
    """Mode 1 — descend an energy landscape ``E`` via gradient flow ``dx/dt = -∇E``.

    With ``noise0 > 0`` the descent is a Langevin-style anneal: the injected noise starts
    at ``noise0`` and decays as ``noise0 * exp(-anneal * t/steps)``, so the state can hop
    out of shallow local minima early and settle into a deep one as the noise cools. This
    is the simulated-annealing / Hopfield / Ising-machine behavior of ``docs/03``.

    ``clip`` bounds the state to ``[-clip, clip]`` (the saturating nonlinearity of a real
    analog medium). Returns the settled state and an energy history for inspection.
    """
    rng = np.random.default_rng() if rng is None else rng
    x = np.array(x0, dtype=float)
    history: list = []
    for t in range(steps):
        x = x - dt * grad_energy(x)
        if noise0 > 0.0:
            temp = noise0 * np.exp(-anneal * t / max(steps, 1))
            x = x + np.sqrt(2.0 * temp * dt) * rng.standard_normal(x.shape)
        if clip is not None:
            np.clip(x, -clip, clip, out=x)
        if energy is not None and (t % 50 == 0 or t == steps - 1):
            history.append(float(energy(x)))
    final_e = float(energy(x)) if energy is not None else float("nan")
    return RelaxTrace(x=x, energy=final_e, energy_history=history)


def evolve(
    dynamics: Callable[[float, np.ndarray], np.ndarray],
    y0: np.ndarray,
    *,
    t_span: tuple[float, float],
    steps: int = 2000,
) -> tuple[np.ndarray, np.ndarray]:
    """Mode 2 — integrate ``dy/dt = f(t, y)`` forward in continuous time.

    This is the op-amp-integrator behavior of ``docs/03``: the substrate *embodies* the
    dynamics and the answer is its trajectory. We use a 4th-order Runge–Kutta step as a
    faithful stand-in for the medium's continuous settling.

    Returns ``(times, ys)`` where ``ys[i]`` is the state at ``times[i]``.
    """
    t0, t1 = t_span
    ts = np.linspace(t0, t1, steps + 1)
    h = (t1 - t0) / steps
    y = np.array(y0, dtype=float)
    ys = np.empty((steps + 1, *y.shape))
    ys[0] = y
    for i in range(steps):
        t = ts[i]
        k1 = dynamics(t, y)
        k2 = dynamics(t + 0.5 * h, y + 0.5 * h * k1)
        k3 = dynamics(t + 0.5 * h, y + 0.5 * h * k2)
        k4 = dynamics(t + h, y + h * k3)
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        ys[i + 1] = y
    return ts, ys


def sample(
    grad_energy: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    *,
    temperature: float,
    steps: int = 20000,
    dt: float = 0.005,
    burn_in: int = 2000,
    thin: int = 5,
    rng: np.random.Generator | None = None,
) -> np.ndarray:
    """Mode 3 — draw samples ``∝ exp(-E/T)`` via overdamped Langevin dynamics.

    ``dx = -∇E(x) dt + sqrt(2 T dt) η``. Sustained thermal noise turns the relaxation of
    Mode 1 into a sampler — the native Monte-Carlo / Bayesian-inference behavior cited in
    ``docs/03`` (thermodynamic computing) and ``docs/05`` (Mode 3).

    Returns the collected samples after discarding ``burn_in`` steps and thinning by
    ``thin`` (to reduce autocorrelation).
    """
    rng = np.random.default_rng() if rng is None else rng
    x = np.array(x0, dtype=float)
    samples: list = []
    scale = np.sqrt(2.0 * temperature * dt)
    for t in range(steps):
        x = x - dt * grad_energy(x) + scale * rng.standard_normal(x.shape)
        if t >= burn_in and (t - burn_in) % thin == 0:
            samples.append(x.copy())
    return np.array(samples)


@dataclass
class Substrate:
    """A thin object wrapper so demos can read like ``substrate.relax(...)``.

    Holds a seeded RNG so a whole run is reproducible (Class-A/B/C reproducibility in
    ``docs/07`` is about *statistics*, and a fixed seed makes the sim itself repeatable).
    """

    seed: int | None = None

    def __post_init__(self) -> None:
        self.rng = np.random.default_rng(self.seed)

    def relax(self, grad_energy, x0, **kw) -> RelaxTrace:
        kw.setdefault("rng", self.rng)
        return relax(grad_energy, x0, **kw)

    def evolve(self, dynamics, y0, **kw):
        return evolve(dynamics, y0, **kw)

    def sample(self, grad_energy, x0, **kw) -> np.ndarray:
        kw.setdefault("rng", self.rng)
        return sample(grad_energy, x0, **kw)
