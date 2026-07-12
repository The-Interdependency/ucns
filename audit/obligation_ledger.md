# Base-geometry obligation ledger

Mirror of §2 of the base-geometry completion handoff (2026-07-10).  The
audit (`audit/reconcile.py`) reconciles this table against the
`# === CONTRACTS ===` witness declarations in `ucns/` **by text parsing
only** — it imports neither the ledger nor the source modules — and
against the RepoLOTO state in `.loto/`.

Run: `python audit/reconcile.py` (from the repo root; exit 0 = reconciled,
zero unmatched either direction).  Latest-run-wins applies per identical
command string.

## Obligations

| id | law | rung on arrival | rung landed | witness (CONTRACTS id → evidence) | proof | loto |
|---|---|---|---|---|---|---|
| `multiply_well_defined` | ⊠ total + representation-independent at all depths | `[test-backed]` | `[mutation-verified]` | `multiply_well_defined` → `contracts/test_multiply_canonical.py` | `docs/base-geometry.md` §1 | CLOSED |
| `multiply_identity` | θ=0 origin is a two-sided identity | `hmmm` | proven two-sided + `[mutation-verified]` | `multiply_identity` → `contracts/test_identity_two_sided.py` | `docs/base-geometry.md` §2 | CLOSED |
| `multiply_associativity` | (a⊠b)⊠c = a⊠(b⊠c) | `hmmm` — never tested | **proven** + `[mutation-verified]` | `multiply_associativity` → `contracts/test_associativity_triples.py` | `docs/base-geometry.md` §3 | CLOSED |
| `multiply_commutativity_ruling` | non-commutative in general; commuting subclass characterized | partial | proven ruling + `[mutation-verified]` | `multiply_commutativity_ruling` → `contracts/test_commutator.py` | `docs/base-geometry.md` §4 | CLOSED |
| `division_theory` | left/right quotients: existence + multiplicity | `hmmm` | solvability theorem + `[mutation-verified]` | `division_theory` → `contracts/test_quotient_solvability.py` | `docs/base-geometry.md` §5 | CLOSED |
| `structure_naming` | name the algebraic object | pending O1–O5 | structure theorem: length-graded non-cancellative monoid | `structure_naming` → `contracts/test_structure_axioms.py` | `docs/base-geometry.md` §6 | CLOSED |
| `addition_boundary` | primitive addition, or only derived? | `hmmm` | ruled: no second primitive; ⊕ derived, right-distributive only | `addition_boundary` → `contracts/test_addition_boundary.py` | `docs/base-geometry.md` §7 | CLOSED |

`loto = CLOSED` means the corresponding `.loto/<id>` lock has been deleted
at target rung per RepoLOTO; `.loto/` empty of lock files = base geometry
closed.  The reconciler fails if a lock exists for a CLOSED row or a lock
is missing for an OPEN row.

## Formal search-model holes and declared boundaries (Theorem N, 2026-07-12)

This section enumerates every remaining `sorry` and every declared opaque
or modeling boundary in `formal/Ucns/TheoremN.lean` after the finite-search
model replaced the opaque `FindsFactorization`/`ContainsPayloads`
predicates.  It is informational: `audit/reconcile.py` reconciles only the
seven base-geometry obligations above and does not parse this section.

- theoremN_catalogue_sufficient_completeness — `sorry`; statement now
  unfolds to "some enumerated candidate survives unit rejection and
  exactly recomposes"; no proof exists.
- lemma7_depth2_oracle_completeness — `sorry`; instance statement, no
  proof exists.
- depth1_restricted_completeness — `sorry`; base statement, no proof
  exists.
- face-superset equivalence — declared boundary: `faceAssignments`
  enumerates all `2^k` bit lists while `recover_face_structures` derives
  the at-most-two XOR-consistent options; witness-space equality under the
  exact-recomposition gate is undischarged in Lean.  Test-backed on the
  declared fixture domain by `tests/test_formal_conformance.py`.
- no-renormalization assembly — declared boundary: Lean `assemble` applies
  no normalization while the Python constructor normalizes; agreement on
  host-normalized products of normalized factors is undischarged in Lean.
  Test-backed on the declared fixture domain by the same suite.
- catalogue-dedup omission — declared boundary: `normalizedCandidates`
  omits structural deduplication (membership-preserving; size/order only).
- Lean-side fixture evaluation — undischarged: the shared conformance
  fixture is currently executed on the Python side only; the authoring
  environment had no Lean toolchain, so `formal.yml` CI is the type-check
  authority and no Lean evaluation of the fixture has run.
- `Ucns/Core.lean` retains the refuted `AlignedComplete` cancellativity
  counterexample (`not_multiply_left_cancellative_on_alignedComplete`);
  cancellativity is not a premise of the Theorem N search model.

No opaque success predicate remains in `formal/Ucns/TheoremN.lean`; a green
`lake build` remains a type-check only and confers no proof status while
any hole above remains.

## Findings of record (this run)

1. **Associativity proven** — the handoff's pivot question ("does the θ
   payload carry the resultant vector?") dissolves: the algebra carries the
   full angle sequence; the circular-mean collapse exists only in the
   `geometry_bridge` projection.  ⊠ is a monoid operation.
