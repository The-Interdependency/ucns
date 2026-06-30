#!/usr/bin/env python
"""Lightweight UCNS cache benchmark harness with no speedup claims."""
from __future__ import annotations

import sys
import time
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ucns import UCNSObject
from ucns_cache import UCNSCacheStore, make_ucns_cache_key
from ucns_cache.instrumentation import timed_metric


def fixtures(count=30):
    return [UCNSObject(4, 2, [(Fraction(0), None), (Fraction(1, 2), None)], [0, i % 2]) for i in range(count)]


def main():
    objs = fixtures()
    metrics = {"total_calls": len(objs), "time_spent_keying": 0.0, "guard_failures": 0}
    store = UCNSCacheStore()
    start = time.perf_counter()
    for obj in objs:
        with timed_metric(metrics, "time_spent_keying"):
            key = make_ucns_cache_key(obj)
        if not store.get(key).hit:
            store.put(key, "computed", value_kind="benchmark")
    metrics.update(store.stats())
    metrics["elapsed_seconds"] = time.perf_counter() - start
    metrics["time_saved"] = None
    print(metrics)


if __name__ == "__main__":
    main()
