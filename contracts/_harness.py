# ratios: loc_comments=122:31 imports_exports=5:15 calls_definitions=65:18
"""Shared deterministic generators, fixtures, and mutants.

Mutant implementations deliberately falsify one law each; the contract
tests run the *same* property check against the mutant and assert the
check fails.  That is the [mutation-verified] rung: a mutation that
would falsify the law is caught by the law's own witness.
"""

import math
import random
from fractions import Fraction
from typing import List, Optional, Tuple

from ucns.canonical import UCNSObject, lcm, multiply

SEED = 20260710
DENOMS = [1, 2, 3, 4, 6]

# Canonical fixtures ---------------------------------------------------

E = UCNSObject(1, 1, [(Fraction(0), None)], [0])       # theta=0 origin
U1 = UCNSObject(1, 1, [(Fraction(0), None)], [1])      # face-flipped unit


def tower(depth: int, faces: Optional[List[int]] = None) -> UCNSObject:
    """Nested length-1 chain: the unit-tower family (central elements)."""
    faces = faces if faces is not None else [0] * depth
    obj: Optional[UCNSObject] = None
    for i in range(depth - 1, -1, -1):
        obj = UCNSObject(1, 1, [(Fraction(0), obj)], [faces[i]])
    assert obj is not None
    return obj


def flat(angles_and_faces: List[Tuple[int, int]]) -> UCNSObject:
    """Depth-1 object from integer half-turn angles and face bits."""
    a_plus = [(Fraction(a), None) for a, _ in angles_and_faces]
    f_plus = [f for _, f in angles_and_faces]
    return UCNSObject(24, 1, a_plus, f_plus)


# Deterministic random objects ----------------------------------------

def make_rng(salt: int = 0) -> random.Random:
    return random.Random(SEED + salt)


def rand_angle(rng: random.Random) -> Fraction:
    d = rng.choice(DENOMS)
    return Fraction(rng.randrange(0, 4 * d), d)


def rand_obj(rng: random.Random, depth: int, max_len: int = 3) -> UCNSObject:
    length = rng.randint(1, max_len)
    a_plus = []
    f_plus = []
    for _ in range(length):
        if depth <= 1 or rng.random() < 0.3:
            payload: Optional[UCNSObject] = None
        else:
            payload = rand_obj(rng, depth - 1, max_len)
        a_plus.append((rand_angle(rng), payload))
        f_plus.append(rng.randint(0, 1))
    # 24 is a multiple of every attainable n_min for DENOMS angles.
    return UCNSObject(24, 1, a_plus, f_plus)


def raw_of(obj: UCNSObject):
    """Raw (angles, payloads, faces) of a normalized object."""
    return (
        [a for a, _ in obj.A_plus],
        [p for _, p in obj.A_plus],
        list(obj.F_plus),
    )


def geo_eq(p, q, tol: float = 1e-9) -> bool:
    """Equality of GeometricPoints with circular theta tolerance."""
    if p.z != q.z or p.w != q.w:
        return False
    if abs(p.r - q.r) > tol:
        return False
    if (p.theta is None) != (q.theta is None):
        return False
    if p.theta is None:
        return True
    tau4 = 4 * math.pi
    d = abs(p.theta - q.theta) % tau4
    return min(d, tau4 - d) < tol


# Mutants --------------------------------------------------------------

def _mutant_product(A, B, angle_fn, face_fn, payload_fn):
    """Template sharing multiply's shape with one law perturbed."""
    if A is None or B is None:
        return A if B is None else B
    beta0 = B.A_plus[0][0]
    new_a, new_f = [], []
    for k in range(len(A.A_plus)):
        alpha_k, s_k = A.A_plus[k]
        f_k = A.F_plus[k]
        for j in range(len(B.A_plus)):
            beta_j, s_j = B.A_plus[j]
            f_j = B.F_plus[j]
            new_a.append((angle_fn(alpha_k, beta_j, beta0), payload_fn(s_k, s_j)))
            new_f.append(face_fn(f_k, f_j))
    # n_dec widened so mutant halves stay constructible
    return UCNSObject(lcm(A.n_dec, B.n_dec) * 4, 1, new_a, new_f)


def _merge(payload_op):
    def merge(s_k, s_j):
        if s_k is not None and s_j is not None:
            return payload_op(s_k, s_j)
        return s_k if s_k is not None else s_j
    return merge


def mutant_multiply_face_flip(A, B):
    """O2 mutant: XORs an extra 1 into every face bit."""
    return _mutant_product(
        A, B,
        lambda a, b, b0: (a + (b - b0)) % 4,
        lambda fk, fj: fk ^ fj ^ 1,
        _merge(mutant_multiply_face_flip),
    )


def mutant_multiply_mean_angle(A, B):
    """O3 mutant: combines angles by (arithmetic circular) mean, the
    exact 'collapsed theta payload' failure mode the handoff feared."""
    return _mutant_product(
        A, B,
        lambda a, b, b0: ((a + (b - b0)) / 2) % 4,
        lambda fk, fj: fk ^ fj,
        _merge(mutant_multiply_mean_angle),
    )


def mutant_multiply_sorted(A, B):
    """O4 mutant: canonically re-sorts product entries, erasing the
    ordering in which the commutator lives."""
    product = multiply(A, B)
    order = sorted(
        range(len(product.A_plus)),
        key=lambda i: (product.A_plus[i][0], product.F_plus[i]),
    )
    return UCNSObject(
        product.n_dec,
        1,
        [product.A_plus[i] for i in order],
        [product.F_plus[i] for i in order],
    )


def mutant_multiply_dedup(A, B):
    """O6 mutant: drops consecutive duplicate cells, breaking grading."""
    product = multiply(A, B)
    new_a, new_f = [], []
    for (angle, payload), face in zip(product.A_plus, product.F_plus):
        if new_a and new_a[-1][0] == angle and new_f[-1] == face:
            continue
        new_a.append((angle, payload))
        new_f.append(face)
    return UCNSObject(product.n_dec, 1, new_a, new_f)


def mutant_canonical_no_mod(angles):
    """O1 mutant canonicalizer: gauge-shifts without reducing mod 4,
    so gauge-equivalent raw representations stop colliding."""
    off = angles[0]
    return tuple(a - off for a in angles)


def canonical_gauge(angles):
    """Reference canonicalizer for raw top-level angle lists."""
    off = angles[0]
    return tuple((a - off) % 4 for a in angles)


def mutant_concat_gauge_drift(A, B):
    """O7 mutant addition: splices B in at A's trailing gauge instead of
    the shared canonical gauge, breaking right-distributivity."""
    drift = A.A_plus[-1][0]
    new_a = list(A.A_plus) + [((x + drift) % 4, p) for x, p in B.A_plus]
    new_f = list(A.F_plus) + list(B.F_plus)
    return UCNSObject(lcm(A.n_dec, B.n_dec), 1, new_a, new_f)


def concat(A: UCNSObject, B: UCNSObject) -> UCNSObject:
    """Derived candidate addition: top-level sequence concatenation."""
    new_a = list(A.A_plus) + list(B.A_plus)
    new_f = list(A.F_plus) + list(B.F_plus)
    return UCNSObject(lcm(A.n_dec, B.n_dec), 1, new_a, new_f)
# ratios: loc_comments=122:31 imports_exports=5:15 calls_definitions=65:18
