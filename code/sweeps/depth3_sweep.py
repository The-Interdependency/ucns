"""Depth-3 empirical sweep for factor_search_v08.

Convention: depth_of() per ucns_recursive.domains, where:
  None        → depth 0
  flat        → depth 1
  d-leading   → 1 + d

Frozen domain D' is depth ≤ 2 (so flat or depth-1-leading).  This
sweep targets depth = 3 cases (objects with at least one depth-2
payload), which sit one step past D'.

Each case:
  - Build A and B with controlled depth structure.
  - Compute P = A ⊠ B.
  - Try factor_search_v08 with two catalogues:
      (a) default depth-1 oracle catalogue
      (b) tailored catalogue containing A's and B's leading payloads
  - Categorize: SUCCESS / FALSE-NEGATIVE / TIMEOUT / EXCEPTION.
  - Time-bound each attempt at TIMEOUT_S.

The point is to map the failure boundary, not to prove anything.
"""
from __future__ import annotations
import sys, time, signal, traceback
from pathlib import Path
from fractions import Fraction
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from ucns_recursive.canonical import UCNSObject, multiply
from ucns_recursive.factor_search_v08 import factor_search_v08, SEQ_PRIME
from ucns_recursive.domains import generate_payload_catalogue, depth_of

TIMEOUT_S = 20

# ---------- timeout helper ----------

class TimeoutError_(Exception):
    pass

@contextmanager
def time_limit(seconds):
    def handler(signum, frame):
        raise TimeoutError_(f"timeout after {seconds}s")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

# ---------- builders ----------

def flat(angles, faces, n_dec=2):
    """Flat (depth-1) object."""
    a_plus = [(Fraction(a), None) for a in angles]
    return UCNSObject(n_dec, n_dec, a_plus, faces)

def host(angle_payload_pairs, faces, n_dec=2):
    a_plus = [(Fraction(a), p) for a, p in angle_payload_pairs]
    return UCNSObject(n_dec, n_dec, a_plus, faces)

# ---------- canonical building blocks ----------

S2  = flat([0, 1], [0, 0])                               # depth 1, smallest oracle atom
S2b = flat([0, 1], [1, 0])                               # depth 1, alt face
S3  = flat([0, 1, 2], [0, 0, 0])                         # depth 1, length 3

# Depth-2 building blocks (objects whose leading payload is depth-1)
D2_a = host([(0, S2), (1, None)], [0, 0])                # depth 2, leading=S2
D2_b = host([(0, S2b), (1, None)], [0, 0])               # depth 2, leading=S2b
D2_c = host([(0, S2), (1, S2)], [0, 0])                  # depth 2, both payloads non-unit

# ---------- result type ----------

@dataclass
class Case:
    name: str
    A: UCNSObject
    B: UCNSObject
    notes: str = ""
    P: Optional[UCNSObject] = None
    P_depth: int = 0
    P_len: int = 0
    res_default: str = ""
    res_tailored: str = ""
    elapsed_default: float = 0.0
    elapsed_tailored: float = 0.0

# ---------- the sweep ----------

cases: List[Case] = [
    # 1. Smallest possible depth-3 P: one factor depth-3, other unit
    #    (Should always succeed: B=unit short-circuits in multiply.)
    Case("01-trivial-unit-right",
         A=host([(0, D2_a), (1, None)], [0, 0]),
         B=UCNSObject(1, 1, [(Fraction(0), None)], [0]),
         notes="A depth-3, B unit. B=unit handled at multiply level; "
               "factor_search_v08 finds the trivial split."),

    # 2. Symmetric: both factors depth-2 (P will be depth-3)
    Case("02-symmetric-d2xd2",
         A=D2_a, B=D2_a,
         notes="A=B=D2_a.  P=A⊠B should be depth-3.  Symmetric."),

    # 3. Asymmetric depths: depth-2 × depth-1
    Case("03-d2-times-d1",
         A=D2_a, B=S2,
         notes="A depth-2, B depth-1.  P will be depth ≤ 3."),

    # 4. Asymmetric: depth-3 × depth-1
    Case("04-d3-times-d1",
         A=host([(0, D2_a), (1, None)], [0, 0]),
         B=S2,
         notes="A depth-3, B flat depth-1."),

    # 5. Both depth-3
    Case("05-d3-times-d3",
         A=host([(0, D2_a), (1, None)], [0, 0]),
         B=host([(0, D2_a), (1, None)], [0, 0]),
         notes="Both factors depth-3.  Hardest core case."),

    # 6. Depth-2 with non-unit second payload (vs case 2 which has D2_a's structure)
    Case("06-d2c-times-s2",
         A=D2_c, B=S2,
         notes="A=D2_c (both payloads non-unit), B=S2 flat."),

    # 7. Length-3 host at depth 2
    Case("07-len3-host-d2-times-d1",
         A=host([(0, S2), (1, S2b), (2, None)], [0, 0, 0]),
         B=S2,
         notes="A has 3 host cells, depth-2.  B flat.  Multi-cell payload row."),

    # 8. Host length 2 × host length 3
    Case("08-d2-times-len3-flat",
         A=D2_a, B=S3,
         notes="A depth-2 (len 2), B flat (len 3).  P will have |P+|=6."),

    # 9. Distinct payloads at depth-2 (D2_a and D2_b leading)
    Case("09-d3-distinct-leadings",
         A=host([(0, D2_a), (1, None)], [0, 0]),
         B=host([(0, D2_b), (1, None)], [0, 0]),
         notes="A and B have different depth-2 leading payloads."),

    # 10. Depth-3 × depth-2
    Case("10-d3-times-d2",
         A=host([(0, D2_a), (1, None)], [0, 0]),
         B=D2_a,
         notes="Depth-3 × depth-2 mixed."),

    # 11. Depth-3 with BOTH outermost cells non-unit at depth-2
    Case("11-d3-both-cells-d2",
         A=host([(0, D2_a), (1, D2_b)], [0, 0]),
         B=S2,
         notes="A depth-3, both outermost payloads depth-2 (different)."),

    # 12. Length-3 host at depth-3
    Case("12-len3-d3-times-d1",
         A=host([(0, D2_a), (1, S2), (2, None)], [0, 0, 0]),
         B=S2,
         notes="A depth-3 length-3 mix of d2 and d1 payloads."),

    # 13. Depth-3 × depth-3, length-3 hosts → |P+|=9
    Case("13-d3xlen3-times-d3xlen3",
         A=host([(0, D2_a), (1, S2), (2, None)], [0, 0, 0]),
         B=host([(0, S2), (1, None), (2, None)], [0, 0, 0]),
         notes="Wider hosts, mixed depths.  |P+|=9; tests scaling."),

    # 14. Heavy outermost: depth-3 with D2_c (both payloads non-unit) leading
    Case("14-d3-with-d2c-leading",
         A=host([(0, D2_c), (1, None)], [0, 0]),
         B=S2,
         notes="A's leading payload D2_c has both inner cells non-unit."),

    # 15. Worst-known shape: depth-4 (per package convention) outer factors
    Case("15-d4-times-d1",
         A=host([(0, host([(0, D2_a), (1, None)], [0, 0])), (1, None)], [0, 0]),
         B=S2,
         notes="A depth 4 (one step further past D').  Probe deeper."),

    # 16. Adversarial: A's non-leading payload D2_b never appears in P alone
    #     (it only appears composed with B's payloads).  Tests whether
    #     "leading-only + P-payloads" catalogue is sufficient.
    Case("16-adversarial-non-leading",
         A=host([(0, D2_a), (1, D2_b)], [0, 0]),
         B=host([(0, S2), (1, S2b)], [0, 0]),
         notes="A's second-cell payload D2_b is not equal to any P_payload "
               "directly — only to (D2_b ⊠ S2) and (D2_b ⊠ S2b).  Tests "
               "whether the search truly recovers atoms not visible in P."),
]

