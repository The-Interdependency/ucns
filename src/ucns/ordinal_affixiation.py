# === MODULE_BUILD ===
# id: ordinal_affixiation_geometry
#   module_name: ordinal_affixiation
#   module_kind: engine
#   summary: equidistant initial identities, exact carrier angles and recursive ordinal contraction
#   owner: Erin Spencer
#   public_surface: Carrier, Participant, Placement, Construction, affixiate
#   internal_surface: canonical receipts and validated exact inputs
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: caller-supplied identities and provenance remain in memory
#   admin_only: false
#   tests: tests/test_ordinal_affixiation.py
#   rollout: explicit operator-requested replacement candidate; no legacy carrier mutation
#   rollback: remove candidate import and restore prior explicitly selected profile
#   unresolved: native Mobius lift and global transport between nested local frames
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: ordinal_exact_placement
#   given: n ordered participants and their declared carrier positions
#   then: occurrence i at zero-based ordinal i has radius R/2**(n-i) and unchanged exact carrier turn
# id: ordinal_recursive_recovery
#   given: closed constructions participate in later constructions
#   then: all interiors, source identities, order and multiplicity remain recoverable
# id: ordinal_equidistant_initial_field
#   given: distinct identities on one declared carrier before angular placement
#   then: every initial pair has exact distance R without claiming that circle placement is isometric
# === END CONTRACTS ===
"""Exact local-frame ordinal affixiation, independent of language.

Usage:
    carrier = Carrier(('A', 'B'), 'example-v1')
    word = affixiate('AB', (Participant.atom(carrier, 'A'),
                           Participant.atom(carrier, 'B')),
                     origin='SPACE', relation='ordered', source='example:AB')
    assert word.placement(0).radius() == Fraction(1, 4)

A closed construction may be registered on another explicitly supplied carrier
with Participant.closed(). It is never flattened into a hash or a last-glyph
angle. Angles are exact turns; floats are optional rendering only. Every frame
is local. No implicit cross-frame translation, rotation, or Mobius lift is made.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from fractions import Fraction
from hashlib import sha256
import json
import math
from types import MappingProxyType
from typing import Mapping


def _text(value: str, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f'{name} must be nonempty text')
    if any(0xD800 <= ord(c) <= 0xDFFF for c in value):
        raise ValueError(f'{name} contains a surrogate')
    return value


def _integer(value: int, name: str, lower: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < lower:
        raise ValueError(f'{name} must be an integer >= {lower}')
    return value


def _positive(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)) or value <= 0:
        raise ValueError('radius must be a positive exact integer or Fraction')
    return Fraction(value)


def _digest(value: object) -> str:
    return sha256(json.dumps(value, ensure_ascii=False, sort_keys=True,
                             separators=(',', ':'), allow_nan=False).encode()).hexdigest()


@dataclass(frozen=True, slots=True)
class Carrier:
    """Explicit ordered angular registry; category and label semantics are external."""
    identities: tuple[str, ...]
    source: str
    _index: Mapping[str, int] = field(init=False, repr=False, compare=False, hash=False)
    receipt: str = field(init=False)

    def __post_init__(self) -> None:
        if not isinstance(self.identities, tuple) or not self.identities:
            raise ValueError('carrier identities must be a nonempty tuple')
        for identity in self.identities:
            _text(identity, 'identity')
        _text(self.source, 'carrier source')
        index = {identity: i for i, identity in enumerate(self.identities)}
        if len(index) != len(self.identities):
            raise ValueError('duplicate carrier identity')
        object.__setattr__(self, '_index', MappingProxyType(index))
        object.__setattr__(self, 'receipt', _digest(
            ['ucns.ordinal-carrier.v1', self.source, self.identities]))

    def index(self, identity: str) -> int:
        try:
            return self._index[identity]
        except (KeyError, TypeError) as exc:
            raise ValueError('identity is not admitted by this carrier') from exc

    def turn(self, identity: str) -> Fraction:
        return Fraction(self.index(identity), len(self.identities))

    def initial_distance(self, left: str, right: str, radius: int | Fraction = 1) -> Fraction:
        """Pairwise equidistant field before angular placement, not a planar claim."""
        self.index(left)
        self.index(right)
        radius = _positive(radius)
        return Fraction(0) if left == right else radius


@dataclass(frozen=True, slots=True)
class Participant:
    """One shared primitive or one closed interior bound to an exact angular carrier."""
    carrier: Carrier
    identity: str
    interior: Construction | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.carrier, Carrier):
            raise TypeError('participant requires a Carrier')
        self.carrier.index(self.identity)
        if self.interior is not None:
            if not isinstance(self.interior, Construction):
                raise TypeError('interior must already be a closed Construction')
            if self.identity != self.interior.identity:
                raise ValueError('participant identity differs from its closed interior')

    @classmethod
    def atom(cls, carrier: Carrier, identity: str) -> Participant:
        return cls(carrier, identity)

    @classmethod
    def closed(cls, carrier: Carrier, interior: Construction) -> Participant:
        if not isinstance(interior, Construction):
            raise TypeError('only a closed Construction can promote')
        return cls(carrier, interior.identity, interior)


@dataclass(frozen=True, slots=True)
class Placement:
    """Symbolic exact radius and angle; constructing it never allocates 2**depth."""
    participant: Participant
    exponent: int

    def __post_init__(self) -> None:
        if not isinstance(self.participant, Participant):
            raise TypeError('placement requires a Participant')
        _integer(self.exponent, 'halving exponent', 1)

    @property
    def turn(self) -> Fraction:
        return self.participant.carrier.turn(self.participant.identity)

    def radius(self, frame_radius: int | Fraction = 1) -> Fraction:
        """Materialize a rational only when explicitly requested; storage stays symbolic."""
        return _positive(frame_radius) / (1 << self.exponent)

    def display_xy(self) -> tuple[float, float]:
        """Lossy display only; underflow raises instead of silently becoming the origin."""
        radius = math.ldexp(1.0, -self.exponent)
        if radius == 0.0:
            raise ArithmeticError('display underflow; use exact exponent and turn')
        angle = math.tau * float(self.turn)
        return radius * math.cos(angle), radius * math.sin(angle)

    def record(self) -> dict:
        phase = self.turn
        return {'identity': self.participant.identity,
                'carrier_receipt': self.participant.carrier.receipt,
                'index': self.participant.carrier.index(self.participant.identity),
                'arity': len(self.participant.carrier.identities),
                'turn': [phase.numerator, phase.denominator],
                'radius': {'numerator': 1, 'power_of_two_denominator': self.exponent},
                'interior_receipt': (self.participant.interior.receipt
                                     if self.participant.interior is not None else None)}


@dataclass(frozen=True, slots=True)
class Construction:
    """Closed ordered local frame with constitutive interiors, not a flattened vector."""
    identity: str
    participants: tuple[Participant, ...]
    origin: str
    relation: str
    source: str
    receipt: str = field(init=False)

    def __post_init__(self) -> None:
        for name in ('identity', 'origin', 'relation', 'source'):
            _text(getattr(self, name), name)
        if not isinstance(self.participants, tuple) or not self.participants:
            raise ValueError('an empty or mutable participation list cannot close')
        for participant in self.participants:
            if not isinstance(participant, Participant):
                raise TypeError('all participants must be closed or declared primitive')
        object.__setattr__(self, 'receipt', _digest(self.record()))

    def placement(self, ordinal: int) -> Placement:
        _integer(ordinal, 'ordinal')
        if ordinal >= len(self.participants):
            raise IndexError('ordinal outside construction')
        return Placement(self.participants[ordinal], len(self.participants) - ordinal)

    def record(self) -> dict:
        return {'schema': 'ucns.ordinal-affixiation.v1', 'identity': self.identity,
                'origin': self.origin, 'relation': self.relation, 'source': self.source,
                'placements': [self.placement(i).record() for i in range(len(self.participants))]}

    def recover(self) -> tuple[str, ...]:
        """Iteratively recover primitive order and multiplicity across arbitrary depth."""
        recovered: list[str] = []
        work = list(reversed(self.participants))
        while work:
            participant = work.pop()
            if participant.interior is None:
                recovered.append(participant.identity)
            else:
                work.extend(reversed(participant.interior.participants))
        return tuple(recovered)


def affixiate(identity: str, participants: tuple[Participant, ...], *,
              origin: str, relation: str, source: str) -> Construction:
    """Close the declared ordered participation using the operator's halving law."""
    return Construction(identity, participants, origin, relation, source)
