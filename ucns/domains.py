"""
ucns.domains
======================
Frozen domain D' for the depth-2 solver, plus oracle-class predicates
and the verified-domain status taxonomy.

Domain parameters
-----------------
    depth ≤ 2,  |A⁺| ≤ 3,  n_min ≤ 4

Verified domain
---------------
The completeness theorems cover three strata:

    depth-0          the unit (None)
    depth-1          any flat object (all payloads None): v0.6 theorem
    depth-2-oracle   depth-2 objects whose cell payloads are all oracle
                     atoms: v0.8.1 oracle theorem

Outside the verified domain (depth-2-non-oracle, depth ≥ 3), soundness
is preserved but completeness is not proven.

Oracle atoms
------------
An oracle atom is ``None`` (the unit) or a **structural member of the
canonical generated oracle catalogue** — nothing else.  The catalogue
is the carrier-grid family produced by ``generate_payload_catalogue()``:
depth-1 objects whose raw angles form the arithmetic progression
``[2k/n_min for k in range(length)]`` over ``n_min ≤ 4`` and
``length ≤ 3``, with every face assignment.

This is deliberately **narrower** than "every depth-1 object within the
frozen-domain geometric bounds": being geometrically bounded
(``in_domain``) is not an oracle certificate.  Example: the depth-1
object with angles ``(0, 3/2)`` satisfies the bounds but is not a
catalogue member and is not an oracle atom (codex-handoff/03).

``is_oracle_atom`` is extensionally equivalent to catalogue membership
by construction: it tests structural membership in the precomputed
canonical catalogue.  ``ORACLE_ATOM_PAYLOADS`` is that catalogue as an
immutable tuple; ``generate_payload_catalogue()`` returns a fresh list
copy.  ``ORACLE_CATALOGUE_RULE_VERSION`` names the generation rule for
certification binding (see ``ucns.catalogue_certificate``).

``S2`` is the canonical smallest oracle atom:
    UCNSObject(2, 2, [(0, None), (1, None)], [0, 0])
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: ucns_domains
#   module_name: domains
#   module_kind: engine
#   summary: Defines the frozen depth-2 domain D', oracle-atom payload catalogue, and oracle-class / verified-domain predicates used to scope completeness claims.
#   owner: Erin Spencer
#   public_surface: DEPTH_MAX, A_PLUS_MAX, N_MIN_MAX, S2, ORACLE_ATOM_PAYLOADS, ORACLE_CATALOGUE_RULE_VERSION, generate_payload_catalogue, in_domain, depth_of, is_oracle_atom, is_in_oracle_class, verified_domain_status
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: ucns.tests.test_depth2_full_domain
#   rollout: default_enabled
#   rollback: remove module and its re-exports
#   requires: ucns_canonical
#   since: 2026-06-02
#   unresolved: none
# === END MODULE_BUILD ===

from fractions import Fraction
from typing import List, Optional, Tuple

from .canonical import UCNSObject, UNIT

__all__ = [
    "DEPTH_MAX",
    "A_PLUS_MAX",
    "N_MIN_MAX",
    "S2",
    "ORACLE_ATOM_PAYLOADS",
    "ORACLE_CATALOGUE_RULE_VERSION",
    "generate_payload_catalogue",
    "in_domain",
    "depth_of",
    "is_oracle_atom",
    "is_in_oracle_class",
    "verified_domain_status",
]


# ------------------------------------------------------------------
# Domain parameters
# ------------------------------------------------------------------

DEPTH_MAX: int = 2
A_PLUS_MAX: int = 3
N_MIN_MAX: int = 4


# ------------------------------------------------------------------
# Canonical oracle atom
# ------------------------------------------------------------------

S2: UCNSObject = UCNSObject(
    2, 2,
    [(Fraction(0), UNIT), (Fraction(1), UNIT)],
    [0, 0],
)


# ------------------------------------------------------------------
# Depth
# ------------------------------------------------------------------

def depth_of(obj: Optional[UCNSObject]) -> int:
    """Return the nesting depth of *obj* (None → 0)."""
    if obj is None:
        return 0
    max_payload_depth = max((depth_of(p) for _, p in obj.A_plus), default=0)
    return 1 + max_payload_depth


# ------------------------------------------------------------------
# Domain membership
# ------------------------------------------------------------------

def in_domain(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is within the frozen domain D'."""
    if obj is None:
        return True
    return (
        depth_of(obj) <= DEPTH_MAX
        and len(obj.A_plus) <= A_PLUS_MAX
        and obj.n_min <= N_MIN_MAX
    )


