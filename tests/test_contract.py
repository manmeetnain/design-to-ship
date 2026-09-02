import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from design_to_ship.cli import main
from design_to_ship.contract import validate_project


ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    def test_showcase_contract_has_no_errors(self):
        project = json.loads((ROOT / "examples/focus-checkout.json").read_text())
        errors = [item for item in validate_project(project) if item.severity == "error"]
        self.assertEqual([], errors)

    def test_ready_requires_verification(self):
        project = json.loads((ROOT / "templates/project.json").read_text())
        project["verdict"] = "READY"
        codes = {item.code for item in validate_project(project)}
        self.assertIn("DTS017", codes)

    def test_unknown_reference_fails(self):
        project = json.loads((ROOT / "templates/project.json").read_text())
        project["requirements"][0]["evidence_ids"] = ["E-999"]
        codes = {item.code for item in validate_project(project)}
        self.assertIn("DTS008", codes)

    def test_library_search(self):
        output = StringIO()
        with redirect_stdout(output):
            result = main(["library", "patterns", "onboarding"])
        self.assertEqual(0, result)
        self.assertIn("onboarding", output.getvalue())

    def test_markdown_export(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "contract.md"
            result = main(["export", str(ROOT / "examples/beacon/project.json"), "--output", str(output)])
            self.assertEqual(0, result)
            self.assertIn("# Beacon incident queue", output.read_text())

if __name__ == "__main__":
    unittest.main()
