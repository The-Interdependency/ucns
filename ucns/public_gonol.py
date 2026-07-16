"""Canonical public 157-gonal carrier for UCNS.

This module promotes the public gonol from
``The-Interdependency/a0-betatest@7af8debf6ef3905f01baff02b43d8c3bee16ccbc``
into the UCNS public package without changing its arrangement law.

Position zero is the canonical SPACE/ZERO Möbius twist point, seam, and origin.
It is not an arbitrary first anchor and is never moved by private transforms.
No continuous-angle interpretation is introduced by this module.
"""

# === MODULE_BUILD ===
# id: ucns_public_gonol
#   module_name: public_gonol
#   module_kind: engine
#   summary: owns the exact public 157-gonal arrangement and fixed SPACE/ZERO twist origin promoted from a0-betatest
#   owner: Erin Spencer
#   public_surface: GonalSpec, build_gonal, validate_gonal, print_gonal, EXAMPLE_157, PUBLIC_GONOL_157, make_example_157, get_default, public_gonol_sha256, PUBLIC_GONOL_SHA256
#   internal_surface: UPPERCASE, LOWERCASE, DIGITS_ODD, DIGITS_EVEN, PAIRED_OPEN, PAIRED_CLOSE, UNPAIRED_ASCII, UNPAIRED_OPS, UNPAIRED_ALL
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_public_gonol
#   rollout: default_enabled
#   rollback: remove public exports after downstream consumers return to the pinned a0-betatest source
#   requires: none
#   since: 2026-07-16
#   unresolved: hmmm — no continuous-angle projection is ratified by this promotion
# === END MODULE_BUILD ===

from __future__ import annotations

import hashlib
import string
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

PUBLIC_GONOL_SOURCE_REPOSITORY = "The-Interdependency/a0-betatest"
PUBLIC_GONOL_SOURCE_COMMIT = "7af8debf6ef3905f01baff02b43d8c3bee16ccbc"
PUBLIC_GONOL_SOURCE_PATH = "backend/interdependent_lib/gonal/gonal.py"
PUBLIC_GONOL_SHA256 = "20d6ed51fdff5505ed9696c38d6dcc82f982eba166d9b712bee68c4521b751ac"

UPPERCASE = list(string.ascii_uppercase)
LOWERCASE = list(string.ascii_lowercase)
DIGITS_ODD = ["1", "3", "5", "7", "9"]
DIGITS_EVEN = ["2", "4", "6", "8", "0"]
DIGITS_ALL = DIGITS_ODD + DIGITS_EVEN

PAIRED_OPEN = ["(", "[", "{", "<", "‘", "“", "«"]
PAIRED_CLOSE = [")", "]", "}", ">", "’", "”", "»"]

UNPAIRED_ASCII = [
    chr(i)
    for i in range(33, 127)
    if chr(i)
    not in (
        set(UPPERCASE)
        | set(LOWERCASE)
        | set(string.digits)
        | set(PAIRED_OPEN)
        | set(PAIRED_CLOSE)
        | {" "}
    )
]

UNPAIRED_OPS = [
    "…", "—", "–", "·", "°", "±", "×", "÷", "√",
    "∂", "∫", "∑", "∏", "∇", "∞", "≈", "≠", "≤", "≥",
    "→", "←", "↑", "↓", "↔", "⊕", "⊗", "⊙", "⊘",
    "∈", "∉", "⊂", "⊃", "⊆", "⊇", "∩", "∪",
    "∧", "∨", "¬", "∀", "∃", "⊢", "⊨", "∴", "∵", "≡",
    "ψ", "φ", "ω", "α", "β", "γ", "δ", "λ", "π", "σ", "τ", "θ",
    "∅", "ℕ", "ℤ", "ℚ", "ℝ", "ℂ", "ℵ",
]

UNPAIRED_ALL = UNPAIRED_ASCII + UNPAIRED_OPS


@dataclass
class GonalSpec:
    n: int = 157
    no_adjacent: List[str] = field(default_factory=lambda: ["letter", "digit"])
    letter_sides: str = "opposite"
    digit_alternation: bool = True
    paired_alignment: str = "opposite"
    horizontal_symmetry: str = "forbidden"
    origin: str = " "
    extra_unpaired: List[str] = field(default_factory=list)
    seed: Optional[int] = None


def _validate_spec(spec: GonalSpec) -> None:
    if not isinstance(spec.n, int) or isinstance(spec.n, bool) or spec.n < 1:
        raise ValueError("gonal arity must be a positive integer")
    if not isinstance(spec.origin, str) or len(spec.origin) != 1:
        raise ValueError("gonal origin must be exactly one character")


