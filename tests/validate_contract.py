#!/usr/bin/env python3
"""Check packaging and instruction coverage with the Python standard library.

These static checks cannot establish agent behavior. Run the prompts in
scenarios.md in fresh contexts to evaluate the learning and provenance rules.
"""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = (
    "references/guided-reading-workflow.md",
    "references/explanation-standard.md",
    "references/evidence-and-review.md",
    "references/figures-and-equations.md",
    "references/reproduction-levels.md",
    "references/source-quality.md",
)
PRODUCTION_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    *REFERENCES,
    "assets/reading-note-template.md",
    "README.md",
    "ACKNOWLEDGMENTS.md",
    "LICENSE",
)

# These recognize explicit positive instruction clauses, not arbitrary mentions
# of the relevant words. They are conservative static coverage checks; scenarios
# remain the authority on whether an agent follows the instructions in practice.
RELATIONSHIPS = {
    "learning request defaults to guided learning": (
        r"\bwhen\b.{0,40}?\b(?:learner|user)\b.{0,40}?\basks? to learn\b"
        r".{0,100}?\bguided learning\b.{0,40}?\b(?:is|as) the default\b",
    ),
    "direct requests receive a direct response": (
        r"\b(?:focused explanations?|non-interactive reports?)\b.{0,100}?"
        r"\bdisclose\b.{0,60}?\b(?:brief |short )?route\b.{0,80}?"
        r"\banswer directly\b.{0,40}?\bsame response\b.{0,80}?"
        r"\bwithout\b.{0,40}?\b(?:learner |reading |agreement )?pause\b",
    ),
    "abstract access limits the reading plan": (
        r"\babstract-only access\b.{0,100}?\b(?:provide|offer|give)\b"
        r".{0,40}?\blimited reading plan\b.{0,100}?\bfull-paper claims\b"
        r".{0,40}?\b(?:unverified|unknown|unestablished)\b",
    ),
    "opening before substantive analysis": (
        r"\bfirst (?:user-facing |assistant )?(?:response|turn)\b.{0,60}?"
        r"\b(?:must|shall)\b.{0,60}?\b(?:explain|disclose|describe|present)\b"
        r".{0,500}?\bbefore (?:any )?substantive (?:paper )?(?:analysis|reading)\b",
        r"\bbefore (?:any )?substantive (?:paper )?(?:analysis|reading)\b"
        r".{0,100}?\bfirst (?:user-facing |assistant )?(?:response|turn)\b"
        r".{0,60}?\b(?:must|shall)\b.{0,60}?\b(?:explain|disclose|describe|present)\b",
    ),
    "guided route agreement before proceeding": (
        r"\bguided (?:mode|learning|session|reading)\b.{0,100}?"
        r"\b(?:obtain|require|wait for)\b.{0,60}?\b(?:learner|user)(?:'s)?\b"
        r".{0,60}?\bagreement\b.{0,60}?\b(?:route|plan|process)\b"
        r".{0,100}?\bbefore\b.{0,60}?\b(?:proceeding|proceed|starting|start|beginning|begin|analysis|reading)\b",
        r"\bguided (?:mode|learning|session|reading)\b.{0,100}?\bask\b"
        r".{0,60}?\b(?:learner|user)\b.{0,60}?\bagree\b.{0,60}?"
        r"\b(?:route|plan|process)\b.{0,100}?\b(?:pause|wait)\b"
        r".{0,100}?\b(?:before proceeding|before starting|until (?:they|the learner|the user) agree)\b",
    ),
    "accurate comprehension before critique": (
        r"\b(?:enter|begin|start|perform|allow|permit|proceed to)\b.{0,60}?"
        r"\b(?:critical review|reviewer(?:-style)? critique|critique)\b"
        r".{0,60}?\bonly after\b.{0,60}?\b(?:learner|user)\b.{0,60}?"
        r"\b(?:accurately (?:reconstruct|explain)|demonstrates? accurate (?:comprehension|understanding))\b",
        r"\b(?:learner|user)\b.{0,60}?\bmust\b.{0,60}?"
        r"\b(?:accurately (?:reconstruct|explain)|demonstrate accurate (?:comprehension|understanding))\b"
        r".{0,300}?\bbefore\b.{0,60}?\b(?:critical review|reviewer(?:-style)? critique|critique)\b",
    ),
}


