"""The agent control plane.

This models the outer loop of ``docs/04-ai-agent-layer.md``: the agent does *not* compute
the answer step by step. It **configures** a substrate primitive, lets the physics run,
**measures** a residual, **refines** if the result is not yet good enough, and finally
**certifies** the answer — attaching an error bound and a reproducibility class, exactly as
``docs/07-io-and-interfacing.md`` §5 requires. "Approximate-and-verify" (``docs/01`` tenet 5)
is the whole point: the substrate gives a fast approximate answer; this layer checks it.

The agent here is deliberately simple (a retry-with-more-effort loop, not an LLM). The
design claim it embodies is structural: *intelligence aims the physics and verifies it;
physics does the descending.*
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable


class ReproClass(str, Enum):
    """Reproducibility classes from ``docs/07-io-and-interfacing.md`` §5."""

    A = "A: verified-exact"          # refined/checked until a hard tolerance is met
    B = "B: bounded-approximate"     # answer with a stated error bound
    C = "C: distributional"          # a sample / distribution; reproducible in statistics


@dataclass
class Result:
    """A certified answer. Never present a B/C result as if it were A (``docs/01`` tenet 8)."""

    value: Any
    error: float
    repro_class: ReproClass
    accepted: bool
    attempts: int
    note: str = ""

    def __str__(self) -> str:
        ok = "accepted" if self.accepted else "NOT accepted"
        return (
            f"[{self.repro_class.value}] {ok} after {self.attempts} attempt(s); "
            f"residual/error = {self.error:.3e}"
            + (f"  ({self.note})" if self.note else "")
        )


@dataclass
class Agent:
    """Wraps a substrate run in configure -> run -> measure -> refine -> certify."""

    max_attempts: int = 4

    def solve(
        self,
        run: Callable[[int], Any],
        residual: Callable[[Any], float],
        *,
        tol: float,
        repro_class: ReproClass = ReproClass.A,
        note: str = "",
    ) -> Result:
        """Run ``run(attempt)``, measure ``residual(candidate)``, and refine until ``tol``.

        ``run`` receives the attempt index (0-based) so it can spend more effort on retries
        — more relaxation steps, a hotter/longer anneal, etc. This is the agent's
        "re-aim and re-run" behavior from ``docs/04`` §4. Returns the best candidate seen
        with its measured error and reproducibility class.
        """
        best_value: Any = None
        best_err = float("inf")
        attempts = 0
        for attempt in range(self.max_attempts):
            attempts = attempt + 1
            candidate = run(attempt)
            err = residual(candidate)
            if err < best_err:
                best_err, best_value = err, candidate
            if err <= tol:
                return Result(best_value, best_err, repro_class, True, attempts, note)
        return Result(best_value, best_err, repro_class, False, attempts, note)
