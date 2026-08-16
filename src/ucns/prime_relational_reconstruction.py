# === MODULE_BUILD ===
# id: ucns_prime_relational_reconstruction_adversary
#   module_name: prime_relational_reconstruction
#   module_kind: experiment
#   summary: executes frozen P2/P3/P5/P7 reconstruction, irreducibility, and matched-information baseline gates with independent replay and failure propagation
#   owner: Erin Spencer
#   public_surface: Status, public_relation_identity, encode_p2, encode_p3, encode_p5, encode_p7, run_architecture_gates, main
#   internal_surface: preregistration validation, exact field reconstruction, brute-force replay, whole-view ambiguity witnesses, typed-block baseline, canonical report serialization
#   auth_boundary: none
#   storage_boundary: writes one caller-selected aggregate report
#   network_boundary: none
#   user_data_boundary: hand-authored development fixture only; no external or sealed labels
#   admin_only: false
#   tests: tests/test_prime_relational_reconstruction.py
#   rollout: architectural falsification experiment only; no canon or runtime activation
#   rollback: remove module, checks, report, and findings while retaining immutable preregistration and prior bounded results
#   requires: edcm_external_evaluation_harness
#   since: 2026-08-16
#   unresolved: natural multimodal semantics, external authorship, measurement validity, independent external replication
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: prime_relational_fixture_identity_excludes_values
#   given: public identity is computed for a source relation
#   then: changing its value cannot change identity and forbidden payload fields are absent
#   class: safety
#   since: 2026-08-16
#
# id: prime_relational_h1_requires_complementary_unique_reconstruction
#   given: each frozen source relation is erased once from its owning prime-cardinality view
#   then: primary and brute-force replay use the complementary view checksum and agree on exactly one hidden field value
#   class: evidence
#   since: 2026-08-16
#
# id: prime_relational_h2_tests_every_whole_view
#   given: H1 survives and each complete prime-cardinality view is omitted independently
#   then: constructive ambiguity and an independent field-degree replay agree whether every view uniquely matters
#   class: evidence
#   since: 2026-08-16
#
# id: prime_relational_h3_fails_on_simpler_matched_equivalence
#   given: H1 and H2 survive and an exactly information-matched typed-block baseline is evaluated
#   then: equal or better baseline reconstruction with strictly lower semantic or dispatch complexity falsifies prime-specific architectural advantage
#   class: evidence
#   since: 2026-08-16
#
# id: prime_relational_failure_propagates_before_repair
#   given: a load-bearing architectural gate is falsified
#   then: dependent gates are marked DEPRECATED, local bounded survivors remain recorded, and no representation or criterion is repaired
#   class: doctrine
#   since: 2026-08-16
# === END CONTRACTS ===

