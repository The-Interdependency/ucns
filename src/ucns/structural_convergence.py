"""Domain-neutral UCNS evidence for multi-origin structural convergence.

The module records geometric/structural evidence only. It does not decide
semantic equivalence, analogy, truth, or domain meaning; METAPAT owns that
adjudication.
"""

# === MODULE_BUILD ===
# id: ucns_multi_origin_convergence_v0
#   module_name: structural_convergence
#   module_kind: schema
#   summary: records deterministic multi-origin path, mapping, invariant, replay, and ancestry evidence for downstream recurrence adjudication
#   owner: Erin Spencer
#   public_surface: OriginPath, StructuralMapping, InvariantObservation, StructuralConvergenceWitness, build_convergence_witness
#   internal_surface: canonical digest validation
#   auth_boundary: none
#   storage_boundary: serialization-only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_structural_convergence
#   rollout: candidate geometry/representation evidence surface
#   rollback: remove module and tests
#   requires: ucns scale/representation jurisdiction
#   since: 2026-10-03
#   unresolved: no universal path metric or equivalence theorem is asserted
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: convergence_preserves_path_distinction
#   given: two paths are recorded
#   then: their origins, path identities, structure identities, and provenance remain separate
#   class: correctness
# id: convergence_records_not_judges
#   given: a witness is built
#   then: it contains structural facts and no semantic-equivalence or analogy outcome
#   class: boundary_contract
# id: convergence_replay_is_typed
#   given: replay has not been established
#   then: replay_passed remains null rather than becoming false or zero
#   class: safety
# id: convergence_digest_tamper_rejected
#   given: a serialized witness is changed without digest rotation
#   then: reconstruction fails closed
#   class: correctness
# === END CONTRACTS ===

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from typing import Any, Mapping, Optional

SCHEMA = "ucns.structural-convergence"
VERSION = "0.1.0"


def _canonical(value: Mapping[str, Any]) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def _nonempty(value: str, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value


@dataclass(frozen=True, slots=True)
class OriginPath:
    origin_id: str
    path_id: str
    structure_id: str
    provenance_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _nonempty(self.origin_id, "origin_id")
        _nonempty(self.path_id, "path_id")
        _nonempty(self.structure_id, "structure_id")
        if any(not isinstance(x, str) or not x.strip() for x in self.provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")


@dataclass(frozen=True, slots=True)
class StructuralMapping:
    source_component: str
    target_component: str

    def __post_init__(self) -> None:
        _nonempty(self.source_component, "source_component")
        _nonempty(self.target_component, "target_component")


@dataclass(frozen=True, slots=True)
class InvariantObservation:
    invariant_id: str
    source_value: str
    target_value: str
    preserved: bool

    def __post_init__(self) -> None:
        _nonempty(self.invariant_id, "invariant_id")
        _nonempty(self.source_value, "source_value")
        _nonempty(self.target_value, "target_value")
        if type(self.preserved) is not bool:
            raise ValueError("preserved must be bool")


@dataclass(frozen=True, slots=True)
class StructuralConvergenceWitness:
    source: OriginPath
    target: OriginPath
    mappings: tuple[StructuralMapping, ...]
    invariants: tuple[InvariantObservation, ...]
    mapping_complete: Optional[bool]
    replay_passed: Optional[bool]
    equivalence_proof_id: Optional[str] = None
    shared_ancestry: tuple[str, ...] = ()
    unresolved: tuple[str, ...] = ()
    schema: str = SCHEMA
    version: str = VERSION
    receipt_sha256: str = ""

    def __post_init__(self) -> None:
        if self.source == self.target:
            raise ValueError("source and target paths must be distinct records")
        if not self.mappings:
            raise ValueError("at least one structural mapping is required")
        if not self.invariants:
            raise ValueError("at least one invariant observation is required")
        ids = [item.invariant_id for item in self.invariants]
        if len(ids) != len(set(ids)):
            raise ValueError("invariant_id values must be unique")
        for value, label in (
            (self.shared_ancestry, "shared_ancestry"),
            (self.unresolved, "unresolved"),
        ):
            if any(not isinstance(x, str) or not x.strip() for x in value):
                raise ValueError(f"{label} must contain non-empty strings")
        if self.equivalence_proof_id is not None:
            _nonempty(self.equivalence_proof_id, "equivalence_proof_id")
        if self.schema != SCHEMA or self.version != VERSION:
            raise ValueError("unsupported structural convergence schema")
        expected = sha256(_canonical(self._payload())).hexdigest()
        if self.receipt_sha256 and self.receipt_sha256 != expected:
            raise ValueError("receipt_sha256 mismatch")
        object.__setattr__(self, "receipt_sha256", expected)

    @property
    def preserved_invariant_ids(self) -> tuple[str, ...]:
        return tuple(i.invariant_id for i in self.invariants if i.preserved)

    @property
    def paths_distinct(self) -> bool:
        return (
            self.source.origin_id != self.target.origin_id
            or self.source.path_id != self.target.path_id
        )

    @property
    def independent(self) -> bool:
        return self.paths_distinct and not self.shared_ancestry

    def _payload(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "source": asdict(self.source),
            "target": asdict(self.target),
            "mappings": [asdict(x) for x in self.mappings],
            "invariants": [asdict(x) for x in self.invariants],
            "mapping_complete": self.mapping_complete,
            "replay_passed": self.replay_passed,
            "equivalence_proof_id": self.equivalence_proof_id,
            "shared_ancestry": list(self.shared_ancestry),
            "unresolved": list(self.unresolved),
        }

    def to_dict(self) -> dict[str, Any]:
        return {**self._payload(), "receipt_sha256": self.receipt_sha256}

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "StructuralConvergenceWitness":
        if not isinstance(data, Mapping):
            raise ValueError("witness must be a mapping")
        expected = {
            "schema", "version", "source", "target", "mappings", "invariants",
            "mapping_complete", "replay_passed", "equivalence_proof_id",
            "shared_ancestry", "unresolved", "receipt_sha256",
        }
        if set(data) != expected:
            raise ValueError("witness fields do not match schema")
        return cls(
            schema=data["schema"],
            version=data["version"],
            source=OriginPath(**data["source"]),
            target=OriginPath(**data["target"]),
            mappings=tuple(StructuralMapping(**x) for x in data["mappings"]),
            invariants=tuple(InvariantObservation(**x) for x in data["invariants"]),
            mapping_complete=data["mapping_complete"],
            replay_passed=data["replay_passed"],
            equivalence_proof_id=data["equivalence_proof_id"],
            shared_ancestry=tuple(data["shared_ancestry"]),
            unresolved=tuple(data["unresolved"]),
            receipt_sha256=data["receipt_sha256"],
        )


def build_convergence_witness(**kwargs: Any) -> StructuralConvergenceWitness:
    return StructuralConvergenceWitness(**kwargs)


__all__ = [
    "SCHEMA", "VERSION", "OriginPath", "StructuralMapping",
    "InvariantObservation", "StructuralConvergenceWitness",
    "build_convergence_witness",
]
