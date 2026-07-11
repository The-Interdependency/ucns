"""
ucns.catalogue
========================
Catalogue builders for :meth:`UCNSStore.factor_decompose`.

Two builders are provided:

``build_catalogue_d1``
    The canonical depth-1 oracle atoms (excluding None).  This is the
    carrier-grid family named by ``ORACLE_CATALOGUE_RULE_VERSION``; it is
    deliberately narrower than every flat object satisfying the frozen
    geometric bounds.

``build_catalogue_d2_oracle``
    Depth-2 oracle-class objects built from a caller-supplied payload
    basis. Full enumeration is ``|basis|^length`` per host combination,
    so callers should restrict the basis when appropriate.

Both functions return plain lists of ``UCNSObject`` values suitable for
passing to :meth:`UCNSStore.factor_decompose`.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_catalogue
#   module_name: catalogue
#   module_kind: engine
#   summary: Catalogue builders enumerating canonical depth-1 oracle atoms and depth-2 oracle-class UCNSObjects for factor decomposition.
#   owner: Erin Spencer
#   public_surface: build_catalogue_d1, build_catalogue_d2_oracle
#   internal_surface: _obj_key
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_catalogue, tests.test_oracle_catalogue_equivalence
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domains
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

import itertools
from fractions import Fraction
from typing import List, Optional

from .canonical import UCNSObject
from .domains import (
    A_PLUS_MAX,
    N_MIN_MAX,
    generate_payload_catalogue,
    is_in_oracle_class,
)

__all__ = ["build_catalogue_d1", "build_catalogue_d2_oracle"]



def build_catalogue_d1() -> List[UCNSObject]:
    """Return canonical oracle atoms, excluding the unit payload.

    Membership is exactly the non-``None`` portion of
    :func:`ucns.domains.generate_payload_catalogue`.
    """
    return [obj for obj in generate_payload_catalogue() if obj is not None]



def build_catalogue_d2_oracle(
    payload_basis: Optional[List[Optional[UCNSObject]]] = None,
) -> List[UCNSObject]:
    """Return depth-2 oracle-class objects built from *payload_basis*.

    If *payload_basis* is ``None``, the canonical oracle catalogue is
    used.  At least one cell payload must be non-unit so every returned
    object has depth exactly two.  Candidates outside the exact oracle
    class are rejected rather than admitted by geometric bounds alone.
    """
    if payload_basis is None:
        payload_basis = generate_payload_catalogue()

    objects: List[UCNSObject] = []
    seen = set()

    for n_min in range(1, N_MIN_MAX + 1):
        for length in range(1, A_PLUS_MAX + 1):
            angles = [Fraction(2 * k, n_min) for k in range(length)]
            for face_bits in range(2 ** length):
                faces = [(face_bits >> i) & 1 for i in range(length)]
                for payloads in itertools.product(payload_basis, repeat=length):
                    if all(payload is None for payload in payloads):
                        continue
                    try:
                        obj = UCNSObject(
                            n_dec=n_min * 2,
                            n_min=n_min,
                            A_plus=list(zip(angles, payloads)),
                            F_plus=faces,
                        )
                    except ValueError:
                        continue
                    if not is_in_oracle_class(obj):
                        continue
                    key = _obj_key(obj)
                    if key in seen:
                        continue
                    seen.add(key)
                    objects.append(obj)

    return objects



def _obj_key(obj: UCNSObject) -> tuple:
    """Structural deduplication key, recursive to depth two."""
    return (
        obj.n_min,
        tuple(obj.F_plus),
        tuple(
            (angle, _obj_key(payload) if payload is not None else None)
            for angle, payload in obj.A_plus
        ),
    )
