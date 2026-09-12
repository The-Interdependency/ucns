# ratios: loc_comments=430:53 imports_exports=12:4 calls_definitions=216:16
# === MODULE_BUILD ===
# id: skill_lib_contract_audit
#   module_name: verify_skill_lib_contracts
#   module_kind: instrument
#   summary: performs a no-exec reconciliation of skill-lib MODULE_BUILD, CONTRACTS, and CHECKS declarations
#   owner: Erin Spencer
#   public_surface: command-line audit
#   internal_surface: parse_blocks, audit_repository
#   auth_boundary: none
#   storage_boundary: read
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_skill_lib_contracts.py
#   rollout: required CI gate
#   rollback: remove workflow invocation and script
#   since: 2026-07-21
#   unresolved: mutation-level verification beyond planted graph gaps
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: contract_audit_is_no_exec
#   given: the repository contract graph is audited
#   then: Python source is parsed without importing product or test modules
#   class: safety
#   since: 2026-07-21
#
# id: contract_audit_reports_graph_gaps
#   given: a contract, check target, or self call is missing or unknown
#   then: the audit reports the gap and exits nonzero, including empty input, malformed syntax/fences, and unsupported class-based tests
#   class: evidence
#   since: 2026-07-21
#
# id: contract_audit_accepts_closed_graph
#   given: every declared contract has a resolving check and every check names known contracts
#   then: the audit exits successfully
#   class: evidence
#   since: 2026-07-21
# === END CONTRACTS ===

"""No-exec contract reconciliation using the vendored canonical msdmd parser.

Usage: ``python tools/verify_skill_lib_contracts.py .``. Product and test files
are parsed, never imported. Only the pinned parser shipped beside this tool is
loaded. Unsupported class-based test targets are visible gaps, not coverage.
"""

from __future__ import annotations

import ast
import configparser
import importlib.util
import re
import shlex
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 verification dependency.
    import tomli as tomllib

BLOCK_RE = re.compile(r"^\s*#\s*===\s*(MODULE_BUILD|CONTRACTS|CHECKS)\s*===\s*$")
END_RE = re.compile(r"^\s*#\s*===\s*END\s+(MODULE_BUILD|CONTRACTS|CHECKS)\s*===\s*$")
DECLARATION_FENCE_RE = re.compile(r"^\s*#\s*=+\s*(?:END\s+)?(?:MODULE_BUILD|CONTRACTS|CHECKS)\b")
ID_LIKE_RE = re.compile(r"^\s*#\s*id\b")
ID_RE = re.compile(r"^#\s*id:\s*([a-z_][a-z0-9_]*)\s*$")
PARSER_PATH = Path(__file__).resolve().parents[1] / ".agents/skills/msdmd/parsers/universal.py"
_SPEC = importlib.util.spec_from_file_location("_ucns_canonical_msdmd", PARSER_PATH)
if _SPEC is None or _SPEC.loader is None:
    raise RuntimeError("canonical msdmd parser unavailable")
_PARSER = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_PARSER)
REQUIRED_MODULE_FIELDS = {
    "module_name",
    "module_kind",
    "summary",
    "owner",
    "public_surface",
    "internal_surface",
    "auth_boundary",
    "storage_boundary",
    "network_boundary",
    "user_data_boundary",
    "admin_only",
    "tests",
    "rollout",
    "rollback",
}
REQUIRED_CONTRACT_FIELDS = {"given", "then"}
REQUIRED_CHECK_FIELDS = {"proves", "call", "timeout", "mutates", "cleanup"}
UNKNOWN_TEST_SETTING = object()


@dataclass(frozen=True)
class Entry:
    block: str
    source: Path
    fields: Dict[str, str]

    @property
    def id(self) -> str:
        return self.fields["id"]


def _source_files(root: Path) -> Iterable[Path]:
    # Reconcile both updated canonical parser implementations beside their owner.
    for name in ("universal.py", "universal.ts"):
        parser = root / ".agents/skills/msdmd/parsers" / name
        if parser.is_file():
            yield parser
    for base in (root / "src", root / "tools", root / "tests"):
        if base.exists():
            yield from (path for path in sorted(base.rglob("*.py")) if "__pycache__" not in path.parts)


