# ratios: loc_comments=229:75 imports_exports=11:11 calls_definitions=160:11
# === CHECKS ===
# id: check_public_pair_census
#   proves: attachment_stack_recurrence, attachment_stack_views
#   call: self::test_public_pair_census
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_append_oracle_and_disk_depth
#   proves: attachment_stack_recurrence
#   call: self::test_append_oracle_and_disk_depth
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_both_views_and_root_frame
#   proves: attachment_stack_views, attachment_complete_replay
#   call: self::test_both_views_and_root_frame
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_recursive_candidates_preserve_interiors
#   proves: attachment_stack_closure, attachment_stack_recurrence
#   call: self::test_recursive_candidates_preserve_interiors
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_no_implicit_bearing_and_candidates_differ
#   proves: attachment_stack_closure
#   call: self::test_no_implicit_bearing_and_candidates_differ
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_compound_transport_and_wrong_occurrence
#   proves: attachment_stack_transport
#   call: self::test_compound_transport_and_wrong_occurrence
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_complete_graph_and_mutation_controls
#   proves: attachment_complete_replay
#   call: self::test_complete_graph_and_mutation_controls
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_deep_closure_and_display_underflow
#   proves: attachment_stack_closure, attachment_stack_display_boundary
#   call: self::test_deep_closure_and_display_underflow
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# id: check_invalid_inputs_and_chain_mutants
#   proves: attachment_stack_recurrence, attachment_stack_views
#   call: self::test_invalid_inputs_and_chain_mutants
#   requires: python3, pytest
#   timeout: hmmm
#   mutates: none
#   cleanup: none
# === END CHECKS ===
"""Native geometry falsifiers. Run: python -m pytest tests/test_attachment_stack.py.

GPT generated; context, prompt Erin Spencer.
The Public Gonol pair census compares exact coefficients against an independent
cyclotomic representation. Candidate-bearing tests establish execution, not
selection. All tests use the real native constructors.
"""
from copy import deepcopy
from fractions import Fraction as F
from itertools import product
import cmath
import json
import math

import pytest

from ucns.ordinal_affixiation import Carrier, Participant
from ucns.public_gonol import PUBLIC_GONOL_157, PUBLIC_GONOL_SHA256
from ucns.attachment_stack import (
    POLICIES, Closed, Direction, Point, Ray, stack, join, attached_view,
    recover_common, common_view, attach, display,
)
from ucns.attachment_codec import export_graph, replay_graph, export_view, replay_view


def make(text, carrier=None):
    carrier = carrier or Carrier(PUBLIC_GONOL_157, PUBLIC_GONOL_SHA256)
    return stack(text, tuple(Participant.atom(carrier, c) for c in text),
                 relation='fixture-ordered', source='fixture:' + text)


def coefficients(point):
    values = [F(0)] * 157
    for direction, q in point.terms:
        assert not direction.endpoints
        index = direction.turn * 157
        assert index.denominator == 1
        values[index.numerator] += q
    return tuple(v - values[-1] for v in values[:-1])


def test_public_pair_census():
    carrier = Carrier(PUBLIC_GONOL_157, PUBLIC_GONOL_SHA256)
    for a, b in product(range(1, 157), repeat=2):
        obj = make(carrier.identities[a] + carrier.identities[b], carrier)
        expected = [F(0)] * 157
        expected[a] += F(1, 4)
        expected[(a + b) % 157] += F(1, 2)
        assert coefficients(obj.endpoint) == tuple(v - expected[-1] for v in expected[:-1])
        rows = attached_view(obj.rays)
        assert rows[1][0] == rows[0][1]
        assert recover_common(rows) == obj.rays
        assert obj.rays[0].heading.turn == F(a, 157)
        assert obj.rays[1].heading.turn == F((a + b) % 157, 157)
        assert obj.recover() == (carrier.identities[a], carrier.identities[b])


def test_append_oracle_and_disk_depth():
    carrier = Carrier(tuple('ABCD'), 'quarter-turn-fixture')
    for n in range(1, 6):
        for text in product('ABC', repeat=n):
            obj = make(''.join(text), carrier)
            oracle, heading = [], 0.0
            for glyph in text:
                oracle = [p / 2 for p in oracle]
                heading += carrier.identities.index(glyph) * math.pi / 2
                oracle.append((oracle[-1] if oracle else 0) + .5 * cmath.exp(1j * heading))
            actual = attached_view(obj.rays)
            for (origin, endpoint), expected in zip(actual, oracle):
                assert abs(display(endpoint) - expected) < 2e-14
            assert [obj.depth(i) for i in range(n)] == list(range(n, 0, -1))
            if n > 1:
                previous = make(''.join(text[:-1]), carrier)
                appended = previous.append(Participant.atom(carrier, text[-1]), identity=obj.identity, source=obj.source)
                assert appended.receipt == obj.receipt
                assert tuple(ray.radius for ray in obj.rays[:-1]) == tuple(ray.radius / 2 for ray in previous.rays)


