# ratios: loc_comments=133:44 imports_exports=7:6 calls_definitions=68:6
# === CHECKS ===
# id: unicode_recursive_reentry_check
#   proves: unicode_closed_objects_reenter, unicode_recursive_equal_radius, unicode_recursive_source_identity
#   call: self::test_complete_objects_reenter_with_interiors_and_exact_text
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_recursive_inverse_check
#   proves: unicode_recursive_placement_inverse
#   call: self::test_placement_composition_and_inverse
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_recursive_boundary_check
#   proves: unicode_recursive_bearing_is_explicit
#   call: self::test_missing_or_inexact_placement_refuses
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_recursive_replay_check
#   proves: unicode_recursive_graph_replay
#   call: self::test_graph_replays_at_depth_and_preserves_shared_occurrences
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_recursive_mutation_check
#   proves: unicode_recursive_graph_replay
#   call: self::test_graph_rejects_mutations_even_with_resealed_outer_receipt
#   requires: pytest
#   timeout: 60
#   mutates: none
#   cleanup: none
# id: unicode_recursive_native_integrity_check
#   proves: unicode_recursive_object_integrity
#   call: self::test_forged_native_objects_and_cycles_refuse
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
from ucns.unicode_gonol import build_unicode_scalar_frame, unicode_glyph_gonol, _digest
from ucns.unicode_recursive import (
    UnicodeClosedFrame, close_unicode, export_unicode_graph, replay_unicode_graph,
    validate_unicode,
)


def test_complete_objects_reenter_with_interiors_and_exact_text():
    text = '\ufeffAë𐍈 e\u0308!\n\x00'
    leaf = build_unicode_scalar_frame(text, radius=Fraction(7, 3))
    leaf_record = leaf.record()
    first = close_unicode((leaf, leaf), bearings=(0, Fraction(1, 2)),
                          relation='ordered', source='fixture:first', radius=5)
    second = close_unicode((first, leaf, first), bearings=(0, Fraction(1, 3), Fraction(2, 3)),
                           relation='ordered', source='fixture:second', radius=11)
    assert second.recover() == text * 5
    assert second.utf8 == (text * 5).encode('utf-8')
    assert second.utf32_be == (text * 5).encode('utf-32-be')
    assert second.participants[0] is first and second.participants[2] is first
    assert first.participants[0] is leaf and first.participants[1] is leaf
    assert {p.radius for p in second.placements} == {11}
    assert {p.radius for p in first.placements} == {5}
    assert {p.radius for p in leaf.placements} == {Fraction(7, 3)}
    assert leaf.record() == leaf_record
    assert all(g.bit_radius == 16 and len(g.utf32_be) == 4 for g in leaf.glyphs)
    glyphs = tuple(unicode_glyph_gonol(c) for c in 'eëe\u0308')
    closed = close_unicode(glyphs, relation='ordered', source='fixture:scalars')
    assert closed.bearings == tuple(g.turn for g in glyphs)
    assert closed.recover() == 'eëe\u0308'
    changed_source = close_unicode(first.participants, bearings=first.bearings,
                                  relation=first.relation, source='different', radius=first.radius)
    assert changed_source.receipt != first.receipt
    regrouped = close_unicode((build_unicode_scalar_frame(text * 2),), bearings=(0,),
                              relation='ordered', source='fixture:first', radius=5)
    assert regrouped.recover() == first.recover() and regrouped.receipt != first.receipt


def test_placement_composition_and_inverse():
    leaf = build_unicode_scalar_frame('A', radius=2)
    child = close_unicode((leaf,), bearings=(Fraction(1, 4),), rotations=(Fraction(1, 3),),
                          relation='placed', source='child', radius=7)
    parent = close_unicode((child,), bearings=(Fraction(3, 4),), rotations=(Fraction(1, 6),),
                           relation='placed', source='parent', radius=11)
    point = Point(((Direction(Fraction(1, 7)), Fraction(5, 2)),))
    p, q = child.placements[0], parent.placements[0]
    assert p.origin == Point(((Direction(Fraction(1, 4)), Fraction(7)),))
    composed = q.to_parent(p.to_parent(point))
    expected = (Point(((Direction(Fraction(3, 4)), Fraction(11)),))
                + Point(((Direction(Fraction(5, 12)), Fraction(7)),))
                + point.rotated(Direction(Fraction(1, 2))))
    assert composed == expected
    assert p.to_local(q.to_local(composed)) == point
    assert p.to_local(p.to_parent(Point())) == Point()


