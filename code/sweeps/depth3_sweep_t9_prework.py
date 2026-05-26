"""Theorem 9 pre-work: augmented depth-3 sweep with full instrumentation.

Goal: verify the asymmetric-factorization conjecture by recording, per case:
  - depth(A), depth(B), depth(P) — confirms which cases are genuinely depth-3
  - max payload depth of A and B — determines minimum catalogue depth needed
  - SUCCESS/FAIL under three catalogues:
      (i)  default depth-1 (Lemma 7's catalogue)
      (ii) depth-2 oracle catalogue from a tight basis containing all
           relevant atoms (Theorem 9's catalogue)
      (iii) broad-tailored (kitchen-sink, includes all payloads
            reachable from A and B)
  - cross-reference: cases that succeed under (ii) but fail under (i)
    are Theorem 9's territory; cases that succeed under (i) are
    Lemma 7's territory.
"""
from __future__ import annotations
import sys, time, signal
from pathlib import Path
from fractions import Fraction
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ucns_recursive.canonical import UCNSObject, multiply
from ucns_recursive.factor_search_v08 import factor_search_v08, SEQ_PRIME
from ucns_recursive.domains import generate_payload_catalogue, depth_of
from ucns_recursive.catalogue import build_catalogue_d2_oracle

TIMEOUT_S = 8

class TimeoutError_(Exception): pass

@contextmanager
def time_limit(seconds):
    def handler(signum, frame): raise TimeoutError_(f"timeout after {seconds}s")
    signal.signal(signal.SIGALRM, handler); signal.alarm(seconds)
    try: yield
    finally: signal.alarm(0)

# Mirror the sweep's building blocks
def flat(angles, faces, n_dec=2):
    return UCNSObject(n_dec, n_dec, [(Fraction(a), None) for a in angles], faces)

def host(angle_payload_pairs, faces, n_dec=2):
    return UCNSObject(n_dec, n_dec, [(Fraction(a), p) for a, p in angle_payload_pairs], faces)

S2  = flat([0, 1], [0, 0])
S2b = flat([0, 1], [1, 0])
S3  = flat([0, 1, 2], [0, 0, 0])
D2_a = host([(0, S2), (1, None)], [0, 0])
D2_b = host([(0, S2b), (1, None)], [0, 0])
D2_c = host([(0, S2), (1, S2)], [0, 0])

@dataclass
class Case:
    name: str
    A: UCNSObject
    B: UCNSObject
    A_depth: int = 0
    B_depth: int = 0
    P: Optional[UCNSObject] = None
    P_depth: int = 0
    P_len: int = 0
    A_payload_max_depth: int = 0
    B_payload_max_depth: int = 0
    res_d1: str = ""
    res_d2: str = ""
    res_broad: str = ""

def max_payload_depth(obj):
    if obj is None: return -1
    return max((depth_of(p) for _, p in obj.A_plus), default=-1)

cases = [
    Case("01-trivial-unit-right", host([(0, D2_a), (1, None)], [0, 0]), UCNSObject(1, 1, [(Fraction(0), None)], [0])),
    Case("02-symmetric-d2xd2", D2_a, D2_a),
    Case("03-d2-times-d1", D2_a, S2),
    Case("04-d3-times-d1", host([(0, D2_a), (1, None)], [0, 0]), S2),
    Case("05-d3-times-d3", host([(0, D2_a), (1, None)], [0, 0]), host([(0, D2_a), (1, None)], [0, 0])),
    Case("06-d2c-times-s2", D2_c, S2),
    Case("07-len3-host-d2-times-d1", host([(0, S2), (1, S2b), (2, None)], [0, 0, 0]), S2),
    Case("08-d2-times-len3-flat", D2_a, S3),
    Case("09-d3-distinct-leadings", host([(0, D2_a), (1, None)], [0, 0]), host([(0, D2_b), (1, None)], [0, 0])),
    Case("10-d3-times-d2", host([(0, D2_a), (1, None)], [0, 0]), D2_a),
    Case("11-d3-both-cells-d2", host([(0, D2_a), (1, D2_b)], [0, 0]), S2),
    Case("12-len3-d3-times-d1", host([(0, D2_a), (1, S2), (2, None)], [0, 0, 0]), S2),
    Case("13-d3xlen3-times-d3xlen3", host([(0, D2_a), (1, S2), (2, None)], [0, 0, 0]), host([(0, S2), (1, None), (2, None)], [0, 0, 0])),
    Case("14-d3-with-d2c-leading", host([(0, D2_c), (1, None)], [0, 0]), S2),
    Case("15-d4-times-d1", host([(0, host([(0, D2_a), (1, None)], [0, 0])), (1, None)], [0, 0]), S2),
    Case("16-adversarial-non-leading", host([(0, D2_a), (1, D2_b)], [0, 0]), host([(0, S2), (1, S2b)], [0, 0])),
]

