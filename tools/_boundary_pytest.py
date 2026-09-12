# ratios: loc_comments=63:27 imports_exports=5:2 calls_definitions=22:4
# === MODULE_BUILD ===
# id: boundary_pytest_observer
#   module_name: _boundary_pytest
#   module_kind: instrument
#   summary: observes actual pytest exceptions, xfail outcomes, and imported source origins for UCNS receipts
#   owner: Erin Spencer
#   public_surface: none; launched by run_skill_lib_boundaries
#   internal_surface: Observer, main
#   auth_boundary: none
#   storage_boundary: writes caller-selected machine outcome report
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_skill_lib_boundary_runner.py
#   rollout: boundary runner subprocess bootstrap
#   rollback: remove with boundary runner bootstrap integration
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: boundary_pytest_observes_actual_outcomes
#   given: a selected pytest boundary runs through this bootstrap
#   then: assertion subclasses fail, unexpected exceptions error, XPASS cannot pass, and imported local package origins must match the bound tree
#   class: evidence
# === END CONTRACTS ===

"""Internal bootstrap. Usage: launched only by tools/run_skill_lib_boundaries.py.

Observations describe executed checks, not theorem standing or a hostile-code
sandbox. Ambient pytest plugins and PYTHONPATH are excluded by the parent.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

import pytest


class Observer:
    def __init__(self, root: Path):
        self.root = root
        self.calls: list[str] = []
        self.other: list[str] = []

    @pytest.hookimpl(hookwrapper=True, tryfirst=True)
    def pytest_runtest_makereport(self, item, call):
        report = (yield).get_result()
        if report.skipped:
            status = "SKIP"
        elif hasattr(report, "wasxfail"):
            status = "FAIL"  # Includes explicit xfail(strict=False) XPASS.
        elif call.excinfo is not None:
            status = "FAIL" if call.when == "call" and (
                call.excinfo.errisinstance(AssertionError)
                or call.excinfo.errisinstance(pytest.fail.Exception)
            ) else "ERROR"
        elif report.failed:
            status = "FAIL" if call.when == "call" else "ERROR"
        else:
            status = "PASS"
        if call.when == "call":
            self.calls.append(status)
        elif status != "PASS":
            self.other.append(status)


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    report_path = Path(sys.argv[2])
    sys.path[:0] = [str(root / "src"), str(root)]
    observer = Observer(root)
    exit_code = int(pytest.main(sys.argv[3:], plugins=[observer]))
    source_root = root / "src"
    local_names = {p.stem if p.is_file() else p.name for p in source_root.iterdir()} if source_root.exists() else set()
    origins = {}
    wrong_origins = []
    for name, module in tuple(sys.modules.items()):
        if name.split(".", 1)[0] not in local_names:
            continue
        paths = [getattr(module, "__file__", None), *getattr(module, "__path__", ())]
        paths = [str(Path(p).resolve()) for p in paths if p is not None]
        origins[name] = paths
        if not paths or any(not Path(p).is_relative_to(source_root) for p in paths):
            wrong_origins.append(name)
    statuses = observer.calls + observer.other
    if wrong_origins or "ERROR" in statuses:
        status = "ERROR"
    elif "FAIL" in statuses:
        status = "FAIL"
    elif "SKIP" in statuses:
        status = "SKIP"
    elif observer.calls and exit_code == 0:
        status = "PASS"
    else:
        status = "ERROR"
    report_path.write_text(json.dumps({"status": status, "calls": observer.calls, "other": observer.other, "origins": origins, "wrong_origins": wrong_origins}), encoding="utf-8")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
# ratios: loc_comments=63:27 imports_exports=5:2 calls_definitions=22:4
