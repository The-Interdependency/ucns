# === MODULE_BUILD ===
# id: edcm_metapat_post_reset_bridge
#   module_name: bridge
#   module_kind: schema
#   summary: provides one immutable validated post-reset bridge record for the ordered-occurrence EDCM/METAPAT profile
#   owner: Erin Spencer
#   public_surface: EdcmMetapatBridgeRecord, BridgeCell, RetainedLayerDigest, InformationLossRecord, BridgeValidationError
#   internal_surface: _canonical_value, _canonical_bytes, _digest
#   auth_boundary: none
#   storage_boundary: serialized bridge bytes only
#   network_boundary: none
#   user_data_boundary: caller-supplied payloads must be deterministic JSON values
#   admin_only: false
#   tests: tests/test_profile_boundary.py
#   rollout: draft bridge only; consumers remain suspended until merge and package validation
#   rollback: remove bridge exports and module without changing current carrier foundations
#   since: 2026-07-23
#   unresolved: downstream consumer pinning and installed-wheel validation
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: post_reset_bridge_is_exact_and_fail_closed
#   given: a downstream bridge record is constructed or parsed
#   then: only the exact post-reset schema, producer epoch, profile identity, fixed false transfer fields, complete field set, and deterministic JSON values are accepted
#   class: safety
#   since: 2026-07-23
#
# id: bridge_identity_binds_order_profile_and_content
#   given: bridge cells, occurrence identities, options, retained layers, operator history, information loss, or source commit differ
#   then: stable identity differs or parsing fails because identity binds the complete ordered bridge payload
#   class: correctness
#   since: 2026-07-23
#
# id: validity_transfer_is_forbidden
#   given: any bridge record claims theorem, EDCM measurement, or METAPAT validity transfer
#   then: construction and parsing fail closed
#   class: doctrine
#   since: 2026-07-23
# === END CONTRACTS ===

