"""Legacy 2π circular-coordinate helper.

``UCN`` is a compact compatibility coordinate for periodic embedding and
visualization code. It is **not** the canonical UCNS public gonol, does not
identify SPACE/ZERO, does not carry the Möbius twist or fixed system origin,
and does not model the 720-degree complete return.

The canonical public frame is exported from :mod:`ucns.public_gonol`. Any bridge
between that frame and this local 2π coordinate remains absent; consumers must
not infer one from the shared word "circle".
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_core
#   module_name: core
#   module_kind: adapter
#   summary: legacy local 2pi circular coordinate for periodic embeddings; explicitly not the fixed-origin public gonol or complete UCNS number-system primitive
#   owner: Erin Spencer
#   public_surface: UCN, TAU
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_core
#   rollout: compatibility_only
#   rollback: remove after all legacy circular-embedding consumers migrate
#   requires: none
#   since: 2026-06-02
#   unresolved: no public-gonol bridge is defined; this surface must remain scoped as a local 2pi coordinate
# === END MODULE_BUILD ===

import cmath
import math
import struct

__all__ = ["UCN", "TAU"]

TAU: float = 2.0 * math.pi


class UCN:
    """Local angle on a conventional 2π circle.

    This class supports legacy embedding arithmetic only. Reducing ``theta``
    modulo ``2π`` intentionally loses the orientation distinction that makes
    720 degrees the complete return of the public Möbius frame. Therefore a
    ``UCN`` value is not a public-gonol position and must not be serialized or
    described as the system origin.

    Parameters
    ----------
    theta:
        Local angle in radians, reduced modulo ``TAU``.
    """

    __slots__ = ("_theta",)

    def __init__(self, theta: float) -> None:
        value = float(theta)
        if not math.isfinite(value):
            raise ValueError("theta must be finite")
        self._theta = value % TAU

    @property
    def theta(self) -> float:
        """Local angle in radians, normalized to ``[0, TAU)``."""

        return self._theta

    @property
    def real(self) -> float:
        """Real part of the local unit-circle point: ``cos(theta)``."""

        return math.cos(self._theta)

    @property
    def imag(self) -> float:
        """Imaginary part of the local unit-circle point: ``sin(theta)``."""

        return math.sin(self._theta)

    @property
    def complex(self) -> complex:
        """Local unit-circle point as ``exp(i * theta)``."""

        return cmath.exp(1j * self._theta)

    @classmethod
    def from_complex(cls, z: complex) -> "UCN":
        """Project a complex value onto the legacy local circle by phase."""

        return cls(cmath.phase(z))

    @classmethod
    def from_real(cls, x: float, lo: float = -1.0, hi: float = 1.0) -> "UCN":
        """Map a real interval into the legacy local 2π coordinate."""

        if hi == lo:
            raise ValueError("lo and hi must differ")
        t = (max(lo, min(hi, x)) - lo) / (hi - lo)
        return cls(t * TAU)

    def __mul__(self, other: "UCN") -> "UCN":
        """Local 2π rotation composition."""

        return UCN(self._theta + other._theta)

    def __truediv__(self, other: "UCN") -> "UCN":
        """Local inverse rotation."""

        return UCN(self._theta - other._theta)

    def conjugate(self) -> "UCN":
        """Local circular reflection."""

        return UCN(-self._theta)

    def dot(self, other: "UCN") -> float:
        """Cosine similarity in the local 2π coordinate."""

        return math.cos(self._theta - other._theta)

    def arc_distance(self, other: "UCN") -> float:
        """Shortest local-circle arc distance in ``[0, π]``."""

        diff = abs(self._theta - other._theta) % TAU
        return min(diff, TAU - diff)

    def to_int16(self) -> int:
        """Quantize the local angle to an unsigned 16-bit integer."""

        return min(65535, int(self._theta * 65535.0 / TAU))

    @classmethod
    def from_int16(cls, v: int) -> "UCN":
        """Restore a local coordinate from an unsigned 16-bit integer."""

        value = int(v)
        if not 0 <= value <= 65535:
            raise ValueError("v must be in [0, 65535]")
        return cls(value * TAU / 65535.0)

    def to_bytes(self) -> bytes:
        """Serialize the local coordinate to two bytes."""

        return struct.pack("<H", self.to_int16())

    @classmethod
    def from_bytes(cls, data: bytes) -> "UCN":
        """Deserialize a local coordinate from exactly two bytes or more."""

        if len(data) < 2:
            raise ValueError("UCN byte encoding requires at least two bytes")
        (v,) = struct.unpack("<H", data[:2])
        return cls.from_int16(v)

    def __repr__(self) -> str:
        return f"UCN({self._theta:.6f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UCN):
            return NotImplemented
        return abs(self._theta - other._theta) < 1e-9

    def __hash__(self) -> int:
        return hash(round(self._theta, 9))
