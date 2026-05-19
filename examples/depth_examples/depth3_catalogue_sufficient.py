"""
Minimal depth-3 catalogue-sufficient example for UCNS v1.0 review.

GPT generated; context, prompt Erin Spencer.
"""

from fractions import Fraction

from ucns import FactorizationResultKind, UCNSObject, UNIT, factorization_result, multiply
from ucns import S2


def payload_closure(*objects):
    """Return None plus recursive payloads from the provided objects."""
    catalogue = [UNIT]

    def collect(obj):
        if obj is None:
            return
        for _, payload in obj.A_plus:
            if payload is not None and payload not in catalogue:
                catalogue.append(payload)
                collect(payload)

    for obj in objects:
        collect(obj)
    return catalogue


# depth-2 payload, then a depth-3 factor carrying it.
depth2_payload = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
A = UCNSObject(2, 2, [(Fraction(0), depth2_payload), (Fraction(1), UNIT)], [0, 0])
B = UCNSObject(2, 2, [(Fraction(0), UNIT), (Fraction(1), UNIT)], [0, 0])
P = multiply(A, B)

catalogue = payload_closure(A, B)
result = factorization_result(P, catalogue=catalogue)

assert result.result_kind == FactorizationResultKind.FACTORS
assert result.has_factors
rec_A, rec_B = result.factors
assert multiply(rec_A, rec_B) == P
assert result.claim_scope == "composite-found"

print("depth3_catalogue_sufficient: ok")
print(f"result_kind={result.result_kind.value}")
print(f"domain={result.product_domain_label}")
print(f"catalogue_size={len(catalogue)}")
print(f"claim_scope={result.claim_scope}")
print("recomposition=True")
