"""
Basic tests for the laya-africa-evals package.
"""

import unittest
import os
import json
from pathlib import Path

class TestLayaAfricaEvals(unittest.TestCase):
    """Test cases for the laya-africa-evals package."""

    def setUp(self):
        """Set up test fixtures."""
        self.package_dir = Path("laya_africa_evals")
        self.datasets_dir = Path("datasets")
        self.harness_dir = Path("harness")
        self.runners_dir = Path("runners")

    def test_package_exists(self):
        """Test that the main package directory exists."""
        self.assertTrue(self.package_dir.exists() and self.package_dir.is_dir(),
                       "laya_africa_evals package directory should exist")

    def test_init_file_exists(self):
        """Test that __init__.py exists in the package."""
        init_file = self.package_dir / "__init__.py"
        self.assertTrue(init_file.exists(), "__init__.py should exist in package")

    def test_datasets_directory_exists(self):
        """Test that datasets directory exists."""
        self.assertTrue(self.datasets_dir.exists() and self.datasets_dir.is_dir(),
                       "datasets directory should exist")

    def test_swahili_dataset_exists(self):
        """Test that Swahili dataset file exists."""
        swahili_file = self.datasets_dir / "swahili_triage.jsonl"
        self.assertTrue(swahili_file.exists(), "Swahili dataset should exist")

    def test_dataset_format(self):
        """Test that dataset files are valid JSONL."""
        swahili_file = self.datasets_dir / "swahili_triage.jsonl"
        with open(swahili_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if line.strip():  # Skip empty lines
                    try:
                        json.loads(line)
                    except json.JSONDecodeError:
                        self.fail(f"Line {i+1} in {swahili_file} is not valid JSON")

    def test_harness_directory_exists(self):
        """Test that harness directory exists."""
        self.assertTrue(self.harness_dir.exists() and self.harness_dir.is_dir(),
                       "harness directory should exist")

    def test_guard_harness_exists(self):
        """Test that guard harness module exists."""
        harness_file = self.harness_dir / "guard_harness.py"
        self.assertTrue(harness_file.exists(), "guard_harness.py should exist")

    def test_runners_directory_exists(self):
        """Test that runners directory exists."""
        self.assertTrue(self.runners_dir.exists() and self.runners_dir.is_dir(),
                       "runners directory should exist")

    def test_checkpoint_runners_exists(self):
        """Test that checkpoint runners module exists."""
        runners_file = self.runners_dir / "checkpoint_runners.py"
        self.assertTrue(runners_file.exists(), "checkpoint_runners.py should exist")

    def test_results_directory_exists(self):
        """Test that results directory exists."""
        results_dir = Path("results")
        self.assertTrue(results_dir.exists() and results_dir.is_dir(),
                       "results directory should exist")

    def test_mock_results_exists(self):
        """Test that mock results file exists."""
        mock_results = Path("results/mock_results.json")
        self.assertTrue(mock_results.exists(), "mock results file should exist")

    def test_mock_results_format(self):
        """Test that mock results file is valid JSON."""
        mock_results = Path("results/mock_results.json")
        with open(mock_results, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                self.assertIn("evaluation_summary", data)
                self.assertIn("dataset_results", data)
                self.assertIsInstance(data["dataset_results"], dict)
            except json.JSONDecodeError:
                self.fail("mock_results.json is not valid JSON")

    def test_readme_exists(self):
        """Test that README.md exists."""
        readme_file = Path("README.md")
        self.assertTrue(readme_file.exists(), "README.md should exist")

    def test_license_exists(self):
        """Test that LICENSE file exists."""
        license_file = Path("LICENSE")
        self.assertTrue(license_file.exists(), "LICENSE file should exist")

    def test_design_document_exists(self):
        """Test that DESIGN_DOCUMENT.md exists."""
        design_file = Path("DESIGN_DOCUMENT.md")
        self.assertTrue(design_file.exists(), "DESIGN_DOCUMENT.md should exist")

    def test_portfolio_case_study_exists(self):
        """Test that PORTFOLIO_CASE_STUDY.md exists."""
        case_study_file = Path("PORTFOLIO_CASE_STUDY.md")
        self.assertTrue(case_study_file.exists(), "PORTFOLIO_CASE_STUDY.md should exist")


if __name__ == '__main__':
    unittest.main()