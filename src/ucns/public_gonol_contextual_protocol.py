# === MODULE_BUILD ===
# id: ucns_public_gonol_contextual_protocol
#   module_name: public_gonol_contextual_protocol
#   module_kind: experiment
#   summary: freezes the source-bound structural evaluation protocol for the Public Gonol definition-derived contextual function table under current resource-run doctrine before results are generated
#   owner: Erin Spencer
#   public_surface: PublicGonolContextualProtocol, PUBLIC_GONOL_CONTEXTUAL_PROTOCOL, contextual_protocol_bytes
#   internal_surface: _canonical_bytes, _identity
#   auth_boundary: none
#   storage_boundary: immutable canonical protocol receipt only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol_contextual_protocol
#   rollout: resource-run repair protocol superseding the historical 420-second blocked protocol before replacement execution
#   rollback: remove protocol and derived receipt without changing the function table or source definition layer
#   requires: ucns_public_gonol_function_table
#   since: 2026-08-18
#   unresolved: externally authorized usefulness outcome, context-selection authority, empirical semantic efficacy
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: public_gonol_contextual_protocol_freezes_all_evaluation_choices
#   given: the contextual-function structural evaluation is prepared
#   then: exact source receipts, anchor selection, target indices, contexts, baseline, metrics, thresholds, resource-run doctrine, natural terminal stopping rule, and outcome propagation are immutable before execution
#   class: safety
#   since: 2026-08-18
#
# id: public_gonol_contextual_protocol_does_not_smuggle_efficacy
#   given: the protocol is frozen
#   then: its only positive conclusion is bounded structural index/context distinction relative to identity-only control; semantic usefulness, parsing, and grammar remain excluded
#   class: doctrine
#   since: 2026-08-18
#
# id: public_gonol_contextual_protocol_receipt_replays_exactly
#   given: the preregistration is serialized
#   then: exact canonical bytes and identity reproduce without evaluation output fields or mutable outcome labels
#   class: evidence
#   since: 2026-08-18
# === END CONTRACTS ===

"""Frozen pre-evaluation protocol for Public Gonol contextual structure.

Usage:
    python -m ucns.public_gonol_contextual_protocol OUTPUT

The command writes the outcome-free protocol receipt only.  It does not read
OEWN source data and cannot produce a contextual evaluation result.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from typing import Iterable

from .public_gonol_functions import FUNCTIONAL_INDEX_NAMES

PROTOCOL_SCHEMA_ID = "ucns.public-gonol-contextual-evaluation-protocol"
PROTOCOL_SCHEMA_VERSION = "1.1.0"
PARENT_MAIN_COMMIT = "564765e34651c83c26b7047d8085fd874e0b7f6d"
SUPERSEDED_PROTOCOL_ID = (
    "ucns.public-gonol-contextual-protocol:sha256:"
    "ea7f9e55b114c91781358c41b8d71a1b459ca39431f39395112d8d64d110c526"
)
SUPERSEDED_BLOCKER_ID = (
    "ucns.public-gonol-contextual-evaluation-blocker:sha256:"
    "5a74f083892fe9e95b3c314c5764e675fcd1e06e1c121ab8dcf535952725feaf"
)
RESOURCE_RUN_DOCTRINE_ID = (
    "The-Interdependency/skill-lib@"
    "e284d02e7d4bedbbcf8481426a389b1d5e39551b:RESOURCE_RUN_INVARIANT.md"
)
PUBLIC_GONOL_FUNCTION_TABLE_RECEIPT_SHA256 = (
    "cabaa71bbae531993c2522e3e8cf30e26f37fcec030c1014f3495a5de62d9f69"
)
PUBLIC_GONOL_FUNCTION_TABLE_ID = (
    "ucns.public-gonol-function-table:sha256:"
    "05e8b6d3c14a34c409343cfee6fec7db9e507cbb179a6b97a606a1d093d1fc10"
)
OEWN_DEFINITION_LAYER_RECEIPT_SHA256 = (
    "bcfbf0c724a8507e00d1d3205f32de2cce489731ce019a2f883e90abd56f7c5c"
)
OEWN_DEFINITION_LAYER_ID = (
    "ucns.oewn-definition-layer:sha256:"
    "e9bc04c98c3663287f9fda1bf17431fb6cffc102ec347294ad02db4007f4aa57"
)
OEWN_SOURCE_RECEIPT_ID = (
    "ucns.oewn-core-receipt:sha256:"
    "3ea1f9f0d60bb0c440d7bcb6375050673c0cd03b774f87fed9e4be223bc3c973"
)
PUBLIC_GONOL_SHA256 = "55d10c84529a4d7bc7714786357e977b68d9df2ac3f73d20e229580b552c2ef5"
ANCHOR_FUNCTION_INDEX = 2
ANCHOR_BINDING_ORDINAL = 0
ANCHOR_DEFINITION_ORDINAL = 0
TARGET_INDICES = tuple(index for index, _, _ in FUNCTIONAL_INDEX_NAMES)
CONTEXTS: tuple[tuple[str, int], ...] = (
    ("empty", 0),
    ("anchor-once", 1),
    ("anchor-twice", 2),
)
IDENTITY_ONLY_CONTROL = "return-current-state-regardless-of-index-or-context"
POSITIVE_STATUS = "SURVIVED — not proved"
NEGATIVE_STATUS = "FALSIFIED"
UNRESOLVED_STATUS = "UNRESOLVED"
BLOCKED_STATUS = "BLOCKED"


class PublicGonolContextualProtocolError(ValueError):
    """Raised when evaluation-relevant preregistration is changed or incomplete."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                      separators=(",", ":")).encode("utf-8") + b"\n"


