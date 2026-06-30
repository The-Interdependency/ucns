"""Small instrumentation helpers for the UCNS cache prototype."""
from __future__ import annotations

from contextlib import contextmanager
import time

@contextmanager
def timed_metric(target: dict, key: str):
    start = time.perf_counter()
    try:
        yield
    finally:
        target[key] = target.get(key, 0.0) + (time.perf_counter() - start)
