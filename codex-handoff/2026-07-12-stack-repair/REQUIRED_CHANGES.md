# UCNS stack repair — required changes

Date: 2026-07-12
Repository: `The-Interdependency/ucns`
Audience: coding specialist AI
Status: implementation handoff

## Governing objective

Make UCNS the single mathematical representation and factorization substrate used by METAPAT adapters and EDCM geometry without overstating theorem status or requiring downstream repositories to reproduce UCNS semantics.

The immediate repair is not a new factorization feature. It is alignment among:

- the current exhaustive Python search;
- the informal Theorem N argument;
- the Lean formal target;
- constructor invariants;
- cross-repository adapter contracts;
- release and claims documentation.

Before editing, read `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/claims-ledger.md`, `docs/base-geometry.md`, `ucns-theorem-n.md`, `formal/README.md`, `formal/Ucns/Core.lean`, `formal/Ucns/TheoremN.lean`, `ucns/factor_search_v08.py`, `ucns/payload_system.py`, `ucns/canonical.py`, and the repo-local `.agents/skills/` material. Follow the pinned `The-Interdependency/skill-lib` doctrine. Preserve `FRONTIER` status wherever a faithful machine proof remains incomplete.

## Required patch order

### 1. Rewrite Theorem N around exhaustive inclusion, not cancellation

The current Python payload solver exhaustively enumerates catalogue assignments and checks every coupled payload equation. The current prose proof still leans on quotient recovery or a cancellativity boundary to recover the original payload uniquely.

Reconcile `ucns-theorem-n.md`, README summaries, docstrings, claims ledger entries, and formal comments around this correct proof shape:

1. the true host split occurs in the finite split enumeration;
2. host recovery includes the true angle hosts;
3. face recovery includes the true face assignment;
4. catalogue sufficiency places every true recursive payload in the candidate catalogue;
5. exhaustive payload enumeration therefore includes the true payload assignment, regardless of non-uniqueness;
6. witness consistency accepts that assignment;
7. exact recomposition accepts the resulting factor pair;
8. the non-multiplicative-unit hypothesis prevents the true pair from being filtered out.

Remove wording that implies general quotient uniqueness, general cancellation, or recovery of *the* original factors. The target is finding **a** valid nontrivial factorization.

Keep the theorem at `FRONTIER` until the finite search and all supporting obligations are faithfully formalized and externally reviewed.

### 2. Replace opaque formal success with a faithful finite-search relation

`formal/Ucns/TheoremN.lean` must not obtain apparent progress by proving implications about an uninterpreted `FindsFactorization` predicate.

Introduce a staged formal model that corresponds to the executable algorithm. At minimum define:

- finite catalogue normalization with one unit sentinel;
- host split candidates;
- candidate payload assignments;
- candidate face assignments;
- exact recomposition acceptance;
- non-multiplicative-unit rejection;
- a success relation whose witness contains actual factors and product equality.

`ContainsPayloads` may remain an abstract hypothesis temporarily only if its semantics are explicit and independently testable. `FindsFactorization` must become a defined existential or executable finite-search outcome rather than an opaque proposition.

Add a conformance fixture shared between Python and Lean for small canonical cases. The formal model need not optimize identically, but it must enumerate the same valid witness space for the declared fixture domain.

Do not remove visible `sorry` markers by replacing them with new opaque assumptions. Every remaining hole and every opaque boundary must appear in `audit/obligation_ledger.md`.

### 3. Make constructor invariants explicit and enforced

The public algebra and contracts describe nonempty normalized objects with positive carrier sizes. Encode that boundary directly.

Required behavior:

- reject empty `A_plus` / `F_plus` objects;
- reject `n_dec < 1`;
- reject `n_min < 1` at input even though normalization recomputes it;
- retain parallel-length and face-bit validation;
- retain the rule that normalized `n_dec` must be a multiple of computed `n_min`;
- verify recursive payload types or document the exact duck-typing boundary;
- add adversarial tests in both the public API suite and compatibility suite.

If an empty object has an intentional mathematical role, stop and record `hmmm`; do not preserve accidental support merely because `normalize()` currently returns early.

### 4. Add one official cross-repository bridge surface

Create a narrow, versioned public adapter surface for sibling repositories. It must reuse `ucns.UCNSObject`; it must not create a second semantic object system.

The bridge should support a neutral record containing, at minimum:

