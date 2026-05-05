"""
ucns_recursive
==============
UCNS recursive factorization engine — frozen depth-2 domain.

Modules
-------
canonical            UCNSObject definition, multiply, is_unit
domains              Frozen domain D' parameters, oracle predicates,
                     verified-domain status taxonomy
host_recovery        Recover host angle/face structures from a product
recursive_quotient   Catalogue-bounded payload factor finders
payload_system       Coupled payload equation solver
witness_matrix       Witness and WitnessMatrix for global consistency
factor_search_v08    Top-level factorization engine (witness-matrix solver)

Deployable surface (May 2026)
-----------------------------
recursive_codec      Python ↔ UCNSObject encoder/decoder        (v0.1, item 2+4)
left_quotient        Constructive left/right quotient            (v0.1, item 3)
store                UCNSStore — keyed corpus + algebraic retrieval
                                                                 (v0.1, item 5)
catalogue            Catalogue builders for factor_decompose
                                                                 (v0.1+v0.2)
domain dispatch      Oracle-class predicates and the
                     enforce_verified_domain insert gate
                                                                 (v0.2, item 6)
"""

from .canonical import UCNSObject, UNIT, multiply, is_unit
from .factor_search_v08 import factor_search_v08

# Codec
from .recursive_codec import (
    EncodingError,
    recursive_decode,
    recursive_encode,
)

# Algebraic primitives
from .left_quotient import left_quotient, right_quotient

# Domain / oracle predicates (Item 6)
from .domains import (
    DEPTH_MAX,
    A_PLUS_MAX,
    N_MIN_MAX,
    S2,
    ORACLE_ATOM_PAYLOADS,
    in_domain,
    depth_of,
    is_oracle_atom,
    is_in_oracle_class,
    verified_domain_status,
)

# Retrieval
from .store import Match, OutOfDomainError, UCNSStore

# Catalogue helpers
from . import catalogue

__all__ = [
    # algebraic core
    "UCNSObject",
    "UNIT",
    "multiply",
    "is_unit",
    "factor_search_v08",
    # codec
    "recursive_encode",
    "recursive_decode",
    "EncodingError",
    # quotient primitives
    "left_quotient",
    "right_quotient",
    # domains / oracle
    "DEPTH_MAX",
    "A_PLUS_MAX",
    "N_MIN_MAX",
    "S2",
    "ORACLE_ATOM_PAYLOADS",
    "in_domain",
    "depth_of",
    "is_oracle_atom",
    "is_in_oracle_class",
    "verified_domain_status",
    # retrieval
    "UCNSStore",
    "Match",
    "OutOfDomainError",
    # catalogue helpers
    "catalogue",
]