def test_both_views_and_root_frame():
    obj = make('lll')
    space = Direction(F(7, 157))
    origin = Point(((Direction(F(1, 4)), F(3, 2)),))
    common = common_view(obj, space=space)
    rows = attached_view(common, origin=origin)
    assert recover_common(rows, origin=origin) == common
    previous = space
    for ray, glyph in zip(recover_common(rows, origin=origin), obj.participants):
        local = ray.heading.compose(previous.inverse())
        assert local == Direction(glyph.carrier.turn(glyph.identity))
        previous = ray.heading
    assert common != obj.rays
    for kind in ('common', 'attached'):
        packet = json.loads(json.dumps(export_view(obj, kind=kind, space=space, origin=origin)))
        rebuilt, s, o = replay_view(packet)
        assert rebuilt.receipt == obj.receipt and s == space and o == origin
        changed = deepcopy(packet)
        changed['space']['turn'] = [8, 157]
        with pytest.raises(ValueError):
            replay_view(changed)
        del packet['space']
        with pytest.raises(ValueError):
            replay_view(packet)
    # Moving every root leaves local displacements recoverable, not congruent
    # to a view which moves each local origin to the same displayed point.
    common_distance = abs(display(common[1].vector - common[0].vector))
    attached_distance = abs(display(rows[1][1] - rows[0][1]))
    assert not math.isclose(common_distance, attached_distance)


def test_recursive_candidates_preserve_interiors():
    word, other = make('bull'), make('shit')
    before = export_graph(word)
    for policy in POLICIES:
        parent = stack('fixture-parent', (Closed(word, policy), Closed(other, policy)),
                       relation='declared-sequence', source='fixture')
        after = parent.append(Closed(word, policy), identity='fixture-three', source='fixture')
        assert after.recover() == tuple('bullshitbull')
        assert [after.depth(i) for i in range(3)] == [3, 2, 1]
        assert after.participants[0].interior is after.participants[2].interior is word
        assert export_graph(word) == before
        for old, new in zip(parent.rays, after.rays):
            assert old.heading == new.heading and new.radius == old.radius / 2
        assert recover_common(attached_view(after.rays)) == after.rays
        higher = stack('next-scale', (Closed(after, policy), Closed(parent, policy)),
                       relation='declared-recursion', source='fixture')
        assert replay_graph(export_graph(higher)).recover() == higher.recover()
        for kind in ('common', 'attached'):
            assert replay_view(export_view(higher, kind=kind))[0].receipt == higher.receipt
        assert math.isfinite(abs(display(higher.endpoint)))


def test_no_implicit_bearing_and_candidates_differ():
    c = Carrier(tuple('ABCD'), 'quarter-turn-fixture')
    word = make('AB', c)  # endpoint=1/4 + i/2; exit heading=i
    with pytest.raises(TypeError):
        Closed(word)
    with pytest.raises(ValueError, match='CLOSED_BEARING_POLICY_REQUIRED'):
        Closed(word, 'automatic')
    values = []
    for policy in POLICIES:
        result = stack('parent', (Closed(word, policy),), relation='fixture', source='fixture')
        values.append(display(result.endpoint))
    assert abs(values[0] - (.25 + .5j) / abs(.25 + .5j) / 2) < 1e-14
    assert abs(values[1] - .5j) < 1e-14
    assert abs(values[0] - values[1]) > .1
    assert make('AB', c).exit_heading == make('BA', c).exit_heading
    assert make('AB', c).receipt != make('BA', c).receipt


def test_compound_transport_and_wrong_occurrence():
    left, right = make('bull'), make('shit')
    rows = attach(left, 3, right)
    left_rows = attached_view(left.rays)
    assert rows[0][0] == left_rows[3][1]
    assert rows[0][0] != left_rows[2][1]
    assert rows != attach(left, 2, right)
    local = recover_common(rows, origin=left_rows[3][1])
    assert [r.radius for r in local] == [r.radius for r in right.rays]
    for transformed, original in zip(local, right.rays):
        assert transformed.heading.compose(left.exit_heading.inverse()) == original.heading
    assert [r.radius / 2 for r in local] != [r.radius for r in right.rays]
    assert right.recover() == tuple('shit') and left.recover() == tuple('bull')
    compound = join('compound', left, right, relation='declared-join', source='fixture')
    assert compound.left is left and compound.right is right
    assert attached_view(compound.rays)[4:] == rows
    assert compound.endpoint_nonzero() is True
    for policy in POLICIES:
        parent = stack('compound-parent', (Closed(compound, policy), Closed(left, policy)), relation='fixture', source='fixture')
        assert replay_graph(export_graph(parent)).recover() == tuple('bullshitbull')
        assert abs(display(parent.endpoint)) > 0
        assert replay_view(export_view(parent))[0].receipt == parent.receipt
    # A closed join can have a zero endpoint; unlike a dyadic stack, it cannot
    # be normalized without a nonzero proof. Its exit frame still exists.
    carrier = Carrier(('A', 'B'), 'half-turn-fixture')
    zero = join('zero', make('A', carrier), make('B', carrier), relation='join', source='fixture')
    assert zero.endpoint_nonzero() is False
    with pytest.raises(ValueError, match='NONZERO_PROOF'):
        stack('invalid', (Closed(zero, 'root-endpoint-v1'),), relation='fixture', source='fixture')
    assert stack('exit', (Closed(zero, 'exit-heading-v1'),), relation='fixture', source='fixture').recover() == ('A', 'B')


