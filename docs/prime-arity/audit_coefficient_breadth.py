#!/usr/bin/env python3
"""Replay the elementary-symmetric arity and restricted-breadth candidate.

The full polynomial is tested separately from its scalar evaluation at t=1.
This is an incubating arithmetic experiment, not a selected UCNS breadth
evaluator or successor constructor.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, permutations
import json
from math import isqrt, prod


ROLE_SETS = {
    "157": (157,),
    "2881": (43, 67),
    "54837698421": (3, 11, 1_661_748_437),
}


def is_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int) or value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def update_coefficients(coefficients: tuple[int, ...], successor: int) -> tuple[int, ...]:
    """Apply e'_j=e_j+q*e_(j-1) for a caller-supplied prime q."""

    if not coefficients or coefficients[0] != 1:
        raise ValueError("coefficient vector must begin with the empty baseline one")
    if not is_prime(successor):
        raise ValueError("supplied successor must be prime")
    return tuple(
        (coefficients[degree] if degree < len(coefficients) else 0)
        + successor * (coefficients[degree - 1] if degree > 0 else 0)
        for degree in range(len(coefficients) + 1)
    )


def coefficient_layers(roles: tuple[int, ...]) -> tuple[int, ...]:
    """Coefficients of the product of (1 + p*t), in ascending degree."""

    coefficients = [1]
    for role in roles:
        if not is_prime(role):
            raise ValueError("roles must be integer primes greater than one")
        coefficients = list(update_coefficients(tuple(coefficients), role))
    return tuple(coefficients)


def evaluated_size(roles: tuple[int, ...]) -> int:
    """C_k(1), kept exact rather than converted through logarithms."""

    return prod(1 + role for role in roles)


def exact_radius(roles: tuple[int, ...]) -> Fraction:
    size = evaluated_size(roles)
    return Fraction(size - 1, size)


def retained_record(roles: tuple[int, ...], provenance: str) -> dict[str, object]:
    """Retain the polynomial together with relations and provenance."""

    return {
        "coefficient_vector": list(coefficient_layers(roles)),
        "relations": {
            "role_semantics": "mutually-constraining roles supplied by caller",
            "layer_semantics": "e_j sums every j-role multiplicative interaction",
            "order_semantics": "coefficient vector is permutation-invariant",
        },
        "provenance": {
            "source": provenance,
            "supplied_roles": list(roles),
            "successor_discovery": "not performed",
        },
    }


def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def replay_canonical_json(data: bytes) -> object:
    """Parse canonical JSON and reject any non-byte-identical representation."""

    value = json.loads(data.decode("utf-8"))
    if canonical_json_bytes(value) != data:
        raise ValueError("record is valid JSON but not the canonical byte representation")
    return value


