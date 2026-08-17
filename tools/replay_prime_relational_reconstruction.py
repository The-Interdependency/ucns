# === MODULE_BUILD ===
# id: prime_relational_reconstruction_independent_replay
#   module_name: replay_prime_relational_reconstruction
#   module_kind: instrument
#   summary: independently replays frozen H1/H2/H3 arithmetic and verifies that the registered baseline is structurally isomorphic before accepting propagation status
#   owner: Erin Spencer
#   public_surface: replay, command-line interface
#   internal_surface: canonical JSON loading, checksum enumeration, dimension audit, matched-baseline tuple comparison, structural-isomorphism audit
#   auth_boundary: none
#   storage_boundary: read
#   network_boundary: none
#   user_data_boundary: hand-authored development fixture and aggregate evidence only
#   admin_only: false
#   tests: tests/test_prime_relational_reconstruction.py
#   rollout: evidence replay and interpretation audit only; no candidate execution, canon, or activation effect
#   rollback: revert the interpretation audit without changing frozen preregistration or historical execution commits
#   requires: ucns_prime_relational_reconstruction_adversary
#   since: 2026-08-16
#   unresolved: genuinely non-prime-cardinality matched control, independent external implementation, and producer authentication
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: prime_relational_replay_avoids_product_import
#   given: the independent architecture replay runs
#   then: it derives H1 candidate sets, H2 dimensions, and H3 comparison from frozen JSON using only the Python standard library
#   class: evidence
#   since: 2026-08-16
#
# id: prime_relational_replay_scopes_registered_falsification
#   given: the committed aggregate report is replayed
#   then: H1/H2 counts, registered H3 falsification, baseline structural isomorphism, unresolved architectural status, and blocked propagation must all agree or replay fails closed
#   class: safety
#   since: 2026-08-17
# === END CONTRACTS ===

"""Independent replay for the prime relational reconstruction result.

Usage::

    python tools/replay_prime_relational_reconstruction.py \
      docs/evidence/UCNS_PRIME_RELATIONAL_RECONSTRUCTION_PREREGISTRATION.json \
      generated/prime-relational-reconstruction-result.json

This file deliberately does not import :mod:`ucns`.  It accepts the frozen H3
criterion as registered while independently refusing to transfer that software-
complexity result to prime-cardinality architecture when the baseline preserves
the same structural signature.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Sequence


MODULUS = 257
GROUPS = ("G2", "G3", "G5", "G7")
CHECKSUM_VIEW = {"G2": "P3", "G3": "P5", "G5": "P7", "G7": "P2"}
OWNER_VIEW = {"G2": "P2", "G3": "P3", "G5": "P5", "G7": "P7"}


def replay(preregistration: Path, report_path: Path) -> dict[str, Any]:
    prereg = json.loads(preregistration.read_text(encoding="utf-8"))
    report = json.loads(report_path.read_text(encoding="utf-8"))
    source = prereg["fixture"]["groups"]

    candidate_sets = []
    for group in GROUPS:
        values = source[group]
        checksum = sum(values) % MODULUS
        for ordinal, hidden in enumerate(values):
            retained = sum(value for index, value in enumerate(values) if index != ordinal)
            candidates = [
                value for value in range(MODULUS)
                if (retained + value) % MODULUS == checksum
            ]
            candidate_sets.append((OWNER_VIEW[group], CHECKSUM_VIEW[group], hidden, candidates))

    h1_exact = sum(candidates == [hidden] for _, _, hidden, candidates in candidate_sets)
    dimensions = {OWNER_VIEW[group]: len(source[group]) - 1 for group in GROUPS}
    h2_irreducible = sum(dimension > 0 for dimension in dimensions.values())

    prime = report["h3"]["prime_family"]
    baseline = report["h3"]["baseline"]
    matched = (
        baseline["h1_exact_recoveries"] >= prime["h1_exact_recoveries"]
        and baseline["h2_irreducible_leave_outs"] >= prime["h2_irreducible_leave_outs"]
        and baseline["encoded_field_cells"] <= prime["encoded_field_cells"]
    )
    simpler = (
        baseline["semantic_control_fields"] < prime["semantic_control_fields"]
        or baseline["encoder_dispatch_branches"] < prime["encoder_dispatch_branches"]
    )
    source_sizes = tuple(len(source[group]) for group in GROUPS)
    baseline_sizes = tuple(prereg["baseline"]["direct_block_sizes"])
    structural_checks = {
        "same_cardinality_signature": source_sizes == baseline_sizes == (2, 3, 5, 7),
        "same_encoded_field_cells": (
            baseline["encoded_field_cells"]
            == prime["encoded_field_cells"]
            == prereg["baseline"]["encoded_field_cells"]
            == 21
        ),
        "same_field_arithmetic": prereg["encoders"]["field_modulus"] == MODULUS,
        "same_relation_partition": (
            len(prereg["baseline"]["block_ids"]) == len(GROUPS)
            and baseline_sizes == source_sizes
        ),
        "same_sum_mod_field_checksum_operator": (
            prereg["baseline"]["kind"] == "typed-block-cyclic-checksum"
        ),
    }
    structurally_isomorphic = all(structural_checks.values())
    checks = {
        "architecture_unresolved": report["architecture_status"] == "UNRESOLVED",
        "deprecation_map_empty": report["failure_propagation"]["deprecation_map"] == [],
        "dependent_claims_unresolved": set(report["dependent_escalations"].values()) == {"UNRESOLVED"},
        "h1_exact_17": h1_exact == report["h1"]["exact_recoveries"] == 17,
        "h2_irreducible_4": h2_irreducible == report["h2"]["irreducible_leave_outs"] == 4,
        "h3_registered_software_advantage_falsified": (
            matched
            and simpler
            and report["h3"]["status"] == "FALSIFIED"
            and report["registered_program_status"] == "FALSIFIED"
        ),
        "load_bearing_failure_h3": report["load_bearing_failure"] == "H3",
        "propagation_blocked": report["failure_propagation"]["status"] == "BLOCKED",
        "structural_isomorphism": (
            structurally_isomorphic
            and report["h3"]["structural_audit"]["checks"] == structural_checks
            and report["h3"]["structural_audit"]["baseline_architecture_relation"]
            == "STRUCTURALLY_ISOMORPHIC"
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"independent replay disagreement: {checks}")
    return {"checks": checks, "h1_exact_recoveries": h1_exact, "h2_dimensions": dimensions, "status": "AGREED"}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("preregistration", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args(argv)
    print(json.dumps(replay(args.preregistration, args.report), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
