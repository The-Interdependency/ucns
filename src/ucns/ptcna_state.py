# === MODULE_BUILD ===
# id: ucns_ptcna_candidate_state
#   module_name: ptcna_state
#   module_kind: schema
#   summary: emits and validates the candidate-scoped dense 157x7x7x53 PTCNA initialization state with deterministic provenance receipts
#   owner: Erin Spencer
#   public_surface: PTCNA_STATE_SHAPE, PTCNAStateReceiptError, build_ptcna_state_receipt, validate_ptcna_state_receipt, write_ptcna_state_receipt
#   internal_surface: canonical serialization, streaming zero-state digest, producer checkout verification
#   auth_boundary: none
#   storage_boundary: write
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_ptcna_state.py
#   rollout: explicit candidate receipt generation only; no universal UCNS or PTCNA selection
#   rollback: remove this module and export without changing the 157-position EDCM carrier or any prior candidate
#   requires: edcm_word_gonol_profile
#   since: 2026-08-17
#   unresolved: continuous seven-fold geometry, representative efficacy, and any canonical higher-gonol composition law
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: ucns_ptcna_state_has_exact_requested_shape
#   given: the PTCNA candidate receipt is built
#   then: it describes exactly 157x7x7x53 C-order little-endian float64 state with every element present and initialized to positive zero
#   class: correctness
#
# id: ucns_ptcna_receipt_is_deterministic_and_provenance_bound
#   given: the same exact UCNS producer commit and module bytes
#   then: canonical receipt bytes and state digest are byte-identical and bind the exact public-gonol provenance
#   class: evidence
#
# id: ucns_ptcna_receipt_rejects_tampering
#   given: any authority-bearing receipt field is changed
#   then: validation fails before downstream state construction
#   class: safety
#
# id: ucns_ptcna_candidate_transfers_no_status
#   given: a valid receipt is produced or consumed
#   then: candidate integration does not select geometry, prove usefulness, or establish privacy
#   class: doctrine
# === END CONTRACTS ===

