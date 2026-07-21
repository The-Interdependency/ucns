# === CHECKS ===
# id: check_explicit_subject_adapters
#   proves: subject_identity_requires_explicit_adapter
#   call: self::test_explicit_subject_adapters
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_manifest_pins_research_inputs
#   proves: experiment_manifests_pin_all_research_inputs
#   call: self::test_manifest_pins_research_inputs
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_holdout_decision_guard
#   proves: development_and_holdout_evidence_are_separate
#   call: self::test_holdout_decision_guard
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_separate_authorship_records
#   proves: candidate_witness_and_decision_authorship_are_recorded
#   call: self::test_separate_authorship_records
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
#
# id: check_reproduction_reporting
#   proves: reproduction_checks_report_match_or_reason
#   call: self::test_reproduction_reporting
#   requires: python3
#   timeout: 5
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import json
from dataclasses import asdict

import pytest

from ucns import (
    AuthorshipRecord,
    CandidateIdentity,
    CorpusPartition,
    EvaluatorCandidate,
    EvaluatorKind,
    ExperimentManifest,
    ExperimentResult,
    HoldoutReport,
    LawSuite,
    LawSuiteDigest,
    PolicyDigest,
    SubjectRecord,
    WitnessCase,
    WitnessCorpus,
    WitnessOrigin,
    build_candidate_decision_packet,
    check_reproduction,
    comparison_policy_digest,
    exact_comparison_policy,
    json_content_adapter,
    null_zero_law,
)
from ucns.experiments import ContentAdapter


def test_explicit_subject_adapters() -> None:
    adapter = json_content_adapter()
    first = SubjectRecord.create("first", {"b": 2, "a": 1}, adapter)
    second = SubjectRecord.create("second", {"a": 1, "b": 2}, adapter)
    assert first.digest == second.digest

    author = AuthorshipRecord("witness-author", "Erin", "multiplicity fixture")
    duplicate_case = WitnessCase(
        "duplicate-occurrence",
        (first.digest, first.digest),
        "the same content occurs twice",
        WitnessOrigin.HAND_AUTHORED,
        CorpusPartition.DEVELOPMENT,
        author,
    )
    corpus = WitnessCorpus("duplicates", "1", (first,), (duplicate_case,))
    assert corpus.cases[0].subject_digests == (first.digest, first.digest)

    with pytest.raises(TypeError):
        SubjectRecord.create("bad", object(), adapter)


def research_fixture():
    adapter = json_content_adapter()
    first = SubjectRecord.create("first", {"x": 1}, adapter)
    second = SubjectRecord.create("second", {"x": 2}, adapter)
    author = AuthorshipRecord("witness-author", "Erin", "test fixture")
    cases = (
        WitnessCase(
            "dev",
            (first.digest,),
            "development",
            WitnessOrigin.HAND_AUTHORED,
            CorpusPartition.DEVELOPMENT,
            author,
        ),
        WitnessCase(
            "holdout",
            (second.digest,),
            "holdout",
            WitnessOrigin.ADVERSARIAL,
            CorpusPartition.HOLDOUT,
            author,
        ),
    )
    corpus = WitnessCorpus("corpus", "1", (first, second), cases)
    candidate = EvaluatorCandidate(
        "zero",
        EvaluatorKind.PRODUCT_CHARACTER,
        lambda subject: 0.0,
        version="1",
        code_reference="tests:zero",
        scope="test",
    )
    suite = LawSuite(
        "null", (null_zero_law(),), exact_comparison_policy()
    )
    return adapter, corpus, candidate, suite


def test_manifest_pins_research_inputs() -> None:
    _, corpus, candidate, suite = research_fixture()
    manifest = ExperimentManifest(
        "experiment",
        "1",
        CandidateIdentity.from_candidate(candidate),
        corpus.digest,
        LawSuiteDigest.from_suite(suite),
        (PolicyDigest.create("ordered", "1"),),
        comparison_policy_digest(suite.comparison),
        environment=(("python", "3.10+"),),
    )
    assert manifest.digest == manifest.digest


def test_holdout_decision_guard() -> None:
    _, corpus, candidate, suite = research_fixture()
    development = suite.evaluate(candidate)
    authors = (
        AuthorshipRecord("candidate-author", "A", "candidate"),
        AuthorshipRecord("witness-author", "B", "witnesses"),
        AuthorshipRecord("decision-author", "C", "decision"),
    )
    without_holdout = build_candidate_decision_packet(
        candidate,
        development_report=development,
        holdout_report=None,
        rollback_behavior="remove candidate",
        candidate_authorship=authors[0],
        witness_authorship=authors[1],
        decision_authorship=authors[2],
    )
    assert not without_holdout.reviewable

    holdout = HoldoutReport(corpus.digest, suite.evaluate(candidate))
    with_holdout = build_candidate_decision_packet(
        candidate,
        development_report=development,
        holdout_report=holdout,
        rollback_behavior="remove candidate",
        candidate_authorship=authors[0],
        witness_authorship=authors[1],
        decision_authorship=authors[2],
    )
    assert with_holdout.reviewable
    assert not with_holdout.canonical


def test_separate_authorship_records() -> None:
    _, _, candidate, suite = research_fixture()
    report = suite.evaluate(candidate)
    packet = build_candidate_decision_packet(
        candidate,
        development_report=report,
        holdout_report=HoldoutReport("holdout", report),
        rollback_behavior="rollback",
        candidate_authorship=AuthorshipRecord(
            "candidate-author", "A", "candidate"
        ),
        witness_authorship=AuthorshipRecord(
            "witness-author", "B", "witness"
        ),
        decision_authorship=AuthorshipRecord(
            "decision-author", "C", "decision"
        ),
    )
    assert (
        packet.candidate_authorship.role
        != packet.witness_authorship.role
    )


def test_reproduction_reporting() -> None:
    _, _, candidate, suite = research_fixture()
    report = suite.evaluate(candidate)
    first = ExperimentResult(
        "manifest", report, CorpusPartition.DEVELOPMENT, True
    )
    second = ExperimentResult(
        "manifest", report, CorpusPartition.DEVELOPMENT, True
    )
    adapter = ContentAdapter(
        "report-json",
        "1",
        lambda value: json.dumps(
            asdict(value), sort_keys=True, default=str
        ).encode(),
    )
    check = check_reproduction(first, second, adapter=adapter)
    assert check.reproduced

    mismatch = check_reproduction(
        first,
        ExperimentResult(
            "other", report, CorpusPartition.DEVELOPMENT, True
        ),
        adapter=adapter,
    )
    assert not mismatch.reproduced
    assert "manifest" in mismatch.note
