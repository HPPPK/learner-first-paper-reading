#!/usr/bin/env python3
"""Deterministic contracts for the standalone project packaging."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_STANDALONE_FILES = (
    "README.zh-CN.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    ".github/workflows/validate.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    "assets/hero.svg",
    "assets/workflow.svg",
    "examples/README.md",
    "examples/dlinear-guided-reading.md",
    "examples/focused-equation.md",
    "examples/reproduction-evidence.md",
)


def markdown_relative_links(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [
        target.split("#", 1)[0]
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
        if target
        and not target.startswith(("http://", "https://", "mailto:", "#"))
    ]


class StandaloneProjectContracts(unittest.TestCase):
    def test_skill_is_promoted_to_repository_root(self) -> None:
        self.assertTrue((ROOT / "SKILL.md").is_file())
        self.assertTrue((ROOT / "references").is_dir())
        self.assertTrue((ROOT / "assets").is_dir())
        self.assertFalse((ROOT / "learner-first-paper-reading" / "SKILL.md").exists())

    def test_brand_and_public_project_files_exist(self) -> None:
        missing = [name for name in REQUIRED_STANDALONE_FILES if not (ROOT / name).is_file()]
        self.assertEqual([], missing, f"Missing standalone files: {missing}")

    def test_root_readme_uses_standalone_brand_and_repository(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("AI scaffolds. You read. Evidence decides.", readme)
        self.assertIn("HPPPK/learner-first-paper-reading", readme)
        self.assertNotIn("git clone https://github.com/HPPPK/norman-skill.git", readme)
        self.assertNotIn("norman-skill-main", readme)
        self.assertNotIn("./learner-first-paper-reading", readme)

    def test_readme_claims_current_contract_count(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        contract_source = (ROOT / "tests" / "validate_contract.py").read_text(encoding="utf-8")
        count = len(re.findall(r"^\s+def test_", contract_source, flags=re.MULTILINE))
        self.assertEqual(37, count, "Update this contract when deterministic coverage changes")
        self.assertRegex(readme, rf"\b{count}\b[^\n]*(?:contract|deterministic)")

    def test_production_markdown_relative_links_resolve(self) -> None:
        missing: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", ".superpowers"} for part in path.parts):
                continue
            for target in markdown_relative_links(path):
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    missing.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual([], missing, f"Broken relative links: {missing}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
