# Pre-Flight & Reverse-Engineering Worksheet

**Project:** In vitro screening of chilli genotypes for osmotic (drought) stress tolerance, with field validation and gene identification
**System applied:** `skills/writing-plant-science-papers/` (§0 gate, §2 audit, §3 reverse-engineering, §8 venue match, §12 scope)
**Date:** 2026-09-29
**Status:** ⛔ **GATE INCOMPLETE — 2 of 6 questions unanswered. No manuscript drafting permitted.**

---

## 1. GATE RESULT — the system refused to proceed

| # | Question | Answer | Status |
| --- | --- | --- | --- |
| 1 | Paper type | User says "review paper"; described workflow is original research | ⛔ **CONTRADICTION — see §2** |
| 2 | Target venue | Not stated | ⛔ **BLOCKING** |
| 3 | Strongest evidence (L0–L7) | Planning stage; realistic ceiling L0–L1 | ✅ Inferable |
| 4 | Stage | Planning only — no data | ✅ Answered |
| 5 | Scope | Multi-stage: screening → field → gene ID | ✅ Answered |
| 6 | Constraints (budget, land, seasons, lab equipment) | Not stated | ⛔ **BLOCKING** |

> **This is the gate working as designed.** A systems-paper blueprint would have started drafting. Drafting here would have produced three thousand words of Methods for an experiment that is not yet designed, at an evidence level that cannot support the claims implied by the title.

---

## 2. THE CONTRADICTION — review vs. research

**You asked for a review paper. You described a research programme.**

| Reviewed request | What you actually described |
| --- | --- |
| "review paper on in vitro screening of chilli genotypes under osmotic stress" | Your own genotypes, your own petri dishes, your own field trial, your own DNA extractions |

A review synthesises *published* literature and reports no new data. What you described — germinating genotypes in PEG, selecting the tolerant ones, validating them in the field, extracting DNA and identifying genes — is **original research**, and it is your data, not anyone else's.

These are two different papers with two different blueprints:

| | **Review paper** | **Research paper** |
| --- | --- | --- |
| Evidence source | Published literature | Your own experiments |
| Structure | Thematic synthesis; no Results section | IMRaD with Results |
| Blueprint applied | Not this one — reviews need a different skeleton | Sequence below |
| Effort | Weeks of literature work | 2–4 seasons |
| Venue | Reviews in Plant Science, Frontiers, Agronomy for Sustainable Development | See §6 |

**Both may be legitimate.** In Indian MSc/PhD programmes a review is often a separate requirement from the thesis research. If that is your situation, you need two deliverables, not one — and this worksheet covers only the research one.

---

## 3. THE PLAN, RE-SEQUENCED

Your four stages, restated with the decision points the system requires you to resolve.

```
STAGE 1 — Laboratory screening (§4)
   Genotypes × PEG levels × replication
   Output: tolerance index per genotype, ranked and grouped
   DECISION: which genotypes advance, and how many?

STAGE 2 — Field validation (§5)
   Selected genotypes under managed drought vs. irrigated control
   Output: field drought response per genotype
   ⭐ KEY CLAIM: does the lab screen predict field performance?

STAGE 3 — Molecular characterisation (§6)
   Contrasting genotypes → candidate gene expression and/or sequence polymorphism
   Output: candidate gene(s) and/or markers associated with the screening index

STAGE 4 — Marker development (optional, only if Stage 3 succeeds)
   Convert polymorphism to a scalable assay (KASP/CAPS/SSR)
   Validate on the wider genotype panel
```

> **Stages are sequential, but writing is not.** Once Stage 1 data exist, the Methods and the screening Results can be drafted — do not wait for Stage 4.

---

## 4. STAGE 1 — Laboratory screening specification

### Design (correcting the common errors)

