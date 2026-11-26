# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2026-11-26

### Fixed

- Pinned the validation runner to Ubuntu 24.04 so the declared Python 3.9 job
  remains available after `ubuntu-latest` moved to Ubuntu 26.04.
- Updated checkout and Python setup to their current Node 24 action releases,
  removing the Node 20 deprecation warning.

## [0.1.0] - 2026-11-26

### Added

- Standalone learner-first paper-reading Agent Skill with guided, focused,
  evidence-review, and reproduction routes.
- Four provenance voices, a guided comprehension gate, and six reproduction
  evidence states.
- English and Chinese landing pages, accessible SVG brand assets, and three
  curated route demonstrations.
- Deterministic contract validation, sampled behavior scenarios, contributor
  guidance, issue forms, and portable CI.

### Evidence boundary

The tracked checks do not establish learning outcomes. They do not establish
universal agent behavior, automatic discovery, or compatibility on every Agent
Skill host. See [evaluation results](tests/evaluation-results.md)
for the tested conditions and missing evidence.

[Unreleased]: https://github.com/HPPPK/learner-first-paper-reading/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/HPPPK/learner-first-paper-reading/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/HPPPK/learner-first-paper-reading/releases/tag/v0.1.0
