"""UCNS-native cache prototype package."""
from .braider import braid_streams
from .dependencies import require_ucns, ucns_available, ucns_dependency_report
from .entries import BraiderOutput, CacheLookupResult, PrimitiveStreams, UCNSCacheEntry, UCNSCacheKey
from .keys import factor_reuse_candidates, make_ucns_cache_key
from .primitive_streams import derive_primitive_streams
from .store import UCNSCacheStore

__all__ = [
    "UCNSCacheKey", "UCNSCacheEntry", "PrimitiveStreams", "BraiderOutput", "CacheLookupResult",
    "UCNSCacheStore", "make_ucns_cache_key", "factor_reuse_candidates", "derive_primitive_streams",
    "braid_streams", "require_ucns", "ucns_available", "ucns_dependency_report",
]
