# === MODULE_BUILD ===
# id: ucns_current_lexical_sources
#   module_name: lexical_sources
#   module_kind: adapter
#   summary: freezes and validates the exact xkcd Simple Writer 0.2.1 floor artifact and OEWN 2025 Core source identity selected by current UCNS lexical architecture
#   owner: Erin Spencer
#   public_surface: XKCDSimpleWriterReceipt, OEWNCoreReceipt, load_xkcd_simplewriter, quoted_xkcd_payload, verify_oewn_2025_core, current_lexical_source_receipts
#   internal_surface: _canonical_bytes, _tree_digest, _git
#   auth_boundary: read-only validation of packaged xkcd bytes and caller-supplied OEWN checkout
#   storage_boundary: packaged immutable source bytes; external OEWN checkout read only
#   network_boundary: none during validation; acquisition is a separate explicit operation
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_lexical_sources
#   rollout: prerequisite for current lexical word-gonol construction; no definition materialization before both receipts validate
#   rollback: remove current source adapter and packaged xkcd artifact without altering deprecated NGSL evidence
#   requires: none
#   since: 2026-08-18
#   unresolved: authoritative mapping of 3,634 accepted xkcd forms to 1,000 word families; xkcd word-list-specific license statement
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: xkcd_floor_bytes_are_exact_and_source_ordered
#   given: the current xkcd lexical-floor candidate is loaded
#   then: exact official Simple Writer 0.2.1 bytes, digest, version, 3,634 unique forms, source order, attribution, and license boundary are validated without inventing a 1,000-family mapping
#   class: evidence
#   since: 2026-08-18
#
# id: oewn_core_receipt_is_exact_release_identity
#   given: the current OEWN lexical-semantic source is verified
#   then: the checkout, 2025 release tag, complete Core YAML tree digest and file count match the frozen identity and Namenet or proper-name extensions are not consumed
#   class: evidence
#   since: 2026-08-18
#
# id: current_lexical_sources_precede_materialization
#   given: current lexical source receipts are requested
#   then: both selected source identities validate together before any word, morphology, definition, or recursion output is authorized
#   class: safety
#   since: 2026-08-18
#
# id: xkcd_receipt_matches_packaged_bytes
#   given: a quoted xkcd payload is requested from a receipt
#   then: packaged official bytes, digest, and quoted word list agree with the receipt or minting fails closed
#   class: evidence
#   since: 2026-08-19
# === END CONTRACTS ===

