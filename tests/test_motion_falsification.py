# === CHECKS ===
# id: check_motion_falsification_runs_declared_controls
#   proves: motion_falsification_runs_declared_controls
#   call: self::test_runs_declared_controls
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_motion_falsification_walk_permutation_changes_path_not_terminal
#   proves: motion_falsification_walk_permutation_changes_path_not_terminal
#   call: self::test_walk_permutation_changes_path_not_terminal
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
#
# id: check_motion_falsification_survival_is_not_selection
#   proves: motion_falsification_survival_is_not_selection
#   call: self::test_survival_is_not_selection
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from __future__ import annotations

from ucns import run_motion_falsification


def test_runs_declared_controls() -> None:
    report = run_motion_falsification()
    for control in (
        "null",
        "single-channel",
        "pair",
        "frame",
        "covering",
        "radius",
        "walk-permutation",
    ):
        assert control in report["results"]
    again = run_motion_falsification()
    assert again["receipt_sha256"] == report["receipt_sha256"]


def test_walk_permutation_changes_path_not_terminal() -> None:
    report = run_motion_falsification()
    result = report["results"]["walk-permutation"]
    assert result["ok"] is True
    assert result["path_differs"] is True
    assert result["terminal_invariant"] is True


def test_survival_is_not_selection() -> None:
    report = run_motion_falsification()
    assert "selected" not in report["survivors"]
    assert "unresolved" in report["hmmm"]
