"""
ucns.catalogue — d3 oracle extension (DRAFT)
======================================================
Adds ``build_catalogue_d3_oracle`` and supporting predicate
``is_in_oracle_class_d3``.

This file is a DRAFT against Lemma 8 (depth-3 factor search soundness +
completeness, under coverage).  Intended as a patch overlay onto
``ucns/catalogue.py`` and ``ucns/domains.py``.

Status of guarantees provided by this draft
-------------------------------------------
- **Soundness**: every returned object satisfies
  ``is_in_oracle_class_d3(obj) == True`` and has depth exactly 3.
- **Coverage**: returned **as an attribute** of the result, not
  unconditionally.  A ``D3CatalogueResult`` carries
  ``exhausted: bool`` — True iff enumeration completed without
  hitting the size budget.  ``exhausted=True`` is necessary for
  Lemma 8's coverage hypothesis to hold against the natural D''
  defined by closure over the chosen ``payload_basis``.

What's NOT settled in this draft (gating ambiguities surfaced by
writing it — these are the new hmmm items):

- **hmmm A — depth-3 multiplication semantics not pinned here.**
  Coverage in the Lemma 8 sense requires: for every P ∈ D'',
  ∃ X, Y ∈ C with multiply(X, Y) ≡_seq P.  This draft enumerates
  the *constructive* D'' (objects built by direct constructor
  with depth-2 oracle payloads), not the *multiplicative* D''
  (objects reachable by multiply over D' × D').  These coincide iff
  the depth-3 multiply rule is exactly "multiply payload-wise +
  lift," which matches the depth-2 oracle case but is asserted
  not proven for depth-3.  See coverage attestation note below.

- **hmmm B — `payload_basis` choice and the chirality interaction.**
  Chirality (per spec v0.3 reassertion) may exclude some
  ``(angles, payloads, faces)`` triples that the constructor
  would otherwise accept.  This draft delegates to ``UCNSObject``'s
  ValueError on construction; if chirality is enforced in the
  constructor, exclusion is automatic.  If it's enforced upstream,
  this enumerator will overgenerate.  Verify before relying.

- **hmmm C — size estimation.**
  With the default basis (full ``build_catalogue_d2_oracle()`` output),
  the inner product is ``|d2_basis|^length`` per ``(n_min, length,
  face_bits)`` combination.  ``|d2_basis|`` for the frozen D' is
  empirically in the few-thousands range; ``length=3`` makes this
  catastrophic.  The ``max_objects`` budget exists precisely
  because naive exhaustion is computationally infeasible — but
  budget exhaustion *forfeits* the coverage attestation.  Caller
  must choose: budget high enough to exhaust (slow, complete),
  or budget capped (fast, requires separate coverage proof for the
  truncated catalogue).
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_catalogue_d3
#   module_name: catalogue_d3
#   module_kind: engine
#   summary: DRAFT depth-3 oracle-class predicate and bounded catalogue enumerator (build_catalogue_d3_oracle) carrying a coverage attestation against Lemma 8.
#   owner: Erin Spencer
#   public_surface: is_in_oracle_class_d3, D3CatalogueResult, build_catalogue_d3_oracle
#   internal_surface: _recursive_obj_key
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_catalogue_d3
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical, ucns_domains, ucns_catalogue
#   since: 2026-06-02
#   unresolved: DRAFT - depth-3 constructive-vs-multiplicative D'' coverage equivalence, payload_basis/chirality interaction, and size-budget exhaustion gating are all unproven (hmmm A/B/C in module docstring)
# === END MODULE_BUILD ===

import itertools
from dataclasses import dataclass
from fractions import Fraction
from typing import List, Optional, Tuple

from .canonical import UCNSObject, UNIT
from .catalogue import build_catalogue_d2_oracle
from .domains import (
    A_PLUS_MAX,
    N_MIN_MAX,
    depth_of,
    is_in_oracle_class,
)


def _recursive_obj_key(obj: Optional[UCNSObject]) -> tuple:
    """Fully-recursive structural deduplication key.

    Mirrors ``catalogue._obj_key`` but recurses to arbitrary depth
    rather than stopping at depth-2.  Required at depth-3 because
    payloads are themselves depth-2 objects whose own payloads
    must be distinguished.
    """
    if obj is None:
        return None
    return (
        obj.n_min,
        tuple(obj.F_plus),
        tuple(
            (a, _recursive_obj_key(p))
            for a, p in obj.A_plus
        ),
    )

__all__ = [
    "is_in_oracle_class_d3",
    "D3CatalogueResult",
    "build_catalogue_d3_oracle",
]


# ----------------------------------------------------------------------
# Predicate: depth-3 oracle class
# ----------------------------------------------------------------------

def is_in_oracle_class_d3(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is in the depth-3 oracle class.

    An object is in the depth-3 oracle class when:
    - it is in the depth-2 oracle class (covered by Lemma 7), OR
    - its depth is exactly 3 AND every cell payload is in the
      depth-2 oracle class (i.e. covered by Lemma 7).

    Objects with depth ≥ 4 are never in the depth-3 oracle class.

    Note: this predicate is the structural definition of D''
    membership.  Whether the depth-3 multiplication rule actually
    closes over this set is hmmm A and is NOT decided by this
    predicate.
    """
    if obj is None:
        return True
    d = depth_of(obj)
    if d <= 2:
        return is_in_oracle_class(obj)
    if d >= 4:
        return False
    # depth == 3: every cell payload must be in the depth-2 oracle class.
    return all(is_in_oracle_class(payload) for _, payload in obj.A_plus)


