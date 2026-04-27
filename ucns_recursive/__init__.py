"""
ucns_recursive
==============
UCNS recursive factorization engine — frozen depth-2 domain.

Modules
-------
canonical        UCNSObject definition, multiply, is_unit
domains          Frozen domain D' parameters and payload catalogue
host_recovery    Recover host angle/face structures from a product object
recursive_quotient   Find a payload factor given the other factor
payload_system   Coupled payload equation solver
witness_matrix   Witness and WitnessMatrix for global consistency checking
factor_search_v08  Top-level factorization engine (witness-matrix solver)
"""

from .canonical import UCNSObject, multiply, is_unit
from .factor_search_v08 import factor_search_v08

__all__ = [
    "UCNSObject",
    "multiply",
    "is_unit",
    "factor_search_v08",
]
