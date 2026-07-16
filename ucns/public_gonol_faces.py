"""Face, chirality, and adjacency formulas over the public 157-gonal."""

# === MODULE_BUILD ===
# id: ucns_public_gonol_faces
#   module_name: public_gonol_faces
#   module_kind: schema
#   summary: preserves the exact public face, chirality, adjacency, arity, and fixed origin formulas from a0-betatest
#   owner: Erin Spencer
#   public_surface: face, chirality, n_plus, n_minus, ARITY, ORIGIN, UPPER_ARC_RANGE, LOWER_ARC_RANGE
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol
#   rollout: default_enabled
#   rollback: remove exports after reverting consumers to the pinned a0-betatest source
#   requires: ucns_public_gonol
#   since: 2026-07-16
#   unresolved: none
# === END MODULE_BUILD ===

from __future__ import annotations

ARITY = 157
ORIGIN = 0
UPPER_ARC_RANGE = (1, 78)
LOWER_ARC_RANGE = (79, 156)


def face(k: int) -> int:
    """Public face value: +1 for origin + upper arc, -1 for lower arc."""

    k = k % ARITY
    if k == ORIGIN:
        return +1
    if UPPER_ARC_RANGE[0] <= k <= UPPER_ARC_RANGE[1]:
        return +1
    return -1


def chirality(k: int, direction: int) -> int:
    """Neighbor in direction (+1 clockwise, -1 counterclockwise) mod 157."""

    if direction not in (+1, -1):
        raise ValueError("direction must be +1 or -1; got {}".format(direction))
    return (k + direction) % ARITY


def n_plus(k: int) -> int:
    """Clockwise neighbor."""

    return (k + 1) % ARITY


def n_minus(k: int) -> int:
    """Counterclockwise neighbor."""

    return (k - 1) % ARITY


__all__ = [
    "face",
    "chirality",
    "n_plus",
    "n_minus",
    "ARITY",
    "ORIGIN",
    "UPPER_ARC_RANGE",
    "LOWER_ARC_RANGE",
]