# ----------------------------------------------------------------------
# Result type with coverage attestation
# ----------------------------------------------------------------------

@dataclass
class D3CatalogueResult:
    """Result of ``build_catalogue_d3_oracle``.

    Attributes
    ----------
    objects:
        The deduplicated list of depth-3 oracle-class UCNSObjects.
    exhausted:
        True iff enumeration completed without hitting ``max_objects``.
        **Lemma 8's coverage hypothesis requires exhausted=True**
        against the natural D'' defined by closure over the
        ``payload_basis`` used.  False means the catalogue is a
        prefix of the full enumeration and coverage must be
        re-established by separate argument (e.g. the narrow-
        tailored catalogue empirical sweep approach).
    payload_basis_size:
        ``len(payload_basis)`` at call time.  Recorded for
        reproducibility — different bases yield different D''.
    truncated_at:
        If exhausted=False, the (n_min, length, face_bits) tuple
        at which the budget was hit.  None if exhausted=True.
    """
    objects: List[UCNSObject]
    exhausted: bool
    payload_basis_size: int
    truncated_at: Optional[Tuple[int, int, int]]

    def coverage_attestation(self) -> str:
        """Human-readable coverage status string.

        Use this when emitting catalogue metadata into proof
        documents or Lemma 8 application sites.
        """
        if self.exhausted:
            return (
                f"COVERS D''[basis_size={self.payload_basis_size}] "
                f"unconditionally (enumeration exhausted, "
                f"{len(self.objects)} objects)"
            )
        return (
            f"PARTIAL: {len(self.objects)} objects, truncated at "
            f"{self.truncated_at}, basis_size="
            f"{self.payload_basis_size} — coverage NOT attested, "
            f"separate proof required for Lemma 8 application"
        )


# ----------------------------------------------------------------------
# Catalogue builder
# ----------------------------------------------------------------------

