# UCNS Cryptographic Domain — v0

**Status:** SPECIFICATION / PLANNING artifact. This document does **not**
claim a secure public-key system exists. It defines a candidate UCNS
cryptographic domain for PCEA-UCNS (see `PLAN.md`) and forbids domains
that the existing UCNS factorization tools demonstrably break. The
forbidden-domain conclusions are derived from measured attacks
(`attack_harness.py`, gated by `tests/test_attack_harness.py`), not from
argument.

**Accreditation:** Claude generated from repository context as prompted
by Erin Spencer; attack numbers reproduced from `attack_harness.run_all()`
against The-Interdependency/ucns at the Carrier-LCM Law + pruning
release.

**Security posture (inherited from `contract.py`):** PCEA's symmetric
security rests on key management, and adversaries are assumed able to
invert carrier arithmetic. This document concerns the *asymmetric* layer
UCNS must supply, where the hardness assumption is different and not yet
established. Nothing here upgrades PCEA's current claims.

## Public-frame correction

This planning artifact concerns the normalized recursive factorization subsystem only. The canonical public gonol is the fixed 157-position twist-bearing frame and is not a cryptographic carrier chosen by `n_min`. The Carrier-LCM result cited below is an internal projected-`n_min` identity, not a theorem about the complete public gonol. No cryptographic construction or hardness claim follows from the public frame. Historical attack counts require the immutable run artifact that produced them; source code and prose alone are not execution evidence.

---

---

## What today's UCNS results force

Three measured facts shape every answer below.

1. **The internal projected-`n_min` LCM identity leaks projected factorization support.** Within the normalized factorization subsystem, `n_min(A ⊠ B) = lcm(n_min(A), n_min(B))` on its declared domain. This is not a public-gonol carrier theorem. A cryptographic design must therefore not hide secrets in that projected support; this statement does not establish security elsewhere.

2. **The oracle domain is unsuitable for key material.** Its declared `ORACLE-COMPLETE` factor-search status means catalogue-bounded negatives and recoveries are not a hardness foundation. Historical recovery rates are not repeated here without their immutable execution artifact.

3. **Internal support pruning can accelerate catalogue search.** Any key space enumerable as a normalized-subsystem payload catalogue may inherit that reduction. Exact historical percentages require a cited immutable run artifact and are not a public-gonol claim.

## The ten questions (PLAN.md Phase 1)

**1. What is a UCNS private key?**
Candidate: structure the public projection's carrier does *not* reveal —
specifically (a) the angle *positions* within a fixed, publicly-known
carrier, (b) face-bit configuration, and (c) payload structure at a depth
beyond any catalogue-complete domain. NOT carrier choice (leaked, fact 1).

**2. What is a UCNS public key?**
A normalized factorization object whose projected `n_min` and gross shape are publishable, derived from
the private key by a forward operation (composition) such that recovering
the private structure requires cross-prime factoring (the open frontier).

**3. What is the base carrier or base object?**
An internal projected-`n_min` instance in the analytic-frontier regime — historically the **carrier-40,
⟨2,5⟩ cross-prime instance** named in the ucns frontier docs: the
smallest case where forward composition stays in-lattice but factoring
must cross prime lines. Real candidates scale the prime set and carrier
well beyond any oracle-complete bound.

**4. What operation derives the public key?**
Forward `multiply` (Law-governed, fast, public). The public key is a
product; the private key is a factor whose recovery is the hard problem.

**5. What operation derives the shared secret?**
KEM-style (preferred per PLAN.md): `encapsulate` composes the peer public
key with fresh randomness into a packet; `decapsulate` uses the private
factor to recover the shared object, which is then run through the
existing `kdf.key_stream` to a PCEA session key. The arithmetic produces
key *material*; `hashlib` does the final derivation.

**6. What exactly is the assumed hard problem?**
**Cross-prime UCNS factoring outside catalogue-complete domains:** given a
public product P with carrier in the frontier regime, recover a private
factor when the catalogue is NOT sufficient (so Theorem N does not apply)
and the prime support spans multiple primes (so forward-lattice closure
gives no shortcut). This problem is **OPEN in ucns** — which is the only
reason it is a candidate. Its hardness is **assumed, not proved**; if the
analytic frontier closes constructively, this assumption dies with it.

**7. Which UCNS domains are forbidden (factor-search-complete)?**
- The frozen depth-2 **oracle domain** (measured ~87% recovery).
- Any domain where the key catalogue is **catalogue-sufficient** for
  Theorem N (factorization complete by construction).
- Any domain whose key carrier's prime support is **small enough to
  enumerate** the pruned catalogue (fact 3: pruning + small support =
  tractable search).
- Any single-prime / prime-power carrier domain (no cross-prime hardness
  to hide behind).

**8. What information is intentionally public?**
Internal projected `n_min`, object depth, gross cell count, the KEM
packet, and all algorithm parameters. Security must survive their
disclosure.

**9. What information must never be serialized publicly?**
Private angle positions within the carrier, private face bits, private
payload structure, the recovered shared object, and the PCEA session key.
The public-key serializer must be incapable of emitting these
(PLAN.md Phase 2 exit gate).

**10. What public object sizes are acceptable for mobile?**
Target: public key and KEM packet each serializable in low single-digit
kilobytes, decapsulation within interactive latency on the reference
device (Termux / Galaxy A16). Internal projected-`n_min` magnitude trades directly against
both — a Phase-2 measurement, not a guess.

## Toy domain (for tests)

A deliberately breakable domain: small ⟨2,5⟩ carriers, catalogue
provided. Used to confirm the harness *recovers* keys here (negative
control — the domain MUST fall), so that survival on the real candidate
domain is meaningful by contrast.

## Real candidate domain (described, not secured)

Cross-prime carriers well beyond oracle-complete bounds, private structure
in angle position / face / deep payload, public projection via forward
composition. **Explicitly unproven.** The path to any security claim runs
through the ucns analytic frontier, not through this document.

## Attack tools (named, not ignored — PLAN.md requirement)

`factor_search_v08`, `left_quotient` / `right_quotient`,
`prune_catalogue` / `prune_payload_catalogue`, `canonical_factorization`,
and the frozen oracle catalogue. `attack_harness.py` wires the first set
against candidate domains; expanding it to the full set is the Phase-1
follow-on.

## hmmm

- The hardness assumption (Q6) is load-bearing and **unproved**; it is
  the same open problem as ucns cross-prime widening, now wearing a
  security hat. If that frontier closes, PCEA-UCNS must fall back to
  symmetric-only — which `contract.py` already ensures it can.
- Q1's claim that angle-position is not Law-projected needs its own
  attack: a positional analog of `factor_search`. Not yet built; until
  it is, "the Law doesn't reach here" is a conjecture, not a result.
