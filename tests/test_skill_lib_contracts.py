# ratios: loc_comments=170:60 imports_exports=9:7 calls_definitions=89:7
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
    branch = root / "tests/test_class.py"
    for code in (
        "if True:\n    def test_hidden(): assert False\n",
        "if False:\n    pass\nelse:\n    def test_hidden(): assert False\n",
        "if UNKNOWN:\n    test_hidden = helper\n",
        "for item in [1]:\n    def test_hidden(): assert False\n",
        "while UNKNOWN:\n    def test_hidden(): assert False\n",
        "try:\n    pass\nfinally:\n    def test_hidden(): assert False\n",
        "with manager():\n    def test_hidden(): assert False\n",
        "match value:\n    case 1:\n        def test_hidden(): assert False\n",
        "class TestConditional:\n    if True:\n        def test_hidden(self): assert False\n",
        "if True:\n    class TestHidden:\n        def test_hidden(self): assert False\n",
        "__test__ = False\nif True:\n    __test__ = True\n    def test_hidden(): assert False\n",
        "class TestConditional:\n    __test__ = False\n    if True:\n        __test__ = True\n        def test_hidden(self): assert False\n",
    ):
        branch.write_text(code)
        ok, problems = audit_repository(root)
        assert not ok and any("conditional" in item for item in problems), (code, problems)
    for code in (
        "if False:\n    def test_inactive(): assert False\n",
        "def helper():\n    if True:\n        def test_local(): assert False\n",
        "__test__ = False\nif True:\n    def test_disabled(): assert False\n",
    ):
        branch.write_text(code)
        ok, problems = audit_repository(root)
        assert ok, (code, problems)


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
        ("import unittest\nclass HiddenName(unittest.TestCase):\n    def test_hidden(self): assert False\n", "HiddenName"),
        ("from unittest import TestCase as Case\nclass HiddenName(Case):\n    def test_hidden(self): assert False\n", "HiddenName"),
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
# === CHECKS ===
# id: check_vendored_msdmd_field_preservation
#   proves: msdmd_python_parser_preserves_field_names
#   call: self::test_vendored_parser_retains_numeric_field_names
#   requires: python3
#   timeout: 10
#   mutates: none
#   cleanup: none
# === END CHECKS ===


def test_vendored_parser_retains_numeric_field_names() -> None:
    from tools.verify_skill_lib_contracts import _PARSER, PARSER_PATH, parse_blocks
    declarations = parse_blocks(PARSER_PATH)
    assert any(entry.block == "MODULE_BUILD" and entry.id == "msdmd_python_reference_parser" for entry in declarations)
    assert any(entry.block == "CONTRACTS" and entry.id == "msdmd_python_parser_preserves_field_names" for entry in declarations)
    text = "# === NARRATIVE ===\n# id: sample\n#   evidence_sha256: abc123\n# === END NARRATIVE ===\nraise RuntimeError('not executable input')\n"
    assert _PARSER.parse_text(text, "NARRATIVE") == [{"id": "sample", "evidence_sha256": "abc123"}]
# === CHECKS ===
# id: check_vendored_typescript_field_preservation
#   proves: msdmd_typescript_parser_preserves_field_names, contract_audit_reports_graph_gaps
#   call: self::test_vendored_typescript_parser_retains_numeric_field_names
#   requires: python3, node24
#   timeout: 10
#   mutates: filesystem
#   cleanup: tempdir_teardown
# === END CHECKS ===


def test_vendored_typescript_parser_retains_numeric_field_names(tmp_path: Path) -> None:
    import json
    import subprocess
    from tools.verify_skill_lib_contracts import parse_blocks
    helper = ROOT / ".agents/skills/msdmd/parsers/universal.ts"
    declarations = parse_blocks(helper)
    assert any(entry.block == "MODULE_BUILD" and entry.id == "msdmd_typescript_reference_parser" for entry in declarations)
    assert any(entry.block == "CONTRACTS" and entry.id == "msdmd_typescript_parser_preserves_field_names" for entry in declarations)
    marker = tmp_path / "executed"
    source = tmp_path / "inspected.ts"
    text = "// === NARRATIVE ===\n// id: sample\n//   evidence_sha256: abc123\n// === END NARRATIVE ===\n"
    source.write_text(text + 'import {writeFileSync} from "node:fs";\n' + f'writeFileSync({json.dumps(str(marker))}, "executed");\n')
    script = f"import {{parseText, parseFile}} from {json.dumps(helper.as_uri())};" + f"process.stdout.write(JSON.stringify([parseText({json.dumps(text)}, 'NARRATIVE', '//'),parseFile({json.dumps(str(source))}, 'NARRATIVE')]));"
    result = subprocess.run(["node", "--input-type=module", "--eval", script], check=True, capture_output=True, text=True)
    expected = [{"id": "sample", "evidence_sha256": "abc123"}]
    assert json.loads(result.stdout) == [expected, expected]
    assert not marker.exists(), "TypeScript parsing executed inspected source"
    broken = tmp_path / "repo/.agents/skills/msdmd/parsers/universal.ts"
    broken.parent.mkdir(parents=True)
    broken.write_text("// no declaration\nthrow new Error('must not execute');\n")
    ok, problems = audit_repository(tmp_path / "repo")
    assert not ok and any("universal.ts missing MODULE_BUILD" in item for item in problems), problems
# ratios: loc_comments=170:60 imports_exports=9:7 calls_definitions=89:7