def has_positive_relationship(text, relationship):
    """Find an affirmative ordering rule within one prose instruction sentence.

    Negated/optional clauses are deliberately not accepted as positive rules.
    This does not parse general natural language or prove behavioral compliance.
    """
    prose = re.sub(r"[*_`]", "", text.lower())
    sentences = re.split(r"(?<=[.!?])\s+|\n\s*\n", prose)
    for sentence in sentences:
        sentence = " ".join(sentence.split())
        if re.search(r"\b(?:not|never|optional|needn't|don't|cannot)\b", sentence):
            continue
        if any(re.search(pattern, sentence) for pattern in RELATIONSHIPS[relationship]):
            return True
    return False


def scalar(frontmatter, key):
    """Read a plain, quoted, or folded top-level scalar, without a YAML library."""
    lines = frontmatter.splitlines()
    for index, line in enumerate(lines):
        match = re.fullmatch(rf"{re.escape(key)}:\s*(.*?)\s*", line)
        if not match:
            continue
        value = match.group(1)
        if value in (">", ">-", ">+", "|", "|-", "|+"):
            continuation = []
            for following in lines[index + 1:]:
                if following and not following[0].isspace():
                    break
                continuation.append(following.strip())
            return " ".join(continuation).strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            return value[1:-1]
        return value
    return None


