# === MODULE_BUILD ===
# id: explicit_comparison_policy_layer
#   module_name: comparison
#   module_kind: instrument
#   summary: defines explicit numerical and structural comparison policies so evaluator laws never rely on hidden tolerance
#   owner: Erin Spencer
#   public_surface: ComparisonMode, ComparisonPolicy, ComparisonRegistry, exact_comparison_policy, absolute_comparison_policy, relative_comparison_policy, combined_comparison_policy, ulp_comparison_policy, interval_overlap_policy, custom_comparison_policy
#   internal_surface: _numeric_pair, _ordered_float
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_comparison.py, tests/test_laboratory.py
#   rollout: explicit candidate-research comparison infrastructure only
#   rollback: remove comparison exports and restore no implicit tolerance
#   requires: structural_choice_policy_layer
#   since: 2026-07-21
#   unresolved: canonical numerical comparison policy
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: evaluator_equality_requires_explicit_comparison_policy
#   given: candidate outputs or law evidence are compared
#   then: an explicit named ComparisonPolicy performs the comparison and no hidden tolerance is selected
#   class: doctrine
#   since: 2026-07-21
#
# id: comparison_registry_preserves_multiple_policies
#   given: exact, relative, absolute, ULP, interval, or custom policies are registered
#   then: every policy remains independently addressable and no default winner is appointed
#   class: doctrine
#   since: 2026-07-21
#
# id: comparison_policy_replacement_is_explicit
#   given: a comparison policy name is already registered
#   then: replacement fails unless replace is explicitly true
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from math import isclose, isfinite
from struct import pack, unpack
from typing import Any, Callable


class ComparisonMode(str, Enum):
    EXACT = "exact"
    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    COMBINED = "combined"
    ULP = "ulp"
    INTERVAL_OVERLAP = "interval-overlap"
    CUSTOM = "custom"


Comparator = Callable[[Any, Any], bool]


@dataclass(frozen=True, slots=True)
class ComparisonPolicy:
    name: str
    mode: ComparisonMode
    comparator: Comparator
    version: str
    description: str = ""
    parameters: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.version.strip():
            raise ValueError("comparison policy name and version must be nonempty")
        object.__setattr__(self, "mode", ComparisonMode(self.mode))
        if not callable(self.comparator):
            raise TypeError("comparison policy comparator must be callable")
        object.__setattr__(self, "parameters", tuple(self.parameters))

    def matches(self, left: Any, right: Any) -> bool:
        result = self.comparator(left, right)
        if not isinstance(result, bool):
            raise TypeError("comparison policy must return bool")
        return result


