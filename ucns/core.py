"""
UCNS core — sealed Chapter 1 foundations made executable.

Implements:
  1.1  Radial map and unique Structural Null
  1.2  Directed branch law (twofold cover)
  1.3  Separation of zeros
  1.4  Parallel valuation triad (W, M, B) + no-go
  1.5  Rectangular-Zero Lemma
  1.6  Carrier pairing vs typed dispatch (dispatch is stub)
  1.7  Memory as geometry (receipts contribute breadth)
  1.8  Complete collapse rule
  1.9  Implementation boundary (evaluators still formal)

No additive faithful real breadth is admitted (no-go proposition).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Optional, Sequence, Tuple, Union
import math


# ---------------------------------------------------------------------------
# 1.1 / 1.3  Structural Null and separation of zeros
# ---------------------------------------------------------------------------

class StructuralNull:
    """
    The unique complete object containing no distinction.
    Symbol: N
    Satisfies B(N) = 0, a(N) = 0, W(N) = 0, M(N) = 0.
    Not algebraic zero, not neutral product character, not an absent cell.
    """
    _instance: Optional["StructuralNull"] = None

    def __new__(cls) -> "StructuralNull":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "N"

    def __bool__(self) -> bool:
        return False

    def __eq__(self, other: object) -> bool:
        return isinstance(other, StructuralNull)

    def __hash__(self) -> int:
        return hash("UCNS_StructuralNull")


N = StructuralNull()


def is_null(obj: Any) -> bool:
    return obj is N or isinstance(obj, StructuralNull)


# ---------------------------------------------------------------------------
# Cell and support
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class Cell:
    """
    A potential carrier cell.
    Support weight μ(c) ≥ 0.
    μ(c) = 0 exactly when the cell is completely absent.
    Algebraic zero payload does not force μ = 0.
    """
    coordinate: Any = None
    payload: Any = None
    type: Any = None
    shape: Any = None
    state: Any = None
    provenance: Any = None
    relation: Any = None
    # explicit support weight; default positive if any distinction present
    mu: float = 1.0

    def has_distinction(self) -> bool:
        return any(
            x is not None
            for x in (
                self.coordinate,
                self.payload,
                self.type,
                self.shape,
                self.state,
                self.provenance,
                self.relation,
            )
        )

    def support(self) -> float:
        # Chapter 1.4 / 1.5: the zero-test of μ determines whether a cell exists.
        # Positive μ means the cell is present and contributes that weight to W,
        # independent of whether payload/coordinate/etc. are populated.
        # Algebraic zero in the payload does not force μ = 0.
        return max(0.0, float(self.mu))


# ---------------------------------------------------------------------------
# Carrier object
# ---------------------------------------------------------------------------

@dataclass
class Carrier:
    """
    A UCNS carrier object (non-null).
    Possesses three independent valuations W, M, B above null.
    Radius is derived solely from faithful breadth B.
    """
    cells: Tuple[Cell, ...] = field(default_factory=tuple)
    # residual product-character grade (default 1.0) for future typed work
    m_contrib: float = 1.0
    # retained causal receipts (ordinary structure)
    receipts: Tuple[Any, ...] = field(default_factory=tuple)
    # recursive payloads, metadata, etc.
    extra: dict = field(default_factory=dict)

    def __post_init__(self) -> None:
        # freeze cells
        object.__setattr__(self, "cells", tuple(self.cells))
        object.__setattr__(self, "receipts", tuple(self.receipts))

    # ----- valuations -----

    def W(self) -> float:
        """Aggregate structural support."""
        return sum(c.support() for c in self.cells)

    def M(self) -> float:
        """
        Product character — derived combinatorial invariant.
        Multiplicative under pairing.
        Neutral value is 1 (any collection of unit-support cells); unique zero is Structural Null.

        Primary factor is the product of the cell supports µ(c).
        This is independent of the sum W, so different partitions of the same
        total support yield different M (separation witness).
        An optional residual m_contrib (default 1) remains for future typed grading.
        Receipts contribute a multiplicative factor.
        """
        if self.W() <= 0.0 and not self.receipts and not self.extra:
            return 0.0
        # product of cell supports (primary combinatorial character)
        prod = 1.0
        for c in self.cells:
            s = c.support()
            if s > 0.0:
                prod *= s
        # residual explicit grade (default 1.0) + receipt distinction
        base = max(0.0, float(self.m_contrib)) * prod
        r = 1.0 + 0.1 * len(self.receipts)
        return base * r

    def B(self) -> float:
        """
        Faithful breadth — complete surviving distinction.
        Null-faithful: B = 0 iff the object is Structural Null.
        No additive or multiplicative law is imposed.
        """
        if self.W() <= 0.0 and not self.receipts and not self.extra:
            return 0.0
        # provisional concrete evaluator: log-support + receipt distinction + extra
        w = self.W()
        b = math.log1p(w) if w > 0 else 0.0
        b += 0.5 * len(self.receipts)
        b += 0.25 * len(self.extra)
        # typed distinction from cells that retain structure
        for c in self.cells:
            if c.has_distinction():
                b += 0.1
        return max(0.0, b)

    def a(self) -> float:
        """Carrier radius a = 1 - exp(-B)."""
        return 1.0 - math.exp(-self.B())

    def is_null(self) -> bool:
        return self.B() <= 0.0


# ---------------------------------------------------------------------------
# Public valuation functions (work on Carrier or N)
# ---------------------------------------------------------------------------

def faithful_breadth(obj: Union[Carrier, StructuralNull]) -> float:
    if is_null(obj):
        return 0.0
    return obj.B()  # type: ignore


def radius(obj: Union[Carrier, StructuralNull]) -> float:
    if is_null(obj):
        return 0.0
    return obj.a()  # type: ignore


def support_weight(obj: Union[Carrier, StructuralNull]) -> float:
    if is_null(obj):
        return 0.0
    return obj.W()  # type: ignore


def product_character(obj: Union[Carrier, StructuralNull]) -> float:
    if is_null(obj):
        return 0.0
    return obj.M()  # type: ignore


# ---------------------------------------------------------------------------
# 1.5 Rectangular-Zero Lemma
# ---------------------------------------------------------------------------

def prune(obj: Union[Carrier, StructuralNull]) -> Union[Carrier, StructuralNull]:
    """
    Remove cells with μ = 0.
    Preserves relative order and relations of surviving cells.
    Commutes with pairing (Rectangular-Zero Lemma).
    """
    if is_null(obj):
        return N
    assert isinstance(obj, Carrier)
    kept = tuple(c for c in obj.cells if c.support() > 0.0)
    if not kept and not obj.receipts and not obj.extra:
        return N
    return Carrier(
        cells=kept,
        m_contrib=obj.m_contrib,
        receipts=obj.receipts,
        extra=dict(obj.extra),
    )


def pair(
    A: Union[Carrier, StructuralNull],
    C: Union[Carrier, StructuralNull],
) -> Union[Carrier, StructuralNull]:
    """
    Carrier product A ⊠ C — complete Cartesian cross-pairing of supported cells.
    Defining axiom: μ(c_i ⊠ d_j) = μ(c_i) * μ(d_j)
    Structural Null is absorbing.
    Rectangular-Zero: prune(A ⊠ C) = prune(A) ⊠ prune(C)
    """
    if is_null(A) or is_null(C):
        return N
    assert isinstance(A, Carrier) and isinstance(C, Carrier)

    # paired cells
    paired_cells: list[Cell] = []
    for c in A.cells:
        for d in C.cells:
            mu = c.support() * d.support()
            if mu > 0.0:
                paired_cells.append(
                    Cell(
                        coordinate=(c.coordinate, d.coordinate),
                        payload=(c.payload, d.payload),
                        type=(c.type, d.type),
                        shape=(c.shape, d.shape),
                        state=(c.state, d.state),
                        provenance=(c.provenance, d.provenance),
                        relation=(c.relation, d.relation),
                        mu=mu,
                    )
                )

    # product character multiplies
    m = A.m_contrib * C.m_contrib

    # receipts are concatenated (ordinary structure)
    receipts = A.receipts + C.receipts

    # extra merged (last wins on key collision; concrete later)
    extra = {**A.extra, **C.extra}

    if not paired_cells and not receipts and not extra:
        return N

    return Carrier(
        cells=tuple(paired_cells),
        m_contrib=m,
        receipts=receipts,
        extra=extra,
    )


# ---------------------------------------------------------------------------
# 1.8 Complete collapse rule
# ---------------------------------------------------------------------------

def collapse(
    raw: Union[Carrier, StructuralNull],
    erase: Optional[Callable[[Carrier], Carrier]] = None,
) -> Union[Carrier, StructuralNull]:
    """
    Canonical post-dispatch state after typed erasure + prune.
    Collapses to N exactly when no structural support survives.
    Payload algebraic zero alone does not force collapse.
    """
    if is_null(raw):
        return N
    assert isinstance(raw, Carrier)
    if erase is not None:
        raw = erase(raw)
    return prune(raw)


# ---------------------------------------------------------------------------
# Convenience constructors
# ---------------------------------------------------------------------------

def unit() -> Carrier:
    """Designated carrier unit (M = 1, positive support)."""
    return Carrier(
        cells=(Cell(coordinate=0, payload=1, mu=1.0),),
        m_contrib=1.0,
    )


def from_payload(
    payload: Any,
    *,
    mu: float = 1.0,
    m_contrib: float = 1.0,
    receipt: Any = None,
) -> Union[Carrier, StructuralNull]:
    """Construct a single-cell carrier. Algebraic zero payload is still non-null if mu > 0."""
    if mu <= 0.0 and receipt is None:
        return N
    cells = (Cell(payload=payload, mu=max(0.0, mu)),)
    receipts = (receipt,) if receipt is not None else ()
    return Carrier(cells=cells, m_contrib=m_contrib, receipts=receipts)


# ---------------------------------------------------------------------------
# Self-check (minimal, no external test runner required)
# ---------------------------------------------------------------------------

def _self_check() -> None:
    assert is_null(N)
    assert faithful_breadth(N) == 0.0
    assert radius(N) == 0.0
    assert support_weight(N) == 0.0
    assert product_character(N) == 0.0

    u = unit()
    assert not is_null(u)
    assert u.M() == 1.0
    assert u.W() > 0.0
    assert u.B() > 0.0
    assert 0.0 < u.a() < 1.0

    # algebraic zero payload with positive support remains non-null
    z = from_payload(0, mu=1.0)
    assert not is_null(z)
    assert support_weight(z) > 0.0

    # pairing is multiplicative on W and M
    p = pair(u, u)
    assert not is_null(p)
    assert abs(p.W() - u.W() * u.W()) < 1e-12
    assert abs(p.M() - u.M() * u.M()) < 1e-12

    # Null absorbs
    assert is_null(pair(N, u))
    assert is_null(pair(u, N))

    # prune of null-support cells
    emptyish = Carrier(cells=(Cell(mu=0.0),), m_contrib=1.0)
    assert is_null(prune(emptyish))

    print("ucns.core self-check passed")


if __name__ == "__main__":
    _self_check()
