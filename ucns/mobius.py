"""Legacy Poincaré-disk and bilinear-transform compatibility utilities.

This module implements classical complex-analytic Möbius transformations of an
ordinary unit disk. The word ``Möbius`` here names the bilinear transformation
family; it does **not** model the canonical public-gonol Möbius twist, fixed
SPACE/ZERO origin, orientation state, or 720-degree complete return.

Angles accepted by this module are conventional local ``2π`` coordinates for
legacy visualization and embedding helpers. They are not public-gonol
positions, and no bridge from this disk model to the public gonol is defined.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_mobius
#   module_name: mobius
#   module_kind: adapter
#   summary: legacy Poincare-disk and bilinear-transform helpers over local 2pi coordinates; explicitly not the public-gonol Mobius twist or UCNS complete-return geometry
#   owner: Erin Spencer
#   public_surface: MobiusTransform, poincare_distance, disk_to_circle, circle_to_disk
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_mobius, tests.test_public_gonol_claim_guard
#   rollout: compatibility_only
#   rollback: remove after legacy disk/visualization consumers migrate to explicitly named application geometry
#   requires: none
#   since: 2026-06-02
#   unresolved: no bridge from this local disk geometry to the fixed-origin public gonol is defined
# === END MODULE_BUILD ===

import cmath
import math

__all__ = ["MobiusTransform", "poincare_distance", "disk_to_circle", "circle_to_disk"]

_TAU = 2.0 * math.pi


class MobiusTransform:
    """Classical conformal automorphism of the open unit disk.

    Parameters
    ----------
    a:
        Translation parameter. Must satisfy ``|a| < 1``.
    phi:
        Conventional local rotation parameter in radians, reduced modulo
        ``2π``. This parameter does not represent UCNS public-frame rotation or
        complete return.
    """

    __slots__ = ("a", "phi")

    def __init__(self, a: complex, phi: float = 0.0) -> None:
        if abs(a) >= 1.0:
            raise ValueError(
                f"|a| must be strictly less than 1; got |a| = {abs(a):.6f}"
            )
        self.a = complex(a)
        self.phi = float(phi) % _TAU

    def __call__(self, z: complex) -> complex:
        """Apply the classical disk transform ``T(z)``."""

        denom = 1.0 - self.a.conjugate() * z
        if abs(denom) < 1e-15:
            raise ValueError("z is the image of infinity under this transform")
        return cmath.exp(1j * self.phi) * (z - self.a) / denom

    def inverse(self) -> "MobiusTransform":
        """Return the inverse classical disk transform."""

        return MobiusTransform(
            -self.a * cmath.exp(1j * self.phi),
            -self.phi,
        )

    def compose(self, other: "MobiusTransform") -> "MobiusTransform":
        """Return ``self ∘ other`` within the local disk model."""

        a_new = self(other(0j))
        p = other(0.5 + 0j)
        q = self(p)
        out = q
        raw = (out - a_new) / (1.0 - a_new.conjugate() * out)
        phi_new = cmath.phase(raw) if abs(raw) > 1e-15 else 0.0
        return MobiusTransform(a_new, phi_new)

    def hyperbolic_distance(self, z: complex, w: complex) -> float:
        """Return the Poincaré-disk distance in this local model."""

        return poincare_distance(z, w)

    def __repr__(self) -> str:
        return f"MobiusTransform(a={self.a:.4f}, phi={self.phi:.4f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MobiusTransform):
            return NotImplemented
        return (
            abs(self.a - other.a) < 1e-9
            and abs(self.phi - other.phi) < 1e-9
        )


def poincare_distance(z: complex, w: complex) -> float:
    """Hyperbolic distance between two points in the open Poincaré disk.

    This is a classical local-disk metric, not a distance on the public gonol.
    """

    for name, point in (("z", z), ("w", w)):
        if abs(point) >= 1.0:
            raise ValueError(
                f"Point {name} = {point} lies outside or on the unit disk boundary"
            )
    denom = 1.0 - w.conjugate() * z
    if abs(denom) < 1e-15:
        return float("inf")
    rho = abs((z - w) / denom)
    rho = min(rho, 1.0 - 1e-15)
    return 2.0 * math.atanh(rho)


def disk_to_circle(z: complex) -> float:
    """Return the local radial-boundary phase of a disk point.

    The result lies in ``[0, 2π)`` and is a compatibility coordinate only. It
    is not a public-gonol position and does not preserve the 720-degree
    orientation return.
    """

    if abs(z) < 1e-15:
        return 0.0
    return cmath.phase(z) % _TAU


def circle_to_disk(theta: float, r: float = 0.5) -> complex:
    """Place a local 2π phase inside the open disk at radius ``r``.

    This helper does not embed or reconstruct the canonical public gonol.
    """

    if not (0.0 < r < 1.0):
        raise ValueError("r must be in (0, 1)")
    return r * cmath.exp(1j * theta)
