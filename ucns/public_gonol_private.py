"""Origin-preserving private transformations of the canonical public gonol.

This is the exact A0 fixed-origin rule separated from the ZFAE application:
position zero is never rotated or permuted; phase and permutation operate only
on the 156 nonzero positions.
"""

# === MODULE_BUILD ===
# id: ucns_public_gonol_private
#   module_name: public_gonol_private
#   module_kind: engine
#   summary: preserves the exact A0 private phase and permutation law that fixes the public SPACE/ZERO twist origin
#   owner: Erin Spencer
#   public_surface: PrivateGonal
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol
#   rollout: default_enabled
#   rollback: remove export after reverting consumers to the pinned a0-betatest source
#   requires: ucns_public_gonol, ucns_public_gonol_faces
#   since: 2026-07-16
#   unresolved: none
# === END MODULE_BUILD ===

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

from .public_gonol import PUBLIC_GONOL_157
from .public_gonol_faces import ARITY, ORIGIN


@dataclass(frozen=True)
class PrivateGonal:
    """Canonical public gonol with a private nonzero-ring transform.

    The arrangement is not a private degree of freedom. It must be the exact
    UCNS public gonol. Secrecy lives only in ``phase`` and ``perm`` over
    positions ``1..156``; position zero remains SPACE/ZERO.
    """

    arrangement: Tuple[str, ...]
    phase: int
    perm: Tuple[int, ...]

    def __post_init__(self) -> None:
        if tuple(self.arrangement) != PUBLIC_GONOL_157:
            raise ValueError("PrivateGonal arrangement must equal the canonical public gonol")
        if len(self.arrangement) != ARITY or self.arrangement[ORIGIN] != " ":
            raise ValueError("PrivateGonal lost the fixed SPACE/ZERO origin")
        if not isinstance(self.phase, int) or isinstance(self.phase, bool):
            raise TypeError("PrivateGonal phase must be an integer")
        if not 0 <= self.phase < ARITY - 1:
            raise ValueError("PrivateGonal phase must be in [0, 155]")
        if len(self.perm) != ARITY:
            raise ValueError("PrivateGonal permutation must contain 157 positions")
        if self.perm[ORIGIN] != ORIGIN:
            raise ValueError("PrivateGonal permutation must fix SPACE/ZERO at position 0")
        if set(self.perm[1:]) != set(range(1, ARITY)):
            raise ValueError("PrivateGonal permutation must biject positions 1..156")

    @property
    def n(self) -> int:
        return len(self.arrangement)

    @classmethod
    def from_seed(
        cls, seed_bytes: bytes, arrangement: Optional[List[str]] = None
    ) -> "PrivateGonal":
        """Derive the exact A0 transform while keeping position zero fixed.

        ``arrangement`` is retained only as a compatibility argument. When
        supplied, it must equal the canonical public arrangement exactly.
        """

        if not isinstance(seed_bytes, bytes):
            raise TypeError("seed_bytes must be bytes")
        arr = PUBLIC_GONOL_157 if arrangement is None else tuple(arrangement)
        if arr != PUBLIC_GONOL_157:
            raise ValueError("custom PrivateGonal arrangements are not public-gonol canon")

        phase = int.from_bytes(
            hashlib.blake2b(seed_bytes + b"::phase", digest_size=8).digest(), "big"
        ) % (ARITY - 1)
        perm = list(range(ARITY))
        state = hashlib.blake2b(seed_bytes + b"::perm", digest_size=8).digest()
        for i in range(ARITY - 1, 1, -1):
            state = hashlib.blake2b(state, digest_size=8).digest()
            j = 1 + int.from_bytes(state, "big") % i
            perm[i], perm[j] = perm[j], perm[i]
        return cls(arrangement=arr, phase=phase, perm=tuple(perm))

    def advance(self, public: int, pcea_digest: str) -> "PrivateGonal":
        """Advance only the nonzero ring; position zero remains fixed."""

        digest = hashlib.blake2b(
            "{}:{}:{}".format(self.phase, int(public), pcea_digest).encode("utf-8"),
            digest_size=8,
        ).digest()
        new_phase = (self.phase + int.from_bytes(digest, "big")) % (ARITY - 1)
        return PrivateGonal(
            arrangement=self.arrangement,
            phase=new_phase,
            perm=self.perm,
        )

    def inscribe(self, angle: float) -> int:
        """Apply the exact A0 continuous-inscription application transform.

        This method is an A0 compatibility surface, not the definition of the
        public-gonol origin or a bridge into normalized ``UCNSObject`` angles.
        """

        value = float(angle)
        if not math.isfinite(value):
            raise ValueError("inscription angle must be finite")
        frac = (value / (2.0 * math.pi)) % 1.0
        base = int(frac * ARITY) % ARITY
        if base == ORIGIN:
            return self.perm[ORIGIN]
        rotated = ((base - 1 + self.phase) % (ARITY - 1)) + 1
        return self.perm[rotated]

    def char_at(self, vertex_idx: int) -> str:
        return self.arrangement[vertex_idx % ARITY]


__all__ = ["PrivateGonal"]
