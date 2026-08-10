# === MODULE_BUILD ===
# id: ucns_mobius_seed_exact_geometry
#   module_name: mobius_seed_exact
#   module_kind: experiment
#   summary: supplies exact Q(sqrt(3)) arithmetic, planar coordinates, and axial hexagonal centers for the seven-band Möbius Seed of Life candidate
#   owner: Erin Spencer
#   public_surface: MobiusSeedError, Surd3, SeedPlanarPoint, HexCoordinate, ORIGIN_POINT, SQRT3_OVER_2, SQRT3_OVER_6
#   internal_surface: exact scalar coercion and rational manifest helpers
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact construction scalars only
#   admin_only: false
#   tests: tests/test_mobius_seed_exact.py
#   rollout: nonselecting exact arithmetic floor for the primitive-seven construction
#   rollback: remove this module and its tests without changing prior UCNS geometry candidates
#   requires: none
#   since: 2026-08-10
#   unresolved: no source-to-seed placement theorem is claimed beyond the declared standard seven-circle scaffold
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: mobius_seed_exact_geometry_is_closed_and_reversible
#   given: rational-plus-sqrt-three scalars and axial Seed centers are constructed
#   then: arithmetic remains exact, the hex map is deterministic, and every derived unit-circle intersection can be checked without binary64 authority
#   class: correctness
#   since: 2026-08-10
# === END CONTRACTS ===

"""Exact arithmetic used by the Möbius Seed of Life candidate."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import sqrt


class MobiusSeedError(ValueError):
    """Raised when evidence violates the bounded candidate construction."""


def _as_fraction(value: Fraction | int) -> Fraction:
    if isinstance(value, bool):
        raise MobiusSeedError("boolean is not an exact scalar")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    raise MobiusSeedError("exact scalar must be int or Fraction")


def fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True, slots=True)
class Surd3:
    """One exact number ``a + b*sqrt(3)`` with rational coefficients."""

    rational: Fraction = Fraction(0)
    sqrt3: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", _as_fraction(self.rational))
        object.__setattr__(self, "sqrt3", _as_fraction(self.sqrt3))

    def __add__(self, other: Surd3 | Fraction | int) -> Surd3:
        other = other if isinstance(other, Surd3) else Surd3(other)
        return Surd3(self.rational + other.rational, self.sqrt3 + other.sqrt3)

    __radd__ = __add__

    def __sub__(self, other: Surd3 | Fraction | int) -> Surd3:
        other = other if isinstance(other, Surd3) else Surd3(other)
        return Surd3(self.rational - other.rational, self.sqrt3 - other.sqrt3)

    def __rsub__(self, other: Surd3 | Fraction | int) -> Surd3:
        return (other if isinstance(other, Surd3) else Surd3(other)) - self

    def __neg__(self) -> Surd3:
        return Surd3(-self.rational, -self.sqrt3)

    def __mul__(self, other: Surd3 | Fraction | int) -> Surd3:
        other = other if isinstance(other, Surd3) else Surd3(other)
        return Surd3(
            self.rational * other.rational + 3 * self.sqrt3 * other.sqrt3,
            self.rational * other.sqrt3 + self.sqrt3 * other.rational,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: Fraction | int) -> Surd3:
        divisor = _as_fraction(other)
        if divisor == 0:
            raise ZeroDivisionError("exact scalar division by zero")
        return Surd3(self.rational / divisor, self.sqrt3 / divisor)

    @property
    def key(self) -> tuple[str, str]:
        return (fraction_key(self.rational), fraction_key(self.sqrt3))

    def to_float(self) -> float:
        return float(self.rational) + float(self.sqrt3) * sqrt(3.0)

    def manifest(self) -> dict[str, str]:
        return {"rational": self.key[0], "sqrt3": self.key[1]}


@dataclass(frozen=True, slots=True)
class SeedPlanarPoint:
    """Exact planar coordinate over ``Q(sqrt(3))``."""

    x: Surd3
    y: Surd3

    def __post_init__(self) -> None:
        if not isinstance(self.x, Surd3) or not isinstance(self.y, Surd3):
            raise MobiusSeedError("planar coordinates must be exact Surd3 values")

    def __add__(self, other: SeedPlanarPoint) -> SeedPlanarPoint:
        return SeedPlanarPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other: SeedPlanarPoint) -> SeedPlanarPoint:
        return SeedPlanarPoint(self.x - other.x, self.y - other.y)

    def __truediv__(self, scalar: Fraction | int) -> SeedPlanarPoint:
        return SeedPlanarPoint(self.x / scalar, self.y / scalar)

    def scaled(self, scalar: Surd3 | Fraction | int) -> SeedPlanarPoint:
        return SeedPlanarPoint(self.x * scalar, self.y * scalar)

    @property
    def squared_norm(self) -> Surd3:
        return self.x * self.x + self.y * self.y

    def to_float(self) -> tuple[float, float]:
        return (self.x.to_float(), self.y.to_float())

    def manifest(self) -> dict[str, dict[str, str]]:
        return {"x": self.x.manifest(), "y": self.y.manifest()}


@dataclass(frozen=True, slots=True)
class HexCoordinate:
    """Axial coordinate for the one-center-plus-six Seed scaffold."""

    q: int
    r: int

    def __post_init__(self) -> None:
        if isinstance(self.q, bool) or not isinstance(self.q, int):
            raise MobiusSeedError("hex q must be an integer")
        if isinstance(self.r, bool) or not isinstance(self.r, int):
            raise MobiusSeedError("hex r must be an integer")

    @property
    def planar_point(self) -> SeedPlanarPoint:
        return SeedPlanarPoint(
            Surd3(Fraction(self.q) + Fraction(self.r, 2)),
            Surd3(Fraction(0), Fraction(self.r, 2)),
        )

    def distance(self, other: HexCoordinate) -> int:
        dq = self.q - other.q
        dr = self.r - other.r
        ds = -(self.q + self.r) + (other.q + other.r)
        return max(abs(dq), abs(dr), abs(ds))

    def manifest(self) -> dict[str, int]:
        return {"q": self.q, "r": self.r}


ORIGIN_POINT = SeedPlanarPoint(Surd3(), Surd3())
SQRT3_OVER_2 = Surd3(Fraction(0), Fraction(1, 2))
SQRT3_OVER_6 = Surd3(Fraction(0), Fraction(1, 6))
