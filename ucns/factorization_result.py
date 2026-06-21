"""
ucns.factorization_result
===================================
A0-facing factorization result envelopes.

The raw solver ``factor_search_v08`` remains unchanged and returns either a
factor pair or the legacy string sentinel ``"SEQ-PRIME"``.  This module wraps
that result with canonical product identity and typed domain-status metadata
so callers do not mistake frontier-domain results for absolute primality.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_factorization_result
#   module_name: factorization_result
#   module_kind: engine
#   summary: A0-facing factorization-result envelope wrapping the raw solver output with canonical product identity and typed domain-status so SEQ-PRIME is correctly scoped.
#   owner: Erin Spencer
#   public_surface: FactorizationResultKind, FactorizationResult, factorization_result
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_factorization_result
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domain_status, ucns_factor_search_v08, ucns_serialization
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple

from .canonical import UCNSObject, multiply
from .domain_status import DomainStatusMetadata, status_for_object
from .factor_search_v08 import SEQ_PRIME, factor_search_v08
from .serialization import stable_hash


class FactorizationResultKind(str, Enum):
    """Result kinds returned by the factorization envelope."""

    FACTORS = "FACTORS"
    SEQ_PRIME = "SEQ-PRIME"


@dataclass(frozen=True)
class FactorizationResult:
    """Self-describing factorization output for A0-facing consumers.

    ``seq_prime_is_absolute`` is True only when the product's declared domain
    has a completeness guarantee and the raw solver returned ``SEQ-PRIME``.
    In frontier / experimental domains, the same sentinel is non-absolute and
    must be scoped accordingly.
    """

    product_hash: str
    product_domain_label: str
    product_domain_metadata: DomainStatusMetadata
    result_kind: FactorizationResultKind
    factors: Optional[Tuple[UCNSObject, UCNSObject]]
    seq_prime_is_absolute: bool
    claim_scope: str
    note: str

    @property
    def has_factors(self) -> bool:
        """Return True iff this envelope contains a recovered factor pair."""
        return self.factors is not None

    @property
    def requires_scope(self) -> bool:
        """Return True iff the result must be presented with domain scope."""
        return not self.seq_prime_is_absolute


def factorization_result(
    P: UCNSObject,
    catalogue: Optional[List[Optional[UCNSObject]]] = None,
) -> FactorizationResult:
    """Run ``factor_search_v08`` and return a self-describing envelope."""
    metadata = status_for_object(P)
    raw = factor_search_v08(P, catalogue=catalogue)
    product_hash = stable_hash(P)

    if isinstance(raw, tuple):
        A, B = raw
        note = "Recovered factors recompose to product."
        if multiply(A, B) != P:
            # This should never happen if factor_search_v08 preserves its
            # soundness contract.  Keep the guard here for envelope callers.
            note = "Recovered factors failed recomposition guard. Treat as invalid."
        return FactorizationResult(
            product_hash=product_hash,
            product_domain_label=metadata.label,
            product_domain_metadata=metadata,
            result_kind=FactorizationResultKind.FACTORS,
            factors=(A, B),
            seq_prime_is_absolute=False,
            claim_scope="composite-found",
            note=note,
        )

    if raw != SEQ_PRIME:
        raise ValueError(f"Unknown factor_search_v08 result: {raw!r}")

    absolute = metadata.completeness_guaranteed
    return FactorizationResult(
        product_hash=product_hash,
        product_domain_label=metadata.label,
        product_domain_metadata=metadata,
        result_kind=FactorizationResultKind.SEQ_PRIME,
        factors=None,
        seq_prime_is_absolute=absolute,
        claim_scope=metadata.seq_prime_claim_scope,
        note=(
            "SEQ-PRIME within a declared complete domain."
            if absolute
            else "SEQ-PRIME is non-absolute outside a declared complete domain."
        ),
    )


__all__ = [
    "FactorizationResultKind",
    "FactorizationResult",
    "factorization_result",
]