def _identity(prefix: str, value: object) -> str:
    return prefix + sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class PublicGonolContextualProtocol:
    """All non-outcome choices required before one structural evaluation run."""

    parent_main_commit: str = PARENT_MAIN_COMMIT
    table_receipt_sha256: str = PUBLIC_GONOL_FUNCTION_TABLE_RECEIPT_SHA256
    table_id: str = PUBLIC_GONOL_FUNCTION_TABLE_ID
    definition_layer_receipt_sha256: str = OEWN_DEFINITION_LAYER_RECEIPT_SHA256
    definition_layer_id: str = OEWN_DEFINITION_LAYER_ID
    oewn_source_receipt_id: str = OEWN_SOURCE_RECEIPT_ID
    public_gonol_sha256: str = PUBLIC_GONOL_SHA256
    target_indices: tuple[int, ...] = TARGET_INDICES
    anchor_function_index: int = ANCHOR_FUNCTION_INDEX
    anchor_binding_ordinal: int = ANCHOR_BINDING_ORDINAL
    anchor_definition_ordinal: int = ANCHOR_DEFINITION_ORDINAL
    contexts: tuple[tuple[str, int], ...] = CONTEXTS
    baseline: str = IDENTITY_ONLY_CONTROL
    required_target_distinct_results: int = len(TARGET_INDICES)
    required_baseline_distinct_results: int = 1
    required_context_changes_per_index: int = 2
    independent_replays: int = 2
    required_full_source_builds: int = 2
    resource_run_doctrine_id: str = RESOURCE_RUN_DOCTRINE_ID
    resource_preflight_required: bool = True
    wall_clock_stopping_rule: str = "none-natural-terminal-condition"
    memory_stopping_rule: str = "none-observe-only"
    artificial_resource_limit_applied: bool = False
    selection_effect: str = "none"
    outcome_recorded: bool = False
    standing: str = "preregistered-before-contextual-evaluation"

    def __post_init__(self) -> None:
        if self.parent_main_commit != PARENT_MAIN_COMMIT:
            raise PublicGonolContextualProtocolError("protocol parent commit is frozen")
        if (
            self.table_receipt_sha256 != PUBLIC_GONOL_FUNCTION_TABLE_RECEIPT_SHA256
            or self.table_id != PUBLIC_GONOL_FUNCTION_TABLE_ID
            or self.definition_layer_receipt_sha256 != OEWN_DEFINITION_LAYER_RECEIPT_SHA256
            or self.definition_layer_id != OEWN_DEFINITION_LAYER_ID
            or self.oewn_source_receipt_id != OEWN_SOURCE_RECEIPT_ID
            or self.public_gonol_sha256 != PUBLIC_GONOL_SHA256
        ):
            raise PublicGonolContextualProtocolError("source evidence is frozen")
        if self.target_indices != TARGET_INDICES or len(set(self.target_indices)) != len(TARGET_INDICES):
            raise PublicGonolContextualProtocolError("target indices are frozen")
        if (
            self.anchor_function_index != ANCHOR_FUNCTION_INDEX
            or self.anchor_binding_ordinal != ANCHOR_BINDING_ORDINAL
            or self.anchor_definition_ordinal != ANCHOR_DEFINITION_ORDINAL
        ):
            raise PublicGonolContextualProtocolError("anchor selection is frozen")
        if self.contexts != CONTEXTS or self.baseline != IDENTITY_ONLY_CONTROL:
            raise PublicGonolContextualProtocolError("contexts and baseline are frozen")
        if (
            self.required_target_distinct_results != len(TARGET_INDICES)
            or self.required_baseline_distinct_results != 1
            or self.required_context_changes_per_index != 2
        ):
            raise PublicGonolContextualProtocolError("acceptance thresholds are frozen")
        if self.independent_replays != 2 or self.required_full_source_builds != 2:
            raise PublicGonolContextualProtocolError("replay count is frozen")
        if (
            self.resource_run_doctrine_id != RESOURCE_RUN_DOCTRINE_ID
            or self.resource_preflight_required is not True
            or self.wall_clock_stopping_rule != "none-natural-terminal-condition"
            or self.memory_stopping_rule != "none-observe-only"
            or self.artificial_resource_limit_applied is not False
        ):
            raise PublicGonolContextualProtocolError("resource-run doctrine is frozen")
        if self.selection_effect != "none" or self.outcome_recorded:
            raise PublicGonolContextualProtocolError("protocol cannot contain outcome information")
        if self.standing != "preregistered-before-contextual-evaluation":
            raise PublicGonolContextualProtocolError("protocol standing cannot be promoted")

    def as_payload(self) -> dict[str, object]:
        return {
            "schema_id": PROTOCOL_SCHEMA_ID,
            "schema_version": PROTOCOL_SCHEMA_VERSION,
            "parent_main_commit": self.parent_main_commit,
            "supersedes": {
                "protocol_id": SUPERSEDED_PROTOCOL_ID,
                "blocker_id": SUPERSEDED_BLOCKER_ID,
                "reason": "historical protocol contained an unauthorized arbitrary runtime bound",
            },
            "sources": {
                "table_receipt_sha256": self.table_receipt_sha256,
                "table_id": self.table_id,
                "definition_layer_receipt_sha256": self.definition_layer_receipt_sha256,
                "definition_layer_id": self.definition_layer_id,
                "oewn_source_receipt_id": self.oewn_source_receipt_id,
                "public_gonol_sha256": self.public_gonol_sha256,
            },
            "target_indices": list(self.target_indices),
            "anchor": {
                "function_index": self.anchor_function_index,
                "binding_ordinal": self.anchor_binding_ordinal,
                "definition_ordinal": self.anchor_definition_ordinal,
            },
            "contexts": [list(item) for item in self.contexts],
            "baseline": self.baseline,
            "thresholds": {
                "target_distinct_results": self.required_target_distinct_results,
                "baseline_distinct_results": self.required_baseline_distinct_results,
                "context_changes_per_index": self.required_context_changes_per_index,
            },
            "resources": {
                "independent_replays": self.independent_replays,
                "required_full_source_builds": self.required_full_source_builds,
                "resource_run_doctrine_id": self.resource_run_doctrine_id,
                "resource_preflight_required": self.resource_preflight_required,
                "wall_clock_stopping_rule": self.wall_clock_stopping_rule,
                "memory_stopping_rule": self.memory_stopping_rule,
                "artificial_resource_limit_applied": self.artificial_resource_limit_applied,
            },
            "outcomes": {
                "positive": POSITIVE_STATUS,
                "negative": NEGATIVE_STATUS,
                "unresolved": UNRESOLVED_STATUS,
                "blocked": BLOCKED_STATUS,
            },
            "selection_effect": self.selection_effect,
            "outcome_recorded": self.outcome_recorded,
            "standing": self.standing,
            "nonclaims": [
                "semantic usefulness",
                "punctuation grammar",
                "parsing or precedence",
                "context-selection authority",
                "EDCM measurement validity",
                "canonical UCNS semantics",
            ],
        }

    @property
    def protocol_id(self) -> str:
        return _identity("ucns.public-gonol-contextual-protocol:sha256:", self.as_payload())