| Element | Specification | Why |
| --- | --- | --- |
| Genotypes | ≥20; must include a known tolerant and a known susceptible check | Without checks your ranking has no anchor |
| PEG-6000 levels | 0 (control), 5% (−0.3 MPa), 10% (−0.6 MPa), 15% (−0.9 MPa); add 20% (−1.09 MPa) for a severe level | Concentrations used in published chilli work: 5/10/15% (IIHR), 12.5% (Molla et al.), 15% (IPB) |
| Osmotic potential | **Verify each solution with a vapour-pressure osmometer or psychrometer** | PEG batch varies; unverified nominal values are a reviewer target |
| Experimental unit | **The petri dish** — not the seed | n = seeds is pseudo-replication (§10) |
| Replicates | ≥4 petri dishes per genotype × treatment; ≥10 seeds per dish | Enough for GLMM convergence |
| Design | Factorial (genotype × PEG level), completely randomised | As published precedent |
| Germination criterion | Radicle ≥ 2 mm; score every 24 h for 10–14 d | Standard, and enables germination rate/MGT |
| Environment | Incubator, 25 ± 1 °C, dark, dishes sealed | "Closed petri dish" must be specified: sealant, humidity, condensation control |

### Traits to record

Germination % · germination rate · mean germination time (MGT) · germination index · root length · shoot length · root:shoot length ratio · seedling fresh weight · seedling dry weight · seedling vigour index

### Tolerance indices — the part that makes the ranking defensible

Compute per genotype, relative to control:

- **GSI** germination stress index
- **SSI** stress susceptibility index (Fischer & Maurer)
- **STI** stress tolerance index (Fernandez)
- **TOL** tolerance index
- **MP** mean productivity · **GMP** geometric mean productivity

Then: **PCA → cluster analysis (Ward) → genotype groups.** This converts a genotype list into tolerant / moderately tolerant / susceptible categories, which is what Stage 2 needs.

### Statistical model

- Germination % is **binomial** → GLMM, binomial family, logit link. *Not* ANOVA on percentages; arcsine transformation is deprecated.
- Continuous traits (lengths, weights) → LMM with genotype, PEG level, and their interaction as fixed effects.
- **The `genotype × PEG level` interaction is the term that matters.** A genotype that simply grows larger overall will look "tolerant" if you only compare genotypes at the high-stress level. The interaction separates true stress tolerance from general vigour.
- Multiple comparisons: Tukey or Holm. Report model, version, and effect sizes with CIs.

### ⚠️ Design flaw to fix before you start

**Do not advance only the extreme genotypes.**

Selecting only the highest performers and then testing whether the screen predicts field performance truncates the range of your predictor variable, which **attenuates the correlation you are trying to measure** — the key claim of the whole paper.

Advance a **spectrum**: 4–6 tolerant, 4–6 intermediate, 4–6 susceptible. The intermediates are not filler; they are what makes the correlation meaningful.

---

## 5. STAGE 2 — Field validation specification

### The central risk, stated plainly

**Germination-stage PEG screening and field drought tolerance are not the same trait.** This is the single largest threat to this paper, and reviewers will raise it.

Evidence: in a 2024 barley study that explicitly set out to test "the reliability of proxy methods in identifying drought tolerant lines," the correlation between germination rate under PEG and seed yield under drought was **negative (r = −0.25)** — an outcome the authors called unexpected. Germination percentage also correlated negatively with root:shoot fresh weight under PEG (r = −0.37). Some genotypes performed better under PEG than under control for some traits.

The reason is biological: germination-phase osmotic tolerance and reproductive-stage field drought tolerance involve different mechanisms. Chilli is typically drought-stressed at **flowering and fruit set**, not at germination.

### Two ways to handle it

| Option | Description | Effect on the paper |
| --- | --- | --- |
| **A. Match the stress stage** | Impose field drought at flowering/fruit set, and add a second lab screen at the seedling stage. Report the correlation honestly, including if it is weak. | Honest, defensible, and the weak correlation becomes the finding |
| **B. Reframe the claim** | Call it "germination-stage osmotic tolerance," drop all claims about general drought tolerance, and present the field trial as a test of whether the proxy transfers | Safe, but the paper becomes narrower |

**Do not** do neither and write as if the proxy is established. That is the path to rejection.

### Field design

