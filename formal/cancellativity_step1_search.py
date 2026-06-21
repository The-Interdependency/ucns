#!/usr/bin/env python3
# Cancellativity Step-1 counterexample search (formalization track).
#
# Faithful stdlib port of amod/amod4/circleFrac/nMin/multiplyFuel/depth/
# HostNormalized from formal/Ucns/Core.lean. Read-only research artifact:
# neither imports nor modifies the engine. Decides whether
# `multiply_left_cancellative` holds as stated and which hypotheses restore it.
#
# Run:  python3 formal/cancellativity_step1_search.py   (Python >= 3.9: uses math.lcm)
#
# Object model:  o = (nd:int, cells: tuple of (angle:Fraction, face:bool, payload:o|None))
import math, itertools
from fractions import Fraction as F

# --- exact ports of the Lean definitions -----------------------------------
def amod(a, n):  return a - n * math.floor(a / n)
def amod4(a):    return amod(a, 4)
def circleFrac(a): return amod(a, 2) / 2
def nMin(cells):                      # canonical carrier: lcm of nonzero circle-fraction denoms
    d = 1
    for (a, _, _) in cells:
        q = circleFrac(a)
        if q != 0:
            d = math.lcm(d, q.denominator)
    return d
def mul(dn, a, b):                     # multiplyFuel : fuel 0 -> LEFT arg
    if dn == 0:
        return a
    nda, csA = a; ndb, csB = b
    b0 = csB[0][0] if csB else F(0)    # β0 = right operand's first-cell angle
    nc = []
    for (aa, af, ap) in csA:
        for (ba, bf, bp) in csB:
            ang = amod4(aa + (ba - b0)); fc = af ^ bf
            if   ap is not None and bp is not None: pay = mul(dn - 1, ap, bp)
            elif ap is not None:                    pay = ap
            elif bp is not None:                    pay = bp
            else:                                   pay = None
            nc.append((ang, fc, pay))
    return (math.lcm(nda, ndb), tuple(nc))
def depth(o):                          # Lean depth = 1 + max payload depth (FLAT OBJECT = 1)
    _, cs = o; m = 0
    for (_, _, p) in cs: m = max(m, 0 if p is None else depth(p))
    return 1 + m

# --- candidate hypotheses ---------------------------------------------------
def hn_top(o):                         # Core.lean HostNormalized: head cell angle == 0 only
    _, cs = o; return (not cs) or cs[0][0] == F(0)
def hn_rec(o):                         # recursive HostNormalized
    _, cs = o
    if cs and cs[0][0] != F(0): return False
    return all(p is None or hn_rec(p) for (_, _, p) in cs)
def nonempty_rec(o):                   # no empty cell-list anywhere
    _, cs = o
    return bool(cs) and all(p is None or nonempty_rec(p) for (_, _, p) in cs)
def canonical(o):                      # nd == nMin(cells), recursively (carrier is canonical)
    nd, cs = o
    return nd == nMin(cs) and all(p is None or canonical(p) for (_, _, p) in cs)
def uniform_depth(o):                  # complete tree: all root->leaf paths equal length
    _, cs = o
    if not cs: return False
    ds = {0 if p is None else depth(p) for (_, _, p) in cs}
    return len(ds) == 1 and all(p is None or uniform_depth(p) for (_, _, p) in cs)
def complete(o):                       # candidate sufficient domain (the conjunction)
    return nonempty_rec(o) and hn_rec(o) and uniform_depth(o) and canonical(o)

def rep(o):
    nd, cs = o
    return "mk%d[%s]" % (nd, ",".join("(%s,%s,%s)" % (c[0], 'T' if c[1] else 'F',
                         '.' if c[2] is None else rep(c[2])) for c in cs))

def ce(dn, S):
    n = 0; w = None
    for A in S:
        for B in S:
            p = mul(dn, A, B)
            for C in S:
                if B != C and mul(dn, A, C) == p:
                    n += 1; w = w or (A, B, C)
    return n, len(S), w

