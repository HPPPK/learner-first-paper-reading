# Source Quality and Provenance

Use this reference to establish what source is available, what has been inspected,
and what each source can support. Respect the learner's source restrictions;
an instruction to work from an abstract alone is not permission to find full text.

## Identify the source before making paper claims

Record title, authors, identifier or supplied file, version and date, publication
status, and source URL as available. Distinguish a preprint revision, accepted
manuscript, publisher version, supplement, and later code revision. Mark missing
identity fields unverified. Check a supplied file against its title page and
version stamp; a familiar title does not identify its version.

For comparisons across versions, identify which claim or anchor belongs to which
version. Preserve that association in notes and citations. Do not silently combine
an equation from one version with an experimental result from another. Official
code needs its own repository and commit/tag identity when implementation details
matter; repository ownership and its link from the paper help verify provenance.

## Separate access from inspection

Record inspected coverage: metadata, abstract, named full-text sections, figures,
tables, appendices, supplements, or code files. An available PDF is full-text
access, not proof that every page was read. A search snippet or abstract page is
not full-text inspection. Anchor statements to the actual inspected location,
using a section, equation, page, figure, or table identifier the learner can open.

With abstract-only access, offer a limited reading plan and leave full-paper
claims unverified. Attribute reported claims to the abstract; the method,
comparison protocol, visual evidence, and limitations remain Unknown until their
sources are inspected. For excerpts, bound the claim to that excerpt. Do not
invent the missing section structure from memory.

Disclose access limits such as unavailable full text, blocked pages, unreadable
figures, incomplete extraction, or unopened supplements. State what each limit
prevents checking and which source would resolve it. A failed visual extraction
does not support descriptions of the figure. If access is unavailable, offer a
bounded explanation or next reading request, and label an uninspected reference
as a candidate rather than a verified supporting citation.

## Choose authority for the claim being taught

Prefer original papers, publisher pages, official code and documentation,
textbooks, and university course material over blogs and unsourced summaries.
Within that set, choose by purpose:

| Need | Preferred source and limit |
| --- | --- |
| Focal paper's design, results, or author claim | The inspected paper version and its supplement; the publisher or official archive establishes identity, while the relevant full-text passage supports content. |
| Origin or technical claim about a method | Primary sources for technical claims, particularly the original research paper, derivation, or official specification. A later summary is a route to that source. |
| Beginner prerequisite or standard definition | A reputable textbook or university course section that explains the mechanism and assumptions at the required level. |
| Software semantics or implementation | Official documentation or author-linked official code at the relevant version. Code shows implementation behavior; it does not independently validate the paper's empirical claim. |

A blog may supply a useful illustration after authoritative checks, but is not
the sole authority for a load-bearing technical claim. A prestigious source is
still unsuitable if its passage does not support the claim. Avoid adding a long
reading list when one relevant section answers the blocking question.

## Inspect and link the supporting material

Inspect the passage or section that supports the background claim before citing
it as verified. Check author or institution, title, edition/version, and whether
the claim and its conditions actually appear there. Prefer a stable direct link
to the official paper, DOI destination, chapter, documentation page, or university
material over search results, tracking URLs, scraped mirrors, and generic homepages.
Follow redirects and use the final authoritative destination when available.

Attach each link to the specific Background claim it supports and name the useful
section or chapter. Provide links when the learner requests further reading or
external background adds material explanatory value. Omit links when a supplied
equation or self-contained worked example already resolves the question and no
external claim needs support. Never fabricate a URL or imply that an unopened
link has been verified; disclose a link-check failure and its practical limit.

## Keep the source voices distinct

Label external material as **Background**. Keep external background separate from
the focal paper's evidence. A textbook can explain why smoothing removes some
variation under stated assumptions; only the focal paper's inspected evidence
can support what its experiments observed. Neither establishes true latent
components merely because the residual was defined by subtraction.

- **Paper:** Attribute the focal paper's statement or reported observation to its
  inspected anchor; an author claim and independent verification are different.
- **Background:** Attribute an external mechanism or definition to the supporting
  authoritative source and link it when it materially supports the explanation.
- **Analyst:** Mark your toy example, interpretation, connection, or recommendation
  as your own; cite the underlying paper or background separately.
- **Unknown:** State what the inspected sources do not establish, including a
  paper-specific role when only general background is available.

Clear attribution in prose can carry these voices; headings are optional. Split
sentences when combining sources would make it unclear who claims what. After
teaching background, return to the focal paper's inspected location and identify
exactly how the concept is used without promoting the background source into
evidence for the paper's performance or generality.