| Element | Requirement |
| --- | --- |
| Drought imposition | **Managed** — withhold irrigation at a defined stage (e.g. 50% flowering) or use a rainout shelter. Not "we relied on the season" |
| Control | Irrigated control, same site, same season, same management |
| Design | RCBD, ≥3 blocks, ≥10 plants per plot per genotype |
| Seasons | **≥2** — one season is an anecdote, and site-year is your random effect |
| Gap | ≥2 m between droughted and irrigated blocks (root and water movement) |
| Traits | Marketable fruit yield (primary), fruit number, fruit weight, plant height, canopy, relative water content, membrane stability index, proline, SPAD/chlorophyll |

### ⚠️ Statistical requirement

Report a **linear mixed model** with genotype as fixed effect and **site-year as random effect**. Do not run a separate ANOVA per season. And do not report "significant at P < 0.05" alone — the agronomic question is effect *magnitude*.

---

## 6. STAGE 3 — Molecular characterisation: the cheap, scalable options

Ranked by cost and by how much evidence they buy you.

| Option | Cost | Scalability | Evidence level | Verdict |
| --- | --- | --- | --- | --- |
| **1. Candidate-gene qRT-PCR** (SYBR, 8–12 genes, 2 contrasting genotypes × 2 treatments × 3 reps) | Low — reagents only | Medium | **L0** (association) | **Start here.** Cheapest route to a gene-level result |
| **2. Amplicon sequencing of candidate genes** across the genotype panel → SNP discovery | Low–moderate; Sanger per amplicon, or pooled amplicon NGS | High | **L0** | **Best value for money.** Finds polymorphism in the genes you already care about |
| **3. Extreme-phenotype pool sequencing** — pool tolerant extremes vs. susceptible extremes, 2–4 libraries only | Moderate, but *per library* not per genotype | High | **L0** | Cheapest genome-wide option. Allele-frequency differences between pools. Good if no candidate hypothesis |
| **4. SSR genotyping** across the panel (published *Capsicum* SSR panels) | Low | High | **L0** | Cheap and reproducible; useful for diversity and marker–trait association |
| **5. Convert SNPs → KASP assays**, validate on wider panel | ~**$0.05–0.10 per data point**; GBS discovery ~$10–50/sample | Very high | **L0** | The deployment endpoint. Only after 2, 3, or 4 succeeds |
| **6. RAPD / ISSR alone** | Very low | Low | — | ⚠️ **Avoid as your primary evidence.** Reproducibility problems; increasingly rejected by journals |

### Candidate genes for *Capsicum* drought response

Grounded in published *Capsicum* work, not invented:

| Category | Genes |
| --- | --- |
| Transcription factors | *CaDREB2*, *CaCBF*, ***CaNAC46*** (characterised in *C. annuum*; regulates salt and drought tolerance), *CaAREB/ABF*, *CaERF*, *CaWRKY* |
| Osmolyte biosynthesis | *CaP5CS*, *CaNCED* (ABA biosynthesis) |
| Protective proteins | *CaLEA*, *CaRD29B*, *CaRD22* |
| ROS scavenging | *CaSOD*, *CaCAT*, *CaPOD* |

*CaNAC46* is the best-documented *Capsicum*-specific entry point — it was shown to regulate drought and salt tolerance and to promote expression of *SOD*, *POD*, *RD29B*, *RD20*, and *P5CS* (BMC Plant Biology, 2020). It is a defensible first candidate.

### ⚠️ MIQE applies to every qRT-PCR claim

- ≥2–3 reference genes **validated for your tissue and treatment** — do not assume *CaActin* or *CaUBP* is stable; many "housekeeping" genes are themselves stress-responsive
- Primer efficiency reported
- n = biological replicates, three independent plants
- All of it reported, or the claims are not supported

### 🔴 The evidence ceiling — read this before choosing a venue

**Chilli is recalcitrant to *Agrobacterium*-mediated transformation.** Functional validation (overexpression, complementation, CRISPR) is slow, expensive, and may not succeed. That caps the entire project.

| Evidence | Requires | Realistic? |
| --- | --- | --- |
| L0 association — gene expression or allele correlates with screening index | qRT-PCR and/or amplicon sequencing | ✅ Yes |
| L1 necessity — knockdown changes tolerance | **VIGS** (virus-induced gene silencing — the affordable route in chilli) | ⚠️ Possible with effort |
| L2–L5 sufficiency, mechanism, order | Stable transformation, multiple alleles, interaction assays | ❌ Not in this project |

