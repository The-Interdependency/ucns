"""
ucns.domain_status
============================
Typed status metadata for UCNS theorem / implementation domains.

This module does not replace the legacy string labels returned by
``verified_domain_status``.  It wraps those labels in explicit metadata so
A0-facing code can distinguish implementation, test, proof, oracle, and
frontier claims without inferring certainty from a bare string.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_domain_status
#   module_name: domain_status
#   module_kind: engine
#   summary: Typed status metadata wrapping legacy UCNS domain labels so callers can distinguish implementation/test/proof/oracle/frontier claims and scope SEQ-PRIME results.
#   owner: Erin Spencer
#   public_surface: DomainProofStatus, DomainStatusMetadata, VERIFIED_DOMAIN_LABELS, domain_status_metadata, status_for_object, is_verified_domain_label, seq_prime_requires_scope
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns_recursive/tests/test_domain_status.py
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

    Attributes
    ----------
    label:
        Legacy domain label such as ``"depth-1"`` or
        ``"depth-2-non-oracle"``.
    statuses:
        Tuple of typed status flags that describe the current claim.
    completeness_guaranteed:
        True only when the current theorem / oracle surface supports treating
        a failed factorization as complete within that declared domain.
    seq_prime_claim_scope:
        Human-readable scope for any ``SEQ-PRIME`` result in this domain.
    note:
        Short explanation suitable for audit logs and A0 status displays.
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
    """Return typed metadata for a legacy domain-status label.

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
    """Return typed status metadata for *obj*.

    This delegates to the existing ``verified_domain_status`` taxonomy, then
    wraps the result in typed metadata for A0-facing consumers.
    """
    from .domains import verified_domain_status

    return domain_status_metadata(verified_domain_status(obj))


def is_verified_domain_label(label: str) -> bool:
    """Return True iff *label* is currently complete in its declared domain."""
    return domain_status_metadata(label).completeness_guaranteed


def seq_prime_requires_scope(label: str) -> bool:
    """Return True iff ``SEQ-PRIME`` must be marked non-absolute for *label*."""
    return not domain_status_metadata(label).completeness_guaranteed


__all__ = [
    "DomainProofStatus",
    "DomainStatusMetadata",
    "VERIFIED_DOMAIN_LABELS",
    "domain_status_metadata",
    "status_for_object",
    "is_verified_domain_label",
    "seq_prime_requires_scope",
]
