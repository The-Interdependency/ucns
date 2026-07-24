"""Bounded downstream profiles built from current UCNS structural foundations."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Iterable

from .bridge import (
    BridgeCell,
    EdcmMetapatBridgeRecord,
    InformationLossRecord,
    PROFILE_ID,
    PROFILE_VERSION,
    PRODUCER_EPOCH,
    retained_layer_digests,
)
from .carrier import STRUCTURAL_NULL, _StructuralNull
from .structure import Carrier, Cell, Structure


PROFILE_OPTIONS: tuple[tuple[str, bool], ...] = tuple(
    sorted(
        {
            "left_right_sidedness_preserved": True,
            "multiplicity_preserved": True,
            "no_deduplication": True,
            "no_implicit_coercion": True,
            "no_shift_to_first_origin": True,
            "no_sorting": True,
            "occurrence_identity_preserved": True,
            "order_preserved": True,
            "retained_layers_outside_scalar_support": True,
            "structural_null_distinct_from_algebraic_zero": True,
        }.items()
    )
)


def _jsonable(value: object) -> object:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, tuple):
        return [_jsonable(item) for item in value]
    if isinstance(value, list):
        return [_jsonable(item) for item in value]
    if isinstance(value, dict):
        if not all(isinstance(key, str) for key in value):
            raise TypeError("profile cell mapping keys must be strings")
        return {key: _jsonable(value[key]) for key in sorted(value)}
    raise TypeError(f"unsupported profile cell value: {type(value).__name__}")


def _cell_identity_payload(cell: Cell) -> dict[str, object]:
    return {
        "coordinate": _jsonable(cell.coordinate),
        "payload": _jsonable(cell.payload),
        "type_tag": _jsonable(cell.type_tag),
        "shape": _jsonable(cell.shape),
        "state": _jsonable(cell.state),
        "provenance": _jsonable(cell.provenance),
        "relation": _jsonable(cell.relation),
        "support": cell.support,
    }


def _occurrence_id(index: int, cell: Cell) -> str:
    encoded = json.dumps(
        {
            "profile_id": PROFILE_ID,
            "profile_version": PROFILE_VERSION,
            "index": index,
            "cell": _cell_identity_payload(cell),
        },
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"occ-{index}-{sha256(encoded).hexdigest()}"


@dataclass(frozen=True, slots=True)
class ProfileBoundStructure:
    """A structure proven to use the EDCM/METAPAT ordered-occurrence profile."""

    structure: Structure
    occurrence_ids: tuple[str, ...]
    profile_id: str = PROFILE_ID
    profile_version: str = PROFILE_VERSION
    producer_epoch: str = PRODUCER_EPOCH
    options: tuple[tuple[str, bool], ...] = PROFILE_OPTIONS

    def __post_init__(self) -> None:
        if self.profile_id != PROFILE_ID or self.profile_version != PROFILE_VERSION:
            raise ValueError("profile identity mismatch")
        if self.producer_epoch != PRODUCER_EPOCH:
            raise ValueError("producer epoch mismatch")
        if self.options != PROFILE_OPTIONS:
            raise ValueError("profile option declaration mismatch")
        if self.structure is STRUCTURAL_NULL:
            if self.occurrence_ids:
                raise ValueError("Structural Null cannot contain occurrences")
            return
        if not isinstance(self.structure, Carrier):
            raise TypeError("profile structure must be Carrier or STRUCTURAL_NULL")
        if len(self.occurrence_ids) != len(self.structure.cells):
            raise ValueError("one occurrence identity is required per ordered cell")
        if len(set(self.occurrence_ids)) != len(self.occurrence_ids):
            raise ValueError("occurrence identities must be unique")
        expected = tuple(
            _occurrence_id(index, cell)
            for index, cell in enumerate(self.structure.cells)
        )
        if self.occurrence_ids != expected:
            raise ValueError("occurrence identities do not match ordered cells")

    @property
    def cells(self) -> tuple[Cell, ...]:
        if self.structure is STRUCTURAL_NULL:
            return ()
        assert isinstance(self.structure, Carrier)
        return self.structure.cells


@dataclass(frozen=True, slots=True)
class EdcmMetapatOrderedOccurrenceProfile:
    """Single post-reset profile for ordered EDCM/METAPAT occurrences."""

    profile_id: str = PROFILE_ID
    version: str = PROFILE_VERSION
    producer_epoch: str = PRODUCER_EPOCH
    options: tuple[tuple[str, bool], ...] = PROFILE_OPTIONS

    def __post_init__(self) -> None:
        if self.profile_id != PROFILE_ID or self.version != PROFILE_VERSION:
            raise ValueError("profile identity is fixed for version 1.0.0")
        if self.producer_epoch != PRODUCER_EPOCH:
            raise ValueError("producer epoch is fixed")
        if self.options != PROFILE_OPTIONS:
            raise ValueError("profile options are fixed and fail closed")

    def bind(self, structure: Structure) -> ProfileBoundStructure:
        """Validate and bind a current-root structure without projecting it."""

        if structure is STRUCTURAL_NULL:
            return ProfileBoundStructure(structure=structure, occurrence_ids=())
        if not isinstance(structure, Carrier):
            raise TypeError("structure must be Carrier or STRUCTURAL_NULL")
        occurrence_ids = tuple(
            _occurrence_id(index, cell)
            for index, cell in enumerate(structure.cells)
        )
        return ProfileBoundStructure(
            structure=structure,
            occurrence_ids=occurrence_ids,
        )

    def to_bridge(
        self,
        bound: ProfileBoundStructure,
        *,
        source_commit: str,
        operator_history: Iterable[str] = (),
        information_loss: Iterable[InformationLossRecord] = (),
    ) -> EdcmMetapatBridgeRecord:
        """Create a validated bridge; the producer commit is always explicit."""

        if not isinstance(bound, ProfileBoundStructure):
            raise TypeError("to_bridge requires a ProfileBoundStructure")
        if bound.options != self.options:
            raise ValueError("bound structure option mismatch")

        cells = tuple(
            BridgeCell(
                occurrence_id=occurrence_id,
                coordinate=_jsonable(cell.coordinate),
                payload=_jsonable(cell.payload),
                type_tag=_jsonable(cell.type_tag),
                shape=_jsonable(cell.shape),
                state=_jsonable(cell.state),
                provenance=_jsonable(cell.provenance),
                relation=_jsonable(cell.relation),
                support=cell.support,
            )
            for occurrence_id, cell in zip(bound.occurrence_ids, bound.cells)
        )
        return EdcmMetapatBridgeRecord(
            source_commit=source_commit,
            options=self.options,
            cells=cells,
            retained_layers=retained_layer_digests(cells),
            operator_history=tuple(operator_history),
            information_loss=tuple(information_loss),
        )


__all__ = [
    "PROFILE_OPTIONS",
    "EdcmMetapatOrderedOccurrenceProfile",
    "ProfileBoundStructure",
]
