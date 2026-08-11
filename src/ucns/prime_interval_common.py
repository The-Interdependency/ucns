"""Shared constants and dependency boundaries for interval and link research."""
from __future__ import annotations

from fractions import Fraction

from .prime_smooth_ribbons import (
    CENTERLINE_SEPARATION_TARGET,
    RIBBON_SEPARATION_LOWER_BOUND,
)

SCHEMA_ID = "ucns.prime-interval-boundary-links"
SCHEMA_VERSION = "0.1.0"
SOURCE_NAME = "Möbius Strips and Quantum Geometry.txt"
SOURCE_SHA256 = "dc3a94ca5070ffff8f2a246f48db77192b08f521e721bc7c2a011aa05ddeb9a1"
SOURCE_LINES = (5, 6, 13, 14, 15, 16, 17)
INTERVAL_DPS = 70
INTERVAL_MAX_DEPTH = 40
INTERVAL_MAX_BOXES_PER_PAIR = 100_000
GENERIC_PROJECTION_DPS = 80
GENERIC_TRANSLATION_BOUND = Fraction(7, 5000)
GENERIC_ISOTOPY_CLEARANCE = (
    RIBBON_SEPARATION_LOWER_BOUND - 2 * GENERIC_TRANSLATION_BOUND
)
GENERIC_CENTER_X = Fraction(137, 10_000_000)
GENERIC_CENTER_Y = Fraction(-223, 10_000_000)


class IntervalBoundaryError(ValueError):
    """Raised when a certificate leaves its declared mathematical boundary."""


def fraction_text(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def require_mpmath():
    try:
        import mpmath as mp
    except ImportError as error:
        raise IntervalBoundaryError(
            "interval replay requires mpmath>=1.3,<2"
        ) from error
    return mp


def require_sympy():
    try:
        import sympy as sp
        from sympy.matrices.normalforms import smith_normal_form
        from sympy.polys.domains import ZZ
    except ImportError as error:
        raise IntervalBoundaryError(
            "integer normal forms require sympy>=1.12,<2"
        ) from error
    return sp, smith_normal_form, ZZ
