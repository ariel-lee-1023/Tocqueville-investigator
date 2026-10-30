# Let Alexis de Tocqueville serve as your investigator

I am Alexis de Tocqueville (29 July 1805). You tell me that a central office
could conduct the business of several neighborhoods with greater regularity.
I can readily believe it. I should still wish to know what the inhabitants
will cease to do together when the office takes charge, and where they will
learn the judgment and perseverance which their common affairs formerly required.

The administrative result and the effect upon the citizen may differ. Yet I
would not conclude that every local power serves liberty: a neighborhood can
defend a privilege as readily as a right. We must examine who decides, who
pays, who is excluded, and who can correct a mistake. Comparison becomes
useful when it tests one of these relations.

Bring me a reform whose consequences seem obvious to both its friends and its
enemies. I shall look for the practice each has omitted. Equality changes men's
expectations and their relations with one another; it does not decide in advance
whether they will become capable of governing themselves. The choices that
form their habits remain part of the inquiry.

*This introduction is a newly written, source-grounded persona reconstruction,
not a historical quotation. [Editorial and birth-date notes](fidelity-ledger/provenance.md#readme-editorial-review-2026-10-30).*

This investigator examines democracy, institutions, social habits, and liberty.
It retains Tocqueville's tensions, including his defense of liberty at home
alongside French colonial ambition. Contemporary cases apply his methods;
they do not supply historical endorsements or independently validated forecasts.

## Begin with a change in who can act

**Suggested first prompt:**

> A city wants to replace neighborhood budgets with a central office. Here are
> the current and proposed arrangements. Investigate who will decide, pay,
> execute, and answer for mistakes, and what residents will gain or lose the
> opportunity to do together.

Bring actual practices as well as the legal plan. The inquiry distinguishes
national coordination from administrative tutelage and asks how institutions
train habits. Greater regularity may have a civic cost; a local arrangement
may also perpetuate exclusion. Neither consequence follows from the label alone.

Other suggested questions:

- Why might reform increase dissatisfaction before it reduces it?
- How could a letter firmly reject a friend's doctrine without ending the friendship?
- How can opposition to racial fatalism coexist with support for French Algeria?

Public analysis is the default. A requested political recollection gives more
space to actors and conduct; correspondence permits affection, disagreement,
and unfinished thought. No form licenses invented memories of a modern event.

## Use the investigator

```sh
git clone https://github.com/ariel-lee-1023/tocqueville-investigator.git
```

Open the folder with an agent that reads [AGENTS.md](AGENTS.md), which activates
the local perspective while preserving explicit requests to change modes or
maintain the files. The current runtime follows the user's language and format.
For another skill host, install [SKILL.md](SKILL.md) and
[references](references/) together under `tocqueville-investigator-perspective`.
The repository keeps one regular root runtime copy.

Before the first substantive answer, read the complete core,
[voice](references/voice.md), and [frameworks](references/frameworks.md), even
for short replies. Reuse retained context; reload missing files after compaction.
Add relevant topic modules when needed. Without file access, supply those three
complete texts and the relevant topic material at the start.

## Follow the question into the sources

| Question | Reference module |
|---|---|
| Associations, opinion, religion, industry, and everyday relations | [Democratic society](references/clusters/democratic-society.md) |
| Administrative continuity, class separation, and revolutionary preparation | [Old regime](references/clusters/old-regime.md) |
| Interviews, comparison, private disagreement, friendship, and doubt | [Inquiry and correspondence](references/clusters/inquiry-and-correspondence.md) |
| Actors, coalitions, 1848–1851, and national ambition | [Political action](references/clusters/political-action.md) |

The five supplied books bring *Democracy in America*, *The Old Regime*,
*Recollections*, travel notes, correspondence, and critical scholarship into
the reconstruction. Their exact identities and hashes are in the
[source manifest](fidelity-ledger/source-manifest.json). The 2006 Cambridge
Companion supplies scholarship, never Tocqueville's own voice. Duplicated
works and alternative translations do not provide independent corroboration.

The personal record runs from the 1820s to 1859; later publication does not
extend his lifetime knowledge. That boundary limits historical attribution,
not the possibility of researching a present-day question. His judgments on
slavery, race, women, and colonial rule retain their historical tensions rather
than forming an entirely consistent defense of equal freedom.

## Evidence and limits

The [coverage report](fidelity-ledger/coverage-report.md) and
[provenance](fidelity-ledger/provenance.md) distinguish primary prose,
interviewees' answers, mixed documents, editorial material, and scholarship.
OCR-damaged selected letters were excluded from the voice baseline.

A name-masked check classified 12 source samples correctly. A heading-visible,
same-agent reconstruction check scored 23/26 over thirteen usable items; it
was not an independent prediction benchmark. Generated samples still differed
in pronoun and punctuation patterns. These results establish neither French
stylometric fidelity nor independently validated modern forecasting.

Historical assessments retain the runtime inputs and scope originally tested;
the loading update has not been reassessed, and this README revision adds no
recognition calls. The repository's structural check is
`python3 scripts/validate.py`. [Reproduction notes](fidelity-ledger/reproduction.md)
explain the corpus measurements; a structural pass is not a literary likeness test.

## Rights

No full source texts or extracted working corpus are committed. [NOTICE](NOTICE.md)
distinguishes the reconstruction from cited works and translations.
[MIT](LICENSE) © 2026 Ariel Lee covers the original repository material.
