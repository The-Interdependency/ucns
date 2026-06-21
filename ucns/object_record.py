"""
ucns.object_record
============================
General UCNS object records for A0-facing inspection.

A record describes any UCNS object without invoking factorization.  It combines
canonical identity, domain-status metadata, and basic structural facts so A0 can
inspect an object before deciding whether to factor, store, compare, retrieve,
or reason over it.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_object_record
#   module_name: object_record
#   module_kind: engine
#   summary: Builds a self-describing inspection record (canonical identity, domain-status metadata, structural facts) for any UCNS object without invoking factorization.
#   owner: Erin Spencer
#   public_surface: UCNSObjectRecord, object_record
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_object_record
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domain_status, ucns_domains, ucns_serialization
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from dataclasses import dataclass
from typing import Optional

from .canonical import UCNSObject, is_unit
from .domain_status import DomainStatusMetadata, status_for_object
from .domains import depth_of
from .serialization import canonical_json as _canonical_json
from .serialization import stable_hash


@dataclass(frozen=True)
class UCNSObjectRecord:
    """Self-describing metadata for a UCNS object.

    ``canonical_json`` is included for audit/display convenience.  Use
    ``object_hash`` for stable identity comparisons.
    """

    object_hash: str
    domain_label: str
    domain_metadata: DomainStatusMetadata
    depth: int
    n_min: int
    length: int
    is_unit: bool
    is_verified_domain: bool
    is_frontier: bool
    canonical_json: str
    note: str


def object_record(obj: Optional[UCNSObject]) -> UCNSObjectRecord:
    """Return a safe inspection record for *obj*."""
    metadata = status_for_object(obj)
    unit = is_unit(obj)
    depth = depth_of(obj)

    if obj is None:
        n_min = 1
        length = 0
    else:
        n_min = int(obj.n_min)
        length = len(obj.A_plus)

    return UCNSObjectRecord(
        object_hash=stable_hash(obj),
        domain_label=metadata.label,
        domain_metadata=metadata,
        depth=depth,
        n_min=n_min,
        length=length,
        is_unit=unit,
        is_verified_domain=metadata.completeness_guaranteed,
        is_frontier=metadata.is_frontier,
        canonical_json=_canonical_json(obj),
        note=metadata.note,
    )


__all__ = ["UCNSObjectRecord", "object_record"]
