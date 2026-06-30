"""Deterministic angle / rotation / chirality stream derivation."""
from __future__ import annotations

from math import gcd
from typing import Iterable, Tuple

from .dependencies import require_ucns
from .entries import PrimitiveStreams


def _lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b) if a and b else max(a, b, 1)


def _align(bits: Iterable[int], length: int) -> Tuple[int, ...]:
    seq = tuple(int(b) & 1 for b in bits) or (0,)
    return tuple(seq[i % len(seq)] for i in range(length))


def derive_primitive_streams(obj) -> PrimitiveStreams:
    """Return equal-length deterministic primitive streams for a UCNS object.

    This adapter uses currently exposed UCNS fields rather than hidden traversal
    semantics: angle numerators/denominators feed angle bits, carrier step
    changes feed rotation bits, and face bits feed chirality bits.
    """
    require_ucns()
    from ucns import a0_safe

    source_hash = a0_safe.identity(obj)
    if obj is None:
        return PrimitiveStreams((0,), (0,), (0,), 1, source_hash)

    angle_bits = []
    rotation_bits = []
    chirality_bits = []
    previous = 0
    carrier = max(int(getattr(obj, "n_min", 1)), 1)
    pairs = list(getattr(obj, "A_plus", []) or [])
    faces = list(getattr(obj, "F_plus", []) or [])
    for index, (angle, _payload) in enumerate(pairs):
        angle_bits.append((int(angle.numerator) + int(angle.denominator)) & 1)
        step = int((angle % 4) * carrier) if carrier else index
        rotation_bits.append((step - previous) & 1)
        previous = step
        chirality_bits.append(int(faces[index]) & 1 if index < len(faces) else 0)

    length = 1
    for size in (len(angle_bits), len(rotation_bits), len(chirality_bits), carrier):
        length = _lcm(length, max(size, 1))
    return PrimitiveStreams(
        _align(angle_bits, length),
        _align(rotation_bits, length),
        _align(chirality_bits, length),
        length,
        source_hash,
    )
