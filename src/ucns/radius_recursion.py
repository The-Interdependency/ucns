# === MODULE_BUILD ===
# id: ucns_radius_recursion_candidate
#   module_name: radius_recursion
#   module_kind: candidate
#   summary: derives the radius/scale transition by composing the canonical radial map with the lifted-carrier deck recursion, and records that UCNS scale recursion supplies layer recursion while radius stays a function of breadth
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, RadiusRecursionError, RadiusRecursionRecord, build_radius_recursion, replay_radius_recursion
#   internal_surface: canonical radial map consumption, deck-translation counting, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_radius_recursion
#   rollout: executable candidate derivation inside the radius-semantics preregistration; candidate standing, not UCNS canon
#   rollback: remove this module, facade exports, tests, and candidate documentation
#   requires: directed_carrier_floor
#   since: 2026-09-15
#   unresolved: ratification of the radius/scale transition; the recovered invariant remains a candidate derivation
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: radius_recursion_radius_is_canonical_radial_map
#   given: a nonnegative faithful breadth
#   then: the radius at every completed depth equals radius_from_breadth(breadth), never an additive depth constant
#   class: correctness
#   since: 2026-09-15
#
# id: radius_recursion_layers_are_deck_translations
#   given: a completed recursion depth d
#   then: the lifted representative advances by exactly d visible laps and the visible projection is unchanged
#   class: correctness
#   requires: one_visible_lap_is_deck_translation_only
#   since: 2026-09-15
#
# id: radius_recursion_two_laps_complete_return
#   given: a completed recursion depth of two
#   then: the lifted representative returns exactly
#   class: correctness
#   requires: two_visible_laps_complete_return
#   since: 2026-09-15
#
# id: radius_recursion_english_depth_is_not_a_radius
#   given: the preregistered English candidate r(x) = r0 + d(x)
#   then: this derivation records it as superseded: UCNS scale recursion supplies the layer recursion and radius is a function of breadth only
#   class: doctrine
#   since: 2026-09-15
#
# id: radius_recursion_fails_closed
#   given: negative depth, non-finite breadth, or a malformed receipt
#   then: construction or replay raises RadiusRecursionError rather than inventing a radial step
#   class: safety
#   since: 2026-09-15
# === END CONTRACTS ===

"""Derive the radius/scale transition from the established UCNS carrier floor.

The open question in the radius-semantics preregistration was whether each
completed construction layer requires a new radius or whether UCNS scale
recursion supplies the radius automatically.

The established carrier primitives answer it:

* radius is the canonical radial map ``a = 1 - exp(-B)`` on faithful breadth;
* scale recursion is the twofold branched cover: one visible lap is a deck
  translation that changes the lifted representative, two laps complete the
  return, and the visible projection never changes.

Therefore each completed affixiation/containment layer is one deck
translation in the lifted carrier. Radius does not advance per layer; it is
already supplied by the canonical radial map on breadth. The English
candidate ``r(x) = r0 + d(x)`` is superseded: depth counts deck-translation
steps, not additive radial units.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from math import isfinite, pi
from typing import Any

from .carrier import (
    LIFTED_PERIOD,
    STRUCTURAL_NULL,
    VISIBLE_PERIOD,
    LiftedCarrierPoint,
    carrier_from_breadth,
    deck_translate,
    project,
    radius_from_breadth,
)

SCHEMA = "ucns.radius-recursion-candidate"
VERSION = "0.1.0"


class RadiusRecursionError(ValueError):
    """Raised when the radius-recursion derivation fails closed."""


@dataclass(frozen=True)
class RadiusRecursionRecord:
    schema: str
    version: str
    depth: int
    base_breadth: float
    radius: float
    lifted_angle: float
    visible_angle: float
    lifted_null: bool
    conclusion: str
    receipt_sha256: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "schema": self.schema,
            "version": self.version,
            "depth": self.depth,
            "base_breadth": repr(self.base_breadth),
            "radius": repr(self.radius),
            "lifted_angle": repr(self.lifted_angle),
            "visible_angle": repr(self.visible_angle),
            "lifted_null": self.lifted_null,
            "conclusion": self.conclusion,
            "receipt_sha256": self.receipt_sha256,
        }

    def canonical_bytes(self) -> bytes:
        payload = self.as_dict()
        payload.pop("receipt_sha256", None)
        return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")

    def receipt_bytes(self) -> bytes:
        return json.dumps(self.as_dict(), sort_keys=True, separators=(",", ":")).encode("utf-8")


_CONCLUSION = (
    "UCNS scale recursion supplies the layer recursion: each completed "
    "construction level is one deck translation in the lifted carrier, and "
    "radius is the canonical radial map on breadth only. The English "
    "candidate r(x) = r0 + d(x) is superseded; depth counts deck-translation "
    "steps, not additive radial units."
)


def build_radius_recursion(depth: int, base_breadth: float) -> RadiusRecursionRecord:
    """Compose the canonical radial map with depth deck translations."""

    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise RadiusRecursionError("depth must be a nonnegative integer")
    breadth = float(base_breadth)
    if not isfinite(breadth) or breadth < 0.0:
        raise RadiusRecursionError("breadth must be finite and nonnegative")

    radius = radius_from_breadth(breadth)
    point = carrier_from_breadth(breadth, angle=0.0)
    for _ in range(depth):
        point = deck_translate(point)

    if point is STRUCTURAL_NULL:
        lifted_null = True
        lifted_angle = 0.0
        visible_angle = 0.0
    else:
        lifted_null = False
        lifted_angle = point.angle % LIFTED_PERIOD
        visible = project(point)
        if visible is STRUCTURAL_NULL:
            visible_angle = 0.0
        else:
            visible_angle = visible.angle % VISIBLE_PERIOD

    payload = {
        "schema": SCHEMA,
        "version": VERSION,
        "depth": depth,
        "base_breadth": repr(breadth),
        "radius": repr(radius),
        "lifted_angle": repr(lifted_angle),
        "visible_angle": repr(visible_angle),
        "lifted_null": lifted_null,
        "conclusion": _CONCLUSION,
    }
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    return RadiusRecursionRecord(
        schema=SCHEMA,
        version=VERSION,
        depth=depth,
        base_breadth=breadth,
        radius=radius,
        lifted_angle=lifted_angle,
        visible_angle=visible_angle,
        lifted_null=lifted_null,
        conclusion=_CONCLUSION,
        receipt_sha256=receipt,
    )


def replay_radius_recursion(data: bytes) -> RadiusRecursionRecord:
    """Rebuild the derivation record and verify it byte-for-byte."""

    if not isinstance(data, bytes):
        raise RadiusRecursionError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RadiusRecursionError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise RadiusRecursionError("receipt root must be an object")
    if obj.get("schema") != SCHEMA or obj.get("version") != VERSION:
        raise RadiusRecursionError("receipt schema or version mismatch")

    record = build_radius_recursion(
        depth=obj["depth"],
        base_breadth=float(obj["base_breadth"]),
    )
    if record.receipt_sha256 != obj.get("receipt_sha256"):
        raise RadiusRecursionError("receipt digest does not match replayed derivation")
    if record.receipt_bytes() != data:
        raise RadiusRecursionError("receipt does not replay byte-identically")
    return record


__all__ = [
    "SCHEMA",
    "VERSION",
    "RadiusRecursionError",
    "RadiusRecursionRecord",
    "build_radius_recursion",
    "replay_radius_recursion",
]
