# Let Alexis de Tocqueville serve as your investigator.

An [Agent Skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) that
lets an AI assistant investigate a question the way **Alexis de Tocqueville** actually worked: find
the master social fact, read a society from its point of departure, rank mores above laws, compare
two cases to isolate the mechanism, separate the letter from the spirit, and project a tendency as a
conditional warning rather than a prophecy. Output is a first-person survey report.

This is a *reasoning* persona, not a costume. It was distilled from a mapped corpus — eighteen
reconstructed judgments with trigger → inference chain → evidentiary standard → unfiltered
conclusion → transferable procedure — and every element in the deployable core is traceable to a
source in [`fidelity-ledger/provenance.md`](fidelity-ledger/provenance.md).

---

## What makes this different from a "write like Tocqueville" prompt

Three design commitments, all auditable:

1. **The engine is separated from the convictions.** Method regularities that generalize (projection
   score ~0.9) live in the deployable core. Historically-local convictions that do *not* generalize
   (race, empire, gender; ~0.5–0.6) are routed to a reference file and are never generated fresh.
2. **Nothing is sanitized away.** Those convictions are recorded in full, in his own terms, with
   their internal contradictions preserved rather than resolved — abolitionist yet racial pessimist,
   liberal at home yet endorsing colonial domination. The skill reports them as *his*, situated in
   his century, and declines to extend them onto questions he never addressed.
3. **The factual world is frozen at 1859.** The method is applied to the present; post-1859 facts
   are not asserted.

---

## Repository layout

```
.
├── README.md
├── SKILL.md                                  # the deployable persona core (loaded first)
├── references/
│   ├── reasoning-engine-map.md               # 18 judgments, full inference chains (J1–J18)
│   ├── frameworks.md                         # named constructs: mœurs, point de départ, etc.
│   └── convictions-and-contradictions.md     # attested positions on race, slavery, women, empire
├── fidelity-ledger/                            # human-facing, never loaded by the host agent
│   └── provenance.md                         # element → source → fidelity ledger; known limits
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md                                 # originality and source-attribution statement
└── .github/workflows/validate-skill.yml      # structural CI check (optional)
```

`SKILL.md` carries the YAML frontmatter (`name`, `description`) the assistant reads to decide when to
invoke the skill. The `references/` files load progressively — only when the question calls for them.

---

## Installation

**Claude Code (personal or project scope)**

```bash
# personal — available in every project
git clone https://github.com/ariel-lee-1023/tocqueville-investigator.git \
  ~/.claude/skills/tocqueville-investigator-perspective

# or project-scoped, committed alongside your repo
git clone https://github.com/ariel-lee-1023/tocqueville-investigator.git \
  .claude/skills/tocqueville-investigator-perspective
```

The skill is discovered automatically; it loads when a question matches its description.

**Claude.ai / the API** — zip the folder (with `SKILL.md` at the top level of the archive) and upload
it as a custom skill. See the
[skill authoring docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
for the current upload path.

**Any other agent runtime** — the format is plain Markdown; point your loader at `SKILL.md` and give
it read access to `references/`.

---

## Usage

Invoke it by naming the perspective or by asking for the kind of analysis it performs:

- "Analyse remote work as Tocqueville would."
- "What is the master social fact behind the decline of local newspapers?"
- "Take the platform moderation debate and read the letter against the spirit."
- "Compare Denmark and Britain on civic association; isolate the mechanism."

Expect: a concrete opening scene, a named master fact, a controlled comparison, a paradox reported
with both faces intact, and a conditional projection with its counter-forces named — not a verdict
dressed as a forecast.

### On the sensitive material

When a question touches race, slavery, the condition of women, or empire/Algeria, the skill loads
`references/convictions-and-contradictions.md` and reports what Tocqueville held and why, with the
locus cited and the contradiction left open. Asked to apply his racial or colonial *premises* to a
new question, it declines the extension and offers instead the part of his thought that travels: the
comparison, the mores-analysis, the tendency-projection. That boundary is deliberate and documented
in the provenance ledger — it is a fidelity decision as much as an ethical one.

---

## Fidelity summary

| gate | result |
|---|---|
| Pre-assembly projection | 0.80 overall (PASS, threshold 0.70); method ~0.9, historical convictions ~0.5–0.6 |
| Cost gate | 8/8 high-signal divergences accounted for; 5 in core, 3 in references with logged reason |
| Assembled-core projection re-check | ~0.9 on claimed domains; PASS |
| Cost-presence assertion | core carries five cost-refusals; PASS |
| Style match | qualitative PASS; formal metrics pass deferred |

Full table, per-element sources, and cluster corroboration: [`fidelity-ledger/provenance.md`](fidelity-ledger/provenance.md).

### Known limits

- Tranche-1 map only (18 judgments). *The Old Regime and the Revolution* and *Recollections* are
  un-mapped.
- Interactional signal is thin — the corpus is largely monologic, so "How I move in an exchange"
  leans on the Letters and *Journey to America*.
- The post-1859 factual world is out of scope by construction.
- `fidelity-ledger/provenance.md` refers to `fidelity-ledger/fidelity.json` and `references/reasoning-engine-map.md`
  refers to `coverage-report.md`; those pipeline artifacts are not published in this repository.

---

## Sources

Tocqueville's own writings are in the public domain: *Democracy in America* (Reeve translation),
*Journey to America*, *Selected Letters*, the 1833 penitentiary report, the abolition writings, the
Algeria notes and Chamber reports, *The Old Regime*, *Recollections*. Secondary reference material
was used only to verify dates and institutions, never to soften a stated position.

The reconstruction, mapping, curation, and prose of this repository are original work and are what
the license below covers.

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

This license covers the original text in this repository. It does not extend to any referenced source books, which remain the property of their respective copyright holders.

