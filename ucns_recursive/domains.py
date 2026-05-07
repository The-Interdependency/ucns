"""
ucns_recursive.domains
======================
Frozen domain D' for the depth-2 solver, plus oracle-class predicates
and the verified-domain status taxonomy.

Domain parameters
-----------------
    depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4

Verified domain
---------------
The completeness theorems cover three strata:

    depth-0          the unit (None)
    depth-1          any flat object (all payloads None): v0.6 theorem
    depth-2-oracle   depth-2 objects whose cell payloads are all oracle
                     atoms: v0.8.1 oracle theorem

Outside the verified domain (depth-2-non-oracle, depth ≥ 3), soundness
is preserved but completeness is not proven.

Oracle atoms
------------
An oracle atom is any object that is either:
- ``None`` (the unit), or
- a depth-1 object within the frozen-domain bounds
  (``|A⁺| ≤ 3``, ``n_min ≤ 4``).

This is exactly the set produced by ``generate_payload_catalogue()``.
``ORACLE_ATOM_PAYLOADS`` is that list, precomputed at import time.

``S2`` is the canonical smallest oracle atom:
    UCNSObject(2, 2, [(0, None), (1, None)], [0, 0])
"""

from __future__ import annotations

from fractions import Fraction
from typing import List, Optional

from .canonical import UCNSObject, UNIT

__all__ = [
    "DEPTH_MAX",
    "A_PLUS_MAX",
    "N_MIN_MAX",
    "S2",
    "ORACLE_ATOM_PAYLOADS",
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


# ------------------------------------------------------------------
# Canonical oracle atom
# ------------------------------------------------------------------

S2: UCNSObject = UCNSObject(
    2, 2,
    [(Fraction(0), UNIT), (Fraction(1), UNIT)],
    [0, 0],
)


# ------------------------------------------------------------------
# Depth
# ------------------------------------------------------------------

def depth_of(obj: Optional[UCNSObject]) -> int:
    """Return the nesting depth of *obj* (None → 0)."""
    if obj is None:
        return 0
    max_payload_depth = max((depth_of(p) for _, p in obj.A_plus), default=0)
    return 1 + max_payload_depth


# ------------------------------------------------------------------
# Domain membership
# ------------------------------------------------------------------

def in_domain(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is within the frozen domain D'."""
    if obj is None:
        return True
    return (
        depth_of(obj) <= DEPTH_MAX
        and len(obj.A_plus) <= A_PLUS_MAX
        and obj.n_min <= N_MIN_MAX
    )


# ------------------------------------------------------------------
# Payload catalogue generation
# ------------------------------------------------------------------

def generate_payload_catalogue() -> List[Optional[UCNSObject]]:
    """Return all depth-1 UCNSObjects with |A⁺| ≤ 3 and n_min ≤ 4.

    These are the oracle atoms that can appear as cell payloads inside
    depth-2 objects from D'.  ``None`` (unit payload) is included first.
    """
    objects: List[Optional[UCNSObject]] = [UNIT]
    seen: set = set()

    for n_min in range(1, N_MIN_MAX + 1):
        for length in range(1, A_PLUS_MAX + 1):
            angles = [Fraction(2 * k, n_min) for k in range(length)]
            for face_bits in range(2 ** length):
                faces = [(face_bits >> i) & 1 for i in range(length)]
                try:
                    obj = UCNSObject(
                        n_dec=n_min * 2,
                        n_min=n_min,
                        A_plus=[(a, None) for a in angles],
                        F_plus=faces,
                    )
                except ValueError:
                    continue
                key = (obj.n_min, tuple(obj.F_plus),
                       tuple(a for a, _ in obj.A_plus))
                if key not in seen:
                    seen.add(key)
                    objects.append(obj)

    return objects


# ------------------------------------------------------------------
# Oracle-class predicates
# ------------------------------------------------------------------

# Precomputed at import time; used by is_oracle_atom and as a public
# constant for catalogue builders.
ORACLE_ATOM_PAYLOADS: List[Optional[UCNSObject]] = generate_payload_catalogue()


def is_oracle_atom(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is an oracle atom.

    Oracle atoms are None (the unit) and every depth-1 object within
    the frozen-domain bounds (|A⁺| ≤ 3, n_min ≤ 4).  Equivalently,
    these are exactly the objects produced by
    :func:`generate_payload_catalogue`.
    """
    if obj is None:
        return True
    return (
        depth_of(obj) == 1
        and len(obj.A_plus) <= A_PLUS_MAX
        and obj.n_min <= N_MIN_MAX
    )


def is_in_oracle_class(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is in the depth-2 oracle class.

    An object is in the oracle class when:
    - its depth is 0 or 1 (trivially covered by existing theorems), or
    - its depth is exactly 2 AND every cell payload is an oracle atom.

    Objects with depth ≥ 3 are never in the oracle class.
    """
    if obj is None:
        return True
    d = depth_of(obj)
    if d <= 1:
        return True
    if d >= 3:
        return False
    # depth == 2: every cell payload must be an oracle atom.
    return all(is_oracle_atom(payload) for _, payload in obj.A_plus)


def verified_domain_status(obj: Optional[UCNSObject]) -> str:
    """Return the verified-domain status string for *obj*.

    Returns one of:

    ``"depth-0"``            obj is None (the unit)
    ``"depth-1"``            flat object, all payloads None
    ``"depth-2-oracle"``     depth-2 object in the oracle class
    ``"depth-2-non-oracle"`` depth-2 object outside the oracle class
    ``"depth-3+"``           depth ≥ 3

    The verified domain (completeness guaranteed) is the union of
    ``"depth-0"``, ``"depth-1"``, and ``"depth-2-oracle"``.
    """
    if obj is None:
        return "depth-0"
    d = depth_of(obj)
    if d == 0:
        return "depth-0"
    if d == 1:
        return "depth-1"
    if d == 2:
        return "depth-2-oracle" if is_in_oracle_class(obj) else "depth-2-non-oracle"
    return "depth-3+"
