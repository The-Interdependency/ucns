"""
Compatibility shim for the v0.6.5 reference snapshot.

The snapshot lives in ``ucns-code-v065.py`` (with dashes), which is not a
valid Python module name. Some proof / verification scripts import the
snapshot as ``ucns_code_v065``. This module loads the dash-named file and
re-exports its public symbols.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

_SNAPSHOT_PATH = Path(__file__).with_name("ucns-code-v065.py")

_spec = importlib.util.spec_from_file_location(
    "ucns_code_v065_snapshot", _SNAPSHOT_PATH
)
if _spec is None or _spec.loader is None:  # pragma: no cover
    raise ImportError(f"Unable to load snapshot module at {_SNAPSHOT_PATH}")

_module: ModuleType = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

for _name in dir(_module):
    if _name.startswith("_"):
        continue
    globals()[_name] = getattr(_module, _name)

# Prefer the canonical ucns_recursive algebra types for compatibility with
# scripts that combine snapshot helpers with the active implementation.
from functools import reduce  # noqa: E402

from ucns_recursive.canonical import UCNSObject as _CanonicalUCNSObject  # noqa: E402
from ucns_recursive.canonical import lcm as _lcm  # noqa: E402
from ucns_recursive.canonical import multiply as multiply  # noqa: E402


def UCNSObject(  # type: ignore[misc]
    n_dec: int,
    n_min: int,
    A_plus,
    F_plus,
):
    """Build a canonical UCNSObject while widening ``n_dec`` if needed.

    Some legacy proof scripts construct objects with a too-small ``n_dec``.
    The canonical UCNSObject enforces ``n_dec % n_min == 0`` after
    normalization; here we widen ``n_dec`` to the minimal compatible carrier.
    """
    if not A_plus:
        return _CanonicalUCNSObject(n_dec, n_min, A_plus, F_plus)

    theta0 = A_plus[0][0]
    shifted_angles = [((theta - theta0) % 4) for theta, _ in A_plus]
    circle_fracs = [((a % 2) / 2) for a in shifted_angles]
    denoms = [f.denominator for f in circle_fracs if f != 0]
    inferred_n_min = reduce(_lcm, denoms) if denoms else 1

    widened_n_dec = _lcm(n_dec, inferred_n_min)
    return _CanonicalUCNSObject(widened_n_dec, widened_n_dec, A_plus, F_plus)

__all__ = [name for name in globals() if not name.startswith("_")]
