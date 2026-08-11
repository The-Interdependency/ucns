# === MODULE_BUILD ===
# id: ucns_prime_independent_interval_replay
#   module_name: prime_independent_interval
#   module_kind: experiment
#   summary: provides a FLINT Arb replay of the P7-first continuous separation calculation that is independent of the earlier mpmath.iv kernel
#   owner: Erin Spencer
#   public_surface: ArbReplayReference, ArbReplayPair, ArbReplayCertificate, reference_interval_receipts, replay_pair_with_arb, replay_prime_with_arb
#   internal_surface: exact rational boxes, Arb flat-step interpolation, rigorous lower and upper ball endpoints, deterministic subdivision ledger
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_prime_phase_sensitivity_milnor.py
#   rollout: optional proof replay; python-flint is imported lazily and this module does not convert an unexecuted replay into evidence
#   rollback: remove this module and its tests without changing the established mpmath.iv receipt
#   requires: ucns_prime_smooth_ribbons_p7_p5
#   since: 2026-08-11
#   unresolved: execute full P7 and P5 replay in a python-flint environment, compare margins, archive accepted-leaf ledgers, proof-assistant replay
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: prime_independent_interval_preserves_reference_receipts
#   given: the prior mpmath.iv interval artifact is referenced
#   then: its P7 and P5 ledger hashes, pair counts, thresholds, and minimum lower endpoints are preserved exactly as external evidence rather than recomputed claims
#   class: evidence
#   since: 2026-08-11
#
# id: prime_independent_interval_uses_a_distinct_kernel
#   given: an independent replay is requested
#   then: FLINT Arb ball arithmetic is used rather than mpmath.iv or binary64 endpoint guards
#   class: doctrine
#   since: 2026-08-11
#
# id: prime_independent_interval_covers_complete_pair_tori
#   given: replay_prime_with_arb completes successfully
#   then: every unordered carrier pair has a deterministic accepted-box cover of the full rational parameter square and every outward lower bound exceeds nine hundredths
#   class: correctness
#   since: 2026-08-11
#
# id: prime_independent_interval_does_not_claim_unexecuted_results
#   given: python-flint is unavailable or the full replay has not been run
#   then: the receipt status remains pending and no Arb margin, ledger hash, or certification result is fabricated
#   class: doctrine
#   since: 2026-08-11
# === END CONTRACTS ===

