# Let Alexis de Tocqueville serve as your investigator

A source-grounded perspective for investigating how social conditions, institutions, habits, and political choices shape the prospects for liberty. It answers directly in the user's language, with public analysis as its default and distinct guidance for private recollection and correspondence.

The investigator begins by distinguishing the question's terms, follows power through actual practices, tests explanations by comparison, and separates a long tendency from the choices that realize it. He retains attachments that do not form a perfectly consistent system: liberty and order, equality and aristocratic taste, religious aspiration and doubt, domestic freedom and French colonial ambition.

## What was rebuilt

The earlier version reduced Tocqueville to eighteen reconstructed judgments and one survey-report voice. This revision returns to the five supplied books, brings *The Old Regime* and *Recollections* into the method, and uses the letters and travel notebooks to recover disagreement, inquiry, friendship, and costly political choices.

Several old rules were removed or qualified:

- Origins influence a development; they do not contain an inevitable future.
- Mores matter greatly, and institutions also form mores. An unexplained difference is not automatically “culture.”
- Comparison tests a relevant explanation; it is not automatically a controlled experiment.
- General causes and particular actions both matter. Tocqueville was not incapable of firm or mistaken forecasts.
- National authority and administrative tutelage are different kinds of power.
- Opposition to Gobineau's racial fatalism belongs alongside Tocqueville's prejudices and colonial commitments.
- His account of women combines a claim to equal worth with prescribed unequal functions.
- Contemporary facts can be researched and analyzed; 1859 limits historical attribution, not the subjects the investigator can address.

The previous unsupported fidelity percentages have been retired. The current audit publishes its inputs, judgments, measurements, exclusions, and limitations.

## Layout and use

The canonical runtime package is [.agents/skills/tocqueville-investigator-perspective](.agents/skills/tocqueville-investigator-perspective). Its folder and frontmatter names match. Root [SKILL.md](SKILL.md) and [references](references) are relative symlinks to that package, preserving the repository's existing root entry point without maintaining duplicate copies. [AGENTS.md](AGENTS.md) preserves the project's default conversation and explicit-maintenance behavior.

For a skill loader, use the inner directory containing `SKILL.md` and `references/`. For a loader that starts at the project root, use the root `SKILL.md`. Copying the inner directory gives a self-contained runtime package. The human audit is separate and need not be supplied to the persona.

| Runtime file | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Identity, ordered inquiry, commitments, voice switches, vocabulary, and loading contract |
| [frameworks.md](references/frameworks.md) | Method, evidence, causal distinctions, historical judgments, personal scale |
| [voice.md](references/voice.md) | Three translated register profiles, editing guidance, and examples |
| [Democratic society](references/clusters/democratic-society.md) | Institutions, associations, opinion, religion, industry, and manners |
| [Old regime](references/clusters/old-regime.md) | Continuity, class separation, reform, and revolutionary preparation |
| [Inquiry and correspondence](references/clusters/inquiry-and-correspondence.md) | Questioning, comparison, disagreement, friendship, and doubt |
| [Political action](references/clusters/political-action.md) | Actors, coalitions, 1848–1851, allegiance, and national ambition |

Example requests:

- “A city wants to replace neighborhood budgets with a central office. Investigate what that changes.”
- “Why might reform increase dissatisfaction before it reduces it?”
- “Write a short letter disagreeing with the claim that citizens are permanently unfit for self-government.”
- “Explain the tension between Tocqueville's rejection of racial fatalism and his support for French Algeria.”

The reasoning sequence is not a mandatory answer template. A short question can receive a short answer. Generated prose and illustrative dialogue are not authentic historical quotations.

## Evidence and validation

[Coverage report](fidelity-ledger/coverage-report.md) and [provenance](fidelity-ledger/provenance.md) give the full accounting. Primary prose, mixed documents, and scholarship are distinguished; the duplicate *Democracy* and second *Old Regime* translation are excluded from independent corroboration. Interviewees' answers, editorial introductions, coauthored prison material, and OCR-damaged selected letters do not enter the voice baseline.

The measured source profiles distinguish public analysis, private recollection, and correspondence. A name-masked classification check assigned 12 of 12 source samples correctly. A heading-visible, same-agent reconstruction check scored 23/26 across thirteen usable items; it is **not an independent prediction benchmark**. Generated prose samples were measured and revised, but still differ in pronoun and punctuation patterns. No claim of indistinguishability from Tocqueville, French-language stylometric fidelity, or independently validated modern forecasting is made.

Run the repository checks with Python 3:

```sh
python3 scripts/validate.py
```

The checks enforce package discovery, relative links, source and element IDs, score arithmetic, audit completeness, and the runtime hash associated with the recorded tests. They do not certify historical truth or literary likeness. [Measurement instructions](fidelity-ledger/reproduction.md) explain how to repeat corpus measurements with local source files and the persona-distiller tools.

## Sources and rights

The five supplied Markdown books are identified by filename and SHA-256 in [source-manifest.json](fidelity-ledger/source-manifest.json). The Cambridge Companion is critical scholarship, never Tocqueville's own voice. Its colonial discussion supports qualified historical interpretation where the supplied collection lacks the relevant standalone reports.

No full source texts or extracted working corpus are committed. [NOTICE.md](NOTICE.md) distinguishes the original reconstruction from cited works and translations. MIT © 2026 Ariel Lee; see [LICENSE](LICENSE).
