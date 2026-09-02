"""Core contract validation without third-party dependencies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

EVIDENCE_STATES = {"CONFIRMED", "INFERRED", "PROPOSED", "UNKNOWN", "CONFLICTING"}
MODES = {"EXPLORE", "DEFINE", "DESIGN", "BUILD", "AUDIT", "FULL"}
VERDICTS = {"READY", "READY WITH RISKS", "REVISE", "BLOCKED"}


@dataclass(frozen=True)
class Finding:
    code: str
    message: str
    severity: str = "error"


def _duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    return {value for value in values if value in seen or seen.add(value)}


def validate_project(project: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for key in ("project", "mode", "evidence", "requirements", "verdict"):
        if key not in project:
            findings.append(Finding("DTS001", f"Missing required field: {key}"))

    if project.get("mode") not in MODES:
        findings.append(Finding("DTS002", "Mode is not recognized"))
    if project.get("verdict") not in VERDICTS:
        findings.append(Finding("DTS003", "Verdict is not recognized"))

    evidence = project.get("evidence", [])
    requirements = project.get("requirements", [])
    decisions = project.get("decisions", [])
    verifications = project.get("verifications", [])
    if not all(isinstance(group, list) for group in (evidence, requirements, decisions, verifications)):
        findings.append(Finding("DTS004", "Evidence, requirements, decisions, and verifications must be arrays"))
        return findings

    evidence_ids = [str(item.get("id", "")) for item in evidence if isinstance(item, dict)]
    requirement_ids = [str(item.get("id", "")) for item in requirements if isinstance(item, dict)]
    decision_ids = [str(item.get("id", "")) for item in decisions if isinstance(item, dict)]

    for kind, ids in (("evidence", evidence_ids), ("requirement", requirement_ids), ("decision", decision_ids)):
        for duplicate in _duplicates(ids):
            findings.append(Finding("DTS005", f"Duplicate {kind} identifier: {duplicate}"))

    evidence_set = set(evidence_ids)
    requirement_set = set(requirement_ids)
    decision_set = set(decision_ids)

    for item in evidence:
        if isinstance(item, dict) and item.get("status") not in EVIDENCE_STATES:
            findings.append(Finding("DTS006", f"{item.get('id', 'Evidence')} has an invalid status"))

    for requirement in requirements:
        if not isinstance(requirement, dict):
            findings.append(Finding("DTS007", "Requirement must be an object"))
            continue
        unknown = set(requirement.get("evidence_ids", [])) - evidence_set
        if unknown:
            findings.append(Finding("DTS008", f"{requirement.get('id')} references unknown evidence: {sorted(unknown)}"))
        if not requirement.get("acceptance_criteria"):
            findings.append(Finding("DTS009", f"{requirement.get('id')} has no acceptance criteria", "warning"))

    covered_requirements: set[str] = set()
    for decision in decisions:
        if not isinstance(decision, dict):
            findings.append(Finding("DTS010", "Decision must be an object"))
            continue
        refs = set(decision.get("requirement_ids", []))
        covered_requirements.update(refs)
        unknown = refs - requirement_set
        if unknown:
            findings.append(Finding("DTS011", f"{decision.get('id')} references unknown requirements: {sorted(unknown)}"))
        for field in ("alternative", "tradeoff", "verification"):
            if not decision.get(field):
                findings.append(Finding("DTS012", f"{decision.get('id')} is missing {field}", "warning"))

    for requirement_id in requirement_set - covered_requirements:
        findings.append(Finding("DTS013", f"{requirement_id} has no linked decision", "warning"))

    verified_requirements: set[str] = set()
    for verification in verifications:
        if not isinstance(verification, dict):
            findings.append(Finding("DTS014", "Verification must be an object"))
            continue
        verified_requirements.update(verification.get("requirement_ids", []))
        unknown_decisions = set(verification.get("decision_ids", [])) - decision_set
        if unknown_decisions:
            findings.append(Finding("DTS015", f"Verification references unknown decisions: {sorted(unknown_decisions)}"))
        if verification.get("result") == "PASS" and not verification.get("evidence"):
            findings.append(Finding("DTS016", "Passing verification has no recorded evidence"))

    if project.get("verdict") == "READY":
        unverified = requirement_set - verified_requirements
        if unverified:
            findings.append(Finding("DTS017", f"READY project has unverified requirements: {sorted(unverified)}"))
        material_unknowns = [item.get("id") for item in evidence if isinstance(item, dict) and item.get("status") in {"UNKNOWN", "CONFLICTING"} and item.get("material", True)]
        if material_unknowns:
            findings.append(Finding("DTS018", f"READY project has unresolved material evidence: {material_unknowns}"))

    return findings