# ------------------------------------------------------------------
# Payload catalogue generation
# ------------------------------------------------------------------

# The generation rule identity, bound into catalogue-coverage
# certificates (ucns.catalogue_certificate).  Bump when the generator
# family, bounds, ordering, or deduplication change.
ORACLE_CATALOGUE_RULE_VERSION: str = "oracle-atoms-carrier-grid-v1"


def _generate_canonical_catalogue() -> Tuple[Optional[UCNSObject], ...]:
    """Generate the canonical oracle-atom catalogue once, at import.

    Deterministic order: the unit first, then the carrier-grid family
    ordered by (n_min, length, face_bits); structural duplicates are
    dropped, keeping the first occurrence.
    """
    objects: List[Optional[UCNSObject]] = [UNIT]
    seen: set = set()

    for n_min in range(1, N_MIN_MAX + 1):
        for length in range(1, A_PLUS_MAX + 1):
            angles = [Fraction(2 * k, n_min) for k in range(length)]
            for face_bits in range(2 ** length):
                faces = [(face_bits >> i) & 1 for i in range(length)]
                try:
                    obj = UCNSObject(
                        n_dec=n_min * 2,
                        n_min=n_min,
                        A_plus=[(a, None) for a in angles],
                        F_plus=faces,
                    )
                except ValueError:
                    continue
                key = (obj.n_min, tuple(obj.F_plus),
                       tuple(a for a, _ in obj.A_plus))
                if key not in seen:
                    seen.add(key)
                    objects.append(obj)

    return tuple(objects)


# Precomputed at import time.  Immutable public constant: the single
# source of truth for oracle-atom membership.
ORACLE_ATOM_PAYLOADS: Tuple[Optional[UCNSObject], ...] = (
    _generate_canonical_catalogue()
)

# Structural membership index (UCNSObject hashing is structural).
_ORACLE_ATOM_SET = frozenset(
    obj for obj in ORACLE_ATOM_PAYLOADS if obj is not None
)


def generate_payload_catalogue() -> List[Optional[UCNSObject]]:
    """Return the canonical oracle-atom catalogue as a fresh list.

    Deterministic, deduplicated, unit-first, copy-on-return.  Members
    are the carrier-grid depth-1 family described in the module
    docstring — NOT every depth-1 object within the geometric bounds.
    Rule identity: :data:`ORACLE_CATALOGUE_RULE_VERSION`.
    """
    return list(ORACLE_ATOM_PAYLOADS)


# ------------------------------------------------------------------
# Oracle-class predicates
# ------------------------------------------------------------------


def is_oracle_atom(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is an oracle atom.

    Oracle atoms are ``None`` (the unit) and the structural members of
    the canonical generated catalogue — extensional equivalence with
    ``generate_payload_catalogue()`` holds by construction because this
    predicate *is* a membership test against that catalogue.

    Geometric bounds are necessary but not sufficient: use
    :func:`in_domain` for the frozen-domain geometry check.
    """
    if obj is None:
        return True
    if not isinstance(obj, UCNSObject):
        return False
    return obj in _ORACLE_ATOM_SET


def is_in_oracle_class(obj: Optional[UCNSObject]) -> bool:
    """Return True iff *obj* is in the depth-2 oracle class.

    An object is in the oracle class when:
    - its depth is 0 or 1 (trivially covered by existing theorems), or
    - its depth is exactly 2 AND every cell payload is an oracle atom.

    Objects with depth ≥ 3 are never in the oracle class.
    """
    if obj is None:
        return True
    d = depth_of(obj)
    if d <= 1:
        return True
    if d >= 3:
        return False
    # depth == 2: every cell payload must be an oracle atom.
    return all(is_oracle_atom(payload) for _, payload in obj.A_plus)


def verified_domain_status(obj: Optional[UCNSObject]) -> str:
    """Return the verified-domain status string for *obj*.

    Returns one of:

    ``"depth-0"``            obj is None (the unit)
    ``"depth-1"``            flat object, all payloads None
    ``"depth-2-oracle"``     depth-2 object in the oracle class
    ``"depth-2-non-oracle"`` depth-2 object outside the oracle class
    ``"depth-3+"``           depth ≥ 3

    The verified domain (completeness guaranteed) is the union of
    ``"depth-0"``, ``"depth-1"``, and ``"depth-2-oracle"``.
    """
    if obj is None:
        return "depth-0"
    d = depth_of(obj)
    if d == 0:
        return "depth-0"
    if d == 1:
        return "depth-1"
    if d == 2:
        return "depth-2-oracle" if is_in_oracle_class(obj) else "depth-2-non-oracle"
    return "depth-3+"
