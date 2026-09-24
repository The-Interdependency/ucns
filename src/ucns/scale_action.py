# === MODULE_BUILD ===
# id: ucns_multiplicative_scale_action_candidate
#   module_name: scale_action
#   module_kind: experiment
#   summary: exact domain-agnostic multiplicative scale action with composition, inversion, monomial-invariant detection, and replayable application receipts
#   owner: Erin Spencer
#   public_surface: SCHEMA, VERSION, ScaleActionError, MultiplicativeScaleAction, ScaleActionRecord, build_scale_action, build_scale_action_record, monomial_value, replay_scale_action_record
#   internal_surface: exact positive-rational coercion, integer exponentiation, canonical receipt serialization
#   auth_boundary: none
#   storage_boundary: immutable records only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_scale_action
#   rollout: executable candidate behind explicit caller construction; not selected or ratified as the complete UCNS scale law
#   rollback: remove this module, facade exports, tests, and scale-action documentation
#   requires: none
#   since: 2026-09-23
#   unresolved: binding to native Mobius origin/attachment, recursive carrier boundaries, and the complete higher-scale composition law
# === END MODULE_BUILD ===
#
# === CONTRACTS ===
# id: scale_action_applies_integer_weights_exactly
#   given: a positive exact rational factor q, an ordered integer weight vector w, and positive exact rational state x
#   then: coordinate i transforms exactly as x_i -> q^w_i * x_i with no floating-point arithmetic
#   class: correctness
#   since: 2026-09-23
#
# id: scale_action_composes_multiplicatively
#   given: two actions with the same ordered weight vector and factors p and q
#   then: sequential application equals one action with factor p*q; factor 1 is identity and reciprocal factor is inverse
#   class: correctness
#   since: 2026-09-23
#
# id: scale_action_monomial_invariants_are_weight_kernel
#   given: a monomial exponent vector a on the same ordered coordinates
#   then: the monomial is structurally invariant exactly when sum(a_i*w_i) = 0, and invariant values are preserved exactly by application
#   class: correctness
#   since: 2026-09-23
#
# id: scale_action_core_is_domain_agnostic
#   given: a scale action or application receipt
#   then: the UCNS core stores only ordered integer weights, exact scale factors, exact coordinates, standing, and provenance receipt data; domain names and interpretations are external
#   class: doctrine
#   since: 2026-09-23
#
# id: scale_action_receipts_replay_exactly
#   given: a canonical application receipt
#   then: replay reconstructs the same action and target byte-identically while malformed or tampered receipts fail closed
#   class: safety
#   since: 2026-09-23
# === END CONTRACTS ===

