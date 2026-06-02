"""
ucns.mobius
===========
Möbius (bilinear) transformations of the unit disk.

The **Poincaré disk model** represents the hyperbolic plane as the open unit
disk  D = {z ∈ ℂ : |z| < 1}.  Its boundary ∂D is the unit circle – the home
of every UCN.  Conformal automorphisms of D are Möbius transformations of the
form

    T_{a,φ}(z) = e^(iφ) · (z − a) / (1 − ā·z),   a ∈ D, φ ∈ ℝ.

These transformations:

* **preserve** the unit circle (boundary maps to boundary),
* **preserve** the hyperbolic (Poincaré) metric,
* compose to form the group Aut(D) ≅ PU(1,1).

Geometric intuition
-------------------
Think of the disk as a "rubber sheet" that can be stretched or compressed while
keeping the circular boundary fixed.  Embedding data on the interior of the
disk naturally encodes *hierarchical* relationships: nearby points are close in
hyperbolic distance; points near the boundary are conceptually "far out" (low
frequency, coarse-grained).  Combining this with the recursive epicycle
structure (see ``ucns.epicycle``) yields a multi-scale embedding space that
is simultaneously compact (unit circle) and hierarchical (Möbius disk).

References
----------
* Poincaré disk model – Wikipedia
* "Poincaré Embeddings for Learning Hierarchical Representations" – Nickel & Kiela 2017
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_mobius
#   module_name: mobius
#   module_kind: engine
#   summary: Mobius (bilinear) transformations of the Poincare unit disk plus hyperbolic-distance and disk/circle projection helpers.
#   owner: Erin Spencer
#   public_surface: MobiusTransform, poincare_distance, disk_to_circle, circle_to_disk
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_mobius
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: none
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

import cmath
import math

__all__ = ["MobiusTransform", "poincare_distance", "disk_to_circle", "circle_to_disk"]

_TAU = 2.0 * math.pi


class MobiusTransform:
    """A conformal automorphism of the open unit disk.

    Parameters
    ----------
    a:
        Translation parameter.  Must satisfy ``|a| < 1`` (interior of disk).
        The transformation maps ``a ↦ 0``.
    phi:
        Rotation angle in radians.  Applied after the translation.
    """

    __slots__ = ("a", "phi")

    def __init__(self, a: complex, phi: float = 0.0) -> None:
        if abs(a) >= 1.0:
            raise ValueError(
                f"|a| must be strictly less than 1; got |a| = {abs(a):.6f}"
            )
        self.a: complex = complex(a)
        self.phi: float = float(phi) % _TAU

    # ------------------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------------------

    def __call__(self, z: complex) -> complex:
        """Apply the transform: T(z) = e^(iφ) · (z − a) / (1 − ā·z)."""
        denom = 1.0 - self.a.conjugate() * z
        if abs(denom) < 1e-15:
            raise ValueError("z is the image of infinity under this transform")
        return cmath.exp(1j * self.phi) * (z - self.a) / denom

    # ------------------------------------------------------------------
    # Group structure
    # ------------------------------------------------------------------

    def inverse(self) -> "MobiusTransform":
        """Return T⁻¹ such that T⁻¹(T(z)) = z for all z ∈ D."""
        return MobiusTransform(
            -self.a * cmath.exp(1j * self.phi),
            -self.phi,
        )

    def compose(self, other: "MobiusTransform") -> "MobiusTransform":
        """Return the composed transform self ∘ other (apply *other* first)."""
        # Numerically stable composition via a sample point
        # We derive the new (a, phi) from where each transform sends 0.
        # T_composed sends 0 → self(other(0))
        a_new = self(other(0j))
        # Determine rotation by evaluating at a second point
        p = other(0.5 + 0j)
        q = self(p)
        # q = e^(i*phi_new) * (q_unnorm) → phi_new = arg(q / T_a_new(a_sample))
        t_check = MobiusTransform(a_new)
        sample = 0.5 + 0j
        out = q
        raw = (out - a_new) / (1.0 - a_new.conjugate() * out)
        phi_new = cmath.phase(raw) if abs(raw) > 1e-15 else 0.0
        return MobiusTransform(a_new, phi_new)

    # ------------------------------------------------------------------
    # Hyperbolic geometry
    # ------------------------------------------------------------------

    def hyperbolic_distance(self, z: complex, w: complex) -> float:
        """Poincaré disk metric  d(z, w) = 2·arctanh(|T_z(w)|).

        This is the intrinsic distance in the hyperbolic plane modelled by D.
        """
        return poincare_distance(z, w)

    # ------------------------------------------------------------------
    # Dunder
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"MobiusTransform(a={self.a:.4f}, phi={self.phi:.4f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MobiusTransform):
            return NotImplemented
        return (
            abs(self.a - other.a) < 1e-9
            and abs(self.phi - other.phi) < 1e-9
        )


# ------------------------------------------------------------------
# Standalone geometric helpers
# ------------------------------------------------------------------


def poincare_distance(z: complex, w: complex) -> float:
    """Hyperbolic distance between two points in the Poincaré disk.

    Parameters
    ----------
    z, w:
        Points in the open unit disk (``|z|, |w| < 1``).

    Returns
    -------
    float
        ``d(z, w) = 2·arctanh(|(z − w) / (1 − w̄·z)|)`` ≥ 0.
    """
    for name, p in (("z", z), ("w", w)):
        if abs(p) >= 1.0:
            raise ValueError(
                f"Point {name} = {p} lies outside or on the unit disk boundary"
            )
    denom = 1.0 - w.conjugate() * z
    if abs(denom) < 1e-15:
        return float("inf")
    rho = abs((z - w) / denom)
    rho = min(rho, 1.0 - 1e-15)  # guard against numerical overshoot
    return 2.0 * math.atanh(rho)


def disk_to_circle(z: complex) -> float:
    """Project a point *z* in the unit disk to its angle on ∂D (the unit circle).

    Uses the Cayley-like radial projection z ↦ z/|z| for z ≠ 0; for z = 0
    returns 0.  The returned angle θ ∈ [0, τ) gives the UCN associated with
    the boundary limit of the radial ray through *z*.
    """
    if abs(z) < 1e-15:
        return 0.0
    return cmath.phase(z) % _TAU


def circle_to_disk(theta: float, r: float = 0.5) -> complex:
    """Embed a unit-circle point (angle) into the interior of the disk at radius *r*.

    This is useful when you want to treat UCN angles as interior hyperbolic
    points (r < 1 keeps them strictly inside D).

    Parameters
    ----------
    theta:
        Angle on the unit circle (radians).
    r:
        Radial depth in (0, 1).  Defaults to 0.5.
    """
    if not (0.0 < r < 1.0):
        raise ValueError("r must be in (0, 1)")
    return r * cmath.exp(1j * theta)
