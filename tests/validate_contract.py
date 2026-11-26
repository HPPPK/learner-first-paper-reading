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
    "prerequisites limited to next reading": (
        r"\bteach only\b.{0,60}?\bprerequisites\b.{0,60}?\bneeded\b"
        r".{0,60}?\bnext (?:selected )?(?:reading|passage|section)\b",
    ),
    "return to source after teaching": (
        r"\bafter\b.{0,60}?\b(?:background|prerequisite)\b.{0,60}?"
        r"\breturn\b.{0,60}?\boriginal\b.{0,60}?\b(?:passage|paragraph|equation|figure|table)\b",
    ),
    "material background receives authoritative links": (
        r"\bwhen\b.{0,60}?\bexternal background\b.{0,60}?\bmaterially\b"
        r".{0,60}?\bprovide\b.{0,60}?\bdirect\b.{0,60}?\bauthoritative\b.{0,60}?\blink\b",
    ),
    "external material is labeled Background": (
        r"\blabel\b.{0,60}?\bexternal (?:material|knowledge|sources?|background)\b"
        r".{0,60}?\bbackground\b",
    ),
    "background stays separate from focal evidence": (
        r"\bkeep\b.{0,60}?\bexternal background\b.{0,60}?\bseparate from\b"
        r".{0,60}?\bfocal paper(?:'s)?\b.{0,60}?\bevidence\b",
    ),
    "authoritative sources rank above blogs": (
        r"\bprefer\b.{0,300}?\boriginal papers?\b.{0,300}?\bpublisher\b"
        r".{0,300}?\bofficial code\b.{0,300}?\btextbooks?\b"
        r".{0,300}?\buniversity\b.{0,100}?\bover\b.{0,60}?\bblogs?\b",
    ),
    "learning request defaults to guided learning": (
        r"\bwhen\b.{0,40}?\b(?:learner|user)\b.{0,40}?\basks? to learn\b"
        r".{0,100}?\bguided learning\b.{0,40}?\b(?:is|as) the default\b",
    ),
    "focused explanations receive a direct response": (
        r"\b(?:focused|direct) explanations?\b.{0,100}?"
        r"\bdisclose\b.{0,60}?\b(?:brief |short )?route\b.{0,80}?"
        r"\banswer directly\b.{0,40}?\bsame response\b.{0,80}?"
        r"\bwithout\b.{0,40}?\b(?:learner |reading |agreement )?pause\b",
    ),
    "non-interactive reports receive a direct response": (
        r"\bnon-interactive reports?\b.{0,100}?"
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


def has_explanation_layer_instruction(text, layer):
    """Check substantive directives in one layer, excluding its heading.

    This bounded coverage matcher is intentionally conservative, not a general
    natural-language parser. Each required relationship must occur in this body;
    a worked example or instruction in another layer cannot supply it.
    """
    prose = " ".join(re.sub(r"[*_`]", "", text.lower()).split())
    _, separator, body = prose.partition(":")
    body = body.strip()
    if not separator or re.search(
        r"(?:^|[.;]\s+)(?:do not|don't|never|skip|omit|avoid|ignore|withhold|leave)\b|"
        r"\b(?:optional|unnecessary|irrelevant|not required)\b",
        body,
    ):
        return False
    rules = {
        "mechanism": (
            r"\b(?:describe|explain|trace)\b.{0,60}\b(?:what enters|inputs?)\b"
            r".{0,100}\b(?:what changes|transformation|operations?|steps?)\b"
            r".{0,100}\b(?:what comes out|outputs?)\b",
        ),
        "example": (
            r"\b(?:give|provide|use|work through)\b.{0,60}"
            r"\b(?:hand[- ]checkable|small|minimal|toy|worked)\b"
            r".{0,60}\b(?:example|diagram|pipeline)\b",
            r"\b(?:show|calculate|trace)\b.{0,60}\bintermediate (?:operations|steps|values)\b"
            r".{0,100}\b(?:result|resulting value|resulting change)\b",
        ),
        "precision": (
            r"\b(?:define|specify)\b.{0,60}\b(?:symbols|notation)\b"
            r".{0,100}\b(?:dimensions|units)\b.{0,100}\b(?:operation|equation)\b",
            r"\b(?:state|identify|explain)\b.{0,60}\b(?:conditions|assumptions)\b"
            r".{0,100}\b(?:accurate|holds|valid)\b",
        ),
        "paper role": (
            r"\b(?:connect|relate)\b.{0,60}\bconcept\b.{0,60}\binspected\b"
            r".{0,40}\b(?:focal[- ]paper|paper)\b.{0,40}\b(?:anchor|section|passage)\b"
            r".{0,100}\b(?:design choice|reasoning|method)\b",
            r"\b(?:mark|state)\b.{0,40}\brole\b.{0,30}\bunknown\b"
            r".{0,30}\b(?:if|when)\b.{0,80}\b(?:absent|uninspected|unavailable)\b",
        ),
        "boundary": (
            r"\b(?:state|explain|identify)\b.{0,60}\bassumptions\b"
            r".{0,100}\b(?:approximation error|failure cases|limits)\b",
            r"\bwhat\b.{0,80}\bdoes not establish\b|"
            r"\bidentify\b.{0,80}\bconclusions\b.{0,40}\bunsupported\b",
        ),
    }
    return all(re.search(pattern, body) for pattern in rules[layer])


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


def task4_contract_errors(text, contract):
    """Conservative directive coverage; this does not establish agent behavior.

    Each pattern encodes an action and its object/condition. Headings alone
    cannot satisfy it. Scenario evaluation must still test the consuming agent.
    """
    prose = " ".join(re.sub(r"[*_`]", "", text.lower()).split())
    rules = {
        "evidence": {
            "Paper attribution": r"paper: attribute.{0,90}explicit.{0,90}inspected.{0,50}anchor",
            "Background attribution": r"background: attribute.{0,100}external.{0,100}authoritative.{0,50}link",
            "Analyst attribution": r"analyst: mark.{0,100}(?:inference|interpretation).{0,70}your own",
            "Unknown attribution": r"unknown: state.{0,100}available evidence does not establish",
            "claim evidence boundary connection": r"for each load-bearing claim, record.{0,100}anchor.{0,160}evidence.{0,160}direct observation.{0,160}support strength.{0,160}conditions.{0,160}alternative explanations.{0,160}unknowns",
            "unit check": r"identify.{0,70}unit of analysis.{0,140}independent.{0,140}repeated.{0,140}uncertainty",
            "fair comparison": r"compare.{0,70}baselines.{0,140}split.{0,140}preprocessing.{0,140}metric.{0,140}tuning.{0,140}compute",
            "guided gate": r"in guided mode, enter reviewer-style critique only after the learner can accurately reconstruct.{0,80}question.{0,80}method.{0,80}evidence.{0,80}scope",
            "failed gate": r"if comprehension is incomplete, defer.{0,80}paper-specific.{0,80}criticism.{0,140}one.{0,70}question",
            "evidence-tied criticism": r"tie every criticism to.{0,100}inspected.{0,80}evidence or.{0,80}missing detail",
            "no flaw quota": r"do not invent.{0,80}(?:flaws|defects).{0,80}quota",
        },
        "visual": {
            "original before description": r"inspect the original.{0,50}(?:figure|table).{0,100}before.{0,70}describ",
            "unavailable disclosure": r"if.{0,70}(?:unreadable|unavailable).{0,100}disclose.{0,140}(?:cannot|cannot be).{0,70}(?:check|read|observe)",
            "no fabricated observations": r"do not invent.{0,70}(?:visual )?observations",
            "purpose": r"1\. purpose: identify.{0,100}(?:question|comparison)",
            "encoding": r"2\. axes/units/legend: read.{0,140}axes.{0,100}units.{0,100}legend.{0,100}table",
            "literal before interpretation": r"3\. literal observations: describe.{0,140}(?:values|patterns).{0,140}separate.{0,100}interpretation",
            "author interpretation": r"4\. author interpretation: attribute.{0,140}authors.{0,100}(?:caption|text)",
            "supported claim": r"5\. supported claim: connect.{0,100}observation.{0,100}anchored claim",
            "boundary": r"6\. boundary: state.{0,100}(?:conditions|limits).{0,100}does not establish",
        },
        "equation": {
            "purpose": r"1\. purpose: explain.{0,100}(?:problem|need).{0,100}equation",
            "symbols and dimensions": r"2\. symbols and dimensions: define.{0,100}symbol.{0,100}(?:shape|dimension).{0,100}units",
            "operation": r"3\. operation: trace.{0,100}inputs.{0,100}(?:operations|steps).{0,100}outputs",
            "worked example": r"4\. hand-checkable example: give.{0,100}(?:small|toy|numerical).{0,100}intermediate.{0,100}result",
            "assumptions": r"5\. assumptions: state.{0,100}(?:conditions|assumptions).{0,100}(?:valid|holds)",
            "paper role": r"6\. paper role: connect.{0,100}inspected.{0,100}(?:anchor|equation).{0,100}(?:method|derivation)",
            "conditional implementation": r"7\. code mapping when relevant: when.{0,100}(?:implementation|code|reproduction).{0,100}map.{0,100}(?:symbol|operation).{0,100}(?:file|function).{0,100}(?:shape|dimension)",
        },
        "reproduction": {
            "no binary collapse": r"keep exactly these six states distinct.{0,200}do not collapse.{0,100}reproduced/not-reproduced",
            "evidence transition": r"advance.{0,100}state only when.{0,100}evidence.{0,100}inspected.{0,150}unverified",
            "independent state support": r"a later state does not automatically establish earlier states",
            "smoke is 3 only": r"(?:forward/shape|forward) smoke test supports state 3 only",
            "user execution attribution": r"label user-reported execution.{0,100}reported.{0,140}independently verified execution.{0,140}inspected.{0,100}(?:logs|run)",
            "single metric boundary": r"one matching metric does not establish full reproduction",
            "alignment before training": r"before training, check.{0,100}paper.{0,100}code.{0,100}data.{0,100}protocol",
        },
        "note": {
            "learner ownership": r"learner-owned.{0,160}optional",
            "learner before AI": r"record your own interpretation before.{0,70}ai synthesis",
            "unanswered remains": r"keep unanswered fields.{0,80}unanswered.{0,100}unresolved questions.{0,100}remain",
            "claims anchored": r"claim.{0,80}anchor.{0,100}evidence.{0,100}observation.{0,100}boundary.{0,100}unknown",
            "questions": r"questions i still have",
        },
    }
    def affirmative_match(pattern):
        for match in re.finditer(pattern, prose):
            prefix = prose[max(0, match.start() - 30):match.start()]
            if not re.search(r"(?:do not|never|skip|optional to)\s*$", prefix):
                return True
        return False

    return [label for label, pattern in rules[contract].items() if not affirmative_match(pattern)]


def reproduction_state_errors(text):
    """Check affirmative evidence duties and state-specific inference limits."""
    rows = re.findall(r"^\|\s*(\d+)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*$", text, re.MULTILINE)
    expected = (
        ("conceptual understanding", r"^explain\b.*question.*method.*evidence.*scope", r"execution"),
        ("paper-to-code mapping", r"^inspect\b.*anchor.*file.*operation.*shape", r"run"),
        ("forward/shape validation", r"^inspect\b.*input.*output.*finite.*log", r"^this does not establish\b.*training.*metric"),
        ("small-scale training", r"^inspect\b.*data.*loss.*update.*checkpoint", r"benchmark"),
        ("metric consistency with the paper", r"^inspect\b.*split.*preprocessing.*metric.*tolerance.*result", r"^one matching (?:setting or metric|setting|metric) does not establish full reproduction\b"),
        ("full reproduction across reported settings", r"^inspect\b.*all.*settings.*seeds.*uncertainty.*deviations", r"scope"),
    )
    errors = []
    if [row[0] for row in rows] != list("123456"):
        return ["exactly six numbered state rows in order"]
    for row, (name, evidence, boundary) in zip(rows, expected):
        _, actual_name, actual_evidence, actual_boundary = (part.strip().lower() for part in row)
        if actual_name != name or not re.search(evidence, actual_evidence) or not re.search(boundary, actual_boundary):
            errors.append(f"state {row[0]} needs its distinct name, evidence, and boundary")
    return errors


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

    def test_focused_explanations_do_not_get_a_fake_pause(self):
        self.assertTrue(
            has_positive_relationship(self.entrypoint(), "focused explanations receive a direct response"),
            "Focused explanations need route disclosure and a direct answer without a learner pause",
        )

    def test_noninteractive_reports_do_not_get_a_fake_pause(self):
        self.assertTrue(
            has_positive_relationship(self.entrypoint(), "non-interactive reports receive a direct response"),
            "Non-interactive reports need route disclosure and a direct answer without a learner pause",
        )

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

    def test_explanation_has_ordered_mechanism_first_layers(self):
        path = ROOT / "references/explanation-standard.md"
        self.assertTrue(path.is_file(), "Prerequisite teaching requires the explanation reference")
        explanation = path.read_text(encoding="utf-8")
        # Detect omitted/reordered teaching stages, without fixing their wording.
        stages = (
            r"problem|technical need",
            r"plain[- ]language mechanism|plain mechanism",
            r"minimal (?:worked )?example",
            r"precise (?:definition|version|statement)",
            r"(?:focal )?paper role|role in (?:the )?(?:focal )?paper",
            r"boundary|assumptions and limits",
            r"further reading",
        )
        numbered = re.findall(r"^\d+\.\s+(.+)$", explanation, re.MULTILINE)
        self.assertGreaterEqual(len(numbered), len(stages), "All seven teaching layers are required")
        for index, pattern in enumerate(stages):
            with self.subTest(layer=index + 1):
                self.assertRegex(numbered[index].lower(), pattern)
        for index, layer in (
            (1, "mechanism"),
            (2, "example"),
            (3, "precision"),
            (4, "paper role"),
            (5, "boundary"),
        ):
            with self.subTest(substantive_layer=layer):
                self.assertTrue(
                    has_explanation_layer_instruction(numbered[index], layer),
                    f"Layer {layer} needs substantive positive instructions in its own body",
                )
        self.assert_concepts(" ".join(explanation.split()), {
            "capable beginner calibration": r"capable beginner",
            "hand-checkable example": r"hand[- ]checkable|calculate.{0,50}by hand",
            "translation alone is insufficient": r"(?:translation[- ]only|translation alone).{0,100}(?:insufficient|incomplete)",
            "childish analogy alone is insufficient": r"childish analog(?:y|ies).{0,100}(?:insufficient|incomplete)",
            "correct answers permit progress": r"technically correct.{0,180}(?:move|progress|continue)",
            "links have a material-value condition": r"(?:omit|skip).{0,70}links?.{0,100}(?:adds? no value|no explanatory value)",
        })
        for relationship in (
            "prerequisites limited to next reading",
            "return to source after teaching",
            "material background receives authoritative links",
        ):
            with self.subTest(relationship=relationship):
                self.assertTrue(has_positive_relationship(explanation, relationship))

    def test_source_quality_checks_identity_access_and_provenance(self):
        path = ROOT / "references/source-quality.md"
        self.assertTrue(path.is_file(), "Source provenance requires the source-quality reference")
        source = path.read_text(encoding="utf-8")
        self.assert_concepts(" ".join(source.split()), {
            "paper identity": r"title.{0,40}authors",
            "version identity": r"version.{0,40}date",
            "publication status": r"publication status",
            "full text access": r"full[- ]text",
            "abstract-only access": r"abstract[- ]only",
            "inspected coverage": r"(?:record|state|disclose).{0,80}(?:inspected|coverage)",
            "access failures disclosed": r"(?:disclose|state).{0,80}(?:access limits|unavailable|blocked|unreadable)",
            "stable direct links": r"stable.{0,40}direct link|direct.{0,40}stable link",
            "primary technical sources": r"primary sources.{0,80}technical claims",
            "inspect supporting passage": r"(?:inspect|read).{0,80}(?:passage|section).{0,80}(?:supports?|supporting)",
            "abstract cannot establish full reading": r"abstract[- ]only.{0,150}(?:unverified|unknown)",
        })
        for relationship in (
            "external material is labeled Background",
            "background stays separate from focal evidence",
            "authoritative sources rank above blogs",
        ):
            with self.subTest(relationship=relationship):
                self.assertTrue(has_positive_relationship(source, relationship))

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

    def test_readme_provides_installation_usage_and_honest_scope(self):
        path = ROOT / "README.md"
        self.assertTrue(path.is_file(), "Public installation guidance requires README.md")
        readme = path.read_text(encoding="utf-8")
        prose = " ".join(readme.lower().split())
        self.assertIn("https://github.com/HPPPK/norman-skill", readme)
        for label, pattern in {
            "Codex destination": r"~/\.codex/skills/learner-first-paper-reading",
            "Claude-compatible destination": r"~/\.claude/skills/learner-first-paper-reading",
            "fork subdirectory source": r"\./learner-first-paper-reading",
            "explicit invocation": r"\$learner-first-paper-reading",
            "automatic discovery": r"automatic discovery.{0,140}(?:host|client)",
            "optional Norman integration": r"norman.{0,160}optional|optional.{0,160}norman",
            "independent fallback": r"works without norman",
            "upstream license exclusion": r"does not (?:apply to|cover).{0,120}(?:upstream|sibling)",
            "testing boundary": r"static.{0,120}(?:cannot|does not).{0,100}(?:behavior|learning)",
        }.items():
            with self.subTest(requirement=label):
                self.assertRegex(prose, pattern)
        for mode in ("guided learning", "quick orientation", "deep evidence review",
                     "implementation/reproduction", "focused explanation"):
            with self.subTest(mode=mode):
                self.assertIn(mode, prose)

    def test_install_commands_enter_clone_or_main_archive_root(self):
        readme = self.read("README.md")
        blocks = re.findall(r"```(bash|powershell)\n(.*?)```", readme, re.DOTALL)
        routes = (
            ("bash", "git clone ", "cd norman-skill"),
            ("bash", "unzip norman-skill-main.zip", "cd norman-skill-main"),
            ("powershell", "Expand-Archive ", "Set-Location norman-skill-main"),
        )
        for language, acquisition, enter_root in routes:
            with self.subTest(language=language, acquisition=acquisition):
                matching = [body for label, body in blocks
                            if label == language and acquisition in body]
                self.assertTrue(matching, f"Missing {language} acquisition commands: {acquisition}")
                self.assertRegex(matching[0], rf"(?m)^{re.escape(enter_root)}$")
        self.assertIn("https://github.com/HPPPK/norman-skill/archive/refs/heads/main.zip", readme)
        for host in ("agents", "claude"):
            self.assertIn(
                f"cp -R ./learner-first-paper-reading ~/.{host}/skills/learner-first-paper-reading",
                readme,
            )
        self.assertEqual(readme.count(
            "Copy-Item -LiteralPath .\\learner-first-paper-reading -Destination $destination -Recurse"
        ), 2, "Both Windows host examples must copy from the selected repository root")

    def test_acknowledgments_credit_every_source_and_its_license_status(self):
        path = ROOT / "ACKNOWLEDGMENTS.md"
        self.assertTrue(path.is_file(), "Public attribution requires ACKNOWLEDGMENTS.md")
        acknowledgments = path.read_text(encoding="utf-8")
        self.assertRegex(acknowledgments, r"N同学|耐心的N同学")
        self.assertRegex(acknowledgments.lower(), r"wording and organization.{0,80}original")
        rows = [line for line in acknowledgments.splitlines() if line.startswith("|")]
        for repo, skill, license_name in (
            ("v0lka/skills", "study-paper", "MIT"),
            ("CUTEPKQ/paper-reading", "paper-reading", "MIT"),
            ("bytedance/deer-flow", "academic-paper-review", "MIT"),
            ("ShaishavMaisuria/research-paper-lifecycle-skills", "verify-results", "Apache-2.0"),
        ):
            with self.subTest(inspiration=skill):
                matching_rows = [row for row in rows if f"https://github.com/{repo}" in row and skill in row]
                self.assertTrue(matching_rows, f"Link and identify {skill} in its attribution row")
                self.assertTrue(any(license_name in row and "/LICENSE" in row for row in matching_rows),
                                f"Identify and link the known {license_name} license for {skill}")
        self.assertRegex(
            " ".join(acknowledgments.lower().split()),
            r"no standard repository license.{0,100}(?:found|identified)",
            "Do not invent an upstream Norman license",
        )

    def test_all_production_markdown_relative_links_resolve(self):
        for relative in PRODUCTION_FILES:
            if not relative.endswith(".md") or not (ROOT / relative).is_file():
                continue
            path = ROOT / relative
            for target in re.findall(r"\[[^\]]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)",
                                     path.read_text(encoding="utf-8")):
                parts = urlsplit(target.strip("<>"))
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                with self.subTest(file=relative, target=target):
                    resolved = (path.parent / unquote(parts.path)).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT), "Keep package links portable inside the skill")
                    self.assertTrue(resolved.exists(), f"Broken relative link: {relative} -> {target}")

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

    def test_teaching_and_source_rules_require_instruction_relationships(self):
        cases = {
            "prerequisites limited to next reading": "Teach only the prerequisites needed for the next selected reading.",
            "return to source after teaching": "After the background detour, return to the original passage.",
            "material background receives authoritative links": "When external background materially improves understanding, provide a direct authoritative link.",
            "external material is labeled Background": "Label external material as Background.",
            "background stays separate from focal evidence": "Keep external background separate from the focal paper's evidence.",
            "authoritative sources rank above blogs": "Prefer original papers, publisher pages, official code, textbooks, and university material over blogs.",
        }
        for relationship, instruction in cases.items():
            with self.subTest(relationship=relationship):
                self.check_cases(relationship, (
                    ("positive", instruction, True),
                    ("negated", "Do not " + instruction.lower(), False),
                    ("keywords only", relationship, False),
                ))

    def test_explanation_layer_bodies_require_substantive_instructions(self):
        # Retain every heading while mutating only its instruction body.
        # Alternate positives keep these checks from requiring exact guide prose.
        cases = {
            "mechanism": (
                "Plain-language mechanism",
                "Describe what enters, what changes step by step, and what comes out.",
                "Trace the inputs through the transformation to the outputs.",
                "Inputs, operations, outputs.",
                "Do not describe what enters, what changes step by step, and what comes out.",
            ),
            "example": (
                "Minimal worked example",
                "Give a hand-checkable numerical example. Show intermediate operations and the resulting value.",
                "Provide a small toy pipeline. Calculate intermediate steps and the result.",
                "Hand-checkable example, intermediate operations, result.",
                "Give a hand-checkable numerical example. Skip intermediate operations and assert the result.",
            ),
            "precision": (
                "Precise definition",
                "Define symbols, dimensions, units, and the formal equation. State the conditions under which the explanation is accurate.",
                "Specify notation, units, and the operation. Explain the assumptions under which it holds.",
                "Symbols, dimensions, units, formal equation, conditions, accurate.",
                "Do not define symbols, dimensions, units, or the formal equation. State the conditions under which the explanation is accurate.",
            ),
            "paper role": (
                "Paper role",
                "Connect the concept to an inspected focal-paper anchor and the design choice it explains. Mark the role Unknown if the paper is absent.",
                "Relate the concept to an inspected paper section and its method. State the role Unknown when the passage is uninspected.",
                "Concept, inspected focal-paper anchor, design choice, role Unknown, paper absent.",
                "Connect the concept to an uninspected focal-paper anchor and invent the design choice. Mark the role known if the paper is absent.",
            ),
            "boundary": (
                "Boundary",
                "State assumptions, approximation error, failure cases, and what the example does not establish.",
                "Explain assumptions and failure cases; identify which conclusions remain unsupported.",
                "Assumptions, approximation error, failure cases, unsupported conclusions.",
                "State assumptions, approximation error, failure cases, and what the example does not establish only as optional material.",
            ),
        }
        for layer, (heading, positive, alternate, keywords, contrary) in cases.items():
            for label, body, expected in (
                ("positive", positive, True),
                ("alternate positive", alternate, True),
                ("empty heading", "", False),
                ("keyword-only body", keywords, False),
                ("contrary instruction", contrary, False),
            ):
                with self.subTest(layer=layer, case=label):
                    text = f"2. **{heading}:** {body}"
                    self.assertEqual(has_explanation_layer_instruction(text, layer), expected)

    def test_learning_default_requires_the_learning_condition(self):
        self.check_cases("learning request defaults to guided learning", (
            ("positive", "When a learner asks to learn a paper, guided learning is the default mode.", True),
            ("unconditional", "Guided learning is the default mode for every request.", False),
            ("negated", "When a learner asks to learn, guided learning is not the default mode.", False),
        ))

    def test_direct_route_requires_answering_without_a_pause(self):
        common_cases = (
            ("positive", "For focused explanations or non-interactive reports, disclose a brief route and answer directly in the same response without a learner pause.", True),
            ("fake pause", "For focused explanations or non-interactive reports, disclose a brief route and wait for the learner to answer before proceeding.", False),
            ("omitted disclosure", "For focused explanations or non-interactive reports, answer directly in the same response without a learner pause.", False),
        )
        for relationship in (
            "focused explanations receive a direct response",
            "non-interactive reports receive a direct response",
        ):
            with self.subTest(relationship=relationship):
                self.check_cases(relationship, common_cases)

    def test_report_route_rejects_split_explanation_and_report_behavior(self):
        split_behavior = (
            "For focused explanations, disclose a brief route and answer directly "
            "in the same response without a learner pause. "
            "For explicit non-interactive reports, disclose a brief route and "
            "require a learner pause before proceeding."
        )
        self.assertTrue(has_positive_relationship(
            split_behavior, "focused explanations receive a direct response",
        ))
        self.assertFalse(has_positive_relationship(
            split_behavior, "non-interactive reports receive a direct response",
        ))

    def test_direct_routes_cannot_borrow_the_other_categorys_instruction(self):
        focused_only = "For direct explanations, disclose a brief route and answer directly in the same response without a learner pause."
        report_only = "For explicit non-interactive reports, disclose a brief route and answer directly in the same response without a learner pause."
        self.check_cases("focused explanations receive a direct response", (
            ("focused only", focused_only, True),
            ("report only", report_only, False),
        ))
        self.check_cases("non-interactive reports receive a direct response", (
            ("focused only", focused_only, False),
            ("report only", report_only, True),
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


class Task4ContentContracts(unittest.TestCase):
    """Static coverage for evidence relationships; fresh scenarios test behavior."""

    def content(self, relative):
        path = ROOT / relative
        self.assertTrue(path.is_file(), f"Task 4 requires {relative}")
        return path.read_text(encoding="utf-8")

    def assert_contract(self, text, contract):
        self.assertEqual(task4_contract_errors(text, contract), [], f"Incomplete {contract} instructions")

    def test_evidence_voices_mapping_and_guided_review_gate(self):
        evidence = self.content("references/evidence-and-review.md")
        self.assert_contract(evidence, "evidence")

    def test_figures_require_original_inspection_and_ordered_evidence_reading(self):
        visual = self.content("references/figures-and-equations.md")
        self.assert_contract(visual, "visual")
        self.assertEqual(
            re.findall(r"^(\d+)\. ", visual, re.MULTILINE),
            list("1234561234567"),
            "Visual and equation steps must retain their teaching order",
        )

    def test_equations_require_operation_example_and_conditional_code_mapping(self):
        equations = self.content("references/figures-and-equations.md")
        self.assert_contract(equations, "equation")

    def test_reproduction_preserves_six_evidence_bounded_states(self):
        reproduction = self.content("references/reproduction-levels.md")
        self.assert_contract(reproduction, "reproduction")
        self.assertEqual(reproduction_state_errors(reproduction), [])

    def test_optional_note_starts_with_learner_interpretation_and_keeps_unknowns(self):
        note = self.content("assets/reading-note-template.md")
        self.assert_contract(note, "note")
        sections = re.findall(r"^## (.+)$", note, re.MULTILINE)
        self.assertTrue(sections)
        self.assertIn("my interpretation", sections[0].lower())
        self.assertLess(note.index("## My interpretation"), note.index("## AI synthesis"))

    def test_negative_mutations_cannot_keep_headings_and_remove_relationships(self):
        cases = (
            ("references/evidence-and-review.md", "evidence", "only after the learner can accurately reconstruct", "before the learner can accurately reconstruct", "guided gate"),
            ("references/evidence-and-review.md", "evidence", "Background: Attribute", "Background: Mention", "Background attribution"),
            ("references/evidence-and-review.md", "evidence", "Tie every criticism to", "List criticisms without", "evidence-tied criticism"),
            ("references/figures-and-equations.md", "visual", "Inspect the original", "Do not inspect the original", "original before description"),
            ("references/figures-and-equations.md", "visual", "3. Literal observations: Describe", "3. Literal observations: Mention", "literal before interpretation"),
            ("references/figures-and-equations.md", "equation", "4. Hand-checkable example: Give", "4. Hand-checkable example: Omit", "worked example"),
            ("references/figures-and-equations.md", "equation", "7. Code mapping when relevant: When", "7. Code mapping when relevant: Ignore when", "conditional implementation"),
            ("references/reproduction-levels.md", "reproduction", "smoke test supports state 3 only", "smoke test supports state 6", "smoke is 3 only"),
            ("references/reproduction-levels.md", "reproduction", "Label user-reported execution", "Ignore user-reported execution", "user execution attribution"),
            ("assets/reading-note-template.md", "note", "Record your own interpretation before", "Record your own interpretation after", "learner before AI"),
        )
        for relative, contract, original, replacement, missing in cases:
            with self.subTest(mutation=missing):
                text = " ".join(re.sub(r"[*_`]", "", self.content(relative)).split())
                self.assertIn(original, text, "Mutation fixture must actually change the source")
                mutated = text.replace(original, replacement, 1)
                self.assertIn(missing, task4_contract_errors(mutated, contract))

    def test_state_rows_reject_missing_evidence_and_merged_states(self):
        reproduction = self.content("references/reproduction-levels.md")
        # A heading plus six state names cannot supply transition evidence.
        empty_evidence = re.sub(r"(?m)^(\| [1-6] \| [^|]+\|)[^|]+", r"\1 Evidence ", reproduction)
        self.assertEqual(len(reproduction_state_errors(empty_evidence)), 6)
        missing_state = re.sub(r"(?m)^\| 5 \|.*\n", "", reproduction)
        self.assertEqual(reproduction_state_errors(missing_state), ["exactly six numbered state rows in order"])
        extra_state = reproduction + "\n| 7 | Extra state | Inspect extra evidence | Extra scope |\n"
        self.assertEqual(reproduction_state_errors(extra_state), ["exactly six numbered state rows in order"])

    def test_state_rows_reject_negated_inspection_and_reversed_inference_boundaries(self):
        reproduction = self.content("references/reproduction-levels.md")
        cases = (
            ("3", "This does not establish training", "This does establish training"),
            ("5", "One matching setting or metric does not establish full reproduction",
             "One matching setting or metric does establish full reproduction"),
            ("4", "Inspect a bounded data subset", "Do not inspect a bounded data subset"),
        )
        for state, original, replacement in cases:
            with self.subTest(state=state):
                self.assertIn(original, reproduction, "Mutation must change the actual guidance")
                mutated = reproduction.replace(original, replacement, 1)
                self.assertEqual(
                    reproduction_state_errors(mutated),
                    [f"state {state} needs its distinct name, evidence, and boundary"],
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
