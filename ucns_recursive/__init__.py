"""Compatibility import path for the UCNS recursive engine.

The recursive engine now lives under the public ``ucns`` package. This package
is retained only so existing ``ucns_recursive`` imports continue to work during
the deprecation window. New code should import from ``ucns`` or ``ucns.a0_safe``.
"""

from ucns import *  # noqa: F401,F403
from ucns import __all__ as _ucns_all

__all__ = list(_ucns_all)
