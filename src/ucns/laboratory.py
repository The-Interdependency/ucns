# === MODULE_BUILD ===
# id: evaluator_candidate_laboratory
#   module_name: laboratory
#   module_kind: instrument
#   summary: registers competing equivalence, product-character, and faithful-breadth candidates and tests them without selecting a winner
#   owner: Erin Spencer
#   public_surface: EvaluatorKind, EvaluatorCandidate, EvaluatorRegistry, Witness, LawResult, Law, LawSuite, EvaluationReport, CandidateOutput, CandidateComparison, compare_candidates, null_zero_law, finite_nonnegative_law, pair_multiplicative_law, invariance_law, sensitivity_law, same_reference_different_candidate_law, same_candidate_different_reference_law
#   internal_surface: _values_equal
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_laboratory.py
#   rollout: candidate research infrastructure; no canonical evaluator
#   rollback: remove public exports and this module
#   requires: structural_cell_support_floor, retained_structure_envelope, structural_choice_policy_layer
#   since: 2026-07-21
#   unresolved: canonical equivalence, canonical M, canonical B, candidate promotion protocol
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: evaluator_registry_has_no_implicit_winner
#   given: multiple candidates of one evaluator kind are registered
#   then: all remain independently addressable and callers must name a candidate or request the full set
#   class: doctrine
#   since: 2026-07-21
#
# id: evaluator_replacement_is_explicit
#   given: a candidate name is already registered for an evaluator kind
#   then: replacement fails unless replace is explicitly true
#   class: safety
#   since: 2026-07-21
#
# id: law_suites_capture_failures_and_errors
#   given: laws are run against an evaluator candidate
#   then: pass, failure, and exception evidence are retained in one complete report
#   class: evidence
#   since: 2026-07-21
#
# id: candidate_comparison_exposes_disagreement_without_ranking
#   given: competing candidates evaluate the same subjects
#   then: outputs and disagreements are recorded without selecting a default, majority, best, or canonical candidate
#   class: doctrine
#   since: 2026-07-21
# === END CONTRACTS ===

