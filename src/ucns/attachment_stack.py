# ratios: loc_comments=291:80 imports_exports=6:13 calls_definitions=150:49
# === MODULE_BUILD ===
# id: ucns_attachment_stack
#   module_name: attachment_stack
#   module_kind: engine
#   summary: exact expression geometry for recursive dyadic stacks and attachment views
#   owner: Erin Spencer
#   public_surface: Direction, Point, Ray, Closed, DiskStack, AttachmentJoin, stack, join, common_view, attached_view, recover_common, attach, display
#   internal_surface: canonical rational expression arithmetic and construction receipts
#   auth_boundary: none
#   storage_boundary: immutable in-memory constructions; graph codec is separate
#   network_boundary: none
#   user_data_boundary: caller supplied identities and sources stay in memory
#   admin_only: false
#   tests: tests/test_attachment_stack.py
#   rollout: explicit versioned planar construction; closed-bearing candidates require a named choice
#   rollback: select the historical ordinal profile explicitly; never rewrite old receipts
#   requires: ordinal_affixiation_geometry
#   unresolved: closed-construction bearing selection and native Mobius lift
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: attachment_stack_recurrence
#   given: ordered primitive or explicitly bound closed participants
#   then: each append halves earlier parent radii, advances their disk depths, and inherits the preceding placement heading and endpoint
# id: attachment_stack_views
#   given: common-origin or attached-origin exact expressions and their root frame
#   then: prefix sums and differences recover the same ordered local rays without glyph labels or a stored SPACE object
# id: attachment_stack_closure
#   given: closed participants including repeated interiors
#   then: parent stacking retains each occurrence and unchanged child-local geometry; no closed bearing is chosen implicitly
# id: attachment_stack_transport
#   given: an explicit attachment occurrence and incoming closed stack
#   then: rigid transport preserves incoming local radii and recoverable interiors without another halving
# id: attachment_stack_display_boundary
#   given: exact expressions outside finite floating display range
#   then: display refuses numerical collapse while exact construction remains available
# === END CONTRACTS ===
"""Recursive planar attachment, with exact constructive coordinate expressions.

GPT generated; context, prompt Erin Spencer.

Usage::

    from ucns.ordinal_affixiation import Carrier, Participant
    c = Carrier(tuple(' ABC'), 'example-v1')
    word = stack('AB', tuple(Participant.atom(c, x) for x in 'AB'),
                 relation='ordered', source='example')
    parent = stack('AB AB', (Closed(word, 'exit-heading-v1'),) * 2,
                   relation='explicit-pair', source='example')

Both closed-bearing policies are named, unselected candidates. The stack law
itself is fixed. Coordinates are exact sums of rational-length directed rays;
endpoint directions are exact normalized sums, not rounded angles. Expression
equality is NOT a complete decision procedure for geometric equality. The
optional display is lossy and never participates in construction or receipts.
No physical camera law or native Mobius/sheet transport is asserted.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
import math

from .ordinal_affixiation import Participant, _digest, _integer, _positive, _text

POLICIES = ('root-endpoint-v1', 'exit-heading-v1')


def _fraction(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError('exact integer or Fraction required')
    return Fraction(value)


def _pair(value):
    return [value.numerator, value.denominator]


@dataclass(frozen=True, slots=True, eq=False)
class Direction:
    """Unit complex expression: rational turn times normalized endpoint factors.

    Endpoint references retain actual closed constructions. Multiplication and
    inverse combine factors exactly; this does not equate unrelated expressions.
    """
    turn: Fraction = Fraction(0)
    endpoints: tuple = ()

    def __post_init__(self):
        turn = _fraction(self.turn) % 1
        if not isinstance(self.endpoints, tuple):
            raise TypeError('endpoint factors must be a tuple')
        factors = {}
        for item in self.endpoints:
            if not isinstance(item, tuple) or len(item) != 2:
                raise ValueError('invalid endpoint factor')
            interior, power = item
            if not isinstance(interior, (DiskStack, AttachmentJoin)) or type(power) is not int:
                raise TypeError('factor requires a closed construction and integer power')
            if interior.endpoint_nonzero() is not True:
                raise ValueError('ENDPOINT_DIRECTION_REQUIRES_NONZERO_PROOF')
            prior = factors.get(interior.receipt, (interior, 0))
            factors[interior.receipt] = (interior, prior[1] + power)
        object.__setattr__(self, 'turn', turn)
        object.__setattr__(self, 'endpoints', tuple(factors[k] for k in sorted(factors) if factors[k][1]))

    @property
    def key(self):
        return self.turn, tuple((obj.receipt, power) for obj, power in self.endpoints)

    def __eq__(self, other):
        return isinstance(other, Direction) and self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def compose(self, other):
        if not isinstance(other, Direction):
            raise TypeError('Direction required')
        return Direction(self.turn + other.turn, self.endpoints + other.endpoints)

    def inverse(self):
        return Direction(-self.turn, tuple((obj, -power) for obj, power in self.endpoints))

    def record(self):
        return {'turn': _pair(self.turn),
                'unit_endpoints': [[obj.receipt, power] for obj, power in self.endpoints]}


@dataclass(frozen=True, slots=True)
class Point:
    """Exact planar vector expression; origin is the empty sum, not Structural Null."""
    terms: tuple = ()

    def __post_init__(self):
        if not isinstance(self.terms, tuple):
            raise TypeError('terms must be a tuple')
        terms = {}
        for direction, coefficient in self.terms:
            if not isinstance(direction, Direction):
                raise TypeError('term direction must be a Direction')
            terms[direction] = terms.get(direction, Fraction(0)) + _fraction(coefficient)
        object.__setattr__(self, 'terms', tuple(sorted(
            ((d, q) for d, q in terms.items() if q), key=lambda term: term[0].key)))

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.terms + other.terms)

    def __sub__(self, other):
        return self + other.scaled(-1)

    def scaled(self, factor):
        factor = _fraction(factor)
        return Point(tuple((d, q * factor) for d, q in self.terms))

    def rotated(self, direction):
        return Point(tuple((d.compose(direction), q) for d, q in self.terms))

    def record(self):
        return [{'direction': d.record(), 'coefficient': _pair(q)} for d, q in self.terms]


@dataclass(frozen=True, slots=True)
class Ray:
    radius: Fraction
    heading: Direction

    def __post_init__(self):
        object.__setattr__(self, 'radius', _positive(self.radius))
        if not isinstance(self.heading, Direction):
            raise TypeError('ray heading requires a Direction')

    @property
    def vector(self):
        return Point(((self.heading, self.radius),))

    def record(self):
        return {'radius': _pair(self.radius), 'heading': self.heading.record()}


@dataclass(frozen=True, slots=True)
class Closed:
    """An atomic participant retaining its interior and explicit candidate binding."""
    interior: DiskStack | AttachmentJoin
    bearing: str

    def __post_init__(self):
        if not isinstance(self.interior, (DiskStack, AttachmentJoin)):
            raise TypeError('an already closed native construction is required')
        if self.bearing not in POLICIES:
            raise ValueError('CLOSED_BEARING_POLICY_REQUIRED')

    @property
    def direction(self):
        if self.bearing == 'exit-heading-v1':
            return self.interior.exit_heading
        # A finite dyadic stack cannot have a zero endpoint: its newest radius
        # exceeds the sum of every earlier radius, regardless of directions.
        return Direction(endpoints=((self.interior, 1),))


@dataclass(frozen=True, slots=True, eq=False)
class DiskStack:
    identity: str
    participants: tuple
    relation: str
    source: str
    radius: Fraction = Fraction(1)
    receipt: str = field(init=False)
    rays: tuple = field(init=False, repr=False)

    def __post_init__(self):
        for name in ('identity', 'relation', 'source'):
            _text(getattr(self, name), name)
        object.__setattr__(self, 'radius', _positive(self.radius))
        if not isinstance(self.participants, tuple) or not self.participants:
            raise ValueError('nonempty immutable participants required')
        heading, rays = Direction(), []
        n = len(self.participants)
        for i, part in enumerate(self.participants):
            if isinstance(part, Participant) and part.interior is None:
                direction = Direction(part.carrier.turn(part.identity))
            elif isinstance(part, Closed):
                direction = part.direction
            else:
                raise TypeError('declared primitive or explicitly bound closed stack required')
            heading = heading.compose(direction)
            rays.append(Ray(self.radius / (1 << (n - i)), heading))
        object.__setattr__(self, 'rays', tuple(rays))
        object.__setattr__(self, 'receipt', _digest(self.record()))

    @property
    def exit_heading(self):
        return self.rays[-1].heading

    @property
    def endpoint(self):
        return sum((ray.vector for ray in self.rays), Point())

    def depth(self, ordinal):
        _integer(ordinal, 'ordinal')
        if ordinal >= len(self.rays):
            raise IndexError('ordinal outside stack')
        return len(self.rays) - ordinal

    def append(self, participant, *, identity, source):
        return stack(identity, self.participants + (participant,),
                     relation=self.relation, source=source, radius=self.radius)

    def recover(self):
        """Iterative primitive recovery preserves multiplicity across nesting."""
        return _recover(self)

    def endpoint_nonzero(self):
        return True  # Strict newest-ray dominance, independently of directions.

    def record(self):
        parts = []
        for part in self.participants:
            if isinstance(part, Closed):
                parts.append({'kind': 'closed', 'interior': part.interior.receipt, 'bearing': part.bearing})
            else:
                parts.append({'kind': 'primitive', 'carrier': part.carrier.receipt, 'identity': part.identity})
        return {'schema': 'ucns.attachment-stack.v1', 'identity': self.identity,
                'relation': self.relation, 'source': self.source,
                'radius': _pair(self.radius), 'participants': parts}


def stack(identity, participants, *, relation, source, radius=Fraction(1)):
    """Close the same ordered dyadic operation at any declared consuming scale."""
    return DiskStack(identity, participants, relation, source, radius)


def _recover(root):
    result, pending = [], [root]
    while pending:
        part = pending.pop()
        if isinstance(part, DiskStack):
            pending.extend(reversed(part.participants))
        elif isinstance(part, AttachmentJoin):
            pending.extend((part.right, part.left))
        elif isinstance(part, Closed):
            pending.append(part.interior)
        else:
            result.append(part.identity)
    return tuple(result)


@dataclass(frozen=True, slots=True, eq=False)
class AttachmentJoin:
    """Closed terminal attachment retaining both components without contraction."""
    identity: str
    left: DiskStack | AttachmentJoin
    right: DiskStack | AttachmentJoin
    relation: str
    source: str
    rays: tuple = field(init=False, repr=False)
    receipt: str = field(init=False)

    def __post_init__(self):
        for name in ('identity', 'relation', 'source'):
            _text(getattr(self, name), name)
        if not all(isinstance(x, (DiskStack, AttachmentJoin)) for x in (self.left, self.right)):
            raise TypeError('closed native components required')
        object.__setattr__(self, 'rays', self.left.rays + common_view(self.right, space=self.left.exit_heading))
        object.__setattr__(self, 'receipt', _digest(self.record()))

    @property
    def exit_heading(self):
        return self.rays[-1].heading

    @property
    def endpoint(self):
        return sum((ray.vector for ray in self.rays), Point())

    def recover(self):
        return _recover(self)

    def record(self):
        return {'schema': 'ucns.attachment-join.v1', 'identity': self.identity,
                'relation': self.relation, 'source': self.source,
                'left': self.left.receipt, 'right': self.right.receipt,
                'attachment_ordinal': len(self.left.rays) - 1}

    def endpoint_nonzero(self):
        """Exact sufficient proof; unresolved algebra never becomes a unit vector.

        Pure prime-order rational directions use Phi_p=1+X+...+X**(p-1).
        Mixed/radical directions use strict triangle dominance when available.
        False means proved zero; None means this implementation cannot decide.
        """
        lengths = [ray.radius for ray in self.rays]
        if 2 * max(lengths) > sum(lengths):
            return True
        if any(ray.heading.endpoints for ray in self.rays):
            return None
        orders = {ray.heading.turn.denominator for ray in self.rays} - {1}
        if not orders:
            return True
        if len(orders) != 1:
            return None
        p = orders.pop()
        if any(p % d == 0 for d in range(2, math.isqrt(p) + 1)):
            return None
        coefficients = [Fraction(0)] * p
        for ray in self.rays:
            coefficients[int(ray.heading.turn * p)] += ray.radius
        return any(q != coefficients[-1] for q in coefficients[:-1])


def join(identity, left, right, *, relation, source):
    """Close an explicitly declared terminal join; never split domain input."""
    return AttachmentJoin(identity, left, right, relation, source)


def common_view(construction, *, space=Direction()):
    """One displayed origin; root SPACE stays explicit in the caller's view."""
    if not isinstance(construction, (DiskStack, AttachmentJoin)):
        raise TypeError('closed native construction required')
    return tuple(Ray(ray.radius, space.compose(ray.heading)) for ray in construction.rays)


