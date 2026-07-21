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
    ContentAdapter,
    CorpusPartition,
    CycleMode,
    EvaluatorCandidate,
    EvaluatorKind,
    ExperimentManifest,
    ExperimentResult,
    HoldoutReport,
    LawSuite,
    LawSuiteDigest,
    PolicyDigest,
    SubjectRecord,
    TraversalPolicy,
    WitnessCase,
    WitnessCorpus,
    WitnessOrigin,
    build_candidate_decision_packet,
    check_reproduction,
    comparison_policy_digest,
    custom_comparison_policy,
    exact_comparison_policy,
    json_content_adapter,
    null_zero_law,
    traversal_policy_digest,
)


def test_explicit_subject_adapters() -> None:
    adapter = json_content_adapter()
    source = {"b": 2, "a": [1]}
    first = SubjectRecord.create("first", source, adapter)
    second = SubjectRecord.create("second", {"a": [1], "b": 2}, adapter)
    assert first.digest == second.digest

    source["a"].append(99)
    assert first.subject == {"b": 2, "a": [1]}
    exposed = first.subject
    exposed["a"].append(88)
    assert first.subject == {"b": 2, "a": [1]}

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


def research_fixture(fixture_digest: str = "structural-null-v1"):
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
        code_reference="tests.test_experiments:zero",
        scope="test",
    )
    suite = LawSuite(
        "null",
        (null_zero_law(fixture_digest=fixture_digest),),
        exact_comparison_policy(),
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

    _, _, _, changed_suite = research_fixture("different-fixtures")
    assert LawSuiteDigest.from_suite(suite).digest != LawSuiteDigest.from_suite(
        changed_suite
    ).digest

    unrecorded = LawSuite(
        "unrecorded",
        (null_zero_law(),),
        exact_comparison_policy(),
    )
    with pytest.raises(ValueError):
        LawSuiteDigest.from_suite(unrecorded)

    first_custom = custom_comparison_policy(
        "custom",
        lambda left, right: left == right,
        version="1",
        code_reference="tests.test_experiments:equal",
    )
    second_custom = custom_comparison_policy(
        "custom",
        lambda left, right: left != right,
        version="1",
        code_reference="tests.test_experiments:not-equal",
    )
    assert comparison_policy_digest(first_custom).digest != comparison_policy_digest(
        second_custom
    ).digest

    first_traversal = TraversalPolicy(
        "fixed",
        CycleMode.FIXED_POINT,
        fixed_point_resolver=lambda node, path: node,
        resolver_reference="tests.test_experiments:resolver-a",
    )
    second_traversal = TraversalPolicy(
        "fixed",
        CycleMode.FIXED_POINT,
        fixed_point_resolver=lambda node, path: path,
        resolver_reference="tests.test_experiments:resolver-b",
    )
    assert traversal_policy_digest(first_traversal).digest != traversal_policy_digest(
        second_traversal
    ).digest


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

    other = EvaluatorCandidate(
        "other",
        EvaluatorKind.PRODUCT_CHARACTER,
        lambda subject: 0.0,
        version="1",
        code_reference="tests.test_experiments:other",
        scope="test",
    )
    other_report = suite.evaluate(other)
    with pytest.raises(ValueError):
        build_candidate_decision_packet(
            candidate,
            development_report=other_report,
            holdout_report=holdout,
            rollback_behavior="remove candidate",
            candidate_authorship=authors[0],
            witness_authorship=authors[1],
            decision_authorship=authors[2],
        )
    with pytest.raises(ValueError):
        build_candidate_decision_packet(
            candidate,
            development_report=development,
            holdout_report=HoldoutReport(corpus.digest, other_report),
            rollback_behavior="remove candidate",
            candidate_authorship=authors[0],
            witness_authorship=authors[1],
            decision_authorship=authors[2],
        )


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
    assert packet.candidate_authorship.role != packet.witness_authorship.role

    subject = SubjectRecord.create("subject", {"x": 1}, json_content_adapter())
    first = WitnessCase(
        "case",
        (subject.digest,),
        "expectation",
        WitnessOrigin.HAND_AUTHORED,
        CorpusPartition.DEVELOPMENT,
        AuthorshipRecord("witness-author", "Erin", "same provenance"),
    )
    second = WitnessCase(
        "case",
        (subject.digest,),
        "expectation",
        WitnessOrigin.HAND_AUTHORED,
        CorpusPartition.DEVELOPMENT,
        AuthorshipRecord("candidate-author", "Erin", "same provenance"),
    )
    assert first.digest != second.digest


def test_reproduction_reporting() -> None:
    _, _, candidate, suite = research_fixture()
    report = suite.evaluate(candidate)
    first = ExperimentResult(
        "manifest", report, CorpusPartition.DEVELOPMENT, True, "stable"
    )
    second = ExperimentResult(
        "manifest", report, CorpusPartition.DEVELOPMENT, True, "stable"
    )
    adapter = ContentAdapter(
        "result-json",
        "1",
        lambda value: json.dumps(
            asdict(value), sort_keys=True, default=str
        ).encode(),
        "tests.test_experiments:result-json",
    )
    check = check_reproduction(first, second, adapter=adapter)
    assert check.reproduced

    metadata_change = check_reproduction(
        first,
        ExperimentResult(
            "manifest", report, CorpusPartition.HOLDOUT, True, "stable"
        ),
        adapter=adapter,
    )
    assert not metadata_change.reproduced

    note_change = check_reproduction(
        first,
        ExperimentResult(
            "manifest", report, CorpusPartition.DEVELOPMENT, False, "failed"
        ),
        adapter=adapter,
    )
    assert not note_change.reproduced

    mismatch = check_reproduction(
        first,
        ExperimentResult(
            "other", report, CorpusPartition.DEVELOPMENT, True
        ),
        adapter=adapter,
    )
    assert not mismatch.reproduced
    assert "manifest" in mismatch.note