@pytest.mark.parametrize('kwargs', [
    {}, {'bearings': (0.5,)}, {'bearings': (True,)}, {'bearings': ()},
    {'bearings': [0]}, {'bearings': (0,), 'radius': 0},
    {'bearings': (0,), 'radius': 1.5}, {'bearings': (0,), 'radius': True},
    {'bearings': (0,), 'rotations': (0.5,)}, {'bearings': (0,), 'rotations': ()},
])
def test_missing_or_inexact_placement_refuses(kwargs):
    with pytest.raises(ValueError):
        close_unicode((build_unicode_scalar_frame('A'),), relation='ordered', source='fixture', **kwargs)
    with pytest.raises(ValueError, match='UNICODE_SCALAR_BEARING_MISMATCH'):
        close_unicode((unicode_glyph_gonol('A'),), bearings=(0,), relation='ordered', source='fixture')


def test_graph_replays_at_depth_and_preserves_shared_occurrences():
    leaf = build_unicode_scalar_frame('ë\x00')
    root = close_unicode((leaf, leaf), bearings=(0, Fraction(1, 2)), relation='pair', source='pair')
    for level in range(1100):
        root = UnicodeClosedFrame((root,), (Fraction(1, 7),), 'nested', str(level))
    graph = export_unicode_graph(root)
    copy = replay_unicode_graph(json.loads(json.dumps(graph)))
    assert copy.receipt == root.receipt
    assert copy.recover() == 'ë\x00ë\x00'
    assert export_unicode_graph(copy) == graph
    for _ in range(1100):
        copy = copy.participants[0]
    assert copy.participants[0] is copy.participants[1]
    assert len(graph['nodes']) == 1102


@pytest.mark.parametrize('mutation', [
    'source', 'relation', 'bearing', 'rotation', 'radius', 'order', 'missing',
    'cycle', 'duplicate', 'extra', 'scalar_bytes', 'root', 'root_space', 'noncanonical', 'boolean',
])
def test_graph_rejects_mutations_even_with_resealed_outer_receipt(mutation):
    leaves = tuple(build_unicode_scalar_frame(text) for text in ('e', 'ë'))
    root = close_unicode(leaves, bearings=(0, Fraction(1, 2)), relation='ordered', source='fixture')
    record = deepcopy(export_unicode_graph(root))
    data = record['nodes'][-1]['object']
    if mutation in ('source', 'relation'):
        data[mutation] = 'changed'
    elif mutation in ('bearing', 'rotation'):
        data[mutation + 's'][0] = [1, 3]
    elif mutation == 'radius':
        data['radius'] = [2, 1]
    elif mutation == 'order':
        data['participants'].reverse()
    elif mutation == 'missing':
        del record['nodes'][0]
    elif mutation == 'cycle':
        data['participants'][0] = root.receipt
    elif mutation == 'duplicate':
        record['nodes'].insert(0, deepcopy(record['nodes'][0]))
    elif mutation == 'extra':
        extra = unicode_glyph_gonol('Q')
        record['nodes'].insert(0, {'receipt': extra.receipt, 'object': extra.record(include_receipt=False)})
    elif mutation == 'scalar_bytes':
        record['nodes'][0]['object']['glyphs'][0]['utf32_be_bytes'][0] = 1
    elif mutation == 'root':
        record['root'] = leaves[0].receipt
    elif mutation == 'root_space':
        record['root_space'] = [1, 2]
    elif mutation == 'noncanonical':
        data['radius'] = [2, 2]
    elif mutation == 'boolean':
        data['bearings'][0] = [False, 1]
    record['receipt'] = _digest({k: v for k, v in record.items() if k != 'receipt'})
    with pytest.raises(ValueError):
        replay_unicode_graph(record)


def test_forged_native_objects_and_cycles_refuse():
    glyph = unicode_glyph_gonol('A')
    object.__setattr__(glyph, 'utf32_be', b'bad')
    with pytest.raises(ValueError, match='RECEIPT'):
        close_unicode((glyph,), relation='ordered', source='fixture')
    frame = build_unicode_scalar_frame('A')
    object.__setattr__(frame, 'text', 'B')
    with pytest.raises(ValueError, match='RECEIPT'):
        close_unicode((frame,), bearings=(0,), relation='ordered', source='fixture')
    with pytest.raises(TypeError, match='NATIVE_UNICODE_OBJECT_REQUIRED'):
        close_unicode(('A',), bearings=(0,), relation='ordered', source='fixture')
    root = close_unicode((unicode_glyph_gonol('A'),), relation='ordered', source='fixture')
    object.__setattr__(root, 'participants', (root,))
    with pytest.raises(ValueError, match='CYCLIC'):
        validate_unicode(root)
# ratios: loc_comments=133:44 imports_exports=7:6 calls_definitions=68:6