def attached_view(rays, *, origin=Point()):
    """Prefix-sum transport: every row is (local origin, placed endpoint)."""
    rows, point = [], origin
    for ray in rays:
        endpoint = point + ray.vector
        rows.append((point, endpoint))
        point = endpoint
    return tuple(rows)


def recover_common(rows, *, origin=Point()):
    """Recover local rays from exact differences; no labels or reset heading."""
    rays, previous = [], origin
    for start, end in rows:
        if start != previous:
            raise ValueError('ATTACHMENT_CHAIN_MISMATCH')
        terms = (end - start).terms
        if len(terms) != 1 or terms[0][1] <= 0:
            raise ValueError('SINGLE_POSITIVE_RAY_REQUIRED')
        rays.append(Ray(terms[0][1], terms[0][0]))
        previous = end
    return tuple(rays)


def attach(left, ordinal, right):
    """Transport right at one left occurrence; returns recoverable exact rows.

    The caller retains both closed stacks and the selected occurrence. This
    transport does not independently close or parse a compound relation.
    """
    _integer(ordinal, 'ordinal')
    if ordinal >= len(left.rays):
        raise IndexError('ordinal outside construction')
    anchor = attached_view(left.rays)[ordinal][1]
    return attached_view(common_view(right, space=left.rays[ordinal].heading), origin=anchor)


