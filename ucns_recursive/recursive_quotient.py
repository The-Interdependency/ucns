"""
ucns_recursive.recursive_quotient
==================================
Payload-level factor finders.

These functions solve one equation at a time:

    find_left_factor(target, right, catalogue)
        Find L such that  multiply(L, right) == target.

    find_right_factor(target, left, catalogue)
        Find R such that  multiply(left, R) == target.

Both enumerate the provided *catalogue* of candidate payload objects and
return the first match, or ``None`` if none exists.  ``None`` (unit) is
always tried as the first candidate.

The "recursive" in the module name reflects the design intent: these
functions do not treat their inputs as atomic.  When the inputs are
themselves non-unit UCNSObjects, the product is computed via the full
``multiply`` operation, which descends into payloads recursively.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_recursive_quotient
#   module_name: recursive_quotient
#   module_kind: engine
#   summary: Payload-level single-equation factor finders (find_left_factor / find_right_factor) that enumerate a candidate catalogue, plus re-exports of the left/right quotient primitives.
#   owner: Erin Spencer
#   public_surface: find_left_factor, find_right_factor, left_quotient, right_quotient
#   internal_surface: find_right_factor_or_sentinel, find_left_factor_or_sentinel
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: hmmm
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_left_quotient
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from typing import List, Optional

from .canonical import UCNSObject, multiply
from .left_quotient import left_quotient, right_quotient

__all__ = [
    "find_left_factor",
    "find_right_factor",
    "left_quotient",
    "right_quotient",
]


def find_right_factor(
    target: Optional[UCNSObject],
    left: Optional[UCNSObject],
    catalogue: List[Optional[UCNSObject]],
) -> Optional[UCNSObject]:
    """Find R from *catalogue* such that ``multiply(left, R) == target``.

    Returns the first matching candidate, or ``None`` if none is found.
    Note: a return value of ``None`` means the unit payload satisfies the
    equation (``multiply(left, None) == target``), which is only possible
    when ``left == target``.
    """
    for cand in catalogue:
        if multiply(left, cand) == target:
            return cand
    return None  # sentinel: no solution found


def find_left_factor(
    target: Optional[UCNSObject],
    right: Optional[UCNSObject],
    catalogue: List[Optional[UCNSObject]],
) -> Optional[UCNSObject]:
    """Find L from *catalogue* such that ``multiply(L, right) == target``.

    Returns the first matching candidate, or ``None`` if none is found.
    """
    for cand in catalogue:
        if multiply(cand, right) == target:
            return cand
    return None


# Sentinel distinguishing "unit is the answer" from "no answer found".
_NO_SOLUTION = object()


def find_right_factor_or_sentinel(
    target: Optional[UCNSObject],
    left: Optional[UCNSObject],
    catalogue: List[Optional[UCNSObject]],
) -> object:
    """Like ``find_right_factor`` but returns ``_NO_SOLUTION`` instead of
    ``None`` when no candidate works.  Use when the caller needs to
    distinguish "unit is the solution" from "unsolvable".
    """
    for cand in catalogue:
        if multiply(left, cand) == target:
            return cand
    return _NO_SOLUTION


def find_left_factor_or_sentinel(
    target: Optional[UCNSObject],
    right: Optional[UCNSObject],
    catalogue: List[Optional[UCNSObject]],
) -> object:
    """Like ``find_left_factor`` but returns ``_NO_SOLUTION`` on failure."""
    for cand in catalogue:
        if multiply(cand, right) == target:
            return cand
    return _NO_SOLUTION
