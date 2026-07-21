# === MODULE_BUILD ===
# id: first_competing_evaluator_candidate_families
#   module_name: candidates
#   module_kind: instrument
#   summary: supplies explicit noncanonical equivalence, product-character, and faithful-breadth candidate families for laboratory pressure
#   owner: Erin Spencer
#   public_surface: CandidateScopeError, exact_evidence_equivalence_candidate, policy_projection_equivalence_candidate, layer_scoped_equivalence_candidate, geometric_mean_product_candidate, maximum_support_product_candidate, minimum_support_product_candidate, cell_log_support_breadth_candidate, cell_detail_breadth_candidate, retained_presence_breadth_candidate
#   internal_surface: _digest, _carrier, _cell_supports
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests/test_candidates.py
#   rollout: explicit candidate families only; no evaluator is canonical
#   rollback: remove candidate constructors; laboratory and evidence remain
#   requires: evaluator_candidate_laboratory, reproducible_witness_experiment_pipeline
#   since: 2026-07-21
#   unresolved: canonical equivalence, canonical M, canonical B
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: first_candidate_families_coexist_without_selection
#   given: multiple equivalence, product-character, or faithful-breadth candidates are constructed
#   then: each has explicit version, code reference, scope, and policy dependencies and none is selected as canonical
#   class: doctrine
#   since: 2026-07-21
#
# id: cell_only_candidates_fail_outside_scope
#   given: a cell-only M or B candidate receives retained evidence without a cell carrier
#   then: evaluation raises CandidateScopeError rather than treating unmeasured layers as zero distinction
#   class: safety
#   since: 2026-07-21
#
# id: initial_product_candidates_multiply_under_actual_pairing
#   given: positive-support carriers are paired by the established Cartesian law
#   then: geometric-mean, maximum-support, and minimum-support candidates satisfy their declared multiplicativity fixtures
#   class: evidence
#   since: 2026-07-21
#
# id: candidate_constructors_do_not_promote_canon
#   given: an initial equivalence, M, or B candidate is constructed
#   then: it remains an EvaluatorCandidate and exposes no canonical or winner status
#   class: safety
#   since: 2026-07-21
# === END CONTRACTS ===

from __future__ import annotations

from hashlib import sha256
from math import exp, log, log1p
from typing import Any

from .carrier import STRUCTURAL_NULL
from .envelope import RetainedStructure, project_layer
from .experiments import ContentAdapter
from .laboratory import EvaluatorCandidate, EvaluatorKind
from .policy import PolicyRegistry, StructurePolicy
from .structure import Carrier, support_weight


class CandidateScopeError(ValueError):
    pass


def _digest(adapter: ContentAdapter, value: Any) -> str:
    payload = (
        b"ucns-candidate-view\0"
        + adapter.name.encode()
        + b"\0"
        + adapter.version.encode()
        + b"\0"
        + adapter.encode(value)
    )
    return sha256(payload).hexdigest()


def exact_evidence_equivalence_candidate(
    adapter: ContentAdapter,
    *,
    name: str = "exact-evidence",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:exact_evidence_equivalence_candidate"
    ),
) -> EvaluatorCandidate:
    return EvaluatorCandidate(
        name,
        EvaluatorKind.EQUIVALENCE,
        lambda subject: _digest(adapter, subject),
        version=version,
        code_reference=code_reference,
        scope="adapter-defined exact retained evidence",
        policy_dependencies=(adapter.name,),
    )


def policy_projection_equivalence_candidate(
    layer_name: str,
    policy: StructurePolicy | str,
    adapter: ContentAdapter,
    *,
    registry: PolicyRegistry | None = None,
    occurrence: int = 0,
    name: str = "policy-projection",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:policy_projection_equivalence_candidate"
    ),
) -> EvaluatorCandidate:
    policy_name = policy if isinstance(policy, str) else policy.name

    def evaluate(subject: Any) -> str:
        if not isinstance(subject, RetainedStructure):
            raise CandidateScopeError(
                "policy-projection equivalence requires RetainedStructure"
            )
        projection = project_layer(
            subject,
            layer_name,
            policy,
            occurrence=occurrence,
            registry=registry,
        )
        return _digest(adapter, projection.view)

    return EvaluatorCandidate(
        name,
        EvaluatorKind.EQUIVALENCE,
        evaluate,
        version=version,
        code_reference=code_reference,
        scope=(
            f"layer {layer_name!r} occurrence {occurrence} "
            "under policy projection"
        ),
        policy_dependencies=(policy_name, adapter.name),
    )


