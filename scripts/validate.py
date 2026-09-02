#!/usr/bin/env python3
"""Dependency-free repository validator for Design to Ship."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{relative}: invalid JSON: {exc}")
        return {}


def check_skill() -> None:
    path = ROOT / "skills/design-to-ship/SKILL.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md: missing YAML frontmatter")
        return
    frontmatter = match.group(1)
    for key in ("name: design-to-ship", "description:"):
        if key not in frontmatter:
            fail(f"SKILL.md: missing {key}")
    if len(text.splitlines()) > 500:
        fail("SKILL.md: exceeds the 500-line progressive-disclosure limit")


def check_versions() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    for path in (".codex-plugin/plugin.json", ".cursor-plugin/plugin.json"):
        manifest = load_json(path)
        if manifest.get("version") != version:
            fail(f"{path}: version does not match VERSION")
        if manifest.get("name") != "design-to-ship":
            fail(f"{path}: unexpected plugin name")
    codex = load_json(".codex-plugin/plugin.json")
    if codex.get("skills") != "./skills/":
        fail(".codex-plugin/plugin.json: skills must point to ./skills/")
    cursor = load_json(".cursor-plugin/plugin.json")
    if cursor.get("skills") != "skills/":
        fail(".cursor-plugin/plugin.json: skills must point to skills/")
    if cursor.get("license") != "MIT":
        fail(".cursor-plugin/plugin.json: license must be MIT")


def check_project(relative: str) -> None:
    project = load_json(relative)
    required = {"project", "mode", "evidence", "requirements", "verdict"}
    missing = required - project.keys()
    if missing:
        fail(f"{relative}: missing {', '.join(sorted(missing))}")
    evidence_ids = {item.get("id") for item in project.get("evidence", [])}
    requirement_ids = {item.get("id") for item in project.get("requirements", [])}
    for requirement in project.get("requirements", []):
        unknown = set(requirement.get("evidence_ids", [])) - evidence_ids
        if unknown:
            fail(f"{relative}: requirement references unknown evidence {sorted(unknown)}")
    for decision in project.get("decisions", []):
        unknown = set(decision.get("requirement_ids", [])) - requirement_ids
        if unknown:
            fail(f"{relative}: decision references unknown requirements {sorted(unknown)}")


def check_evals() -> None:
    cases = load_json("evals/trigger-cases.json")
    for group in ("should_trigger", "should_not_trigger"):
        prompts = cases.get(group)
        if not isinstance(prompts, list) or len(prompts) < 5:
            fail(f"evals/trigger-cases.json: {group} needs at least five prompts")
        elif any(not isinstance(prompt, str) or not prompt.strip() for prompt in prompts):
            fail(f"evals/trigger-cases.json: {group} contains an empty prompt")


def check_links() -> None:
    link_pattern = re.compile(r"\[[^]]*]\((?!https?://|mailto:|#)([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            clean = target.split("#", 1)[0].replace("%20", " ")
            if clean and not (path.parent / clean).resolve().exists():
                fail(f"{path.relative_to(ROOT)}: broken local link {target}")


def check_required_files() -> None:
    paths = [
        "README.md",
        "LICENSE",
        "AGENTS.md",
        "skills/design-to-ship/SKILL.md",
        "skills/design-to-ship/agents/openai.yaml",
        "schemas/design-project.schema.json",
        ".github/workflows/validate.yml",
    ]
    for relative in paths:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")


def main() -> int:
    check_required_files()
    check_skill()
    check_versions()
    load_json("schemas/design-project.schema.json")
    check_project("templates/project.json")
    check_project("examples/focus-checkout.json")
    check_evals()
    check_links()
    if ERRORS:
        for error in ERRORS:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Design to Ship validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
