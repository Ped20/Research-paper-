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
| **`REVIEW-final.md`** | **The assembled paper** — title, abstract, nine sections, 59 in-text citations, five figure legends, eight tables populated from primary sources, verified reference list, author notes. **No placeholder markers.** |
| **`figures/`** | **Figures 1–5, drawn at 300 dpi.** Framework; PEG concentration→osmotic potential computed from Michel and Kaufmann (1973); developmental strata; evidence map; concordance reporting |
| **`supplementary-table-S1.md`** | Supplementary Tables S1–S2 — per-study design and limitation detail, which keeps the main text inside the word limit |
| **`reference-verification.md`** | **The audit log.** Every reference checked against Crossref; the ten DOIs that resolved to different papers; the six markers and their resolution; the Table 4 cells and the claim one of them broke; the two entries that are publisher-verified only |
| `make-figures.py` | Re-runnable: draws all five figures and prints the PEG conversion table on every run |
| `resolve-markers.py`, `final-pass.py` | The two one-shot marker-resolution passes, kept as an audit record; both refuse to write unless every anchor matches |
| `study-inventory.md` | The backbone: 14 screening studies tabulated, candidate genes with validation hosts, connecting studies, corrections log |
| `preflight-and-plan.md` | The gate result and reverse-engineered research plan |
| `review-outline.md` | Pre-draft outline, Frontiers format constraints, section plan |
| `register-and-balance.md` | How to write a critical review the field accepts |
| `insert-citations.py` | The 59 exact-substring citation insertions, with a per-anchor assertion that refuses to write if any anchor fails |
| `splice-tables.py` | The table renumbering and late citations, kept as an audit record |
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
| Most tomato genotypes fail above −0.35 MPa | True of that panel — and now cited; but it is a panel result, not a universal ceiling |
| A model comparison supports ANOVA on germination data | The source supports it only in a 0.3–0.7 proportion band — not where osmotic screening operates |
| Only one *Capsicum* gene has functional evidence in pepper | Three do — *CaNAC46*, *CaDIM1* and *CaSBP13*, all by VIGS in pepper. The count was too low, not too high |
| *CaSBP13* is a drought-tolerance candidate | It is a **negative** regulator; silencing it improves tolerance |

Not random failures — a pattern. **Conventional wisdom in this field is repeated more than it is checked.** Some of it was tested decades ago and "rejected" results never entered the citation loop. That is a citation problem, not a competence problem, which is both more accurate and more publishable.

The final review is correspondingly **constructive rather than contrarian**: every criticism is paired with an acknowledgement of what the field achieved, a reason the original choice was reasonable, and a cheap fix. Six of the fifteen items in its proposed reporting standard require no additional experiment.

### Key numbers

- **11,907 words counted** against the Frontiers 12,000 limit — abstract, prose, legends and tables, references excluded (93 headroom; Table 2's detail columns moved to supplementary to make room)
- **59 in-text citations** inserted, where the body previously cited nothing at all; **52 references**, six added to resolve the last markers
- **10 of ~30 DOIs resolved to different papers** and were corrected; one pointed at a *Citrus* study
- **7 claims** withdrawn or reversed before drafting; **1 deleted** at the reference audit for want of a source
- **14 studies** tabulated with genotype counts, PEG levels and identified lines; **5 figures drawn**; **6 of 6 verification markers** closed to primary sources
- **15-item** minimum reporting standard proposed, 6 items requiring no new experiment

### The reference audit

The bibliography was rebuilt from Crossref metadata rather than from memory. One in three DOIs was wrong — not randomly wrong, but *plausibly* wrong: right shape, right journal family, right year, wrong paper. Several differed only in an article number and would have passed a glance.

The same pass found something larger: the manuscript's **body contained no in-text citations whatsoever**. Nine thousand words of critical review resting on a 46-item bibliography with nothing attributing anything. That is a desk rejection, and no amount of reference-list formatting would have caught it. Both findings are documented in `reference-verification.md`.

---

## Integrity note

These documents provide **structural guidance and literature synthesis only**. They do not generate findings, figures, images, or citations, and nothing here should be submitted without checking every reference against its source. The final paper's bibliography is explicitly marked incomplete — fields requiring completion are flagged. Fabrication, image manipulation, and memory-generated citations are prohibited by `SKILL.md` §15 and by `review-paper-blueprint.md` §8.