def layer_scoped_equivalence_candidate(
    layer_names: tuple[str, ...],
    adapter: ContentAdapter,
    *,
    name: str = "layer-scoped",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:layer_scoped_equivalence_candidate"
    ),
) -> EvaluatorCandidate:
    selected = tuple(layer_names)
    if not selected or any(not layer.strip() for layer in selected):
        raise ValueError("layer-scoped equivalence requires named layers")

    def evaluate(subject: Any) -> str:
        if not isinstance(subject, RetainedStructure):
            raise CandidateScopeError(
                "layer-scoped equivalence requires RetainedStructure"
            )
        evidence = tuple(
            (layer.name, layer.evidence)
            for layer in subject.retained_layers
            if layer.name in selected
        )
        return _digest(adapter, evidence)

    return EvaluatorCandidate(
        name,
        EvaluatorKind.EQUIVALENCE,
        evaluate,
        version=version,
        code_reference=code_reference,
        scope=f"retained layers {selected!r}",
        policy_dependencies=(adapter.name,),
    )


def _carrier(subject: Any) -> Carrier | None:
    if subject is STRUCTURAL_NULL:
        return None
    if isinstance(subject, Carrier):
        return subject
    if isinstance(subject, RetainedStructure):
        if subject.carrier is STRUCTURAL_NULL:
            raise CandidateScopeError(
                "cell-only candidate cannot evaluate an envelope without cells"
            )
        return subject.carrier
    raise CandidateScopeError(
        "cell-only candidate requires Carrier, RetainedStructure with cells, "
        "or Structural Null"
    )


def _cell_supports(subject: Any) -> tuple[float, ...]:
    carrier = _carrier(subject)
    return (
        ()
        if carrier is None
        else tuple(cell.support for cell in carrier.cells)
    )


def geometric_mean_product_candidate(
    *,
    name: str = "cell-support-geometric-mean",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:geometric_mean_product_candidate"
    ),
) -> EvaluatorCandidate:
    def evaluate(subject: Any) -> float:
        values = _cell_supports(subject)
        if not values:
            return 0.0
        return exp(sum(log(value) for value in values) / len(values))

    return EvaluatorCandidate(
        name,
        EvaluatorKind.PRODUCT_CHARACTER,
        evaluate,
        version=version,
        code_reference=code_reference,
        scope="positive cell supports only",
    )


def maximum_support_product_candidate(
    *,
    name: str = "cell-support-maximum",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:maximum_support_product_candidate"
    ),
) -> EvaluatorCandidate:
    return EvaluatorCandidate(
        name,
        EvaluatorKind.PRODUCT_CHARACTER,
        lambda subject: max(_cell_supports(subject), default=0.0),
        version=version,
        code_reference=code_reference,
        scope="positive cell supports only",
    )


def minimum_support_product_candidate(
    *,
    name: str = "cell-support-minimum",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:minimum_support_product_candidate"
    ),
) -> EvaluatorCandidate:
    return EvaluatorCandidate(
        name,
        EvaluatorKind.PRODUCT_CHARACTER,
        lambda subject: min(_cell_supports(subject), default=0.0),
        version=version,
        code_reference=code_reference,
        scope="positive cell supports only",
    )


def cell_log_support_breadth_candidate(
    *,
    name: str = "cell-log-support",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:cell_log_support_breadth_candidate"
    ),
) -> EvaluatorCandidate:
    def evaluate(subject: Any) -> float:
        carrier = _carrier(subject)
        return 0.0 if carrier is None else log1p(support_weight(carrier))

    return EvaluatorCandidate(
        name,
        EvaluatorKind.FAITHFUL_BREADTH,
        evaluate,
        version=version,
        code_reference=code_reference,
        scope="cell-only aggregate support",
    )


def cell_detail_breadth_candidate(
    *,
    name: str = "cell-detail",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:cell_detail_breadth_candidate"
    ),
) -> EvaluatorCandidate:
    def evaluate(subject: Any) -> float:
        values = _cell_supports(subject)
        return (
            0.0
            if not values
            else sum(log1p(value) for value in values)
            + float(len(values))
        )

    return EvaluatorCandidate(
        name,
        EvaluatorKind.FAITHFUL_BREADTH,
        evaluate,
        version=version,
        code_reference=code_reference,
        scope="cell supports and cell occurrence count",
    )


def retained_presence_breadth_candidate(
    *,
    name: str = "retained-presence",
    version: str = "1",
    code_reference: str = (
        "ucns.candidates:retained_presence_breadth_candidate"
    ),
) -> EvaluatorCandidate:
    def evaluate(subject: Any) -> float:
        if subject is STRUCTURAL_NULL:
            return 0.0
        if isinstance(subject, Carrier):
            return log1p(support_weight(subject)) + float(
                len(subject.cells)
            )
        if not isinstance(subject, RetainedStructure):
            raise CandidateScopeError(
                "retained-presence breadth requires a retained envelope"
            )
        cell_component = (
            0.0
            if subject.carrier is STRUCTURAL_NULL
            else log1p(support_weight(subject.carrier))
            + float(len(subject.carrier.cells))
        )
        return cell_component + float(len(subject.retained_layers))

    return EvaluatorCandidate(
        name,
        EvaluatorKind.FAITHFUL_BREADTH,
        evaluate,
        version=version,
        code_reference=code_reference,
        scope="cell carrier plus retained-layer occurrence presence",
    )
