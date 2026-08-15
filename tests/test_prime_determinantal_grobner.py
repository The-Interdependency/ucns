# === CHECKS ===
# id: check_prime_grobner_protocol_frozen
#   proves: prime_grobner_protocol_identity_is_frozen
#   call: self::test_protocol_and_parent_presentations_are_frozen
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_prime_grobner_complete_accounting
#   proves: prime_grobner_generators_cover_every_maximal_minor
#   call: self::test_complete_minor_accounting_is_sealed
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_prime_grobner_reduced_bases
#   proves: prime_grobner_basis_is_complete_reduced_and_saturated
#   call: self::test_sealed_reduced_bases_have_expected_digests
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_prime_grobner_replay
#   proves: prime_grobner_independent_replay_agrees
#   call: self::test_independent_replay_is_exact
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_prime_grobner_nonclaims
#   proves: prime_grobner_receipt_preserves_nonclaims
#   call: self::test_result_document_preserves_research_boundary
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===
import hashlib,json
from pathlib import Path
from ucns.prime_determinantal_grobner import PROTOCOL_SHA256,PRESENTATION_SHA256,_sha
ROOT=Path(__file__).parents[1]
def _receipt(p): return json.loads((ROOT/f"generated/prime-determinantal-grobner-p{p}.json").read_text())
def test_protocol_and_parent_presentations_are_frozen():
    assert hashlib.sha256((ROOT/"docs/PREREGISTRATION_P7_P5_DETERMINANTAL_GROEBNER.md").read_bytes()).hexdigest()==PROTOCOL_SHA256
    prior=json.loads((ROOT/"generated/prime-symbolic-alexander-family-certificate.json").read_text())
    assert prior["p7"]["presentation_sha256"]==PRESENTATION_SHA256[7]
    assert prior["p5"]["presentation_sha256"]==PRESENTATION_SHA256[5]
def test_complete_minor_accounting_is_sealed():
    p7,p5=_receipt(7),_receipt(5)
    assert p7["accounting"]|{} == p7["accounting"]
    assert p7["accounting"]["candidate_pairs"]==38**2
    assert p5["accounting"]["candidate_pairs"]==816**2
    assert p5["accounting"]["nonzero_pair_products"]==174*565
def test_sealed_reduced_bases_have_expected_digests():
    assert _receipt(7)["basis_sha256"]=="c3bdb9b27f20191320e85360063113ed7e250996830ca4a4fd2ca8f11637127d"
    assert _receipt(5)["basis_sha256"]=="5e20f2539229070c12261d70cd6f1ba202ddeee04c7105e4bea1945253b79711"
    assert _sha(_receipt(7)["reduced_lex_basis"])==_receipt(7)["basis_sha256"]
    assert _sha(_receipt(5)["reduced_lex_basis"])==_receipt(5)["basis_sha256"]
def test_independent_replay_is_exact():
    for p in (7,5): assert _receipt(p)["independent_replay"]=={"canonical_basis_equal":True,"mutual_reduction":True}
def test_result_document_preserves_research_boundary():
    text=(ROOT/"docs/UCNS_P7_P5_DETERMINANTAL_GROEBNER_RESULTS.md").read_text()
    assert "rational-Laurent" in text and "does not" in text and "Length-four Milnor" in text