def build_gonal(spec: GonalSpec) -> List[str]:
    """Build an arrangement by the exact A0 declarative placement law."""

    _validate_spec(spec)
    n = spec.n
    slot: List[str] = [""] * n
    slot[0] = spec.origin

    upper_arc = list(range(1, (n // 2) + 1))
    lower_arc = list(range((n // 2) + 1, n))

    if spec.letter_sides == "opposite":
        upper_l = list(range(1, upper_arc[-1], 3))[:26]
        lower_l = list(range(lower_arc[1], lower_arc[-1], 3))[:26]
        if len(upper_l) < len(UPPERCASE) or len(lower_l) < len(LOWERCASE):
            raise ValueError("gonal arity is too small for opposite-side letter placement")
        for i, ch in enumerate(UPPERCASE):
            slot[upper_l[i]] = ch
        for i, ch in enumerate(LOWERCASE):
            slot[lower_l[i]] = ch
    elif spec.letter_sides == "same":
        all_letters: List[Optional[str]] = [None] * 52
        all_letters[::2] = UPPERCASE
        all_letters[1::2] = LOWERCASE
        upper_l = list(range(1, upper_arc[-1], 2))[:52]
        if len(upper_l) < len(all_letters):
            raise ValueError("gonal arity is too small for same-side letter placement")
        for i, ch in enumerate(all_letters):
            if ch is not None:
                slot[upper_l[i]] = ch
    else:
        raise ValueError("unsupported letter_sides {!r}".format(spec.letter_sides))

    if spec.digit_alternation:
        upper_gaps = [p for p in upper_arc if slot[p] == ""]
        step = max(1, len(upper_gaps) // (len(DIGITS_ODD) + 1))
        for i, ch in enumerate(DIGITS_ODD):
            idx = step * (i + 1)
            if idx < len(upper_gaps):
                slot[upper_gaps[idx]] = ch

        lower_gaps = [p for p in lower_arc if slot[p] == ""]
        step_l = max(1, len(lower_gaps) // (len(DIGITS_EVEN) + 1))
        for i, ch in enumerate(DIGITS_EVEN):
            idx = step_l * (i + 1)
            if idx < len(lower_gaps):
                slot[lower_gaps[idx]] = ch
    else:
        all_gaps = [p for p in range(1, n) if slot[p] == ""]
        step = max(1, len(all_gaps) // (len(DIGITS_ALL) + 1))
        for i, ch in enumerate(DIGITS_ALL):
            idx = step * (i + 1)
            if idx < len(all_gaps):
                slot[all_gaps[idx]] = ch

    if spec.paired_alignment == "opposite":
        upper_rem = [p for p in upper_arc if slot[p] == ""]
        lower_rem = [p for p in lower_arc if slot[p] == ""]
        step_o = max(1, len(upper_rem) // (len(PAIRED_OPEN) + 1))
        step_c = max(1, len(lower_rem) // (len(PAIRED_CLOSE) + 1))
        for i, ch in enumerate(PAIRED_OPEN):
            idx = step_o * (i + 1)
            if idx < len(upper_rem):
                slot[upper_rem[idx]] = ch
        for i, ch in enumerate(PAIRED_CLOSE):
            idx = step_c * (i + 1)
            if idx < len(lower_rem):
                slot[lower_rem[idx]] = ch
    elif spec.paired_alignment == "interleaved":
        all_rem = [p for p in range(1, n) if slot[p] == ""]
        step_p = max(1, len(all_rem) // (len(PAIRED_OPEN) + 1))
        for i, (op, cl) in enumerate(zip(PAIRED_OPEN, PAIRED_CLOSE)):
            idx = step_p * (i + 1)
            if idx < len(all_rem):
                pos = all_rem[idx]
                slot[pos] = op
                nxt = (pos + 1) % n
                if slot[nxt] == "":
                    slot[nxt] = cl
    else:
        raise ValueError("unsupported paired_alignment {!r}".format(spec.paired_alignment))

    unpaired = UNPAIRED_ALL + spec.extra_unpaired
    fill_positions = [p for p in range(n) if slot[p] == ""]
    for i, pos in enumerate(fill_positions):
        if i < len(unpaired):
            slot[pos] = unpaired[i]
        else:
            slot[pos] = "\x00{}".format(i)

    return slot


def validate_gonal(slot: List[str], spec: GonalSpec) -> Dict[str, object]:
    """Validate structure, fixed origin, uniqueness, adjacency, and overflow."""

    violations: List[str] = []
    warnings: List[str] = []

    try:
        _validate_spec(spec)
    except ValueError as exc:
        violations.append(str(exc))

    n = len(slot)
    if n != spec.n:
        violations.append("arity mismatch: expected {}, got {}".format(spec.n, n))
    if n == 0:
        violations.append("carrier must be nonempty")

    malformed = [
        index
        for index, glyph in enumerate(slot)
        if not isinstance(glyph, str) or not glyph
    ]
    if malformed:
        violations.append("non-string or empty glyph positions: {}".format(malformed))

    if n > 0 and slot[0] != spec.origin:
        violations.append(
            "fixed origin mismatch at position 0: expected {!r}, got {!r}".format(
                spec.origin, slot[0]
            )
        )

    origin_positions = [index for index, glyph in enumerate(slot) if glyph == spec.origin]
    if origin_positions != [0]:
        violations.append(
            "origin must occur exactly once at position 0; got {}".format(origin_positions)
        )

    duplicates = sorted(
        glyph
        for glyph in set(slot)
        if slot.count(glyph) > 1
    )
    if duplicates:
        violations.append("duplicate glyphs are not allowed: {!r}".format(duplicates))

    def char_type(ch: str) -> str:
        if ch in UPPERCASE:
            return "uppercase"
        if ch in LOWERCASE:
            return "lowercase"
        if ch in string.digits:
            return "digit"
        if ch in PAIRED_OPEN:
            return "paired_open"
        if ch in PAIRED_CLOSE:
            return "paired_close"
        if ch == spec.origin:
            return "origin"
        return "unpaired"

    def is_letter(ch: str) -> bool:
        return ch in string.ascii_letters

    def is_digit(ch: str) -> bool:
        return ch in string.digits

    if n > 0 and not malformed:
        for k in range(n):
            curr = slot[k]
            nxt = slot[(k + 1) % n]
            for constraint in spec.no_adjacent:
                if constraint == "letter" and is_letter(curr) and is_letter(nxt):
                    violations.append(
                        "letter-letter at pos {}-{}: {!r}-{!r}".format(
                            k, (k + 1) % n, curr, nxt
                        )
                    )
                elif constraint == "digit" and is_digit(curr) and is_digit(nxt):
                    violations.append(
                        "digit-digit at pos {}-{}: {!r}-{!r}".format(
                            k, (k + 1) % n, curr, nxt
                        )
                    )
                elif constraint == "uppercase" and curr in UPPERCASE and nxt in UPPERCASE:
                    violations.append(
                        "upper-upper at pos {}-{}: {!r}-{!r}".format(
                            k, (k + 1) % n, curr, nxt
                        )
                    )
                elif constraint == "lowercase" and curr in LOWERCASE and nxt in LOWERCASE:
                    violations.append(
                        "lower-lower at pos {}-{}: {!r}-{!r}".format(
                            k, (k + 1) % n, curr, nxt
                        )
                    )

    overflow = [
        k for k, glyph in enumerate(slot)
        if isinstance(glyph, str) and glyph.startswith("\x00")
    ]
    if overflow:
        violations.append("overflow positions (ran out of unpaired chars): {}".format(overflow))

    count_names = [
        "uppercase",
        "lowercase",
        "digit",
        "paired_open",
        "paired_close",
        "unpaired",
        "origin",
    ]
    counts = {
        name: sum(
            1
            for glyph in slot
            if isinstance(glyph, str) and glyph and char_type(glyph) == name
        )
        for name in count_names
    }
    return {
        "valid": len(violations) == 0,
        "violations": violations,
        "warnings": warnings,
        "counts": counts,
        "n": n,
    }


def print_gonal(slot: List[str], width: int = 10) -> None:
    """Print the arrangement with position zero explicitly identified as origin."""

    n = len(slot)
    print("\n{}-GONAL ARRANGEMENT".format(n))
    if n:
        print("  pos   0: {!r}  ORIGIN".format(slot[0]))
    for i in range(0, n, width):
        end = min(i + width, n)
        row = "  ".join("{:3}:{!r}".format(j, slot[j]) for j in range(i, end))
        print("  {}".format(row))


def make_example_157() -> List[str]:
    """Build the canonical public 157-gonal arrangement."""

    spec = GonalSpec(
        n=157,
        no_adjacent=["letter", "digit"],
        letter_sides="opposite",
        digit_alternation=True,
        paired_alignment="opposite",
        horizontal_symmetry="forbidden",
        origin=" ",
    )
    arrangement = build_gonal(spec)
    report = validate_gonal(arrangement, spec)
    if not report["valid"]:
        raise RuntimeError("public gonol construction invalid: {!r}".format(report["violations"]))
    return arrangement


def public_gonol_sha256(glyphs: Tuple[str, ...]) -> str:
    """Hash the exact one-glyph-per-line representation used by the source pin."""

    return hashlib.sha256(("\n".join(glyphs) + "\n").encode("utf-8")).hexdigest()


EXAMPLE_157 = make_example_157()
PUBLIC_GONOL_157 = tuple(EXAMPLE_157)
if public_gonol_sha256(PUBLIC_GONOL_157) != PUBLIC_GONOL_SHA256:
    raise RuntimeError("public gonol source drift")


def get_default() -> List[str]:
    """Return a caller-owned copy of the canonical public arrangement."""

    return list(PUBLIC_GONOL_157)


__all__ = [
    "PUBLIC_GONOL_SOURCE_REPOSITORY",
    "PUBLIC_GONOL_SOURCE_COMMIT",
    "PUBLIC_GONOL_SOURCE_PATH",
    "PUBLIC_GONOL_SHA256",
    "GonalSpec",
    "build_gonal",
    "validate_gonal",
    "print_gonal",
    "EXAMPLE_157",
    "PUBLIC_GONOL_157",
    "make_example_157",
    "get_default",
    "public_gonol_sha256",
    "UPPERCASE",
    "LOWERCASE",
    "DIGITS_ODD",
    "DIGITS_EVEN",
    "PAIRED_OPEN",
    "PAIRED_CLOSE",
    "UNPAIRED_ALL",
]
