# ratios: loc_comments=71:10 imports_exports=6:1 calls_definitions=32:2
# === CHECKS ===
# id: check_distribution_replay_inputs
#   proves: distributions_retain_exact_replay_inputs
#   call: self::test_distribution_replay_inputs_fail_closed
#   requires: python3, pytest
#   timeout: 10
#   mutates: temporary_path
#   cleanup: pytest temporary_path
# === END CHECKS ===

"""Build small archive fixtures; missing evidence must fail independently of Twine."""

import importlib.util
import io
from pathlib import Path
import tarfile
import zipfile

import pytest


SPEC = importlib.util.spec_from_file_location("distribution_audit", Path(__file__).parents[1] / "tools/verify_distributions.py")
assert SPEC is not None and SPEC.loader is not None
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def _archives(root, sdist, wheel, *, omit="", altered="", extra="", sdist_extra="", wheel_omit="", wheel_altered=""):
    with tarfile.open(sdist, "w:gz") as archive:
        for name, data in audit.expected_files(root).items():
            if name == omit:
                continue
            if name == altered:
                data += b"drift"
            member = tarfile.TarInfo(f"ucns-0/{name}")
            member.size = len(data)
            archive.addfile(member, io.BytesIO(data))
        if sdist_extra:
            member = tarfile.TarInfo(f"ucns-0/{sdist_extra}")
            member.size = 10
            archive.addfile(member, io.BytesIO(b"unexpected"))
    with zipfile.ZipFile(wheel, "w") as archive:
        for name, data in audit.expected_files(root).items():
            if name.startswith("src/ucns/"):
                archive.writestr(name.removeprefix("src/"), data)
        metadata = {
            "METADATA": b"Metadata-Version: 2.4\nName: ucns\nVersion: 0\n",
            "WHEEL": b"Wheel-Version: 1.0\nRoot-Is-Purelib: true\nTag: py3-none-any\n",
            "RECORD": b"",
            "licenses/LICENSE": (root / "LICENSE").read_bytes(),
        }
        for name, data in metadata.items():
            if name != wheel_omit:
                archive.writestr(f"ucns-0.dist-info/{name}", data + (b"drift" if name == wheel_altered else b""))
        if extra:
            archive.writestr(extra, b"unexpected")


def test_distribution_replay_inputs_fail_closed(tmp_path: Path) -> None:
    root = tmp_path / "repo"
    root.mkdir()
    for name in (*audit.ROOT_INPUTS, "src/ucns/__init__.py", "generated/receipt.json", "docs/preregistration.md", ".agents/skills/msdmd/parsers/universal.py"):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture\n")
    sdist, wheel = tmp_path / "ucns.tar.gz", tmp_path / "ucns.whl"
    _archives(root, sdist, wheel)
    assert audit.verify_distributions(root, sdist, wheel) == []
    for options, message in (
        ({"omit": "LICENSE"}, "missing LICENSE"),
        ({"altered": "LICENSE"}, "altered LICENSE"),
        ({"wheel_omit": "licenses/LICENSE"}, "missing wheel metadata"),
        ({"wheel_altered": "licenses/LICENSE"}, "altered wheel license"),
        ({"wheel_omit": "METADATA"}, "missing wheel metadata"),
        ({"wheel_omit": "WHEEL"}, "missing wheel metadata"),
        ({"wheel_omit": "RECORD"}, "missing wheel metadata"),
        ({"sdist_extra": "setup.py"}, "unexpected payload setup.py"),
        ({"extra": "ucns-0.dist-info/entry_points.txt"}, "unexpected wheel metadata"),
    ):
        _archives(root, sdist, wheel, **options)
        assert any(message in problem for problem in audit.verify_distributions(root, sdist, wheel)), options
    for key, name, expected in (("omit", "generated/receipt.json", "missing"), ("altered", "docs/preregistration.md", "altered"), ("extra", "ucns/lexical.py", "unexpected")):
        _archives(root, sdist, wheel, **{key: name})
        assert any(expected in problem for problem in audit.verify_distributions(root, sdist, wheel))
    _archives(root, sdist, wheel, extra="../escaped.py")
    assert any("unsafe" in problem for problem in audit.verify_distributions(root, sdist, wheel))
    _archives(root, sdist, wheel)
    with zipfile.ZipFile(wheel, "a") as archive, pytest.warns(UserWarning, match="Duplicate"):
        archive.writestr("ucns/__init__.py", b"duplicate")
    assert any("duplicate" in problem for problem in audit.verify_distributions(root, sdist, wheel))
# ratios: loc_comments=71:10 imports_exports=6:1 calls_definitions=32:2
