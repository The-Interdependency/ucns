"""
ucns_recursive.domains
======================
Frozen domain D' for the depth-2 solver.

    depth ≤ 2
    |A⁺| ≤ 3
    n_min ≤ 4

``generate_payload_catalogue`` returns every depth-0 UCNSObject that can
appear as a cell payload inside a depth-2 object from D'.  These are the
candidates tried by the payload-system solver.
"""

from __future__ import annotations

from fractions import Fraction
from typing import List, Optional

from .canonical import UCNSObject, UNIT

__all__ = [
    "DEPTH_MAX",
    "A_PLUS_MAX",
    "N_MIN_MAX",
    "generate_payload_catalogue",
    "in_domain",
]

# ------------------------------------------------------------------
# Domain parameters
# ------------------------------------------------------------------

DEPTH_MAX: int = 2
A_PLUS_MAX: int = 3
N_MIN_MAX: int = 4


# ------------------------------------------------------------------
# Domain membership
# ------------------------------------------------------------------

def _depth(obj: Optional[UCNSObject]) -> int:
    """Return the nesting depth of *obj* (None → 0)."""
    if obj is None:
        return 0
    max_payload_depth = max((_depth(p) for _, p in obj.A_plus), default=0)
    return 1 + max_payload_depth


def in_domain(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is within the frozen domain D'."""
    if obj is None:
        return True
    return (
        _depth(obj) <= DEPTH_MAX
        and len(obj.A_plus) <= A_PLUS_MAX
        and obj.n_min <= N_MIN_MAX
    )


# ------------------------------------------------------------------
# Payload catalogue generation
# ------------------------------------------------------------------

def generate_payload_catalogue() -> List[Optional[UCNSObject]]:
    """Return all depth-0 UCNSObjects with |A⁺| ≤ 3 and n_min ≤ 4.

    These are the atomic building blocks that appear as payloads in
    depth-1 and depth-2 objects from D'.  ``None`` (unit payload) is
    included first.
    """
    objects: List[Optional[UCNSObject]] = [UNIT]
    seen: set = set()

    for n_min in range(1, N_MIN_MAX + 1):
        for length in range(1, A_PLUS_MAX + 1):
            # Evenly-spaced angles: k/n_min * 2  for k = 0..length-1
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