def test_complete_graph_and_mutation_controls():
    word = make('word')
    parent = stack('repeated', (Closed(word, 'exit-heading-v1'),) * 2, relation='pair', source='fixture')
    packet = json.loads(json.dumps(export_graph(parent)))
    rebuilt = replay_graph(packet)
    assert rebuilt.participants[0].interior is rebuilt.participants[1].interior
    assert rebuilt.recover() == tuple('wordword')
    mutants = []
    for mutate in (
        lambda x: x.pop('root_space'),
        lambda x: x.update(root_space=[False, True]),
        lambda x: x['nodes'].pop(0),
        lambda x: x['nodes'].append(x['nodes'][0]),
        lambda x: x['nodes'][-1]['construction']['participants'][0].update(interior=x['root']),
        lambda x: x['nodes'][-1]['construction']['participants'].pop(),
        lambda x: x['nodes'][-1]['construction'].update(radius=[2, 2]),
        lambda x: x['nodes'][-1]['construction']['participants'][0].update(bearing='root-endpoint-v1'),
        lambda x: x['carriers'][0]['identities'].reverse(),
    ):
        bad = deepcopy(packet)
        mutate(bad)
        mutants.append(bad)
    for bad in mutants:
        with pytest.raises(ValueError):
            replay_graph(bad)
    view = export_view(parent)
    for mutate in (
        lambda x: x['rows'][1].update(origin=x['rows'][0]['origin']),
        lambda x: x['rows'][0]['point'][0].update(coefficient=[1, 1]),
        lambda x: x['space'].update(turn=[False, True]),
    ):
        bad = deepcopy(view)
        mutate(bad)
        with pytest.raises(ValueError):
            replay_view(bad)


def test_deep_closure_and_display_underflow():
    obj = make('A')
    for i in range(1100):
        obj = stack(str(i), (Closed(obj, 'exit-heading-v1'),), relation='nested', source='fixture')
    assert obj.recover() == ('A',)
    assert replay_graph(export_graph(obj)).recover() == ('A',)
    endpoint_nested = make('AB', Carrier(tuple('ABCD'), 'quarter-turn-fixture'))
    for i in range(1100):
        endpoint_nested = stack(str(i), (Closed(endpoint_nested, 'root-endpoint-v1'),), relation='nested', source='fixture')
    assert replay_graph(export_graph(endpoint_nested)).recover() == ('A', 'B')
    assert abs(display(endpoint_nested.endpoint)) > 0
    primitive = make('A', Carrier(('A', 'B'), 'half-turn-fixture'))
    joined = primitive
    for i in range(1100):
        joined = join(str(i), joined, primitive, relation='join', source='fixture')
    assert replay_graph(export_graph(joined)).recover() == ('A',) * 1101
    assert display(joined.endpoint) == complex(1101 / 2, 0)
    parent = stack('joined-parent', (Closed(joined, 'root-endpoint-v1'),), relation='fixture', source='fixture')
    assert display(parent.endpoint) == complex(.5, 0)
    deep = make('l' * 1076)
    assert deep.rays[0].radius == F(1, 1 << 1076)
    assert deep.depth(0) == 1076
    with pytest.raises(ArithmeticError, match='DISPLAY_RANGE'):
        display(deep.rays[0].vector)
    tiny_turn = Point(((Direction(), F(1)), (Direction(F(1, 1 << 1076)), F(-1))))
    with pytest.raises(ArithmeticError, match='DISPLAY_RANGE'):
        display(tiny_turn)


def test_invalid_inputs_and_chain_mutants():
    word = make('ll')
    carrier = word.participants[0].carrier
    for invalid in ((), list(word.participants), (Closed,), (object(),)):
        with pytest.raises((ValueError, TypeError)):
            stack('bad', invalid, relation='fixture', source='fixture')
    for invalid in (True, 1.0, 0, -1):
        with pytest.raises(ValueError):
            stack('bad', word.participants, relation='fixture', source='fixture', radius=invalid)
    for invalid in (True, 1.5, -1):
        with pytest.raises(ValueError):
            word.depth(invalid)
    rows = attached_view(word.rays)
    with pytest.raises(ValueError, match='ATTACHMENT_CHAIN_MISMATCH'):
        recover_common((rows[0], (Point(), rows[1][1])))
    reset = (word.rays[0], Ray(word.rays[1].radius, word.rays[0].heading))
    assert attached_view(reset) != rows
# ratios: loc_comments=229:75 imports_exports=11:11 calls_definitions=160:11
