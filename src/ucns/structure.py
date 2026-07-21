# === MODULE_BUILD ===
# id: structural_cell_support_floor
#   module_name: structure
#   module_kind: schema
#   summary: defines canonical cells, non-null carriers, aggregate support, pairing, pruning, and complete collapse
#   owner: Erin Spencer
#   public_surface: Cell, Carrier, Structure, make_carrier, support_weight, pair, prune, collapse
#   internal_surface: _has_distinction, _cells_from
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_structure.py
#   rollout: importable foundations surface; no product character or faithful-breadth evaluator
#   rollback: remove exports and this module
#   requires: directed_carrier_floor
#   since: 2026-07-21
#   unresolved: domain-specific mu assignment, receipts, metadata, canonical structural equivalence, M, B
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: cell_support_zero_test_is_fail_closed
#   given: a structural cell is constructed with support mu and optional retained fields
#   then: mu is finite and nonnegative; mu is zero exactly for a field-empty absent cell; positive support requires retained distinction
#   class: doctrine
#   since: 2026-07-21
#
# id: algebraic_zero_payload_remains_structural
#   given: a cell retains payload value zero with positive support
#   then: the cell is present and may form a non-null carrier
#   class: doctrine
#   since: 2026-07-21
#
# id: carrier_is_non_null_by_construction
#   given: Carrier is constructed directly
#   then: it contains at least one present cell and contains no absent cells
#   class: safety
#   since: 2026-07-21
#
# id: carrier_factory_returns_unique_null
#   given: an iterable of potential cells contains no positive support after pruning
#   then: make_carrier returns the unique STRUCTURAL_NULL rather than an empty Carrier
#   class: safety
#   since: 2026-07-21
#
# id: aggregate_support_is_cell_sum
#   given: a non-null carrier contains present cells
#   then: support_weight returns the sum of their support weights and returns zero only for STRUCTURAL_NULL
#   class: correctness
#   since: 2026-07-21
#
# id: carrier_pairing_is_cartesian_and_support_multiplicative
#   given: two non-null carriers are paired
#   then: every present cell meets every present cell, paired support is multiplicative, aggregate support multiplies, and STRUCTURAL_NULL absorbs
#   class: doctrine
#   since: 2026-07-21
#
# id: pruning_removes_only_absent_cells
#   given: potential cells contain zero-support absent cells and positive-support present cells
#   then: prune removes only absent cells and preserves all present cells in order
#   class: doctrine
#   since: 2026-07-21
#
# id: collapse_requires_complete_structural_absence
#   given: optional erasure is applied to a raw cell collection
#   then: collapse returns STRUCTURAL_NULL exactly when no positive-support cells survive
#   class: doctrine
#   since: 2026-07-21
# === END CONTRACTS ===

