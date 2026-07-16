"""Lossless lifted text traversal over the canonical public gonol.

The implementation is promoted from the exact A0 source. Position zero is the
SPACE/ZERO Möbius seam and fixed origin. A repeated character advances by a
full 157-step revolution. Spaces are emitted seam events, never deletions.
"""

# === MODULE_BUILD ===
# id: ucns_public_gonol_lifted_path
#   module_name: public_gonol_lifted_path
#   module_kind: engine
#   summary: losslessly encodes and decodes text as the exact lifted traversal over the fixed-origin public gonol
#   owner: Erin Spencer
#   public_surface: encode_text_path, decode_text_path, vertex_of_char, char_of_vertex, is_seam_event, path_vertices, CarrierCharError, ARITY, ORIGIN
#   internal_surface: _ARRANGEMENT, _VERTEX_OF_CHAR
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: read
#   admin_only: false
#   tests: tests.test_public_gonol
#   rollout: default_enabled
#   rollback: remove exports after reverting consumers to the pinned a0-betatest source
#   requires: ucns_public_gonol, ucns_public_gonol_faces
#   since: 2026-07-16
#   unresolved: none
# === END MODULE_BUILD ===

from __future__ import annotations

from typing import Dict, List, Sequence

from .public_gonol import get_default
from .public_gonol_faces import ARITY, ORIGIN

_ARRANGEMENT = tuple(get_default())
_VERTEX_OF_CHAR = {ch: i for i, ch in enumerate(_ARRANGEMENT)}  # type: Dict[str, int]


class CarrierCharError(ValueError):
    """Raised when a character is not present on the 157-gonal carrier."""


def vertex_of_char(ch: str) -> int:
    """Return the carrier vertex for one character. SPACE maps to origin zero."""

    if not isinstance(ch, str) or len(ch) != 1:
        raise CarrierCharError("expected a single character, got {!r}".format(ch))
    vertex = _VERTEX_OF_CHAR.get(ch)
    if vertex is None:
        raise CarrierCharError("character {!r} is not on the 157-gonal carrier".format(ch))
    return vertex


def char_of_vertex(vertex: int) -> str:
    """Return the glyph at a carrier vertex."""

    return _ARRANGEMENT[int(vertex) % ARITY]


def is_seam_event(pos: int) -> bool:
    """True iff a lifted position sits over the fixed SPACE/ZERO seam."""

    return int(pos) % ARITY == ORIGIN


def encode_text_path(text: str) -> List[int]:
    """Lift text to an ordered, strictly increasing path on the universal cover."""

    path: List[int] = []
    prev_abs = ORIGIN
    for ch in text:
        target = vertex_of_char(ch)
        prev_vertex = prev_abs % ARITY
        delta = ((target - prev_vertex - 1) % ARITY) + 1
        prev_abs += delta
        path.append(prev_abs)
    return path


def decode_text_path(path: Sequence[int]) -> str:
    """Exact inverse of encode_text_path over the public carrier alphabet."""

    return "".join(char_of_vertex(pos) for pos in path)


def path_vertices(path: Sequence[int]) -> List[int]:
    """Return the local carrier vertices visited by a lifted path."""

    return [int(pos) % ARITY for pos in path]


__all__ = [
    "encode_text_path",
    "decode_text_path",
    "vertex_of_char",
    "char_of_vertex",
    "is_seam_event",
    "path_vertices",
    "CarrierCharError",
    "ARITY",
    "ORIGIN",
]
