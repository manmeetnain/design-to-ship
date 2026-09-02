#!/usr/bin/env python3
"""Run the public Design to Ship contract benchmark."""

from __future__ import annotations

import json
from pathlib import Path

from design_to_ship.contract import validate_project

ROOT = Path(__file__).resolve().parent


def main() -> int:
    manifest = json.loads((ROOT / "cases.json").read_text(encoding="utf-8"))
    failed = 0
    for case in manifest["cases"]:
        project = json.loads((ROOT / "fixtures" / case["fixture"]).read_text(encoding="utf-8"))
        observed = sorted(item.code for item in validate_project(project) if item.severity == "error")
        expected = sorted(case["expected_errors"])
        passed = observed == expected
        print(f"{'PASS' if passed else 'FAIL'} {case['name']}: expected={expected} observed={observed}")
        failed += 0 if passed else 1
    print(f"{len(manifest['cases']) - failed}/{len(manifest['cases'])} benchmark cases passed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