2. **Commutator relocated** — the handoff guessed the commutator lives in
   the chirality bits; the (z, w) composition is symmetric and the whole
   geometric projection commutes.  The commutator lives in sequence
   ordering.  Center = unit towers.
3. **v0.6 Left-Quotient Completeness scope-corrected** — counterexample
   found (2026-07-10); the theorem's E10.4 cancellativity premise is false
   at depth ≥ 2 divisors.  Greedy primitives remain sound; complete
   enumeration now in `ucns/division_theory.py`; flat-divisor
   cancellativity proven (explains the v0.5.1 depth-0/1 regression's zero
   violations).  `right_quotient` additionally used a left-quotient payload
   helper where the dual needs a right quotient — observed as extra misses.
4. **Non-uniqueness canonized** — `T_d ⊠ x = T_d` has exactly `d`
   solutions; ALT-FACTOR / `store.left_factors` multiplicity is structural
   (O6 ruling), not a defect.  Canonical choice remains open.
   Cancellativity is fully characterized by the **dichotomy** (Theorem
   5.5): a divisor cancels iff at least one top-level payload is the unit
   (flat divisors are the special case; found via adversarial review of
   an earlier "exactly flat" over-claim, then proven).
5. **Carrier boundary pinned** — empty objects are excluded from the
   carrier: left-empty absorbs, right-empty raises; totality holds on the
   nonempty carrier.

## File plan deltas vs the handoff

- `contracts/test_addition_boundary.py` added (the handoff's §4 file plan
  listed no O7 test file; its `tests:` field was `hmmm`).  The O7 ruling
  needs a witness, so it got one.
- `contracts/_harness.py` added: shared deterministic generators and the
  mutant implementations used by every `[mutation-verified]` check.
- `tests/test_base_geometry_contracts.py` added so the existing CI pytest
  invocation runs the seven aggregates without a workflow change.

## Conventions applied (best effort where the skill is not vendored)

- `# ratios:` bookends (first + last line) are present on every **new**
  source file.  The canonical counting rule is not vendored in this repo;
  counts here use: `loc_comments` = non-blank non-comment code lines :
  comment+docstring lines; `imports_exports` = import statements : public
  surface entries; `calls_definitions` = call sites : def/class
  definitions.  Calibrated against `.agents/skills/manifest/generate.py`
  and `msdmd/parsers/universal.py` precedents (defs/imports match; comment
  accounting approximate — `hmmm`).
- `self::fn` call resolution interpreted as: contract modules call their
  own helpers unqualified and cross-module code only through explicit
  module imports; no dynamic dispatch.  Exact skill-lib semantics `hmmm`
  (skill-lib is not vendored here).
- Field-entry rule: CONTRACTS blocks use only fields the test-build
  reference runner consumes (`id`, `given`, `then`, `class`, `call`).

## Run log (latest-run-wins per identical command string)

| command | last run | result |
|---|---|---|
| `python -m pytest ucns_recursive/tests tests -v` | 2026-07-10 | see PR CI |
| `python audit/reconcile.py` | 2026-07-10 | reconciled |
| `UCNS_EXHAUSTIVE=1 python -m pytest contracts/test_quotient_solvability.py` | 2026-07-10 | 10 passed (full 6,084-pair sweep; CI default is a stride sample per PR #96 review) |

Adversarial-review note: a multi-agent refutation pass was run before
commit; the division-theory refuter surfaced two statement-precision
defects (the cancellativity boundary over-claim, fixed by Theorem 5.5;
the `SolutionLimitExceeded` docstring over-claim, reworded).  The
remaining lanes were re-run post-merge-request:

- **Compliance lane**: one violation — the CI shim lacked ratios
  bookends — fixed; RepoLOTO lifecycle, CONTRACTS doctrine, MODULE_BUILD
  schema, claims honesty, and packaging verified compliant.
- **Code lane**: four findings, all fixed — (D1) O5's mutation check
  mutated the greedy primitive rather than the witnessed enumerators
  (the enumerators' final verification is a never-firing guard; the
  cross-row intersection is load-bearing) → replaced with a row-0-only
  enumerator mutant caught by the soundness law; (D2) O1's mutation
  check used a toy canonicalizer → now monkeypatches the real
  `UCNSObject.normalize`; (D3) the CONTRACTS then-clause now carries the
  identity-convention carve-out; (D4) dichotomy fibers strengthened from
  `<= 1` to exact singleton `{b}`.  Reconciler negative paths verified
  (missing witness, bad call target, stray/duplicate locks, malformed
  block all exit 1); determinism and non-vacuity of every conditional
  test loop probed at their exact seeds.
- **Core-algebra lane**: complete — NO DEFECTS FOUND under hostile
  attack: ~4,000 associativity triples (depth ≤ 5, adversarial grids,
  all payload None-patterns); center two-witness separation over 3,041
  random length-≥2 objects plus engineered evaders with cores buried at
  nesting 4–7 (one false alarm traced to the attacker's witness pool,
  resolved by the theorem's own recursive lift recipe); unit-group
  search over 30,976 ordered pairs found exactly {e, u₁}; dichotomy
  held both directions including engineered identical-absorption rows.
  All three review lanes are closed; no open review follow-up remains.
