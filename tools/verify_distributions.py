# ratios: loc_comments=87:32 imports_exports=5:4 calls_definitions=49:5
# === MODULE_BUILD ===
# id: ucns_distribution_audit
#   module_name: verify_distributions
#   module_kind: instrument
#   summary: checks built UCNS source and wheel archive bytes against repository-owned replay inputs
#   owner: Erin Spencer
#   public_surface: verify_distributions, command-line audit
#   internal_surface: expected_files, read_archive
#   auth_boundary: none
#   storage_boundary: read-only repository and archives
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_distributions.py
#   rollout: CI artifact gate after build
#   rollback: remove tool, test, and CI invocation together
#   since: 2026-09-11
#   unresolved: semantic validity of archived certificates and independent wheel runtime replay
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: distributions_retain_exact_replay_inputs
#   given: a built sdist and wheel are compared to a UCNS source tree
#   then: missing or altered required inputs, unsafe archive members, duplicate members, and unexpected wheel payloads fail without extraction or execution
#   class: evidence
#   since: 2026-09-11
# === END CONTRACTS ===

"""Usage: ``python tools/verify_distributions.py . dist`` after a clean build.

The wheel contains the package; the sdist also contains the tests, their
evidence, preregistrations, tools, and vendored parser. Matching archive bytes
is packaging evidence only, not certificate verification or ratification.
"""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import tarfile
import zipfile


ROOT_INPUTS = ("pyproject.toml", "README.md", "AGENTS.md", "CANON.md", "CLAUDE.md", "uv.lock", "MANIFEST.in")
TREE_INPUTS = {
    "src/ucns": {".py"}, "tests": {".py"}, "tools": {".py"},
    "docs": {".md", ".json", ".jsonl", ".svg"}, "generated": {".json"},
    ".agents/skills": {".md", ".json", ".py", ".ts"},
}


def expected_files(root: Path) -> dict[str, bytes]:
    paths = {root / name for name in ROOT_INPUTS}
    for directory, suffixes in TREE_INPUTS.items():
        paths.update(path for path in (root / directory).rglob("*")
                     if path.is_file() and path.suffix in suffixes and "__pycache__" not in path.parts)
    if not any(path.is_relative_to(root / "src/ucns") for path in paths):
        raise ValueError("missing UCNS package source")
    return {path.relative_to(root).as_posix(): path.read_bytes() for path in sorted(paths)}


def read_archive(path: Path, *, wheel: bool) -> dict[str, bytes]:
    """Read regular files only; reject ambiguous names rather than extracting."""
    files: dict[str, bytes] = {}
    prefixes: set[str] = set()

    def record(name: str, data: bytes) -> None:
        parts = PurePosixPath(name).parts
        if not parts or name.startswith("/") or ".." in parts or "\\" in name:
            raise ValueError(f"unsafe archive name: {name}")
        if not wheel:
            prefixes.add(parts[0])
            if len(parts) < 2 or len(prefixes) != 1:
                raise ValueError("sdist must have one enclosing directory")
            name = "/".join(parts[1:])
        if name in files:
            raise ValueError(f"duplicate archive member: {name}")
        files[name] = data

    if wheel:
        with zipfile.ZipFile(path) as archive:
            for member in archive.infolist():
                if not member.is_dir():
                    if (member.external_attr >> 16) & 0o170000 == 0o120000:
                        raise ValueError(f"archive symlink: {member.filename}")
                    record(member.filename, archive.read(member))
    else:
        with tarfile.open(path, "r:gz") as archive:
            for member in archive:
                if member.isdir():
                    continue
                if not member.isfile():
                    raise ValueError(f"non-regular archive member: {member.name}")
                stream = archive.extractfile(member)
                if stream is None:
                    raise ValueError(f"unreadable archive member: {member.name}")
                with stream:
                    record(member.name, stream.read())
    return files


def verify_distributions(root: Path, sdist: Path, wheel: Path) -> list[str]:
    expected = expected_files(root.resolve())
    wheel_expected = {name.removeprefix("src/"): data for name, data in expected.items() if name.startswith("src/ucns/")}
    problems = []
    for path, inputs, is_wheel in ((sdist, expected, False), (wheel, wheel_expected, True)):
        try:
            actual = read_archive(path, wheel=is_wheel)
        except (OSError, ValueError, tarfile.TarError, zipfile.BadZipFile) as error:
            problems.append(f"{path.name}: {error}")
            continue
        for name, data in inputs.items():
            if name not in actual:
                problems.append(f"{path.name}: missing {name}")
            elif actual[name] != data:
                problems.append(f"{path.name}: altered {name}")
        for name in actual.keys() - inputs.keys():
            metadata = name.split("/", 1)[0].endswith(".dist-info")
            if (is_wheel and not metadata) or (not is_wheel and name.startswith("src/ucns/")):
                problems.append(f"{path.name}: unexpected payload {name}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("dist", type=Path)
    args = parser.parse_args()
    sdists, wheels = sorted(args.dist.glob("*.tar.gz")), sorted(args.dist.glob("*.whl"))
    if len(sdists) != 1 or len(wheels) != 1:
        parser.error("expected exactly one sdist and one wheel; use a clean output directory")
    problems = verify_distributions(args.root, sdists[0], wheels[0])
    print("\n".join(problems) if problems else "distribution replay inputs: exact")
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(main())
# ratios: loc_comments=87:32 imports_exports=5:4 calls_definitions=49:5