"""Candidate evaluator registration, law testing, and comparison."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from enum import Enum
from math import isclose, isfinite
from typing import Any

from .carrier import STRUCTURAL_NULL
from .structure import Structure, pair


class EvaluatorKind(str, Enum):
    """Unresolved instrument families currently admitted to the laboratory."""

    EQUIVALENCE = "equivalence"
    PRODUCT_CHARACTER = "product-character"
    FAITHFUL_BREADTH = "faithful-breadth"


Evaluator = Callable[[Any], Any]


@dataclass(frozen=True, slots=True)
class EvaluatorCandidate:
    """One named candidate with explicit policy dependencies and no status promotion."""

    name: str
    kind: EvaluatorKind
    evaluator: Evaluator
    policy_dependencies: tuple[str, ...] = ()
    notes: str = ""
    version: str = "unversioned"

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("candidate name must be nonempty")
        try:
            kind = EvaluatorKind(self.kind)
        except ValueError as exc:
            raise ValueError("unknown evaluator kind") from exc
        object.__setattr__(self, "kind", kind)
        if not callable(self.evaluator):
            raise TypeError("candidate evaluator must be callable")
        dependencies = tuple(self.policy_dependencies)
        if any(not dependency.strip() for dependency in dependencies):
            raise ValueError("policy dependency names must be nonempty")
        object.__setattr__(self, "policy_dependencies", dependencies)
        if not self.version.strip():
            raise ValueError("candidate version must be nonempty")

    def evaluate(self, subject: Any) -> Any:
        return self.evaluator(subject)


@dataclass(slots=True)
class EvaluatorRegistry:
    """Multiple candidates per kind, deliberately without a default selector."""

    _candidates: dict[EvaluatorKind, dict[str, EvaluatorCandidate]] = field(
        default_factory=dict, repr=False
    )

    def register(self, candidate: EvaluatorCandidate, *, replace: bool = False) -> None:
        bucket = self._candidates.setdefault(candidate.kind, {})
        if candidate.name in bucket and not replace:
            raise ValueError(
                f"candidate already registered for {candidate.kind.value}: {candidate.name}"
            )
        bucket[candidate.name] = candidate

    def resolve(self, kind: EvaluatorKind, name: str) -> EvaluatorCandidate:
        selected_kind = EvaluatorKind(kind)
        try:
            return self._candidates[selected_kind][name]
        except KeyError as exc:
            raise KeyError(
                f"unknown {selected_kind.value} evaluator candidate: {name}"
            ) from exc

    def names(self, kind: EvaluatorKind) -> tuple[str, ...]:
        return tuple(self._candidates.get(EvaluatorKind(kind), {}))

    def candidates(self, kind: EvaluatorKind) -> tuple[EvaluatorCandidate, ...]:
        return tuple(self._candidates.get(EvaluatorKind(kind), {}).values())

    def evaluate_all(self, kind: EvaluatorKind, subject: Any) -> tuple["CandidateOutput", ...]:
        return _evaluate_candidates(self.candidates(kind), subject)


@dataclass(frozen=True, slots=True)
class Witness:
    """Retained subjects and the intended pressure they place on a candidate."""

    name: str
    subjects: tuple[Any, ...]
    expectation: str
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.expectation.strip():
            raise ValueError("witness name and expectation must be nonempty")
        subjects = tuple(self.subjects)
        if not subjects:
            raise ValueError("a witness requires at least one subject")
        object.__setattr__(self, "subjects", subjects)


@dataclass(frozen=True, slots=True)
class LawResult:
    """One law outcome with retained evidence and optional exception text."""

    law_name: str
    passed: bool
    detail: str
    evidence: Any = None
    error: str | None = None

    def __post_init__(self) -> None:
        if not self.law_name.strip() or not self.detail.strip():
            raise ValueError("law result name and detail must be nonempty")
        if self.passed and self.error is not None:
            raise ValueError("a passing law result cannot carry an error")


LawCheck = Callable[[EvaluatorCandidate], LawResult]


@dataclass(frozen=True, slots=True)
class Law:
    """A named candidate check that captures exceptions as evidence."""

    name: str
    check: LawCheck

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("law name must be nonempty")
        if not callable(self.check):
            raise TypeError("law check must be callable")

    def run(self, candidate: EvaluatorCandidate) -> LawResult:
        try:
            result = self.check(candidate)
            if not isinstance(result, LawResult):
                raise TypeError("law check must return LawResult")
        except Exception as exc:
            return LawResult(
                self.name,
                False,
                "law raised while evaluating candidate",
                error=f"{type(exc).__name__}: {exc}",
            )
        if result.law_name == self.name:
            return result
        return LawResult(
            self.name,
            result.passed,
            result.detail,
            result.evidence,
            result.error,
        )


@dataclass(frozen=True, slots=True)
class EvaluationReport:
    """Complete ordered law evidence for one candidate."""

    candidate_name: str
    kind: EvaluatorKind
    suite_name: str
    results: tuple[LawResult, ...]

    @property
    def all_passed(self) -> bool:
        return bool(self.results) and all(result.passed for result in self.results)


@dataclass(frozen=True, slots=True)
class LawSuite:
    """An explicit ordered set of laws applicable to selected candidates."""

    name: str
    laws: tuple[Law, ...]

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("law-suite name must be nonempty")
        laws = tuple(self.laws)
        if not laws:
            raise ValueError("a law suite requires at least one law")
        object.__setattr__(self, "laws", laws)

    def evaluate(self, candidate: EvaluatorCandidate) -> EvaluationReport:
        return EvaluationReport(
            candidate.name,
            candidate.kind,
            self.name,
            tuple(law.run(candidate) for law in self.laws),
        )


@dataclass(frozen=True, slots=True)
class CandidateOutput:
    """One candidate output or captured evaluation error."""

    candidate_name: str
    output: Any = None
    error: str | None = None

    @property
    def succeeded(self) -> bool:
        return self.error is None


@dataclass(frozen=True, slots=True)
class CandidateComparison:
    """Side-by-side candidate outputs for one retained subject."""

    kind: EvaluatorKind
    subject: Any
    outputs: tuple[CandidateOutput, ...]
    disagreement: bool


def _values_equal(first: Any, second: Any) -> bool:
    if isinstance(first, (int, float)) and isinstance(second, (int, float)):
        return isclose(float(first), float(second), rel_tol=1e-12, abs_tol=1e-12)
    try:
        result = first == second
    except Exception:
        return False
    return result if isinstance(result, bool) else False


def _evaluate_candidates(
    candidates: Iterable[EvaluatorCandidate], subject: Any
) -> tuple[CandidateOutput, ...]:
    outputs: list[CandidateOutput] = []
    for candidate in tuple(candidates):
        try:
            outputs.append(CandidateOutput(candidate.name, candidate.evaluate(subject)))
        except Exception as exc:
            outputs.append(
                CandidateOutput(
                    candidate.name,
                    error=f"{type(exc).__name__}: {exc}",
                )
            )
    return tuple(outputs)


def compare_candidates(
    candidates: Iterable[EvaluatorCandidate], subjects: Iterable[Any]
) -> tuple[CandidateComparison, ...]:
    """Expose candidate disagreements without ranking or selecting a winner."""

    selected = tuple(candidates)
    if not selected:
        raise ValueError("candidate comparison requires at least one candidate")
    kinds = {candidate.kind for candidate in selected}
    if len(kinds) != 1:
        raise ValueError("candidate comparison requires one evaluator kind")
    kind = selected[0].kind

    comparisons: list[CandidateComparison] = []
    for subject in tuple(subjects):
        outputs = _evaluate_candidates(selected, subject)
        successful = [output.output for output in outputs if output.succeeded]
        disagreement = any(not output.succeeded for output in outputs)
        if successful:
            first = successful[0]
            disagreement = disagreement or any(
                not _values_equal(first, value) for value in successful[1:]
            )
        comparisons.append(CandidateComparison(kind, subject, outputs, disagreement))
    return tuple(comparisons)


def null_zero_law(
    *, name: str = "null-evaluates-to-zero", null_subject: Any = STRUCTURAL_NULL
) -> Law:
    """Require a candidate to map Structural Null to numeric zero."""

    def check(candidate: EvaluatorCandidate) -> LawResult:
        value = candidate.evaluate(null_subject)
        passed = _values_equal(value, 0.0)
        return LawResult(name, passed, "candidate null output compared with zero", value)

    return Law(name, check)


def finite_nonnegative_law(
    subjects: Iterable[Any], *, name: str = "finite-nonnegative"
) -> Law:
    """Require finite nonnegative numeric outputs on declared subjects."""

    retained = tuple(subjects)

    def check(candidate: EvaluatorCandidate) -> LawResult:
        values = tuple(candidate.evaluate(subject) for subject in retained)
        passed = all(
            isinstance(value, (int, float))
            and isfinite(float(value))
            and float(value) >= 0.0
            for value in values
        )
        return LawResult(name, passed, "candidate outputs checked for finite nonnegativity", values)

    return Law(name, check)


def pair_multiplicative_law(
    pairs: Iterable[tuple[Structure, Structure]],
    *,
    name: str = "pair-multiplicative",
    tolerance: float = 1e-12,
) -> Law:
    """Require evaluation of the actual Cartesian pair to multiply."""

    retained = tuple(pairs)

    def check(candidate: EvaluatorCandidate) -> LawResult:
        evidence: list[tuple[Any, Any, Any]] = []
        passed = True
        for left, right in retained:
            left_value = float(candidate.evaluate(left))
            right_value = float(candidate.evaluate(right))
            paired_value = float(candidate.evaluate(pair(left, right)))
            evidence.append((left_value, right_value, paired_value))
            passed = passed and isclose(
                paired_value,
                left_value * right_value,
                rel_tol=tolerance,
                abs_tol=tolerance,
            )
        return LawResult(name, passed, "candidate checked under actual carrier pairing", tuple(evidence))

    return Law(name, check)


def invariance_law(
    witnesses: Iterable[Witness], *, name: str = "declared-invariance"
) -> Law:
    """Require equal outputs only for explicitly declared equivalent subjects."""

    retained = tuple(witnesses)

    def check(candidate: EvaluatorCandidate) -> LawResult:
        evidence: list[tuple[str, tuple[Any, ...]]] = []
        passed = True
        for witness in retained:
            values = tuple(candidate.evaluate(subject) for subject in witness.subjects)
            evidence.append((witness.name, values))
            first = values[0]
            passed = passed and all(_values_equal(first, value) for value in values[1:])
        return LawResult(name, passed, "candidate checked on declared equivalent witnesses", tuple(evidence))

    return Law(name, check)


def sensitivity_law(
    witnesses: Iterable[Witness], *, name: str = "declared-sensitivity"
) -> Law:
    """Require different outputs for explicitly declared distinct subject pairs."""

    retained = tuple(witnesses)

    def check(candidate: EvaluatorCandidate) -> LawResult:
        evidence: list[tuple[str, tuple[Any, ...]]] = []
        passed = True
        for witness in retained:
            values = tuple(candidate.evaluate(subject) for subject in witness.subjects)
            evidence.append((witness.name, values))
            if len(values) < 2:
                passed = False
            else:
                passed = passed and any(
                    not _values_equal(values[0], value) for value in values[1:]
                )
        return LawResult(name, passed, "candidate checked on declared distinct witnesses", tuple(evidence))

    return Law(name, check)


def same_reference_different_candidate_law(
    reference: Callable[[Any], Any],
    witnesses: Iterable[Witness],
    *,
    name: str = "same-reference-different-candidate",
) -> Law:
    """Require equal reference outputs and distinct candidate outputs."""

    if not callable(reference):
        raise TypeError("reference evaluator must be callable")
    retained = tuple(witnesses)

    def check(candidate: EvaluatorCandidate) -> LawResult:
        evidence: list[tuple[str, Any, Any, Any, Any]] = []
        passed = True
        for witness in retained:
            if len(witness.subjects) != 2:
                raise ValueError("separation witnesses require exactly two subjects")
            left, right = witness.subjects
            reference_left = reference(left)
            reference_right = reference(right)
            candidate_left = candidate.evaluate(left)
            candidate_right = candidate.evaluate(right)
            evidence.append(
                (
                    witness.name,
                    reference_left,
                    reference_right,
                    candidate_left,
                    candidate_right,
                )
            )
            passed = passed and _values_equal(reference_left, reference_right)
            passed = passed and not _values_equal(candidate_left, candidate_right)
        return LawResult(
            name,
            passed,
            "equal reference outputs checked against distinct candidate outputs",
            tuple(evidence),
        )

    return Law(name, check)


def same_candidate_different_reference_law(
    reference: Callable[[Any], Any],
    witnesses: Iterable[Witness],
    *,
    name: str = "same-candidate-different-reference",
) -> Law:
    """Require equal candidate outputs and distinct reference outputs."""

    if not callable(reference):
        raise TypeError("reference evaluator must be callable")
    retained = tuple(witnesses)

    def check(candidate: EvaluatorCandidate) -> LawResult:
        evidence: list[tuple[str, Any, Any, Any, Any]] = []
        passed = True
        for witness in retained:
            if len(witness.subjects) != 2:
                raise ValueError("separation witnesses require exactly two subjects")
            left, right = witness.subjects
            reference_left = reference(left)
            reference_right = reference(right)
            candidate_left = candidate.evaluate(left)
            candidate_right = candidate.evaluate(right)
            evidence.append(
                (
                    witness.name,
                    reference_left,
                    reference_right,
                    candidate_left,
                    candidate_right,
                )
            )
            passed = passed and not _values_equal(reference_left, reference_right)
            passed = passed and _values_equal(candidate_left, candidate_right)
        return LawResult(
            name,
            passed,
            "equal candidate outputs checked against distinct reference outputs",
            tuple(evidence),
        )

    return Law(name, check)
