"""Policy placeholders for downstream A0_UCNS_CACHE integration."""
from __future__ import annotations

import os

def ucns_cache_enabled(env_var: str = "A0_UCNS_CACHE") -> bool:
    return os.environ.get(env_var, "").strip().lower() in {"1", "true", "yes", "on"}
