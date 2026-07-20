from fractions import Fraction

from ucns import FactorizationResultKind, UCNSObject, UNIT, factorization_result
from ucns import S2

payload = UCNSObject(2, 2, [(Fraction(0), S2), (Fraction(1), UNIT)], [0, 0])
P = UCNSObject(2, 2, [(Fraction(0), payload), (Fraction(1), UNIT)], [0, 0])
result = factorization_result(P, catalogue=[UNIT])

assert result.result_kind == FactorizationResultKind.SEQ_PRIME
assert result.seq_prime_is_absolute is False
assert result.requires_scope is True

print("catalogue_boundary: ok")
print(f"domain={result.product_domain_label}")
print(f"scope={result.claim_scope}")