- schema/version;
- declared and intrinsic carriers;
- normalized angles;
- face bits;
- recursive payload records;
- external provenance/tags that do not participate in UCNS equality unless explicitly declared;
- source canon digest where supplied.

Required operations:

- import a neutral bridge record into an actual `UCNSObject`;
- export an actual `UCNSObject` into the record;
- round trip without changing UCNS equality or stable hash;
- reject malformed or unsupported schema versions;
- keep provenance separate from theorem/domain status.

METAPAT may use this to encode semantic modules. EDCM may use it for geometry. Neither consumer may infer proof status from successful construction.

### 5. Define downstream proof-status metadata rules

Add a small public status envelope or adapter helper that lets consumers report UCNS evidence without flattening it into a boolean.

The surface must distinguish at least:

- object construction succeeded;
- search exhausted a declared finite boundary;
- catalogue coverage was validated;
- a negative result was certified within a declared domain;
- theorem layer status such as `DEFENDED`, `TEST-BACKED`, `ORACLE-COMPLETE`, or `FRONTIER`;
- no proof status attached.

Do not let a bare import, object hash, geometry equivalence, or successful bridge round trip imply theorem status.

### 6. Add the shared UCNS/METAPAT/EDCM contract suite

Create deterministic fixtures covering:

1. a METAPAT semantic module represented through the official UCNS bridge;
2. round-trip preservation of UCNS equality and stable hash;
3. preservation of external canon/provenance fields without letting them alter UCNS equality;
4. EDCM construction of a geometry/readout from the actual UCNS object;
5. `NA != 0` at the EDCM boundary;
6. explicit absence of UCNS theorem-status transfer into EDCM measurement output;
7. invalid bridge records rejected fail-closed;
8. manifest or canon digest change visible as an identity/provenance change.

The UCNS repository should own the canonical bridge fixtures. Sibling repositories may import or mirror only the fixture data with a pinned source commit and drift check.

### 7. Reconcile all claims and release surfaces

After implementation, reconcile:

- `README.md`;
- `docs/claims-ledger.md`;
- `ucns-theorem-n.md`;
- `CHANGELOG.md`;
- `formal/README.md`;
- `audit/obligation_ledger.md`;
- examples and docstrings;
- A0-facing status language;
- `MODULE_BUILD` and other msdmd metadata.

The source of truth must say that Theorem N is an exhaustive-inclusion completeness target, not a cancellativity theorem and not a uniqueness theorem.

### 8. Preserve and extend negative-certification discipline

Do not weaken the recently added certification boundary.

Any bridge or downstream convenience API must preserve these facts:

- raw `factor_search_v08` remains catalogue-relative;
- only the evidence-bearing result envelope may certify a negative;
- no caller boolean can promote certainty;
- malformed provenance, mismatched catalogue fingerprints, incomplete coverage, truncation, unrecognized pruning, or unit-domain targets fail closed;
- returned factors must exactly recompose.

Add regression tests proving bridge metadata cannot forge or promote negative certification.

## Required non-goals

Do not:

- claim universal recursive primality;
- claim canonical or unique factor recovery;
- restore general cancellativity language;
- call a successful Lean build with `sorry` a proof;
- encode METAPAT ontology into UCNS core definitions;
- encode EDCM behavioral meanings into UCNS core algebra;
- make external provenance affect UCNS equality without a separately ratified rule;
- weaken catalogue or domain scope in order to simplify the formal proof;
- advertise performance or tractability not established by benchmarks and declared domains.

## Verification gate

Run the existing release gate and the new bridge/formal conformance checks from a clean checkout:

```bash
python -m pip install -e .[dev]
python -m build
python -m twine check dist/*
python -m pytest ucns_recursive/tests tests contracts -v
```

Also run:

- clean-wheel installation and import smoke test;
- documented depth examples;
- docs claim guardrail;
- constructor adversarial tests;
- bridge round-trip tests;
- shared UCNS/METAPAT/EDCM fixtures;
- repo-local skill-lib drift and msdmd checks;
- `lake build Ucns.CarrierLcm`;
- the faithful finite-search Lean target and its conformance fixtures.

## hmmm

The formal search may be represented as an executable function, a finite relation, or a proved correspondence to a simpler reference enumerator. The unresolved implementation choice is acceptable. What is not acceptable is an opaque predicate whose name asserts that the real solver succeeds.