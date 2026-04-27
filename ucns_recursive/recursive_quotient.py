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

from typing import List, Optional

from .canonical import UCNSObject, multiply

__all__ = ["find_left_factor", "find_right_factor"]


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