def parse_blocks(path: Path) -> List[Entry]:
    """Check fence integrity, then delegate entry grammar to canonical msdmd."""
    text = path.read_text(encoding="utf-8")
    marker = _PARSER.marker_for(path)
    if marker not in {"#", "//"}:
        raise ValueError(f"unsupported declaration source: {path}")
    active: str | None = None
    declarations = 0
    for line in text.splitlines():
        raw = "#" + line[len(marker):] if line.startswith(marker) else line
        start = BLOCK_RE.match(raw)
        if start:
            if active is not None:
                raise ValueError(f"{path}: nested {start.group(1)} inside {active}")
            active = start.group(1)
            continue
        end = END_RE.match(raw)
        if end:
            if active != end.group(1):
                raise ValueError(f"{path}: mismatched END {end.group(1)}")
            active = None
            continue
        if DECLARATION_FENCE_RE.match(raw):
            raise ValueError(f"{path}: malformed declaration fence: {raw.strip()}")
        if active is not None and ID_LIKE_RE.match(raw):
            if ID_RE.fullmatch(raw) is None:
                raise ValueError(f"{path}: malformed id declaration: {raw.strip()}")
            declarations += 1
    if active is not None:
        raise ValueError(f"{path}: unterminated {active} block")
    entries = [
        Entry(block, path, fields)
        for block in ("MODULE_BUILD", "CONTRACTS", "CHECKS")
        for fields in _PARSER.parse_text(text, block, marker=marker)
    ]
    if len(entries) != declarations:
        raise ValueError(f"{path}: declarations lost by canonical parser")
    return entries


def _target_names(target: ast.AST) -> list[str]:
    if isinstance(target, ast.Name):
        return [target.id]
    if isinstance(target, (ast.Tuple, ast.List)):
        return [name for item in target.elts for name in _target_names(item)]
    if isinstance(target, ast.Starred):
        return _target_names(target.value)
    return []


def _bindings(body: list[ast.stmt]) -> dict[str, str]:
    """Track direct namespace bindings; callable aliases remain unsupported."""
    bindings = {}
    for node in body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bindings[node.name] = "class" if isinstance(node, ast.ClassDef) else "function"
        elif isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None:
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            kind = "literal" if isinstance(node.value, (ast.Constant, ast.List, ast.Tuple, ast.Set, ast.Dict)) else "unknown"
            for target in targets:
                for name in _target_names(target):
                    bindings[name] = kind
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                bindings[alias.asname or alias.name.split(".", 1)[0]] = "literal" if isinstance(node, ast.Import) else "unknown"
        elif isinstance(node, ast.AugAssign):
            for name in _target_names(node.target):
                bindings[name] = "unknown"
        elif isinstance(node, ast.Delete):
            for target in node.targets:
                for name in _target_names(target):
                    bindings.pop(name, None)
    return bindings


_COMPOUND_STATEMENTS = (ast.If, ast.For, ast.AsyncFor, ast.While, ast.Try, ast.With, ast.AsyncWith, ast.Match, getattr(ast, "TryStar", ast.Try))


def _header_bindings(node: ast.AST, *, named_only: bool = False) -> set[str]:
    """Include assignment targets in statement headers, without executing them."""
    names: set[str] = set()
    if isinstance(node, ast.NamedExpr):
        names.update(_target_names(node.target))
    for field, value in ast.iter_fields(node):
        if field in {"body", "orelse", "finalbody"}:
            continue
        values = value if isinstance(value, list) else [value]
        for item in values:
            if isinstance(item, ast.AST):
                if not named_only and isinstance(item, ast.Name) and isinstance(item.ctx, ast.Store):
                    names.add(item.id)
                if not named_only and isinstance(item, (ast.MatchAs, ast.MatchStar, ast.ExceptHandler)) and item.name:
                    names.add(item.name)
                if not named_only and isinstance(item, ast.MatchMapping) and item.rest:
                    names.add(item.rest)
                names.update(_header_bindings(item, named_only=named_only))
    return names


