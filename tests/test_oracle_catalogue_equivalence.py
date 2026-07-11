"""Regression tests for exact oracle-catalogue equivalence.

Geometric bounds and oracle membership are distinct. An oracle atom is exactly
``None`` or a structural member of the canonical generated catalogue.
"""

import itertools
from fractions import Fraction

from ucns import (
    ORACLE_ATOM_PAYLOADS,
    ORACLE_CATALOGUE_RULE_VERSION,
    S2,
    UCNSObject,
    UNIT,
    generate_payload_catalogue,
    in_domain,
    is_in_oracle_class,
    is_oracle_atom,
    payload_catalogue_fingerprint,
    verified_domain_status,
)
from ucns.catalogue import build_catalogue_d1


def _member(obj, catalogue):
    if obj is None:
        return any(candidate is None for candidate in catalogue)
    return any(
        candidate is not None and obj == candidate
        for candidate in catalogue
    )


def test_catalogue_is_deterministic_unit_first_and_copy_on_return():
    first = generate_payload_catalogue()
    second = generate_payload_catalogue()

    assert isinstance(ORACLE_ATOM_PAYLOADS, tuple)
    assert first is not second
    assert first == second
    assert first[0] is UNIT
    assert payload_catalogue_fingerprint(first) == payload_catalogue_fingerprint(second)
    assert ORACLE_CATALOGUE_RULE_VERSION == "oracle-atoms-carrier-grid-v1"

    first.pop()
    assert generate_payload_catalogue() == second, "list mutation changed canon"

    mutable_copy = generate_payload_catalogue()
    original = generate_payload_catalogue()
    assert mutable_copy[1] is not original[1]
    mutable_copy[1].F_plus[0] ^= 1
    assert generate_payload_catalogue() == original, "object mutation changed canon"


def test_public_constant_mutation_does_not_change_membership_truth():
    public_obj = ORACLE_ATOM_PAYLOADS[1]
    canonical_obj = generate_payload_catalogue()[1]
    assert public_obj is not canonical_obj
    assert is_oracle_atom(canonical_obj)

    old_bit = public_obj.F_plus[0]
    try:
        public_obj.F_plus[0] ^= 1
        assert is_oracle_atom(canonical_obj)
        assert generate_payload_catalogue()[1] == canonical_obj
    finally:
        public_obj.F_plus[0] = old_bit


def test_catalogue_has_no_structural_duplicates():
    catalogue = generate_payload_catalogue()
    for index, candidate in enumerate(catalogue):
        assert not any(
            (candidate is None and prior is None)
            or (
                candidate is not None
                and prior is not None
                and candidate == prior
            )
            for prior in catalogue[:index]
        )


def test_every_catalogue_member_is_an_oracle_atom():
    for candidate in generate_payload_catalogue():
        assert is_oracle_atom(candidate)


def test_predicate_equals_membership_on_adversarial_bounded_universe():
    """Exercise thousands of flat objects inside the geometric bounds."""
    catalogue = generate_payload_catalogue()
    angle_pool = [Fraction(k, 2) for k in range(8)]

    for length in (1, 2, 3):
        for angles in itertools.product(angle_pool, repeat=length):
            for faces in itertools.product((0, 1), repeat=length):
                obj = UCNSObject(
                    8,
                    1,
                    list(zip(angles, [UNIT] * length)),
                    list(faces),
                )
                assert in_domain(obj)
                assert is_oracle_atom(obj) == _member(obj, catalogue)


def test_bounded_non_catalogue_witness_is_not_oracle():
    witness = UCNSObject(
        4,
        4,
        [(Fraction(0), UNIT), (Fraction(3, 2), UNIT)],
        [0, 0],
    )

    assert in_domain(witness)
    assert not _member(witness, generate_payload_catalogue())
    assert not is_oracle_atom(witness)


def test_depth_two_status_uses_exact_payload_membership():
    witness = UCNSObject(
        4,
        4,
        [(Fraction(0), UNIT), (Fraction(3, 2), UNIT)],
        [0, 0],
    )
    outside = UCNSObject(4, 4, [(Fraction(0), witness)], [0])
    inside = UCNSObject(2, 2, [(Fraction(0), S2)], [0])

    assert not is_in_oracle_class(outside)
    assert verified_domain_status(outside) == "depth-2-non-oracle"
    assert is_in_oracle_class(inside)
    assert verified_domain_status(inside) == "depth-2-oracle"


def test_depth_one_catalogue_builder_matches_canonical_members():
    expected = [
        candidate
        for candidate in generate_payload_catalogue()
        if candidate is not None
    ]
    assert build_catalogue_d1() == expected


def test_public_and_compatibility_exports():
    import ucns
    import ucns_recursive

    for module in (ucns, ucns_recursive):
        assert module.ORACLE_CATALOGUE_RULE_VERSION == ORACLE_CATALOGUE_RULE_VERSION
        assert module.generate_payload_catalogue() == generate_payload_catalogue()
