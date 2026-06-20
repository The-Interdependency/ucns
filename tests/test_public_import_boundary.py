"""Public import boundary tests for the ucns package."""

from __future__ import annotations

import builtins
import importlib
import sys
import unittest


class TestPublicImportBoundary(unittest.TestCase):
    def test_ucns_import_does_not_depend_on_ucns_recursive(self) -> None:
        """The public package must import without reaching for the legacy shim."""
        original_import = builtins.__import__
        removed = {
            name: module
            for name, module in list(sys.modules.items())
            if name == "ucns" or name.startswith("ucns.")
        }

        for name in removed:
            sys.modules.pop(name, None)

        def guarded_import(name, globals=None, locals=None, fromlist=(), level=0):
            if name == "ucns_recursive" or name.startswith("ucns_recursive."):
                raise AssertionError(f"ucns imported deprecated compatibility package {name!r}")
            return original_import(name, globals, locals, fromlist, level)

        try:
            builtins.__import__ = guarded_import
            module = importlib.import_module("ucns")
            self.assertTrue(hasattr(module, "UCNSObject"))
            self.assertTrue(hasattr(module, "factor_search_v08"))
        finally:
            builtins.__import__ = original_import
            for name in [n for n in sys.modules if n == "ucns" or n.startswith("ucns.")]:
                sys.modules.pop(name, None)
            sys.modules.update(removed)


if __name__ == "__main__":
    unittest.main()
