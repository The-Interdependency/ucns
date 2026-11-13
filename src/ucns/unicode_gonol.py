# === MODULE_BUILD ===
# id: unicode_gonol_geometry
#   module_name: unicode_gonol
#   module_kind: geometry
#   summary: exact Unicode-scalar gonols with 16-bit radius, 32-bit big-endian diameter, retained UTF-8 anatomy and equal placement radius
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
# id: unicode_gonol_fixed_bit_radius
#   given: any valid Unicode scalar including ASCII and supplementary-plane scalars
#   then: bit radius is 16 and diameter is 32 bits stored as exactly four big-endian bytes without a byte-order marker; ASCII has three leading zero bytes
# id: unicode_gonol_big_endian_round_trip
#   given: an exact four-byte big-endian scalar representation
#   then: recover the same scalar or reject invalid width and nonscalar values without truncation or normalization
# id: unicode_bit_radius_is_independent_of_placement
#   given: a scalar frame with any admissible geometric placement radius
#   then: every glyph keeps 16-bit radius and its complete 32-bit representation while the frame preserves every occurrence
# === END CONTRACTS ===
"""Exact Unicode scalar geometry with UTF-8 anatomy.

This is the active primitive text-glyph geometry.

One Unicode scalar is one glyph gonol. Its scalar value determines one exact
bearing from SPACE. The exact UTF-8 bytes and bits are retained as a second,
internal representation of that same scalar; they do not replace scalar
identity.

UCHC's bit radius ("b rad") is fixed at 16; the bit diameter is 32. Each
scalar occupies four big-endian bytes (UTF-32BE, without a BOM). ASCII therefore
has three leading zero bytes. These are encoding widths, independent of the
geometric placement ``radius``. A text frame retains one complete diameter per
scalar; the width is never a limit on the frame's text length.

Usage: ``unicode_glyph_gonol("A").utf32_be == bytes.fromhex("00 00 00 41")``.
``UnicodeGlyphGonol.from_utf32_be`` validates and recovers one diameter.
Version 2 receipts include the width and byte-order contract; version 1 receipts
remain bound to their historical producer and are not reinterpreted.

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
GONOL_BIT_RADIUS = 16
GONOL_BIT_DIAMETER = 2 * GONOL_BIT_RADIUS
SCHEMA = "ucns.unicode-gonol.v2"
VERSION = "2"


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
    """One scalar with a 16-bit radius and exact UTF-32BE/UTF-8 views."""

    character: str
    scalar: int = field(init=False)
    turn: Fraction = field(init=False)
    utf8: bytes = field(init=False, repr=False)
    utf32_be: bytes = field(init=False, repr=False)
    receipt: str = field(init=False)

    def __post_init__(self) -> None:
        value = _scalar(self.character)
        encoded = self.character.encode("utf-8", errors="strict")
        turn = unicode_scalar_turn(self.character)
        object.__setattr__(self, "scalar", value)
        object.__setattr__(self, "turn", turn)
        object.__setattr__(self, "utf8", encoded)
        object.__setattr__(self, "utf32_be", value.to_bytes(GONOL_BIT_DIAMETER // 8, "big"))
        object.__setattr__(self, "receipt", _digest(self.record(include_receipt=False)))

    @classmethod
    def from_utf32_be(cls, data: bytes) -> UnicodeGlyphGonol:
        """Recover exactly one four-byte diameter; refuse padding/truncation."""
        if not isinstance(data, bytes):
            raise TypeError("gonol diameter must be immutable bytes")
        if len(data) != GONOL_BIT_DIAMETER // 8:
            raise ValueError("gonol diameter must contain exactly four bytes")
        return cls(data.decode("utf-32-be", errors="strict"))

    @property
    def bit_radius(self) -> int:
        return GONOL_BIT_RADIUS

    @property
    def bit_diameter(self) -> int:
        return GONOL_BIT_DIAMETER

    @property
    def diameter_bits(self) -> str:
        return "".join(f"{byte:08b}" for byte in self.utf32_be)

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
            "bit_radius": self.bit_radius,
            "bit_diameter": self.bit_diameter,
            "diameter_encoding": "UTF-32BE",
            "utf32_be_bytes": list(self.utf32_be),
            "utf32_be_hex": self.utf32_be.hex().upper(),
            "diameter_bits": self.diameter_bits,
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

    @property
    def utf32_be(self) -> bytes:
        """Ordered full diameters; four bytes per scalar, with no stream BOM."""
        return b"".join(glyph.utf32_be for glyph in self.glyphs)

    def record(self, *, include_receipt: bool = True) -> dict:
        record = {
            "schema": "ucns.unicode-scalar-frame.v2",
            "text": self.text,
            "scalar_sequence": list(self.scalar_sequence),
            "utf8_bytes": list(self.utf8),
            "utf8_hex": self.utf8.hex().upper(),
            "glyph_bit_radius": GONOL_BIT_RADIUS,
            "glyph_bit_diameter": GONOL_BIT_DIAMETER,
            "diameter_encoding": "UTF-32BE",
            "utf32_be_hex": self.utf32_be.hex().upper(),
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
    "GONOL_BIT_RADIUS",
    "GONOL_BIT_DIAMETER",
    "UnicodeGlyphGonol",
    "UnicodeScalarPlacement",
    "UnicodeScalarFrame",
    "unicode_scalar_turn",
    "unicode_glyph_gonol",
    "build_unicode_scalar_frame",
]
