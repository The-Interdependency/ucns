# ratios: loc_comments=105:36 imports_exports=8:1 calls_definitions=48:5
# === MODULE_BUILD ===
# id: boundary_process_supervisor
#   module_name: _boundary_supervisor
#   module_kind: instrument
#   summary: owns check descendant lifetime outside the pytest process and its signal handlers
#   owner: Erin Spencer
#   public_surface: none; launched by run_skill_lib_boundaries
#   internal_surface: main, child subreaping
#   auth_boundary: none
#   storage_boundary: write
#   storage_notes: updates machine outcome report after child cleanup
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_skill_lib_boundary_runner.py
#   rollout: process supervisor for every selected check
#   rollback: remove with boundary-runner integration
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: boundary_supervisor_ends_descendants
#   given: a selected check or executable capability probe exits or exceeds its timeout, including after replacing its signal handlers
#   then: a separate Linux subreaper kills and reaps remaining check descendants before accepting or returning its outcome
#   class: evidence
# === END CONTRACTS ===
"""Internal usage: python _boundary_supervisor.py TIMEOUT BOOTSTRAP ROOT REPORT PYTEST_ARGS.

For a capability executable: python _boundary_supervisor.py --probe TIMEOUT COMMAND ARGS.

Only the child runs pytest or test code. Descendant adoption therefore survives
child signal-handler changes, crashes, and detached sessions. This is trusted
check instrumentation, not containment against hostile code targeting ancestors.
"""
from __future__ import annotations

import ctypes
import json
import os
from pathlib import Path
import signal
import subprocess
import sys


def _enable_descendant_reaping() -> None:
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(36, 1, 0, 0, 0) != 0:  # Linux PR_SET_CHILD_SUBREAPER.
        raise OSError(ctypes.get_errno(), "cannot bind check descendant lifetime")


def _owned_children(proc_root: Path = Path("/proc")) -> list[int]:
    """Find owned children in procfs and translate them to caller-namespace IDs.

    A procfs mount can describe an ancestor PID namespace. Its stat/children
    numbers must never be compared to getpid or passed directly to kill/waitpid.
    The synthetic proc_root used by fixtures may omit status for local-ID data.
    """
    local_parent = os.getpid()
    try:
        fields = dict(line.split(":", 1) for line in (proc_root / "self/status").read_text().splitlines() if ":" in line)
    except FileNotFoundError:
        if proc_root == Path("/proc"):
            raise OSError("procfs cannot establish the supervisor PID namespace")
        fields = {}  # Local-ID synthetic snapshot; never the live default.
    parent = int(fields.get("Pid", local_parent))
    namespace_pids = tuple(int(p) for p in fields.get("NSpid", str(parent)).split())
    if not namespace_pids or namespace_pids[0] != parent or namespace_pids[-1] != local_parent:
        raise OSError("procfs PID namespace does not resolve to this supervisor")
    namespace_index = len(namespace_pids) - 1
    try:
        raw_children = {int(pid) for pid in (proc_root / f"self/task/{parent}/children").read_text().split()}
    except FileNotFoundError:
        raw_children = set()
        for process in proc_root.iterdir():
            if not process.name.isdecimal():
                continue
            try:
                state = (process / "stat").read_text().rpartition(")")[2].split()
                if int(state[1]) == parent:
                    raw_children.add(int(process.name))
            except (FileNotFoundError, ProcessLookupError, PermissionError):
                continue  # Exited processes or unrelated users hidden by procfs.
    children = set()
    for pid in raw_children:
        try:
            child_fields = dict(line.split(":", 1) for line in (proc_root / str(pid) / "status").read_text().splitlines() if ":" in line)
        except (FileNotFoundError, ProcessLookupError):
            if fields:
                continue  # Exited before namespace translation.
            child_fields = {}  # Synthetic local-ID fixture.
        child_pids = tuple(int(p) for p in child_fields.get("NSpid", str(pid)).split())
        if len(child_pids) <= namespace_index or child_pids[0] != pid:
            raise OSError("owned child PID namespace cannot be resolved")
        local_pid = child_pids[namespace_index]
        if local_pid <= 0 or local_pid == local_parent:
            raise OSError("invalid owned child PID mapping")
        children.add(local_pid)
    return sorted(children)


def _reap_descendants() -> int:
    """Terminate and reap only children owned/adopted by this bootstrap."""
    observed = 0
    while True:
        children = _owned_children()
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


def _supervise(command: list[str], timeout: int) -> tuple[int, bool, int]:
    _enable_descendant_reaping()
    _owned_children()  # Verify procfs support before any check code is launched.
    process = subprocess.Popen(command, start_new_session=True)
    timed_out = False
    try:
        returncode = process.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        process.kill()
        returncode = process.wait()
    descendants = _reap_descendants()
    return returncode, timed_out, descendants


def main() -> int:
    if sys.argv[1] == "--probe":
        returncode, timed_out, descendants = _supervise(sys.argv[3:], int(sys.argv[2]))
        return 124 if timed_out else 1 if descendants else returncode
    timeout = int(sys.argv[1])
    report = Path(sys.argv[4])
    returncode, timed_out, descendants = _supervise([sys.executable, *sys.argv[2:]], timeout)
    try:
        observed = json.loads(report.read_text())
        if not isinstance(observed, dict):
            raise ValueError("invalid bootstrap report")
    except (OSError, ValueError):
        observed = {"status": "ERROR", "calls": [], "other": ["ERROR"], "origins": {}, "wrong_origins": []}
    if timed_out or descendants:
        observed["status"] = "ERROR"
        observed.setdefault("other", []).append("ERROR")
    observed.update(descendants_reaped=descendants, timed_out=timed_out)
    report.write_text(json.dumps(observed), encoding="utf-8")
    return 124 if timed_out else returncode


if __name__ == "__main__":
    raise SystemExit(main())
# ratios: loc_comments=105:36 imports_exports=8:1 calls_definitions=48:5
