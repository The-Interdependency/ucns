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
domain_status        Typed theorem / implementation status metadata
serialization        Canonical JSON serialization and stable hashing

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
domain status        A0-facing typed certainty metadata
serialization        A0-facing canonical identity bytes + hashes
canonical              UCNSObject definition, multiply, is_unit,
                       is_multiplicative_unit
domains                Frozen domain D' parameters, oracle predicates,
                       verified-domain status taxonomy
host_recovery          Recover host angle/face structures from a product
recursive_quotient     Catalogue-bounded payload factor finders
payload_system         Coupled payload equation solver
witness_matrix         Witness and WitnessMatrix for global consistency
factor_search_v08      Top-level factorization engine (witness-matrix solver)
domain_status          Typed theorem / implementation status metadata
serialization          Canonical JSON serialization and stable hashing
factorization_result   A0-facing factorization result envelopes
object_record          A0-facing object inspection records

Deployable surface (May 2026)
-----------------------------
recursive_codec        Python ↔ UCNSObject encoder/decoder        (v0.1, item 2+4)
left_quotient          Constructive left/right quotient            (v0.1, item 3)
store                  UCNSStore — keyed corpus + algebraic retrieval
                                                                   (v0.1, item 5)
catalogue              Catalogue builders for factor_decompose
                                                                   (v0.1+v0.2)
domain dispatch        Oracle-class predicates and the
                       enforce_verified_domain insert gate
                                                                   (v0.2, item 6)
domain status          A0-facing typed certainty metadata
serialization          A0-facing canonical identity bytes + hashes
factorization result   A0-facing scoped factorization claims
object record          A0-facing object inspection metadata
"""

from .canonical import (
    UCNSObject,
    UNIT,
    multiply,
    is_unit,
    is_multiplicative_unit,
)
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

# Typed domain-status metadata
from .domain_status import (
    DomainProofStatus,
    DomainStatusMetadata,
    VERIFIED_DOMAIN_LABELS,
    domain_status_metadata,
    is_verified_domain_label,
    seq_prime_requires_scope,
    status_for_object,
)

# Canonical serialization / stable identity hashes
from .serialization import (
    CANONICAL_SERIALIZATION_VERSION,
    DEFAULT_HASH_ALGORITHM,
    canonical_data,
    canonical_json,
    canonical_bytes,
    stable_hash,
    stable_hash_bytes,
)

# Factorization result envelope
from .factorization_result import (
    FactorizationResultKind,
    FactorizationResult,
    factorization_result,
)

# Object inspection record
from .object_record import UCNSObjectRecord, object_record

# Retrieval
from .store import Match, OutOfDomainError, UCNSStore

# Catalogue helpers
from . import catalogue
from .geometry_bridge import (
    GeometricPoint,
    HomomorphismResult,
    check_injectivity,
    compose,
    homomorphism_check,
    ucns_a_to_g,
)

__all__ = [
    # algebraic core
    "UCNSObject",
    "UNIT",
    "multiply",
    "is_unit",
    "is_multiplicative_unit",
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
    # typed domain-status metadata
    "DomainProofStatus",
    "DomainStatusMetadata",
    "VERIFIED_DOMAIN_LABELS",
    "domain_status_metadata",
    "status_for_object",
    "is_verified_domain_label",
    "seq_prime_requires_scope",
    # canonical serialization / stable identity hashes
    "CANONICAL_SERIALIZATION_VERSION",
    "DEFAULT_HASH_ALGORITHM",
    "canonical_data",
    "canonical_json",
    "canonical_bytes",
    "stable_hash",
    "stable_hash_bytes",
    # factorization result envelope
    "FactorizationResultKind",
    "FactorizationResult",
    "factorization_result",
    # object inspection record
    "UCNSObjectRecord",
    "object_record",
    # retrieval
    "UCNSStore",
    "Match",
    "OutOfDomainError",
    # catalogue helpers
    "catalogue",
    # geometry bridge: homomorphism proof UCNS-A ↔ UCNS-G
    "GeometricPoint",
    "ucns_a_to_g",
    "compose",
    "homomorphism_check",
    "HomomorphismResult",
    "check_injectivity",
]
