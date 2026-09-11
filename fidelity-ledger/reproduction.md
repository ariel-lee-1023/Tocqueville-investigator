# Reproducing the measurements

The committed audit contains derived records and short evidence fragments. The source books and full extracted text remain local. The manifest's filenames and SHA-256 checksums identify the exact supplied Markdown editions; line numbers refer to those originals, before cleaning.

## Corpus replay

With the five books in one local folder and a persona-distiller checkout containing its `scripts/` directory:

```sh
python3 scripts/measure_corpus.py \
  --corpus /path/to/owned/source-books \
  --distiller /path/to/persona-distiller \
  --work /tmp/tocqueville-measurements
```

The scratch directory must be new or empty and outside this repository. The command verifies source checksums, reconstructs the eighteen broad slices, invokes cleaning and segmentation, removes bracketed material and repeated letter metadata for style, runs register discovery and per-family metrics, replays the seeded chapter split, and counts the runtime package. It uses only Python's standard library plus the distiller's standard-library scripts. The family memberships are the accepted discovery result; a changed discovery result requires editorial review before reusing them.

The initial broad raw-file cleaning census is published separately. Slices preserve original line boundaries, so they are reconstructed from originals and cleaned after segmentation. Mixed files remain mixed even after mechanical repairs. The selected-letter OCR has substantial remaining corruption and is excluded from the style baseline. Removing bracketed notes is deliberately conservative and also removes some authorial notes.

## What is reproducible mechanically

- Segmentation and source checksums: source-manifest and source-spans records.
- Corpus repair: cleaning reports and style-exclusions record.
- The three-family proposal and distance matrix: registers record.
- Per-family English metrics: style-metrics record; the pooled tool aggregate is not a runtime baseline.
- Seeded body-mask membership: passages and holdout-split records.
- Literal name occurrence counts: the name-audit records; counts do not certify a claim's authorship or truth.
- Token accounting: the distiller's `token_count.py`, uncalibrated default estimator. It adds whitespace and punctuation runs as well as 1.3 per Latin word and 1.6667 per Han/kana character. These estimates are not BPE token counts.
- Runtime/test association: `python3 scripts/validate.py` checks the stored SHA-256 against canonical runtime files.

## What still requires judgment

Extraction, evidence interpretation, curation scores, module-budget inventory, and the assessment of generated prose are editorial work. Their records permit review; they do not make those judgments objectively measured. The published five-probe ratings are qualitative rubric assignments expressed numerically, not empirical probabilities. The source-occurrence scanner counts substrings, so “press,” for example, includes other words containing those letters. Such counts serve occurrence checks, not construct-frequency estimates.

The masked-body projection used chapter headings visible to the same agent, with thirteen scored items after two contaminated items were excluded. Headings often reveal direction; some source material was already familiar. It checks recovery of mechanisms under this limited setup. It is not a fresh-context or expert-blind benchmark. The final review checks whether the completed package sustains those distinctions and records residual weaknesses; it does not pretend that rereading creates another independent holdout.

For register discrimination, `discrimination_test.py sample` was run on three separate family files with twelve passages, names masked, seed 71, and 130 words per passage. Predictions were supplied before the key was inspected. The initial seed-42 run was superseded after note and metadata contamination was found. Familiar subject matter, translation, and occasional date cues still limit the stronger interpretation of the score. No source sample text is redistributed here.

The three generated samples are newly composed test illustrations. The recollection is a fictional council scene; the correspondence is a fictional exchange; none is a quotation or an assertion that a historical event occurred. Initial and revised sample metrics are retained. Revision after measurement is part of development, so the revised samples are not an untouched evaluation set. Full pressure-dependent modulation remains unvalidated.

## Budget inventories

The module estimates count distinct retained distinctions, operative moves, entry situations, and source anchors. They are editorial counts rather than counts of headings or raw corpus matches. The four depth modules fold nearby source units; that does not make a reused passage independent evidence. The budget input and routing records identify those folds.

The standalone 1841 and 1847 Algeria reports and the 1839 abolition report were not found as complete texts in the supplied files. Some relevant judgments are supported through letters or scholarship. A claim to have independently distilled those complete reports would require additional material.
