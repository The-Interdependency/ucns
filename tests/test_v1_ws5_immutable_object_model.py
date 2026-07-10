"""Workstream 5 — nonempty, immutable, stably hashable UCNSObject.

A valid ``UCNSObject`` cannot be mutated into an invalid or differently
hashed value, and an empty UCNS object cannot be constructed through
the public API (codex-handoff/05).
"""

import copy
from fractions import Fraction

import pytest

from ucns import UCNSObject, UNIT, multiply, recursive_encode, stable_hash

E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
NESTED = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 1])


def test_empty_construction_rejected():
    with pytest.raises(ValueError):
        UCNSObject(1, 1, [], [])


@pytest.mark.parametrize("bad", [0, -1, True, False, 1.5, "2", None])
def test_bad_carrier_values_rejected(bad):
    with pytest.raises((ValueError, TypeError)):
        UCNSObject(bad, 1, [(Fraction(0), UNIT)], [0])
    with pytest.raises((ValueError, TypeError)):
        UCNSObject(1, bad, [(Fraction(0), UNIT)], [0])


@pytest.mark.parametrize("faces", [[2], [-1], [0.0], [Fraction(0)], [True], ["0"]])
def test_bad_faces_rejected(faces):
    with pytest.raises(ValueError):
        UCNSObject(1, 1, [(Fraction(0), UNIT)], faces)


@pytest.mark.parametrize(
    "angle", [0.5, float("nan"), float("inf"), True, "1", None]
)
def test_bad_angles_rejected(angle):
    with pytest.raises(ValueError):
        UCNSObject(24, 1, [(angle, UNIT)], [0])


def test_int_angles_convert_to_fraction():
    obj = UCNSObject(24, 1, [(0, UNIT), (1, UNIT)], [0, 0])
    assert all(isinstance(a, Fraction) for a, _ in obj.A_plus)


@pytest.mark.parametrize("cell", [(Fraction(0),), (Fraction(0), UNIT, 1), 3, "x"])
def test_malformed_cells_rejected(cell):
    with pytest.raises(ValueError):
        UCNSObject(24, 1, [cell], [0])


def test_bad_payload_rejected():
    with pytest.raises(ValueError):
        UCNSObject(24, 1, [(Fraction(0), "payload")], [0])


def test_construction_normalizes_and_normalize_is_noop():
    obj = UCNSObject(24, 1, [(Fraction(3), UNIT), (Fraction(1), UNIT)], [0, 1])
    assert obj.A_plus[0][0] == 0, "gauge-normalized at construction"
    assert obj.A_plus[1][0] == (Fraction(1) - Fraction(3)) % 4
    before = obj.A_plus
    assert obj.normalize() is obj
    assert obj.A_plus is before, "normalize must not mutate"


def test_canonical_fields_are_tuples_and_frozen():
    for field in ("A_plus", "F_plus", "A_minus", "F_minus"):
        assert isinstance(getattr(NESTED, field), tuple)
    with pytest.raises(TypeError):
        NESTED.A_plus[0] = (Fraction(1), None)
    for field in ("A_plus", "F_plus", "n_dec", "n_min"):
        with pytest.raises(AttributeError):
            setattr(NESTED, field, None)
    with pytest.raises(AttributeError):
        del NESTED.A_plus


def test_nested_payloads_equally_immutable():
    payload = NESTED.A_plus[0][1]
    assert isinstance(payload.A_plus, tuple)
    with pytest.raises(AttributeError):
        payload.F_plus = (1, 1)


def test_hash_follows_equality_and_membership_is_stable():
    a = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
    assert a == S2 and hash(a) == hash(S2)
    pool = {a, S2, E, NESTED}
    assert len(pool) == 3
    assert S2 in pool and E in pool and NESTED in pool
    assert stable_hash(a) == stable_hash(S2)


def test_copy_and_deepcopy_preserve_identity():
    assert copy.copy(NESTED) is NESTED
    assert copy.deepcopy(NESTED) is NESTED


def test_algebra_serialization_codec_survive_immutability():
    prod = multiply(NESTED, S2)
    assert len(prod.A_plus) == len(NESTED.A_plus) * len(S2.A_plus)
    assert isinstance(prod.A_plus, tuple)
    assert stable_hash(prod)
    encoded = recursive_encode({"k": [1, 2]})
    assert isinstance(encoded.A_plus, tuple)


def test_no_production_path_manufactures_empty():
    """multiply on carrier members always yields carrier members."""
    for a in (E, S2, NESTED):
        for b in (E, S2, NESTED):
            assert len(multiply(a, b).A_plus) >= 1