def categorize(P, catalogue, true_A, true_B):
    try:
        with time_limit(TIMEOUT_S):
            res = factor_search_v08(P, catalogue=catalogue)
        if res == SEQ_PRIME: return "FALSE-NEG"
        A_rec, B_rec = res
        if A_rec == true_A and B_rec == true_B: return "SUCCESS"
        return "ALT-FACTOR"
    except TimeoutError_: return "TIMEOUT"
    except Exception as e: return f"EXC({type(e).__name__})"

def gather(obj, acc=None):
    if acc is None: acc = []
    if obj is None: return acc
    for _, p in obj.A_plus:
        if p is not None and p not in acc:
            acc.append(p); gather(p, acc)
    return acc

# Three catalogues
cat_d1 = generate_payload_catalogue()
# Build d2 catalogue from a minimal basis (S2 only — the most-used atom)
tight_d1_basis = [None, S2]
cat_d2_partial = build_catalogue_d2_oracle(payload_basis=tight_d1_basis)
cat_d2 = list(cat_d1) + cat_d2_partial

print(f"Catalogue sizes: d1={len(cat_d1)}, d2={len(cat_d2)}")
print()

print(f"{'#':<4}{'name':<28}{'dA':<3}{'dB':<3}{'dP':<3}{'|P+|':<5}"
      f"{'pA':<3}{'pB':<3}{'d1':<11}{'d2':<11}{'broad':<11}")
print("-" * 120)

for c in cases:
    c.A_depth = depth_of(c.A)
    c.B_depth = depth_of(c.B)
    c.P = multiply(c.A, c.B)
    c.P_depth = depth_of(c.P)
    c.P_len = len(c.P.A_plus)
    c.A_payload_max_depth = max_payload_depth(c.A)
    c.B_payload_max_depth = max_payload_depth(c.B)

    # broad: kitchen-sink including all payloads of A and B
    broad = list(cat_d2)
    for x in gather(c.A) + gather(c.B):
        if x not in broad: broad.append(x)

    c.res_d1 = categorize(c.P, cat_d1, c.A, c.B)
    c.res_d2 = categorize(c.P, cat_d2, c.A, c.B)
    c.res_broad = categorize(c.P, broad, c.A, c.B)

    print(f"{c.name[:3]:<4}{c.name[3:]:<28}{c.A_depth:<3}{c.B_depth:<3}{c.P_depth:<3}{c.P_len:<5}"
          f"{c.A_payload_max_depth:<3}{c.B_payload_max_depth:<3}"
          f"{c.res_d1:<11}{c.res_d2:<11}{c.res_broad:<11}")
    sys.stdout.flush()

print()
print("=" * 70)
print("Cross-reference by territory")
print("=" * 70)

def tally(cs, field): 
    counts = {}
    for c in cs:
        v = getattr(c, field)
        counts[v] = counts.get(v, 0) + 1
    return counts

# Symmetric (d_A == d_B): Lemma 7 territory (depth lift doesn't happen)
sym = [c for c in cases if c.A_depth == c.B_depth]
asym = [c for c in cases if c.A_depth != c.B_depth]
print(f"\nSymmetric (dA==dB), n={len(sym)}:")
print(f"  d1 catalogue:  {tally(sym, 'res_d1')}")
print(f"  d2 catalogue:  {tally(sym, 'res_d2')}")
print(f"  broad:         {tally(sym, 'res_broad')}")

print(f"\nAsymmetric (dA!=dB), n={len(asym)}:")
print(f"  d1 catalogue:  {tally(asym, 'res_d1')}")
print(f"  d2 catalogue:  {tally(asym, 'res_d2')}")
print(f"  broad:         {tally(asym, 'res_broad')}")

# Theorem 9 territory: P depth = 3, asymmetric, max factor depth >= 3
t9 = [c for c in cases if c.P_depth == 3 and (c.A_depth >= 3 or c.B_depth >= 3) and c.A_depth != c.B_depth]
print(f"\nTheorem 9 candidates (asymmetric, dP=3, at least one factor d>=3), n={len(t9)}:")
for c in t9:
    print(f"  {c.name}: d1={c.res_d1}, d2={c.res_d2}, broad={c.res_broad}")

# Cases where d2 catalogue resolves something d1 can't — direct Theorem 9 evidence
lifted_by_d2 = [c for c in cases if c.res_d1 != "SUCCESS" and c.res_d2 == "SUCCESS"]
print(f"\nResolved by d2 catalogue but not d1 (direct T9 evidence), n={len(lifted_by_d2)}:")
for c in lifted_by_d2:
    print(f"  {c.name}: dA={c.A_depth} dB={c.B_depth} dP={c.P_depth}")
