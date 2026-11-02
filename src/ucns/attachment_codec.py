# ratios: loc_comments=138:34 imports_exports=3:4 calls_definitions=87:8
# === MODULE_BUILD ===
# id: ucns_attachment_codec
#   module_name: attachment_codec
#   module_kind: adapter
#   summary: complete replayable graphs and view receipts for attachment stacks
#   owner: Erin Spencer
#   public_surface: export_graph, replay_graph, export_view, replay_view
#   internal_surface: strict exact data parsing and topological graph replay
#   auth_boundary: integrity only; receipts are not producer authentication
#   storage_boundary: caller owns persistence; this module performs no IO
#   network_boundary: none
#   user_data_boundary: caller source remains in returned records
#   admin_only: false
#   tests: tests/test_attachment_stack.py
#   rollout: new schema; old ordinal records retain their old meanings
#   rollback: remove the explicit new codec API
#   requires: ucns_attachment_stack
#   unresolved: cryptographic authentication remains external
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: attachment_complete_replay
#   given: a serialized recursive stack or view
#   then: replay reconstructs every carrier and closed interior and rejects tampering, missing root data, cycles, extra records and noncanonical exact values
# === END CONTRACTS ===
"""Safe data-only replay of complete attachment geometry.

GPT generated; context, prompt Erin Spencer.
Usage: ``copy = replay_graph(json.loads(json.dumps(export_graph(closed))))``.
No labels, carrier definitions or interiors are fetched from another service.
The root SPACE datum is retained; view transforms never change the closed
construction. Receipts authenticate no producer. Expressions are exact recipes,
not a claim that unrelated coordinate expressions have different values.
"""
from fractions import Fraction

from .ordinal_affixiation import Carrier, Participant, _digest
from .attachment_stack import Closed, Direction, Point, AttachmentJoin, stack, join, common_view, attached_view


def _shape(value, keys):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise ValueError('RECORD_SHAPE_MISMATCH')


def _rational(value):
    if (not isinstance(value, list) or len(value) != 2
            or any(type(v) is not int for v in value) or value[1] <= 0):
        raise ValueError('EXACT_CANONICAL_RATIONAL_REQUIRED')
    number = Fraction(*value)
    if [number.numerator, number.denominator] != value:
        raise ValueError('EXACT_CANONICAL_RATIONAL_REQUIRED')
    return number


def export_graph(root):
    """One deterministic topological graph, retaining repeated participation."""
    nodes, carriers, seen, todo = [], {}, set(), [(root, False)]
    while todo:
        obj, ready = todo.pop()
        if obj.receipt in seen:
            continue
        if not ready:
            todo.append((obj, True))
            children = ((obj.right, obj.left) if isinstance(obj, AttachmentJoin) else
                        tuple(p.interior for p in reversed(obj.participants) if isinstance(p, Closed)))
            todo.extend((child, False) for child in children)
            continue
        for part in (() if isinstance(obj, AttachmentJoin) else obj.participants):
            if not isinstance(part, Closed):
                c = part.carrier
                carriers[c.receipt] = {'receipt': c.receipt, 'identities': list(c.identities), 'source': c.source}
        nodes.append({'receipt': obj.receipt, 'construction': obj.record()})
        seen.add(obj.receipt)
    body = {'schema': 'ucns.attachment-graph.v1', 'root': root.receipt,
            'root_space': [0, 1], 'carriers': [carriers[k] for k in sorted(carriers)], 'nodes': nodes}
    return {**body, 'receipt': _digest(body)}