def _conditional_test_names(body: list[ast.stmt]) -> set[str]:
    """Find possible module/class test bindings without entering function bodies."""
    names: set[str] = set()
    for node in body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("test"):
                names.add(node.name)
        elif isinstance(node, ast.ClassDef):
            found, setting = _test_setting(node)
            if not (found and setting is False) and (node.name.startswith("Test") or node.bases or setting is True):
                names.add(node.name)
        elif isinstance(node, ast.If) and isinstance(node.test, ast.Constant):
            names.update(_conditional_test_names(node.body if node.test.value else node.orelse))
        elif isinstance(node, _COMPOUND_STATEMENTS):
            groups = [getattr(node, name, []) for name in ("body", "orelse", "finalbody")]
            groups.extend(handler.body for handler in getattr(node, "handlers", []))
            groups.extend(case.body for case in getattr(node, "cases", []))
            for group in groups:
                names.update(_conditional_test_names(group))
        else:
            for name, kind in _bindings([node]).items():
                if name in {"*", "__test__"} or name.startswith("test") and kind != "literal" or name.startswith("Test") and kind == "unknown":
                    names.add(name)
        header = _header_bindings(node, named_only=not isinstance(node, _COMPOUND_STATEMENTS))
        names.update(name for name in header if name == "__test__" or name.startswith(("test", "Test")))
    return names


def _conditional_surface(body: list[ast.stmt]) -> set[str]:
    names = _conditional_test_names([node for node in body if isinstance(node, _COMPOUND_STATEMENTS)])
    for node in body:
        names.update(name for name in _header_bindings(node, named_only=True) if name == "__test__" or name.startswith(("test", "Test")))
    return names


def _class_mro(name: str, classes: dict[str, ast.ClassDef], active=()) -> list[str] | None:
    """Compute local C3 order; unresolved bases and inconsistent orders are gaps."""
    if name == "object":
        return [name]
    if name not in classes or name in active:
        return None
    cls = classes[name]
    if any(not isinstance(base, ast.Name) for base in cls.bases):
        return None
    bases = [base.id for base in cls.bases] or ["object"]
    if len(set(bases)) != len(bases):
        return None
    parents = [_class_mro(base, classes, (*active, name)) for base in bases]
    if any(parent is None for parent in parents):
        return None
    sequences = [list(parent) for parent in parents] + [list(bases)]
    result = [name]
    while any(sequences):
        candidates = [sequence[0] for sequence in sequences if sequence]
        candidate = next((head for head in candidates if all(head not in sequence[1:] for sequence in sequences)), None)
        if candidate is None:
            return None
        result.append(candidate)
        for sequence in sequences:
            if sequence and sequence[0] == candidate:
                sequence.pop(0)
    return result


def _test_setting(cls: ast.ClassDef | ast.Module) -> tuple[bool, object]:
    found, value = False, None
    for node in cls.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)) and node.value is not None:
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any("__test__" in _target_names(target) for target in targets):
                found = True
                try:
                    value = ast.literal_eval(node.value)
                except (ValueError, TypeError, SyntaxError):
                    value = UNKNOWN_TEST_SETTING
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == "__test__":
            found, value = True, UNKNOWN_TEST_SETTING
        elif isinstance(node, ast.AugAssign) and "__test__" in _target_names(node.target):
            found, value = True, UNKNOWN_TEST_SETTING
        elif isinstance(node, ast.Delete) and any("__test__" in _target_names(target) for target in node.targets):
            found, value = False, None
    return found, value


def _defined_functions(path: Path) -> Set[str]:
    """Return top-level functions without importing or executing the module."""

    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found, setting = _test_setting(tree)
    if found and not setting:
        return set()
    return {name for name, kind in _bindings(tree.body).items() if kind == "function"}


def _missing(fields: Dict[str, str], required: Set[str]) -> Set[str]:
    return {name for name in required if not fields.get(name)}


