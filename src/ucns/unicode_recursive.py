# ratios: loc_comments=207:60 imports_exports=5:6 calls_definitions=117:22
# === MODULE_BUILD ===
# id: unicode_recursive_geometry
#   module_name: unicode_recursive
#   module_kind: engine
#   summary: equal-radius recursive Unicode closure with retained interiors and explicit reversible local-frame placement
#   owner: Erin Spencer
#   public_surface: UnicodeClosedFrame, UnicodeObjectPlacement, close_unicode, validate_unicode, export_unicode_graph, replay_unicode_graph
#   internal_surface: iterative object validation and topological graph replay
#   auth_boundary: exact native objects and data integrity; no producer authentication
#   storage_boundary: immutable in-memory objects; caller owns serialization
#   network_boundary: none
#   user_data_boundary: caller text and provenance remain in returned objects
#   admin_only: false
#   tests: tests/test_unicode_recursive.py
#   rollout: explicit equal-radius closure alongside unchanged v2 primitive receipts
#   rollback: select the pinned prior producer; never reinterpret stored receipts
#   requires: unicode_gonol_geometry, ucns_attachment_stack
#   unresolved: automatic closed-object bearing selection and affixiation beyond caller-declared rigid placement
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: unicode_closed_objects_reenter
#   given: valid glyphs, scalar frames or already closed Unicode frames
#   then: the same constructor accepts their ordered occurrences without rebuilding labels or flattening interiors
# id: unicode_recursive_equal_radius
#   given: one positive exact parent radius and explicit closed-object bearings
#   then: sibling origins lie on that circle and child-local radii and scalar bit widths remain unchanged
# id: unicode_recursive_placement_inverse
#   given: a declared parent bearing and local-frame rotation
#   then: exact native translation and rotation place local points and invert without loss
# id: unicode_recursive_bearing_is_explicit
#   given: a closed frame without supplied parent bearings or an inexact geometric input
#   then: construction refuses rather than choosing a historical policy or interpreting bit width as distance
# id: unicode_recursive_source_identity
#   given: ordered participants, relation and source provenance
#   then: receipts bind those inputs, all occurrences remain recoverable and distinct boundaries remain distinct
# id: unicode_recursive_graph_replay
#   given: a complete serialized Unicode object graph
#   then: iterative replay preserves shared interiors and every occurrence and rejects altered, cyclic, missing, extra or noncanonical records
# id: unicode_recursive_object_integrity
#   given: a forged native object or unsupported object type
#   then: validation refuses before admitting it to a new closed construction
# === END CONTRACTS ===
"""Recursive closure at a declared equal-radius boundary.

GPT generated; context, prompt Erin Spencer.

``close_unicode((frame, frame), bearings=(0, Fraction(1, 2)),
relation='ordered', source='example')`` retains both complete interiors. Repeat
the same operation at any declared scale. A bearing here is caller-supplied
placement, not a derived property of the child. The rigid local-frame map is
``parent = radius * exp(2*pi*i*bearing) + rotation * local``. Existing native
Point/Direction arithmetic supplies this map; no dyadic stack is constructed.
No next-scale selector, physical sheet lift or general affixiation law follows.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from .attachment_stack import Direction, Point
from .unicode_gonol import UnicodeGlyphGonol, UnicodeScalarFrame, _digest


def _exact(value, *, positive=False):
    if type(value) is not int and not isinstance(value, Fraction):
        raise ValueError('EXACT_INTEGER_OR_FRACTION_REQUIRED')
    value = Fraction(value)
    if positive and value <= 0:
        raise ValueError('POSITIVE_RADIUS_REQUIRED')
    return value


def _text(value):
    if not isinstance(value, str) or not value:
        raise ValueError('NONEMPTY_PROVENANCE_REQUIRED')
    value.encode('utf-8', errors='strict')
    return value


def _pair(value):
    return [value.numerator, value.denominator]


def _supported(obj):
    if type(obj) not in (UnicodeGlyphGonol, UnicodeScalarFrame, UnicodeClosedFrame):
        raise TypeError('NATIVE_UNICODE_OBJECT_REQUIRED')


@dataclass(frozen=True, slots=True, eq=False)
class UnicodeObjectPlacement:
    """One retained child and its explicit embedding in a parent frame."""
    ordinal: int
    interior: object
    radius: Fraction
    turn: Fraction
    rotation: Fraction = Fraction(0)

    def __post_init__(self):
        if type(self.ordinal) is not int or self.ordinal < 0:
            raise ValueError('NONNEGATIVE_ORDINAL_REQUIRED')
        _supported(self.interior)
        object.__setattr__(self, 'radius', _exact(self.radius, positive=True))
        object.__setattr__(self, 'turn', _exact(self.turn) % 1)
        object.__setattr__(self, 'rotation', _exact(self.rotation) % 1)
        if type(self.interior) is UnicodeGlyphGonol and self.turn != self.interior.turn:
            raise ValueError('UNICODE_SCALAR_BEARING_MISMATCH')

    @property
    def origin(self):
        return Point(((Direction(self.turn), self.radius),))

    def to_parent(self, point):
        if not isinstance(point, Point):
            raise TypeError('NATIVE_POINT_REQUIRED')
        return self.origin + point.rotated(Direction(self.rotation))

    def to_local(self, point):
        if not isinstance(point, Point):
            raise TypeError('NATIVE_POINT_REQUIRED')
        return (point - self.origin).rotated(Direction(-self.rotation))

    def record(self):
        return {'ordinal': self.ordinal, 'interior': self.interior.receipt,
                'radius': _pair(self.radius), 'turn': _pair(self.turn),
                'rotation': _pair(self.rotation), 'origin': self.origin.record()}


@dataclass(frozen=True, slots=True, eq=False)
class UnicodeClosedFrame:
    """A complete declared frame which can participate in another frame."""
    participants: tuple
    bearings: tuple
    relation: str
    source: str
    radius: Fraction = Fraction(1)
    rotations: tuple | None = None
    placements: tuple = field(init=False)
    receipt: str = field(init=False)

    def __post_init__(self):
        _text(self.relation)
        _text(self.source)
        if not isinstance(self.participants, tuple) or not self.participants:
            raise ValueError('NONEMPTY_IMMUTABLE_PARTICIPANTS_REQUIRED')
        if not isinstance(self.bearings, tuple) or len(self.bearings) != len(self.participants):
            raise ValueError('ONE_EXPLICIT_BEARING_PER_PARTICIPANT_REQUIRED')
        rotations = self.rotations
        if rotations is None:
            rotations = (Fraction(0),) * len(self.participants)
        if not isinstance(rotations, tuple) or len(rotations) != len(self.participants):
            raise ValueError('ONE_ROTATION_PER_PARTICIPANT_REQUIRED')
        radius = _exact(self.radius, positive=True)
        placements = tuple(UnicodeObjectPlacement(i, child, radius, turn, rotation)
                           for i, (child, turn, rotation) in enumerate(
                               zip(self.participants, self.bearings, rotations)))
        object.__setattr__(self, 'radius', radius)
        object.__setattr__(self, 'bearings', tuple(p.turn for p in placements))
        object.__setattr__(self, 'rotations', tuple(p.rotation for p in placements))
        object.__setattr__(self, 'placements', placements)
        object.__setattr__(self, 'receipt', _digest(self.record(include_receipt=False)))

    def record(self, *, include_receipt=True):
        result = {'schema': 'ucns.unicode-closed-frame.v1',
                  'participants': [p.receipt for p in self.participants],
                  'bearings': [_pair(t) for t in self.bearings],
                  'rotations': [_pair(t) for t in self.rotations],
                  'radius': _pair(self.radius), 'relation': self.relation,
                  'source': self.source, 'placements': [p.record() for p in self.placements],
                  'next_scale_bearing': 'hmmm'}
        if include_receipt and hasattr(self, 'receipt'):
            result['receipt'] = self.receipt
        return result

    def recover(self):
        """Expand occurrences, not the deduplicated storage graph."""
        chunks, pending = [], [self]
        while pending:
            obj = pending.pop()
            if type(obj) is UnicodeClosedFrame:
                pending.extend(reversed(obj.participants))
            elif type(obj) is UnicodeScalarFrame:
                chunks.append(obj.recover())
            else:
                chunks.append(obj.character)
        return ''.join(chunks)

    @property
    def utf8(self):
        return self.recover().encode('utf-8')

    @property
    def utf32_be(self):
        return self.recover().encode('utf-32-be')


def _ordered_objects(root):
    """Identity-based visitation detects even forged cyclic objects."""
    pending, active, done = [(root, False)], set(), set()
    while pending:
        obj, ready = pending.pop()
        _supported(obj)
        key = id(obj)
        if key in done:
            continue
        if ready:
            active.remove(key)
            done.add(key)
            yield obj
        else:
            if key in active:
                raise ValueError('CYCLIC_UNICODE_OBJECT')
            active.add(key)
            pending.append((obj, True))
            if type(obj) is UnicodeClosedFrame:
                pending.extend((child, False) for child in reversed(obj.participants))


def validate_unicode(root):
    """Validate retained objects by their actual construction, never a label."""
    for obj in _ordered_objects(root):
        if type(obj) is UnicodeGlyphGonol:
            expected = UnicodeGlyphGonol(obj.character)
        elif type(obj) is UnicodeScalarFrame:
            expected = UnicodeScalarFrame(obj.text, obj.radius)
        else:
            expected = UnicodeClosedFrame(obj.participants, obj.bearings, obj.relation,
                                          obj.source, obj.radius, obj.rotations)
        if (_digest(obj.record()) != _digest(expected.record())
                or obj.receipt != expected.receipt):
            raise ValueError('UNICODE_OBJECT_RECEIPT_MISMATCH')
    return root


def close_unicode(participants, *, bearings=None, relation, source, radius=1, rotations=None):
    """Close the same object contract at every explicitly placed scale."""
    if bearings is None:
        if (not isinstance(participants, tuple) or not participants
                or any(type(p) is not UnicodeGlyphGonol for p in participants)):
            raise ValueError('CLOSED_OBJECT_BEARINGS_REQUIRED')
        bearings = tuple(p.turn for p in participants)
    return validate_unicode(UnicodeClosedFrame(participants, bearings, relation,
                                               source, radius, rotations))


def export_unicode_graph(root):
    """Self-contained graph; shared storage retains every parent occurrence."""
    validate_unicode(root)
    nodes, seen = [], set()
    for obj in _ordered_objects(root):
        if obj.receipt not in seen:
            nodes.append({'receipt': obj.receipt, 'object': obj.record(include_receipt=False)})
            seen.add(obj.receipt)
    body = {'schema': 'ucns.unicode-object-graph.v1', 'root': root.receipt,
            'root_space': [0, 1], 'nodes': nodes}
    return {**body, 'receipt': _digest(body)}


def _rational(value):
    if (not isinstance(value, list) or len(value) != 2
            or any(type(v) is not int for v in value) or value[1] <= 0):
        raise ValueError('CANONICAL_RATIONAL_REQUIRED')
    number = Fraction(*value)
    if _pair(number) != value:
        raise ValueError('CANONICAL_RATIONAL_REQUIRED')
    return number


def replay_unicode_graph(record):
    """Data-only replay, including exact producer-built geometry and interiors."""
    try:
        if (not isinstance(record, dict)
                or set(record) != {'schema', 'root', 'root_space', 'nodes', 'receipt'}
                or record['schema'] != 'ucns.unicode-object-graph.v1'
                or _rational(record['root_space']) != 0
                or not isinstance(record['nodes'], list)):
            raise ValueError('GRAPH_SHAPE_MISMATCH')
        nodes = {}
        for row in record['nodes']:
            if not isinstance(row, dict) or set(row) != {'receipt', 'object'}:
                raise ValueError('NODE_SHAPE_MISMATCH')
            data = row['object']
            schema = data['schema']
            if schema == 'ucns.unicode-gonol.v2':
                obj = UnicodeGlyphGonol(data['character'])
            elif schema == 'ucns.unicode-scalar-frame.v2':
                obj = UnicodeScalarFrame(data['text'], _rational(data['radius']))
            elif schema == 'ucns.unicode-closed-frame.v1':
                if any(not isinstance(data[k], list) for k in ('participants', 'bearings', 'rotations')):
                    raise ValueError('NODE_ARRAYS_REQUIRED')
                obj = UnicodeClosedFrame(tuple(nodes[key] for key in data['participants']),
                                          tuple(_rational(t) for t in data['bearings']),
                                          data['relation'], data['source'], _rational(data['radius']),
                                          tuple(_rational(t) for t in data['rotations']))
            else:
                raise ValueError('UNKNOWN_UNICODE_OBJECT_SCHEMA')
            if (obj.receipt != row['receipt'] or obj.receipt in nodes
                    or _digest(obj.record(include_receipt=False)) != _digest(data)):
                raise ValueError('NODE_RECEIPT_MISMATCH')
            nodes[obj.receipt] = obj
        root = nodes[record['root']]
        if _digest(export_unicode_graph(root)) != _digest(record):
            raise ValueError('GRAPH_REPLAY_MISMATCH')
        return root
    except (KeyError, TypeError, AttributeError, UnicodeError) as exc:
        raise ValueError('INVALID_UNICODE_OBJECT_GRAPH') from exc
# ratios: loc_comments=207:60 imports_exports=5:6 calls_definitions=117:22
