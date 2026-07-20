"""
ucns.domain_status
============================
Typed status metadata for UCNS theorem / implementation domains.

This module describes domain-level prerequisites only.  A domain label can say
that a completeness theorem is available, but cannot by itself certify a
particular ``SEQ-PRIME`` result.  Result-level certification belongs to
``ucns.factorization_result`` and additionally requires validated catalogue
coverage, exact search-report binding, exhaustive untruncated search,
recognized coverage-preserving pruning, and a non-unit target.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_domain_status
#   module_name: domain_status
#   module_kind: engine
#   summary: Typed domain-level prerequisite metadata; bare labels never certify SEQ-PRIME, and result-level certainty is delegated to ucns.factorization_result.
#   owner: Erin Spencer
#   public_surface: DomainProofStatus, DomainStatusMetadata, VERIFIED_DOMAIN_LABELS, domain_status_metadata, status_for_object, is_verified_domain_label, seq_prime_requires_scope
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive/tests/test_domain_status.py, tests/test_certified_negative_results.py
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple

from .canonical import UCNSObject


class DomainProofStatus(str, Enum):
    """Canonical status vocabulary for UCNS domain claims."""

    DEFENDED = "DEFENDED"
    IMPLEMENTED = "IMPLEMENTED"
    TEST_BACKED = "TEST_BACKED"
    ORACLE_COMPLETE = "ORACLE_COMPLETE"
    FRONTIER = "FRONTIER"
    EXPERIMENTAL = "EXPERIMENTAL"


@dataclass(frozen=True)
class DomainStatusMetadata:
    """Self-describing metadata for a UCNS domain label.

    ``completeness_guaranteed`` means a domain-level completeness result is
    available as a prerequisite.  It is necessary but not sufficient for
    certifying a concrete negative search result.
    """

    label: str
    statuses: Tuple[DomainProofStatus, ...]
    completeness_guaranteed: bool
    seq_prime_claim_scope: str
    note: str

    @property
    def is_frontier(self) -> bool:
        """Return True when this label should be treated as frontier work."""
        return (
            DomainProofStatus.FRONTIER in self.statuses
            or DomainProofStatus.EXPERIMENTAL in self.statuses
            or not self.completeness_guaranteed
        )

    @property
    def is_defended(self) -> bool:
        """Return True when this label has a proof-defended status."""
        return DomainProofStatus.DEFENDED in self.statuses


_DOMAIN_STATUS_TABLE = {
    "depth-0": DomainStatusMetadata(
        label="depth-0",
        statuses=(DomainProofStatus.DEFENDED, DomainProofStatus.TEST_BACKED),
        completeness_guaranteed=True,
        seq_prime_claim_scope="not-prime-unit-domain",
        note="Unit / empty object domain; primality claims are not meaningful.",
    ),
    "depth-1": DomainStatusMetadata(
        label="depth-1",
        statuses=(DomainProofStatus.DEFENDED, DomainProofStatus.TEST_BACKED),
        completeness_guaranteed=True,
        seq_prime_claim_scope="defended-domain-relative",
        note="Flat / depth-1 restricted completeness surface.",
    ),
    "depth-2-oracle": DomainStatusMetadata(
        label="depth-2-oracle",
        statuses=(DomainProofStatus.ORACLE_COMPLETE, DomainProofStatus.TEST_BACKED),
        completeness_guaranteed=True,
        seq_prime_claim_scope="oracle-domain-relative",
        note="Complete only under the declared depth-2 oracle/catalogue assumptions.",
    ),
    "depth-2-non-oracle": DomainStatusMetadata(
        label="depth-2-non-oracle",
        statuses=(DomainProofStatus.IMPLEMENTED, DomainProofStatus.FRONTIER),
        completeness_guaranteed=False,
        seq_prime_claim_scope="frontier-non-absolute",
        note="Soundness may hold, but completeness is not proof-defended for this class.",
    ),
    "depth-3+": DomainStatusMetadata(
        label="depth-3+",
        statuses=(DomainProofStatus.EXPERIMENTAL, DomainProofStatus.FRONTIER),
        completeness_guaranteed=False,
        seq_prime_claim_scope="experimental-non-absolute",
        note="Recursive depth beyond the current defended / oracle-complete frontier.",
    ),
}


VERIFIED_DOMAIN_LABELS = frozenset(
    label for label, metadata in _DOMAIN_STATUS_TABLE.items()
    if metadata.completeness_guaranteed
)


def domain_status_metadata(label: str) -> DomainStatusMetadata:
    """Return typed prerequisite metadata for a legacy domain-status label.

    Unknown labels are treated as experimental frontier labels rather than
    silently promoted to a verified status.
    """
    try:
        return _DOMAIN_STATUS_TABLE[label]
    except KeyError:
        return DomainStatusMetadata(
            label=label,
            statuses=(DomainProofStatus.EXPERIMENTAL, DomainProofStatus.FRONTIER),
            completeness_guaranteed=False,
            seq_prime_claim_scope="unknown-non-absolute",
            note="Unknown UCNS domain label; treat as experimental frontier work.",
        )


def status_for_object(obj: Optional[UCNSObject]) -> DomainStatusMetadata:
    """Return typed domain prerequisite metadata for *obj*."""
    from .domains import verified_domain_status

    return domain_status_metadata(verified_domain_status(obj))


def is_verified_domain_label(label: str) -> bool:
    """Return True iff *label* has a domain-level completeness prerequisite.

    This does not certify a concrete search result.
    """
    return domain_status_metadata(label).completeness_guaranteed


def seq_prime_requires_scope(label: str) -> bool:
    """Return True because a bare domain label never certifies ``SEQ-PRIME``.

    Retained for compatibility.  Callers deciding result-level scope must use
    ``FactorizationResult.requires_scope`` from ``factorization_result``.
    The *label* argument is intentionally ignored: domain metadata is only one
    prerequisite among several required by the result policy.
    """
    del label
    return True


__all__ = [
    "DomainProofStatus",
    "DomainStatusMetadata",
    "VERIFIED_DOMAIN_LABELS",
    "domain_status_metadata",
    "status_for_object",
    "is_verified_domain_label",
    "seq_prime_requires_scope",
]
