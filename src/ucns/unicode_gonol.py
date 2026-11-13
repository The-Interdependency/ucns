# ratios: loc_comments=151:71 imports_exports=5:7 calls_definitions=58:19
# === MODULE_BUILD ===
# id: unicode_gonol_geometry
#   module_name: unicode_gonol
#   module_kind: geometry
#   summary: exact Unicode-scalar gonol bearings with exact UTF-8 anatomy and equal-radius scalar frames
#   owner: Erin Spencer
#   public_surface: UnicodeGlyphGonol, UnicodeScalarFrame, unicode_scalar_turn, unicode_glyph_gonol, build_unicode_scalar_frame
#   internal_surface: exact scalar/UTF-8 receipts
#   auth_boundary: Unicode scalar value and exact source sequence; no normalization
#   storage_boundary: immutable in-memory records
#   network_boundary: none
#   user_data_boundary: caller-supplied Unicode text remains in memory
#   admin_only: false
#   tests: tests/test_unicode_gonol.py
#   rollout: replaces Public-Gonol-157 admission and ordinal radius-halving as active text glyph geometry
#   rollback: explicit historical profiles remain replayable; do not reinterpret their receipts
#   requires: none
#   since: 2026-11-08
#   unresolved: exact affixiation transform and bearing of a completed construction at the next recursive scale
# === END MODULE_BUILD ===
# === CONTRACTS ===
# id: unicode_scalar_has_one_space_relative_bearing
#   given: one valid Unicode scalar
#   then: its exact turn is ((scalar-SPACE) mod 0x110000)/0x110000 with SPACE at turn zero
# id: unicode_scalar_and_utf8_views_are_both_retained
#   given: one valid Unicode scalar or exact scalar sequence
#   then: scalar identity/bearing and exact UTF-8 byte/bit anatomy are both recoverable without normalization
# id: unicode_scalar_frame_is_equal_radius
#   given: an exact nonempty scalar sequence and one positive exact frame radius
#   then: every scalar occurrence is placed at that same radius and its own scalar bearing
# id: unicode_scalar_sequence_is_not_normalized
#   given: canonically equivalent but byte-distinct Unicode sequences
#   then: their scalar sequences, UTF-8 bytes and receipts remain distinct
# id: unicode_scalar_frame_rejects_invalid_text
#   given: empty or non-string text, or a sequence containing a surrogate
#   then: construction refuses the input rather than emitting a Unicode scalar frame
# id: unicode_scalar_frame_rejects_inexact_radius
#   given: a radius that is not an exact integer or Fraction
#   then: construction refuses the radius rather than rounding it
# id: unicode_scalar_frame_preserves_unresolved_bearing
#   given: a primitive Unicode frame is serialized
#   then: its record declares no normalization and preserves next-scale bearing as hmmm
# === END CONTRACTS ===
"""Exact Unicode scalar geometry with UTF-8 anatomy.

This is the active primitive text-glyph geometry.

One Unicode scalar is one glyph gonol. Its scalar value determines one exact
bearing from SPACE. The exact UTF-8 bytes and bits are retained as a second,
internal representation of that same scalar; they do not replace scalar
identity.

No Unicode normalization is performed. Precomposed and decomposed sequences
remain distinct constructions.

The 157-position Public Gonol remains a separate preserved carrier/function
surface. It is not the admission gate or angular registry for arbitrary Unicode
text.

Higher recursive scales preserve closed interiors and begin from equal-radius
siblings. The exact affixiation transform, and the bearing assigned to a
completed word when it participates in a sentence, remain unresolved here
rather than being filled with ordinal radius-halving or a hash.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from hashlib import sha256
import json

UNICODE_SCALAR_MODULUS = 0x110000
SPACE_SCALAR = 0x20
SCHEMA = "ucns.unicode-gonol.v1"
VERSION = "1"


def _digest(value: object) -> str:
    return sha256(json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")).hexdigest()


def _scalar(character: str) -> int:
    if not isinstance(character, str) or len(character) != 1:
        raise TypeError("glyph must be exactly one Unicode scalar")
    value = ord(character)
    if 0xD800 <= value <= 0xDFFF:
        raise ValueError("surrogate code points are not Unicode scalars")
    return value


def unicode_scalar_turn(character: str) -> Fraction:
    """Exact SPACE-relative turn for one Unicode scalar.

    The full scalar numeric range is the stable modulus. Assignment status is
    deliberately irrelevant, so future Unicode versions cannot move existing
    bearings. Surrogate values are holes, not compressed-away positions.
    """
    value = _scalar(character)
    return Fraction((value - SPACE_SCALAR) % UNICODE_SCALAR_MODULUS,
                    UNICODE_SCALAR_MODULUS)


@dataclass(frozen=True, slots=True)
class UnicodeGlyphGonol:
    """One Unicode scalar with exact scalar and UTF-8 views."""

    character: str
    scalar: int = field(init=False)
    turn: Fraction = field(init=False)
    utf8: bytes = field(init=False, repr=False)
    receipt: str = field(init=False)

    def __post_init__(self) -> None:
        value = _scalar(self.character)
        encoded = self.character.encode("utf-8", errors="strict")
        turn = unicode_scalar_turn(self.character)
        object.__setattr__(self, "scalar", value)
        object.__setattr__(self, "turn", turn)
        object.__setattr__(self, "utf8", encoded)
        object.__setattr__(self, "receipt", _digest(self.record(include_receipt=False)))

    @property
    def codepoint(self) -> str:
        return f"U+{self.scalar:04X}"

    @property
    def utf8_bits(self) -> tuple[str, ...]:
        return tuple(f"{byte:08b}" for byte in self.utf8)

    def record(self, *, include_receipt: bool = True) -> dict:
        record = {
            "schema": SCHEMA,
            "version": VERSION,
            "character": self.character,
            "scalar": self.scalar,
            "codepoint": self.codepoint,
            "space_scalar": SPACE_SCALAR,
            "scalar_modulus": UNICODE_SCALAR_MODULUS,
            "turn": [self.turn.numerator, self.turn.denominator],
            "utf8_bytes": list(self.utf8),
            "utf8_hex": self.utf8.hex().upper(),
            "utf8_bits": list(self.utf8_bits),
        }
        if include_receipt and hasattr(self, "receipt"):
            record["receipt"] = self.receipt
        return record


@dataclass(frozen=True, slots=True)
class UnicodeScalarPlacement:
    """One occurrence in an equal-radius scalar frame."""

    ordinal: int
    glyph: UnicodeGlyphGonol
    radius: Fraction

    def __post_init__(self) -> None:
        if isinstance(self.ordinal, bool) or not isinstance(self.ordinal, int) or self.ordinal < 0:
            raise ValueError("ordinal must be a nonnegative integer")
        if not isinstance(self.glyph, UnicodeGlyphGonol):
            raise TypeError("placement requires a UnicodeGlyphGonol")
        if not isinstance(self.radius, Fraction) or self.radius <= 0:
            raise ValueError("radius must be a positive exact Fraction")

    @property
    def turn(self) -> Fraction:
        return self.glyph.turn

    def record(self) -> dict:
        return {
            "ordinal": self.ordinal,
            "glyph_receipt": self.glyph.receipt,
            "radius": [self.radius.numerator, self.radius.denominator],
            "turn": [self.turn.numerator, self.turn.denominator],
        }


@dataclass(frozen=True, slots=True)
class UnicodeScalarFrame:
    """Exact non-normalizing Unicode sequence at one equal radius.

    This frame supplies the primitive glyph placements used before/through
    glyph-level affixiation. It does not invent the next-scale bearing of the
    completed construction.
    """

    text: str
    radius: Fraction = Fraction(1)
    glyphs: tuple[UnicodeGlyphGonol, ...] = field(init=False)
    placements: tuple[UnicodeScalarPlacement, ...] = field(init=False)
    utf8: bytes = field(init=False, repr=False)
    receipt: str = field(init=False)

    def __post_init__(self) -> None:
        if not isinstance(self.text, str) or not self.text:
            raise ValueError("text must be nonempty Unicode text")
        if not isinstance(self.radius, Fraction) or self.radius <= 0:
            raise ValueError("radius must be a positive exact Fraction")
        glyphs = tuple(UnicodeGlyphGonol(ch) for ch in self.text)
        placements = tuple(
            UnicodeScalarPlacement(i, glyph, self.radius)
            for i, glyph in enumerate(glyphs)
        )
        encoded = self.text.encode("utf-8", errors="strict")
        object.__setattr__(self, "glyphs", glyphs)
        object.__setattr__(self, "placements", placements)
        object.__setattr__(self, "utf8", encoded)
        object.__setattr__(self, "receipt", _digest(self.record(include_receipt=False)))

    def recover(self) -> str:
        return "".join(glyph.character for glyph in self.glyphs)

    @property
    def scalar_sequence(self) -> tuple[int, ...]:
        return tuple(glyph.scalar for glyph in self.glyphs)

    def record(self, *, include_receipt: bool = True) -> dict:
        record = {
            "schema": "ucns.unicode-scalar-frame.v1",
            "text": self.text,
            "scalar_sequence": list(self.scalar_sequence),
            "utf8_bytes": list(self.utf8),
            "utf8_hex": self.utf8.hex().upper(),
            "radius": [self.radius.numerator, self.radius.denominator],
            "glyphs": [glyph.record() for glyph in self.glyphs],
            "placements": [placement.record() for placement in self.placements],
            "normalization": "none",
            "next_scale_bearing": "hmmm",
        }
        if include_receipt and hasattr(self, "receipt"):
            record["receipt"] = self.receipt
        return record


def unicode_glyph_gonol(character: str) -> UnicodeGlyphGonol:
    return UnicodeGlyphGonol(character)


def build_unicode_scalar_frame(
    text: str, *, radius: Fraction = Fraction(1)
) -> UnicodeScalarFrame:
    if isinstance(radius, int) and not isinstance(radius, bool):
        radius = Fraction(radius)
    if not isinstance(radius, Fraction):
        raise ValueError("radius must be an exact integer or Fraction")
    return UnicodeScalarFrame(text, radius)


__all__ = [
    "SCHEMA",
    "VERSION",
    "UNICODE_SCALAR_MODULUS",
    "SPACE_SCALAR",
    "UnicodeGlyphGonol",
    "UnicodeScalarPlacement",
    "UnicodeScalarFrame",
    "unicode_scalar_turn",
    "unicode_glyph_gonol",
    "build_unicode_scalar_frame",
]
# ratios: loc_comments=151:71 imports_exports=5:7 calls_definitions=58:19
