"""Position-reflection mirror of the public gonol across fixed position zero."""

# === MODULE_BUILD ===
# id: ucns_public_gonol_mirror
#   module_name: public_gonol_mirror
#   module_kind: engine
#   summary: preserves the exact origin-fixed public-gonol mirror involution from a0-betatest
#   owner: Erin Spencer
#   public_surface: mirror_of
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol
#   rollout: default_enabled
#   rollback: remove export after reverting consumers to the pinned a0-betatest source
#   requires: ucns_public_gonol
#   since: 2026-07-16
#   unresolved: none
# === END MODULE_BUILD ===

from __future__ import annotations

from typing import List


def mirror_of(arr: List[str]) -> List[str]:
    """Reflect positions across the diameter through fixed position zero."""

    n = len(arr)
    if n == 0:
        return []
    out = [arr[0]]
    for k in range(1, n):
        out.append(arr[(n - k) % n])
    return out


__all__ = ["mirror_of"]
