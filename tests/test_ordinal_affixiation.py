# === CHECKS ===
# id: ordinal_placement_check
#   proves: ordinal_exact_placement, ordinal_equidistant_initial_field
#   call: self::test_independent_append_oracle
#   requires: python3, pytest
#   mutates: none
#   cleanup: none
# id: ordinal_recursive_check
#   proves: ordinal_recursive_recovery
#   call: self::test_nested_recovery
#   requires: python3, pytest
#   mutates: none
#   cleanup: none
# === END CHECKS ===
"""Usage: PYTHONPATH=src python -m pytest -q tests/test_ordinal_affixiation.py."""
from fractions import Fraction
from itertools import product
import dataclasses
import pytest
from ucns.ordinal_affixiation import Carrier, Participant, Placement, affixiate


def construct(text, carrier=None):
    carrier = carrier or Carrier(tuple(' ABC'), 'fixture-v1')
    return affixiate(text, tuple(Participant.atom(carrier, s) for s in text),
                     origin='SPACE', relation='ordered', source='fixture:' + text)


def test_independent_append_oracle():
    carrier = Carrier(tuple(' ABC'), 'fixture-v1')
    for length in range(1, 7):
        for values in product('ABC', repeat=length):
            obj = construct(''.join(values), carrier)
            oracle = []
            for _ in values:
                oracle = [r / 2 for r in oracle] + [Fraction(1, 2)]
            assert [obj.placement(i).radius() for i in range(length)] == oracle
            assert [obj.placement(i).turn for i in range(length)] == [
                Fraction(carrier.identities.index(v), 4) for v in values]
            assert obj.recover() == values
    for a in carrier.identities:
        for b in carrier.identities:
            assert carrier.initial_distance(a, b, Fraction(3, 2)) == (
                0 if a == b else Fraction(3, 2))


def test_nested_recovery():
    glyphs = Carrier(tuple(' ABC'), 'fixture-v1')
    first, second = construct('ABA', glyphs), construct('C', glyphs)
    words = Carrier(('ABA', 'C'), 'fixture-words-v1')
    p = Participant.closed(words, first)
    phrase = affixiate('phrase', (p, Participant.closed(words, second), p),
                        origin='SPACE', relation='ordered-text', source='fixture:phrase')
    assert phrase.recover() == tuple('ABACABA')
    assert phrase.participants[0] is phrase.participants[2]
    assert phrase.participants[0].interior is first
    assert [phrase.placement(i).radius() for i in range(3)] == [
        Fraction(1, 8), Fraction(1, 4), Fraction(1, 2)]
    assert first.placement(0).radius() == Fraction(1, 8)
    assert phrase.placement(1).turn == Fraction(1, 2)


def test_deep_recursion_is_iterative():
    obj = construct('A')
    for i in range(1500):
        carrier = Carrier((obj.identity,), 'level:' + str(i))
        obj = affixiate('level:' + str(i), (Participant.closed(carrier, obj),),
                        origin='SPACE', relation='explicit-nesting', source='fixture')
    assert obj.recover() == ('A',)


def test_large_exponent_does_not_underflow_in_storage():
    obj = construct('A' * 10000)
    assert obj.placement(0).exponent == 10000
    assert obj.placement(0).radius().denominator.bit_length() == 10001
    assert obj.placement(9999).radius() == Fraction(1, 2)
    with pytest.raises(ArithmeticError):
        obj.placement(0).display_xy()


def test_initial_and_placed_metrics_are_not_conflated():
    obj = construct('AA')
    assert obj.participants[0].carrier.initial_distance('A', 'A') == 0
    assert obj.placement(1).radius() - obj.placement(0).radius() == Fraction(1, 4)


def test_exact_nonunit_radius():
    assert construct('ABC').placement(0).radius(Fraction(5, 3)) == Fraction(5, 24)


def test_carrier_revision_is_bound():
    a = construct('AB', Carrier(('A', 'B'), 'v1'))
    b = construct('AB', Carrier(('B', 'A'), 'v2'))
    assert a.receipt != b.receipt
    assert a.placement(0).turn != b.placement(0).turn


def test_identity_does_not_replace_geometry():
    a = construct('AB')
    assert len(a.record()['placements']) == 2
    assert a.record()['placements'][0]['radius']['power_of_two_denominator'] == 2
    with pytest.raises(dataclasses.FrozenInstanceError):
        a.origin = 'changed'
    with pytest.raises(TypeError):
        a.participants[0].carrier._index['A'] = 0


@pytest.mark.parametrize('values', [(), ('A', 'A'), ('',), ('\ud800',), ['A']])
def test_invalid_carriers_fail(values):
    with pytest.raises((ValueError, TypeError)):
        Carrier(values, 'fixture')


@pytest.mark.parametrize('radius', [0, -1, True, 0.5, float('nan'), '1'])
def test_inexact_or_invalid_radius_fails(radius):
    with pytest.raises(ValueError):
        construct('A').placement(0).radius(radius)


@pytest.mark.parametrize('ordinal', [True, -1, 0.5, '0', 9])
def test_bad_ordinals_fail(ordinal):
    with pytest.raises((ValueError, IndexError)):
        construct('A').placement(ordinal)


def test_empty_closure_refuses():
    with pytest.raises(ValueError):
        affixiate('empty', (), origin='SPACE', relation='ordered', source='fixture')


def test_unadmitted_identity_refuses():
    with pytest.raises(ValueError):
        Participant.atom(Carrier(('A',), 'fixture'), 'B')


def test_mismatched_closed_identity_refuses():
    with pytest.raises(ValueError):
        Participant(Carrier(('A', 'B'), 'fixture'), 'B', construct('A'))


def test_source_and_relation_affect_receipt():
    a = construct('A')
    b = affixiate('A', a.participants, origin='SPACE', relation='different', source=a.source)
    c = affixiate('A', a.participants, origin='other', relation=a.relation, source=a.source)
    assert len({a.receipt, b.receipt, c.receipt}) == 3