PUBLIC_GONOL_CONTEXTUAL_PROTOCOL = PublicGonolContextualProtocol()


def contextual_protocol_bytes(protocol: PublicGonolContextualProtocol = PUBLIC_GONOL_CONTEXTUAL_PROTOCOL) -> bytes:
    """Return the sole canonical pre-evaluation protocol receipt."""

    if not isinstance(protocol, PublicGonolContextualProtocol):
        raise TypeError("protocol must be a PublicGonolContextualProtocol")
    return _canonical_bytes({"protocol_id": protocol.protocol_id, **protocol.as_payload()})


def main(argv: Iterable[str] | None = None) -> int:
    """Write the preregistration receipt; no evaluator is available here."""

    arguments = tuple(argv) if argv is not None else tuple(sys.argv[1:])
    if len(arguments) != 1:
        raise SystemExit("usage: python -m ucns.public_gonol_contextual_protocol OUTPUT")
    output = Path(arguments[0])
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(contextual_protocol_bytes())
    return 0


__all__ = [
    "ANCHOR_BINDING_ORDINAL", "ANCHOR_DEFINITION_ORDINAL", "ANCHOR_FUNCTION_INDEX",
    "BLOCKED_STATUS", "CONTEXTS", "IDENTITY_ONLY_CONTROL", "NEGATIVE_STATUS",
    "POSITIVE_STATUS", "PUBLIC_GONOL_CONTEXTUAL_PROTOCOL",
    "PublicGonolContextualProtocol", "PublicGonolContextualProtocolError",
    "TARGET_INDICES", "UNRESOLVED_STATUS", "contextual_protocol_bytes",
]


if __name__ == "__main__":  # pragma: no cover - receipt-only command
    raise SystemExit(main())
