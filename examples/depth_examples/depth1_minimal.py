"""
Minimal depth-1 seq-prime example for UCNS v1.0 review.

GPT generated; context, prompt Erin Spencer.
"""

from fractions import Fraction

from ucns import FactorizationResultKind, UCNSObject, UNIT, factorization_result


P = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
result = factorization_result(P)

assert result.result_kind == FactorizationResultKind.SEQ_PRIME
assert result.product_domain_label == "depth-1"
assert result.seq_prime_is_absolute is True
assert result.claim_scope == "defended-domain-relative"

print("depth1_minimal: ok")
print(f"result_kind={result.result_kind.value}")
print(f"domain={result.product_domain_label}")
print(f"seq_prime_is_absolute={result.seq_prime_is_absolute}")
print(f"claim_scope={result.claim_scope}")