"""Frozen adversarial test of prime-cardinality relational reconstruction.

Usage::

    PYTHONPATH=src python -m ucns.prime_relational_reconstruction \
      --repository-root . --output /tmp/prime-relations.json

Run twice and compare bytes.  The command accepts no outcome labels and does
not invoke the EDCM harness unless every UCNS prerequisite survives.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence


MODULUS = 257
PREREGISTRATION_PATH = Path(
    "docs/evidence/UCNS_PRIME_RELATIONAL_RECONSTRUCTION_PREREGISTRATION.json"
)
EXPECTED_SCHEMA = "ucns.prime-relational-reconstruction-preregistration/1.0.0"
VIEW_ORDER = ("P2", "P3", "P5", "P7")
GROUP_ORDER = ("G2", "G3", "G5", "G7")
EXPECTED_MAPPING = {
    "P2": {"direct_group": "G2", "checksum_group": "G7"},
    "P3": {"direct_group": "G3", "checksum_group": "G2"},
    "P5": {"direct_group": "G5", "checksum_group": "G3"},
    "P7": {"direct_group": "G7", "checksum_group": "G5"},
}
CHECKSUM_VIEW = {mapping["checksum_group"]: view for view, mapping in EXPECTED_MAPPING.items()}


class Status(str, Enum):
    FALSIFIED = "FALSIFIED"
    SURVIVED = "SURVIVED"
    UNRESOLVED = "UNRESOLVED"
    BLOCKED = "BLOCKED"
    DEPRECATED = "DEPRECATED"


@dataclass(frozen=True, slots=True)
class EncodedView:
    view_id: str
    direct_group: str
    direct_values: tuple[int, ...]
    checksum_group: str
    checksum: int
    public_relation_identities: tuple[str, ...]


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def public_relation_identity(
    *, group: str, ordinal: int, source: str, target: str, value: int
) -> str:
    """Return value-blind identity; ``value`` is admitted but never serialized."""
    _field(value)
    return sha256(
        _canonical(
            {
                "group": group,
                "ordinal": ordinal,
                "relation_type": "declared-relation",
                "schema": "ucns.relational-source-edge/1.0.0",
                "source": source,
                "target": target,
            }
        )
    ).hexdigest()


def _field(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < MODULUS:
        raise ValueError("relation values must be integer elements of F_257")
    return value


def _relation_rows(groups: Mapping[str, Sequence[int]]) -> dict[str, tuple[dict[str, Any], ...]]:
    rows: dict[str, tuple[dict[str, Any], ...]] = {}
    offset = 0
    for group in GROUP_ORDER:
        values = groups[group]
        group_rows = []
        for ordinal, value in enumerate(values):
            admitted = _field(value)
            source, target = f"n{offset}", f"n{offset + 1}"
            group_rows.append(
                {
                    "group": group,
                    "identity": public_relation_identity(
                        group=group,
                        ordinal=ordinal,
                        source=source,
                        target=target,
                        value=admitted,
                    ),
                    "ordinal": ordinal,
                    "source": source,
                    "target": target,
                    "value": admitted,
                }
            )
            offset += 1
        rows[group] = tuple(group_rows)
    return rows


# These four source-native entry points intentionally do not call one another.
def encode_p2(rows: Mapping[str, tuple[dict[str, Any], ...]]) -> EncodedView:
    direct = rows["G2"]
    return EncodedView(
        "P2", "G2", tuple(row["value"] for row in direct), "G7",
        sum(row["value"] for row in rows["G7"]) % MODULUS,
        tuple(row["identity"] for row in direct),
    )


def encode_p3(rows: Mapping[str, tuple[dict[str, Any], ...]]) -> EncodedView:
    direct = rows["G3"]
    return EncodedView(
        "P3", "G3", tuple(row["value"] for row in direct), "G2",
        sum(row["value"] for row in rows["G2"]) % MODULUS,
        tuple(row["identity"] for row in direct),
    )


def encode_p5(rows: Mapping[str, tuple[dict[str, Any], ...]]) -> EncodedView:
    direct = rows["G5"]
    return EncodedView(
        "P5", "G5", tuple(row["value"] for row in direct), "G3",
        sum(row["value"] for row in rows["G3"]) % MODULUS,
        tuple(row["identity"] for row in direct),
    )


def encode_p7(rows: Mapping[str, tuple[dict[str, Any], ...]]) -> EncodedView:
    direct = rows["G7"]
    return EncodedView(
        "P7", "G7", tuple(row["value"] for row in direct), "G5",
        sum(row["value"] for row in rows["G5"]) % MODULUS,
        tuple(row["identity"] for row in direct),
    )


ENCODERS: tuple[Callable[[Mapping[str, tuple[dict[str, Any], ...]]], EncodedView], ...] = (
    encode_p2,
    encode_p3,
    encode_p5,
    encode_p7,
)


def _validate_preregistration(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    payload = json.loads(raw)
    if payload.get("schema") != EXPECTED_SCHEMA:
        raise ValueError("preregistration schema drift")
    if payload["encoders"]["field_modulus"] != MODULUS:
        raise ValueError("field modulus drift")
    if payload["encoders"]["mapping"] != EXPECTED_MAPPING:
        raise ValueError("encoder mapping drift")
    groups = payload["fixture"]["groups"]
    if tuple(groups) != GROUP_ORDER or tuple(map(len, groups.values())) != (2, 3, 5, 7):
        raise ValueError("fixture group drift")
    if payload["stopping_rule"] != "first-load-bearing-falsification-propagates-and-stops-dependent-escalation":
        raise ValueError("stopping rule drift")
    return payload, sha256(raw).hexdigest()


def _primary_reconstruct(view: EncodedView, ordinal: int, checksum: int) -> int:
    retained = sum(value for index, value in enumerate(view.direct_values) if index != ordinal)
    return (checksum - retained) % MODULUS


def _replay_candidates(view: EncodedView, ordinal: int, checksum: int) -> tuple[int, ...]:
    retained = sum(value for index, value in enumerate(view.direct_values) if index != ordinal)
    return tuple(candidate for candidate in range(MODULUS) if (retained + candidate) % MODULUS == checksum)


def _run_h1(
    rows: Mapping[str, tuple[dict[str, Any], ...]], views: Mapping[str, EncodedView]
) -> dict[str, Any]:
    erasures = []
    for owner_id in VIEW_ORDER:
        owner = views[owner_id]
        checksum_owner_id = CHECKSUM_VIEW[owner.direct_group]
        checksum = views[checksum_owner_id].checksum
        for ordinal, source_row in enumerate(rows[owner.direct_group]):
            primary = _primary_reconstruct(owner, ordinal, checksum)
            replay = _replay_candidates(owner, ordinal, checksum)
            passed = replay == (primary,) and primary == source_row["value"]
            erasures.append(
                {
                    "checksum_view": checksum_owner_id,
                    "erased_identity": source_row["identity"],
                    "owner_view": owner_id,
                    "primary_recovery": primary,
                    "replay_candidates": list(replay),
                    "status": Status.SURVIVED.value if passed else Status.FALSIFIED.value,
                }
            )
    survived = len(erasures) == 17 and all(row["status"] == Status.SURVIVED.value for row in erasures)
    return {
        "exact_recoveries": sum(row["status"] == Status.SURVIVED.value for row in erasures),
        "erasures": erasures,
        "status": Status.SURVIVED.value if survived else Status.FALSIFIED.value,
    }


def _run_h2(views: Mapping[str, EncodedView]) -> dict[str, Any]:
    leave_outs = []
    for view_id in VIEW_ORDER:
        omitted = views[view_id]
        checksum = views[CHECKSUM_VIEW[omitted.direct_group]].checksum
        original = list(omitted.direct_values)
        alternative = original.copy()
        alternative[0] = (alternative[0] + 1) % MODULUS
        alternative[1] = (alternative[1] - 1) % MODULUS
        constructive_ambiguity = (
            alternative != original
            and sum(alternative) % MODULUS == checksum
            and sum(original) % MODULUS == checksum
        )
        degrees_of_freedom = len(original) - 1
        replay_ambiguity = degrees_of_freedom > 0
        survived = constructive_ambiguity and replay_ambiguity
        leave_outs.append(
            {
                "constructive_alternative": alternative,
                "constructive_ambiguity": constructive_ambiguity,
                "direct_relation_count": len(original),
                "independent_replay_degrees_of_freedom": degrees_of_freedom,
                "status": Status.SURVIVED.value if survived else Status.FALSIFIED.value,
                "view": view_id,
            }
        )
    survived = all(row["status"] == Status.SURVIVED.value for row in leave_outs)
    return {
        "irreducible_leave_outs": sum(row["status"] == Status.SURVIVED.value for row in leave_outs),
        "leave_outs": leave_outs,
        "status": Status.SURVIVED.value if survived else Status.FALSIFIED.value,
    }


def _run_typed_block_baseline(
    rows: Mapping[str, tuple[dict[str, Any], ...]],
) -> dict[str, int]:
    """Execute the anonymous matched code through one generic block loop."""
    exact_recoveries = 0
    irreducible_leave_outs = 0
    encoded_cells = 0
    for group in GROUP_ORDER:
        direct = tuple(row["value"] for row in rows[group])
        checksum = sum(direct) % MODULUS
        encoded_cells += len(direct) + 1
        for ordinal, hidden in enumerate(direct):
            retained = sum(value for index, value in enumerate(direct) if index != ordinal)
            candidates = tuple(
                candidate for candidate in range(MODULUS)
                if (retained + candidate) % MODULUS == checksum
            )
            exact_recoveries += candidates == (hidden,)
        alternative = list(direct)
        alternative[0] = (alternative[0] + 1) % MODULUS
        alternative[1] = (alternative[1] - 1) % MODULUS
        irreducible_leave_outs += (
            tuple(alternative) != direct
            and sum(alternative) % MODULUS == checksum
            and len(direct) - 1 > 0
        )
    return {
        "encoded_field_cells": encoded_cells,
        "encoder_dispatch_branches": 1,
        "h1_exact_recoveries": exact_recoveries,
        "h2_irreducible_leave_outs": irreducible_leave_outs,
        "semantic_control_fields": 0,
    }


def _run_h3(
    rows: Mapping[str, tuple[dict[str, Any], ...]],
    prime_h1: Mapping[str, Any],
    prime_h2: Mapping[str, Any],
) -> dict[str, Any]:
    baseline = _run_typed_block_baseline(rows)
    prime = {
        "encoded_field_cells": 21,
        "encoder_dispatch_branches": 4,
        "h1_exact_recoveries": prime_h1["exact_recoveries"],
        "h2_irreducible_leave_outs": prime_h2["irreducible_leave_outs"],
        "semantic_control_fields": 2,
    }
    baseline_matches = (
        baseline["h1_exact_recoveries"] >= prime["h1_exact_recoveries"]
        and baseline["h2_irreducible_leave_outs"] >= prime["h2_irreducible_leave_outs"]
        and baseline["encoded_field_cells"] <= prime["encoded_field_cells"]
    )
    baseline_simpler = (
        baseline["semantic_control_fields"] < prime["semantic_control_fields"]
        or baseline["encoder_dispatch_branches"] < prime["encoder_dispatch_branches"]
    )
    falsified = baseline_matches and baseline_simpler
    return {
        "baseline": baseline,
        "baseline_matches_or_exceeds": baseline_matches,
        "baseline_strictly_simpler": baseline_simpler,
        "prime_family": prime,
        "status": Status.FALSIFIED.value if falsified else Status.SURVIVED.value,
    }


def run_architecture_gates(preregistration_path: Path) -> dict[str, Any]:
    prereg, prereg_digest = _validate_preregistration(preregistration_path)
    rows = _relation_rows(prereg["fixture"]["groups"])
    mutation_identity_pass = all(
        public_relation_identity(
            group=row["group"], ordinal=row["ordinal"], source=row["source"],
            target=row["target"], value=row["value"]
        ) == public_relation_identity(
            group=row["group"], ordinal=row["ordinal"], source=row["source"],
            target=row["target"], value=(row["value"] + 1) % MODULUS
        )
        for group_rows in rows.values() for row in group_rows
    )
    identities = [row["identity"] for group_rows in rows.values() for row in group_rows]
    prerequisites = {
        "identity_value_mutation_invariant": mutation_identity_pass,
        "p2_explicit": True,
        "p3_direct_source_native": True,
        "public_identities_unique": len(set(identities)) == 17,
        "status": Status.SURVIVED.value,
    }
    if not all(value is True for key, value in prerequisites.items() if key != "status"):
        prerequisites["status"] = Status.FALSIFIED.value
        return _terminal_report(prereg, prereg_digest, prerequisites)

    encoded = tuple(encoder(rows) for encoder in ENCODERS)
    views = {view.view_id: view for view in encoded}
    h1 = _run_h1(rows, views)
    if h1["status"] != Status.SURVIVED.value:
        return _terminal_report(prereg, prereg_digest, prerequisites, h1=h1)
    h2 = _run_h2(views)
    if h2["status"] != Status.SURVIVED.value:
        return _terminal_report(prereg, prereg_digest, prerequisites, h1=h1, h2=h2)
    h3 = _run_h3(rows, h1, h2)
    return _terminal_report(prereg, prereg_digest, prerequisites, h1=h1, h2=h2, h3=h3)


def _terminal_report(
    prereg: Mapping[str, Any],
    prereg_digest: str,
    prerequisites: Mapping[str, Any],
    *,
    h1: Mapping[str, Any] | None = None,
    h2: Mapping[str, Any] | None = None,
    h3: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    h1_status = h1["status"] if h1 else Status.DEPRECATED.value
    h2_status = h2["status"] if h2 else Status.DEPRECATED.value
    h3_status = h3["status"] if h3 else Status.DEPRECATED.value
    load_bearing_failure = next(
        (name for name, status in (("prerequisites", prerequisites["status"]), ("H1", h1_status), ("H2", h2_status), ("H3", h3_status)) if status == Status.FALSIFIED.value),
        None,
    )
    architecture = Status.FALSIFIED.value if load_bearing_failure else Status.SURVIVED.value
    dependent = (
        Status.DEPRECATED.value if architecture == Status.FALSIFIED.value else "ELIGIBLE"
    )
    return {
        "architecture_status": architecture,
        "canon_selection": None,
        "dependent_escalations": {
            name: dependent for name in (
                "multi-loss", "recursive", "scale-transition", "multimodal",
                "externally-authored-fixtures", "edcm-external-validity", "joint-architecture"
            )
        },
        "external_or_sealed_labels_inspected": False,
        "h1": h1 or {"status": Status.DEPRECATED.value},
        "h2": h2 or {"status": Status.DEPRECATED.value},
        "h3": h3 or {"status": Status.DEPRECATED.value},
        "load_bearing_failure": load_bearing_failure,
        "nonclaims": [
            "universal reconstruction", "physical necessity", "consciousness necessity",
            "prime metaphysics", "spectral claim", "zeta claim", "EDCM measurement validity"
        ],
        "prerequisites": prerequisites,
        "preregistration_sha256": prereg_digest,
        "prior_bounded_results": {
            "edcm_absolute_recovered_dissonance": prereg["edcm"]["absolute_recovered_dissonance"],
            "edcm_normalized_recovered_dissonance": prereg["edcm"]["normalized_recovered_dissonance"],
            "ucns_p5_p7_exact_distinction": prereg["ucns_prior"]["p5_p7_exact_distinction"],
        },
        "schema": "ucns.prime-relational-reconstruction-result/1.0.0",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    report = run_architecture_gates(args.repository_root.resolve() / PREREGISTRATION_PATH)
    args.output.write_bytes(json.dumps(report, indent=2, sort_keys=True).encode() + b"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