def build_catalogue_d3_oracle(
    payload_basis: List[Optional[UCNSObject]],
    max_objects: Optional[int] = None,
) -> D3CatalogueResult:
    """Return depth-3 oracle-class UCNSObjects built from *payload_basis*.

    Parameters
    ----------
    payload_basis:
        The depth-2-oracle objects (and unit) to place in cell
        payloads of depth-3 objects.  **Required, not optional.**

        Originally drafted with a default of
        ``[None] + build_catalogue_d2_oracle()``.  Empirically this
        OOM-kills before the d3 enumeration even starts:
        ``build_catalogue_d2_oracle()`` with the full d1 basis
        is itself catastrophically large.  No safe default exists —
        caller must specify.

        Suggested constructions:

        - **Narrow-tailored** (matches Item 3 sweep approach):
          hand-pick depth-2 payloads relevant to the targets you
          intend to factor.  Forfeits unconditional D'' coverage but
          tractable.
        - **Tight oracle**: call ``build_catalogue_d2_oracle(
          payload_basis=[None, S2, ...small list])`` to get a
          bounded depth-2 basis, then prepend ``None`` and pass
          here.  Coverage holds against the D'' defined by
          *that* basis, not against the frozen D' D''.

    max_objects:
        If non-None, terminate enumeration after this many
        deduplicated objects have been collected.  The result's
        ``exhausted`` field will be False and ``truncated_at`` will
        record the truncation point.  ``None`` = unbounded
        (recommended only for narrow ``payload_basis``).

    Returns
    -------
    A ``D3CatalogueResult`` carrying the objects and a coverage
    attestation.  Each object satisfies
    ``is_in_oracle_class_d3(obj) == True`` and has depth exactly 3
    (at least one payload is itself depth ≥ 1, ensuring depth lift).

    Notes
    -----
    Lemma 8 application requires ``result.exhausted == True``
    against the same ``payload_basis`` used to define D''.
    Use ``result.coverage_attestation()`` to emit the status string
    for inclusion in proof artifacts.
    """
    if payload_basis is None:
        raise ValueError(
            "payload_basis is required — no safe default exists. "
            "The natural default ([None] + build_catalogue_d2_oracle()) "
            "OOM-kills before enumeration starts. See module docstring "
            "(hmmm C) for tractable construction patterns."
        )

    # Filter the basis to ensure every element is actually in the
    # depth-2 oracle class (defensive — caller may pass arbitrary list).
    payload_basis = [p for p in payload_basis if is_in_oracle_class(p)]

    objects: List[UCNSObject] = []
    seen: set = set()
    truncated_at: Optional[Tuple[int, int, int]] = None
    exhausted: bool = True

    outer_iter = (
        (n_min, length, face_bits)
        for n_min in range(1, N_MIN_MAX + 1)
        for length in range(1, A_PLUS_MAX + 1)
        for face_bits in range(2 ** length)
    )

    for (n_min, length, face_bits) in outer_iter:
        angles = [Fraction(2 * k, n_min) for k in range(length)]
        faces = [(face_bits >> i) & 1 for i in range(length)]

        for payloads in itertools.product(payload_basis, repeat=length):
            # Need at least one payload of depth >= 1 to reach depth 3.
            # (All-None payloads → depth 1; all depth-1 payloads → depth 2;
            #  at least one depth-2 payload → depth 3.)
            if not any(depth_of(p) >= 2 for p in payloads):
                continue

            try:
                obj = UCNSObject(
                    n_dec=n_min * 2,
                    n_min=n_min,
                    A_plus=list(zip(angles, payloads)),
                    F_plus=faces,
                )
            except ValueError:
                # Constructor rejected (chirality, well-formedness,
                # whatever the canonical layer enforces — hmmm B).
                continue

            if not is_in_oracle_class_d3(obj):
                # Defensive — shouldn't happen given filtered basis,
                # but if `is_in_oracle_class` and the constructor
                # disagree on edge cases, surface that here rather
                # than silently include garbage.
                continue

            if depth_of(obj) != 3:
                # The "any payload depth >= 2" check above is
                # necessary but not sufficient if the constructor
                # canonicalizes payloads in ways that collapse depth.
                # Skip rather than admit a non-depth-3 into the d3
                # catalogue.
                continue

            key = _recursive_obj_key(obj)
            if key in seen:
                continue

            seen.add(key)
            objects.append(obj)

            if max_objects is not None and len(objects) >= max_objects:
                exhausted = False
                truncated_at = (n_min, length, face_bits)
                break

        if not exhausted:
            break

    return D3CatalogueResult(
        objects=objects,
        exhausted=exhausted,
        payload_basis_size=len(payload_basis),
        truncated_at=truncated_at,
    )
