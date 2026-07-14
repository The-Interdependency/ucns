"""
ucns.geometry_bridge
================================
Commutative audit projection from UCNS-A into UCNS-G coordinates.

The bridge deliberately separates:

    rho       recursive radius / payload depth.
              rho(A box B) = max(rho(A), rho(B)).

    r         backward-compatible storage name for breadth lambda.
    lambda    breadth valuation log(len(A_plus)).
              lambda(A box B) = lambda(A) + lambda(B).

    theta     circular mean angle on R/4piZ.

    (z, w)    two-bit chirality state.

The enriched target (rho, lambda, theta, z, w) remains commutative. It is a
projection of any future nonabelian quaternionic lift, not that lift: it does
not retain SU(2) axis data and remains blind to the UCNS commutator.

Public API:
    GeometricPoint
    ucns_a_to_g
    compose
    homomorphism_check
    HomomorphismResult
    check_injectivity
    ThetaDegenerate
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple

from .canonical import multiply as _canonical_multiply
from .relational_geometry import breadth as _breadth
from .relational_geometry import recursive_radius as _recursive_radius

# === MODULE_BUILD ===
# id: ucns_geometry_bridge
#   module_name: geometry_bridge
#   module_kind: engine
#   summary: commutative audit projection via recursive radius, breadth, spinor angle, and chirality coordinates
#   owner: Erin Spencer
#   public_surface: GeometricPoint, ucns_a_to_g, compose, homomorphism_check, HomomorphismResult, check_injectivity
#   internal_surface: _r, _rho, _theta, _zw, ThetaDegenerate
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive.tests.test_geometry_bridge, contracts.test_local_groups_and_geometry
#   rollout: default_enabled
#   rollback: remove export from ucns/__init__.py
#   requires: ucns.canonical, ucns.relational_geometry
#   unresolved: injectivity-proof-analytical, degenerate-theta-canonical-form, quaternionic-axis-lift
# === END MODULE_BUILD ===

__all__ = [
    "GeometricPoint",
    "ucns_a_to_g",
    "compose",
    "homomorphism_check",
    "HomomorphismResult",
    "check_injectivity",
    "ThetaDegenerate",
]

_TAU4 = 4.0 * math.pi
_TOL = 1e-9


class ThetaDegenerate(Exception):
    """The circular mean of an object's angles is undefined."""


@dataclass(frozen=True, eq=False)
class GeometricPoint:
    """Commutative audit coordinates ``(rho, lambda, theta, z, w)``.

    ``r`` is retained as the backward-compatible field name for breadth
    ``lambda = log(len(A_plus))``. Use ``breadth`` in new prose and code.
    """

    r: float
    theta: Optional[float]
    z: int
    w: int
    rho: int = 0

    def __post_init__(self) -> None:
        if self.r < 0:
            raise ValueError("r/breadth must be non-negative; got {0}".format(self.r))
        if not isinstance(self.rho, int) or isinstance(self.rho, bool) or self.rho < 0:
            raise ValueError("rho must be a non-negative integer; got {0!r}".format(self.rho))
        if self.z not in (0, 1):
            raise ValueError("z must be 0 or 1; got {0}".format(self.z))
        if self.w not in (0, 1):
            raise ValueError("w must be 0 or 1; got {0}".format(self.w))
        if self.theta is not None:
            object.__setattr__(self, "theta", float(self.theta) % _TAU4)

    @property
    def breadth(self) -> float:
        """Correct name for the backward-compatible ``r`` field."""
        return self.r

    @property
    def lambda_value(self) -> float:
        """ASCII-safe alias for breadth lambda."""
        return self.r

    @property
    def is_degenerate(self) -> bool:
        return self.theta is None

    @property
    def chirality(self) -> int:
        return 1 if self.z == 0 else -1

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GeometricPoint):
            return NotImplemented
        if self.rho != other.rho or self.z != other.z or self.w != other.w:
            return False
        if abs(self.r - other.r) >= _TOL:
            return False
        if self.theta is None and other.theta is None:
            return True
        if self.theta is None or other.theta is None:
            return False
        diff = abs(self.theta - other.theta) % _TAU4
        return min(diff, _TAU4 - diff) < _TOL

    __hash__ = None

    def __repr__(self) -> str:
        theta = "{0:.6f}".format(self.theta) if self.theta is not None else "None(deg)"
        return (
            "GeometricPoint(rho={0}, breadth={1:.6f}, theta={2}, z={3}, w={4})"
            .format(self.rho, self.r, theta, self.z, self.w)
        )


def _r(obj: Any) -> float:
    """Backward-compatible breadth extractor."""
    return _breadth(obj)


def _rho(obj: Any) -> int:
    return _recursive_radius(obj)


