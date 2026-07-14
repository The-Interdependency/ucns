"""Relational geometry and local-group structure for UCNS.

This module separates recursive radius from top-level breadth, exposes the
first-level fork observable, and provides exact constructors/predicates for the
finite unit-tower local groups proved in ``docs/local-groups.md``.

The semantic meaning of a payload fork is intentionally out of scope. UCNS can
represent and count forks; METAPAT-to-UCNS encoding policy must decide whether
a fork denotes simultaneous constitutive components.
"""
from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_relational_geometry
#   module_name: relational_geometry
#   module_kind: engine
#   summary: recursive radius, breadth, fork observables, idempotent towers, and home-relative local-group predicates
#   owner: Erin Spencer
#   public_surface: recursive_radius, breadth, first_level_fork_count, is_normalized, zero_faced_tower, face_tower, idempotent_tower_depth, is_local_group_pair, is_local_group_member, local_group_elements
#   internal_surface: _face_tower_bits
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_local_groups_and_geometry, tests.test_base_geometry_contracts
#   rollout: default_enabled
#   rollback: remove exports and dependent contracts
#   requires: ucns_canonical
#   since: 2026-07-14
#   unresolved: full fork-profile counting convention; METAPAT fork admissibility remains downstream
# === END MODULE_BUILD ===

import math
from fractions import Fraction
from itertools import product
from numbers import Integral
from typing import Iterable, Optional, Tuple

from .canonical import UCNSObject, multiply

__all__ = [
    "recursive_radius",
    "breadth",
    "first_level_fork_count",
    "is_normalized",
    "zero_faced_tower",
    "face_tower",
    "idempotent_tower_depth",
    "is_local_group_pair",
    "is_local_group_member",
    "local_group_elements",
]


def recursive_radius(obj: Optional[UCNSObject]) -> int:
    """Return recursive payload depth: ``None -> 0``."""
    if obj is None:
        return 0
    return 1 + max(
        (recursive_radius(payload) for _, payload in obj.A_plus),
        default=0,
    )


def breadth(obj: Optional[UCNSObject]) -> float:
    """Return ``lambda = log(len(A_plus))``; the unit sentinel has breadth 0."""
    if obj is None:
        return 0.0
    return math.log(len(obj.A_plus))


def first_level_fork_count(obj: Optional[UCNSObject]) -> int:
    """Count top-level cells carrying a non-unit payload."""
    if obj is None:
        return 0
    return sum(1 for _, payload in obj.A_plus if payload is not None)


def is_normalized(obj: Optional[UCNSObject]) -> bool:
    """Return whether every recursive object has first stored angle zero."""
    if obj is None:
        return True
    if not obj.A_plus or obj.A_plus[0][0] != 0:
        return False
    return all(is_normalized(payload) for _, payload in obj.A_plus)


def _validated_faces(faces: Iterable[int]) -> Tuple[int, ...]:
    result = tuple(faces)
    if not result:
        raise ValueError("faces must contain at least one recursive level")
    for index, face in enumerate(result):
        if (
            not isinstance(face, Integral)
            or isinstance(face, bool)
            or int(face) not in (0, 1)
        ):
            raise ValueError(
                "faces[{0}] must be an integer face bit 0 or 1".format(index)
            )
    return tuple(int(face) for face in result)


def face_tower(faces: Iterable[int]) -> UCNSObject:
    """Construct a normalized recursively singleton tower with the given faces."""
    bits = _validated_faces(faces)
    payload: Optional[UCNSObject] = None
    for face in reversed(bits):
        payload = UCNSObject(1, 1, [(Fraction(0), payload)], [face])
    assert payload is not None
    return payload


def zero_faced_tower(depth: int) -> UCNSObject:
    """Return the unique zero-faced idempotent tower at positive *depth*."""
    if not isinstance(depth, Integral) or isinstance(depth, bool) or int(depth) < 1:
        raise ValueError("depth must be a positive integer")
    return face_tower([0] * int(depth))


def _face_tower_bits(obj: Optional[UCNSObject]) -> Optional[Tuple[int, ...]]:
    """Return tower face bits, or ``None`` when *obj* is not a singleton tower."""
    if obj is None:
        return ()
    if len(obj.A_plus) != 1 or obj.A_plus[0][0] != 0:
        return None
    payload = obj.A_plus[0][1]
    rest = _face_tower_bits(payload)
    if rest is None:
        return None
    return (obj.F_plus[0],) + rest


def idempotent_tower_depth(obj: Optional[UCNSObject]) -> Optional[int]:
    """Return ``d`` iff *obj* is the zero-faced idempotent tower ``T_d``."""
    bits = _face_tower_bits(obj)
    if bits is None or not bits or any(bits):
        return None
    return len(bits)


def is_local_group_pair(
    x: UCNSObject,
    y: UCNSObject,
    identity: UCNSObject,
) -> bool:
    """Check cancellation and two-sided identity absorption for an inverse pair."""
    return (
        multiply(x, y) == identity
        and multiply(y, x) == identity
        and multiply(identity, x) == x
        and multiply(x, identity) == x
        and multiply(identity, y) == y
        and multiply(y, identity) == y
    )


def is_local_group_member(obj: UCNSObject, identity: UCNSObject) -> bool:
    """Return whether *obj* belongs to the classified local group at *identity*."""
    depth = idempotent_tower_depth(identity)
    bits = _face_tower_bits(obj)
    if depth is None or bits is None or len(bits) != depth:
        return False
    return is_local_group_pair(obj, obj, identity)


def local_group_elements(depth: int) -> Tuple[UCNSObject, ...]:
    """Enumerate ``G_d`` as all depth-*d* face towers."""
    if not isinstance(depth, Integral) or isinstance(depth, bool) or int(depth) < 1:
        raise ValueError("depth must be a positive integer")
    return tuple(face_tower(bits) for bits in product((0, 1), repeat=int(depth)))