"""Independent FLINT/Arb replay for the smooth P7 and P5 centerlines.

The established interval artifact used ``mpmath.iv``.  This module deliberately
uses the independent FLINT Arb ball-arithmetic kernel.  Importing it does not
require python-flint; the dependency is loaded only when a replay is invoked.

The algorithm covers each parameter torus ``[0,1]^2`` by exact rational boxes.
At every box center it evaluates the smooth lifted centerlines with Arb balls
and subtracts rigorous speed upper bounds times the half box widths.  A leaf is
accepted only when the resulting lower ball is strictly greater than 9/100.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import itertools
from typing import Any, Iterable

from .prime_smooth_ribbons import (
    SmoothPeriodicField,
    SmoothPrimeRibbon,
    build_smooth_prime_five,
    build_smooth_prime_seven,
)

TARGET = Fraction(9, 100)
P7_REFERENCE_LEDGER_SHA256 = "bd47e350974f5bd483f223e93891d13ea797f03215f76223ca165e8941e96b04"
P5_REFERENCE_LEDGER_SHA256 = "977fd5042549635d47e56201095bda7f4b309720ae1f10670b235d8c3f445979"
P7_REFERENCE_MINIMUM = (
    "0.0900051500007549740920351063114207391872401600828304981190671962364227063227389015334"
)
P5_REFERENCE_MINIMUM = (
    "0.09000862353879262596261062584061589120675653732999479434582033467343400987575583438023"
)


class IndependentIntervalError(RuntimeError):
    """Raised when the optional independent replay cannot issue a certificate."""


@dataclass(frozen=True, slots=True)
class ArbReplayReference:
    prime: int
    backend: str
    pair_count: int
    target: Fraction
    minimum_outward_lower_endpoint: str
    accepted_leaf_ledger_sha256: str
    standing: str = "prior-mpmath-iv-reference-only"

    def as_dict(self) -> dict[str, object]:
        return {
            "prime": self.prime,
            "backend": self.backend,
            "pair_count": self.pair_count,
            "target": _fraction_text(self.target),
            "minimum_outward_lower_endpoint": self.minimum_outward_lower_endpoint,
            "accepted_leaf_ledger_sha256": self.accepted_leaf_ledger_sha256,
            "standing": self.standing,
        }


@dataclass(frozen=True, slots=True)
class RationalBox:
    t0: Fraction
    t1: Fraction
    s0: Fraction
    s1: Fraction
    depth: int = 0

    def __post_init__(self) -> None:
        if not (self.t0 < self.t1 and self.s0 < self.s1):
            raise IndependentIntervalError("parameter box must have positive area")
        if self.depth < 0:
            raise IndependentIntervalError("box depth cannot be negative")

    @property
    def t_mid(self) -> Fraction:
        return (self.t0 + self.t1) / 2

    @property
    def s_mid(self) -> Fraction:
        return (self.s0 + self.s1) / 2

    @property
    def t_radius(self) -> Fraction:
        return (self.t1 - self.t0) / 2

    @property
    def s_radius(self) -> Fraction:
        return (self.s1 - self.s0) / 2

    def split_t(self) -> tuple["RationalBox", "RationalBox"]:
        middle = self.t_mid
        return (
            RationalBox(self.t0, middle, self.s0, self.s1, self.depth + 1),
            RationalBox(middle, self.t1, self.s0, self.s1, self.depth + 1),
        )

    def split_s(self) -> tuple["RationalBox", "RationalBox"]:
        middle = self.s_mid
        return (
            RationalBox(self.t0, self.t1, self.s0, middle, self.depth + 1),
            RationalBox(self.t0, self.t1, middle, self.s1, self.depth + 1),
        )

    def ledger_prefix(self) -> str:
        return "|".join(
            (
                _fraction_text(self.t0),
                _fraction_text(self.t1),
                _fraction_text(self.s0),
                _fraction_text(self.s1),
                str(self.depth),
            )
        )


@dataclass(frozen=True, slots=True)
class ArbReplayPair:
    pair_id: str
    accepted_leaf_boxes: int
    boxes_evaluated: int
    maximum_depth: int
    minimum_outward_lower_endpoint: str
    accepted_leaf_ledger_sha256: str
    certified: bool

    def as_dict(self) -> dict[str, object]:
        return {
            "pair_id": self.pair_id,
            "accepted_leaf_boxes": self.accepted_leaf_boxes,
            "boxes_evaluated": self.boxes_evaluated,
            "maximum_depth": self.maximum_depth,
            "minimum_outward_lower_endpoint": self.minimum_outward_lower_endpoint,
            "accepted_leaf_ledger_sha256": self.accepted_leaf_ledger_sha256,
            "certified": self.certified,
        }


@dataclass(frozen=True, slots=True)
class ArbReplayCertificate:
    prime: int
    backend: str
    precision_bits: int
    target: Fraction
    pairs: tuple[ArbReplayPair, ...]
    reference: ArbReplayReference

    @property
    def all_pairs_certified(self) -> bool:
        return bool(self.pairs) and all(item.certified for item in self.pairs)

    @property
    def minimum_outward_lower_endpoint(self) -> str:
        return min(
            (item.minimum_outward_lower_endpoint for item in self.pairs),
            key=lambda value: Fraction(value),
        )

    @property
    def global_accepted_leaf_ledger_sha256(self) -> str:
        digest = hashlib.sha256()
        for item in self.pairs:
            digest.update(
                f"{item.pair_id}|{item.accepted_leaf_ledger_sha256}\n".encode("utf-8")
            )
        return digest.hexdigest()

    def as_dict(self) -> dict[str, object]:
        return {
            "prime": self.prime,
            "backend": self.backend,
            "precision_bits": self.precision_bits,
            "target": _fraction_text(self.target),
            "all_pairs_certified": self.all_pairs_certified,
            "minimum_outward_lower_endpoint": self.minimum_outward_lower_endpoint,
            "global_accepted_leaf_ledger_sha256": self.global_accepted_leaf_ledger_sha256,
            "pair_replays": [item.as_dict() for item in self.pairs],
            "reference_receipt": self.reference.as_dict(),
            "comparison_standing": (
                "independent-kernel result; leaf hashes need not equal the mpmath.iv "
                "hashes because Arb enclosures can change the subdivision tree"
            ),
        }


def _fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def reference_interval_receipts() -> tuple[ArbReplayReference, ArbReplayReference]:
    """Return the frozen, externally produced mpmath.iv receipt identities."""

    return (
        ArbReplayReference(
            prime=7,
            backend="mpmath.iv 1.3.0 at 80 decimal digits",
            pair_count=21,
            target=TARGET,
            minimum_outward_lower_endpoint=P7_REFERENCE_MINIMUM,
            accepted_leaf_ledger_sha256=P7_REFERENCE_LEDGER_SHA256,
        ),
        ArbReplayReference(
            prime=5,
            backend="mpmath.iv 1.3.0 at 80 decimal digits",
            pair_count=10,
            target=TARGET,
            minimum_outward_lower_endpoint=P5_REFERENCE_MINIMUM,
            accepted_leaf_ledger_sha256=P5_REFERENCE_LEDGER_SHA256,
        ),
    )


def independent_replay_plan() -> dict[str, object]:
    """Return a nonclaiming plan when the optional Arb replay has not run."""

    return {
        "status": "pending-execution",
        "required_backend": "python-flint / FLINT Arb ball arithmetic",
        "reference_receipts": [item.as_dict() for item in reference_interval_receipts()],
        "acceptance": [
            "cover every unordered carrier-pair parameter torus",
            "use exact rational subdivision boxes",
            "accept every leaf only when the Arb lower ball is strictly greater than 9/100",
            "archive pair and global accepted-leaf ledgers",
            "report any disagreement instead of selecting the preferred kernel",
        ],
        "nonclaim": "no independent Arb result exists until replay_prime_with_arb returns successfully",
    }


def _load_arb() -> tuple[Any, Any]:
    try:
        from flint import arb, ctx  # type: ignore[import-not-found]
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise IndependentIntervalError(
            "python-flint is required for the independent Arb replay"
        ) from exc
    return arb, ctx


def _arb_fraction(arb: Any, value: Fraction) -> Any:
    return arb(_fraction_text(value))


def _arb_flat_step(arb: Any, value: Any) -> Any:
    """Evaluate the flat C-infinity step with Arb balls."""

    zero, one = arb(0), arb(1)
    if value == zero:
        return zero
    if value == one:
        return one
    left = (-one / value).exp()
    right = (-one / (one - value)).exp()
    return left / (left + right)


def _field_value_arb(arb: Any, field: SmoothPeriodicField, turn: Fraction) -> Any:
    target = turn % 1
    for index, segment in enumerate(field.segments):
        adjusted = target
        if index == len(field.segments) - 1 and adjusted < segment.left_turn:
            adjusted += 1
        if segment.left_turn <= adjusted <= segment.right_turn:
            if adjusted == segment.left_turn:
                return _arb_fraction(arb, segment.left_value)
            if adjusted == segment.right_turn:
                return _arb_fraction(arb, segment.right_value)
            local = (adjusted - segment.left_turn) / segment.turn_width
            return _arb_fraction(arb, segment.left_value) + _arb_fraction(
                arb, segment.right_value - segment.left_value
            ) * _arb_flat_step(arb, _arb_fraction(arb, local))
    raise IndependentIntervalError(f"no smooth segment contains {turn} on {field.carrier}")


def _exact_center_arb(arb: Any, prime: int, carrier: str) -> tuple[Any, Any]:
    zero, one, half = arb(0), arb(1), arb("1/2")
    if carrier == "C":
        return zero, zero
    index = int(carrier[1:])
    if prime == 7:
        root3_over2 = arb(3).sqrt() / 2
        centers = (
            (one, zero),
            (half, root3_over2),
            (-half, root3_over2),
            (-one, zero),
            (-half, -root3_over2),
            (half, -root3_over2),
        )
        return centers[index]
    if prime == 5:
        centers = ((one, zero), (zero, one), (-one, zero), (zero, -one))
        return centers[index]
    raise IndependentIntervalError("only P7 and P5 are supported")


def _centerline_point_arb(
    arb: Any,
    ribbon: SmoothPrimeRibbon,
    carrier: str,
    turn: Fraction,
) -> tuple[Any, Any, Any]:
    angle = _arb_fraction(arb, 2 * turn)
    sine, cosine = angle.sin_cos_pi()
    center_x, center_y = _exact_center_arb(arb, ribbon.prime, carrier)
    height = _field_value_arb(arb, ribbon.field(carrier), turn)
    return center_x + cosine, center_y + sine, height


def _speed_upper_arb(arb: Any, ribbon: SmoothPrimeRibbon, carrier: str) -> Any:
    derivative = _arb_fraction(arb, ribbon.field(carrier).maximum_derivative_bound)
    return ((2 * arb.pi()) ** 2 + derivative**2).sqrt().upper()


def _box_lower_bound_arb(
    arb: Any,
    ribbon: SmoothPrimeRibbon,
    left: str,
    right: str,
    box: RationalBox,
    left_speed: Any,
    right_speed: Any,
) -> Any:
    left_point = _centerline_point_arb(arb, ribbon, left, box.t_mid)
    right_point = _centerline_point_arb(arb, ribbon, right, box.s_mid)
    distance = sum((a - b) ** 2 for a, b in zip(left_point, right_point)).sqrt()
    lower = distance.lower()
    lower -= left_speed * _arb_fraction(arb, box.t_radius)
    lower -= right_speed * _arb_fraction(arb, box.s_radius)
    return lower.lower()


def replay_pair_with_arb(
    ribbon: SmoothPrimeRibbon,
    left: str,
    right: str,
    *,
    precision_bits: int = 256,
    maximum_depth: int = 32,
    maximum_boxes: int = 250_000,
) -> ArbReplayPair:
    """Certify one complete pair-parameter torus using FLINT Arb.

    The return value is evidence only when this function has actually completed.
    """

    if left == right or left not in ribbon.carriers or right not in ribbon.carriers:
        raise IndependentIntervalError("replay requires two distinct known carriers")
    if precision_bits < 128 or maximum_depth < 1 or maximum_boxes < 1:
        raise IndependentIntervalError("invalid replay resource boundary")

    arb, ctx = _load_arb()
    previous_precision = ctx.prec
    ctx.prec = precision_bits
    try:
        target_ball = _arb_fraction(arb, TARGET)
        left_speed = _speed_upper_arb(arb, ribbon, left)
        right_speed = _speed_upper_arb(arb, ribbon, right)
        pending = [RationalBox(Fraction(0), Fraction(1), Fraction(0), Fraction(1))]
        accepted: list[tuple[RationalBox, str]] = []
        boxes_evaluated = 0
        observed_depth = 0

        while pending:
            box = pending.pop()
            boxes_evaluated += 1
            if boxes_evaluated > maximum_boxes:
                raise IndependentIntervalError(
                    f"box budget exceeded for {left}::{right}"
                )
            observed_depth = max(observed_depth, box.depth)
            lower = _box_lower_bound_arb(
                arb, ribbon, left, right, box, left_speed, right_speed
            )
            if lower > target_ball:
                accepted.append((box, lower.str(80)))
                continue
            if box.depth >= maximum_depth:
                raise IndependentIntervalError(
                    f"depth boundary reached without proving {left}::{right}"
                )
            t_contribution = left_speed * _arb_fraction(arb, box.t_radius)
            s_contribution = right_speed * _arb_fraction(arb, box.s_radius)
            children = box.split_t() if t_contribution >= s_contribution else box.split_s()
            pending.extend(reversed(children))

        digest = hashlib.sha256()
        for box, lower_text in accepted:
            digest.update(f"{box.ledger_prefix()}|{lower_text}\n".encode("utf-8"))
        minimum = min((text for _, text in accepted), key=lambda text: Fraction(text))
        return ArbReplayPair(
            pair_id=f"{left}::{right}",
            accepted_leaf_boxes=len(accepted),
            boxes_evaluated=boxes_evaluated,
            maximum_depth=observed_depth,
            minimum_outward_lower_endpoint=minimum,
            accepted_leaf_ledger_sha256=digest.hexdigest(),
            certified=True,
        )
    finally:
        ctx.prec = previous_precision


def replay_prime_with_arb(
    prime: int,
    *,
    precision_bits: int = 256,
    maximum_depth: int = 32,
    maximum_boxes_per_pair: int = 250_000,
) -> ArbReplayCertificate:
    """Replay every P7 or P5 carrier pair with the independent Arb kernel."""

    if prime == 7:
        ribbon = build_smooth_prime_seven()
        reference = reference_interval_receipts()[0]
    elif prime == 5:
        ribbon = build_smooth_prime_five()
        reference = reference_interval_receipts()[1]
    else:
        raise IndependentIntervalError("only P7 and P5 are supported")

    pairs = tuple(
        replay_pair_with_arb(
            ribbon,
            left,
            right,
            precision_bits=precision_bits,
            maximum_depth=maximum_depth,
            maximum_boxes=maximum_boxes_per_pair,
        )
        for left, right in itertools.combinations(ribbon.carriers, 2)
    )
    certificate = ArbReplayCertificate(
        prime=prime,
        backend="FLINT Arb via python-flint",
        precision_bits=precision_bits,
        target=TARGET,
        pairs=pairs,
        reference=reference,
    )
    if len(pairs) != reference.pair_count or not certificate.all_pairs_certified:
        raise IndependentIntervalError("independent replay did not close every pair")
    return certificate