"""Validated post-reset bridge records for bounded downstream profiles.

This module does not migrate archived bridge schemas and does not transfer theorem,
measurement, or semantic validity between projects.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
import re
from typing import Any, Iterable, Mapping

BRIDGE_SCHEMA_ID = "ucns.bridge.edcm-metapat-ordered-occurrence"
BRIDGE_SCHEMA_VERSION = "1.0.0"
PRODUCER_EPOCH = "ucns.post-reset.v1"
PROFILE_ID = "ucns.profile.edcm-metapat-ordered-occurrence"
PROFILE_VERSION = "1.0.0"

_SOURCE_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


class BridgeValidationError(ValueError):
    """Raised when a bridge record violates the post-reset profile contract."""


def _canonical_value(value: Any) -> Any:
    """Return a deterministic JSON value or fail closed for unsupported values."""

    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        if value != value or value in (float("inf"), float("-inf")):
            raise BridgeValidationError("non-finite floats are not bridge-serializable")
        return value
    if isinstance(value, (list, tuple)):
        return [_canonical_value(item) for item in value]
    if isinstance(value, Mapping):
        if not all(isinstance(key, str) for key in value):
            raise BridgeValidationError("bridge mapping keys must be strings")
        return {key: _canonical_value(value[key]) for key in sorted(value)}
    raise BridgeValidationError(
        f"unsupported bridge value type: {type(value).__name__}"
    )


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        _canonical_value(value),
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _digest(value: Any) -> str:
    return sha256(_canonical_bytes(value)).hexdigest()


@dataclass(frozen=True, slots=True)
class BridgeCell:
    """One ordered occurrence in the downstream bridge."""

    occurrence_id: str
    coordinate: Any = None
    payload: Any = None
    type_tag: Any = None
    shape: Any = None
    state: Any = None
    provenance: Any = None
    relation: Any = None
    support: float = 1.0

    def __post_init__(self) -> None:
        if not self.occurrence_id or not isinstance(self.occurrence_id, str):
            raise BridgeValidationError("occurrence_id must be a nonempty string")
        support = float(self.support)
        if support <= 0.0 or support != support or support in (
            float("inf"),
            float("-inf"),
        ):
            raise BridgeValidationError("bridge cells require finite positive support")
        object.__setattr__(self, "support", support)
        _canonical_value(self.as_payload())

    def as_payload(self) -> dict[str, Any]:
        return {
            "occurrence_id": self.occurrence_id,
            "coordinate": self.coordinate,
            "payload": self.payload,
            "type_tag": self.type_tag,
            "shape": self.shape,
            "state": self.state,
            "provenance": self.provenance,
            "relation": self.relation,
            "support": self.support,
        }


@dataclass(frozen=True, slots=True)
class RetainedLayerDigest:
    """Digest of evidence retained separately from scalar cell support."""

    name: str
    digest: str

    def __post_init__(self) -> None:
        if not self.name:
            raise BridgeValidationError("retained layer name must be nonempty")
        if not re.fullmatch(r"[0-9a-f]{64}", self.digest):
            raise BridgeValidationError("retained layer digest must be SHA-256 hex")


@dataclass(frozen=True, slots=True)
class InformationLossRecord:
    """Named disclosure of an explicit lossy projection."""

    operation: str
    lost: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.operation:
            raise BridgeValidationError("information-loss operation must be named")
        if not self.lost or any(not item for item in self.lost):
            raise BridgeValidationError("information-loss record must name lost fields")


@dataclass(frozen=True, slots=True)
class EdcmMetapatBridgeRecord:
    """Immutable bridge for the single ordered-occurrence downstream profile."""

    source_commit: str
    options: tuple[tuple[str, bool], ...]
    cells: tuple[BridgeCell, ...]
    retained_layers: tuple[RetainedLayerDigest, ...] = ()
    operator_history: tuple[str, ...] = ()
    information_loss: tuple[InformationLossRecord, ...] = ()
    schema_id: str = BRIDGE_SCHEMA_ID
    schema_version: str = BRIDGE_SCHEMA_VERSION
    producer_epoch: str = PRODUCER_EPOCH
    profile_id: str = PROFILE_ID
    profile_version: str = PROFILE_VERSION
    theorem_status_transfer: bool = False
    edcm_measurement_validity_transfer: bool = False
    metapat_validity_transfer: bool = False
    stable_identity: str = ""

    def __post_init__(self) -> None:
        if self.schema_id != BRIDGE_SCHEMA_ID:
            raise BridgeValidationError(
                "unsupported or archived bridge schema; automatic migration is forbidden"
            )
        if self.schema_version != BRIDGE_SCHEMA_VERSION:
            raise BridgeValidationError("unsupported bridge schema version")
        if self.producer_epoch != PRODUCER_EPOCH:
            raise BridgeValidationError("unsupported producer epoch")
        if self.profile_id != PROFILE_ID or self.profile_version != PROFILE_VERSION:
            raise BridgeValidationError("bridge profile identity mismatch")
        if not _SOURCE_COMMIT_RE.fullmatch(self.source_commit):
            raise BridgeValidationError("source_commit must be 40 lowercase hex characters")
        if any(
            (
                self.theorem_status_transfer,
                self.edcm_measurement_validity_transfer,
                self.metapat_validity_transfer,
            )
        ):
            raise BridgeValidationError("validity-transfer fields are permanently false")

        option_keys = [key for key, _ in self.options]
        if option_keys != sorted(option_keys) or len(option_keys) != len(set(option_keys)):
            raise BridgeValidationError("options must be uniquely keyed and sorted")
        if any(not isinstance(value, bool) for _, value in self.options):
            raise BridgeValidationError("profile options must be boolean")

        occurrence_ids = [cell.occurrence_id for cell in self.cells]
        if len(occurrence_ids) != len(set(occurrence_ids)):
            raise BridgeValidationError("occurrence identities must be unique")
        if any(not operation for operation in self.operator_history):
            raise BridgeValidationError("operator history entries must be nonempty")

        retained_names = [layer.name for layer in self.retained_layers]
        if len(retained_names) != len(set(retained_names)):
            raise BridgeValidationError("retained layer names must be unique")

        expected = self.compute_stable_identity()
        if self.stable_identity:
            if self.stable_identity != expected:
                raise BridgeValidationError(
                    "bridge stable identity does not match ordered record content"
                )
        else:
            object.__setattr__(self, "stable_identity", expected)

    def identity_payload(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "producer_epoch": self.producer_epoch,
            "source_commit": self.source_commit,
            "profile_id": self.profile_id,
            "profile_version": self.profile_version,
            "options": dict(self.options),
            "cells": [cell.as_payload() for cell in self.cells],
            "retained_layers": [
                {"name": layer.name, "digest": layer.digest}
                for layer in self.retained_layers
            ],
            "operator_history": list(self.operator_history),
            "information_loss": [
                {"operation": item.operation, "lost": list(item.lost)}
                for item in self.information_loss
            ],
            "theorem_status_transfer": self.theorem_status_transfer,
            "edcm_measurement_validity_transfer": (
                self.edcm_measurement_validity_transfer
            ),
            "metapat_validity_transfer": self.metapat_validity_transfer,
        }

    def compute_stable_identity(self) -> str:
        return _digest(self.identity_payload())

    def to_json_bytes(self) -> bytes:
        payload = self.identity_payload()
        payload["stable_identity"] = self.stable_identity
        return _canonical_bytes(payload)

    @classmethod
    def from_json_bytes(cls, raw: bytes | str) -> "EdcmMetapatBridgeRecord":
        try:
            text = raw.decode("utf-8") if isinstance(raw, bytes) else raw
            payload = json.loads(text)
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise BridgeValidationError("invalid bridge JSON") from exc
        if not isinstance(payload, dict):
            raise BridgeValidationError("bridge JSON root must be an object")

        required = {
            "schema_id",
            "schema_version",
            "producer_epoch",
            "source_commit",
            "profile_id",
            "profile_version",
            "options",
            "cells",
            "retained_layers",
            "operator_history",
            "information_loss",
            "theorem_status_transfer",
            "edcm_measurement_validity_transfer",
            "metapat_validity_transfer",
            "stable_identity",
        }
        if set(payload) != required:
            missing = sorted(required - set(payload))
            extra = sorted(set(payload) - required)
            raise BridgeValidationError(
                f"bridge fields mismatch; missing={missing}, extra={extra}"
            )
        if not isinstance(payload["options"], dict):
            raise BridgeValidationError("bridge options must be an object")

        cells = tuple(BridgeCell(**cell) for cell in payload["cells"])
        retained = tuple(
            RetainedLayerDigest(**item) for item in payload["retained_layers"]
        )
        losses = tuple(
            InformationLossRecord(
                operation=item["operation"], lost=tuple(item["lost"])
            )
            for item in payload["information_loss"]
        )
        return cls(
            schema_id=payload["schema_id"],
            schema_version=payload["schema_version"],
            producer_epoch=payload["producer_epoch"],
            source_commit=payload["source_commit"],
            profile_id=payload["profile_id"],
            profile_version=payload["profile_version"],
            options=tuple(sorted(payload["options"].items())),
            cells=cells,
            retained_layers=retained,
            operator_history=tuple(payload["operator_history"]),
            information_loss=losses,
            theorem_status_transfer=payload["theorem_status_transfer"],
            edcm_measurement_validity_transfer=payload[
                "edcm_measurement_validity_transfer"
            ],
            metapat_validity_transfer=payload["metapat_validity_transfer"],
            stable_identity=payload["stable_identity"],
        )


def retained_layer_digests(cells: Iterable[BridgeCell]) -> tuple[RetainedLayerDigest, ...]:
    """Digest retained evidence fields without adding them to scalar support."""

    cell_list = tuple(cells)
    layers: list[RetainedLayerDigest] = []
    for name in ("state", "provenance", "relation"):
        values = [getattr(cell, name) for cell in cell_list]
        if any(value is not None for value in values):
            layers.append(RetainedLayerDigest(name=name, digest=_digest(values)))
    return tuple(layers)


__all__ = [
    "BRIDGE_SCHEMA_ID",
    "BRIDGE_SCHEMA_VERSION",
    "PRODUCER_EPOCH",
    "PROFILE_ID",
    "PROFILE_VERSION",
    "BridgeCell",
    "BridgeValidationError",
    "EdcmMetapatBridgeRecord",
    "InformationLossRecord",
    "RetainedLayerDigest",
    "retained_layer_digests",
]