def main() -> None:
    layers = {name: coefficient_layers(roles) for name, roles in ROLE_SETS.items()}
    assert layers == {
        "157": (1, 157),
        "2881": (1, 110, 2_881),
        "54837698421": (
            1,
            1_661_748_451,
            23_264_478_151,
            54_837_698_421,
        ),
    }
    assert all(coefficients[-1] == int(name) for name, coefficients in layers.items())

    sizes = {name: evaluated_size(roles) for name, roles in ROLE_SETS.items()}
    assert sizes == {
        "157": 158,
        "2881": 2_992,
        "54837698421": 79_763_925_024,
    }

    radii = {name: exact_radius(roles) for name, roles in ROLE_SETS.items()}
    assert radii == {
        "157": Fraction(157, 158),
        "2881": Fraction(2_991, 2_992),
        "54837698421": Fraction(79_763_925_023, 79_763_925_024),
    }

    # The update law is exact on a genuinely nested role set, but q is an input.
    base = coefficient_layers((43, 67))
    added_role = 3
    updated = coefficient_layers((43, 67, added_role))
    replayed_update = update_coefficients(base, added_role)
    assert updated == replayed_update

    # Supplying a different q gives a different valid extension.  Nothing in
    # update_coefficients chooses between them.
    supplied_successor_controls = {
        "q=3": update_coefficients(base, 3),
        "q=5": update_coefficients(base, 5),
    }
    assert supplied_successor_controls == {
        "q=3": (1, 113, 3_211, 8_643),
        "q=5": (1, 115, 3_431, 14_405),
    }

    # Deterministic finite replay of the algebraic identity and unordered
    # multiset preservation.  The general status is PROVEN independently by
    # polynomial multiplication and unique factorization in Z[t].
    small_primes = (2, 3, 5, 7, 11)
    seen_vectors: dict[tuple[int, ...], tuple[int, ...]] = {}
    exhaustive_cases = 0
    for arity in range(5):
        for roles in combinations_with_replacement(small_primes, arity):
            coefficients = coefficient_layers(roles)
            prior = seen_vectors.setdefault(coefficients, roles)
            assert prior == roles
            for successor in small_primes:
                assert update_coefficients(coefficients, successor) == coefficient_layers(
                    roles + (successor,)
                )
            exhaustive_cases += 1
    assert exhaustive_cases == 126

    # The observed anchors are not nested role sets, so that exact update law
    # does not transform one observed anchor factorization into the next.
    role_sets = tuple(ROLE_SETS.values())
    nested_transitions = []
    for left, right in zip(role_sets, role_sets[1:]):
        left_counts = Counter(left)
        right_counts = Counter(right)
        nested_transitions.append(
            len(right) == len(left) + 1
            and all(right_counts[role] >= count for role, count in left_counts.items())
        )
    nested_transitions = tuple(nested_transitions)
    assert nested_transitions == (False, False)

    # Full coefficient layers retain the unordered role multiset but erase its
    # order.  Any order or provenance claim therefore needs separate structure.
    assert all(
        coefficient_layers(ordering) == layers["54837698421"]
        for ordering in permutations(ROLE_SETS["54837698421"])
    )

    # Matched arity-two control: different coefficient structures collapse to
    # the same C(1), breadth log(C(1)), and radius.
    collision_left = (3, 11)
    collision_right = (5, 7)
    assert coefficient_layers(collision_left) == (1, 14, 33)
    assert coefficient_layers(collision_right) == (1, 12, 35)
    assert coefficient_layers(collision_left) != coefficient_layers(collision_right)
    assert evaluated_size(collision_left) == evaluated_size(collision_right) == 48
    assert exact_radius(collision_left) == exact_radius(collision_right) == Fraction(47, 48)

    # Restricted null-faithfulness only: B_c=log(C(1)) is zero exactly when
    # C(1)=1, and positive for every nonempty positive-prime role multiset.
    # This says nothing about receipt-only, provenance-only, relational, or
    # otherwise retained UCNS objects.
    assert evaluated_size(()) == 1
    assert exact_radius(()) == 0
    assert all(exact_radius(roles) > 0 for roles in ROLE_SETS.values())
    null_faithfulness_cases = tuple(
        roles
        for arity in range(5)
        for roles in combinations_with_replacement(small_primes, arity)
    )
    assert all(
        (evaluated_size(roles) == 1) == (roles == ()) for roles in null_faithfulness_cases
    )

    # Preserve the object rather than identifying it with its lossy radius.
    retained_records = {
        name: retained_record(roles, f"observed-anchor:{name}")
        for name, roles in ROLE_SETS.items()
    }
    record_replays = {}
    for name, record in retained_records.items():
        encoded = canonical_json_bytes(record)
        replayed = replay_canonical_json(encoded)
        assert replayed == record
        assert canonical_json_bytes(replayed) == encoded
        record_replays[name] = True

    result = {
        "candidate": "C_k(t)=product_i(1+p_i*t); B_k=log(C_k(1))",
        "standing": "incubating; non-canonical",
        "retained_object": "R=(C_k(t), relations, provenance)",
        "anchors": {
            name: {
                "roles": list(ROLE_SETS[name]),
                "coefficients": list(layers[name]),
                "C_at_1": sizes[name],
                "radius": f"{radii[name].numerator}/{radii[name].denominator}",
                "retained_record": retained_records[name],
            }
            for name in ROLE_SETS
        },
        "tests": {
            "coefficient_update_law": "PROVEN",
            "full_coefficient_vector_preserves_unordered_prime_multiset": "PROVEN",
            "finite_exhaustive_replay_cases": exhaustive_cases,
            "complete_product_is_top_coefficient": "PROVEN",
            "supplied_successor_controls": {
                key: list(value) for key, value in supplied_successor_controls.items()
            },
            "update_requires_supplied_successor_q": True,
            "successor_q_discovery": "UNRESOLVED",
            "observed_role_sets_are_nested": list(nested_transitions),
            "constructs_observed_successors": False,
            "coefficient_vector_preserves_order_or_provenance": False,
            "order_and_provenance_location": "separate retained structure",
            "scalar_breadth_collision": {
                "left_roles": list(collision_left),
                "left_coefficients": list(coefficient_layers(collision_left)),
                "right_roles": list(collision_right),
                "right_coefficients": list(coefficient_layers(collision_right)),
                "shared_C_at_1": 48,
                "shared_radius": "47/48",
            },
            "C_at_1_as_injective_structure_encoding": "FALSIFIED",
            "B_c_null_faithful_on_positive_prime_role_multisets": "SURVIVED",
            "B_c_as_complete_UCNS_breadth_evaluator": "UNRESOLVED",
            "full_retained_structure_breadth": "BLOCKED",
            "retained_record_byte_identical_replay": record_replays,
            "factor_count_is_UCNS_arity": False,
            "arity_admission_rule": "factors count only when assigned mutually-constraining roles",
        },
        "verdict": "UNRESOLVED",
        "hmmm": (
            "The coefficient recursion and unordered-multiset preservation are "
            "proven. C_k(1) is not an injective structure encoding, while "
            "log(C_k(1)) survives the restricted null-faithfulness test. Whether "
            "it is complete UCNS breadth and how q is selected remain unresolved; "
            "radius may be lossy while the retained object is not."
        ),
    }
    result_bytes = canonical_json_bytes(result)
    assert replay_canonical_json(result_bytes) == result
    assert canonical_json_bytes(replay_canonical_json(result_bytes)) == result_bytes
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
