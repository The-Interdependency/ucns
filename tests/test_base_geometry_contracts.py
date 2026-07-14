# ratios: loc_comments=25:12 imports_exports=10:8 calls_definitions=12:8
"""CI shim: run every base-geometry contract aggregate under pytest.

The contract implementations live in ``contracts/`` (test-build / msdmd
convention: the promises are ``# === CONTRACTS ===`` blocks in engine modules;
the evidence is one aggregate callable per obligation). CI's pytest invocation
collects ``ucns_recursive/tests`` and ``tests``, so this shim gives the
obligations first-class CI presence without a workflow change.
``audit/reconcile.py`` checks the obligation/witness bijection for declared
canonical contracts.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from contracts.test_addition_boundary import contract_addition_boundary
from contracts.test_associativity_triples import contract_multiply_associativity
from contracts.test_commutator import contract_multiply_commutativity_ruling
from contracts.test_identity_two_sided import contract_multiply_identity
from contracts.test_local_groups_and_geometry import (
    contract_local_groups_and_relational_geometry,
)
from contracts.test_multiply_canonical import contract_multiply_well_defined
from contracts.test_quotient_solvability import contract_division_theory
from contracts.test_structure_axioms import contract_structure_naming


def test_o1_multiply_well_defined():
    contract_multiply_well_defined()


def test_o2_multiply_identity():
    contract_multiply_identity()


def test_o3_multiply_associativity():
    contract_multiply_associativity()


def test_o4_multiply_commutativity_ruling():
    contract_multiply_commutativity_ruling()


def test_o5_division_theory():
    contract_division_theory()


def test_o6_structure_naming():
    contract_structure_naming()


def test_o7_addition_boundary():
    contract_addition_boundary()


def test_o8_o9_local_groups_and_relational_geometry():
    contract_local_groups_and_relational_geometry()

# ratios: loc_comments=25:12 imports_exports=10:8 calls_definitions=12:8