def _theta(obj: Any) -> Optional[float]:
    """Circular mean angle on R/4piZ. None when degenerate."""
    if obj is None or not obj.A_plus:
        return 0.0
    vectors = [cmath.exp(1j * math.pi * float(a) / 2) for a, _ in obj.A_plus]
    mean_vec = sum(vectors) / len(vectors)
    if abs(mean_vec) < _TOL:
        return None
    halfturns = (cmath.phase(mean_vec) % (2 * math.pi)) * 2 / math.pi
    return halfturns * math.pi


def _zw(obj: Any) -> Tuple[int, int]:
    if obj is None:
        return (0, 0)
    return (sum(obj.F_plus) % 2, len(obj.A_plus) % 2)


def ucns_a_to_g(obj: Any) -> GeometricPoint:
    """Map a UCNSObject to its commutative audit projection."""
    z, w = _zw(obj)
    return GeometricPoint(
        r=_r(obj),
        theta=_theta(obj),
        z=z,
        w=w,
        rho=_rho(obj),
    )


def compose(p: GeometricPoint, q: GeometricPoint) -> GeometricPoint:
    """Compose projected coordinates.

    Radius uses max; breadth uses addition; theta uses addition modulo 4pi.
    """
    theta_new = (
        None
        if p.theta is None or q.theta is None
        else (p.theta + q.theta) % _TAU4
    )
    return GeometricPoint(
        r=p.r + q.r,
        theta=theta_new,
        z=(p.z * q.w + p.w * q.z) % 2,
        w=(p.w * q.w) % 2,
        rho=max(p.rho, q.rho),
    )


@dataclass
class HomomorphismResult:
    """Diagnostic result for one audit-projection homomorphism check."""

    holds: bool
    lhs: GeometricPoint
    rhs: GeometricPoint
    r_match: bool
    theta_match: bool
    zw_match: bool
    degenerate: bool
    delta_r: float
    delta_theta: Optional[float]

    @property
    def breadth_match(self) -> bool:
        return self.r_match

    @property
    def rho_match(self) -> bool:
        return self.lhs.rho == self.rhs.rho

    @property
    def delta_rho(self) -> int:
        return abs(self.lhs.rho - self.rhs.rho)

    def __repr__(self) -> str:
        status = "DEGENERATE" if self.degenerate else ("HOLDS" if self.holds else "FAILS")
        parts = [status]
        if not self.rho_match:
            parts.append("delta_rho={0}".format(self.delta_rho))
        if not self.r_match:
            parts.append("delta_lambda={0:.2e}".format(self.delta_r))
        if not self.theta_match and self.delta_theta is not None:
            parts.append("delta_theta={0:.2e}".format(self.delta_theta))
        if not self.zw_match:
            parts.append("zw_MISMATCH")
        return "HomomorphismResult(" + " | ".join(parts) + ")"


def homomorphism_check(a: Any, b: Any, multiply_fn: Any = None) -> HomomorphismResult:
    """Check projection(a box b) == compose(projection(a), projection(b))."""
    mult = multiply_fn if multiply_fn is not None else _canonical_multiply
    lhs = ucns_a_to_g(mult(a, b))
    rhs = compose(ucns_a_to_g(a), ucns_a_to_g(b))

    delta_r = abs(lhs.r - rhs.r)
    r_match = delta_r < _TOL
    degenerate = lhs.is_degenerate or rhs.is_degenerate
    if degenerate:
        theta_match = lhs.is_degenerate == rhs.is_degenerate
        delta_theta = None
    else:
        assert lhs.theta is not None and rhs.theta is not None
        diff = abs(lhs.theta - rhs.theta) % _TAU4
        delta_theta = min(diff, _TAU4 - diff)
        theta_match = delta_theta < _TOL

    zw_match = lhs.z == rhs.z and lhs.w == rhs.w
    holds = lhs.rho == rhs.rho and r_match and theta_match and zw_match
    return HomomorphismResult(
        holds=holds,
        lhs=lhs,
        rhs=rhs,
        r_match=r_match,
        theta_match=theta_match,
        zw_match=zw_match,
        degenerate=degenerate,
        delta_r=delta_r,
        delta_theta=delta_theta,
    )


def check_injectivity(objects: List[Any]) -> dict:
    """Check projection injectivity over a supplied finite collection."""
    seen = {}
    collisions = []
    for obj in objects:
        point = ucns_a_to_g(obj)
        key = (
            point.rho,
            round(point.r, 9),
            round(point.theta, 9) if point.theta is not None else None,
            point.z,
            point.w,
        )
        if key in seen:
            collisions.append((seen[key], obj, point))
        else:
            seen[key] = obj
    return {
        "injective": len(collisions) == 0,
        "total": len(seen) + len(collisions),
        "collisions": collisions,
    }