@dataclass(slots=True)
class ComparisonRegistry:
    _policies: dict[str, ComparisonPolicy] = field(default_factory=dict, repr=False)

    def register(self, policy: ComparisonPolicy, *, replace: bool = False) -> None:
        if policy.name in self._policies and not replace:
            raise ValueError(f"comparison policy already registered: {policy.name}")
        self._policies[policy.name] = policy

    def resolve(self, name: str) -> ComparisonPolicy:
        try:
            return self._policies[name]
        except KeyError as exc:
            raise KeyError(f"unknown comparison policy: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(self._policies)


def _numeric_pair(left: Any, right: Any) -> tuple[float, float] | None:
    if isinstance(left, bool) or isinstance(right, bool):
        return None
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return float(left), float(right)
    return None


def exact_comparison_policy(
    *, name: str = "exact", version: str = "1"
) -> ComparisonPolicy:
    def comparator(left: Any, right: Any) -> bool:
        try:
            result = left == right
        except Exception:
            return False
        return result if isinstance(result, bool) else False

    return ComparisonPolicy(
        name, ComparisonMode.EXACT, comparator, version, "exact Python equality"
    )


def absolute_comparison_policy(
    tolerance: float, *, name: str = "absolute", version: str = "1"
) -> ComparisonPolicy:
    tolerance = float(tolerance)
    if not isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("absolute tolerance must be finite and nonnegative")
    exact = exact_comparison_policy()

    def comparator(left: Any, right: Any) -> bool:
        pair = _numeric_pair(left, right)
        return (
            abs(pair[0] - pair[1]) <= tolerance
            if pair
            else exact.matches(left, right)
        )

    return ComparisonPolicy(
        name,
        ComparisonMode.ABSOLUTE,
        comparator,
        version,
        parameters=(("tolerance", repr(tolerance)),),
    )


def relative_comparison_policy(
    tolerance: float, *, name: str = "relative", version: str = "1"
) -> ComparisonPolicy:
    tolerance = float(tolerance)
    if not isfinite(tolerance) or tolerance < 0.0:
        raise ValueError("relative tolerance must be finite and nonnegative")
    exact = exact_comparison_policy()

    def comparator(left: Any, right: Any) -> bool:
        pair = _numeric_pair(left, right)
        if not pair:
            return exact.matches(left, right)
        first, second = pair
        scale = max(abs(first), abs(second))
        return abs(first - second) <= tolerance * scale

    return ComparisonPolicy(
        name,
        ComparisonMode.RELATIVE,
        comparator,
        version,
        parameters=(("tolerance", repr(tolerance)),),
    )


def combined_comparison_policy(
    *,
    rel_tol: float,
    abs_tol: float,
    name: str = "combined",
    version: str = "1",
) -> ComparisonPolicy:
    rel_tol = float(rel_tol)
    abs_tol = float(abs_tol)
    if not all(isfinite(value) and value >= 0.0 for value in (rel_tol, abs_tol)):
        raise ValueError("comparison tolerances must be finite and nonnegative")
    exact = exact_comparison_policy()

    def comparator(left: Any, right: Any) -> bool:
        pair = _numeric_pair(left, right)
        return (
            isclose(pair[0], pair[1], rel_tol=rel_tol, abs_tol=abs_tol)
            if pair
            else exact.matches(left, right)
        )

    return ComparisonPolicy(
        name,
        ComparisonMode.COMBINED,
        comparator,
        version,
        parameters=(("rel_tol", repr(rel_tol)), ("abs_tol", repr(abs_tol))),
    )


def _ordered_float(value: float) -> int:
    bits = unpack(">q", pack(">d", float(value)))[0]
    return 0x8000000000000000 - bits if bits < 0 else bits


def ulp_comparison_policy(
    max_ulps: int,
    *,
    signed_zero_equal: bool = True,
    name: str = "ulp",
    version: str = "1",
) -> ComparisonPolicy:
    if not isinstance(max_ulps, int) or max_ulps < 0:
        raise ValueError("max_ulps must be a nonnegative integer")
    if not isinstance(signed_zero_equal, bool):
        raise TypeError("signed_zero_equal must be bool")
    exact = exact_comparison_policy()

    def comparator(left: Any, right: Any) -> bool:
        pair = _numeric_pair(left, right)
        if not pair:
            return exact.matches(left, right)
        first, second = pair
        if not isfinite(first) or not isfinite(second):
            return first == second
        if signed_zero_equal and first == second:
            return True
        return abs(_ordered_float(first) - _ordered_float(second)) <= max_ulps

    return ComparisonPolicy(
        name,
        ComparisonMode.ULP,
        comparator,
        version,
        parameters=(
            ("max_ulps", str(max_ulps)),
            ("signed_zero_equal", str(signed_zero_equal).lower()),
        ),
    )


def interval_overlap_policy(
    *, name: str = "interval-overlap", version: str = "1"
) -> ComparisonPolicy:
    def interval(value: Any) -> tuple[float, float]:
        if not isinstance(value, (tuple, list)) or len(value) != 2:
            raise TypeError("interval comparison expects two-element intervals")
        lower, upper = float(value[0]), float(value[1])
        if not isfinite(lower) or not isfinite(upper) or lower > upper:
            raise ValueError("invalid interval")
        return lower, upper

    def comparator(left: Any, right: Any) -> bool:
        left_lower, left_upper = interval(left)
        right_lower, right_upper = interval(right)
        return max(left_lower, right_lower) <= min(left_upper, right_upper)

    return ComparisonPolicy(
        name, ComparisonMode.INTERVAL_OVERLAP, comparator, version
    )


def custom_comparison_policy(
    name: str,
    comparator: Comparator,
    *,
    version: str,
    description: str = "",
    parameters: tuple[tuple[str, str], ...] = (),
) -> ComparisonPolicy:
    return ComparisonPolicy(
        name,
        ComparisonMode.CUSTOM,
        comparator,
        version,
        description,
        parameters,
    )
