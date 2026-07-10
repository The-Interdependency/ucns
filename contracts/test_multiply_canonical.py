# ratios: loc_comments=88:40 imports_exports=2:5 calls_definitions=46:6
"""O1 — multiply_well_defined: ⊠ total + representation-independent.

Witness for the CONTRACTS entry ``multiply_well_defined`` in
``ucns/canonical.py``.  Proof: ``docs/base-geometry.md`` §1.
"""

# === MODULE_BUILD ===
# id: multiply_well_defined
#   module_name: multiply_totality
#   module_kind: engine
#   summary: prove multiply is total and canonical (representation-independent) at all depths
#   owner: Erin Spencer
#   public_surface: none
#   internal_surface: contract_multiply_well_defined, test_totality_and_grading, test_representation_independence, test_empty_carrier_boundary, test_mutation_caught
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: contracts.test_multiply_canonical
#   rollout: backbone; everything downstream assumes it
#   rollback: revert to empirical closure
#   since: 2026-07-10
#   unresolved: none
# === END MODULE_BUILD ===

from ucns.canonical import UCNSObject, multiply

from contracts._harness import E, make_rng, rand_angle, rand_obj, raw_of


def test_totality_and_grading():
    """600 mixed-depth pairs: product constructs, is normalized, carrier
    divisibility holds, and length multiplies (the grading)."""
    rng = make_rng(1)
    for i in range(600):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        p = multiply(a, b)
        assert isinstance(p, UCNSObject), f"pair {i}: product not an object"
        assert p.A_plus[0][0] == 0, f"pair {i}: product not normalized"
        assert p.n_dec % p.n_min == 0, f"pair {i}: carrier not a multiple of n_min"
        assert len(p.A_plus) == len(a.A_plus) * len(b.A_plus), (
            f"pair {i}: grading violated"
        )


def test_representation_independence():
    """Gauge-shifted and n_dec-varied raw representations of the same
    object multiply to equal products."""
    rng = make_rng(2)
    for i in range(300):
        a = rand_obj(rng, rng.randint(1, 3))
        b = rand_obj(rng, rng.randint(1, 3))
        delta = rand_angle(rng)
        angles, payloads, faces = raw_of(a)
        a_rep = UCNSObject(
            48, 1,
            [((x + delta) % 4, p) for x, p in zip(angles, payloads)],
            faces,
        )
        assert a_rep == a, f"pair {i}: gauge representation not canonicalized"
        assert multiply(a_rep, b) == multiply(a, b), (
            f"pair {i}: product depends on the representation"
        )


def test_empty_carrier_boundary():
    """The carrier of the base geometry is NONEMPTY objects: an empty
    left operand absorbs, an empty right operand is undefined.  This
    pins the boundary rather than papering over it."""
    empty = UCNSObject(1, 1, [], [])
    absorbed = multiply(empty, E)
    assert len(absorbed.A_plus) == 0, "empty left operand must absorb"
    try:
        multiply(E, empty)
    except IndexError:
        pass
    else:
        raise AssertionError(
            "multiply(E, empty) unexpectedly succeeded; carrier boundary moved"
        )


def test_mutation_caught():
    """[mutation-verified], against the real code path: the actual
    canonicalizer (UCNSObject.normalize) is replaced by a mutant that
    forgets the mod-4 reduction; gauge-equivalent raw representations
    then stop colliding (or totality breaks), and the
    representation-independence witness detects it."""
    rng = make_rng(3)
    original_normalize = UCNSObject.normalize

    def mutant_normalize(self):
        if not self.A_plus:
            return self
        theta0 = self.A_plus[0][0]
        shifted = []
        for theta, payload in self.A_plus:
            new_theta = theta - theta0  # mutant: no % 4 reduction
            new_payload = payload.normalize() if payload is not None else None
            shifted.append((new_theta, new_payload))
        self.A_plus = shifted
        angles = [x for x, _ in self.A_plus]
        self.n_min = self._compute_n_min(angles)
        self.A_minus, self.F_minus = self._star()
        if self.n_dec % self.n_min != 0:
            raise ValueError("mutant carrier violation")
        return self

    caught = False
    UCNSObject.normalize = mutant_normalize
    try:
        for _ in range(50):
            a = rand_obj(rng, 1, 3)
            if len(a.A_plus) < 2:
                continue
            angles = [x for x, _ in a.A_plus]
            payloads = [payload for _, payload in a.A_plus]
            delta = rand_angle(rng)
            try:
                a_rep = UCNSObject(
                    48, 1,
                    [((x + delta) % 4, payload)
                     for x, payload in zip(angles, payloads)],
                    list(a.F_plus),
                )
            except ValueError:
                caught = True  # totality broke under the mutant
                break
            if a_rep != a:
                caught = True  # representation independence broke
                break
    finally:
        UCNSObject.normalize = original_normalize
    assert caught, "real-canonicalizer mutant was not caught"


def contract_multiply_well_defined():
    """test-build aggregate entry point for obligation O1."""
    test_totality_and_grading()
    test_representation_independence()
    test_empty_carrier_boundary()
    test_mutation_caught()
# ratios: loc_comments=88:40 imports_exports=2:5 calls_definitions=46:6
