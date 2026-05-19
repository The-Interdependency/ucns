"""
Minimal depth-2 oracle composite example for UCNS v1.0 review.

GPT generated; context, prompt Erin Spencer.
"""

from fractions import Fraction

from ucns import FactorizationResultKind, UCNSObject, UNIT, factorization_result, multiply
from ucns import S2


A = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
B = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
P = multiply(A, B)

result = factorization_result(P)

assert result.result_kind == FactorizationResultKind.FACTORS
assert result.has_factors
rec_A, rec_B = result.factors
assert multiply(rec_A, rec_B) == P
assert result.claim_scope == "composite-found"

print("depth2_oracle_minimal: ok")
print(f"result_kind={result.result_kind.value}")
print(f"domain={result.product_domain_label}")
print(f"claim_scope={result.claim_scope}")
print("recomposition=True")
