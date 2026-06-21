#!/usr/bin/env python3
# Cancellativity Step-1 counterexample search (formalization track).
#
# Faithful port of `multiplyFuel`, `amod4`, `depth`, `HostNormalized` from
# formal/Ucns/Core.lean. Read-only research artifact: it neither imports nor
# modifies the engine. Decides whether `multiply_left_cancellative` holds as
# stated and, if not, which added hypotheses restore it.
#
# Run:  python3 formal/cancellativity_step1_search.py
#
# Object model:  o = (nd:int, cells: tuple of (angle:Fraction, face:bool, payload:o|None))
import math
from fractions import Fraction as F

# --- exact ports of the Lean definitions -----------------------------------
def amod4(x):                       # amod a 4 = a - 4*floor(a/4)
    return x - 4 * math.floor(x / 4)

def mul(d, a, b):                   # multiplyFuel : fuel 0 -> LEFT arg
    if d == 0:
        return a
    nda, csA = a
    ndb, csB = b
    b0 = csB[0][0] if csB else F(0)         # β0 = right operand's first-cell angle
    nc = []
    for (aa, af, ap) in csA:
        for (ba, bf, bp) in csB:
            ang = amod4(aa + (ba - b0))
            fc = af ^ bf
            if   ap is not None and bp is not None: pay = mul(d - 1, ap, bp)   # some,some
            elif ap is not None:                    pay = ap                   # some,none
            elif bp is not None:                    pay = bp                   # none,some
            else:                                   pay = None                # none,none
            nc.append((ang, fc, pay))
    return (math.lcm(nda, ndb), tuple(nc))

def depth(o):                       # Lean depth = 1 + max payload depth  (FLAT OBJECT = 1)
    _, cs = o
    m = 0
    for (_, _, p) in cs:
        m = max(m, 0 if p is None else depth(p))
    return 1 + m

# --- candidate hypotheses ---------------------------------------------------
def hn_top(o):                      # Core.lean HostNormalized: ONLY the head cell angle == 0
    _, cs = o
    return (not cs) or cs[0][0] == F(0)

def hn_rec(o):                      # recursive HostNormalized: every object + all payloads
    _, cs = o
    if cs and cs[0][0] != F(0):
        return False
    return all(p is None or hn_rec(p) for (_, _, p) in cs)

def all_present(o):                 # AllPayloadsPresent: no `none` at any multiplied cell;
    _, cs = o                       # recursion bottoms at atoms (leaves whose cells are all none)
    for (_, _, p) in cs:
        if p is None:
            return False
        _, pcs = p
        if any(pp is not None for (_, _, pp) in pcs) and not all_present(p):
            return False
    return True

def rep(o):
    _, cs = o
    return "[%s]" % ",".join("(%s,%s,%s)" % (c[0], 'T' if c[1] else 'F',
                             '.' if c[2] is None else rep(c[2])) for c in cs)

def first_ce(d, objs, pred):
    S = [o for o in objs if pred(o) and depth(o) <= d]
    n = 0; witness = None
    for A in S:
        for B in S:
            p = mul(d, A, B)
            for C in S:
                if B != C and mul(d, A, C) == p:
                    n += 1
                    if witness is None: witness = (A, B, C)
    return n, witness, len(S)

# --- universes --------------------------------------------------------------
LEAVES = [(1, ((a, f, None),)) for a in (F(0), F(1)) for f in (False, True)]
FLAT   = LEAVES[:]                                          # depth-1 objects
NESTED = [(1, ((a, f, p),)) for a in (F(0), F(1)) for f in (False, True) for p in LEAVES]  # depth-2

def main():
    print("=== Cancellativity Step 1: counterexample search (Core.lean port) ===\n")

    # (1) bare theorem
    n, w, _ = first_ce(1, FLAT, lambda o: True)
    print("[1] BARE theorem, d=1 (only depth B,C <= d):  FALSE" if n else "[1] bare: no CE")
    if w:
        A, B, C = w
        print("    witness  A=%s  B=%s  C=%s" % (rep(A), rep(B), rep(C)))
        print("    mul(1,A,B)=%s == mul(1,A,C)=%s ,  B!=C" % (rep(mul(1, A, B)), rep(mul(1, A, C))))
        print("    cause: β0 = right operand's head angle is subtracted -> host angle gauge collapses.\n")

    # (2) top-only HostNormalized (as in Core.lean) + AllPayloadsPresent  -> INSUFFICIENT
    for d in (2, 3):
        n, w, k = first_ce(d, NESTED, lambda o: hn_top(o) and all_present(o))
        print("[2] d=%d  top-only HostNormalized + AllPayloadsPresent (|S|=%d):  CE=%d" % (d, k, n))
        if w:
            A, B, C = w
            print("    witness  A=%s  B=%s  C=%s  (payload head angles differ; payload-level β0 collapse)" %
                  (rep(A), rep(B), rep(C)))

    # (3) recursive HostNormalized + AllPayloadsPresent  -> no CE
    for d in (2, 3):
        n, _, k = first_ce(d, NESTED, lambda o: hn_rec(o) and all_present(o))
        print("[3] d=%d  RECURSIVE HostNormalized + AllPayloadsPresent (|S|=%d):  CE=%d" % (d, k, n))

    # (4) depth-A unconstrained (deep A) under the recursive hypotheses
    deepA = (1, ((F(0), False, (1, ((F(0), False, LEAVES[0]), (F(1), True, LEAVES[1])))),))
    BC = [o for o in NESTED if hn_rec(o) and all_present(o) and depth(o) <= 2]
    n = 0
    for B in BC:
        p = mul(2, deepA, B)
        for C in BC:
            if B != C and mul(2, deepA, C) == p:
                n += 1
    print("[4] d=2  deep A (depth %d, recursive-HN, all-present), B,C recursive-HN+present, depth<=2:  CE=%d"
          % (depth(deepA), n))
    print("    -> no depth-A hypothesis needed; existing depth B,C <= d suffices.")

if __name__ == "__main__":
    main()