"""Exact multiplicative scale-action candidate.

For an ordered positive coordinate state ``x`` and integer weight vector ``w``,
this module implements the diagonal action

    T_q(x)_i = q**w_i * x_i

for positive exact rational ``q``. Actions with the same weights compose as

    T_p o T_q = T_(p*q),

with identity ``q = 1`` and inverse ``q -> 1/q``.

For a monomial ``I_a(x) = product(x_i**a_i)``, the structural scale weight is

    sum(a_i * w_i).

The monomial is invariant under every factor in this one-parameter action
exactly when that weight is zero.

This is a domain-agnostic mathematical representation candidate. UCNS does not
assign physical, chemical, linguistic, consciousness, or other semantics to the
coordinates or weights. Consumers own those bindings. The candidate also does
not claim to be the complete UCNS scale-transition law: attachment/origin,
recursive carrier transitions, and composition with the native Mobius geometry
remain separate unresolved work.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from typing import Iterable

SCHEMA = "ucns.multiplicative-scale-action-candidate"
VERSION = "0.1.0"
_STANDING = "candidate"


class ScaleActionError(ValueError):
    """Raised when an exact multiplicative scale action fails closed."""


def _coerce_weights(weights: Iterable[int]) -> tuple[int, ...]:
    try:
        resolved = tuple(weights)
    except TypeError as exc:
        raise ScaleActionError("weights must be an iterable of integers") from exc
    if not resolved:
        raise ScaleActionError("weights must be nonempty")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in resolved):
        raise ScaleActionError("weights must contain nonboolean integers only")
    return resolved


def _coerce_positive_fraction(name: str, value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ScaleActionError(f"{name} must be an exact integer or Fraction")
    resolved = Fraction(value)
    if resolved <= 0:
        raise ScaleActionError(f"{name} must be positive")
    return resolved


def _coerce_state(
    state: Iterable[int | Fraction],
    arity: int,
) -> tuple[Fraction, ...]:
    try:
        raw = tuple(state)
    except TypeError as exc:
        raise ScaleActionError("state must be an iterable of exact coordinates") from exc
    if len(raw) != arity:
        raise ScaleActionError("state arity must equal the action weight arity")
    return tuple(
        _coerce_positive_fraction(f"state[{index}]", value)
        for index, value in enumerate(raw)
    )


def _coerce_powers(powers: Iterable[int], arity: int) -> tuple[int, ...]:
    try:
        resolved = tuple(powers)
    except TypeError as exc:
        raise ScaleActionError("powers must be an iterable of integers") from exc
    if len(resolved) != arity:
        raise ScaleActionError("monomial power arity must equal the action weight arity")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in resolved):
        raise ScaleActionError("monomial powers must contain nonboolean integers only")
    return resolved


def _fraction_power(value: Fraction, exponent: int) -> Fraction:
    if exponent >= 0:
        return value ** exponent
    return Fraction(1, 1) / (value ** (-exponent))


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _fraction_from_text(name: str, value: object) -> Fraction:
    if not isinstance(value, str):
        raise ScaleActionError(f"{name} must be a canonical fraction string")
    try:
        resolved = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ScaleActionError(f"{name} is not a valid fraction") from exc
    if _fraction_text(resolved) != value:
        raise ScaleActionError(f"{name} is not in canonical fraction form")
    if resolved <= 0:
        raise ScaleActionError(f"{name} must be positive")
    return resolved


def monomial_value(
    state: Iterable[int | Fraction],
    powers: Iterable[int],
) -> Fraction:
    """Evaluate one exact monomial on positive exact rational coordinates."""

    raw_state = tuple(state)
    raw_powers = tuple(powers)
    resolved_state = _coerce_state(raw_state, len(raw_state))
    resolved_powers = _coerce_powers(raw_powers, len(resolved_state))
    value = Fraction(1, 1)
    for coordinate, exponent in zip(resolved_state, resolved_powers, strict=True):
        value *= _fraction_power(coordinate, exponent)
    return value


@dataclass(frozen=True, slots=True)
class MultiplicativeScaleAction:
    """One exact diagonal multiplicative action on an ordered scale carrier."""

    weights: tuple[int, ...]
    factor: Fraction

    def __post_init__(self) -> None:
        if not isinstance(self.weights, tuple):
            raise ScaleActionError("canonical weights must be an immutable tuple")
        _coerce_weights(self.weights)
        if not isinstance(self.factor, Fraction):
            raise ScaleActionError("canonical factor must be a Fraction")
        _coerce_positive_fraction("factor", self.factor)

    @property
    def arity(self) -> int:
        return len(self.weights)

    def apply(
        self,
        state: Iterable[int | Fraction],
    ) -> tuple[Fraction, ...]:
        """Apply ``x_i -> factor**weight_i * x_i`` exactly."""

        resolved = _coerce_state(state, self.arity)
        return tuple(
            coordinate * _fraction_power(self.factor, weight)
            for coordinate, weight in zip(resolved, self.weights, strict=True)
        )

    def compose(self, other: "MultiplicativeScaleAction") -> "MultiplicativeScaleAction":
        """Return the action equivalent to applying this action then ``other``."""

        if not isinstance(other, MultiplicativeScaleAction):
            raise ScaleActionError("composition requires another scale action")
        if self.weights != other.weights:
            raise ScaleActionError("scale actions compose only when ordered weights match")
        return MultiplicativeScaleAction(
            weights=self.weights,
            factor=self.factor * other.factor,
        )

    def inverse(self) -> "MultiplicativeScaleAction":
        """Return the exact reciprocal-factor inverse action."""

        return MultiplicativeScaleAction(
            weights=self.weights,
            factor=Fraction(1, 1) / self.factor,
        )

    def monomial_weight(self, powers: Iterable[int]) -> int:
        """Return the scale weight ``sum(a_i*w_i)`` of one monomial."""

        resolved = _coerce_powers(powers, self.arity)
        return sum(
            exponent * weight
            for exponent, weight in zip(resolved, self.weights, strict=True)
        )

    def is_invariant(self, powers: Iterable[int]) -> bool:
        """Return whether the monomial exponent vector lies in the weight kernel."""

        return self.monomial_weight(powers) == 0

    def preserves_monomial(
        self,
        state: Iterable[int | Fraction],
        powers: Iterable[int],
    ) -> bool:
        """Verify exact preservation for a structurally invariant monomial."""

        resolved_state = _coerce_state(state, self.arity)
        resolved_powers = _coerce_powers(powers, self.arity)
        if self.monomial_weight(resolved_powers) != 0:
            return False
        return monomial_value(resolved_state, resolved_powers) == monomial_value(
            self.apply(resolved_state),
            resolved_powers,
        )

    def as_dict(self) -> dict[str, object]:
        return {
            "weights": list(self.weights),
            "factor": _fraction_text(self.factor),
        }


def build_scale_action(
    weights: Iterable[int],
    factor: int | Fraction,
) -> MultiplicativeScaleAction:
    """Build the canonical exact action from caller-supplied ordered weights."""

    return MultiplicativeScaleAction(
        weights=_coerce_weights(weights),
        factor=_coerce_positive_fraction("factor", factor),
    )


def _record_payload(
    action: MultiplicativeScaleAction,
    source: tuple[Fraction, ...],
    target: tuple[Fraction, ...],
) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "version": VERSION,
        "standing": _STANDING,
        "action": action.as_dict(),
        "source": [_fraction_text(value) for value in source],
        "target": [_fraction_text(value) for value in target],
    }


@dataclass(frozen=True, slots=True)
class ScaleActionRecord:
    """Replayable exact witness of one scale-action application."""

    action: MultiplicativeScaleAction
    source: tuple[Fraction, ...]
    target: tuple[Fraction, ...]
    receipt_sha256: str

    def __post_init__(self) -> None:
        if not isinstance(self.action, MultiplicativeScaleAction):
            raise ScaleActionError("record action must be a validated scale action")
        if not isinstance(self.source, tuple) or not isinstance(self.target, tuple):
            raise ScaleActionError("record source and target must be immutable tuples")
        resolved_source = _coerce_state(self.source, self.action.arity)
        resolved_target = _coerce_state(self.target, self.action.arity)
        if resolved_source != self.source or resolved_target != self.target:
            raise ScaleActionError("record coordinates must be canonical Fractions")
        if self.action.apply(self.source) != self.target:
            raise ScaleActionError("record target does not equal exact action on source")
        expected = sha256(
            json.dumps(
                _record_payload(self.action, self.source, self.target),
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        if self.receipt_sha256 != expected:
            raise ScaleActionError("record receipt digest does not match its exact payload")

    def as_dict(self) -> dict[str, object]:
        payload = _record_payload(self.action, self.source, self.target)
        payload["receipt_sha256"] = self.receipt_sha256
        return payload

    def receipt_bytes(self) -> bytes:
        return json.dumps(
            self.as_dict(),
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")


def build_scale_action_record(
    weights: Iterable[int],
    factor: int | Fraction,
    source: Iterable[int | Fraction],
) -> ScaleActionRecord:
    """Apply one exact action and bind the result into a replayable receipt."""

    action = build_scale_action(weights, factor)
    resolved_source = _coerce_state(source, action.arity)
    target = action.apply(resolved_source)
    payload = _record_payload(action, resolved_source, target)
    receipt = sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return ScaleActionRecord(
        action=action,
        source=resolved_source,
        target=target,
        receipt_sha256=receipt,
    )


def replay_scale_action_record(data: bytes) -> ScaleActionRecord:
    """Reconstruct an application receipt and require byte-identical replay."""

    if not isinstance(data, bytes):
        raise ScaleActionError("receipt must be bytes")
    try:
        obj = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ScaleActionError("receipt is not valid canonical JSON") from exc
    if not isinstance(obj, dict):
        raise ScaleActionError("receipt root must be an object")
    expected_keys = {
        "schema",
        "version",
        "standing",
        "action",
        "source",
        "target",
        "receipt_sha256",
    }
    if set(obj) != expected_keys:
        raise ScaleActionError("receipt fields do not match the scale-action schema")
    if obj["schema"] != SCHEMA or obj["version"] != VERSION or obj["standing"] != _STANDING:
        raise ScaleActionError("receipt schema, version, or standing mismatch")
    action_obj = obj["action"]
    if not isinstance(action_obj, dict) or set(action_obj) != {"weights", "factor"}:
        raise ScaleActionError("receipt action is malformed")
    weights = action_obj["weights"]
    if not isinstance(weights, list):
        raise ScaleActionError("receipt weights must be a list")
    factor = _fraction_from_text("action.factor", action_obj["factor"])
    source_obj = obj["source"]
    target_obj = obj["target"]
    if not isinstance(source_obj, list) or not isinstance(target_obj, list):
        raise ScaleActionError("receipt source and target must be lists")
    source = tuple(
        _fraction_from_text(f"source[{index}]", value)
        for index, value in enumerate(source_obj)
    )
    target = tuple(
        _fraction_from_text(f"target[{index}]", value)
        for index, value in enumerate(target_obj)
    )
    rebuilt = build_scale_action_record(weights, factor, source)
    if rebuilt.target != target:
        raise ScaleActionError("receipt target does not match replayed target")
    if rebuilt.receipt_sha256 != obj["receipt_sha256"]:
        raise ScaleActionError("receipt digest does not match replayed application")
    if rebuilt.receipt_bytes() != data:
        raise ScaleActionError("receipt does not replay byte-identically")
    return rebuilt


__all__ = [
    "SCHEMA",
    "VERSION",
    "ScaleActionError",
    "MultiplicativeScaleAction",
    "ScaleActionRecord",
    "build_scale_action",
    "build_scale_action_record",
    "monomial_value",
    "replay_scale_action_record",
]
