# ratios: loc_comments=113:42 imports_exports=5:5 calls_definitions=65:5
# === CHECKS ===
# id: check_contract_audit_no_exec
#   proves: contract_audit_is_no_exec
#   call: self::test_contract_audit_no_exec
#   requires: python3
#   timeout: 5
#   mutates: filesystem
#   cleanup: tempdir_teardown
#
# id: check_contract_audit_detects_gaps
#   proves: contract_audit_reports_graph_gaps
#   call: self::test_contract_audit_detects_gaps
#   requires: python3
#   timeout: 5
#   mutates: filesystem
#   cleanup: tempdir_teardown
#
# id: check_repository_contract_graph
#   proves: contract_audit_accepts_closed_graph
#   call: self::test_repository_contract_graph
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

# === CHECKS ===
# id: check_contract_audit_empty_syntax_and_class_gaps
#   proves: contract_audit_reports_graph_gaps
#   call: self::test_empty_syntax_and_class_coverage_are_not_closed
#   requires: python3
#   timeout: 10
#   mutates: filesystem
#   cleanup: tempdir_teardown
#
# id: check_contract_audit_canonical_parser
#   proves: contract_audit_reports_graph_gaps, contract_audit_is_no_exec
#   call: self::test_nested_fences_cannot_hide_an_obligation
#   requires: python3
#   timeout: 10
#   mutates: filesystem
#   cleanup: tempdir_teardown
# === END CHECKS ===

from pathlib import Path
from tempfile import TemporaryDirectory

from tools.verify_skill_lib_contracts import audit_repository

ROOT = Path(__file__).resolve().parents[1]


def test_contract_audit_no_exec() -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "src").mkdir()
        marker = root / "executed.txt"
        (root / "src" / "module.py").write_text(
            "# === CONTRACTS ===\n"
            "# id: safe_import\n"
            "#   given: source is audited\n"
            "#   then: top-level code is not executed\n"
            "# === END CONTRACTS ===\n"
            f"open({str(marker)!r}, 'w').write('executed')\n",
            encoding="utf-8",
        )
        ok, problems = audit_repository(root)
        assert not ok
        assert problems
        assert not marker.exists()


def test_contract_audit_detects_gaps() -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "tests").mkdir()
        (root / "src").mkdir()
        (root / "src" / "bare.py").write_text(
            "def behavior():\n"
            "    return 1\n",
            encoding="utf-8",
        )
        (root / "tests" / "test_orphan.py").write_text(
            "# === CHECKS ===\n"
            "# id: orphan_check\n"
            "#   proves: absent_contract\n"
            "#   call: self::missing_function\n"
            "#   mutates: none\n"
            "#   cleanup: none\n"
            "# === END CHECKS ===\n"
            "def missing_function():\n"
            "    return None\n",
            encoding="utf-8",
        )
        ok, problems = audit_repository(root)
        assert not ok
        assert any("unknown contract" in problem for problem in problems)
        assert any("missing MODULE_BUILD" in problem for problem in problems)
        assert any("missing CONTRACTS" in problem for problem in problems)
        assert any("orphan_check missing fields: timeout" in problem for problem in problems)
        assert any("does not target an executable pytest test" in problem for problem in problems)


def test_repository_contract_graph() -> None:
    ok, problems = audit_repository(ROOT)
    assert ok, "\n".join(problems)


def test_empty_syntax_and_class_coverage_are_not_closed(tmp_path: Path) -> None:
    from test_skill_lib_boundary_runner import _repo

    ok, problems = audit_repository(tmp_path)
    assert not ok and any("empty" in item for item in problems)
    root = _repo(tmp_path, "def test_probe():\n    pass\n", [{"id": "check_probe", "function": "test_probe"}])
    source = root / "src/pkg/feature.py"
    original = source.read_text()
    source.write_text(original + "\ndef syntax broken\n")
    ok, problems = audit_repository(root)
    assert not ok and any("syntax" in item.lower() for item in problems)
    source.write_text(original)
    (root / "tests/test_class.py").write_text("class TestUnregistered:\n    def test_untracked(self):\n        assert False\n")
    ok, problems = audit_repository(root)
    assert not ok and any("TestUnregistered::test_untracked" in item for item in problems)


def test_nested_fences_cannot_hide_an_obligation(tmp_path: Path) -> None:
    from test_skill_lib_boundary_runner import _repo

    root = _repo(tmp_path, "def test_probe():\n    pass\n", [{"id": "check_probe", "function": "test_probe"}])
    source = root / "src/pkg/feature.py"
    original = source.read_text()
    source.write_text(original.replace("# === CONTRACTS ===", "# === CONTRACTS ===\n# id: hidden\n#   given: x\n#   then: y\n# === CONTRACTS ==="))
    ok, problems = audit_repository(root)
    assert not ok and any("nested" in item for item in problems)

    for malformed in ("# === CONTRACTS ==", "# == CONTRACTS ==="):
        source.write_text(original + malformed + "\n# id: dropped\n#   given: x\n#   then: y\n# === END CONTRACTS ===\n")
        ok, problems = audit_repository(root)
        assert not ok and any("malformed declaration fence" in item for item in problems)
    for malformed in ("# id:", "# id: two words", "# id missing_colon"):
        source.write_text(original.replace("# === END CONTRACTS ===", malformed + "\n#   given: x\n#   then: y\n# === END CONTRACTS ==="))
        ok, problems = audit_repository(root)
        assert not ok and any("malformed id" in item for item in problems)
    source.write_text(original)
    (root / "tests/test_helpers.py").write_text("class Helper:\n    def test_helper(self): pass\nclass TestDisabled:\n    __test__ = False\n    def test_disabled(self): pass\nclass TestTypedDisabled:\n    __test__: bool = False\n    def test_disabled(self): pass\ndef helper():\n    class TestNested:\n        def test_nested(self): pass\n")
    ok, problems = audit_repository(root)
    assert ok, problems
    (root / "tests/test_inherited.py").write_text("class Base:\n    def test_inherited(self): assert False\nclass TestChild(Base):\n    pass\n")
    ok, problems = audit_repository(root)
    assert not ok and any("inherited class check" in item for item in problems)
    inherited = root / "tests/test_inherited.py"
    for declaration in ("__test__ = False", "__test__: bool = False"):
        inherited.write_text(f"class Base:\n    {declaration}\n    def test_hidden(self): assert False\nclass TestChild(Base):\n    pass\n")
        ok, problems = audit_repository(root)
        assert ok, problems
    inherited.write_text("class A:\n    __test__ = False\n    def test_hidden(self): pass\nclass B(A): pass\nclass C(A):\n    __test__ = True\nclass TestChild(B, C): pass\n")
    ok, problems = audit_repository(root)
    assert not ok and any("TestChild::test_hidden" in item for item in problems)
    for code, label in (
        ("def hidden(): assert False\ntest_aliased = hidden\n", "unresolved executable alias"),
        ("class Helper:\n    __test__ = True\n    def test_explicit(self): pass\n", "Helper::test_explicit"),
        ("class TestAlias:\n    def hidden(self): pass\n    test_aliased = hidden\n", "TestAlias::test_aliased"),
    ):
        inherited.write_text(code)
        ok, problems = audit_repository(root)
        assert not ok and any(label in item for item in problems), problems
    inherited.write_text("test_data = [1, 2]\n")
    ok, problems = audit_repository(root)
    assert ok, problems
    inherited.write_text("__test__ = False\ndef test_disabled(): assert False\n")
    ok, problems = audit_repository(root)
    assert ok, problems
# ratios: loc_comments=113:42 imports_exports=5:5 calls_definitions=65:5