"""Exact source custody for the current UCNS lexical recursion program.

Usage::

    xkcd, oewn = current_lexical_source_receipts("/cache/english-wordnet")
    words = load_xkcd_simplewriter().surface_forms

The OEWN checkout must already be at the exact detached release commit. This
module performs no network access and writes no files.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from importlib.resources import files
import json
from pathlib import Path
import re
import subprocess

XKCD_WORDS_RESOURCE = "data/xkcd_simplewriter_words_0_2_1.js"
XKCD_ATTRIBUTION_RESOURCE = "data/XKCD_SIMPLEWRITER_ATTRIBUTION.txt"
XKCD_SOURCE_URL = "https://xkcd.com/simplewriter/words.js"
XKCD_INTERFACE_URL = "https://xkcd.com/simplewriter/"
XKCD_LICENSE_URL = "https://xkcd.com/license.html"
XKCD_VERSION = "0.2.1"
XKCD_BYTES = 26_180
XKCD_SHA256 = "8705ddff1b3fc3feb3ac902e0fce763321b12ead2569bc38292e39d9ece24873"
XKCD_SURFACE_COUNT = 3_634
XKCD_DECLARED_FAMILY_COUNT = 1_000
XKCD_STANDING = "source-pinned-lexical-floor-candidate"

OEWN_REPOSITORY = "globalwordnet/english-wordnet"
OEWN_TAG = "2025-edition"
OEWN_COMMIT = "dc343f2683279ecbb13fab4e2fd778d7b162d287"
OEWN_LICENSE = "Princeton WordNet License plus CC BY 4.0"
OEWN_CORE_TREE_SHA256 = "3a46546a1ffbb4aed98990535ad5155c69be12ad09fdf093701b257d2a3e468f"
OEWN_CORE_FILE_COUNT = 73
OEWN_CORE_STANDING = "source-pinned-primary-lexical-semantic-corpus"

_WORDS_PATTERN = re.compile(
    r'/\*\*\n \*\n \* XKCD Simple Writer Word List 0\.2\.1\n \*/\n'
    r'window\.__WORDS = "([^"]*)";\n?'
)


class LexicalSourceError(ValueError):
    """Raised when selected lexical source custody cannot be replayed exactly."""


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"


@dataclass(frozen=True, slots=True)
class XKCDSimpleWriterReceipt:
    source_url: str
    interface_url: str
    version: str
    byte_count: int
    sha256: str
    surface_forms: tuple[str, ...]
    attribution_sha256: str
    license_url: str
    license_identity: str
    family_count: int
    family_mapping_available: bool
    standing: str = XKCD_STANDING

    def as_payload(self) -> dict[str, object]:
        return {
            "source_url": self.source_url,
            "interface_url": self.interface_url,
            "version": self.version,
            "byte_count": self.byte_count,
            "sha256": self.sha256,
            "surface_forms": list(self.surface_forms),
            "attribution_sha256": self.attribution_sha256,
            "license_url": self.license_url,
            "license_identity": self.license_identity,
            "family_count": self.family_count,
            "family_mapping_available": self.family_mapping_available,
            "standing": self.standing,
        }

    @property
    def receipt_id(self) -> str:
        return "ucns.xkcd-simplewriter-receipt:sha256:" + sha256(
            _canonical_bytes(self.as_payload())
        ).hexdigest()


@dataclass(frozen=True, slots=True)
class OEWNCoreReceipt:
    repository: str
    tag: str
    commit: str
    license_identity: str
    core_tree_sha256: str
    core_file_count: int
    source_scope: str
    standing: str = OEWN_CORE_STANDING

    def as_payload(self) -> dict[str, object]:
        return {
            "repository": self.repository, "tag": self.tag,
            "commit": self.commit, "license_identity": self.license_identity,
            "core_tree_sha256": self.core_tree_sha256,
            "core_file_count": self.core_file_count,
            "source_scope": self.source_scope, "standing": self.standing,
        }

    @property
    def receipt_id(self) -> str:
        return "ucns.oewn-core-receipt:sha256:" + sha256(
            _canonical_bytes(self.as_payload())
        ).hexdigest()


def load_xkcd_simplewriter() -> XKCDSimpleWriterReceipt:
    """Load exact packaged official bytes and preserve their surface order."""

    package = files("ucns")
    payload = package.joinpath(XKCD_WORDS_RESOURCE).read_bytes()
    attribution = package.joinpath(XKCD_ATTRIBUTION_RESOURCE).read_bytes()
    if len(payload) != XKCD_BYTES or sha256(payload).hexdigest() != XKCD_SHA256:
        raise LexicalSourceError("xkcd Simple Writer source bytes mismatch")
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise LexicalSourceError("xkcd Simple Writer source is not strict UTF-8") from exc
    match = _WORDS_PATTERN.fullmatch(text)
    if match is None:
        raise LexicalSourceError("xkcd Simple Writer source syntax or version mismatch")
    surface_forms = tuple(match.group(1).split("|"))
    if len(surface_forms) != XKCD_SURFACE_COUNT or len(set(surface_forms)) != len(surface_forms):
        raise LexicalSourceError("xkcd Simple Writer surface inventory mismatch")
    if any(not value or value != value.strip() for value in surface_forms):
        raise LexicalSourceError("xkcd Simple Writer contains an invalid surface")
    return XKCDSimpleWriterReceipt(
        source_url=XKCD_SOURCE_URL,
        interface_url=XKCD_INTERFACE_URL,
        version=XKCD_VERSION,
        byte_count=len(payload),
        sha256=sha256(payload).hexdigest(),
        surface_forms=surface_forms,
        attribution_sha256=sha256(attribution).hexdigest(),
        license_url=XKCD_LICENSE_URL,
        license_identity="Creative Commons Attribution-NonCommercial 2.5; artifact-specific applicability hmmm",
        family_count=XKCD_DECLARED_FAMILY_COUNT,
        family_mapping_available=False,
    )


def quoted_xkcd_payload(source: XKCDSimpleWriterReceipt) -> str:
    """Return the official quoted word list after checking packaged bytes."""

    if not isinstance(source, XKCDSimpleWriterReceipt):
        raise TypeError("source must be an XKCDSimpleWriterReceipt")
    package = files("ucns")
    payload = package.joinpath(XKCD_WORDS_RESOURCE).read_bytes()
    if (
        len(payload) != source.byte_count
        or sha256(payload).hexdigest() != source.sha256
        or sha256(payload).hexdigest() != XKCD_SHA256
    ):
        raise LexicalSourceError("xkcd receipt does not match packaged official bytes")
    try:
        text = payload.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise LexicalSourceError("xkcd Simple Writer source is not strict UTF-8") from exc
    match = _WORDS_PATTERN.fullmatch(text)
    if match is None:
        raise LexicalSourceError("xkcd Simple Writer source syntax or version mismatch")
    quoted = match.group(1)
    if quoted != "|".join(source.surface_forms):
        raise LexicalSourceError("xkcd surfaces do not reconstruct the official quoted payload")
    official = load_xkcd_simplewriter()
    if (
        source.source_url != official.source_url
        or source.interface_url != official.interface_url
        or source.version != official.version
        or source.attribution_sha256 != official.attribution_sha256
        or source.license_url != official.license_url
        or source.license_identity != official.license_identity
        or source.family_count != official.family_count
        or source.family_mapping_available
        or source.standing != official.standing
        or source.receipt_id != official.receipt_id
    ):
        raise LexicalSourceError("xkcd receipt provenance does not match the official packaged source")
    return quoted


def _git(root: Path, *arguments: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(root), *arguments], text=True,
            stderr=subprocess.STDOUT,
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise LexicalSourceError("OEWN Git identity verification failed") from exc


def _tree_digest(root: Path) -> tuple[str, int]:
    paths = tuple(sorted(root.rglob("*.yaml")))
    digest = sha256()
    for path in paths:
        relative = path.relative_to(root).as_posix().encode("utf-8")
        payload = path.read_bytes()
        digest.update(len(relative).to_bytes(4, "big"))
        digest.update(relative)
        digest.update(len(payload).to_bytes(8, "big"))
        digest.update(payload)
    return digest.hexdigest(), len(paths)


def verify_oewn_2025_core(source_repo: str | Path) -> OEWNCoreReceipt:
    """Verify exact OEWN 2025 Core checkout without consuming extensions."""

    root = Path(source_repo).resolve()
    if _git(root, "rev-parse", "HEAD") != OEWN_COMMIT:
        raise LexicalSourceError("OEWN checkout commit mismatch")
    if _git(root, "rev-list", "-n", "1", OEWN_TAG) != OEWN_COMMIT:
        raise LexicalSourceError("OEWN release tag mismatch")
    changed = subprocess.run(
        ["git", "-C", str(root), "diff", "--quiet", "HEAD", "--", "src/yaml"],
        check=False,
    )
    if changed.returncode != 0 or _git(root, "ls-files", "--others", "--", "src/yaml"):
        raise LexicalSourceError("OEWN Core source tree is not clean")
    digest, count = _tree_digest(root / "src" / "yaml")
    if digest != OEWN_CORE_TREE_SHA256 or count != OEWN_CORE_FILE_COUNT:
        raise LexicalSourceError("OEWN Core source tree identity mismatch")
    return OEWNCoreReceipt(
        repository=OEWN_REPOSITORY,
        tag=OEWN_TAG,
        commit=OEWN_COMMIT,
        license_identity=OEWN_LICENSE,
        core_tree_sha256=digest,
        core_file_count=count,
        source_scope="src/yaml Core only; Namenet and proper-name extensions excluded",
    )


def current_lexical_source_receipts(
    oewn_source_repo: str | Path,
) -> tuple[XKCDSimpleWriterReceipt, OEWNCoreReceipt]:
    """Validate both selected source identities as one prerequisite gate."""

    return load_xkcd_simplewriter(), verify_oewn_2025_core(oewn_source_repo)


__all__ = [
    "OEWN_COMMIT", "OEWN_CORE_FILE_COUNT", "OEWN_CORE_TREE_SHA256",
    "OEWN_LICENSE", "OEWN_REPOSITORY", "OEWN_TAG", "LexicalSourceError",
    "OEWNCoreReceipt", "XKCDSimpleWriterReceipt", "current_lexical_source_receipts",
    "load_xkcd_simplewriter", "quoted_xkcd_payload", "verify_oewn_2025_core",
]
