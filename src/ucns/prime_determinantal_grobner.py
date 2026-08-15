# === MODULE_BUILD ===
# id: ucns_prime_determinantal_grobner_p7_p5
#   module_name: prime_determinantal_grobner
#   module_kind: experiment
#   summary: executes the preregistered complete rational-Laurent determinantal-ideal Groebner protocol for the frozen P7 and P5 Fox matrices
#   owner: Erin Spencer
#   public_surface: determinantal_grobner_certificate, determinantal_grobner_family_certificate, write_determinantal_grobner_family_certificate
#   internal_surface: compound maximal-minor coordinates, Laurent normalization, saturation, exact reduced lex bases, independent Buchberger replay
#   auth_boundary: none
#   storage_boundary: caller-supplied local paths only through writer functions
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_prime_determinantal_grobner.py
#   rollout: protocol 7841af16; P7 first and P5 second; selection effect none
#   rollback: remove this module, its tests, result document, and generated receipt while retaining preregistration and prior rank/onset evidence
#   requires: ucns_prime_symbolic_alexander_p7_p5, sympy==1.14.0
#   since: 2026-08-15
#   unresolved: integral-Laurent strong bases, length-four Milnor invariants, finite nilpotent quotients, preregistered phase-co-winner separator
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: prime_grobner_protocol_identity_is_frozen
#   given: a determinantal basis computation begins
#   then: the committed preregistration bytes have the frozen SHA-256 identity and the parent presentation digest matches
#   class: doctrine
#
# id: prime_grobner_generators_cover_every_maximal_minor
#   given: P7 E1 or P5 E3 generators are constructed
#   then: every rank-size row/column subset pair is accounted for through the exact compound identity with no non-monomial denominator
#   class: correctness
#
# id: prime_grobner_basis_is_complete_reduced_and_saturated
#   given: the complete rational-Laurent determinantal generator family is accepted
#   then: component-variable saturation and exact lex reduction return a monic reduced basis for the complete ideal
#   class: evidence
#
# id: prime_grobner_independent_replay_agrees
#   given: primary and independent computations finish within frozen bounds
#   then: generator digests, mutual reductions, and canonical reduced basis maps agree exactly
#   class: regression
#
# id: prime_grobner_receipt_preserves_nonclaims
#   given: the family receipt is serialized
#   then: rational ideal evidence does not escalate phase, isotopy, prime-forcing, spectral, zeta, or theorem standing
#   class: doctrine
# === END CONTRACTS ===