**Therefore the venue tier is fixed by the evidence, not by ambition:**

| Tier | Venues | Fit |
| --- | --- | --- |
| ✅ **Realistic** | *Scientia Horticulturae* · *Journal of Horticultural Sciences* · *Plant Physiology Reports* · *South African Journal of Botany* · *Vegetable Science* | Honest fit for L0–L1 |
| ✅ **Reachable if field data are strong and multi-season** | *BMC Plant Biology* · *Frontiers in Plant Science* · *PLoS ONE* · *Agronomy* (MDPI) | Possible; field validation is the selling point |
| ❌ **Not reachable** | *The Plant Cell* · *New Phytologist* · *Nature Plants* · *Molecular Plant* | Requires L4+ with transformation. Submitting here costs ~3 months to a desk rejection |

> The match table in `SKILL.md` §8 is doing exactly its job: your evidence ceiling is L0–L1, and the venue follows from that. The field validation stage is what could carry this into the middle tier — which is an argument for investing in Stage 2, not in more molecular work.

---

## 7. PLANNED FIGURE SEQUENCE

Calibrated per §12: this is a **discovery + validation** paper with an applied component.

| # | Step | Content | Level |
| --- | --- | --- | --- |
| Fig 1 | System | Workflow: screening → selection → field → molecular | — |
| Fig 2 | Dose–response | Germination % and seedling traits vs. PEG level, by genotype. Shows G×T interaction | L0 |
| Fig 3 | Ranking | Tolerance indices (STI, GSI, SSI), PCA, cluster dendrogram → tolerant/intermediate/susceptible groups | L0 |
| Table 1 | Site | Soil, weather, management per season | — |
| Table 2 | ANOVA/LMM | Sources of variation, df, F, P, variance components | — |
| Fig 4 | Field response | Yield and components, drought vs. control, across genotypes and seasons | L7* |
| **Fig 5** | **⭐ Validation** | **Lab screening index vs. field drought tolerance index — the key figure** | **L0** |
| Fig 6 | Expression | Candidate gene qRT-PCR in contrasting genotypes, control vs. stress | L0 |
| Fig 7 | Polymorphism | Sequence variation in candidate genes; marker development | L0 |
| Fig 8 | Model | Integrated selection workflow + proposed candidate genes | — |

*L7 only if the drought is managed, multi-season, and the effect sizes are agronomically meaningful. Otherwise treat Fig 4 as descriptive.

**Fig 5 is the paper.** If the correlation is weak, that is still a finding — report it. A weak correlation honestly quantified and discussed is publishable. A strong correlation assumed and not tested is not.

---

## 8. EVIDENCE AUDIT — BASELINE (re-score after every experiment)

| Claim you intend to make | Current level | Experiment that would raise it | Permitted verb |
| --- | --- | --- | --- |
| These genotypes differ in germination-stage osmotic tolerance | L0 | Stage 1 complete | "differ in" / "is associated with" |
| The lab screen predicts field drought performance | L0 | Stage 2 correlation | "predicts" *only if r is significant and reported with CI* |
| *CaNAC46* / *CaDREB2* expression is associated with tolerance | L0 | Stage 3 qRT-PCR | "is associated with" — **not "regulates"** |
| This allele confers tolerance | **Not reachable** | Requires transformation or VIGS | Do not claim |

**Last audit:** 2026-09-29 · **Next audit:** after Stage 1 phenotyping

---

## 9. OPEN DECISIONS — required before any drafting

1. Review paper, research paper, or both?
2. Target venue — or accept the tier implied by the L0–L1 ceiling?
3. How many genotypes, and from where? Is any tolerant/susceptible check included?
4. Field access: how many seasons, and can drought be **managed** rather than waited for?
5. Molecular capacity: qPCR available in-house, or outsourced? Budget ceiling?
6. Scope: does Stage 3 proceed regardless of the Stage 2 correlation, or only if the correlation holds?

> **The gate reopens when items 1–6 are answered.** Until then this worksheet is the deliverable, and no manuscript section should be drafted.
