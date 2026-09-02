"""Command-line interface for Design to Ship."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

from .contract import Finding, validate_project


def _load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Project not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")


def _print_findings(findings: list[Finding]) -> None:
    if not findings:
        print("PASS: project contract is valid")
        return
    for finding in findings:
        print(f"{finding.severity.upper()} {finding.code}: {finding.message}")


def command_init(args: argparse.Namespace) -> int:
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    template = Path(__file__).resolve().parents[2] / "templates/project.json"
    target = output / "design-to-ship.json"
    if target.exists() and not args.force:
        raise SystemExit(f"Refusing to overwrite {target}; pass --force to replace it")
    shutil.copyfile(template, target)
    project = _load(target)
    project["project"] = args.name
    target.write_text(json.dumps(project, indent=2) + "\n", encoding="utf-8")
    print(target)
    return 0


def command_validate(args: argparse.Namespace) -> int:
    findings = validate_project(_load(Path(args.project)))
    _print_findings(findings)
    return 1 if any(item.severity == "error" for item in findings) else 0


def command_trace(args: argparse.Namespace) -> int:
    project = _load(Path(args.project))
    decisions = project.get("decisions", [])
    verifications = project.get("verifications", [])
    print("Requirement | Evidence | Decisions | Verification")
    print("--- | --- | --- | ---")
    for requirement in project.get("requirements", []):
        rid = requirement.get("id", "?")
        linked_decisions = [d.get("id") for d in decisions if rid in d.get("requirement_ids", [])]
        linked_verifications = [v.get("id") for v in verifications if rid in v.get("requirement_ids", [])]
        print(f"{rid} | {', '.join(requirement.get('evidence_ids', [])) or '—'} | {', '.join(linked_decisions) or '—'} | {', '.join(linked_verifications) or '—'}")
    return 0


def command_evidence(args: argparse.Namespace) -> int:
    source = Path(args.project).resolve()
    project = _load(source)
    findings = validate_project(project)
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    normalized = json.dumps(project, indent=2, sort_keys=True) + "\n"
    digest = hashlib.sha256(normalized.encode()).hexdigest()
    (output / "project.json").write_text(normalized, encoding="utf-8")
    report = [
        f"# Evidence bundle — {project.get('project', 'Untitled')}" ,
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Source: `{source}`",
        f"- SHA-256: `{digest}`",
        f"- Verdict: `{project.get('verdict', 'UNKNOWN')}`",
        "",
        "## Validation findings",
        "",
    ]
    report.extend(f"- **{item.severity.upper()} {item.code}:** {item.message}" for item in findings)
    if not findings:
        report.append("- No contract findings.")
    (output / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    (output / "manifest.json").write_text(json.dumps({"project_sha256": digest, "source": str(source), "files": ["project.json", "report.md"]}, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 1 if any(item.severity == "error" for item in findings) else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="design-to-ship", description="Validate traceable product-design contracts")
    from . import __version__
    parser.add_argument("--version", action="version", version=f"design-to-ship {__version__}")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="Create a project contract")
    init.add_argument("name")
    init.add_argument("--output", default=".")
    init.add_argument("--force", action="store_true")
    init.set_defaults(handler=command_init)

    validate = commands.add_parser("validate", help="Validate a project contract")
    validate.add_argument("project")
    validate.set_defaults(handler=command_validate)

    trace = commands.add_parser("trace", help="Print the traceability matrix")
    trace.add_argument("project")
    trace.set_defaults(handler=command_trace)

    evidence = commands.add_parser("evidence", help="Create a deterministic evidence bundle")
    evidence.add_argument("project")
    evidence.add_argument("--output", default="evidence-bundle")
    evidence.set_defaults(handler=command_evidence)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
