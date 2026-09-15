# === MODULE_BUILD ===
# id: ucns_placement_frame_candidate
#   module_name: placement_frame
#   module_kind: candidate
#   summary: maps the three evidence residue channels into the established placement frame (angle from the 157-position carrier, radius from the canonical radial map, layer from deck recursion) using only UCNS primitives
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, PlacementFrameError, PlacementFrameRecord, build_placement_frame, replay_placement_frame
#   internal_surface: channel-to-axis candidate mapping, exact rational angle/layer arithmetic, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_placement_frame
#   rollout: executable candidate placement frame; candidate standing, not UCNS canon
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: directed_carrier_floor, ucns_native_mobius_geometry, ucns_public_gonol_geometry
#   since: 2026-09-15
#   unresolved: the channel-to-axis mapping is a candidate; the exact displacement law that consumes this frame remains hmmm
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: placement_frame_ordinal_carries_angle
#   given: an exact ordinal residue channel
#   then: angle is exactly ordinal/157 visible turns on the 157-position carrier
#   class: correctness
#   since: 2026-09-15
#
# id: placement_frame_semantic_carries_radius_via_breadth
#   given: an exact semantic residue channel declared as faithful breadth
#   then: radius is the canonical radial map on that breadth, never an invented depth constant
#   class: correctness
#   since: 2026-09-15
#
# id: placement_frame_context_carries_layer
#   given: an exact context residue channel
#   then: layer is context deck translations in the lifted carrier with two-lap complete return
#   class: correctness
#   requires: two_visible_laps_complete_return
#   since: 2026-09-15
#
# id: placement_frame_preserves_native_mobius_law
#   given: the computed angle turn
#   then: advancing a NativeMobiusState by it preserves the 360/720 frame law
#   class: correctness
#   requires: native_mobius_one_turn_reverses_frame
#   since: 2026-09-15
#
# id: placement_frame_remains_candidate
#   given: an exact executable frame
#   then: the channel-to-axis mapping and the displacement law that consumes it remain candidates; execution alone is not ratification
#   class: doctrine
#   since: 2026-09-15
#
# id: placement_frame_fails_closed
#   given: non-integer channels, non-finite semantic breadth, or a malformed receipt
#   then: construction or replay raises PlacementFrameError rather than inventing a mapping
#   class: safety
#   since: 2026-09-15
# === END CONTRACTS ===

"""Map the three evidence residue channels into the placement frame.

The frame is built only from established UCNS primitives:

```text
ordinal  -> angle  = ordinal/157 visible turns on the Public Gonol carrier
semantic -> radius = radius_from_breadth(semantic breadth)
context  -> layer  = context deck translations in the lifted carrier
```

Angle and layer use exact rational arithmetic; radius is consumed from the
canonical radial map. The channel-to-axis mapping and the displacement law
that consumes this frame remain candidates, not ratified UCNS law.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from math import isfinite, pi
from typing import Any

from .carrier import LIFTED_PERIOD, VISIBLE_PERIOD, radius_from_breadth
from .direct_mobius import NativeMobiusState, native_mobius_state
from .public_gonol import PUBLIC_GONOL_157

SCHEMA = "ucns.placement-frame-candidate"
VERSION = "0.1.0"
_MODULUS = len(PUBLIC_GONOL_157)

_CHANNEL_MAPPING = {
    "ordinal": "angle (ordinal/157 visible turns)",
    "semantic": "radius (canonical radial map on semantic breadth)",
    "context": "layer (context deck translations, two-lap return)",
}

_HMMM = (
    "the channel-to-axis mapping and the displacement law that consumes "
    "this frame remain candidates; execution alone is not ratification"
)


class PlacementFrameError(ValueError):
    """Raised when the placement frame fails closed."""


@dataclass(frozen=True)
class PlacementFrameRecord:
    schema: str
    version: str
    ordinal: int
    semantic: int
    context: int
    angle_turn: Fraction
    mobius: NativeMobiusState
    radius: float
    layer: int
    lifted_angle: float
    channel_mapping: dict[str, str]
    hmmm: str
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "ordinal": self.ordinal,
            "semantic": self.semantic,
            "context": self.context,
            "angle_turn": f"{self.angle_turn.numerator}/{self.angle_turn.denominator}",
            "mobius": {
                "phase_turns": f"{self.mobius.phase_turns.numerator}/{self.mobius.phase_turns.denominator}",
                "frame": self.mobius.frame.value,
            },
            "radius": repr(self.radius),
            "layer": self.layer,
            "lifted_angle": repr(self.lifted_angle),
            "channel_mapping": self.channel_mapping,
            "hmmm": self.hmmm,
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


def _coerce_channel(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise PlacementFrameError(f"{name} must be an exact integer")
    return value % _MODULUS


def build_placement_frame(
    ordinal: int,
    semantic: int,
    context: int,
) -> PlacementFrameRecord:
    """Map the three channels into (angle, radius, layer) with exact arithmetic."""

    ordinal_residue = _coerce_channel("ordinal", ordinal)
    semantic_residue = _coerce_channel("semantic", semantic)
    context_residue = _coerce_channel("context", context)

    angle_turn = Fraction(ordinal_residue, _MODULUS)
    mobius = native_mobius_state().advance(angle_turn)

    breadth = float(semantic_residue)
    if not isfinite(breadth) or breadth < 0.0:
        raise PlacementFrameError("semantic breadth must be finite and nonnegative")
    radius = radius_from_breadth(breadth)

    layer = context_residue % 2
    lifted_angle = (layer * VISIBLE_PERIOD) % LIFTED_PERIOD

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "ordinal": ordinal_residue,
        "semantic": semantic_residue,
        "context": context_residue,
        "angle_turn": f"{angle_turn.numerator}/{angle_turn.denominator}",
        "mobius": {
            "phase_turns": f"{mobius.phase_turns.numerator}/{mobius.phase_turns.denominator}",
            "frame": mobius.frame.value,
        },
        "radius": repr(radius),
        "layer": layer,
        "lifted_angle": repr(lifted_angle),
        "channel_mapping": _CHANNEL_MAPPING,
        "hmmm": _HMMM,
    }
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return PlacementFrameRecord(
        schema=SCHEMA,
        version=VERSION,
        ordinal=ordinal_residue,
        semantic=semantic_residue,
        context=context_residue,
        angle_turn=angle_turn,
        mobius=mobius,
        radius=radius,
        layer=layer,
        lifted_angle=lifted_angle,
        channel_mapping=_CHANNEL_MAPPING,
        hmmm=_HMMM,
        receipt_sha256=receipt,
    )


def replay_placement_frame(data: bytes) -> PlacementFrameRecord:
    """Rebuild the frame record and verify it byte-for-byte."""

    if not isinstance(data, bytes):
        raise PlacementFrameError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise PlacementFrameError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise PlacementFrameError("receipt root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise PlacementFrameError("receipt schema or version mismatch")

    record = build_placement_frame(
        ordinal=obj["ordinal"],
        semantic=obj["semantic"],
        context=obj["context"],
    )
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise PlacementFrameError("receipt digest does not match replayed frame")
    if record.receipt_bytes() != data:
        raise PlacementFrameError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "PlacementFrameError",
    "PlacementFrameRecord",
    "build_placement_frame",
    "replay_placement_frame",
]
