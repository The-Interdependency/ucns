"""
ucns.core
=========
Unit Circle Number (UCN) – the fundamental numeric primitive.

Every UCN is an angle θ ∈ [0, 2π) that identifies a point on the unit circle
e^(iθ) ∈ ℂ.  Because |e^(iθ)| = 1 for all θ, the set of all UCNs forms a
compact abelian group under multiplication (rotation), making them a natural
substrate for periodic / cyclic data and for efficient angular embeddings.

Key properties
--------------
* **Closure**: multiplying two UCNs (adding angles) always stays on the unit
  circle.
* **Compact storage**: an angle fits in a 16-bit integer (65 536 steps vs 32
  bits for a single-precision float).
* **Fast inner product**: dot(u, v) = cos(θ_u − θ_v) – no square root needed.
* **No external dependencies**: pure Python / math stdlib only.
"""

from __future__ import annotations

import math
import cmath
import struct

__all__ = ["UCN", "TAU"]

TAU: float = 2.0 * math.pi  # full turn = τ


class UCN:
    """Unit Circle Number – a real number encoded as an angle on the unit circle.

    Parameters
    ----------
    theta:
        Angle in radians.  Automatically reduced modulo τ = 2π so that
        ``self.theta`` is always in ``[0, τ)``.
    """

    __slots__ = ("_theta",)

    def __init__(self, theta: float) -> None:
        self._theta: float = float(theta) % TAU

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def theta(self) -> float:
        """Angle in radians, normalised to ``[0, τ)``."""
        return self._theta

    @property
    def real(self) -> float:
        """Real part of the corresponding unit-circle point: cos θ."""
        return math.cos(self._theta)

    @property
    def imag(self) -> float:
        """Imaginary part of the corresponding unit-circle point: sin θ."""
        return math.sin(self._theta)

    @property
    def complex(self) -> complex:
        """The unit-circle point as a Python ``complex``: e^(iθ)."""
        return cmath.exp(1j * self._theta)

    # ------------------------------------------------------------------
    # Constructors
    # ------------------------------------------------------------------

    @classmethod
    def from_complex(cls, z: complex) -> "UCN":
        """Project any complex number *z* onto the unit circle (keep phase)."""
        return cls(cmath.phase(z))

    @classmethod
    def from_real(cls, x: float, lo: float = -1.0, hi: float = 1.0) -> "UCN":
        """Map a real number *x* ∈ [lo, hi] uniformly onto [0, τ).

        Values outside ``[lo, hi]`` are clamped before mapping.
        """
        if hi == lo:
            raise ValueError("lo and hi must differ")
        t = (max(lo, min(hi, x)) - lo) / (hi - lo)  # ∈ [0, 1]
        return cls(t * TAU)

    # ------------------------------------------------------------------
    # Group arithmetic  (unit circle = ℝ/τℤ)
    # ------------------------------------------------------------------

    def __mul__(self, other: "UCN") -> "UCN":
        """Rotation: θ₁ ⊗ θ₂ ≡ θ₁ + θ₂  (mod τ)."""
        return UCN(self._theta + other._theta)

    def __truediv__(self, other: "UCN") -> "UCN":
        """Inverse rotation: θ₁ ⊘ θ₂ ≡ θ₁ − θ₂  (mod τ)."""
        return UCN(self._theta - other._theta)

    def conjugate(self) -> "UCN":
        """Conjugate (reflection): θ* ≡ −θ  (mod τ)."""
        return UCN(-self._theta)

    # ------------------------------------------------------------------
    # Metric / similarity
    # ------------------------------------------------------------------

    def dot(self, other: "UCN") -> float:
        """Angular inner product: cos(θ_self − θ_other) ∈ [−1, 1]."""
        return math.cos(self._theta - other._theta)

    def arc_distance(self, other: "UCN") -> float:
        """Geodesic (arc-length) distance on the unit circle ∈ [0, π]."""
        diff = abs(self._theta - other._theta) % TAU
        return min(diff, TAU - diff)

    # ------------------------------------------------------------------
    # Compact serialisation
    # ------------------------------------------------------------------

    def to_int16(self) -> int:
        """Quantise angle to an unsigned 16-bit integer (0 … 65 535).

        Provides ~0.0001 rad (≈ 0.006°) angular resolution with only 2 bytes.
        """
        return min(65535, int(self._theta * 65535.0 / TAU))

    @classmethod
    def from_int16(cls, v: int) -> "UCN":
        """Restore a UCN from a 16-bit quantised integer."""
        return cls(int(v) * TAU / 65535.0)

    def to_bytes(self) -> bytes:
        """Serialise to 2 bytes (little-endian unsigned short)."""
        return struct.pack("<H", self.to_int16())

    @classmethod
    def from_bytes(cls, data: bytes) -> "UCN":
        """Deserialise from 2 bytes."""
        (v,) = struct.unpack("<H", data[:2])
        return cls.from_int16(v)

    # ------------------------------------------------------------------
    # Dunder helpers
    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"UCN({self._theta:.6f})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, UCN):
            return NotImplemented
        return abs(self._theta - other._theta) < 1e-9

    def __hash__(self) -> int:
        return hash(round(self._theta, 9))

    def __float__(self) -> float:
        return self._theta

    def __lt__(self, other: "UCN") -> bool:
        return self._theta < other._theta
