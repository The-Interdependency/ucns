"""
ucns.canonical
========================
Core UCNS algebraic objects.

UCNSObject               The fundamental recursive sequence object — a
                         recursively immutable canonical value.
multiply                 Ordered-concatenation product  A ⊠ B.
is_unit                  True iff obj is the sequence identity (length-1,
                         angle 0, no payload, F=(0,)).
is_multiplicative_unit   True iff obj is in the multiplicative unit group
                         (length-1, no payload, any face bit). These elements
                         are self-inverse: u ⊠ u = identity.

Value model (codex-handoff/05)
------------------------------
``UCNSObject`` is a recursively immutable canonical value object:

- construction rejects empty ``A_plus``/``F_plus`` — the runtime
  carrier is the NONEMPTY normalized object set, and an empty object
  cannot be manufactured through the public API;
- inputs may be any sequences; storage is canonical tuples
  (``A_plus``, ``F_plus``, ``A_minus``, ``F_minus``);
- angles are converted deliberately to ``Fraction`` (``Fraction`` or
  ``int`` accepted; floats, booleans, and other types rejected) and
  gauge-normalized into ``[0, 4)`` at construction;
- face bits are exact integers ``0``/``1`` (booleans rejected);
- carrier arguments are positive non-boolean integers; the intrinsic
  ``n_min`` is recomputed from the normalized angles and ``n_dec`` must
  be a multiple of it (the constructor's ``n_min`` argument is
  validated but superseded by the intrinsic value, as before);
- canonical fields cannot be reassigned after construction, and
  ``normalize()`` is an idempotent no-op returning ``self``;
- ``copy.copy``/``copy.deepcopy`` return ``self`` (immutable value);
- equality semantics are unchanged: ``n_min``, the ordered normalized
  cells (recursively), and the face tuple are identity; ``n_dec``
  remains deliberately excluded.  ``__hash__`` is consistent with
  ``__eq__`` and is safe because mutation is impossible.

This module is the stable algebraic foundation; it does not contain any
factorization or quotient logic.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_canonical
#   module_name: canonical
#   module_kind: engine
#   summary: Core UCNS algebraic objects and operations - the recursively immutable UCNSObject value, the ordered-concatenation product, and unit predicates.
#   owner: Erin Spencer
#   public_surface: UCNSObject, multiply, is_unit, is_multiplicative_unit, lcm, UNIT
#   internal_surface: _gauge_cells, _compute_n_min, _star_of, _disk_flip
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_v1_ws5_immutable_object_model.py, ucns_recursive/tests/test_depth2_full_domain.py, ucns_recursive/tests/test_canonical_constructor_validation.py, tests/test_canonical_constructor_validation.py
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

from fractions import Fraction
from functools import reduce
from math import gcd
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


def _gauge_cells(
    cells: List[Tuple[Fraction, Optional["UCNSObject"]]],
) -> Tuple[Tuple[Fraction, Optional["UCNSObject"]], ...]:
    """Gauge-normalize: shift every angle by the first angle, mod 4.

    Module-level so the canonicalization step is a single named hook
    (the O1 mutation contract perturbs exactly this function).
    """
    theta0 = cells[0][0]
    return tuple(
        ((theta - theta0) % 4, payload) for theta, payload in cells
    )


def _compute_n_min(angles: Tuple[Fraction, ...]) -> int:
    circle_fracs = [((a % 2) / 2) for a in angles]
    denoms = [f.denominator for f in circle_fracs if f != 0]
    if not denoms:
        return 1
    return reduce(lcm, denoms)


def _disk_flip(obj: Optional["UCNSObject"]) -> Optional["UCNSObject"]:
    if obj is None:
        return None
    return UCNSObject(obj.n_dec, obj.n_min, obj.A_minus, obj.F_minus)


def _star_of(
    a_plus: Tuple[Tuple[Fraction, Optional["UCNSObject"]], ...],
    f_plus: Tuple[int, ...],
) -> Tuple[Tuple[Tuple[Fraction, Optional["UCNSObject"]], ...], Tuple[int, ...]]:
    starred_a = tuple(
        ((-theta) % 4, _disk_flip(payload))
        for theta, payload in reversed(a_plus)
    )
    starred_f = tuple(reversed(f_plus))
    return starred_a, starred_f


class UCNSObject:
    """A UCNS sequence object: a recursively immutable canonical value.

    Parameters
    ----------
    n_dec:
        Declared carrier size (positive integer, must be a multiple of
        the intrinsic n_min).
    n_min:
        Carrier-size argument (positive integer); validated, then
        superseded by the intrinsic n_min computed from the normalized
        angles.
    A_plus:
        Sequence of (angle, payload) cells.  ``angle`` is a ``Fraction``
        or ``int`` (a fraction of a half-turn on the pairing circle,
        normalized into [0, 4)); ``payload`` is another ``UCNSObject``
        or ``None`` (unit payload).  Must be nonempty.
    F_plus:
        Face-flip sequence parallel to ``A_plus`` (exact integer bits
        0/1; booleans rejected).
    """

    __slots__ = ("n_dec", "n_min", "A_plus", "F_plus", "A_minus", "F_minus",
                 "_frozen")

    def __init__(
        self,
        n_dec: int,
        n_min: int,
        A_plus,
        F_plus,
    ) -> None:
        cells = list(A_plus)
        faces = list(F_plus)

        if len(cells) != len(faces):
            raise ValueError(
                "Invalid object: A_plus and F_plus must have the same length "
                f"(got {len(cells)} and {len(faces)})."
            )
        if not cells:
            raise ValueError(
                "Invalid object: A_plus must be nonempty; the empty object "
                "is outside the UCNS carrier and cannot be constructed."
            )

        invalid_faces = [
            f for f in faces
            if isinstance(f, bool) or not isinstance(f, int) or f not in (0, 1)
        ]
        if invalid_faces:
            raise ValueError(
                "Invalid object: F_plus entries must be face bits 0 or 1 "
                f"(got {invalid_faces!r})."
            )

        for name, value in (("n_dec", n_dec), ("n_min", n_min)):
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                raise ValueError(
                    f"Invalid object: {name} must be a positive integer "
                    f"(got {value!r})."
                )

        checked_cells: List[Tuple[Fraction, Optional["UCNSObject"]]] = []
        for cell in cells:
            try:
                angle, payload = cell
            except (TypeError, ValueError):
                raise ValueError(
                    f"Invalid object: malformed A_plus cell {cell!r}; "
                    "expected an (angle, payload) pair."
                )
            if isinstance(angle, bool) or not isinstance(angle, (Fraction, int)):
                raise ValueError(
                    "Invalid object: angles must be Fraction or int "
                    f"(got {angle!r})."
                )
            if payload is not None and not isinstance(payload, UCNSObject):
                raise ValueError(
                    "Invalid object: payloads must be UCNSObject or None "
                    f"(got {payload!r})."
                )
            checked_cells.append((Fraction(angle), payload))

        normalized = _gauge_cells(checked_cells)
        intrinsic_n_min = _compute_n_min(tuple(a for a, _ in normalized))
        if n_dec % intrinsic_n_min != 0:
            raise ValueError(
                f"Invalid object: n_dec={n_dec} not multiple of "
                f"n_min={intrinsic_n_min}"
            )

        object.__setattr__(self, "n_dec", n_dec)
        object.__setattr__(self, "n_min", intrinsic_n_min)
        object.__setattr__(self, "A_plus", normalized)
        object.__setattr__(self, "F_plus", tuple(int(f) for f in faces))
        a_minus, f_minus = _star_of(self.A_plus, self.F_plus)
        object.__setattr__(self, "A_minus", a_minus)
        object.__setattr__(self, "F_minus", f_minus)
        object.__setattr__(self, "_frozen", True)

    # ------------------------------------------------------------------
    # Immutability
    # ------------------------------------------------------------------

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError(
            f"UCNSObject is immutable; cannot assign {name!r}."
        )

    def __delattr__(self, name: str) -> None:
        raise AttributeError(
            f"UCNSObject is immutable; cannot delete {name!r}."
        )

    def __copy__(self) -> "UCNSObject":
        return self

    def __deepcopy__(self, memo) -> "UCNSObject":
        return self

    # ------------------------------------------------------------------
    # Normalization (construction already produced the canonical value)
    # ------------------------------------------------------------------

    def normalize(self) -> "UCNSObject":
        """Idempotent no-op: construction produces normalized values.

        Retained for API compatibility; returns ``self`` unchanged.
        """
        return self

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
    directly — safe because ``UCNSObject`` values are immutable.  This
    makes ``None`` the identity element.
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
    return UCNSObject(n_dec_new, n_min_new, new_A_plus, new_F_plus)


# ------------------------------------------------------------------
# Unit test
# ------------------------------------------------------------------

def is_unit(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is the sequence identity (length-1, angle 0,
    no payload, F=(0,)).

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
    if obj.F_plus != (0,) or obj.n_min != 1:
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
