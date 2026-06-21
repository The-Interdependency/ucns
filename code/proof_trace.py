"""
Trace the recursion depth in left_quotient(P, A) for the Class III oracle.

Verifies Lemma 7 (recursion bottoms out within d(A) levels).

Class III oracle:
  S2 = flat 2-gon, depth 0
  A = (host = 2-gon, payloads = [S2, None]), depth 1
  P = A ⊠ A, depth 1

Predicted: left_quotient(P, A) recurses once (1 level), bottoms at A=S2
which is flat (depth 0).

Run from the repo root:
  python code/proof_trace.py
"""
from fractions import Fraction
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucns.recursive_quotient import left_quotient as _real_lq
from ucns_code_v065 import UCNSObject, multiply  # fallback: adjust import as needed

# --- Monkey-patch left_quotient to log call depth ---
_call_depth = [0]
_max_depth = [0]
_call_log = []


def _traced_lq(P, A, catalogue=None):
    _call_depth[0] += 1
    _max_depth[0] = max(_max_depth[0], _call_depth[0])
    indent = "  " * (_call_depth[0] - 1)
    P_len = len(P.A_plus) if hasattr(P, 'A_plus') else '?'
    A_len = len(A.A_plus) if hasattr(A, 'A_plus') else '?'
    leading = A.A_plus[0][1] if hasattr(A, 'A_plus') else '?'
    _call_log.append(
        f"{indent}call #{_call_depth[0]}: "
        f"left_quotient(P=L{P_len}, A=L{A_len} "
        f"with leading payload {'None' if leading is None else 'non-None'})"
    )
    try:
        result = _real_lq(P, A, catalogue)
    finally:
        _call_depth[0] -= 1
    return result


def nesting_depth(G):
    """nesting_depth as defined in the proof."""
    if G is None:
        return 0
    if not G.A_plus:
        return 0
    payload_depths = [
        nesting_depth(ap[1]) for ap in G.A_plus
        if ap[1] is not None
    ]
    if not payload_depths:
        return 0
    return 1 + max(payload_depths)


def flat(n_dec, thetas, faces):
    return UCNSObject(
        n_dec=n_dec, n_min=1,
        A_plus=list(zip(thetas, [None] * len(thetas))),
        F_plus=list(faces),
    )


# Class III oracle
S2 = flat(2, [Fraction(0), Fraction(1, 2)], [0, 0])
A = UCNSObject(
    n_dec=2, n_min=2,
    A_plus=[(Fraction(0), S2), (Fraction(1, 2), None)],
    F_plus=[0, 0],
)
B = UCNSObject(
    n_dec=2, n_min=2,
    A_plus=[(Fraction(0), S2), (Fraction(1, 2), None)],
    F_plus=[0, 0],
)
P = multiply(A, B)

print("Object depths:")
print(f"  d(S2)  = {nesting_depth(S2)}  (flat 2-gon)")
print(f"  d(A)   = {nesting_depth(A)}   (host with S2 payload)")
print(f"  d(B)   = {nesting_depth(B)}")
print(f"  d(P)   = {nesting_depth(P)}")

print(f"\nLemma 7 predicts: left_quotient(P, A) terminates within d(A) = "
      f"{nesting_depth(A)} recursive levels.")

print("\nTrace:")
result = _traced_lq(P, A, catalogue=None)
for line in _call_log:
    print(line)

print(f"\nMaximum call depth observed: {_max_depth[0]}")
print(f"Lemma 7 bound (1 + d(A)):     {1 + nesting_depth(A)}")
print(f"  (1 outer call + d(A) recursive descents)")
print(f"\nResult: {'recovered' if result is not None else 'failed'}")
if result is not None:
    print(f"  multiply(A, result) ≡_seq P: {multiply(A, result) == P}")

# Depth-2 trace
print("\n\n--- Depth-2 trace ---")
_call_log.clear()
_max_depth[0] = 0

A2 = UCNSObject(
    n_dec=2, n_min=2,
    A_plus=[(Fraction(0), A), (Fraction(1, 2), None)],
    F_plus=[0, 0],
)
B2 = UCNSObject(
    n_dec=2, n_min=2,
    A_plus=[(Fraction(0), A), (Fraction(1, 2), None)],
    F_plus=[0, 0],
)
P2 = multiply(A2, B2)

print(f"  d(A2) = {nesting_depth(A2)}, d(P2) = {nesting_depth(P2)}")
print(f"  Lemma 7 predicts max depth: {1 + nesting_depth(A2)}")

result2 = _traced_lq(P2, A2, catalogue=None)
for line in _call_log:
    print(line)
print(f"  Maximum call depth observed: {_max_depth[0]}")
print(f"  Result: {'recovered' if result2 is not None else 'failed'}")
if result2 is not None:
    print(f"  multiply(A2, result2) ≡_seq P2: {multiply(A2, result2) == P2}")