"""Candidate-scoped UCNS producer for the requested PTCNA state.

Usage:
    python -m ucns.ptcna_state \
      --repository-root /path/to/exact/ucns-checkout \
      --producer-commit "$(git -C /path/to/exact/ucns-checkout rev-parse HEAD)" \
      --output /tmp/ucns-ptcna-state.json

The state is an actual dense initialization contract: ``157 x 7 x 7 x 53``
IEEE-754 binary64 positive-zero values in C order. The receipt hashes the exact
state bytes without materializing them in JSON. It is a candidate transport
surface, not a UCNS geometry selection or a usefulness claim.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from typing import Any, Mapping

from .edcm import (
    PUBLIC_GONOL_157,
    PUBLIC_GONOL_SHA256,
    PUBLIC_GONOL_SOURCE_COMMIT,
    PUBLIC_GONOL_SOURCE_PATH,
    PUBLIC_GONOL_SOURCE_REPOSITORY,
)


PTCNA_STATE_SCHEMA = "ucns.ptcna-candidate-state-receipt"
PTCNA_STATE_VERSION = "1.0.0"
PTCNA_CANDIDATE_ID = "ucns-ptcna-157x7x7x53-v1"
PTCNA_STATE_SHAPE = (157, 7, 7, 53)
PTCNA_AXIS_NAMES = (
    "public_gonol_position",
    "circle_phase",
    "seed_phase",
    "neural_node",
)
PTCNA_STATE_DTYPE = "<f8"
PTCNA_STATE_LAYOUT = "C"
PTCNA_STATE_INITIAL_VALUE = "+0.0"
PTCNA_STATE_ELEMENTS = 157 * 7 * 7 * 53
PTCNA_STATE_BYTES = PTCNA_STATE_ELEMENTS * 8
_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
_ZERO_CHUNK = b"\x00" * (1024 * 1024)


class PTCNAStateReceiptError(ValueError):
    """Raised when a candidate receipt or producer identity is invalid."""


def canonical_receipt_bytes(value: Mapping[str, Any]) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _zero_state_sha256() -> str:
    digest = sha256()
    remaining = PTCNA_STATE_BYTES
    while remaining:
        part = _ZERO_CHUNK[: min(remaining, len(_ZERO_CHUNK))]
        digest.update(part)
        remaining -= len(part)
    return digest.hexdigest()


def _module_sha256() -> str:
    return sha256(Path(__file__).read_bytes()).hexdigest()


def _payload(producer_commit: str) -> dict[str, Any]:
    if not _COMMIT_RE.fullmatch(producer_commit):
        raise PTCNAStateReceiptError("producer_commit must be an exact lowercase 40-hex Git commit")
    return {
        "schema": PTCNA_STATE_SCHEMA,
        "version": PTCNA_STATE_VERSION,
        "candidate": {
            "id": PTCNA_CANDIDATE_ID,
            "scope": "ptcna-initialization-only",
            "standing": "candidate",
            "selected": False,
        },
        "producer": {
            "repository": "The-Interdependency/ucns",
            "commit": producer_commit,
            "module": "ucns.ptcna_state",
            "module_sha256": _module_sha256(),
        },
        "state": {
            "shape": list(PTCNA_STATE_SHAPE),
            "axis_names": list(PTCNA_AXIS_NAMES),
            "elements": PTCNA_STATE_ELEMENTS,
            "bytes": PTCNA_STATE_BYTES,
            "dtype": PTCNA_STATE_DTYPE,
            "layout": PTCNA_STATE_LAYOUT,
            "initial_value": PTCNA_STATE_INITIAL_VALUE,
            "sha256": _zero_state_sha256(),
        },
        "provenance": {
            "public_gonol_tokens": len(PUBLIC_GONOL_157),
            "public_gonol_sha256": PUBLIC_GONOL_SHA256,
            "public_gonol_source_repository": PUBLIC_GONOL_SOURCE_REPOSITORY,
            "public_gonol_source_commit": PUBLIC_GONOL_SOURCE_COMMIT,
            "public_gonol_source_path": PUBLIC_GONOL_SOURCE_PATH,
            "seven_fold_axes": "declared PTCNA candidate composition counts; not UCNS geometry canon",
            "neural_nodes": 53,
        },
        "boundaries": {
            "geometry_selected": False,
            "proof_status_transfer": False,
            "usefulness_established": False,
            "production_privacy_established": False,
            "hmmm": [
                "continuous seven-fold geometry",
                "representative efficacy",
                "production privacy",
            ],
        },
    }


def build_ptcna_state_receipt(producer_commit: str) -> dict[str, Any]:
    """Build the canonical candidate receipt for one exact UCNS commit."""

    payload = _payload(producer_commit)
    return {**payload, "receipt_sha256": sha256(canonical_receipt_bytes(payload)).hexdigest()}


def validate_ptcna_state_receipt(receipt: Mapping[str, Any]) -> dict[str, Any]:
    """Validate all receipt fields against this exact producer implementation."""

    if not isinstance(receipt, Mapping):
        raise PTCNAStateReceiptError("receipt must be a mapping")
    commit = receipt.get("producer", {}).get("commit") if isinstance(receipt.get("producer"), Mapping) else None
    if not isinstance(commit, str):
        raise PTCNAStateReceiptError("receipt producer commit is missing")
    expected = build_ptcna_state_receipt(commit)
    if dict(receipt) != expected:
        raise PTCNAStateReceiptError("receipt identity or authority-bearing content mismatch")
    return expected


def write_ptcna_state_receipt(path: Path, producer_commit: str) -> dict[str, Any]:
    """Write canonical receipt bytes and return the validated receipt."""

    receipt = build_ptcna_state_receipt(producer_commit)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_bytes(canonical_receipt_bytes(receipt))
    temporary.replace(path)
    return receipt


def verify_checkout_commit(repository_root: Path, producer_commit: str) -> None:
    """Fail closed unless ``repository_root`` is exactly the declared checkout."""

    result = subprocess.run(
        ["git", "-C", str(repository_root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode or result.stderr or result.stdout.strip() != producer_commit:
        raise PTCNAStateReceiptError("checkout HEAD does not match producer_commit")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, required=True)
    parser.add_argument("--producer-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        verify_checkout_commit(args.repository_root, args.producer_commit)
        receipt = write_ptcna_state_receipt(args.output, args.producer_commit)
    except (OSError, subprocess.SubprocessError, PTCNAStateReceiptError) as exc:
        print(json.dumps({"status": "BLOCKED", "failure": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps({"status": "SURVIVED", "receipt_sha256": receipt["receipt_sha256"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "PTCNA_AXIS_NAMES",
    "PTCNA_CANDIDATE_ID",
    "PTCNA_STATE_BYTES",
    "PTCNA_STATE_DTYPE",
    "PTCNA_STATE_ELEMENTS",
    "PTCNA_STATE_LAYOUT",
    "PTCNA_STATE_SCHEMA",
    "PTCNA_STATE_SHAPE",
    "PTCNA_STATE_VERSION",
    "PTCNAStateReceiptError",
    "build_ptcna_state_receipt",
    "canonical_receipt_bytes",
    "validate_ptcna_state_receipt",
    "verify_checkout_commit",
    "write_ptcna_state_receipt",
]
