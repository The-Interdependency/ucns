"""Python/Lean conformance fixture for the formal finite-search model.

``formal/Ucns/TheoremN.lean`` defines a staged model of
``factor_search_v08``: catalogue normalization with one unit sentinel,
split candidates ``p = 2..n`` then ``p = 1``, structural host-angle
recovery, exhaustive payload assignments, face assignments, unit-group
rejection, and exact-recomposition acceptance.

This suite re-enumerates that model's witness space LITERALLY (the
functions below are transcriptions of the Lean definitions) and checks,
on the declared fixture domain, that it accepts exactly the same valid
witnesses as the executable solver machinery. The Lean-side evaluation
of the same fixture is an undischarged obligation recorded in
``audit/obligation_ledger.md``; this test is the Python half of the
shared fixture, not a substitute for the Lean half.

Declared fixture domain: products of normalized non-unit factors of
depth <= 1 and width <= 2 with the minimal catalogue of their recursive
payloads, searched without pruning.
"""

import unittest
from fractions import Fraction
from itertools import product as iproduct

from ucns import (
    UCNSObject,
    UNIT,
    factor_search_v08,
    is_multiplicative_unit,
    multiply,
    stable_hash,
)
from ucns.host_recovery import recover_face_structures, recover_host_angles
from ucns.payload_system import (
    iter_payload_system_solutions,
    normalize_payload_catalogue,
)
from ucns.witness_matrix import build_witness_matrix

S2 = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
DEPTH1 = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])


# --- Literal transcription of the Lean model (formal/Ucns/TheoremN.lean) ---

def normalized_candidates(catalogue):
    """Lean ``normalizedCandidates``: one unit sentinel, first."""
    return [None] + list(catalogue)


def split_candidates(n):
    """Lean ``splitCandidates``: p = 2..n then p = 1, divisors only."""
    return [
        (p, n // p)
        for p in list(range(2, n + 1)) + [1]
        if p > 0 and n % p == 0
    ]


def recover_host_angles_model(P, p, q):
    """Lean ``recoverHostAngles``: structural index extraction."""
    return (
        [P.A_plus[k * q][0] for k in range(p)],
        [P.A_plus[j][0] for j in range(q)],
    )


def model_witnesses(P, catalogue):
    """Enumerate the Lean model's accepted witness space for P over C."""
    accepted = set()
    n = len(P.A_plus)
    candidates = normalized_candidates(catalogue)
    for p, q in split_candidates(n):
        a_angles, b_angles = recover_host_angles_model(P, p, q)
        for sa in iproduct(candidates, repeat=p):
            for sb in iproduct(candidates, repeat=q):
                for fa in iproduct((0, 1), repeat=p):
                    for fb in iproduct((0, 1), repeat=q):
                        a_cand = UCNSObject(
                            P.n_dec, P.n_min,
                            list(zip(a_angles, sa)), list(fa),
                        )
                        b_cand = UCNSObject(
                            P.n_dec, P.n_min,
                            list(zip(b_angles, sb)), list(fb),
                        )
                        if is_multiplicative_unit(a_cand):
                            continue
                        if is_multiplicative_unit(b_cand):
                            continue
                        if multiply(a_cand, b_cand) == P:
                            accepted.add(
                                (stable_hash(a_cand), stable_hash(b_cand))
                            )
    return accepted


def solver_witnesses(P, catalogue):
    """Enumerate the executable solver's accepted witness space.

    Same staged machinery as ``_search_exhaustive`` (unpruned), but
    collecting every accepted pair instead of returning the first.
    """
    accepted = set()
    n = len(P.A_plus)
    effective = normalize_payload_catalogue(list(catalogue))
    for p in list(range(2, n + 1)) + [1]:
        if n % p != 0:
            continue
        q = n // p
        a_angles, b_angles = recover_host_angles(P, p, q)
        face_options = recover_face_structures(P, p, q)
        if not face_options:
            continue
        payload_grid = [
            [P.A_plus[k * q + j][1] for j in range(q)] for k in range(p)
        ]
        for s_a, s_b in iter_payload_system_solutions(
            payload_grid, p, q, effective
        ):
            matrix = build_witness_matrix(s_a, s_b, payload_grid)
            if not matrix.globally_consistent():
                continue
            for a_faces, b_faces in face_options:
                a_cand = UCNSObject(
                    P.n_dec, P.n_min, list(zip(a_angles, s_a)), a_faces
                )
                b_cand = UCNSObject(
                    P.n_dec, P.n_min, list(zip(b_angles, s_b)), b_faces
                )
                if is_multiplicative_unit(a_cand):
                    continue
                if is_multiplicative_unit(b_cand):
                    continue
                if multiply(a_cand, b_cand) == P:
                    accepted.add(
                        (stable_hash(a_cand), stable_hash(b_cand))
                    )
    return accepted


def minimal_catalogue(*objs):
    """Recursive payload closure of the given objects (no unit entry)."""
    catalogue = []

    def collect(obj):
        if obj is None:
            return
        for _, payload in obj.A_plus:
            if payload is not None and payload not in catalogue:
                catalogue.append(payload)
                collect(payload)

    for obj in objs:
        collect(obj)
    return catalogue


FIXTURE_CASES = [
    ("flat-square", S2, S2),
    ("depth1-square", DEPTH1, DEPTH1),
    ("asymmetric-depth1-flat", DEPTH1, S2),
]


class TestFormalSearchModelConformance(unittest.TestCase):
    def test_model_and_solver_witness_spaces_coincide(self) -> None:
        for name, a, b in FIXTURE_CASES:
            with self.subTest(case=name):
                product_obj = multiply(a, b)
                catalogue = minimal_catalogue(a, b)
                model = model_witnesses(product_obj, catalogue)
                solver = solver_witnesses(product_obj, catalogue)
                self.assertEqual(model, solver)
                self.assertTrue(model, "fixture case accepted no witness")

    def test_true_pair_is_in_the_witness_space(self) -> None:
        for name, a, b in FIXTURE_CASES:
            with self.subTest(case=name):
                product_obj = multiply(a, b)
                catalogue = minimal_catalogue(a, b)
                model = model_witnesses(product_obj, catalogue)
                self.assertIn((stable_hash(a), stable_hash(b)), model)

    def test_public_solver_result_is_in_the_witness_space(self) -> None:
        for name, a, b in FIXTURE_CASES:
            with self.subTest(case=name):
                product_obj = multiply(a, b)
                catalogue = minimal_catalogue(a, b)
                result = factor_search_v08(
                    product_obj, catalogue=[None] + catalogue, prune=False
                )
                self.assertNotEqual(result, "SEQ-PRIME")
                found_a, found_b = result
                self.assertIn(
                    (stable_hash(found_a), stable_hash(found_b)),
                    model_witnesses(product_obj, catalogue),
                )


if __name__ == "__main__":
    unittest.main()