def _replay_graph(record):
    _shape(record, ('schema', 'root', 'root_space', 'carriers', 'nodes', 'receipt'))
    if record['schema'] != 'ucns.attachment-graph.v1' or _rational(record['root_space']) != 0:
        raise ValueError('GRAPH_SCHEMA_OR_ROOT_DATUM_MISMATCH')
    if not isinstance(record['carriers'], list) or not isinstance(record['nodes'], list):
        raise ValueError('GRAPH_ARRAYS_REQUIRED')
    carriers, nodes = {}, {}
    for row in record['carriers']:
        _shape(row, ('receipt', 'identities', 'source'))
        if not isinstance(row['identities'], list):
            raise ValueError('CARRIER_IDENTITIES_REQUIRED')
        c = Carrier(tuple(row['identities']), row['source'])
        if c.receipt != row['receipt'] or c.receipt in carriers:
            raise ValueError('CARRIER_RECEIPT_MISMATCH')
        carriers[c.receipt] = c
    for row in record['nodes']:
        _shape(row, ('receipt', 'construction'))
        data = row['construction']
        if isinstance(data, dict) and data.get('schema') == 'ucns.attachment-join.v1':
            _shape(data, ('schema', 'identity', 'relation', 'source', 'left', 'right', 'attachment_ordinal'))
            if data['left'] not in nodes or data['right'] not in nodes:
                raise ValueError('MISSING_CYCLIC_OR_FORWARD_INTERIOR')
            obj = join(data['identity'], nodes[data['left']], nodes[data['right']],
                       relation=data['relation'], source=data['source'])
            if (type(data['attachment_ordinal']) is not int
                    or data['attachment_ordinal'] != len(obj.left.rays) - 1
                    or obj.receipt != row['receipt'] or obj.receipt in nodes):
                raise ValueError('JOIN_RECEIPT_MISMATCH')
            nodes[obj.receipt] = obj
            continue
        _shape(data, ('schema', 'identity', 'relation', 'source', 'radius', 'participants'))
        if data['schema'] != 'ucns.attachment-stack.v1' or not isinstance(data['participants'], list):
            raise ValueError('STACK_SCHEMA_MISMATCH')
        participants = []
        for part in data['participants']:
            if not isinstance(part, dict):
                raise ValueError('PARTICIPANT_RECORD_REQUIRED')
            if part.get('kind') == 'primitive':
                _shape(part, ('kind', 'carrier', 'identity'))
                if part['carrier'] not in carriers:
                    raise ValueError('CARRIER_NOT_INCLUDED')
                participants.append(Participant.atom(carriers[part['carrier']], part['identity']))
            elif part.get('kind') == 'closed':
                _shape(part, ('kind', 'interior', 'bearing'))
                if part['interior'] not in nodes:
                    raise ValueError('MISSING_CYCLIC_OR_FORWARD_INTERIOR')
                participants.append(Closed(nodes[part['interior']], part['bearing']))
            else:
                raise ValueError('UNKNOWN_PARTICIPANT_KIND')
        obj = stack(data['identity'], tuple(participants), relation=data['relation'],
                    source=data['source'], radius=_rational(data['radius']))
        if obj.receipt != row['receipt'] or obj.receipt in nodes:
            raise ValueError('CONSTRUCTION_RECEIPT_MISMATCH')
        nodes[obj.receipt] = obj
    if record['root'] not in nodes:
        raise ValueError('ROOT_NOT_INCLUDED')
    root = nodes[record['root']]
    if _digest(export_graph(root)) != _digest(record):
        raise ValueError('GRAPH_REPLAY_MISMATCH')
    return root, nodes


def replay_graph(record):
    return _replay_graph(record)[0]


def export_view(root, *, kind='attached', space=Direction(), origin=Point()):
    """Self-contained exact view with root frame and every referenced interior."""
    if kind not in ('attached', 'common'):
        raise ValueError('UNKNOWN_VIEW')
    graph = export_graph(root)
    included = {row['receipt'] for row in graph['nodes']}
    directions = (space,) + tuple(d for d, _q in origin.terms)
    if any(child.receipt not in included for d in directions for child, _power in d.endpoints):
        raise ValueError('VIEW_REFERENCES_EXTERNAL_INTERIOR')
    rays = common_view(root, space=space)
    rows = ([ray.record() for ray in rays] if kind == 'common' else
            [{'origin': a.record(), 'point': b.record()} for a, b in attached_view(rays, origin=origin)])
    body = {'schema': 'ucns.attachment-view.v1', 'kind': kind, 'graph': graph,
            'space': space.record(), 'origin': origin.record(), 'rows': rows}
    return {**body, 'receipt': _digest(body)}


def replay_view(record):
    _shape(record, ('schema', 'kind', 'graph', 'space', 'origin', 'rows', 'receipt'))
    if record['schema'] != 'ucns.attachment-view.v1':
        raise ValueError('VIEW_SCHEMA_MISMATCH')
    root, nodes = _replay_graph(record['graph'])
    def direction(data):
        _shape(data, ('turn', 'unit_endpoints'))
        if not isinstance(data['unit_endpoints'], list):
            raise ValueError('DIRECTION_FACTORS_REQUIRED')
        factors = []
        for factor in data['unit_endpoints']:
            if (not isinstance(factor, list) or len(factor) != 2
                    or type(factor[1]) is not int or factor[0] not in nodes):
                raise ValueError('INVALID_DIRECTION_FACTOR')
            factors.append((nodes[factor[0]], factor[1]))
        return Direction(_rational(data['turn']), tuple(factors))
    space = direction(record['space'])
    if not isinstance(record['origin'], list):
        raise ValueError('ORIGIN_TERMS_REQUIRED')
    terms = []
    for term in record['origin']:
        _shape(term, ('direction', 'coefficient'))
        terms.append((direction(term['direction']), _rational(term['coefficient'])))
    origin = Point(tuple(terms))
    if _digest(export_view(root, kind=record['kind'], space=space, origin=origin)) != _digest(record):
        raise ValueError('VIEW_REPLAY_MISMATCH')
    return root, space, origin
# ratios: loc_comments=138:34 imports_exports=3:4 calls_definitions=87:8
