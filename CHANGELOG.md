# Changelog

All notable changes to this skill are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html), read for a persona as:

- **MAJOR** — the reasoning engine changes: a method regularity is added, removed, or reversed, or a
  fidelity gate is re-run with a different outcome.
- **MINOR** — new reference material, new coverage (a mapped tranche, a new construct), or a
  behavioural rule added without altering existing moves.
- **PATCH** — wording, citations, typos, layout, and documentation that leave behaviour unchanged.

## [Unreleased]

### Changed
- **`audit/` renamed to `fidelity-ledger/`.** Aligns this repo with the naming used across the
  other perspective skills (a top-level, human-facing folder holding `provenance.md`, sibling to
  `references/`, never loaded by the host agent). This repo already kept the provenance ledger
  outside `references/`, so only the folder name changed — pure rename, no content changes.
  `README.md` and `.github/workflows/validate-skill.yml` updated to reference the new path.
- **Loading depth now states a real-world-retrieval rule, distinct from the corpus-internal lookup
  and expanded from the existing "hard boundary" line.** `references/` and `fidelity-ledger/`
  answer questions about the reasoning engine and his own attested positions — the SOURCE OF TRUTH
  search, corpus-internal by design; the hard boundary at 1859 was already there but did not say
  this is a *second, separate* mechanism. `SKILL.md` now says so explicitly: retrieve any
  present-day fact the question depends on from the live world first, then run it through the
  reasoning-engine judgments, and do not treat the corpus as either currently accurate or as the
  limit of what the engine can be turned on.

### Fixed
- Repository layout now matches the one documented in `README.md` and already referenced by
  `SKILL.md`. The reference files, the provenance ledger, and the CI workflow sat loose at the
  repository root, so every `references/…` load path in `SKILL.md` and the `audit/provenance.md`
  link in `README.md` pointed at files that did not exist. Moved into `references/`, `audit/`,
  and `.github/workflows/` respectively; no file contents changed.

### Planned
- Tranche 2 of the reasoning-engine map: *The Old Regime and the Revolution* and *Recollections*.
- Formal `style_metrics.py` comparison against held-out originals (the deferred full-rigor style pass).
- Publish `audit/fidelity.json`, the machine-readable record referenced by the provenance ledger.

## [1.0.0] — 2026-07-22

First public release.

### Added
- `SKILL.md` — the deployable persona core: master-fact search, point of departure, the causal
  ranking (mores > laws > circumstances), letter-vs-spirit reading, comparison as method, conditional
  tendency projection, paradox as the default expectation; five cost-refusals under "What I will not
  concede"; interactional and expressive layers.
- `references/reasoning-engine-map.md` — Tranche-1 extraction map, 18 judgments (J1–J18) in the
  five-field schema (trigger → inference chain → evidentiary standard → unfiltered conclusion →
  transferable procedure), with provenance lines and cross-cluster corroboration.
- `references/frameworks.md` — named constructs preserved in his own terms: équalité des conditions,
  point de départ, mœurs, individualisme, tutelary despotism, tyranny of the majority, intérêt bien
  entendu, the art of associating, providential fact, domination vs. colonization.
- `references/convictions-and-contradictions.md` — attested positions on race (J12), Native Americans
  (J13), women (J14), Algeria and empire (J15), and abolition (J16), with contradictions preserved
  and premises flagged as his, not the engine's.
- `audit/provenance.md` — element-to-source fidelity ledger, gate results, routing rationale, and
  known limits.
- Repository scaffolding: README, MIT license, `.gitignore`, this changelog, and a structural
  validation workflow.

### Design decisions recorded at release
- Convictions scoring ~0.5–0.6 on the projection gate (race, empire, gender) were routed to
  references rather than the generative core; they are reported as historical positions and never
  generated fresh onto new targets.
- The expressive layer was inherited from `tocqueville-surveyor` v1 rather than re-derived, and
  capped so that voice does not crowd out method.
- The factual world is frozen at 1859 by construction; the method alone is applied to the present.

[Unreleased]: https://github.com/ariel-lee-1023/tocqueville-investigator/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ariel-lee-1023/tocqueville-investigator/releases/tag/v1.0.0
