"""Public import namespace for the Unit Circle Number System package.

The recursive factorization engine lives directly under this package. Public
code should import from ``ucns`` and ``ucns.a0_safe``; ``ucns_recursive`` is only
a deprecated compatibility shim.

Core recursive modules include ``canonical``, ``domains``, ``host_recovery``,
``payload_system``, ``witness_matrix``, ``factor_search_v08``,
``domain_status``, ``serialization``, ``factorization_result``,
``object_record``, ``recursive_codec``, ``left_quotient``, ``store``,
``catalogue``, ``canonical_factorization``, ``catalogue_pruning``, and
``geometry_bridge``.
"""

from .canonical import (
    UCNSObject,
    UNIT,
    multiply,
    is_unit,
    is_multiplicative_unit,
)
from .factor_search_v08 import (
    FactorSearchReport,
    factor_search_report,
    factor_search_v08,
    payload_catalogue_fingerprint,
)

# Codec
from .recursive_codec import (
    EncodingError,
    recursive_decode,
    recursive_encode,
)

# Algebraic primitives
from .left_quotient import left_quotient, right_quotient

# Domain / oracle predicates
from .domains import (
    DEPTH_MAX,
    A_PLUS_MAX,
    N_MIN_MAX,
    S2,
    ORACLE_ATOM_PAYLOADS,
    ORACLE_CATALOGUE_RULE_VERSION,
    generate_payload_catalogue,
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
from .canonical_factorization import (
    enumerate_factorizations,
    canonical_factorization,
    canonical_key,
)
from .catalogue_pruning import (
    prime_support,
    carrier_lcm,
    prune_catalogue,
    payload_support,
    prune_payload_catalogue,
)
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
    "factor_search_report",
    "FactorSearchReport",
    "payload_catalogue_fingerprint",
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
    "ORACLE_CATALOGUE_RULE_VERSION",
    "generate_payload_catalogue",
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
    # canonical factor selection
    "enumerate_factorizations",
    "canonical_factorization",
    "canonical_key",
    # carrier-LCM law / carrier-support pruning
    "prime_support",
    "carrier_lcm",
    "prune_catalogue",
    "payload_support",
    "prune_payload_catalogue",
    # geometry bridge: homomorphism proof UCNS-A ↔ UCNS-G
    "GeometricPoint",
    "ucns_a_to_g",
    "compose",
    "homomorphism_check",
    "HomomorphismResult",
    "check_injectivity",
]