def _collection_config_problems(root: Path) -> list[str]:
    """The no-exec graph supports the repository's bounded default collection."""
    problems = []
    alternatives = {"pytest.toml", ".pytest.toml", "pytest.ini", ".pytest.ini", "tox.ini", "setup.cfg"}
    for base in (root, root / "tests"):
        paths = base.iterdir() if base == root else base.rglob("*")
        if not base.exists():
            continue
        for path in paths:
            if path.is_file() and path.name == "conftest.py":
                problems.append(f"GAP unsupported conftest collection/plugin surface: {path}")
            if path.is_file() and path.name in alternatives:
                if path.name in {"setup.cfg", "tox.ini"}:
                    try:
                        parser = configparser.ConfigParser(interpolation=None)
                        parser.read_string(path.read_text(encoding="utf-8"))
                        section = "tool:pytest" if path.name == "setup.cfg" else "pytest"
                        if not parser.has_section(section):
                            continue  # Setuptools emits setup.cfg with only egg_info.
                    except (OSError, UnicodeError, configparser.Error) as error:
                        problems.append(f"GAP invalid pytest collection configuration: {path}: {error}")
                        continue
                problems.append(f"GAP unsupported pytest collection configuration: {path}; use root pyproject.toml with default collection")
    path = root / "pyproject.toml"
    if not path.exists():
        problems.append("GAP pytest collection requires explicit testpaths = ['tests'] in root pyproject.toml")
        return problems
    try:
        document = tomllib.loads(path.read_text(encoding="utf-8"))
        section = document.get("tool", {}).get("pytest", {})
        if set(section) - {"ini_options"}:
            problems.append(f"GAP unsupported native pytest collection configuration: {path}")
        config = section.get("ini_options", {})
        if "testpaths" not in config:
            problems.append("GAP pytest collection requires explicit testpaths = ['tests']")
        if config.get("required_plugins"):
            problems.append("GAP unsupported pytest plugin collection configuration")
        defaults = {"python_files": ["test_*.py", "*_test.py"], "python_classes": ["Test"], "python_functions": ["test"], "testpaths": ["tests"]}
        for name, expected in defaults.items():
            if name in config:
                actual = config[name].split() if isinstance(config[name], str) else config[name]
                if actual != expected:
                    problems.append(f"GAP unsupported pytest collection setting {name}: {actual!r}")
        options = config.get("addopts", [])
        options = shlex.split(options) if isinstance(options, str) else options
        if not isinstance(options, list) or any(option not in {"-q", "-v", "-vv", "-ra", "--strict-markers", "--strict-config"} for option in options):
            problems.append("GAP unsupported pytest addopts; collection-changing arguments are outside the audited boundary")
    except (OSError, UnicodeError, ValueError, AttributeError, TypeError) as error:
        problems.append(f"GAP invalid pytest collection configuration: {error}")
    return problems


