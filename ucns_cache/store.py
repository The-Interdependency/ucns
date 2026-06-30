"""In-memory UCNS cache store with exact, structural, and factor lookup paths."""
from __future__ import annotations

import time
from typing import Any, Dict, Optional

from .entries import CacheLookupResult, UCNSCacheEntry, UCNSCacheKey
from .keys import factor_reuse_candidates, make_ucns_cache_key


class UCNSCacheStore:
    def __init__(self) -> None:
        self._exact: Dict[str, UCNSCacheEntry] = {}
        self._braider: Dict[str, UCNSCacheEntry] = {}
        self._stats = {"puts": 0, "exact_hits": 0, "structural_hits": 0, "factor_hits": 0, "misses": 0}

    def put(self, key: UCNSCacheKey, value: Any, value_kind: str = "unknown", metadata: Optional[Dict[str, Any]] = None) -> UCNSCacheEntry:
        entry = UCNSCacheEntry(key, value, value_kind, time.time(), 0, "ucns_cache", "not_applicable", None, dict(metadata or {}))
        self._exact[key.canonical_hash] = entry
        if key.braider_hash:
            self._braider.setdefault(key.braider_hash, entry)
        self._stats["puts"] += 1
        return entry

    def get(self, key: UCNSCacheKey) -> CacheLookupResult:
        entry = self._exact.get(key.canonical_hash)
        if entry is not None:
            entry.hit_count += 1; self._stats["exact_hits"] += 1
            return CacheLookupResult(True, True, False, False, key, entry, "exact canonical_hash hit")
        if key.braider_hash:
            entry = self._braider.get(key.braider_hash)
            if entry is not None:
                entry.hit_count += 1; self._stats["structural_hits"] += 1
                return CacheLookupResult(True, False, True, False, key, entry, "structural braider_hash hit")
        for payload_hash in key.payload_hashes:
            entry = self._exact.get(payload_hash)
            if entry is not None:
                entry.hit_count += 1; self._stats["factor_hits"] += 1
                return CacheLookupResult(True, False, False, True, key, entry, "payload/factor candidate hit")
        self._stats["misses"] += 1
        return CacheLookupResult(False, False, False, False, key, None, "miss")

    def get_by_object(self, obj) -> CacheLookupResult:
        key = make_ucns_cache_key(obj)
        result = self.get(key)
        if result.hit:
            return result
        for candidate in factor_reuse_candidates(obj):
            entry = self._exact.get(candidate.canonical_hash)
            if entry is not None:
                entry.hit_count += 1; self._stats["factor_hits"] += 1
                return CacheLookupResult(True, False, False, True, key, entry, "factorization-informed hit")
        return result

    def put_by_object(self, obj, value: Any, value_kind: str = "unknown", metadata: Optional[Dict[str, Any]] = None) -> UCNSCacheEntry:
        return self.put(make_ucns_cache_key(obj), value, value_kind, metadata)

    def stats(self) -> Dict[str, int]:
        data = dict(self._stats)
        data["memory_entries"] = len(self._exact)
        data["braider_entries"] = len(self._braider)
        return data

    def clear(self) -> None:
        self._exact.clear(); self._braider.clear()
        for key in self._stats: self._stats[key] = 0
