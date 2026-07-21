# === CHECKS ===
# id: check_cell_support_zero_test
#   proves: cell_support_zero_test_is_fail_closed
#   call: self::test_cell_support_zero_test
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_algebraic_zero_cell
#   proves: algebraic_zero_payload_remains_structural
#   call: self::test_algebraic_zero_cell
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_carrier_constructor
#   proves: carrier_is_non_null_by_construction
#   call: self::test_carrier_constructor
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_carrier_factory_null
#   proves: carrier_factory_returns_unique_null
#   call: self::test_carrier_factory_null
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_aggregate_support
#   proves: aggregate_support_is_cell_sum
#   call: self::test_aggregate_support
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_pairing_support_law
#   proves: carrier_pairing_is_cartesian_and_support_multiplicative
#   call: self::test_pairing_support_law
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_pruning_rule
#   proves: pruning_removes_only_absent_cells
#   call: self::test_pruning_rule
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_complete_collapse
#   proves: collapse_requires_complete_structural_absence
#   call: self::test_complete_collapse
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from math import inf, isclose

import pytest

from ucns import (
    STRUCTURAL_NULL,
    Carrier,
    Cell,
    collapse,
    make_carrier,
    pair,
    prune,
    support_weight,
)


def test_cell_support_zero_test() -> None:
    absent = Cell(mu=0.0)
    assert not absent.is_present
    assert not absent.has_distinction()

    with pytest.raises(ValueError):
        Cell(mu=-1.0)
    with pytest.raises(ValueError):
        Cell(mu=inf)
    with pytest.raises(ValueError):
        Cell(payload="retained", mu=0.0)
    with pytest.raises(ValueError):
        Cell(mu=1.0)


def test_algebraic_zero_cell() -> None:
    zero = Cell(payload=0, mu=1.0)
    obj = make_carrier((zero,))
    assert obj is not STRUCTURAL_NULL
    assert support_weight(obj) == 1.0


def test_carrier_constructor() -> None:
    present = Cell(coordinate="a", mu=1.0)
    obj = Carrier((present,))
    assert obj.cells == (present,)

    with pytest.raises(ValueError):
        Carrier(())
    with pytest.raises(ValueError):
        Carrier((Cell(mu=0.0),))


def test_carrier_factory_null() -> None:
    assert make_carrier(()) is STRUCTURAL_NULL
    assert make_carrier((Cell(mu=0.0), Cell(mu=0.0))) is STRUCTURAL_NULL


def test_aggregate_support() -> None:
    obj = make_carrier(
        (
            Cell(coordinate="a", mu=2.0),
            Cell(payload="b", mu=3.5),
        )
    )
    assert obj is not STRUCTURAL_NULL
    assert support_weight(obj) == 5.5
    assert support_weight(STRUCTURAL_NULL) == 0.0


def test_pairing_support_law() -> None:
    left = make_carrier(
        (
            Cell(coordinate="a", mu=2.0),
            Cell(coordinate="b", mu=3.0),
        )
    )
    right = make_carrier(
        (
            Cell(payload="c", mu=5.0),
            Cell(payload="d", mu=7.0),
        )
    )
    assert isinstance(left, Carrier)
    assert isinstance(right, Carrier)

    product = pair(left, right)
    assert isinstance(product, Carrier)
    assert len(product.cells) == 4
    assert isclose(
        support_weight(product),
        support_weight(left) * support_weight(right),
        rel_tol=1e-12,
        abs_tol=1e-12,
    )
    assert pair(STRUCTURAL_NULL, left) is STRUCTURAL_NULL
    assert pair(right, STRUCTURAL_NULL) is STRUCTURAL_NULL


def test_pruning_rule() -> None:
    first = Cell(coordinate="first", mu=1.0)
    second = Cell(coordinate="second", mu=2.0)
    result = prune((Cell(mu=0.0), first, Cell(mu=0.0), second))
    assert isinstance(result, Carrier)
    assert result.cells == (first, second)


def test_complete_collapse() -> None:
    retained = Cell(payload=0, mu=1.0)
    obj = collapse((retained,))
    assert isinstance(obj, Carrier)

    erased = collapse((retained,), erase=lambda cells: ())
    assert erased is STRUCTURAL_NULL
    assert collapse((Cell(mu=0.0),)) is STRUCTURAL_NULL
