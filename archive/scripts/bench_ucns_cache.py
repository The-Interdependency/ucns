#!/usr/bin/env python
"""Lightweight UCNS cache benchmark harness with no speedup claims."""
from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ucns.domains import generate_payload_catalogue
from ucns_cache import UCNSCacheStore
from ucns_cache.instrumentation import timed_metric


def fixtures(count=50):
    """Return a deterministic UCNS-domain workload for cache smoke metrics.

    The workload uses the frozen payload catalogue rather than hand-made cache
    twins.  It intentionally remains small and claim-light: it exercises exact
    and structural lookup accounting, but it is not a performance benchmark.
    """
    return [obj for obj in generate_payload_catalogue() if obj is not None][:count]


def run(count=50):
    """Run the cache smoke workload and return metrics."""
    objs = fixtures(count)
    metrics = {"total_calls": len(objs), "time_spent_keying": 0.0, "guard_failures": 0}
    store = UCNSCacheStore()
    start = time.perf_counter()
    for obj in objs:
        with timed_metric(metrics, "time_spent_keying"):
            result = store.get_by_object(obj)
        if not result.hit:
            store.put_by_object(obj, "computed", value_kind="benchmark")
    metrics.update(store.stats())
    metrics["elapsed_seconds"] = time.perf_counter() - start
    metrics["time_saved"] = None
    return metrics


def main():
    print(run())


if __name__ == "__main__":
    main()
