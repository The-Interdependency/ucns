"""
ucns.witness_matrix
==============================
Witness objects and the WitnessMatrix consistency checker.

A Witness records one cell of a proposed host factorisation:

    W_{i,j} :  multiply(left_payload, right_payload) ≡ product_payload

The WitnessMatrix collects all p×q witnesses and checks:

1.  Every individual witness is verified (multiply agrees with the target).
2.  Row consistency: all witnesses in row i share the same left_payload.
3.  Column consistency: all witnesses in column j share the same right_payload.

Global consistency (``WitnessMatrix.globally_consistent()``) is the
central correctness criterion for factor_search_v08: a factorisation
candidate is only returned if its witness matrix passes this check.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_witness_matrix
#   module_name: witness_matrix
#   module_kind: engine
#   summary: Witness and WitnessMatrix types plus build_witness_matrix; verifies per-cell factor products and row/column global consistency for a host factorisation candidate.
#   owner: Erin Spencer
#   public_surface: Witness, WitnessMatrix, build_witness_matrix
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_failure_boundary_e109
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass, field
from typing import List, Optional

from .canonical import UCNSObject, multiply

__all__ = ["Witness", "WitnessMatrix", "build_witness_matrix"]


@dataclass
class Witness:
    """One cell of the host factorisation.

    Attributes
    ----------
    i, j:
        Row and column indices within the host grid.
    left_payload:
        The S_i^A payload assigned to row *i*.
    right_payload:
        The S_j^B payload assigned to column *j*.
    product_payload:
        The target payload P[i,j] extracted from the product object P.
    verified:
        True iff ``multiply(left_payload, right_payload) == product_payload``.
    """

    i: int
    j: int
    left_payload: Optional[UCNSObject]
    right_payload: Optional[UCNSObject]
    product_payload: Optional[UCNSObject]
    verified: bool = field(init=False)

    def __post_init__(self) -> None:
        self.verified = (
            multiply(self.left_payload, self.right_payload) == self.product_payload
        )


class WitnessMatrix:
    """p×q matrix of Witness objects with a global consistency check.

    Parameters
    ----------
    p, q:
        Grid dimensions (rows × columns).
    """

    def __init__(self, p: int, q: int) -> None:
        self.p = p
        self.q = q
        self._grid: List[List[Optional[Witness]]] = [
            [None] * q for _ in range(p)
        ]

    def set(
        self,
        i: int,
        j: int,
        left_payload: Optional[UCNSObject],
        right_payload: Optional[UCNSObject],
        product_payload: Optional[UCNSObject],
    ) -> None:
        """Record a witness at position (i, j)."""
        self._grid[i][j] = Witness(i, j, left_payload, right_payload, product_payload)

    def get(self, i: int, j: int) -> Optional[Witness]:
        return self._grid[i][j]

    def globally_consistent(self) -> bool:
        """Return True iff all witnesses are verified and the matrix is
        row-consistent and column-consistent.

        Row-consistent means every witness in row *i* has the same
        ``left_payload``.  Column-consistent means every witness in column
        *j* has the same ``right_payload``.
        """
        # All cells must be filled and individually verified
        for i in range(self.p):
            for j in range(self.q):
                w = self._grid[i][j]
                if w is None or not w.verified:
                    return False

        # Row consistency: all left_payloads in a row must agree
        for i in range(self.p):
            first_left = self._grid[i][0].left_payload  # type: ignore[union-attr]
            for j in range(1, self.q):
                w = self._grid[i][j]
                if w.left_payload != first_left:  # type: ignore[union-attr]
                    return False

        # Column consistency: all right_payloads in a column must agree
        for j in range(self.q):
            first_right = self._grid[0][j].right_payload  # type: ignore[union-attr]
            for i in range(1, self.p):
                w = self._grid[i][j]
                if w.right_payload != first_right:  # type: ignore[union-attr]
                    return False

        return True

    def __repr__(self) -> str:
        filled = sum(
            1 for i in range(self.p) for j in range(self.q)
            if self._grid[i][j] is not None
        )
        verified = sum(
            1 for i in range(self.p) for j in range(self.q)
            if self._grid[i][j] is not None and self._grid[i][j].verified
        )
        return f"WitnessMatrix({self.p}×{self.q}, filled={filled}, verified={verified})"


def build_witness_matrix(
    S_A: List[Optional[UCNSObject]],
    S_B: List[Optional[UCNSObject]],
    P_payloads: List[List[Optional[UCNSObject]]],
) -> WitnessMatrix:
    """Construct a WitnessMatrix from a payload assignment and target grid."""
    p, q = len(S_A), len(S_B)
    wm = WitnessMatrix(p, q)
    for i in range(p):
        for j in range(q):
            wm.set(i, j, S_A[i], S_B[j], P_payloads[i][j])
    return wm
