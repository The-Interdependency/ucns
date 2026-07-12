"""Versioned serialized evidence envelopes for UCNS consumers.

Usage guidance
--------------
Use :func:`bridge_record` to serialize canonical UCNS object identity and typed
domain prerequisite metadata without reconstructing or reimplementing the
algebra. Use :func:`factorization_evidence` to run the authoritative
:func:`ucns.factorization_result` path and serialize its search, coverage,
pruning, and certification evidence.

Canonical JSON and SHA-256 evidence digests are tamper-evident, not signatures
or proof of who transmitted a record. Consumers must keep UCNS status evidence
separate from their own empirical validity claims.
"""

# === MODULE_BUILD ===
# id: ucns_evidence_envelope
#   module_name: evidence_envelope
#   module_kind: schema
#   summary: versioned deterministic bridge records and factorization evidence envelopes binding UCNS stable identity, canonical serialization, typed domain status, exhaustive-search provenance, catalogue coverage, pruning policy, and negative-certification scope.
#   owner: Erin Spencer
#   public_surface: BRIDGE_RECORD_SCHEMA_ID, BRIDGE_RECORD_SCHEMA_VERSION, FACTORIZATION_EVIDENCE_SCHEMA_ID, FACTORIZATION_EVIDENCE_SCHEMA_VERSION, UCNSBridgeRecord, UCNSFactorizationEvidence, bridge_record, factorization_evidence
#   internal_surface: _canonical_bytes, _digest, _tuple_of_strings, _status_values
#   auth_boundary: none
#   storage_boundary: deterministic serialization only; no persistence
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_evidence_envelope
#   rollout: default_enabled
#   rollback: remove envelope exports while preserving object_record and factorization_result
#   requires: ucns_object_record, ucns_factorization_result, ucns_serialization, ucns_domain_status
#   since: 2026-07-12
#   unresolved: cryptographic producer authentication is not provided; evidence digests are tamper-evident content identities only
# === END MODULE_BUILD ===

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any, Iterable, Mapping, Optional

from .canonical import UCNSObject
from .factorization_result import (
    NEGATIVE_CERTIFICATION_POLICY_VERSION,
    FactorizationResultKind,
    factorization_result,
)
from .object_record import object_record
from .serialization import CANONICAL_SERIALIZATION_VERSION, stable_hash

BRIDGE_RECORD_SCHEMA_ID = "ucns.bridge-record"
BRIDGE_RECORD_SCHEMA_VERSION = "1.0.0"
FACTORIZATION_EVIDENCE_SCHEMA_ID = "ucns.factorization-evidence"
FACTORIZATION_EVIDENCE_SCHEMA_VERSION = "1.0.0"


def _canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _digest(value: Mapping[str, Any]) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _tuple_of_strings(name: str, values: Iterable[str]) -> tuple[str, ...]:
    result = tuple(values)
    for index, value in enumerate(result):
        if not isinstance(value, str) or not value:
            raise ValueError(f"{name}[{index}] must be a non-empty string")
    return result


def _status_values(metadata: Any) -> tuple[str, ...]:
    return tuple(
        status.value if hasattr(status, "value") else str(status)
        for status in metadata.statuses
    )