def display(point):
    """Lossy complex coordinate; raises on underflow/overflow/zero normalization.

    Endpoint evaluation uses a stack to avoid Python recursion depth limits.
    Exact expressions and child references remain the authoritative result.
    """
    if not isinstance(point, Point):
        raise TypeError('Point required')
    cache, work = {}, []
    for direction, _q in point.terms:
        work.extend((child, False) for child, _power in direction.endpoints)
    def evaluate(vector):
        terms = []
        for direction, q in vector.terms:
            value = float(q)
            if value == 0 or not math.isfinite(value):
                raise ArithmeticError('DISPLAY_RANGE; use exact expressions')
            turn = float(direction.turn)
            if direction.turn and (turn == 0 or turn == 1):
                raise ArithmeticError('DISPLAY_RANGE; exact turn rounded to zero')
            angle = math.tau * turn
            factor = complex(math.cos(angle), math.sin(angle))
            for child, power in direction.endpoints:
                factor *= cache[child.receipt] ** power
            terms.append(value * factor)
        result = complex(math.fsum(v.real for v in terms), math.fsum(v.imag for v in terms))
        if not math.isfinite(result.real) or not math.isfinite(result.imag):
            raise ArithmeticError('DISPLAY_RANGE; use exact expressions')
        if terms and result == 0:
            raise ArithmeticError('DISPLAY_COLLAPSE; use exact expressions')
        return result
    while work:
        child, ready = work.pop()
        if child.receipt in cache:
            continue
        if not ready:
            work.append((child, True))
            for ray in child.rays:
                work.extend((obj, False) for obj, _power in ray.heading.endpoints if obj.receipt not in cache)
        else:
            scale = max(ray.radius for ray in child.rays)
            value = evaluate(child.endpoint.scaled(1 / scale))
            if abs(value) == 0:
                raise ArithmeticError('DISPLAY_ZERO_DIRECTION; exact endpoint is nonzero')
            cache[child.receipt] = value / abs(value)
    return evaluate(point)
# ratios: loc_comments=291:80 imports_exports=6:13 calls_definitions=150:49
