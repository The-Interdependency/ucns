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

from .public_gonol import get_default


@dataclass(frozen=True)
class PrivateGonal:
    """Public gonol with deterministic private nonzero-ring phase/permutation."""

    arrangement: Tuple[str, ...]
    phase: int
    perm: Tuple[int, ...]

    @property
    def n(self) -> int:
        return len(self.arrangement)

    @classmethod
    def from_seed(
        cls, seed_bytes: bytes, arrangement: Optional[List[str]] = None
    ) -> "PrivateGonal":
        """Derive a transform while keeping position zero fixed."""

        arr = tuple(arrangement) if arrangement is not None else tuple(get_default())
        n = len(arr)
        phase = int.from_bytes(
            hashlib.blake2b(seed_bytes + b"::phase", digest_size=8).digest(), "big"
        ) % (n - 1)
        perm = list(range(n))
        state = hashlib.blake2b(seed_bytes + b"::perm", digest_size=8).digest()
        for i in range(n - 1, 1, -1):
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
        new_phase = (self.phase + int.from_bytes(digest, "big")) % (self.n - 1)
        return PrivateGonal(
            arrangement=self.arrangement,
            phase=new_phase,
            perm=self.perm,
        )

    def inscribe(self, angle: float) -> int:
        """Apply the exact A0 continuous-inscription transform."""

        frac = (float(angle) / (2.0 * math.pi)) % 1.0
        base = int(frac * self.n) % self.n
        if base == 0:
            return self.perm[0]
        rotated = ((base - 1 + self.phase) % (self.n - 1)) + 1
        return self.perm[rotated]

    def char_at(self, vertex_idx: int) -> str:
        return self.arrangement[vertex_idx % self.n]


__all__ = ["PrivateGonal"]
