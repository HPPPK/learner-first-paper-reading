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

EXAMPLE_FILES = (
    "examples/dlinear-guided-reading.md",
    "examples/focused-equation.md",
    "examples/reproduction-evidence.md",
)

GOVERNANCE_FILES = (
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
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
        standalone_source = Path(__file__).read_text(encoding="utf-8")
        contract_count = len(re.findall(r"^\s+def test_", contract_source, flags=re.MULTILINE))
        standalone_count = len(re.findall(r"^\s+def test_", standalone_source, flags=re.MULTILINE))
        self.assertEqual(37, contract_count, "Update this contract when core coverage changes")
        self.assertEqual(14, standalone_count, "Update this contract when project coverage changes")
        self.assertRegex(readme, rf"\b{contract_count}\b[^\n]*(?:contract|deterministic)")
        self.assertRegex(readme, rf"\b{standalone_count}\b[^\n]*standalone")

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

    def test_curated_examples_are_discoverable_and_evidence_labeled(self) -> None:
        index = (ROOT / "examples" / "README.md").read_text(encoding="utf-8")
        for relative in EXAMPLE_FILES:
            path = ROOT / relative
            self.assertTrue(path.is_file(), f"Missing curated example: {relative}")
            self.assertIn(path.name, index)
            text = path.read_text(encoding="utf-8")
            self.assertRegex(text, r"(?i)evidence status")
            for voice in ("Paper", "Background", "Analyst", "Unknown"):
                self.assertIn(voice, text, f"{relative} must demonstrate the {voice} voice")
        for readme in ("README.md", "README.zh-CN.md"):
            text = (ROOT / readme).read_text(encoding="utf-8")
            self.assertIn("examples/README.md", text)

    def test_examples_demonstrate_three_distinct_routes_without_inflated_claims(self) -> None:
        guided = (ROOT / EXAMPLE_FILES[0]).read_text(encoding="utf-8")
        self.assertIn("https://arxiv.org/abs/2205.13504", guided)
        self.assertRegex(guided, r"(?i)route agreement")
        self.assertRegex(guided, r"(?i)(reading assignment|read now)")
        self.assertRegex(guided, r"(?i)(illustrative|demonstration)")

        focused = (ROOT / EXAMPLE_FILES[1]).read_text(encoding="utf-8")
        self.assertIn("y = Wx + b", focused)
        self.assertRegex(focused, r"(?i)(worked|numerical).{0,80}example")
        self.assertRegex(focused, r"(?i)paper role.{0,120}unknown")

        reproduction = (ROOT / EXAMPLE_FILES[2]).read_text(encoding="utf-8")
        self.assertRegex(reproduction, r"(?i)reported state[- ]3")
        self.assertRegex(reproduction, r"(?i)full reproduction.{0,160}(?:unverified|not established)")
        for state in range(1, 7):
            self.assertRegex(reproduction, rf"(?i)state {state}\b")

    def test_contributor_and_release_files_enforce_evidence_boundaries(self) -> None:
        for relative in GOVERNANCE_FILES:
            self.assertTrue((ROOT / relative).is_file(), f"Missing governance file: {relative}")

        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        for phrase in (
            "behavior change",
            "validate_contract.py",
            "validate_standalone.py",
            "attribution",
            "fabricated paper anchors",
        ):
            self.assertIn(phrase, contributing.lower())

        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        changelog_prose = " ".join(changelog.lower().split())
        self.assertIn("[0.1.0]", changelog)
        self.assertRegex(changelog_prose, r"do(?:es)? not establish.{0,120}learning outcomes")
        self.assertRegex(changelog_prose, r"do(?:es)? not establish.{0,120}universal agent behavior")

        issue_text = "\n".join(
            (ROOT / relative).read_text(encoding="utf-8")
            for relative in GOVERNANCE_FILES[2:]
        ).lower()
        self.assertIn("evidence", issue_text)
        self.assertIn("source", issue_text)

    def test_ci_workflow_is_portable_and_runs_both_local_validators(self) -> None:
        workflow_path = ROOT / ".github" / "workflows" / "validate.yml"
        self.assertTrue(workflow_path.is_file())
        workflow = workflow_path.read_text(encoding="utf-8")
        for trigger in ("push:", "pull_request:", "workflow_dispatch:"):
            self.assertIn(trigger, workflow)
        for version in ('"3.9"', '"3.11"', '"3.13"'):
            self.assertIn(version, workflow)
        self.assertIn("runs-on: ubuntu-24.04", workflow)
        self.assertIn("python tests/validate_contract.py", workflow)
        self.assertIn("python tests/validate_standalone.py", workflow)
        self.assertNotRegex(workflow, r"(?i)(secret|token|curl |wget |pip install)")

    def test_bilingual_landing_pages_show_matching_project_badges(self) -> None:
        expected = (
            "actions/workflows/validate.yml/badge.svg",
            "img.shields.io/github/v/release/HPPPK/learner-first-paper-reading",
            "img.shields.io/github/license/HPPPK/learner-first-paper-reading",
            "img.shields.io/badge/Agent%20Skill-learner--first-42D3C5",
        )
        for name in ("README.md", "README.zh-CN.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            for badge in expected:
                self.assertIn(badge, text, f"{name} is missing badge {badge}")

    def test_public_examples_render_and_preserve_mathematical_precision(self) -> None:
        focused = (ROOT / "examples" / "focused-equation.md").read_text(encoding="utf-8")
        focused_prose = " ".join(focused.lower().split())
        self.assertIn("affine", focused.lower())
        self.assertRegex(focused_prose, r"linear only when.{0,30}b\s*=\s*0")
        self.assertNotIn("The mapping is linear in", focused)
        self.assertIn("$$", focused)
        self.assertNotIn(r"\[", focused)
        self.assertNotIn(r"\]", focused)

        evaluation = (ROOT / "tests" / "evaluation-results.md").read_text(encoding="utf-8")
        evaluation_prose = " ".join(evaluation.lower().split())
        self.assertRegex(evaluation_prose, r"historical.{0,120}former fork root")
        self.assertIn("python3 learner-first-paper-reading/tests/validate_contract.py", evaluation)


if __name__ == "__main__":
    unittest.main(verbosity=2)
