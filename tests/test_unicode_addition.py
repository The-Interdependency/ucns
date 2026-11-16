# ratios: loc_comments=100:45 imports_exports=7:6 calls_definitions=66:6
# === CHECKS ===
# id: unicode_addition_result_check
#   proves: unicode_recursive_addition
#   call: self::test_addition_carries_the_exact_result_at_each_scale
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_addition_structure_check
#   proves: unicode_recursive_addition_retains_zero
#   call: self::test_zero_result_retains_its_operands_and_reenters
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_addition_grouping_check
#   proves: unicode_recursive_addition, unicode_recursive_addition_retains_zero
#   call: self::test_grouping_and_order_survive_equal_resultants
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_addition_replay_check
#   proves: unicode_recursive_addition, unicode_recursive_graph_replay
#   call: self::test_addition_replays_and_reenters_at_depth
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_addition_integrity_check
#   proves: unicode_recursive_object_integrity, unicode_recursive_graph_replay
#   call: self::test_addition_rejects_forged_results_and_graphs
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_addition_transform_check
#   proves: unicode_recursive_addition
#   call: self::test_addition_retains_native_radii_and_explicit_transforms
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# === END CHECKS ===
from copy import deepcopy
from fractions import Fraction
import json

import pytest

from ucns.attachment_stack import Direction, Point
from ucns.unicode_gonol import _digest, build_unicode_scalar_frame, unicode_glyph_gonol
from ucns.unicode_recursive import (
    UnicodeSum, add_unicode, close_unicode, export_unicode_graph,
    replay_unicode_graph, unicode_resultant, validate_unicode,
)


def test_addition_carries_the_exact_result_at_each_scale():
    # Four exact cardinal directions in the Unicode carrier, without trig or a selector.
    east = unicode_glyph_gonol(' ')
    north = unicode_glyph_gonol(chr(0x44020))
    word = close_unicode((east, north), relation='addition', source='fixture:word')
    expected = Point(((Direction(), Fraction(1)), (Direction(Fraction(1, 4)), Fraction(1))))
    assert word.resultant == expected
    assert unicode_resultant(build_unicode_scalar_frame(' ' + chr(0x44020))) == expected
    sentence = close_unicode((word, word), relation='addition', source='fixture:sentence')
    assert sentence.resultant == expected.scaled(2)
    assert sentence.participants == (word, word)
    assert sentence.recover() == (' ' + chr(0x44020)) * 2
    parent = close_unicode((sentence, word), relation='addition', source='fixture:parent')
    assert parent.resultant == expected.scaled(3)
    assert parent.utf8 == parent.recover().encode('utf-8')
    assert parent.utf32_be == parent.recover().encode('utf-32-be')


def test_zero_result_retains_its_operands_and_reenters():
    east = unicode_glyph_gonol(' ')
    west = unicode_glyph_gonol(chr(0x88020))
    zero = add_unicode((east, west), relation='addition', source='fixture:zero')
    assert zero.resultant == Point()
    assert zero.participants == (east, west)
    assert zero.recover() == ' ' + chr(0x88020)
    parent = add_unicode((zero, east, zero), relation='addition', source='fixture:after-zero')
    assert parent.resultant == Point(((Direction(), Fraction(1)),))
    assert parent.participants[0] is parent.participants[2]
    assert parent.recover() == zero.recover() + ' ' + zero.recover()


def test_grouping_and_order_survive_equal_resultants():
    a, b, c = (unicode_glyph_gonol(ch) for ch in 'ABC')
    left = add_unicode((add_unicode((a, b), relation='addition', source='ab'), c),
                       relation='addition', source='left')
    right = add_unicode((a, add_unicode((b, c), relation='addition', source='bc')),
                        relation='addition', source='right')
    forward = add_unicode((a, b, c), relation='addition', source='same-order-source')
    reverse = add_unicode((c, b, a), relation='addition', source='same-order-source')
    assert left.resultant == right.resultant == reverse.resultant
    assert left.recover() == right.recover() == 'ABC'
    assert reverse.recover() == 'CBA'
    assert len({left.receipt, right.receipt, reverse.receipt}) == 3
    assert forward.resultant == reverse.resultant and forward.receipt != reverse.receipt


def test_addition_replays_and_reenters_at_depth():
    leaf = build_unicode_scalar_frame('\ufeffAë𐍈 e\u0308!\n\x00')
    root = add_unicode((leaf, leaf), relation='addition', source='shared')
    expected = root.resultant
    for level in range(1100):
        root = UnicodeSum((root,), 'addition', str(level))
    graph = export_unicode_graph(root)
    copy = replay_unicode_graph(json.loads(json.dumps(graph)))
    assert copy.receipt == root.receipt
    assert copy.resultant == expected
    assert copy.recover() == leaf.text * 2
    assert export_unicode_graph(copy) == graph
    continued = add_unicode((copy, leaf), relation='addition', source='after-replay')
    assert continued.recover() == leaf.text * 3
    for _ in range(1100):
        copy = copy.participants[0]
    assert copy.participants[0] is copy.participants[1]


def test_addition_rejects_forged_results_and_graphs():
    leaf = build_unicode_scalar_frame('Aë')
    good = add_unicode((leaf, leaf), relation='addition', source='fixture')
    for field, value in (('resultant', []), ('operation', 'normalize'), ('source', 'forged'),
                         ('rotations', [[1, 2], [0, 1]]), ('radius', [2, 2])):
        graph = deepcopy(export_unicode_graph(good))
        graph['nodes'][-1]['object'][field] = value
        graph['receipt'] = _digest({k: v for k, v in graph.items() if k != 'receipt'})
        with pytest.raises(ValueError):
            replay_unicode_graph(graph)
    object.__setattr__(good, 'resultant', Point())
    with pytest.raises(ValueError, match='RECEIPT'):
        validate_unicode(good)
    cyclic = UnicodeSum((leaf,), 'addition', 'cycle')
    object.__setattr__(cyclic, 'participants', (cyclic,))
    with pytest.raises(ValueError, match='CYCLIC'):
        validate_unicode(cyclic)
    with pytest.raises(TypeError, match='NATIVE_UNICODE_OBJECT_REQUIRED'):
        add_unicode(('A',), relation='addition', source='bad')
    with pytest.raises(ValueError, match='NONEMPTY'):
        add_unicode((), relation='addition', source='empty')


def test_addition_retains_native_radii_and_explicit_transforms():
    leaf = build_unicode_scalar_frame(' ', radius=Fraction(7, 3))
    before = leaf.record()
    first = add_unicode((leaf, leaf), relation='addition', source='radius')
    assert first.resultant == Point(((Direction(), Fraction(14, 3)),))
    rotated = add_unicode((first,), relation='addition', source='rotated',
                          radius=3, rotations=(Fraction(1, 4),))
    assert rotated.resultant == Point(((Direction(Fraction(1, 4)), Fraction(14)),))
    assert leaf.record() == before
    assert rotated.participants[0] is first and first.participants[0] is leaf
    for kwargs in ({'radius': 0}, {'radius': 1.5}, {'rotations': (True,)}, {'rotations': ()}):
        with pytest.raises(ValueError):
            add_unicode((leaf,), relation='addition', source='bad', **kwargs)
# ratios: loc_comments=100:45 imports_exports=7:6 calls_definitions=66:6
