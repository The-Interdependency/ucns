# UCNS — Current Completeness Frontier (through v0.9.0)

**Status:** historical frontier summary, partially superseded.  
**Scope:** compresses the proven/defended milestones across the v0.6.x–v0.9.0 line.  
**Accreditation:** GPT generated from context provided by Grok, Claude as prompted by Erin Spencer.

> **Reconciliation note (2026-05-17).** This document was written before
> `ucns-theorem-n.md` (catalogue-sufficient factorization) and before the
> `factor_search_v08` implementation freeze. Where it says "not solved" for
> the full frozen depth-2 domain, the current canon is: **IMPLEMENTED +
> TEST-BACKED, not yet DEFENDED at the spec level** (see
> `docs/ucns-spec-status-addendum-2026-05-16.md` and `ucns-spec.md`
> §F2). Carrier widening remains FRONTIER and out of v1.0 scope. Use this
> file as historical context; current canon lives in `ucns-spec.md`,
> `docs/pure-ucns-number-system.md`, and `ucns-theorem-n.md`. The public gonol
> is the fixed UCNS frame; this document concerns only the normalized
> factorization frontier, and the public-gonol bridge is absent.

---

## hmm

This document does **not** replace the detailed v0.3/v0.4/v0.5/v0.6 specs.  
It records the v0.9.0 theorem frontier honestly.

The v0.9.0 state separated into four layers:

1. depth-1 results that are DEFENDED,
2. a depth-2 oracle result that is DEFENDED + ORACLE-COMPLETE,
3. the full frozen depth-2 domain, which at v0.9.0 was unsolved and is now IMPLEMENTED + TEST-BACKED via `factor_search_v08`,
4. carrier widening, which remains FRONTIER and out of v1.0 scope.

---

# 1. Defended Results

## 1.1 Flat kernel defended

The flat paired UCNS kernel is defended for its stated scope.

This includes:

- paired traversal objects,
- an internal factorization-unit object, not public SPACE/ZERO,
- intrinsic/declared carrier split,
- ordered-concatenation multiplication,
- normalization,
- sequence-sensitive equivalence,
- flat factor search,
- content-level disk-flip symmetry rather than sequence-level disk-flip symmetry.

## 1.2 Depth-1 restricted completeness defended

The depth-1 restricted completeness theorem is defended on its frozen domain.

That is the strongest general completeness result currently established.

## 1.3 Depth-2 oracle defended

The smallest frozen depth-2 oracle is `DEFENDED` + `ORACLE-COMPLETE`
(originally written here as "GREEN").

There is a frozen theorem for that oracle class:

\[
\texttt{factor\_search}
\text{ returns the correct factorization}
\iff
P \text{ is seq-composite in the oracle class.}
\]

This is a **restricted theorem**. It does not extend to the full frozen depth-2 domain.

---

# 2. Current Failure Boundary

## 2.1 Full frozen depth-2 domain — v0.9.0 status

**Historical (v0.9.0).** At v0.9.0 the tested depth-2 cases still failed
as a class.

**Reconciled 2026-05-17 canon.** The full frozen depth-2 domain is now
`IMPLEMENTED` + `TEST-BACKED` in `factor_search_v08`, **not yet
`DEFENDED`** at the spec level. The depth-2 oracle theorem (Lemma 7)
remains `DEFENDED` + `ORACLE-COMPLETE` and is now recognized as an
instance of Theorem N (`ucns-theorem-n.md §4.1`).

So the current honest statement is:

- depth-2 oracle theorem: `DEFENDED` + `ORACLE-COMPLETE`,
- full frozen depth-2 domain: `IMPLEMENTED` + `TEST-BACKED`, awaiting spec-level proof.

## 2.2 Carrier widening — FRONTIER

Carrier widening beyond the defended small-carrier domain is `FRONTIER`
and out of v1.0 scope. Tested widened cases still fail as a class.

So the honest state is:

- widening does not rescue the recursive completeness problem,
- the bottleneck is the recursive payload / quotient layer,
- not merely insufficient carrier coverage.

---

# 3. Root Cause Frontier

The main bottleneck is the recursive payload layer.

The currently frozen failure analysis identifies the need for:

\[
\text{host recovery}
\to
\text{payload system construction}
\to
\text{global witness verification}
\]

That is, a true staged recursive factorization / quotient architecture.