def audit_repository(root: Path) -> Tuple[bool, List[str]]:
    root = root.resolve()
    entries: List[Entry] = []
    problems: List[str] = _collection_config_problems(root)
    paths = tuple(_source_files(root))
    trees: Dict[Path, ast.Module] = {}
    if not paths:
        problems.append(f"GAP empty source/test tree: {root}")
    for path in paths:
        try:
            if path.suffix == ".py":
                trees[path] = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            path_entries = parse_blocks(path)
        except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
            problems.append(f"GAP parse {type(exc).__name__}: {exc}")
            continue

        entries.extend(path_entries)
        if (path.is_relative_to(root / "src") or path.is_relative_to(root / "tools")
                or path.is_relative_to(root / ".agents/skills/msdmd/parsers")):
            declared = {entry.block for entry in path_entries}
            for required_block in ("MODULE_BUILD", "CONTRACTS"):
                if required_block not in declared:
                    problems.append(f"GAP {path} missing {required_block} declaration block")

    ids: Dict[str, Entry] = {}
    for entry in entries:
        if not entry.id:
            problems.append(f"GAP {entry.source}: entry without id")
            continue
        if entry.id in ids:
            problems.append(f"GAP duplicate id {entry.id}: {ids[entry.id].source} and {entry.source}")
        ids[entry.id] = entry
        required = {
            "MODULE_BUILD": REQUIRED_MODULE_FIELDS,
            "CONTRACTS": REQUIRED_CONTRACT_FIELDS,
            "CHECKS": REQUIRED_CHECK_FIELDS,
        }[entry.block]
        missing = _missing(entry.fields, required)
        if missing:
            problems.append(f"GAP {entry.id} missing fields: {', '.join(sorted(missing))}")

    contracts = {entry.id: entry for entry in entries if entry.block == "CONTRACTS"}
    checks = [entry for entry in entries if entry.block == "CHECKS"]
    if not contracts or not checks:
        problems.append("GAP empty contract/check graph cannot establish evidence")
    proved: Set[str] = set()

    for check in checks:
        targets = [target.strip() for target in check.fields.get("proves", "").split(",") if target.strip()]
        for target in targets:
            if target not in contracts:
                problems.append(f"GAP {check.id} claims unknown contract: {target}")
            else:
                proved.add(target)

        call = check.fields.get("call", "")
        if not call.startswith("self::"):
            problems.append(f"GAP {check.id} call is not no-exec self::fn: {call}")
        else:
            name = call[len("self::") :]
            try:
                defined = _defined_functions(check.source)
            except SyntaxError as exc:
                problems.append(f"GAP {check.id} cannot parse call source: {exc}")
            else:
                is_test_module = (
                    check.source.is_relative_to(root / "tests")
                    and (check.source.name.startswith("test_") or check.source.name.endswith("_test.py"))
                )
                if not is_test_module or not name.startswith("test"):
                    problems.append(
                        f"GAP {check.id} call does not target an executable pytest test: {call}"
                    )
                elif name not in defined:
                    problems.append(f"GAP {check.id} call does not resolve: {call}")

    for contract_id in sorted(set(contracts) - proved):
        problems.append(f"GAP {contract_id} has no CHECKS entry claiming to prove it")

    for test_path, tree in trees.items():
        if test_path.is_relative_to(root / "tests") and any(isinstance(node, ast.Name) and node.id == "pytest_plugins" for node in ast.walk(tree)):
            problems.append(f"GAP unsupported pytest plugin collection surface: {test_path}")
        if not test_path.is_relative_to(root / "tests") or not (
            test_path.name.startswith("test_") or test_path.name.endswith("_test.py")
        ):
            continue
        declared_calls = {
            entry.fields.get("call", "")[len("self::") :]
            for entry in checks
            if entry.source == test_path and entry.fields.get("call", "").startswith("self::")
        }
        found, setting = _test_setting(tree)
        conditional = _conditional_surface(tree.body)
        if found and not setting and "__test__" not in conditional:
            continue
        for name in sorted(conditional):
            problems.append(f"GAP conditional test binding {test_path}::{name}; use direct module-level test definitions")
        if setting is UNKNOWN_TEST_SETTING:
            problems.append(f"GAP dynamic test-module opt-out {test_path}")
        bindings = _bindings(tree.body)
        for name, kind in bindings.items():
            if name == "*":
                problems.append(f"GAP unresolved wildcard test-module import {test_path}")
            elif name.startswith("test"):
                if kind == "unknown":
                    problems.append(f"GAP unresolved executable alias {test_path}::{name}")
                elif kind == "function" and name not in declared_calls:
                    problems.append(f"GAP executable check {test_path}::{name} has no resolving CHECKS declaration")
            elif name.startswith("Test") and kind == "unknown":
                problems.append(f"GAP unresolved class alias {test_path}::{name}")
        classes = {node.name: node for node in tree.body if isinstance(node, ast.ClassDef) and bindings.get(node.name) == "class"}
        for cls in classes.values():
            found, setting = _test_setting(cls)
            order = _class_mro(cls.name, classes)
            conditional_opt_out = any("__test__" in _conditional_surface(classes[name].body) for name in (order or [cls.name]) if name in classes)
            if conditional_opt_out:
                problems.append(f"GAP conditional class opt-out {test_path}::{cls.name}")
            if not found and order is not None:
                for ancestor in order[1:]:
                    if ancestor in classes:
                        found, setting = _test_setting(classes[ancestor])
                        if found:
                            break
            if found and not setting and not conditional_opt_out:
                continue
            if setting is UNKNOWN_TEST_SETTING:
                problems.append(f"GAP dynamic class opt-out {test_path}::{cls.name}")
                continue
            if order is None:
                # unittest.TestCase collection does not require a Test prefix.
                # Unknown external bases can carry executable tests under any name.
                problems.append(f"GAP inherited class check {test_path}::{cls.name}; unresolved base surface")
                continue
            if not cls.name.startswith("Test") and setting is not True:
                continue
            inherited = [classes[name] for name in order if name in classes]
            for ancestor in inherited:
                for name in sorted(_conditional_surface(ancestor.body)):
                    problems.append(f"GAP conditional class check {test_path}::{cls.name}::{name}")
            if any(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in {"__init__", "__new__"} for ancestor in inherited for node in ancestor.body):
                continue
            methods = {}
            for ancestor in reversed(inherited):
                methods.update(_bindings(ancestor.body))
            for name, kind in methods.items():
                if name.startswith("test") and kind in {"function", "unknown"}:
                    label = "inherited class check" if cls.bases else "unsupported class check"
                    problems.append(f"GAP {label} {test_path}::{cls.name}::{name}; use a declared top-level self::test_fn witness")

    return not problems, problems


def main(argv: Sequence[str] | None = None) -> int:
    args = list(argv or sys.argv[1:])
    root = Path(args[0] if args else ".").resolve()
    ok, problems = audit_repository(root)
    if ok:
        print("skill-lib contract graph: closed")
        return 0
    for problem in problems:
        print(problem)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
# ratios: loc_comments=430:53 imports_exports=12:4 calls_definitions=216:16
