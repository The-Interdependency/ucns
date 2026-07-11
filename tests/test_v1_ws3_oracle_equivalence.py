"""Workstream 3 — oracle predicate/catalogue equivalence.

``is_oracle_atom(obj)`` must be extensionally identical to structural
membership in the canonical generated catalogue, by construction
(codex-handoff/03).  Geometric boundedness is not an oracle
certificate.
"""

from fractions import Fraction

from ucns import (
    UCNSObject,
    UNIT,
    ORACLE_ATOM_PAYLOADS,
    ORACLE_CATALOGUE_RULE_VERSION,
    catalogue_fingerprint,
    factorization_result,
    FactorizationResultKind,
    generate_payload_catalogue,
    in_domain,
    is_oracle_atom,
    verified_domain_status,
)

CANONICAL = generate_payload_catalogue()


def _structural_member(obj, catalogue):
    return any(m is not None and m == obj for m in catalogue)


def test_every_catalogue_member_is_oracle_atom():
    for member in CANONICAL:
        assert is_oracle_atom(member)


def test_witness_bounded_but_not_catalogue_is_not_oracle():
    """The prior false-certainty witness, covered explicitly and not by
    special-casing: within geometric bounds, outside the catalogue."""
    x = UCNSObject(
        4, 4,
        [(Fraction(0), None), (Fraction(3, 2), None)],
        [0, 0],
    )
    assert in_domain(x), "witness must sit inside the geometric bounds"
    assert not _structural_member(x, CANONICAL)
    assert not is_oracle_atom(x)


def test_predicate_equals_membership_on_adversarial_universe():
    """Every normalized depth-one object over the full carrier-grid
    angle set (n_min <= 4), lengths 1..3, all face assignments:
    predicate == structural membership, no exceptions."""
    angles = []
    for q in range(1, 5):
        for p in range(0, 2 * q):
            a = Fraction(2 * p, q) % 4
            if a not in angles:
                angles.append(a)
    catalogue_set = set(m for m in CANONICAL if m is not None)
    checked = inside = 0
    for length in range(1, 4):
        def gen(prefix):
            if len(prefix) == length:
                yield list(prefix)
                return
            for a in angles:
                yield from gen(prefix + [a])
        for angle_seq in gen([]):
            for face_bits in range(2 ** length):
                faces = [(face_bits >> i) & 1 for i in range(length)]
                try:
                    obj = UCNSObject(
                        24, 1,
                        [(a, None) for a in angle_seq],
                        faces,
                    )
                except ValueError:
                    continue
                member = obj in catalogue_set
                assert is_oracle_atom(obj) == member, (
                    f"predicate/membership split on angles={angle_seq} "
                    f"faces={faces}"
                )
                checked += 1
                inside += 1 if member else 0
    assert checked > 5000, "universe too small to be adversarial"
    assert 0 < inside < checked, "universe must straddle the boundary"


def test_none_is_oracle_atom():
    assert is_oracle_atom(None)
    assert CANONICAL[0] is None


def test_catalogue_deterministic_dedup_stable_fingerprint():
    a = generate_payload_catalogue()
    b = generate_payload_catalogue()
    assert len(a) == len(b)
    for x, y in zip(a, b):
        assert (x is None and y is None) or (x == y)
    assert catalogue_fingerprint(a) == catalogue_fingerprint(b)
    non_unit = [m for m in a if m is not None]
    for i, m in enumerate(non_unit):
        assert not any(m == other for other in non_unit[:i]), "duplicate member"
    assert a is not b, "copy-on-return"
    assert isinstance(ORACLE_ATOM_PAYLOADS, tuple), "immutable public constant"
    assert isinstance(ORACLE_CATALOGUE_RULE_VERSION, str)


def test_bounded_noncatalogue_payload_is_depth2_non_oracle():
    """A depth-two object carrying a bounded-but-non-catalogue payload is
    classified depth-2-non-oracle and cannot receive a certified
    negative from the default catalogue."""
    payload = UCNSObject(
        4, 4,
        [(Fraction(0), None), (Fraction(3, 2), None)],
        [0, 0],
    )
    obj = UCNSObject(4, 4, [(Fraction(0), payload)], [0])
    assert verified_domain_status(obj) == "depth-2-non-oracle"
    res = factorization_result(obj)
    if res.result_kind == FactorizationResultKind.SEQ_PRIME:
        assert not res.negative_result_certified
        assert not res.seq_prime_is_absolute
