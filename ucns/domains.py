"""
ucns.domains
======================
Frozen domain D' for the depth-2 solver, plus oracle-class predicates
and the verified-domain status taxonomy.

Domain parameters
-----------------
    depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4

Verified domain
---------------
The completeness surfaces distinguish three strata:

    depth-0          the unit (None)
    depth-1          any flat object (all payloads None)
    depth-2-oracle   depth-2 objects whose cell payloads are all members
                     of the canonical oracle catalogue

Outside the verified domain (depth-2-non-oracle, depth ≥ 3), soundness
is preserved but completeness is not proven.

Oracle atoms
------------
An oracle atom is ``None`` or a structural member of the canonical
catalogue produced by :func:`generate_payload_catalogue`.  The catalogue
is the deterministic carrier-grid family with raw angles
``2*k/n_min`` for ``n_min <= 4`` and lengths ``1..3``, across every face
assignment.

This is deliberately narrower than every geometrically bounded flat
object.  ``in_domain`` answers the geometric question; ``is_oracle_atom``
answers catalogue membership.  Keeping those predicates separate makes
future catalogue-coverage checks machine-verifiable.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_domains
#   module_name: domains
#   module_kind: engine
#   summary: Defines the frozen depth-2 geometry, canonical oracle catalogue, and exact catalogue-membership predicates used to scope oracle claims.
#   owner: Erin Spencer
#   public_surface: DEPTH_MAX, A_PLUS_MAX, N_MIN_MAX, S2, ORACLE_ATOM_PAYLOADS, ORACLE_CATALOGUE_RULE_VERSION, generate_payload_catalogue, in_domain, depth_of, is_oracle_atom, is_in_oracle_class, verified_domain_status
#   internal_surface: _generate_canonical_catalogue
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_oracle_catalogue_equivalence.py, ucns_recursive/tests/test_depth2_full_domain.py
#   rollout: default_enabled
#   rollback: restore geometric-bounds oracle classification (reintroduces catalogue mismatch)
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from fractions import Fraction
from typing import List, Optional, Tuple

from .canonical import UCNSObject, UNIT

__all__ = [
    "DEPTH_MAX",
    "A_PLUS_MAX",
    "N_MIN_MAX",
    "S2",
    "ORACLE_ATOM_PAYLOADS",
    "ORACLE_CATALOGUE_RULE_VERSION",
    "generate_payload_catalogue",
    "in_domain",
    "depth_of",
    "is_oracle_atom",
    "is_in_oracle_class",
    "verified_domain_status",
]


# ------------------------------------------------------------------
# Domain parameters
# ------------------------------------------------------------------

DEPTH_MAX: int = 2
A_PLUS_MAX: int = 3
N_MIN_MAX: int = 4

# Bump whenever the canonical catalogue generation family, bounds,
# ordering, or structural deduplication policy changes.
ORACLE_CATALOGUE_RULE_VERSION: str = "oracle-atoms-carrier-grid-v1"


# ------------------------------------------------------------------
# Canonical oracle atom
# ------------------------------------------------------------------

S2: UCNSObject = UCNSObject(
    2,
    2,
    [(Fraction(0), UNIT), (Fraction(1), UNIT)],
    [0, 0],
)


# ------------------------------------------------------------------
# Depth and geometric domain membership
# ------------------------------------------------------------------


def depth_of(obj: Optional[UCNSObject]) -> int:
    """Return the nesting depth of *obj* (None → 0)."""
    if obj is None:
        return 0
    max_payload_depth = max((depth_of(p) for _, p in obj.A_plus), default=0)
    return 1 + max_payload_depth



def in_domain(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is within the frozen geometric domain D'.

    This predicate does not imply oracle-catalogue membership.
    """
    if obj is None:
        return True
    return (
        depth_of(obj) <= DEPTH_MAX
        and len(obj.A_plus) <= A_PLUS_MAX
        and obj.n_min <= N_MIN_MAX
    )


# ------------------------------------------------------------------
# Canonical payload catalogue
# ------------------------------------------------------------------


def _generate_canonical_catalogue() -> Tuple[Optional[UCNSObject], ...]:
    """Generate the deterministic oracle catalogue once.

    Order is unit first, then ``(n_min, length, face_bits)`` generation
    order.  Structurally equal objects are deduplicated while retaining
    the first occurrence.
    """
    objects: List[Optional[UCNSObject]] = [UNIT]
    seen = set()

    for n_min in range(1, N_MIN_MAX + 1):
        for length in range(1, A_PLUS_MAX + 1):
            angles = [Fraction(2 * k, n_min) for k in range(length)]
            for face_bits in range(2 ** length):
                faces = [(face_bits >> i) & 1 for i in range(length)]
                try:
                    obj = UCNSObject(
                        n_dec=n_min * 2,
                        n_min=n_min,
                        A_plus=[(angle, None) for angle in angles],
                        F_plus=faces,
                    )
                except ValueError:
                    continue
                key = (
                    obj.n_min,
                    tuple(obj.F_plus),
                    tuple(angle for angle, _ in obj.A_plus),
                )
                if key in seen:
                    continue
                seen.add(key)
                objects.append(obj)

    return tuple(objects)


# Immutable container and single source of truth. UCNSObject itself remains
# mutable in the current release, so membership intentionally uses structural
# equality rather than a hash index until the object-model repair lands.
ORACLE_ATOM_PAYLOADS: Tuple[Optional[UCNSObject], ...] = (
    _generate_canonical_catalogue()
)



def generate_payload_catalogue() -> List[Optional[UCNSObject]]:
    """Return a fresh list containing the canonical oracle catalogue.

    The family is deterministic, structurally deduplicated, unit-first,
    and identified by :data:`ORACLE_CATALOGUE_RULE_VERSION`.  It is not
    every flat object satisfying the geometric bounds.
    """
    return list(ORACLE_ATOM_PAYLOADS)


# ------------------------------------------------------------------
# Oracle-class predicates
# ------------------------------------------------------------------


def is_oracle_atom(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is in the canonical oracle catalogue.

    This is extensionally identical to structural membership in
    :func:`generate_payload_catalogue` by construction.
    """
    if obj is None:
        return True
    if not isinstance(obj, UCNSObject):
        return False
    return any(
        candidate is not None and obj == candidate
        for candidate in ORACLE_ATOM_PAYLOADS
    )



def is_in_oracle_class(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is in the depth-2 oracle class.

    Depth-zero and depth-one objects remain covered by their own strata.
    A depth-two object is oracle-class only when every immediate payload
    is a canonical oracle atom.  Depth three and above are excluded.
    """
    if obj is None:
        return True
    depth = depth_of(obj)
    if depth <= 1:
        return True
    if depth >= 3:
        return False
    return all(is_oracle_atom(payload) for _, payload in obj.A_plus)



def verified_domain_status(obj: Optional[UCNSObject]) -> str:
    """Return the verified-domain status string for *obj*.

    Returns one of ``depth-0``, ``depth-1``, ``depth-2-oracle``,
    ``depth-2-non-oracle``, or ``depth-3+``.
    """
    if obj is None:
        return "depth-0"
    depth = depth_of(obj)
    if depth == 0:
        return "depth-0"
    if depth == 1:
        return "depth-1"
    if depth == 2:
        return (
            "depth-2-oracle"
            if is_in_oracle_class(obj)
            else "depth-2-non-oracle"
        )
    return "depth-3+"
