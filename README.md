# Research-paper-

Structural blueprints for writing research papers, packaged as agent-loadable skills — plus a complete worked example applying one of them.

---

## 1. The skill

### `skills/writing-plant-science-papers/`

A structural blueprint for **molecular biology, plant science, and agricultural research papers** — the biology counterpart to a systems-conference writing guide.

| File | Purpose |
| --- | --- |
| `SKILL.md` | The bluebook. Mandatory pre-flight gate, evidence ladder, rolling audit, section blueprints, venue match checker, statistics and nomenclature rules |
| `references/quick-reference.md` | One-page condensed card for daily use |
| `references/review-paper-blueprint.md` | **Reviews — a different genre.** Review-type taxonomy, R0–R5 quality ladder, thesis requirement, integrity constraints |
| `references/manuscript-scaffold.md` | Fillable section-by-section scaffold with an evidence audit table and planning block |
| `references/figure-table-plan.md` | Figure-first planning, reverse-engineering from a target venue, panel craft |
| `references/reporting-checklists.md` | Submission gates: venue match, MIQE, MIAPPE, MINSEQE, statistics, integrity |

**Core idea.** A systems paper's currency is architectural novelty; a biology paper's currency is **evidence strength for a causal claim**. The blueprint is built around that difference — an Evidence Ladder (L0 association → L7 field impact) with a *verb ceiling*, a rolling audit that treats evidence as a variable rather than an input, and "alternatives and limitations" as mandatory Discussion paragraphs.

---

## 2. The worked example

### `projects/chilli-osmotic-stress/`

A complete critical review, built by applying the blueprint: **screening for drought tolerance in *Capsicum* and the Solanaceae**, targeted at *Frontiers in Plant Science* (Review, 12,000 words).

| File | What it is |
| --- | --- |
| **`REVIEW-final.md`** | **The assembled paper** — title, abstract, nine sections, five figure legends, seven table specifications, working bibliography, author notes |
| `study-inventory.md` | The backbone: 14 screening studies tabulated, candidate genes with validation hosts, connecting studies, corrections log |
| `preflight-and-plan.md` | The gate result and reverse-engineered research plan |
| `review-outline.md` | Pre-draft outline, Frontiers format constraints, section plan |
| `register-and-balance.md` | How to write a critical review the field accepts |
| `draft-section-2.md`, `-3`, `-4`, `-5`, `sections-6-7` | Section drafts with verification notes and correction notices |

### What the exercise revealed

Applying the blueprint to a real topic caused **seven planned claims to be withdrawn or reversed** before any of them reached the paper. The pattern was consistent:

| Claim | What verification found |
| --- | --- |
| *Capsicum* lacks validated drought loci | Contradicted by a 2026 GWAS+QTL study |
| No study connects developmental stages | Contradicted by nine connecting studies |
| The predictive link is negative | Genuinely contradictory — four studies each way |
| PEG impurities cause artefacts | Tested and rejected in 1970 |
| PEG detergent effects cause toxicity | Tested and rejected in 1970 |
| PEG does not enter plant tissue | Contradicted by direct measurement in pepper itself |
| "Drought" is an appropriate label | Correct, but had to become a finding rather than an assumption |

Not random failures — a pattern. **Conventional wisdom in this field is repeated more than it is checked.** Some of it was tested decades ago and "rejected" results never entered the citation loop. That is a citation problem, not a competence problem, which is both more accurate and more publishable.

The final review is correspondingly **constructive rather than contrarian**: every criticism is paired with an acknowledgement of what the field achieved, a reason the original choice was reasonable, and a cheap fix. Six of the fifteen items in its proposed reporting standard require no additional experiment.

### Key numbers

- **9,384 words** — measured body text, against a 12,000 limit (~2,600 headroom)
- **7 corrections** logged and withdrawn before drafting
- **14 studies** tabulated with genotype counts, PEG levels and identified lines
- **15-item** minimum reporting standard proposed
- **~2,300 words** of verification notes preserved alongside the drafts

---

## Integrity note

These documents provide **structural guidance and literature synthesis only**. They do not generate findings, figures, images, or citations, and nothing here should be submitted without checking every reference against its source. The final paper's bibliography is explicitly marked incomplete — fields requiring completion are flagged. Fabrication, image manipulation, and memory-generated citations are prohibited by `SKILL.md` §15 and by `review-paper-blueprint.md` §8.
