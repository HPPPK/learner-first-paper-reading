# Learner-First Paper Reading

An Agent Skill for learning to read a research paper with AI support. It is for
capable beginners who can reason carefully but may be new to the paper's field.
The aim is to explain the research question, method, evidence, and valid scope
in your own words.

This original skill lives in the `learner-first-paper-reading/` subdirectory of
[HPPPK/norman-skill](https://github.com/HPPPK/norman-skill), a fork of
[Norman-Skill](https://github.com/N-tongxue/norman-skill). See
[ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) for the upstream creator and inspirations.

## How a session works

The assistant first explains the proposed route, your role, its role, the source
available, pause points, and the intended outcome. In guided learning, you agree
on that route before teaching begins.

1. Learn only the prerequisites needed for the next selected passage, with a
   small worked example and precise assumptions.
2. Read the original section or visual and record your own interpretation.
3. Explain it back, one consequential question at a time. Correct answers allow
   progress; demonstrated gaps receive targeted teaching and a return to the source.
4. Connect claims to inspected evidence and boundaries. Begin reviewer criticism
   after you can reconstruct the question, method, evidence, and scope.
5. Finish with a closed-book explanation and explicit unresolved questions. If
   implementing the method, record the exact verification state separately.

Throughout, **Paper**, **Background**, **Analyst**, and **Unknown** distinguish the
paper's statements, external teaching material, AI interpretation, and missing
evidence. The optional [reading note](assets/reading-note-template.md) keeps your
initial answers before AI synthesis.

| Mode | Use it for |
| --- | --- |
| Guided learning (default for learning requests) | Stepwise original reading, prerequisite teaching, and teach-back. |
| Quick orientation | Source identity, a prerequisite map, a selective reading route, and a first question. |
| Deep evidence review | Claims, comparisons, uncertainty, and evidence-tied criticism after reconstruction. |
| Implementation/reproduction | Paper-to-code mapping and separate evidence for six verification states. |
| Focused explanation | One concept, passage, equation, figure, or table explained directly. |

For a focused explanation or explicit non-interactive report, the assistant
briefly discloses the route and answers in the same response. These requests
do not require an agreement pause or a pretend learner exchange.

## Install only this skill

Keep the complete subdirectory together, including `references/`, `assets/`, and
`agents/`. Copying `SKILL.md` alone loses required instructions. There are no
runtime scripts, bundled model, PDF engine, or API credentials in this skill.
The host supplies its normal file, PDF, browser, and optional execution tools.

Choose one acquisition route in an unused working directory. With Git installed,
these commands work in a macOS/Linux terminal or Windows PowerShell:

```bash
git clone https://github.com/HPPPK/norman-skill.git
cd norman-skill
```

Alternatively, download and extract the main-branch ZIP. Its root directory is
`norman-skill-main/`. On macOS/Linux:

```bash
curl -fL https://github.com/HPPPK/norman-skill/archive/refs/heads/main.zip -o norman-skill-main.zip
unzip norman-skill-main.zip
cd norman-skill-main
```

On Windows PowerShell:

```powershell
Invoke-WebRequest -Uri https://github.com/HPPPK/norman-skill/archive/refs/heads/main.zip -OutFile norman-skill-main.zip
Expand-Archive -LiteralPath norman-skill-main.zip -DestinationPath .
Set-Location norman-skill-main
```

Both routes leave your terminal in the repository root, with
`./learner-first-paper-reading` as the source. Run your host's copy commands
below from there. They stop if the destination already exists, including a
symbolic link; review an existing installation before replacing it.

### Codex

The [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)
lists `~/.agents/skills/` as the user skill location. On macOS/Linux:

```bash
test ! -e ~/.agents/skills/learner-first-paper-reading &&
test ! -L ~/.agents/skills/learner-first-paper-reading &&
mkdir -p ~/.agents/skills &&
cp -R ./learner-first-paper-reading ~/.agents/skills/learner-first-paper-reading
```

On Windows PowerShell:

```powershell
$skillDirectory = Join-Path $HOME '.agents/skills'
$destination = Join-Path $skillDirectory 'learner-first-paper-reading'
if (Get-Item -LiteralPath $destination -Force -ErrorAction SilentlyContinue) { throw "Destination already exists: $destination" }
New-Item -ItemType Directory -Path $skillDirectory -Force | Out-Null
Copy-Item -LiteralPath .\learner-first-paper-reading -Destination $destination -Recurse
```

Some Codex installations, including the bundled skill-installer layout used to
develop this package, use `~/.codex/skills/learner-first-paper-reading`. If that
is your client's skill location, replace `.agents` with `.codex` in the commands
for your platform. Install in one location to avoid duplicate names.
You can also ask Codex's `$skill-installer` to install only the
`learner-first-paper-reading` subdirectory from `HPPPK/norman-skill`.

### Claude-compatible hosts

[Claude Code](https://code.claude.com/docs/en/skills) supports personal skills in
`~/.claude/skills/`. On macOS/Linux:

```bash
test ! -e ~/.claude/skills/learner-first-paper-reading &&
test ! -L ~/.claude/skills/learner-first-paper-reading &&
mkdir -p ~/.claude/skills &&
cp -R ./learner-first-paper-reading ~/.claude/skills/learner-first-paper-reading
```

On Windows PowerShell:

```powershell
$skillDirectory = Join-Path $HOME '.claude/skills'
$destination = Join-Path $skillDirectory 'learner-first-paper-reading'
if (Get-Item -LiteralPath $destination -Force -ErrorAction SilentlyContinue) { throw "Destination already exists: $destination" }
New-Item -ItemType Directory -Path $skillDirectory -Force | Out-Null
Copy-Item -LiteralPath .\learner-first-paper-reading -Destination $destination -Recurse
```

Other Claude-compatible hosts may have different import locations and invocation
syntax. Use their documented Agent Skills support; compatibility is not a claim
that every client has been tested. Local personal skills do not automatically
become available in hosted or cloud sessions.

## Start reading

Open a fresh session if the client has not discovered the new folder. In Codex,
invoke the skill explicitly:

```text
Use $learner-first-paper-reading to help me learn the attached paper.
I'm new to this field. Start with a proposed route, teach the prerequisites
for one short reading assignment, and pause for my own interpretation.
```

In Claude Code, use `/learner-first-paper-reading` with the same request. For a
direct explanation, say so and provide the passage or equation. Include a PDF,
official paper link, or excerpt and your goal when available.

Automatic discovery remains enabled; the host decides whether a request matches
the skill description. If it is not selected, invoke it explicitly and check that
the complete folder is in the host's supported skill location.

## Optional Norman integration

[Norman Paper Reading](https://github.com/N-tongxue/norman-skill/tree/main/norman-paper-reading)
is an optional integration for PDF extraction, original-figure rendering, and
source mapping through its documented interface. Install it separately if wanted
and follow its own usage and rights information. This workflow works without
Norman, using the host's normal tools. Neither extraction nor an available PDF
establishes that the full paper has been inspected.

## Limits and testing status

This package contains instructions, not an enforcement mechanism. Source access,
visual inspection, citations, and execution depend on the host and permissions.
Abstract-only input supports a limited plan, not full-paper conclusions.
A forward test or one matching metric does not establish full reproduction.

The [static validator](tests/validate_contract.py) checks structure, instruction
coverage, package links, and attribution. Static validation cannot establish
agent behavior or learner understanding. The [scenario rubric](tests/scenarios.md)
defines seven fresh-context behavior checks, and the
[baseline observations](tests/baseline-observations.md) record three no-skill
controls. The [with-skill evaluation](tests/evaluation-results.md) records seven
sampled scenarios. All passed the exercised criteria after correcting and
freshly rerunning the abstract-only case, which initially omitted a future
full-text reading plan; a neighboring critique-deferral case was also rerun.
A separate explicit installed-path DLinear opening smoke observed process
disclosure and a route-agreement pause. Cross-client compatibility and automatic
discovery across clients were not established. Neither a completed full-paper
learning session nor improved learning outcomes are established by these checks.

From the repository root, run the package checks with Python 3.9 or newer:

```bash
python3 learner-first-paper-reading/tests/validate_contract.py
```

If Codex's skill-creator is installed, also run its `scripts/quick_validate.py`
against `learner-first-paper-reading/` using the script's actual installed path.
Use the scenario rubric to assess behavior separately.

## License scope

The [MIT License](LICENSE) applies only to the original files under this
`learner-first-paper-reading/` directory. It does not cover sibling directories
or upstream Norman files, binaries, branding, or templates. Their rights and
notices remain separate; this directory does not relicense the repository.
