"""Dependency boundary for the UCNS-native cache prototype."""
from __future__ import annotations

import importlib
from typing import Any, Dict

_INSTALL = "Install sibling ucns with: python -m pip install -e ../ucns"


def ucns_available() -> bool:
    try:
        importlib.import_module("ucns")
        importlib.import_module("ucns.a0_safe")
        return True
    except ImportError:
        return False


def ucns_dependency_report() -> Dict[str, Any]:
    if not ucns_available():
        return {"available": False, "install_hint": _INSTALL}
    ucns = importlib.import_module("ucns")
    return {
        "available": True,
        "module_path": getattr(ucns, "__file__", None),
        "version": getattr(ucns, "__version__", None),
    }


def require_ucns():
    try:
        return importlib.import_module("ucns")
    except ImportError as exc:
        raise ImportError(_INSTALL) from exc