class SkillContract(unittest.TestCase):
    def entrypoint(self):
        path = ROOT / "SKILL.md"
        self.assertTrue(path.is_file(), "Entrypoint routing requires SKILL.md")
        return path.read_text(encoding="utf-8")

    def read(self, relative):
        path = ROOT / relative
        if not path.is_file():
            self.skipTest(f"Missing {relative}; reported by required-files check")
        return path.read_text(encoding="utf-8")

    def assert_concepts(self, text, concepts):
        for label, pattern in concepts.items():
            with self.subTest(concept=label):
                self.assertRegex(text.lower(), pattern, f"Missing contract concept: {label}")

    def test_required_files_exist_and_are_nonempty(self):
        for relative in (*PRODUCTION_FILES, "tests/scenarios.md"):
            with self.subTest(file=relative):
                path = ROOT / relative
                self.assertTrue(path.is_file(), f"Missing required file: {relative}")
                self.assertTrue(path.read_text(encoding="utf-8").strip(), f"Empty file: {relative}")

    def test_discovery_frontmatter(self):
        skill = self.read("SKILL.md")
        match = re.match(r"\A---\s*\n(.*?)\n---(?:\n|$)", skill, re.DOTALL)
        self.assertIsNotNone(match, "SKILL.md needs YAML frontmatter")
        metadata = match.group(1)
        self.assertEqual(scalar(metadata, "name"), "learner-first-paper-reading")
        description = scalar(metadata, "description")
        self.assertIsNotNone(description, "Frontmatter needs a description")
        self.assertTrue(description.startswith("Use when"), "Description must begin with 'Use when'")

    def test_all_six_reference_routes_resolve_inside_skill(self):
        skill = self.read("SKILL.md")
        links = re.findall(r"\[[^\]]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", skill)
        routes = set()
        for target in links:
            parts = urlsplit(target.strip("<>"))
            if parts.scheme or parts.netloc or not parts.path:
                continue
            relative = unquote(parts.path)
            resolved = (ROOT / relative).resolve()
            with self.subTest(link=target):
                self.assertTrue(resolved.is_relative_to(ROOT), "Local route escapes the skill directory")
                self.assertTrue(resolved.is_file(), f"Unresolved local link: {target}")
            if resolved.is_relative_to(ROOT):
                routes.add(resolved.relative_to(ROOT).as_posix())
        for reference in REFERENCES:
            with self.subTest(reference=reference):
                self.assertIn(reference, routes, f"SKILL.md must route to {reference}")

    def test_implicit_invocation_is_not_disabled(self):
        metadata = self.read("agents/openai.yaml")
        active_lines = "\n".join(line.split("#", 1)[0] for line in metadata.splitlines())
        self.assertNotRegex(
            active_lines.lower(),
            r"\ballow_implicit_invocation\s*:\s*[\"']?(?:false|no|off|0)\b",
            "Implicit invocation must remain enabled (omitting the policy is allowed)",
        )

    def test_learning_requests_default_to_the_linked_guided_workflow(self):
        skill = self.entrypoint()
        self.assertTrue(
            has_positive_relationship(skill, "learning request defaults to guided learning"),
            "An explicit request to learn must default to guided learning",
        )
        self.assertRegex(
            skill.lower(),
            r"guided learning[^\n]*\[[^\]]+\]\(references/guided-reading-workflow\.md\)",
            "The guided learning route must point to its workflow",
        )

    def test_focused_and_noninteractive_requests_do_not_get_a_fake_pause(self):
        skill = self.entrypoint()
        self.assertTrue(
            has_positive_relationship(skill, "direct requests receive a direct response"),
            "Direct requests need brief route disclosure followed by an answer in the same response",
        )
        self.assertRegex(skill.lower(), r"focused explanation")
        self.assertRegex(skill.lower(), r"non-interactive report")

    def test_abstract_only_access_limits_the_plan_and_claims(self):
        self.assertTrue(
            has_positive_relationship(self.entrypoint(), "abstract access limits the reading plan"),
            "Abstract-only access must limit the reading plan and leave full-paper claims unverified",
        )

    def test_opening_contract_is_in_routed_workflow(self):
        routed = self.read("SKILL.md") + "\n" + self.read(REFERENCES[0])
        for relationship in (
            "opening before substantive analysis",
            "guided route agreement before proceeding",
        ):
            with self.subTest(relationship=relationship):
                self.assertTrue(
                    has_positive_relationship(routed, relationship),
                    f"Missing explicit positive contract: {relationship}",
                )
        self.assert_concepts(routed, {
            "learner goal": r"goal",
            "starting level": r"beginner|starting level|prior knowledge|starting knowledge",
            "source identity": r"source|version",
            "session route": r"phase|stage|route",
            "assistant role": r"\bai\b|assistant",
            "learner role": r"learner",
            "reading or answer pauses": r"pause",
            "completion target": r"artifact|outcome|completion target|end of (?:the )?session",
            "missing source or decision": r"missing|unavailable|unresolved decision",
        })

    def test_four_voices_and_comprehension_gate_are_routed(self):
        evidence = self.read("references/evidence-and-review.md")
        self.assertTrue(
            has_positive_relationship(evidence, "accurate comprehension before critique"),
            "Critical review must explicitly follow demonstrated accurate comprehension",
        )
        self.assert_concepts(evidence, {
            "Paper voice": r"\bpaper\b",
            "Background voice": r"\bbackground\b",
            "Analyst voice": r"\banalyst\b",
            "Unknown voice": r"\bunknown\b",
            "source anchors": r"anchor|section|page",
            "external background sources": r"authoritative|textbook|original paper|official documentation",
        })

    def test_six_reproduction_levels_are_routed(self):
        reproduction = self.read("references/reproduction-levels.md")
        self.assert_concepts(reproduction, {
            "conceptual understanding": r"conceptual understanding",
            "paper-to-code mapping": r"paper[- ]to[- ]code mapping",
            "forward or shape validation": r"forward.{0,20}(?:validation|shape|smoke)|shape validation",
            "small-scale training": r"small[- ]scale training",
            "metric consistency": r"metric consistency",
            "full reproduction": r"full reproduction",
        })

    def test_license_and_acknowledgments_are_directory_scoped(self):
        license_text = self.read("LICENSE")
        readme = self.read("README.md")
        acknowledgments = self.read("ACKNOWLEDGMENTS.md")
        self.assertIn("MIT License", license_text)
        self.assertIn("Permission is hereby granted, free of charge", license_text)
        self.assertRegex(
            (license_text + "\n" + readme).lower(),
            r"(?:this|new|learner-first-paper-reading/?)[^\n.]{0,90}directory",
            "License or README must state the directory scope",
        )
        self.assertRegex(acknowledgments, r"N-tongxue/norman-skill|github\.com/N-tongxue/norman-skill")

    def test_production_files_have_no_unfinished_scaffolding(self):
        # Test prompts and evaluator records are excluded: they can quote defects.
        markers = re.compile(
            r"\b(?:TODO|TBD|FIXME)\b|\[INSERT[^\]]*\]|\[REPLACE[^\]]*\]|"
            r"your[- ]skill[- ]name|replace (?:this|with your)|generated scaffold|"
            r"write (?:your|the) (?:description|instructions) here",
            re.IGNORECASE,
        )
        for relative in PRODUCTION_FILES:
            with self.subTest(file=relative):
                path = ROOT / relative
                if path.is_file():
                    self.assertIsNone(markers.search(path.read_text(encoding="utf-8")), f"Unfinished marker in {relative}")