@dataclass(frozen=True, slots=True)
class UCNSBridgeRecord:
    """Immutable serialized identity and domain-prerequisite record."""

    object_hash: str
    canonical_json: str
    domain_label: str
    domain_statuses: tuple[str, ...]
    completeness_guaranteed: bool
    seq_prime_claim_scope: str
    depth: int
    n_min: int
    length: int
    is_unit: bool
    is_verified_domain: bool
    is_frontier: bool
    note: str
    ucns_serialization_version: str = CANONICAL_SERIALIZATION_VERSION
    schema_id: str = BRIDGE_RECORD_SCHEMA_ID
    schema_version: str = BRIDGE_RECORD_SCHEMA_VERSION
    evidence_digest: str = ""

    def __post_init__(self) -> None:
        if self.schema_id != BRIDGE_RECORD_SCHEMA_ID:
            raise ValueError(f"unsupported schema_id {self.schema_id!r}")
        if self.schema_version != BRIDGE_RECORD_SCHEMA_VERSION:
            raise ValueError(f"unsupported schema_version {self.schema_version!r}")
        if self.ucns_serialization_version != CANONICAL_SERIALIZATION_VERSION:
            raise ValueError(
                "unsupported UCNS canonical serialization version "
                f"{self.ucns_serialization_version!r}"
            )
        if len(self.object_hash) != 64 or any(
            character not in "0123456789abcdef" for character in self.object_hash
        ):
            raise ValueError("object_hash must be a lowercase hexadecimal SHA-256 digest")
        if not isinstance(self.canonical_json, str) or not self.canonical_json:
            raise ValueError("canonical_json must be non-empty")

        try:
            canonical_data = json.loads(self.canonical_json)
        except json.JSONDecodeError as exc:
            raise ValueError("canonical_json must contain valid JSON") from exc
        if not isinstance(canonical_data, dict):
            raise ValueError("canonical_json must decode to an object")
        if canonical_data.get("version") != self.ucns_serialization_version:
            raise ValueError("canonical_json version does not match record serialization version")
        observed_hash = hashlib.sha256(self.canonical_json.encode("utf-8")).hexdigest()
        if observed_hash != self.object_hash:
            raise ValueError("object_hash does not match canonical_json")

        statuses = _tuple_of_strings("domain_statuses", self.domain_statuses)
        if not statuses:
            raise ValueError("domain_statuses must not be empty")
        object.__setattr__(self, "domain_statuses", statuses)
        if self.depth < 0 or self.n_min < 1 or self.length < 0:
            raise ValueError("depth, n_min, and length must be non-negative with n_min >= 1")
        if self.is_verified_domain != self.completeness_guaranteed:
            raise ValueError("is_verified_domain must match completeness_guaranteed")

        expected = _digest(self._evidence_fields())
        if self.evidence_digest and self.evidence_digest != expected:
            raise ValueError("evidence_digest does not match bridge record contents")
        object.__setattr__(self, "evidence_digest", expected)

    def _evidence_fields(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "ucns_serialization_version": self.ucns_serialization_version,
            "object_hash": self.object_hash,
            "canonical_json": self.canonical_json,
            "domain_label": self.domain_label,
            "domain_statuses": list(self.domain_statuses),
            "completeness_guaranteed": self.completeness_guaranteed,
            "seq_prime_claim_scope": self.seq_prime_claim_scope,
            "depth": self.depth,
            "n_min": self.n_min,
            "length": self.length,
            "is_unit": self.is_unit,
            "is_verified_domain": self.is_verified_domain,
            "is_frontier": self.is_frontier,
            "note": self.note,
        }

    def to_dict(self) -> dict[str, Any]:
        data = self._evidence_fields()
        data["evidence_digest"] = self.evidence_digest
        return data

    def to_json(self) -> str:
        return _canonical_bytes(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "UCNSBridgeRecord":
        expected_fields = {
            "schema_id",
            "schema_version",
            "ucns_serialization_version",
            "object_hash",
            "canonical_json",
            "domain_label",
            "domain_statuses",
            "completeness_guaranteed",
            "seq_prime_claim_scope",
            "depth",
            "n_min",
            "length",
            "is_unit",
            "is_verified_domain",
            "is_frontier",
            "note",
            "evidence_digest",
        }
        unknown = set(data) - expected_fields
        missing = expected_fields - set(data)
        if unknown:
            raise ValueError(f"unknown bridge record fields: {sorted(unknown)!r}")
        if missing:
            raise ValueError(f"missing bridge record fields: {sorted(missing)!r}")
        return cls(
            schema_id=str(data["schema_id"]),
            schema_version=str(data["schema_version"]),
            ucns_serialization_version=str(data["ucns_serialization_version"]),
            object_hash=str(data["object_hash"]),
            canonical_json=str(data["canonical_json"]),
            domain_label=str(data["domain_label"]),
            domain_statuses=tuple(data["domain_statuses"]),
            completeness_guaranteed=bool(data["completeness_guaranteed"]),
            seq_prime_claim_scope=str(data["seq_prime_claim_scope"]),
            depth=int(data["depth"]),
            n_min=int(data["n_min"]),
            length=int(data["length"]),
            is_unit=bool(data["is_unit"]),
            is_verified_domain=bool(data["is_verified_domain"]),
            is_frontier=bool(data["is_frontier"]),
            note=str(data["note"]),
            evidence_digest=str(data["evidence_digest"]),
        )

    @classmethod
    def from_json(cls, value: str) -> "UCNSBridgeRecord":
        decoded = json.loads(value)
        if not isinstance(decoded, dict):
            raise ValueError("bridge record JSON must decode to an object")
        return cls.from_dict(decoded)


@dataclass(frozen=True, slots=True)
class UCNSFactorizationEvidence:
    """Immutable serialized output from UCNS's authoritative result policy."""

    product_hash: str
    product_domain_label: str
    product_domain_statuses: tuple[str, ...]
    completeness_guaranteed: bool
    result_kind: str
    factor_hashes: tuple[str, ...]
    negative_result_certified: bool
    seq_prime_is_absolute: bool
    claim_scope: str
    note: str
    certification_policy_version: str
    search_exhausted: bool
    truncation_occurred: bool
    catalogue_source: str
    supplied_catalogue_size: int
    supplied_catalogue_fingerprint: str
    effective_catalogue_size: int
    effective_catalogue_fingerprint: str
    catalogue_coverage_status: str
    catalogue_coverage_reason: str
    catalogue_coverage_rule_version: str
    required_catalogue_rule_version: str
    required_catalogue_fingerprint: str
    coverage_record_validated: bool
    coverage_bound_to_search_report: bool
    pruning_applied: bool
    pruning_rule: str
    pruning_rule_version: str
    pruning_preserves_coverage: bool
    uncertified_reasons: tuple[str, ...]
    schema_id: str = FACTORIZATION_EVIDENCE_SCHEMA_ID
    schema_version: str = FACTORIZATION_EVIDENCE_SCHEMA_VERSION
    evidence_digest: str = ""

    def __post_init__(self) -> None:
        if self.schema_id != FACTORIZATION_EVIDENCE_SCHEMA_ID:
            raise ValueError(f"unsupported schema_id {self.schema_id!r}")
        if self.schema_version != FACTORIZATION_EVIDENCE_SCHEMA_VERSION:
            raise ValueError(f"unsupported schema_version {self.schema_version!r}")
        if len(self.product_hash) != 64 or any(
            character not in "0123456789abcdef" for character in self.product_hash
        ):
            raise ValueError("product_hash must be a lowercase hexadecimal SHA-256 digest")
        statuses = _tuple_of_strings("product_domain_statuses", self.product_domain_statuses)
        object.__setattr__(self, "product_domain_statuses", statuses)
        factor_hashes = tuple(self.factor_hashes)
        for value in factor_hashes:
            if len(value) != 64 or any(
                character not in "0123456789abcdef" for character in value
            ):
                raise ValueError("factor_hashes must contain SHA-256 digests")
        object.__setattr__(self, "factor_hashes", factor_hashes)
        reasons = tuple(str(value) for value in self.uncertified_reasons)
        object.__setattr__(self, "uncertified_reasons", reasons)

        allowed = {kind.value for kind in FactorizationResultKind}
        if self.result_kind not in allowed:
            raise ValueError(f"unsupported result_kind {self.result_kind!r}")
        if self.result_kind == FactorizationResultKind.FACTORS.value:
            if len(self.factor_hashes) != 2:
                raise ValueError("FACTORS evidence must contain exactly two factor hashes")
            if self.negative_result_certified or self.seq_prime_is_absolute:
                raise ValueError("factor evidence cannot claim negative certification")
        else:
            if self.factor_hashes:
                raise ValueError("SEQ-PRIME evidence must not contain factor hashes")

        if self.negative_result_certified != self.seq_prime_is_absolute:
            raise ValueError(
                "negative_result_certified and seq_prime_is_absolute must agree"
            )
        if self.negative_result_certified:
            certification_requirements = {
                "complete_domain": self.completeness_guaranteed,
                "policy_version": (
                    self.certification_policy_version
                    == NEGATIVE_CERTIFICATION_POLICY_VERSION
                ),
                "search_exhausted": self.search_exhausted,
                "not_truncated": not self.truncation_occurred,
                "coverage_validated": self.coverage_record_validated,
                "coverage_bound": self.coverage_bound_to_search_report,
                "pruning_preserves_coverage": self.pruning_preserves_coverage,
                "no_uncertified_reasons": not self.uncertified_reasons,
            }
            failed = [name for name, passed in certification_requirements.items() if not passed]
            if failed:
                raise ValueError(
                    "certified negative evidence violates policy requirements: "
                    + ", ".join(failed)
                )

        for name in ("supplied_catalogue_size", "effective_catalogue_size"):
            if getattr(self, name) < 0:
                raise ValueError(f"{name} must be non-negative")

        expected = _digest(self._evidence_fields())
        if self.evidence_digest and self.evidence_digest != expected:
            raise ValueError("evidence_digest does not match factorization evidence contents")
        object.__setattr__(self, "evidence_digest", expected)

    def _evidence_fields(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "product_hash": self.product_hash,
            "product_domain_label": self.product_domain_label,
            "product_domain_statuses": list(self.product_domain_statuses),
            "completeness_guaranteed": self.completeness_guaranteed,
            "result_kind": self.result_kind,
            "factor_hashes": list(self.factor_hashes),
            "negative_result_certified": self.negative_result_certified,
            "seq_prime_is_absolute": self.seq_prime_is_absolute,
            "claim_scope": self.claim_scope,
            "note": self.note,
            "certification_policy_version": self.certification_policy_version,
            "search_exhausted": self.search_exhausted,
            "truncation_occurred": self.truncation_occurred,
            "catalogue_source": self.catalogue_source,
            "supplied_catalogue_size": self.supplied_catalogue_size,
            "supplied_catalogue_fingerprint": self.supplied_catalogue_fingerprint,
            "effective_catalogue_size": self.effective_catalogue_size,
            "effective_catalogue_fingerprint": self.effective_catalogue_fingerprint,
            "catalogue_coverage_status": self.catalogue_coverage_status,
            "catalogue_coverage_reason": self.catalogue_coverage_reason,
            "catalogue_coverage_rule_version": self.catalogue_coverage_rule_version,
            "required_catalogue_rule_version": self.required_catalogue_rule_version,
            "required_catalogue_fingerprint": self.required_catalogue_fingerprint,
            "coverage_record_validated": self.coverage_record_validated,
            "coverage_bound_to_search_report": self.coverage_bound_to_search_report,
            "pruning_applied": self.pruning_applied,
            "pruning_rule": self.pruning_rule,
            "pruning_rule_version": self.pruning_rule_version,
            "pruning_preserves_coverage": self.pruning_preserves_coverage,
            "uncertified_reasons": list(self.uncertified_reasons),
        }

    def to_dict(self) -> dict[str, Any]:
        data = self._evidence_fields()
        data["evidence_digest"] = self.evidence_digest
        return data

    def to_json(self) -> str:
        return _canonical_bytes(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "UCNSFactorizationEvidence":
        expected_fields = {
            "schema_id",
            "schema_version",
            "product_hash",
            "product_domain_label",
            "product_domain_statuses",
            "completeness_guaranteed",
            "result_kind",
            "factor_hashes",
            "negative_result_certified",
            "seq_prime_is_absolute",
            "claim_scope",
            "note",
            "certification_policy_version",
            "search_exhausted",
            "truncation_occurred",
            "catalogue_source",
            "supplied_catalogue_size",
            "supplied_catalogue_fingerprint",
            "effective_catalogue_size",
            "effective_catalogue_fingerprint",
            "catalogue_coverage_status",
            "catalogue_coverage_reason",
            "catalogue_coverage_rule_version",
            "required_catalogue_rule_version",
            "required_catalogue_fingerprint",
            "coverage_record_validated",
            "coverage_bound_to_search_report",
            "pruning_applied",
            "pruning_rule",
            "pruning_rule_version",
            "pruning_preserves_coverage",
            "uncertified_reasons",
            "evidence_digest",
        }
        unknown = set(data) - expected_fields
        missing = expected_fields - set(data)
        if unknown:
            raise ValueError(
                f"unknown factorization evidence fields: {sorted(unknown)!r}"
            )
        if missing:
            raise ValueError(
                f"missing factorization evidence fields: {sorted(missing)!r}"
            )
        return cls(
            schema_id=str(data["schema_id"]),
            schema_version=str(data["schema_version"]),
            product_hash=str(data["product_hash"]),
            product_domain_label=str(data["product_domain_label"]),
            product_domain_statuses=tuple(data["product_domain_statuses"]),
            completeness_guaranteed=bool(data["completeness_guaranteed"]),
            result_kind=str(data["result_kind"]),
            factor_hashes=tuple(data["factor_hashes"]),
            negative_result_certified=bool(data["negative_result_certified"]),
            seq_prime_is_absolute=bool(data["seq_prime_is_absolute"]),
            claim_scope=str(data["claim_scope"]),
            note=str(data["note"]),
            certification_policy_version=str(data["certification_policy_version"]),
            search_exhausted=bool(data["search_exhausted"]),
            truncation_occurred=bool(data["truncation_occurred"]),
            catalogue_source=str(data["catalogue_source"]),
            supplied_catalogue_size=int(data["supplied_catalogue_size"]),
            supplied_catalogue_fingerprint=str(data["supplied_catalogue_fingerprint"]),
            effective_catalogue_size=int(data["effective_catalogue_size"]),
            effective_catalogue_fingerprint=str(data["effective_catalogue_fingerprint"]),
            catalogue_coverage_status=str(data["catalogue_coverage_status"]),
            catalogue_coverage_reason=str(data["catalogue_coverage_reason"]),
            catalogue_coverage_rule_version=str(data["catalogue_coverage_rule_version"]),
            required_catalogue_rule_version=str(data["required_catalogue_rule_version"]),
            required_catalogue_fingerprint=str(data["required_catalogue_fingerprint"]),
            coverage_record_validated=bool(data["coverage_record_validated"]),
            coverage_bound_to_search_report=bool(data["coverage_bound_to_search_report"]),
            pruning_applied=bool(data["pruning_applied"]),
            pruning_rule=str(data["pruning_rule"]),
            pruning_rule_version=str(data["pruning_rule_version"]),
            pruning_preserves_coverage=bool(data["pruning_preserves_coverage"]),
            uncertified_reasons=tuple(data["uncertified_reasons"]),
            evidence_digest=str(data["evidence_digest"]),
        )

    @classmethod
    def from_json(cls, value: str) -> "UCNSFactorizationEvidence":
        decoded = json.loads(value)
        if not isinstance(decoded, dict):
            raise ValueError("factorization evidence JSON must decode to an object")
        return cls.from_dict(decoded)


def bridge_record(obj: Optional[UCNSObject]) -> UCNSBridgeRecord:
    """Build a serialized bridge record from the canonical object inspector."""

    record = object_record(obj)
    metadata = record.domain_metadata
    return UCNSBridgeRecord(
        object_hash=str(record.object_hash),
        canonical_json=str(record.canonical_json),
        domain_label=str(record.domain_label),
        domain_statuses=_status_values(metadata),
        completeness_guaranteed=bool(metadata.completeness_guaranteed),
        seq_prime_claim_scope=str(metadata.seq_prime_claim_scope),
        depth=int(record.depth),
        n_min=int(record.n_min),
        length=int(record.length),
        is_unit=bool(record.is_unit),
        is_verified_domain=bool(record.is_verified_domain),
        is_frontier=bool(record.is_frontier),
        note=str(record.note),
    )


def factorization_evidence(
    product: Optional[UCNSObject],
    catalogue: Optional[Iterable[Optional[UCNSObject]]] = None,
) -> UCNSFactorizationEvidence:
    """Run the authoritative UCNS result policy and serialize its evidence.

    No caller-supplied result object or certification boolean is accepted.
    """

    result = factorization_result(product, catalogue=catalogue)
    metadata = result.product_domain_metadata
    factor_hashes = (
        tuple(stable_hash(factor) for factor in result.factors)
        if result.factors is not None
        else ()
    )
    result_kind = (
        result.result_kind.value
        if hasattr(result.result_kind, "value")
        else str(result.result_kind)
    )
    return UCNSFactorizationEvidence(
        product_hash=str(result.product_hash),
        product_domain_label=str(result.product_domain_label),
        product_domain_statuses=_status_values(metadata),
        completeness_guaranteed=bool(metadata.completeness_guaranteed),
        result_kind=result_kind,
        factor_hashes=factor_hashes,
        negative_result_certified=bool(result.negative_result_certified),
        seq_prime_is_absolute=bool(result.seq_prime_is_absolute),
        claim_scope=str(result.claim_scope),
        note=str(result.note),
        certification_policy_version=str(result.certification_policy_version),
        search_exhausted=bool(result.search_exhausted),
        truncation_occurred=bool(result.truncation_occurred),
        catalogue_source=str(result.catalogue_source),
        supplied_catalogue_size=int(result.supplied_catalogue_size),
        supplied_catalogue_fingerprint=str(result.supplied_catalogue_fingerprint),
        effective_catalogue_size=int(result.effective_catalogue_size),
        effective_catalogue_fingerprint=str(result.effective_catalogue_fingerprint),
        catalogue_coverage_status=str(result.catalogue_coverage_status),
        catalogue_coverage_reason=str(result.catalogue_coverage_reason),
        catalogue_coverage_rule_version=str(result.catalogue_coverage_rule_version),
        required_catalogue_rule_version=str(result.required_catalogue_rule_version),
        required_catalogue_fingerprint=str(result.required_catalogue_fingerprint),
        coverage_record_validated=bool(result.coverage_record_validated),
        coverage_bound_to_search_report=bool(result.coverage_bound_to_search_report),
        pruning_applied=bool(result.pruning_applied),
        pruning_rule=str(result.pruning_rule),
        pruning_rule_version=str(result.pruning_rule_version),
        pruning_preserves_coverage=bool(result.pruning_preserves_coverage),
        uncertified_reasons=tuple(result.uncertified_reasons),
    )


__all__ = [
    "BRIDGE_RECORD_SCHEMA_ID",
    "BRIDGE_RECORD_SCHEMA_VERSION",
    "FACTORIZATION_EVIDENCE_SCHEMA_ID",
    "FACTORIZATION_EVIDENCE_SCHEMA_VERSION",
    "UCNSBridgeRecord",
    "UCNSFactorizationEvidence",
    "bridge_record",
    "factorization_evidence",
]
