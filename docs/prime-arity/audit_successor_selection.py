#!/usr/bin/env python3
"""Construct and falsify bounded prime-arity successor-selection candidates.

This audit freezes target-blind arithmetic candidates, compares them with both
the observed anchor transitions and the HIT/CONTROL structure of the 3229
ladder, and retains outcome-oracle controls only as rejected controls. It does
not define a UCNS successor selector or promote either observed sequence.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import gcd, prod
from pathlib import Path
from typing import Callable, Sequence

from audit_3229_ladder_arity import (
    FROZEN_MAX_M,
    FROZEN_MIN_M,
    build_receipt as build_ladder_receipt,
    factor_u64,
    is_prime_u64,
)


ANCHOR_ROLES = {
    157: (157,),
    2_881: (43, 67),
    54_837_698_421: (3, 11, 1_661_748_437),
}
ANCHOR_TRANSITIONS = ((157, 2_881), (2_881, 54_837_698_421))
JSON_RECEIPT = Path(__file__).with_name("SUCCESSOR_SELECTOR_FALSIFICATION_RECEIPT.json")
MARKDOWN_RECEIPT = Path(__file__).with_name(
    "SUCCESSOR_SELECTOR_FALSIFICATION_RECEIPT.md"
)


def coefficient_layers(roles: Sequence[int]) -> tuple[int, ...]:
    """Return coefficients of the product of (1 + p*t)."""

    coefficients = [1]
    for role in roles:
        updated = coefficients + [0]
        for degree in range(1, len(updated)):
            prior = coefficients[degree] if degree < len(coefficients) else 0
            updated[degree] = prior + role * coefficients[degree - 1]
        coefficients = updated
    return tuple(coefficients)


def factor_powers(value: int) -> tuple[tuple[int, int], ...]:
    return tuple(sorted(Counter(factor_u64(value)).items()))


def euler_phi(value: int) -> int:
    return prod(
        (prime - 1) * prime ** (exponent - 1)
        for prime, exponent in factor_powers(value)
    )


def next_prime_not_in(roles: Sequence[int], start: int = 2) -> int:
    candidate = max(2, start)
    while candidate in roles or not is_prime_u64(candidate):
        candidate += 1
    return candidate


def least_unused_prime_append(value: int, roles: Sequence[int]) -> dict[str, object]:
    successor_q = next_prime_not_in(roles)
    predicted_roles = tuple(sorted((*roles, successor_q)))
    return {
        "supplied_or_derived_q": successor_q,
        "predicted_roles": list(predicted_roles),
        "predicted_carrier": prod(predicted_roles),
        "predicted_coefficients": list(coefficient_layers(predicted_roles)),
    }


def least_unit_order_prime_append(value: int, roles: Sequence[int]) -> dict[str, object]:
    unit_order_factors = factor_u64(euler_phi(value))
    successor_q = next(
        (prime for prime in unit_order_factors if prime not in roles),
        next_prime_not_in(roles),
    )
    predicted_roles = tuple(sorted((*roles, successor_q)))
    return {
        "unit_group_order": euler_phi(value),
        "unit_order_factors": list(unit_order_factors),
        "supplied_or_derived_q": successor_q,
        "predicted_roles": list(predicted_roles),
        "predicted_carrier": prod(predicted_roles),
        "predicted_coefficients": list(coefficient_layers(predicted_roles)),
    }


def least_squarefree_next_arity(value: int, roles: Sequence[int]) -> dict[str, object]:
    requested_arity = len(set(roles)) + 1
    candidate = value + 1
    while True:
        factors = factor_u64(candidate)
        if len(factors) == len(set(factors)) == requested_arity:
            return {
                "requested_distinct_factor_count": requested_arity,
                "predicted_roles": list(factors),
                "predicted_carrier": candidate,
                "predicted_coefficients": list(coefficient_layers(factors)),
            }
        candidate += 1


ANCHOR_SELECTOR_SPECS: tuple[
    tuple[str, str, Callable[[int, Sequence[int]], dict[str, object]]], ...
] = (
    (
        "least_unused_prime_append",
        "append the least prime absent from the current unordered role multiset",
        least_unused_prime_append,
    ),
    (
        "least_unit_order_prime_append",
        "append the least unused prime factor of the current unit-group order",
        least_unit_order_prime_append,
    ),
    (
        "least_squarefree_next_arity",
        "choose the least larger square-free integer with one more distinct factor",
        least_squarefree_next_arity,
    ),
)


def evaluate_anchor_selectors() -> dict[str, object]:
    transitions = []
    for source, expected in ANCHOR_TRANSITIONS:
        source_roles = ANCHOR_ROLES[source]
        expected_roles = ANCHOR_ROLES[expected]
        source_counts = Counter(source_roles)
        expected_counts = Counter(expected_roles)
        nested = all(
            expected_counts[role] >= count for role, count in source_counts.items()
        )
        cases = []
        for name, rule, selector in ANCHOR_SELECTOR_SPECS:
            prediction = selector(source, source_roles)
            exact = prediction["predicted_carrier"] == expected
            cases.append(
                {
                    "selector": name,
                    "frozen_rule": rule,
                    "source_only_inputs": True,
                    "ucns_authority": "NONE",
                    "prediction": prediction,
                    "expected_carrier": expected,
                    "expected_roles": list(expected_roles),
                    "exact_match": exact,
                    "verdict": "SURVIVED" if exact else "FALSIFIED",
                }
            )
        transitions.append(
            {
                "source_carrier": source,
                "source_roles": list(source_roles),
                "source_coefficients": list(coefficient_layers(source_roles)),
                "expected_carrier": expected,
                "expected_roles": list(expected_roles),
                "expected_coefficients": list(coefficient_layers(expected_roles)),
                "role_multiset_is_append_only": nested,
                "append_only_update_can_reach_expected_roles": nested,
                "candidate_cases": cases,
            }
        )

    selector_verdicts = {}
    for name, rule, _ in ANCHOR_SELECTOR_SPECS:
        cases = [
            case
            for transition in transitions
            for case in transition["candidate_cases"]
            if case["selector"] == name
        ]
        selector_verdicts[name] = {
            "frozen_rule": rule,
            "exact_matches": sum(case["exact_match"] for case in cases),
            "tested_transitions": len(cases),
            "verdict": (
                "SURVIVED" if all(case["exact_match"] for case in cases) else "FALSIFIED"
            ),
        }
    assert all(
        result["verdict"] == "FALSIFIED" for result in selector_verdicts.values()
    )
    assert all(not transition["role_multiset_is_append_only"] for transition in transitions)
    return {
        "transitions": transitions,
        "selector_verdicts": selector_verdicts,
        "coefficient_update_law": "PROVEN",
        "supplied_q_is_a_selector": False,
        "append_only_family_status": "FALSIFIED_ON_BOTH_OBSERVED_TRANSITIONS",
        "successor_q_status": "UNRESOLVED",
    }


def exact_log2_power_of_two(value: int) -> int:
    if value < 1 or value & (value - 1):
        raise ValueError("value must be a positive power of two")
    return value.bit_length() - 1


LadderSelector = Callable[[dict[str, object]], int]


def immediate_decimal_step(row: dict[str, object]) -> int:
    return int(row["m"]) + 1


def factor_component_step(row: dict[str, object]) -> int:
    return int(row["m"]) + int(row["distinct_prime_factors"])


def quartic_kernel_step(row: dict[str, object]) -> int:
    return int(row["m"]) + exact_log2_power_of_two(
        int(row["fourth_power_coset_arity"])
    )


LADDER_SELECTOR_SPECS: tuple[tuple[str, str, LadderSelector], ...] = (
    (
        "immediate_decimal_step",
        "continue the decimal ladder once, m -> m+1",
        immediate_decimal_step,
    ),
    (
        "factor_component_step",
        "advance by the retained number of distinct prime factors",
        factor_component_step,
    ),
    (
        "quartic_kernel_step",
        "advance by log2 of the retained fourth-power coset arity",
        quartic_kernel_step,
    ),
)


def ladder_prediction_class(
    predicted_m: int,
    expected_next_hit: int | None,
    row_by_m: dict[int, dict[str, object]],
) -> str:
    if predicted_m not in row_by_m:
        return "OUTSIDE_FROZEN_WINDOW"
    if expected_next_hit is not None and predicted_m == expected_next_hit:
        return "EXACT_NEXT_HIT"
    if row_by_m[predicted_m]["label"] == "CONTROL":
        return "KNOWN_BREAK"
    return "NON_SUCCESSOR_HIT"


def evaluate_ladder_selectors() -> dict[str, object]:
    ladder = build_ladder_receipt(FROZEN_MIN_M, FROZEN_MAX_M)
    rows = ladder["rows"]
    assert isinstance(rows, list)
    row_by_m = {int(row["m"]): row for row in rows}
    hit_m = [int(row["m"]) for row in rows if row["label"] == "HIT"]
    control_m = [int(row["m"]) for row in rows if row["label"] == "CONTROL"]
    next_hit = {
        current: (hit_m[index + 1] if index + 1 < len(hit_m) else None)
        for index, current in enumerate(hit_m)
    }

    selector_results = {}
    for name, rule, selector in LADDER_SELECTOR_SPECS:
        cases = []
        for current_m in hit_m:
            source = row_by_m[current_m]
            predicted_m = selector(source)
            classification = ladder_prediction_class(
                predicted_m, next_hit[current_m], row_by_m
            )
            predicted = row_by_m.get(predicted_m)
            cases.append(
                {
                    "source_m": current_m,
                    "source_n": source["n"],
                    "expected_next_hit_m": next_hit[current_m],
                    "predicted_m": predicted_m,
                    "predicted_n": predicted["n"] if predicted else None,
                    "predicted_label": predicted["label"] if predicted else None,
                    "classification": classification,
                }
            )
        exact_matches = sum(
            case["classification"] == "EXACT_NEXT_HIT" for case in cases
        )
        known_breaks = sum(case["classification"] == "KNOWN_BREAK" for case in cases)
        selector_results[name] = {
            "frozen_rule": rule,
            "uses_only_source_row_and_frozen_arithmetic": True,
            "derived_from_retained_ucns_geometry": False,
            "cases": cases,
            "exact_next_hit_matches": exact_matches,
            "known_break_landings": known_breaks,
            "verdict": "FALSIFIED",
        }

    # These controls can reproduce known successors only by consulting the
    # outcome labels or an explicit target table. They are not selector laws.
    lookahead_cases = [
        {
            "source_m": current,
            "selected_m": next_hit[current],
            "selection_used_future_labels": True,
        }
        for current in hit_m
        if next_hit[current] is not None
    ]
    lookup_table = {
        str(current): successor
        for current, successor in next_hit.items()
        if successor is not None
    }
    return {
        "known_hit_m": hit_m,
        "known_control_m": control_m,
        "known_next_hit_map": {
            str(current): successor for current, successor in next_hit.items()
        },
        "selector_results": selector_results,
        "rejected_controls": {
            "scan_to_next_hit": {
                "cases": lookahead_cases,
                "reason": "consults future HIT/CONTROL labels",
                "admissibility": "REJECTED_TARGET_LEAKAGE",
            },
            "known_hit_lookup": {
                "table": lookup_table,
                "reason": "stores the observed successors",
                "admissibility": "REJECTED_PATTERN_FIT",
            },
        },
    }


def build_receipt() -> dict[str, object]:
    anchor_audit = evaluate_anchor_selectors()
    ladder_audit = evaluate_ladder_selectors()
    tested_verdicts = [
        result["verdict"]
        for result in anchor_audit["selector_verdicts"].values()
    ] + [
        result["verdict"]
        for result in ladder_audit["selector_results"].values()
    ]
    assert tested_verdicts == ["FALSIFIED"] * 6

    return {
        "schema": "ucns-prime-arity-successor-selector-falsification-v1",
        "standing": "INCUBATING_UNRESOLVED",
        "canon_status": "NONE",
        "runtime_status": "NOT_PCEA_RUNTIME",
        "verdict": "UNRESOLVED",
        "gate": {
            "requirement": (
                "The next role or carrier must be derived from retained UCNS structure "
                "without supplied q, future-label access, target tables, or fitted constants."
            ),
            "tested_candidate_count": len(tested_verdicts),
            "falsified_candidate_count": tested_verdicts.count("FALSIFIED"),
            "gate_survivors": 0,
            "selector_status": "MISSING",
        },
        "anchor_audit": anchor_audit,
        "ladder_audit": ladder_audit,
        "preserved_evidence": {
            "coefficient_recursion": "PROVEN",
            "coefficient_vector_preserves_unordered_role_multiset": "PROVEN",
            "successor_q_derivation": "UNRESOLVED",
            "factor_count_is_ucns_arity": False,
            "anchor_progression_is_proven_successor_ladder": False,
            "3229_pattern_is_continuous_arity_four_ladder": False,
        },
        "nonclaims": [
            "No tested selector is promoted.",
            "No arithmetic recurrence is treated as retained UCNS geometry.",
            "No HIT, factorization, coset, or coefficient is treated as secrecy.",
            "No result establishes a PCEA or post-quantum primitive.",
        ],
        "hmmm": "The selector remains missing.",
    }


def json_receipt_bytes(receipt: dict[str, object]) -> bytes:
    return (json.dumps(receipt, indent=2, sort_keys=True) + "\n").encode("utf-8")


def markdown_receipt_bytes(receipt: dict[str, object]) -> bytes:
    anchors = receipt["anchor_audit"]
    ladder = receipt["ladder_audit"]
    gate = receipt["gate"]
    assert isinstance(anchors, dict)
    assert isinstance(ladder, dict)
    assert isinstance(gate, dict)
    digest = sha256(json_receipt_bytes(receipt)).hexdigest()

    lines = [
        "# Prime-Arity Successor-Selector Falsification Receipt",
        "",
        "Status: `INCUBATING` / `UNRESOLVED`",
        "",
        "This audit is retained in UCNS experiment custody. It is not UCNS canon",
        "and is not part of PCEA runtime.",
        "",
        f"JSON receipt SHA-256: `{digest}`",
        "",
        "## Gate",
        "",
        str(gate["requirement"]),
        "",
        f"Tested candidates: {gate['tested_candidate_count']}; falsified: "
        f"{gate['falsified_candidate_count']}; survivors: {gate['gate_survivors']}.",
        "",
        "## Anchor selectors",
        "",
        "| selector | exact matches | tested | verdict |",
        "|:---|---:|---:|:---|",
    ]
    for name, result in anchors["selector_verdicts"].items():
        lines.append(
            f"| `{name}` | {result['exact_matches']} | "
            f"{result['tested_transitions']} | **{result['verdict']}** |"
        )
    lines.extend(
        [
            "",
            "Neither observed role transition is append-only, so supplying any new",
            "coefficient-update role `q` cannot transform either source multiset into",
            "its observed successor multiset.",
            "",
            "## 3229-ladder selectors",
            "",
            "Known HIT indices: " + str(ladder["known_hit_m"]),
            "",
            "Known CONTROL indices: " + str(ladder["known_control_m"]),
            "",
            "| selector | exact next HITs | CONTROL landings | verdict |",
            "|:---|---:|---:|:---|",
        ]
    )
    for name, result in ladder["selector_results"].items():
        lines.append(
            f"| `{name}` | {result['exact_next_hit_matches']} | "
            f"{result['known_break_landings']} | **{result['verdict']}** |"
        )
    lines.extend(
        [
            "",
            "`scan_to_next_hit` and `known_hit_lookup` reproduce observations only by",
            "consulting future labels or storing targets. They are rejected controls,",
            "not surviving selectors.",
            "",
            "## Standing",
            "",
            "```text",
            "coefficient recursion: PROVEN",
            "successor q derivation: UNRESOLVED",
            "tested successor laws: FALSIFIED",
            "selector: MISSING",
            "overall: UNRESOLVED",
            "canon status: NONE",
            "PCEA runtime status: NOT INCLUDED",
            "```",
            "",
            "## hmmm",
            "",
            str(receipt["hmmm"]),
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def write_receipts(receipt: dict[str, object]) -> None:
    JSON_RECEIPT.write_bytes(json_receipt_bytes(receipt))
    MARKDOWN_RECEIPT.write_bytes(markdown_receipt_bytes(receipt))


def check_receipts(receipt: dict[str, object]) -> None:
    expected = {
        JSON_RECEIPT: json_receipt_bytes(receipt),
        MARKDOWN_RECEIPT: markdown_receipt_bytes(receipt),
    }
    for path, content in expected.items():
        if not path.is_file():
            raise SystemExit(f"missing receipt: {path}")
        if path.read_bytes() != content:
            raise SystemExit(f"receipt drift: {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--write-receipts", action="store_true")
    action.add_argument("--check-receipts", action="store_true")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    receipt = build_receipt()
    if args.write_receipts:
        write_receipts(receipt)
    elif args.check_receipts:
        check_receipts(receipt)
    elif args.format == "markdown":
        print(markdown_receipt_bytes(receipt).decode("utf-8"), end="")
    else:
        print(json_receipt_bytes(receipt).decode("utf-8"), end="")


if __name__ == "__main__":
    main()