"""The structural cell/support floor selectively recovered from ``ucns-Grok``.

This module intentionally implements only the parts that follow directly from
Chapter 1 without inventing the still-open measuring instruments:

* a fail-closed support-weight zero test for cells;
* canonical non-null carrier construction;
* aggregate support ``W`` as the sum of present-cell supports;
* Cartesian pairing with multiplicative paired-cell support;
* pruning and complete collapse.

It does not define a product character ``M``, faithful breadth ``B``, receipts,
metadata semantics, canonical structural equivalence, typed dispatch, or a
complete ``UCNSObject``.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass
from math import isclose, isfinite
from typing import Any, TypeAlias, Union

from .carrier import STRUCTURAL_NULL, _StructuralNull


@dataclass(frozen=True, slots=True)
class Cell:
    """A potential structural cell with definitive support weight ``mu``.

    ``mu == 0`` denotes an absent cell and is valid only when every retained
    field is absent. ``mu > 0`` denotes a present cell and requires at least one
    retained distinction. Numeric/algebraic payload zero is still a distinction.
    """

    coordinate: Any = None
    payload: Any = None
    type_tag: Any = None
    shape: Any = None
    state: Any = None
    provenance: Any = None
    relation: Any = None
    mu: float = 1.0

    def __post_init__(self) -> None:
        support = float(self.mu)
        if not isfinite(support) or support < 0.0:
            raise ValueError("cell support mu must be finite and nonnegative")
        object.__setattr__(self, "mu", support)

        distinguished = self.has_distinction()
        if support == 0.0 and distinguished:
            raise ValueError("an absent cell cannot retain structural distinction")
        if support > 0.0 and not distinguished:
            raise ValueError("a present cell requires at least one retained distinction")

    def has_distinction(self) -> bool:
        return any(
            value is not None
            for value in (
                self.coordinate,
                self.payload,
                self.type_tag,
                self.shape,
                self.state,
                self.provenance,
                self.relation,
            )
        )

    @property
    def support(self) -> float:
        return self.mu

    @property
    def is_present(self) -> bool:
        return self.mu > 0.0


@dataclass(frozen=True, slots=True)
class Carrier:
    """A canonical non-null structural carrier.

    Direct construction is fail-closed: an empty carrier or a carrier retaining
    an absent cell is invalid. Use :func:`make_carrier` for raw potential cells;
    it prunes absent cells and returns ``STRUCTURAL_NULL`` when nothing remains.
    """

    cells: tuple[Cell, ...]

    def __post_init__(self) -> None:
        cells = tuple(self.cells)
        if not cells:
            raise ValueError("an empty carrier is Structural Null, not Carrier")
        if any(not cell.is_present for cell in cells):
            raise ValueError("a canonical Carrier cannot retain absent cells")
        object.__setattr__(self, "cells", cells)

    @property
    def W(self) -> float:
        return sum(cell.support for cell in self.cells)


Structure: TypeAlias = Union[_StructuralNull, Carrier]
RawStructure: TypeAlias = Union[_StructuralNull, Carrier, Iterable[Cell]]


def make_carrier(cells: Iterable[Cell]) -> Structure:
    """Prune absent cells and return either a canonical Carrier or Structural Null."""

    present = tuple(cell for cell in cells if cell.is_present)
    return STRUCTURAL_NULL if not present else Carrier(present)


def support_weight(obj: Structure) -> float:
    """Return aggregate support ``W`` with a unique zero at Structural Null."""

    if obj is STRUCTURAL_NULL:
        return 0.0
    if not isinstance(obj, Carrier):
        raise TypeError("obj must be STRUCTURAL_NULL or Carrier")
    return obj.W


def prune(raw: RawStructure) -> Structure:
    """Remove only zero-support absent cells, preserving present-cell order."""

    if raw is STRUCTURAL_NULL:
        return STRUCTURAL_NULL
    if isinstance(raw, Carrier):
        return raw
    return make_carrier(raw)


def pair(left: Structure, right: Structure) -> Structure:
    """Cartesian carrier pairing with multiplicative paired-cell support."""

    if left is STRUCTURAL_NULL or right is STRUCTURAL_NULL:
        return STRUCTURAL_NULL
    if not isinstance(left, Carrier) or not isinstance(right, Carrier):
        raise TypeError("pair operands must be STRUCTURAL_NULL or Carrier")

    paired = (
        Cell(
            coordinate=(first.coordinate, second.coordinate),
            payload=(first.payload, second.payload),
            type_tag=(first.type_tag, second.type_tag),
            shape=(first.shape, second.shape),
            state=(first.state, second.state),
            provenance=(first.provenance, second.provenance),
            relation=(first.relation, second.relation),
            mu=first.support * second.support,
        )
        for first in left.cells
        for second in right.cells
    )
    result = make_carrier(paired)
    assert result is not STRUCTURAL_NULL
    assert isclose(
        support_weight(result),
        support_weight(left) * support_weight(right),
        rel_tol=1e-12,
        abs_tol=1e-12,
    )
    return result


def _cells_from(raw: RawStructure) -> tuple[Cell, ...]:
    if raw is STRUCTURAL_NULL:
        return ()
    if isinstance(raw, Carrier):
        return raw.cells
    return tuple(raw)


def collapse(
    raw: RawStructure,
    erase: Callable[[tuple[Cell, ...]], Iterable[Cell]] | None = None,
) -> Structure:
    """Apply optional structural erasure and collapse only on complete absence."""

    cells = _cells_from(raw)
    if erase is not None:
        cells = tuple(erase(cells))
    return make_carrier(cells)