# ---------- run ----------

def categorize(label, P, catalogue, true_A=None, true_B=None):
    t0 = time.time()
    try:
        with time_limit(TIMEOUT_S):
            res = factor_search_v08(P, catalogue=catalogue)
        elapsed = time.time() - t0
        if res == SEQ_PRIME:
            return ("FALSE-NEGATIVE", elapsed)
        A_rec, B_rec = res
        if true_A is not None and true_B is not None:
            if A_rec == true_A and B_rec == true_B:
                return ("SUCCESS", elapsed)
            else:
                return ("ALT-FACTOR", elapsed)
        return ("SUCCESS", elapsed)
    except TimeoutError_:
        return (f"TIMEOUT(>{TIMEOUT_S}s)", TIMEOUT_S)
    except Exception as e:
        return (f"EXCEPTION({type(e).__name__})", time.time() - t0)

def _gather_payloads(obj, acc=None):
    """Collect every non-None payload appearing anywhere in obj (recursively)."""
    if acc is None: acc = []
    if obj is None: return acc
    for _, p in obj.A_plus:
        if p is not None and p not in acc:
            acc.append(p)
            _gather_payloads(p, acc)
    return acc

default_cat = generate_payload_catalogue()
print(f"Default catalogue size: {len(default_cat)}\n")

print(f"{'#':<3}{'name':<30}{'P_d':<5}{'|P+|':<6}"
      f"{'default':<24}{'narrow-tailored':<24}{'broad-tailored':<24}")
print("-" * 132)

for c in cases:
    c.P = multiply(c.A, c.B)
    c.P_depth = depth_of(c.P)
    c.P_len = len(c.P.A_plus)

    # Narrow tailored: default + leading payloads + payloads visible in P
    narrow_cat = list(default_cat)
    for x in [c.A.A_plus[0][1], c.B.A_plus[0][1]]:
        if x is not None and x not in narrow_cat:
            narrow_cat.append(x)
    for _, p in c.P.A_plus:
        if p is not None and p not in narrow_cat:
            narrow_cat.append(p)

    # Broad tailored: narrow + every payload anywhere in A and B (recursively)
    broad_cat = list(narrow_cat)
    for x in _gather_payloads(c.A) + _gather_payloads(c.B):
        if x not in broad_cat:
            broad_cat.append(x)

    c.res_default,  c.elapsed_default  = categorize("default",  c.P, default_cat,  c.A, c.B)
    c.res_tailored, c.elapsed_tailored = categorize("narrow",   c.P, narrow_cat,   c.A, c.B)
    res_broad, t_broad                 = categorize("broad",    c.P, broad_cat,    c.A, c.B)

    print(f"{c.name[:3]:<3}{c.name[3:]:<30}{c.P_depth:<5}{c.P_len:<6}"
          f"{c.res_default:<16}{c.elapsed_default:5.2f}s   "
          f"{c.res_tailored:<16}{c.elapsed_tailored:5.2f}s   "
          f"{res_broad:<16}{t_broad:5.2f}s")

# ---------- summary ----------

print()
print("=" * 60)
print("Summary")
print("=" * 60)
def tally(field):
    counts = {}
    for c in cases:
        v = getattr(c, field).split("(")[0]
        counts[v] = counts.get(v, 0) + 1
    return counts

print(f"Default catalogue (depth-1):   {tally('res_default')}")
print(f"Narrow-tailored catalogue:     {tally('res_tailored')}")
print(f"\n(Broad-tailored results in main table.)")
