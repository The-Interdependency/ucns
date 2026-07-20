"""Regression for one-shot payload catalogue handling in result envelopes."""

from fractions import Fraction

from ucns import (
    FactorizationResultKind,
    UCNSObject,
    UNIT,
    factorization_result,
    multiply,
)


E = UCNSObject(1, 1, [(Fraction(0), UNIT)], [0])
T2 = UCNSObject(1, 1, [(Fraction(0), E)], [0])


def test_one_shot_catalogue_is_materialized_once_and_still_finds_factors():
    """Coverage and search must consume the same materialized sequence.

    ``T2`` is the one-cell recursive composite satisfying ``T2 * T2 == T2``.
    A generator yielding ``[None, E]`` contains the payloads needed to recover
    that factorization. Re-consuming the generator would present an empty
    catalogue to search and could turn this composite into a false negative.
    """
    assert multiply(T2, T2) == T2

    one_shot = (entry for entry in (UNIT, E))
    result = factorization_result(T2, catalogue=one_shot)

    assert result.result_kind == FactorizationResultKind.FACTORS
    assert result.factors is not None
    assert multiply(result.factors[0], result.factors[1]) == T2
    assert result.catalogue_source == "caller"
    assert result.supplied_catalogue_size == 2
    assert result.coverage_bound_to_search_report
    assert not result.negative_result_certified
    assert result.uncertified_reasons == ("factors-found",)
