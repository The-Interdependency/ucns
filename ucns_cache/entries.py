"""Dataclasses for the UCNS-native cache prototype."""
from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_native_cache
#   module_name: ucns_cache
#   module_kind: experiment
#   summary: Software-only UCNS-native cache prototype for canonical keying, primitive streams, braider identity, and conservative structural reuse.
#   owner: Erin Spencer / Codex
#   public_surface: UCNSCacheKey, UCNSCacheEntry, PrimitiveStreams, BraiderOutput, CacheLookupResult, UCNSCacheStore, make_ucns_cache_key, derive_primitive_streams, braid_streams, factor_reuse_candidates
#   internal_surface: dependencies, keys, entries, primitive_streams, braider, store, policy, instrumentation
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_ucns_cache_keys.py, tests/test_ucns_cache_streams.py, tests/test_ucns_cache_store.py, tests/test_ucns_cache_factor_reuse.py
#   rollout: opt-in prototype / downstream A0_UCNS_CACHE integration
#   rollback: remove ucns_cache package, docs/ucns-native-caching.md, scripts/bench_ucns_cache.py, and tests/test_ucns_cache_*.py
#   feature_flag: A0_UCNS_CACHE for downstream a0-betatest integration
#   since: 2026-06-28
#   unresolved: a0-betatest checkout unavailable in this workspace, downstream inference hook not installed, stable shared-braid fixture pending
# === END MODULE_BUILD ===

from dataclasses import dataclass, field
from typing import Any, Dict, Optional, Tuple


@dataclass(frozen=True)
class UCNSCacheKey:
    canonical_hash: str
    domain_label: Optional[str]
    depth: Optional[int]
    carrier: Optional[int]
    face_signature: Optional[str]
    payload_hashes: Tuple[str, ...]
    braider_hash: Optional[str]
    scope_note: str


@dataclass
class UCNSCacheEntry:
    key: UCNSCacheKey
    value: Any
    value_kind: str
    created_at: float
    hit_count: int
    source_stage: str
    recomposition_guard: Optional[str]
    fidelity_score: Optional[float]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PrimitiveStreams:
    angle_bits: Tuple[int, ...]
    rotation_bits: Tuple[int, ...]
    chirality_bits: Tuple[int, ...]
    lcm_length: int
    source_hash: str


@dataclass(frozen=True)
class BraiderOutput:
    primitive_streams: PrimitiveStreams
    lattice_hash: str
    braid_events: Tuple[Dict[str, Any], ...]
    reusable_windows: Tuple[Dict[str, Any], ...]


@dataclass(frozen=True)
class CacheLookupResult:
    hit: bool
    exact_hit: bool
    structural_hit: bool
    factor_hit: bool
    key: UCNSCacheKey
    entry: Optional[UCNSCacheEntry]
    reason: str
