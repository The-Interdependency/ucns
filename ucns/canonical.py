"""
ucns.canonical
========================
Core UCNS algebraic objects.

UCNSObject               The fundamental recursive sequence object.
multiply                 Ordered-concatenation product  A ⊠ B.
is_unit                  True iff obj is the sequence identity (length-1,
                         angle 0, no payload, F=[0]).
is_multiplicative_unit   True iff obj is in the multiplicative unit group
                         (length-1, no payload, any face bit). These elements
                         are self-inverse: u ⊠ u = identity.

This module is the stable algebraic foundation; it does not contain any
factorization or quotient logic.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_canonical
#   module_name: canonical
#   module_kind: engine
#   summary: Core UCNS algebraic objects and operations - UCNSObject, the ordered-concatenation product, and unit predicates.
#   owner: Erin Spencer
#   public_surface: UCNSObject, multiply, is_unit, is_multiplicative_unit, lcm, UNIT
#   internal_surface: normalize, _compute_n_min, _star, _disk_flip
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive/tests/test_depth2_full_domain.py, ucns_recursive/tests/test_canonical_constructor_validation.py, tests/test_canonical_constructor_validation.py
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: none
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: multiply_well_defined
#   given: normalized nonempty UCNSObjects at mixed depths, plus gauge-shifted
#          and n_dec-varied raw representations of the same objects
#   then:  multiply is total, its output is normalized with n_dec a multiple of
#          n_min, len multiplies, and the product depends only on the
#          equality class of each operand (representation independence)
#   class: correctness
#   call:  contracts.test_multiply_canonical.contract_multiply_well_defined
#
# id: multiply_identity
#   given: the theta=0 origin e = UCNSObject(1, 1, [(0, None)], [0]) and
#          arbitrary normalized objects a
#   then:  multiply(e, a) == a and multiply(a, e) == a (two-sided, checked
#          separately); the None sentinel behaves identically; the face-1
#          unit u1 is NOT an identity but is self-inverse
#   class: correctness
#   call:  contracts.test_identity_two_sided.contract_multiply_identity
#
# id: multiply_associativity
#   given: TRIPLES of normalized objects at mixed depths, including
#          adversarial mixed-None payloads, towers, and degenerate-theta
#          objects
#   then:  multiply(multiply(a, b), c) == multiply(a, multiply(b, c));
#          the object carries its full angle sequence, so the circular-mean
#          collapse feared in the O3 manifest lives only in the
#          geometry_bridge projection, never in the algebra
#   class: correctness
#   call:  contracts.test_associativity_triples.contract_multiply_associativity
#
# id: multiply_commutativity_ruling
#   given: normalized objects; the separating witnesses B1 = [0,1] and
#          B2 = [0,2]
#   then:  multiply is non-commutative in general; the (r, theta, z, w)
#          projection always commutes (the commutator lives in sequence
#          ordering, not chirality); the center is exactly the unit towers
#   class: correctness
#   call:  contracts.test_commutator.contract_multiply_commutativity_ruling
#
# id: structure_naming
#   given: obligations O1-O5 discharged (well-definedness, identity,
#          associativity, commutativity ruling, division theory)
#   then:  (nonempty normalized objects, multiply, e) is a non-commutative,
#          non-cancellative monoid graded by length (r = log len additive),
#          with unit group of order 2 and center the unit towers
#   class: correctness
#   call:  contracts.test_structure_axioms.contract_structure_naming
#
# id: addition_boundary
#   given: the derived candidate addition (top-level sequence concatenation)
#          and the r valuation
#   then:  no second primitive operation exists in the base geometry; r is
#          additive under multiply alone; derived concatenation is
#          associative and right-distributive over multiply but left
#          distributivity fails, so it earns no primitive status
#   class: correctness
#   call:  contracts.test_addition_boundary.contract_addition_boundary
# === END CONTRACTS ===

import copy
from fractions import Fraction
from functools import reduce
from math import gcd
from numbers import Integral
from typing import List, Optional, Tuple

__all__ = [
    "UCNSObject",
    "multiply",
    "is_unit",
    "is_multiplicative_unit",
    "lcm",
    "UNIT",
]

# Sentinel for the unit / empty payload
UNIT = None

FractionType = Fraction


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b) if a and b else 0


class UCNSObject:
    """A UCNS sequence object.

    Parameters
    ----------
    n_dec:
        Declared carrier size (must be a multiple of n_min).
    n_min:
        Intrinsic carrier size (LCM of angle denominators).
    A_plus:
        Sequence of (angle, payload) pairs.  ``angle`` is a
        ``Fraction`` in ``[0, 4)`` (representing a fraction of a
        half-turn on the pairing circle); ``payload`` is another
        ``UCNSObject`` or ``None`` (unit payload).
    F_plus:
        Face-flip sequence parallel to ``A_plus`` (list of 0/1 ints).
    """

    __slots__ = ("n_dec", "n_min", "A_plus", "F_plus", "A_minus", "F_minus")

    def __init__(
        self,
        n_dec: int,
        n_min: int,
        A_plus: List[Tuple[FractionType, Optional["UCNSObject"]]],
        F_plus: List[int],
    ) -> None:
        if len(A_plus) != len(F_plus):
            raise ValueError(
                "Invalid object: A_plus and F_plus must have the same length "
                f"(got {len(A_plus)} and {len(F_plus)})."
            )
        invalid_faces = [
            f
            for f in F_plus
            if not isinstance(f, Integral) or int(f) not in (0, 1)
        ]
        if invalid_faces:
            raise ValueError(
                "Invalid object: F_plus entries must be face bits 0 or 1 "
                f"(got {invalid_faces!r})."
            )

        self.n_dec = n_dec
        self.n_min = n_min
        self.A_plus: List[Tuple[FractionType, Optional[UCNSObject]]] = [
            (a, copy.deepcopy(p) if p is not None else None) for a, p in A_plus
        ]
        self.F_plus: List[int] = [int(f) for f in F_plus]
        self.A_minus: Optional[List] = None
        self.F_minus: Optional[List] = None
        self.normalize()

    # ------------------------------------------------------------------
    # Normalization
    # ------------------------------------------------------------------

    def normalize(self) -> "UCNSObject":
        if not self.A_plus:
            return self
        theta0 = self.A_plus[0][0]
        shifted = []
        for theta, payload in self.A_plus:
            new_theta = (theta - theta0) % 4
            new_payload = payload.normalize() if payload is not None else None
            shifted.append((new_theta, new_payload))
        self.A_plus = shifted
        angles = [a for a, _ in self.A_plus]
        self.n_min = self._compute_n_min(angles)
        self.A_minus, self.F_minus = self._star()
        if self.n_dec % self.n_min != 0:
            raise ValueError(
                f"Invalid object: n_dec={self.n_dec} not multiple of n_min={self.n_min}"
            )
        return self

    def _compute_n_min(self, angles: List[FractionType]) -> int:
        if not angles:
            return 1
        circle_fracs = [((a % 2) / 2) for a in angles]
        denoms = [f.denominator for f in circle_fracs if f != 0]
        if not denoms:
            return 1
        return reduce(lcm, denoms)

    def _star(self) -> Tuple[List, List]:
        rev = list(reversed(self.A_plus))
        starred_A = []
        for theta, payload in rev:
            new_theta = (-theta) % 4
            new_payload = self._disk_flip(payload) if payload is not None else None
            starred_A.append((new_theta, new_payload))
        starred_F = list(reversed(self.F_plus))
        return starred_A, starred_F

    @staticmethod
    def _disk_flip(obj: Optional["UCNSObject"]) -> Optional["UCNSObject"]:
        if obj is None:
            return None
        obj = copy.deepcopy(obj).normalize()
        flipped = UCNSObject(
            obj.n_dec,
            obj.n_min,
            copy.deepcopy(obj.A_minus),
            obj.F_minus[:],
        )
        return flipped.normalize()

    # ------------------------------------------------------------------
    # Equality
    # ------------------------------------------------------------------

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UCNSObject):
            return False
        if self.n_min != other.n_min or len(self.A_plus) != len(other.A_plus):
            return False
        for (a1, p1), (a2, p2) in zip(self.A_plus, other.A_plus):
            if a1 != a2:
                return False
            if (p1 is None) != (p2 is None):
                return False
            if p1 is not None and p1 != p2:
                return False
        return self.F_plus == other.F_plus

    def __hash__(self) -> int:
        def _payload_key(p: Optional["UCNSObject"]) -> object:
            return None if p is None else (p.n_min, tuple(p.F_plus), tuple(
                (a, _payload_key(pl)) for a, pl in p.A_plus
            ))
        return hash((
            self.n_min,
            tuple(self.F_plus),
            tuple((a, _payload_key(pl)) for a, pl in self.A_plus),
        ))

    def __repr__(self) -> str:
        return f"UCNS(n_min={self.n_min}, L={len(self.A_plus)})"


# ------------------------------------------------------------------
# Product
# ------------------------------------------------------------------

def multiply(
    A: Optional[UCNSObject], B: Optional[UCNSObject]
) -> Optional[UCNSObject]:
    """Ordered-concatenation product  A ⊠ B.

    If either factor is ``None`` (unit), the other factor is returned
    unchanged.  This makes ``None`` the identity element.
    """
    if A is None or B is None:
        return A if B is None else B
    p, q = len(A.A_plus), len(B.A_plus)
    n_dec_new = lcm(A.n_dec, B.n_dec)
    n_min_new = lcm(A.n_min, B.n_min)
    new_A_plus: List[Tuple[FractionType, Optional[UCNSObject]]] = []
    new_F_plus: List[int] = []
    beta0 = B.A_plus[0][0]
    for k in range(p):
        alpha_k = A.A_plus[k][0]
        S_k_A = A.A_plus[k][1]
        f_k_A = A.F_plus[k]
        for j in range(q):
            beta_j = B.A_plus[j][0]
            S_j_B = B.A_plus[j][1]
            f_j_B = B.F_plus[j]
            new_angle = (alpha_k + (beta_j - beta0)) % 4
            if S_k_A is not None and S_j_B is not None:
                new_payload: Optional[UCNSObject] = multiply(S_k_A, S_j_B)
            elif S_k_A is not None:
                new_payload = S_k_A
            else:
                new_payload = S_j_B
            new_f = f_k_A ^ f_j_B
            new_A_plus.append((new_angle, new_payload))
            new_F_plus.append(new_f)
    return UCNSObject(n_dec_new, n_min_new, new_A_plus, new_F_plus).normalize()


# ------------------------------------------------------------------
# Unit test
# ------------------------------------------------------------------

def is_unit(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is the sequence identity (length-1, angle 0,
    no payload, F=[0]).

    This is the narrow predicate: it identifies only the identity element
    of the multiplicative monoid. For the full unit group (the set of
    invertible elements), use :func:`is_multiplicative_unit`.
    """
    if obj is None:
        return True
    if not isinstance(obj, UCNSObject):
        return False
    if len(obj.A_plus) != 1:
        return False
    angle, payload = obj.A_plus[0]
    if angle != 0 or payload is not None:
        return False
    if obj.F_plus != [0] or obj.n_min != 1:
        return False
    return True


def is_multiplicative_unit(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is in the multiplicative unit group.

    The unit group of (UCNSObject, ⊠) consists of length-1 objects with
    UNIT payload and any face bit f ∈ {0, 1}. These elements are
    self-inverse: u ⊠ u equals the identity because XOR of any bit with
    itself is 0 and angles collapse to 0 in the length-1 product.

    Factorizations where one factor is in the unit group are degenerate
    (they only re-sign the other factor) and should be filtered out by
    primality predicates. :func:`is_unit` is the stricter "is the
    identity" predicate; this is the broader "is invertible" predicate.
    """
    if obj is None:
        return True
    if not isinstance(obj, UCNSObject):
        return False
    if len(obj.A_plus) != 1:
        return False
    _, payload = obj.A_plus[0]
    return payload is None
