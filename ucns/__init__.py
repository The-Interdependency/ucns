"""
ucns
====
Public import namespace for the Unit Circle Number System package.

The recursive factorization engine currently lives in `ucns_recursive`.
This namespace re-exports the stable public surface so users can write:

    from ucns import UCNSObject, multiply, factor_search_v08

`ucns_recursive` remains supported as a compatibility import path.
"""

from ucns_recursive import *  # noqa: F401,F403
from ucns_recursive import __all__ as _recursive_all

__all__ = list(_recursive_all)