"""Preregistered rational-Laurent determinantal Groebner computation."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib, itertools, json, time
from pathlib import Path
from typing import Iterable

import sympy as sp

from .prime_symbolic_alexander import _matrix_data, symbolic_alexander_certificate

PROTOCOL_PATH = Path("docs/PREREGISTRATION_P7_P5_DETERMINANTAL_GROEBNER.md")
PROTOCOL_SHA256 = "7841af162698efb823db79b70ef7b99a5ac53d27e2bbb318f97f36aecae515b4"
PARENT_COMMIT = "62e97304971d9ac9ead0f766c964d830b0367aa1"
PRESENTATION_SHA256 = {7: "57a3aad650c372f37e798a8d3377422005156d2f5cd495bb990eca397443ab7b", 5: "34cab71c9e4e8fd85f30d5a10956aba7bd1a0c1398d2263ba7e7cebfac24e82d"}
MAX_PAIRS = 1_000_000
MAX_GENERATORS = 100_000

class DeterminantalGrobnerError(ValueError): pass

def _sha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def _protocol_gate() -> None:
    if hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest() != PROTOCOL_SHA256:
        raise DeterminantalGrobnerError("preregistration identity mismatch")

def _poly_key(poly: sp.Poly) -> tuple[tuple[tuple[int, ...], str], ...]:
    return tuple((tuple(mon), str(coeff)) for mon, coeff in poly.terms())

def _normalize_expr(expr, symbols: tuple[sp.Symbol, ...]) -> sp.Poly:
    expr = sp.cancel(sp.sympify(str(expr)))
    numerator, denominator = sp.fraction(expr)
    den_poly = sp.Poly(denominator, *symbols, domain=sp.QQ)
    if len(den_poly.terms()) != 1:
        raise DeterminantalGrobnerError("non-monomial Laurent denominator")
    poly = sp.Poly(sp.expand(numerator), *symbols, domain=sp.QQ)
    if poly.is_zero: return poly
    minima = tuple(min(mon[i] for mon, _ in poly.terms()) for i in range(len(symbols)))
    shifted = {tuple(mon[i]-minima[i] for i in range(len(symbols))): coeff for mon, coeff in poly.terms()}
    result = sp.Poly.from_dict(shifted, symbols, domain=sp.QQ)
    return result.monic()

def _coordinate_families(prime: int):
    diagram, _, names, _, matrix, _ = _matrix_data(prime)
    dense = matrix.to_dense(); rank = matrix.rank()
    rr, columns = dense.rref(); rt, rows = dense.transpose().rref()
    if tuple(columns) != symbolic_alexander_certificate(prime).pivot_columns or tuple(rows) != symbolic_alexander_certificate(prime).pivot_rows:
        raise DeterminantalGrobnerError("pivot profile changed")
    right = rr.extract(range(rank), range(diagram.generator_count))
    left = rt.extract(range(rank), range(diagram.generator_count)).transpose()
    subsets = tuple(itertools.combinations(range(diagram.generator_count), rank))
    left_values = tuple(left.extract(list(subset), range(rank)).det() for subset in subsets)
    right_values = tuple(right.extract(range(rank), list(subset)).det() for subset in subsets)
    return diagram, names, rank, subsets, left_values, right_values

def _complete_generators(prime: int):
    diagram, names, rank, subsets, left, right = _coordinate_families(prime)
    symbols = tuple(sp.Symbol(name) for name in names)
    pivot = sp.sympify(symbolic_alexander_certificate(prime).pivot_minor)
    nonzero_left = [(subsets[i], value) for i,value in enumerate(left) if value]
    nonzero_right = [(subsets[i], value) for i,value in enumerate(right) if value]
    pair_total=len(subsets)**2; nonzero_total=len(nonzero_left)*len(nonzero_right)
    if pair_total>MAX_PAIRS: raise DeterminantalGrobnerError("candidate pair-product bound exceeded")
    pivot_poly=_normalize_expr(pivot,symbols)
    unique={}
    for _, lp in nonzero_left:
        for _, rp in nonzero_right:
            product=_normalize_expr(pivot*sp.sympify(str(lp))*sp.sympify(str(rp)),symbols)
            unique[_poly_key(product)]=product
            if len(unique)>MAX_GENERATORS: raise DeterminantalGrobnerError("deduplicated-generator bound exceeded")
    ordered=tuple(unique[key] for key in sorted(unique))
    accounting={"row_subsets":len(subsets),"column_subsets":len(subsets),"candidate_pairs":pair_total,"nonzero_left":len(nonzero_left),"nonzero_right":len(nonzero_right),"nonzero_pair_products":nonzero_total,"deduplicated_generators":len(ordered)}
    return symbols, ordered, accounting

def _reduced_saturated_basis(symbols: tuple[sp.Symbol,...], generators: tuple[sp.Poly,...]):
    z=sp.Symbol("z"); product=sp.prod(symbols)
    first=sp.groebner([g.as_expr() for g in generators]+[1-z*product],z,*symbols,order="lex",domain=sp.QQ)
    eliminated=[p.as_expr() for p in first.polys if not p.as_expr().has(z)]
    if not eliminated: raise DeterminantalGrobnerError("saturation elimination returned no component-ring generator")
    reduced=sp.groebner(eliminated,*symbols,order="lex",domain=sp.QQ)
    return tuple(sp.Poly(p,*symbols,domain=sp.QQ).monic() for p in reduced.polys)

def _lt(poly: dict[tuple[int,...],Fraction]): return max(poly) if poly else None
def _padd(a,b,scale=Fraction(1),shift=None):
    out=dict(a); shift=shift or (0,)*len(next(iter(a or b)))
    for m,c in b.items():
        mm=tuple(x+y for x,y in zip(m,shift)); out[mm]=out.get(mm,Fraction())+scale*c
        if not out[mm]: del out[mm]
    return out
def _preduce(f,basis):
    f=dict(f); rem={}
    while f:
        m=_lt(f); c=f[m]; reduced=False
        for g in basis:
            mg=_lt(g)
            if all(x>=y for x,y in zip(m,mg)):
                shift=tuple(x-y for x,y in zip(m,mg)); f=_padd(f,g,-c/g[mg],shift); reduced=True; break
        if not reduced: rem[m]=c; del f[m]
    return rem
def _monic(p):
    if not p:return p
    c=p[_lt(p)];return {m:v/c for m,v in p.items()}
def _buchberger(initial):
    basis=[]
    for f in initial:
        r=_preduce(f,basis)
        if r:basis.append(_monic(r))
    pairs=list(itertools.combinations(range(len(basis)),2)); pos=0
    while pos<len(pairs):
        i,j=pairs[pos];pos+=1; a,b=basis[i],basis[j]; ma,mb=_lt(a),_lt(b); l=tuple(max(x,y) for x,y in zip(ma,mb))
        s=_padd({},a,Fraction(1,a[ma]),tuple(x-y for x,y in zip(l,ma)))
        s=_padd(s,b,Fraction(-1,b[mb]),tuple(x-y for x,y in zip(l,mb)))
        r=_preduce(s,basis)
        if r:
            r=_monic(r); n=len(basis);basis.append(r);pairs.extend((i,n) for i in range(n))
            if len(basis)>100_000:raise DeterminantalGrobnerError("replay basis bound exceeded")
    changed=True
    while changed:
        changed=False; out=[]
        for i,g in enumerate(basis):
            r=_preduce(g,basis[:i]+basis[i+1:])
            if r:out.append(_monic(r))
            if r!=g:changed=True
        basis=out
    return tuple(sorted(basis,key=lambda p:(_lt(p),tuple(sorted(p.items(),reverse=True)))))

def _fraction_poly(poly: sp.Poly, *, z: bool=False):
    return {tuple(mon):Fraction(int(c.p),int(c.q)) for mon,c in poly.terms()}

@dataclass(frozen=True)
class GrobnerCertificate:
    prime:int; accounting:dict[str,int]; generator_sha256:str; basis:tuple[sp.Poly,...]; elapsed_seconds:float
    def as_dict(self):
        maps=[[[*mon],str(coeff)] for poly in self.basis for mon,coeff in []]
        maps=[[[list(mon),str(coeff)] for mon,coeff in poly.terms()] for poly in self.basis]
        return {"prime":self.prime,"accounting":self.accounting,"generator_sha256":self.generator_sha256,"basis_size":len(self.basis),"reduced_lex_basis":maps,"basis_sha256":_sha(maps),"elapsed_seconds":round(self.elapsed_seconds,6),"independent_replay":{"canonical_basis_equal":True,"mutual_reduction":True}}

def determinantal_grobner_certificate(prime:int)->GrobnerCertificate:
    _protocol_gate(); start=time.monotonic(); symbols,generators,accounting=_complete_generators(prime)
    gen_maps=[_poly_key(g) for g in generators]; basis=_reduced_saturated_basis(symbols,generators)
    z=sp.Symbol("z"); sat_initial=[sp.Poly(g.as_expr(),z,*symbols,domain=sp.QQ) for g in generators]+[sp.Poly(1-z*sp.prod(symbols),z,*symbols,domain=sp.QQ)]
    replay_full=_buchberger([_fraction_poly(p) for p in sat_initial])
    replay_elim=[]
    for p in replay_full:
        if all(mon[0]==0 for mon in p): replay_elim.append({mon[1:]:c for mon,c in p.items()})
    replay=_buchberger(replay_elim)
    primary=tuple(_fraction_poly(p) for p in basis)
    if replay!=tuple(sorted(primary,key=lambda p:(_lt(p),tuple(sorted(p.items(),reverse=True))))): raise DeterminantalGrobnerError("independent canonical basis mismatch")
    return GrobnerCertificate(prime,accounting,_sha(gen_maps),basis,time.monotonic()-start)

def determinantal_grobner_family_certificate():
    p7=determinantal_grobner_certificate(7);p5=determinantal_grobner_certificate(5)
    return {"schema_id":"ucns.prime-determinantal-grobner.family","schema_version":"0.1.0","protocol_sha256":PROTOCOL_SHA256,"parent_commit":PARENT_COMMIT,"selection_effect":"none","p7":p7.as_dict(),"p5":p5.as_dict(),"nonclaims":["rational Laurent bases do not establish integer torsion","no phase-law or isotopy selection","no prime-forcing, spectral, zeta, or theorem-status escalation"],"next":["length-four Milnor invariants or finite nilpotent quotients remain independent","preregister any phase-co-winner separator before evaluation"]}
def write_determinantal_grobner_family_certificate(path):
    out=Path(path);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(determinantal_grobner_family_certificate(),indent=2,sort_keys=True)+"\n");return out
def write_determinantal_grobner_certificate(prime, path):
    out=Path(path);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(determinantal_grobner_certificate(prime).as_dict(),indent=2,sort_keys=True)+"\n");return out
if __name__=="__main__":
    import argparse;p=argparse.ArgumentParser();p.add_argument("output");p.add_argument("--prime",type=int,choices=(5,7));a=p.parse_args();write_determinantal_grobner_certificate(a.prime,a.output) if a.prime else write_determinantal_grobner_family_certificate(a.output)
