"""
UCNS — Unit Carrier Number System
Public root restarted from the sealed Chapter 1 subtractive foundations (2026-07-20).

This package implements the object model, radial map, directed branch law,
parallel valuation triad, Rectangular-Zero Lemma, and complete collapse rule
exactly as specified in the sealed foundations.

No prior Möbius-seam implementation is present or imported.
"""

from .core import (
    StructuralNull,
    N,
    Cell,
    Carrier,
    faithful_breadth,
    radius,
    support_weight,
    product_character,
    is_null,
    prune,
    pair,
    collapse,
    unit,
    from_payload,
)

__all__ = [
    "StructuralNull",
    "N",
    "Cell",
    "Carrier",
    "faithful_breadth",
    "radius",
    "support_weight",
    "product_character",
    "is_null",
    "prune",
    "pair",
    "collapse",
    "unit",
    "from_payload",
]

__version__ = "0.1.0-foundations"
