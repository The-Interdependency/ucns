# ratios: loc_comments=101:28 imports_exports=8:2 calls_definitions=39:7
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
#   then: assertion subclasses fail, unexpected exceptions error, XPASS cannot pass, imported local package origins must match the bound tree, and leaked descendants prevent acceptance
#   class: evidence
# === END CONTRACTS ===

"""Internal bootstrap. Usage: launched only by tools/run_skill_lib_boundaries.py.

Observations describe executed checks, not theorem standing or a hostile-code
sandbox. Ambient pytest plugins and PYTHONPATH are excluded by the parent.
"""
from __future__ import annotations

import json
import ctypes
import os
from pathlib import Path
import signal
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


def _enable_descendant_reaping() -> None:
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(36, 1, 0, 0, 0) != 0:  # Linux PR_SET_CHILD_SUBREAPER.
        raise OSError(ctypes.get_errno(), "cannot bind check descendant lifetime")


def _reap_descendants() -> int:
    """Terminate and reap only children owned/adopted by this bootstrap."""
    observed = 0
    children_path = Path(f"/proc/self/task/{os.getpid()}/children")
    while True:
        children = [int(pid) for pid in children_path.read_text().split()]
        if not children:
            return observed
        observed += len(children)
        for pid in children:
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        for pid in children:
            try:
                os.waitpid(pid, 0)
            except ChildProcessError:
                pass


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    report_path = Path(sys.argv[2])
    sys.path[:0] = [str(root / "src"), str(root)]
    observer = Observer(root)
    _enable_descendant_reaping()
    def terminate_check(signum, frame):
        _reap_descendants()
        raise SystemExit(124)
    signal.signal(signal.SIGTERM, terminate_check)
    hook = sys.modules.get("sitecustomize")
    if getattr(hook, "BOUND_ROOT", None) != str(root) or getattr(hook, "FINDER", None) not in sys.meta_path:
        raise RuntimeError("bound descendant import hook is unavailable")
    try:
        exit_code = int(pytest.main(sys.argv[3:], plugins=[observer]))
    finally:
        descendants = _reap_descendants()
    if descendants:
        observer.other.append("ERROR")
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
    report_path.write_text(json.dumps({"status": status, "calls": observer.calls, "other": observer.other, "origins": origins, "wrong_origins": wrong_origins, "descendants_reaped": descendants}), encoding="utf-8")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
# ratios: loc_comments=101:28 imports_exports=8:2 calls_definitions=39:7
