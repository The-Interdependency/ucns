"""Pin the boundary between domain prerequisites and result certification."""

from ucns import S2, factorization_result, seq_prime_requires_scope


def test_complete_domain_label_alone_never_clears_scope():
    assert seq_prime_requires_scope("depth-1")
    assert seq_prime_requires_scope("depth-2-oracle")


def test_certified_result_envelope_may_clear_scope():
    result = factorization_result(S2)
    assert result.negative_result_certified
    assert not result.requires_scope
