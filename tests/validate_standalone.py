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

    def test_bilingual_pages_cross_link_and_share_core_claims(self) -> None:
        chinese_path = ROOT / "README.zh-CN.md"
        self.assertTrue(chinese_path.is_file(), "README.zh-CN.md must exist")
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = chinese_path.read_text(encoding="utf-8")
        self.assertRegex(english, r'href="README\.zh-CN\.md"[^>]*>简体中文</a>')
        self.assertRegex(chinese, r'href="README\.md"[^>]*>English</a>')
        for text in (english, chinese):
            self.assertIn("AI scaffolds. You read. Evidence decides.", text)
            self.assertIn("$learner-first-paper-reading", text)
            self.assertIn("37", text)
            self.assertIn("seven", text.lower() if text is english else text.replace("七", "seven"))
            self.assertIn("automatic discovery", text.lower())
            self.assertIn("learning outcomes", text.lower())

    def test_landing_pages_show_brand_visuals_and_fast_start(self) -> None:
        for name in ("README.md", "README.zh-CN.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("assets/hero.svg", text)
            self.assertIn("assets/workflow.svg", text)
            self.assertRegex(text, r"(?i)(quick start|快速开始)")
            self.assertRegex(text, r"(?i)(paper|论文).*(evidence|证据)")

    def test_svg_assets_are_accessible_and_brand_consistent(self) -> None:
        for name in ("hero.svg", "workflow.svg"):
            path = ROOT / "assets" / name
            self.assertTrue(path.is_file(), f"{name} must exist")
            text = path.read_text(encoding="utf-8")
            self.assertIn("<title", text)
            self.assertIn("<desc", text)
            self.assertIn('role="img"', text)
            self.assertIn("aria-labelledby=", text)
            self.assertIn("#07111F", text)
            self.assertIn("#42D3C5", text)
            self.assertIn("#F3B562", text)

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