# ===========================================================================
def main():
    print("=== Cancellativity Step 1 (Core.lean port) ===\n")

    # (1) bare theorem — M1 host-angle (β0) collapse
    flat = [(1, ((a, f, None),)) for a in (F(0), F(1)) for f in (False, True)]
    n, _, w = ce(1, flat)
    A, B, C = w
    print("[M1] bare theorem, d=1: FALSE (β0 host-angle gauge).  witness B=%s C=%s -> %s"
          % (rep(B), rep(C), rep(mul(1, A, B))))

    # (1') top-only vs recursive HostNormalized (+ payloads present)
    nested = [(1, ((a, f, p),)) for a in (F(0), F(1)) for f in (False, True) for p in flat]
    pres = lambda o: all(p is not None for (_, _, p) in o[1])
    n, _, _ = ce(2, [o for o in nested if hn_top(o) and pres(o)])
    print("[M1'] top-only HostNormalized + payloads-present, d=2: CE=%d (payload-level β0)" % n)
    n, _, _ = ce(2, [o for o in nested if hn_rec(o) and pres(o)])
    print("      recursive HostNormalized + payloads-present, d=2: CE=%d" % n)

    # (2) Codex regression witnesses — four CONFIRMED counterexamples that
    #     survive (recursive HostNormalized + naive AllPayloadsPresent + depth<=d)
    print("\n[CODEX] confirmed counterexamples to the earlier 'corrected' statement:")
    leaf = (1, ((F(0), False, None),))
    d2 = (1, ((F(0), False, leaf),)); d3 = (1, ((F(0), False, d2),))
    E = (1, ())
    cases = [
        ("depth-mismatch atom", 3, d3, d2, d3),                         # B bottoms out before A
        ("carrier nDec/lcm",    2, (2, ((F(0), False, leaf),)),
                                    (1, ((F(0), False, leaf),)),
                                    (2, ((F(0), False, leaf),))),         # lcm not cancellative
        ("empty left operand",  2, E, (1, ((F(0), False, leaf),)),
                                       (1, ((F(0), True, leaf),))),        # csA.bind [] erases B
        ("empty payload atom",  2, (1, ((F(0), False, E),)),
                                    (1, ((F(0), False, E),)),
                                    (1, ((F(0), False, leaf),))),          # IsAtom accepts []
    ]
    for name, dn, A, B, C in cases:
        eq = mul(dn, A, B) == mul(dn, A, C)
        print("  %-20s d=%d: CE=%s  (B!=C:%s)" % (name, dn, "CONFIRMED" if (eq and B != C) else "no", B != C))

    # (3) candidate sufficient domain: complete = nonempty + recursive-HN + uniform-depth + canonical-carrier
    print("\n[DOMAIN] complete = nonempty(rec) + recursive HostNormalized + uniform-depth + canonical carrier (nd=nMin)")
    A1 = []
    for L in (1, 2):
        for combo in itertools.product([(F(0), False), (F(0), True), (F(1), False), (F(1), True)], repeat=L):
            if combo[0][0] != F(0): continue
            cells = tuple((a, f, None) for (a, f) in combo); A1.append((nMin(cells), cells))
    S1 = [o for o in A1 if complete(o)]
    n, k, _ = ce(1, S1); print("  d=1 over complete depth-1 (atoms), |S|=%d: CE=%d" % (k, n))
    # depth-2 Complete objects, length 1 AND 2 — multi-cell operands exercise the
    # csA.bind row partition (Obligation 3). Atom set includes a nonzero-carrier atom.
    atoms3 = [(1, ((F(0), False, None),)), (1, ((F(0), True, None),)),
              (2, ((F(0), False, None), (F(1), False, None)))]
    head = [(F(0), f, a) for f in (False, True) for a in atoms3]          # HN head angle 0
    snd  = [(a, f, p) for a in (F(0), F(1)) for f in (False, True) for p in atoms3]
    A2 = [(nMin((c,)), (c,)) for c in head]
    for c1 in head:
        for c2 in snd:
            A2.append((nMin((c1, c2)), (c1, c2)))
    S2 = [o for o in A2 if complete(o) and depth(o) == 2]
    multi = any(len(o[1]) == 2 for o in S2)
    n, k, _ = ce(2, S2)
    print("  d=2 over complete depth-2 (incl. multi-cell=%s), |S|=%d: CE=%d" % (multi, k, n))
    # drop the carrier condition -> counterexamples return
    Svar = []
    for (_, cs) in [o for o in A2 if nonempty_rec(o) and hn_rec(o) and uniform_depth(o) and depth(o) == 2][:8]:
        Svar += [(1, cs), (2, cs)]
    n, k, _ = ce(2, Svar); print("  drop canonical carrier (vary nd),    |S|=%d: CE=%d  (condition is necessary)" % (k, n))

    # --- common depth (AlignedComplete): per-object Complete is NOT enough ACROSS operands.
    # A shallower B against a deeper A re-fires some,none (the depth-mismatch CE). Pool
    # complete objects of depth 2 AND 3; require depth A = depth B = depth C to fix it.
    leaf = (1, ((F(0), False, None),))
    pool = []
    for f in (False, True):
        pool.append((1, ((F(0), f, leaf),)))                          # depth 2
        pool.append((1, ((F(0), f, (1, ((F(0), False, leaf),))),)))   # depth 3
    pool = [o for o in pool if complete(o)]
    def ce_aligned(dn, S, common):
        m = 0
        for A in S:
            for B in S:
                if common and depth(A) != depth(B): continue
                p = mul(dn, A, B)
                for C in S:
                    if common and depth(A) != depth(C): continue
                    if B != C and mul(dn, A, C) == p: m += 1
        return m
    print("  d=3 mixed-depth Complete pool |S|=%d: Complete-only CE=%d ; +common-depth CE=%d"
          % (len(pool), ce_aligned(3, pool, False), ce_aligned(3, pool, True)))

if __name__ == "__main__":
    main()