class ContractRelationshipChecks(unittest.TestCase):
    """Bounded self-checks for the static matchers, without production fixtures."""

    def check_cases(self, relationship, cases):
        for label, text, expected in cases:
            with self.subTest(case=label):
                self.assertEqual(has_positive_relationship(text, relationship), expected)

    def test_opening_requires_positive_before_relationship(self):
        self.check_cases("opening before substantive analysis", (
            ("positive", "The first user-facing response must explain the session route before substantive paper analysis.", True),
            ("omitted ordering", "Opening: the first response must explain the session route. Substantive paper analysis follows a plan.", False),
            ("reversed ordering", "The first user-facing response must explain the session route after substantive paper analysis.", False),
            ("negated rule", "The first user-facing response must not explain the route before substantive paper analysis.", False),
            ("keywords only", "Opening, first response, route, before, substantive analysis.", False),
        ))

    def test_learning_default_requires_the_learning_condition(self):
        self.check_cases("learning request defaults to guided learning", (
            ("positive", "When a learner asks to learn a paper, guided learning is the default mode.", True),
            ("unconditional", "Guided learning is the default mode for every request.", False),
            ("negated", "When a learner asks to learn, guided learning is not the default mode.", False),
        ))

    def test_direct_route_requires_answering_without_a_pause(self):
        self.check_cases("direct requests receive a direct response", (
            ("positive", "For focused explanations or non-interactive reports, disclose a brief route and answer directly in the same response without a learner pause.", True),
            ("fake pause", "For non-interactive reports, disclose a brief route and wait for the learner to answer before proceeding.", False),
            ("omitted disclosure", "For focused explanations, answer directly in the same response without a learner pause.", False),
        ))

    def test_abstract_route_requires_a_limited_plan_and_claim_boundary(self):
        self.check_cases("abstract access limits the reading plan", (
            ("positive", "With abstract-only access, provide a limited reading plan and label full-paper claims as unverified.", True),
            ("full plan", "With abstract-only access, provide a full reading plan and label full-paper claims as verified.", False),
            ("omitted boundary", "With abstract-only access, provide a limited reading plan.", False),
        ))

    def test_guided_agreement_requires_positive_before_relationship(self):
        self.check_cases("guided route agreement before proceeding", (
            ("positive", "In guided mode, obtain the learner's agreement on the route before proceeding.", True),
            ("positive ask and wait", "In guided learning, ask the learner to agree to the route and wait until they agree.", True),
            ("omitted agreement", "In guided mode, explain the route before proceeding.", False),
            ("reversed ordering", "In guided mode, obtain the learner's agreement on the route after proceeding.", False),
            ("negated rule", "In guided mode, do not require the learner's agreement on the route before proceeding.", False),
        ))

    def test_comprehension_requires_positive_before_critique_relationship(self):
        self.check_cases("accurate comprehension before critique", (
            ("positive only after", "Enter reviewer-style critique only after the learner can accurately reconstruct the question, method, evidence, and scope.", True),
            ("positive before", "The learner must demonstrate accurate comprehension before beginning critical review.", True),
            ("omitted ordering", "Check accurate comprehension. Perform critical review. Use a gate before the next section.", False),
            ("reversed ordering", "Perform critical review before the learner demonstrates accurate comprehension.", False),
            ("negated rule", "Do not enter reviewer-style critique only after the learner can accurately reconstruct the paper.", False),
        ))


if __name__ == "__main__":
    unittest.main(verbosity=2)
