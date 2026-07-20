"""UCNS-native cache key generation and factor reuse candidates."""
from __future__ import annotations

from typing import List, Optional, Tuple

from .braider import braid_streams
from .dependencies import require_ucns
from .entries import UCNSCacheKey
from .primitive_streams import derive_primitive_streams


def _payloads(obj) -> Tuple[object, ...]:
    if obj is None:
        return ()
    return tuple(payload for _angle, payload in getattr(obj, "A_plus", ()) if payload is not None)


def _face_signature(obj) -> Optional[str]:
    if obj is None:
        return None
    return "".join(str(int(bit) & 1) for bit in getattr(obj, "F_plus", []) or [])


def make_ucns_cache_key(obj) -> UCNSCacheKey:
    require_ucns()
    from ucns import a0_safe
    from ucns.domain_status import seq_prime_requires_scope, status_for_object

    record = a0_safe.describe(obj)
    status = status_for_object(obj)
    payload_hashes = tuple(a0_safe.identity(payload) for payload in _payloads(obj))
    braider_hash = braid_streams(derive_primitive_streams(obj)).lattice_hash
    scope = status.seq_prime_claim_scope
    if seq_prime_requires_scope(status.label):
        scope = f"{scope}; non-absolute frontier/domain-scoped reuse only"
    return UCNSCacheKey(
        canonical_hash=a0_safe.identity(obj),
        domain_label=getattr(record, "domain_label", status.label),
        depth=getattr(record, "depth", None),
        carrier=getattr(record, "n_min", None),
        face_signature=_face_signature(obj),
        payload_hashes=payload_hashes,
        braider_hash=braider_hash,
        scope_note=scope,
    )


def factor_reuse_candidates(obj) -> List[UCNSCacheKey]:
    require_ucns()
    from ucns import a0_safe

    result = a0_safe.factor(obj)
    factors = getattr(result, "factors", None)
    if not factors:
        return []
    return [make_ucns_cache_key(factor) for factor in factors]