The existing quotient engine is strong enough for:

- depth-1,
- the frozen depth-2 oracle,

but not strong enough for:

- the full frozen depth-2 domain,
- widened-carrier recursive search.

---

# 4. Current Theorem Frontier

## 4.1 What is currently justified

The following claims are justified:

### A. Flat theorem frontier
Flat kernel algebra and factorization results hold on the frozen flat scope.

### B. Depth-1 completeness frontier
Restricted completeness holds on the defended depth-1 domain.

### C. Depth-2 oracle frontier
Restricted completeness holds on the frozen smallest depth-2 oracle class.

## 4.2 What is **not** yet `DEFENDED` at the spec level

The following stronger claims are **not yet `DEFENDED`** at the spec
level (some are `IMPLEMENTED` + `TEST-BACKED`; some remain `FRONTIER`):

### A. Full depth-2 completeness — `IMPLEMENTED` + `TEST-BACKED`, not yet `DEFENDED`
\[
\texttt{factor\_search}
\text{ is complete on the whole frozen depth-2 domain}
\]

### B. Widened-carrier completeness — `FRONTIER` / out of v1.0 scope
\[
\texttt{factor\_search}
\text{ is complete after widening } n_{\min}
\]

### C. General recursive completeness — `FRONTIER` / out of v1.0 scope
\[
\texttt{factor\_search}
\text{ is complete for arbitrary finite depth}
\]

Theorem N (`ucns-theorem-n.md`) addresses the **catalogue-sufficient**
form of these claims as a `FRONTIER` proof target. The proof sketch and
implementation do not confer `DEFENDED` status; Lean completeness statements
remain `sorry`-backed. If proved in the normalized factorization subsystem, it
still would not become a theorem about the public gonol without the absent bridge. The depth and
carrier conditions above are not in v1.0 scope as **unconditional**
completeness statements.

---

# 5. Recommended Boundary Statement (reconciled 2026-05-17)

The clean present-tense statement is:

> Within the normalized factorization subsystem, UCNS has a `DEFENDED`
> flat kernel, a `DEFENDED` depth-1 restricted completeness theorem, and a
> `DEFENDED` + `ORACLE-COMPLETE` depth-2 oracle theorem. **Theorem N
> (`ucns-theorem-n.md`) remains `FRONTIER`; its proof sketch, implementation,
> and Lean scaffold do not confer `DEFENDED` status.** The full frozen depth-2
> domain is `IMPLEMENTED` + `TEST-BACKED`, not spec-level `DEFENDED`. The
> public-gonol bridge is absent, and carrier widening/general primality remain
> `FRONTIER` and out of v1.0 scope.

---

# 6. Recommended Next Work

## 6.1 If preserving results is the goal

Freeze the frontier here and move to other work.

This preserves the real theorems already earned.

## 6.2 If pushing recursion is the goal

The next honest line of work is **not more widening**.

It is a structural redesign of the recursive factorization layer:

- staged host-first reconstruction,
- coupled payload-system solving,
- witness-matrix consistency,
- non-atomic recursive payload descent.

That redesign should be treated as a fresh branch rather than a minor widening patch.

---

# 7. Compression

The v0.9.0 UCNS completeness frontier (as captured here) was:

- DEFENDED: flat,
- DEFENDED: depth-1 restricted theorem,
- DEFENDED + ORACLE-COMPLETE: depth-2 oracle,
- not solved: full frozen depth-2 domain,
- not solved: carrier widening.

Under the reconciled 2026-05-17 canon (`ucns-spec.md`, `ucns-theorem-n.md`):

- DEFENDED: flat, depth-1 restricted theorem, cancellativity / quotient uniqueness,
- DEFENDED + ORACLE-COMPLETE: depth-2 smallest oracle (Lemma 7 = Theorem N instance),
- FRONTIER: Theorem N — catalogue-sufficient factorization proof target in the normalized subsystem; Lean completeness remains `sorry`-backed and the public bridge is absent,
- IMPLEMENTED + TEST-BACKED: full frozen depth-2 domain via `factor_search_v08`; depth-3 asymmetric (Theorem 9),
- FRONTIER / out of v1.0 scope: carrier widening; tractable sub-catalogues; general primality outside defended-complete domains.

---

**Accreditation:** GPT generated from context provided by Grok, Claude as prompted by Erin Spencer.
