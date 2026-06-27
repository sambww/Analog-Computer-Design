"""Continuum Engine — a conceptual simulation of the AI-agent-first analog computer.

This package does NOT pretend to be the speculative hardware described in ``docs/``.
It is a small, numpy-only *behavioral* model that lets you run the design's core ideas
and watch them converge to known-correct answers.

Two layers, mirroring the architecture in ``docs/02-architecture-overview.md``:

- :mod:`continuum.substrate` — the analog substrate's native operations as the three
  execution modes from ``docs/05-computational-model.md``:
  ``relax`` (Mode 1), ``evolve`` (Mode 2), ``sample`` (Mode 3).
- :mod:`continuum.agent` — the agent control plane from ``docs/04-ai-agent-layer.md``:
  it configures a substrate primitive, runs it, measures a residual, refines if needed,
  and returns a result tagged with an error bound and a reproducibility class
  (``docs/07-io-and-interfacing.md`` §5).
"""

from .substrate import Substrate, relax, evolve, sample
from .agent import Agent, Result, ReproClass

__all__ = [
    "Substrate",
    "relax",
    "evolve",
    "sample",
    "Agent",
    "Result",
    "ReproClass",
]
