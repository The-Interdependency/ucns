"""
Tests for typed UCNS domain-status metadata.
"""

import unittest

from ucns_recursive import (
    DomainProofStatus,
    domain_status_metadata,
    is_verified_domain_label,
    seq_prime_requires_scope,
    status_for_object,
)
from ucns_recursive.domains import S2
from ucns_recursive.canonical import UCNSObject, UNIT
from fractions import Fraction


class TestDomainStatusMetadata(unittest.TestCase):
    def test_depth_1_is_defended_and_verified(self):
        metadata = domain_status_metadata("depth-1")
        self.assertIn(DomainProofStatus.DEFENDED, metadata.statuses)
        self.assertTrue(metadata.completeness_guaranteed)
        self.assertTrue(metadata.is_defended)
        self.assertFalse(metadata.is_frontier)

    def test_depth_2_oracle_is_oracle_complete(self):
        metadata = domain_status_metadata("depth-2-oracle")
        self.assertIn(DomainProofStatus.ORACLE_COMPLETE, metadata.statuses)
        self.assertTrue(metadata.completeness_guaranteed)
        self.assertEqual(metadata.seq_prime_claim_scope, "oracle-domain-relative")

    def test_depth_2_non_oracle_is_frontier_not_absolute(self):
        metadata = domain_status_metadata("depth-2-non-oracle")
        self.assertIn(DomainProofStatus.FRONTIER, metadata.statuses)
        self.assertFalse(metadata.completeness_guaranteed)
        self.assertTrue(metadata.is_frontier)
        self.assertTrue(seq_prime_requires_scope("depth-2-non-oracle"))

    def test_unknown_label_is_experimental_frontier(self):
        metadata = domain_status_metadata("future-domain")
        self.assertIn(DomainProofStatus.EXPERIMENTAL, metadata.statuses)
        self.assertFalse(metadata.completeness_guaranteed)
        self.assertTrue(metadata.is_frontier)
        self.assertEqual(metadata.seq_prime_claim_scope, "unknown-non-absolute")

    def test_verified_domain_label_helper(self):
        self.assertTrue(is_verified_domain_label("depth-0"))
        self.assertTrue(is_verified_domain_label("depth-1"))
        self.assertTrue(is_verified_domain_label("depth-2-oracle"))
        self.assertFalse(is_verified_domain_label("depth-2-non-oracle"))
        self.assertFalse(is_verified_domain_label("depth-3+"))

    def test_status_for_object_unit(self):
        metadata = status_for_object(UNIT)
        self.assertEqual(metadata.label, "depth-0")
        self.assertTrue(metadata.completeness_guaranteed)

    def test_status_for_object_depth_1(self):
        metadata = status_for_object(S2)
        self.assertEqual(metadata.label, "depth-1")
        self.assertTrue(metadata.completeness_guaranteed)

    def test_status_for_object_depth_2_oracle(self):
        obj = UCNSObject(
            2,
            2,
            [(Fraction(0), S2), (Fraction(1), UNIT)],
            [0, 0],
        )
        metadata = status_for_object(obj)
        self.assertEqual(metadata.label, "depth-2-oracle")
        self.assertTrue(metadata.completeness_guaranteed)


if __name__ == "__main__":
    unittest.main()
