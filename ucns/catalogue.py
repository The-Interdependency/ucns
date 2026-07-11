"""
ucns.catalogue
========================
Catalogue builders for :meth:`UCNSStore.factor_decompose`.

Two builders are provided:

``build_catalogue_d1``
    All depth-1 UCNSObjects within the frozen domain D' — i.e. every
    oracle atom (excluding None).  Exhaustive and bounded (the domain
    parameters cap the count to a few hundred objects at most).
    Use this as the catalogue argument when the left factor of a
    target product is known to be depth-1.

``build_catalogue_d2_oracle``
    Depth-2 oracle-class objects built from a caller-supplied payload
    basis.  Full enumeration over all payload assignments is
    ``|basis|^length`` per ``(n_min, length, face_bits)`` combination,
    so callers must restrict the basis when the full depth-1 catalogue
    is too large.  The default (full depth-1 catalogue) is correct but
    may be slow for ``length=3`` — benchmark before use in production
    corpora.

Both functions return plain lists of ``UCNSObject``s suitable for
passing directly to :meth:`UCNSStore.factor_decompose` as the
``catalogue`` argument.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_catalogue
#   module_name: catalogue
#   module_kind: engine
#   summary: Catalogue builders enumerating depth-1 and depth-2 oracle-class UCNSObjects for use as factor_decompose payload catalogues.
#   owner: Erin Spencer
#   public_surface: build_catalogue_d1, build_catalogue_d2_oracle
#   internal_surface: _obj_key
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_catalogue
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domains
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

import itertools
from fractions import Fraction
from typing import List, Optional, Tuple

from .canonical import UCNSObject, UNIT
from .domains import (
    A_PLUS_MAX,
    N_MIN_MAX,
    generate_payload_catalogue,
    is_in_oracle_class,
)

__all__ = ["build_catalogue_d1", "build_catalogue_d2_oracle"]


def build_catalogue_d1() -> List[UCNSObject]:
    """Return all depth-1 UCNSObjects in the frozen domain D'.

    These are the oracle atoms: objects with ``|A⁺| ≤ A_PLUS_MAX``,
    ``n_min ≤ N_MIN_MAX``, and all cell payloads ``None``.  ``None``
    itself (the unit) is excluded.

    Suitable as the catalogue for factorizations whose left factor is
    known to be depth-1 (covered by the v0.6 left-quotient completeness
    theorem).
    """
    return [obj for obj in generate_payload_catalogue() if obj is not None]


def build_catalogue_d2_oracle(
    payload_basis: Optional[List[Optional[UCNSObject]]] = None,
) -> List[UCNSObject]:
    """Return depth-2 oracle-class UCNSObjects built from *payload_basis*.

    Parameters
    ----------
    payload_basis:
        The oracle atoms to place in cell payloads.  If ``None``,
        defaults to the full depth-1 catalogue (the result of
        :func:`ucns.domains.generate_payload_catalogue`,
        which includes ``None`` as the unit payload).

        **Size warning**: enumeration is ``|basis|^length`` per
        ``(n_min, length, face_bits)`` combination.  With the default
        full basis and ``length=3`` this is large — benchmark before
        passing the result to a large corpus.

    Returns
    -------
    A deduplicated list of ``UCNSObject``s, each satisfying
    ``is_in_oracle_class(obj) == True`` and having depth exactly 2
    (at least one non-``None`` payload).
    """
    if payload_basis is None:
        payload_basis = generate_payload_catalogue()

    objects: List[UCNSObject] = []
    seen: set = set()

    for n_min in range(1, N_MIN_MAX + 1):
        for length in range(1, A_PLUS_MAX + 1):
            angles = [Fraction(2 * k, n_min) for k in range(length)]
            for face_bits in range(2 ** length):
                faces = [(face_bits >> i) & 1 for i in range(length)]
                for payloads in itertools.product(payload_basis, repeat=length):
                    # Need at least one non-None payload to reach depth 2.
                    if all(p is None for p in payloads):
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
                    if key not in seen:
                        seen.add(key)
                        objects.append(obj)

    return objects


def _obj_key(obj: UCNSObject) -> tuple:
    """Structural deduplication key, recursive to depth-2."""
    return (
        obj.n_min,
        tuple(obj.F_plus),
        tuple(
            (a, _obj_key(p) if p is not None else None)
            for a, p in obj.A_plus
        ),
    )
