# Draft — Sections 6 and 7

**Status:** First draft. §6 cost figures now from peer-reviewed sources only (§6.5).
**Combined word count:** ~3,100

---

## 6. Low-cost, scalable genotyping: options for resource-limited laboratories

Sections 4 and 5 establish that early-stage screening ranks genotypes for tolerance at that stage, and that the field disagrees about whether those rankings transfer. For a laboratory that has completed a screen with limited resources, the practical question is what to do next. This section compares the available genotyping platforms on the criteria that actually constrain such laboratories — not only cost, but equipment availability and the bioinformatics capacity required.

### 6.1 The constraint is often not money

Cost per data point is the headline metric and the least useful one in isolation. Three constraints bind in practice, and they bind differently:

| Constraint | Binds when |
| --- | --- |
| **Equipment** | No real-time PCR instrument, no capillary sequencer, no access to a sequencing service |
| **Bioinformatics capacity** | No one able to process raw reads, call variants, or run association analysis |
| **Money** | Which is often the least binding, because the cheapest methods are also the most labour-intensive |

Genome-wide approaches are frequently presented as the affordable option because sequencing costs have fallen. They are affordable in reagents and demanding in analysis. A laboratory with a thermal cycler, a gel documentation system and no bioinformatician is better served by a small number of targeted assays than by a sequencing dataset it cannot interpret.

### 6.2 Targeted assays requiring only PCR

**Simple sequence repeat (SSR) genotyping** remains the most accessible route to a marker–trait association. It requires a thermal cycler and either gel electrophoresis or a capillary sequencer, both widely available, and validated *Capsicum* SSR panels are published. Markers **Hpms1172** and **CAMS177**, for example, have been associated with stress tolerance index in chilli across a 78-genotype panel ✅, and the study's principal coordinate analysis aligned with its marker-assisted selection output. The limitations are intrinsic: SSRs are low-density, they sample only a small number of loci, and they cannot detect a causal polymorphism unless it happens to be in linkage disequilibrium with the amplified repeat — which in a crop with the linkage decay characteristics of pepper may be a substantial distance.

**Amplicon sequencing of candidate genes** is the highest-value option for a laboratory with PCR access and a sequencing service. Rather than screening the genome, it interrogates the genes the literature already implicates — *CaNAC46*, *CaDREBLP1*, *CaDREB*, the *CaP5CS* and aquaporin families — across the genotype panel, and identifies sequence polymorphism within them. It is cheap because the target is small, it produces interpretable variants rather than anonymous markers, and it generates a hypothesis that can be tested. Its limitation is equally clear: it can only find variation in genes someone has already chosen to look at.

### 6.3 Genome-wide approaches

**Bulk segregant analysis with sequencing (BSA-seq)** is the most cost-effective genome-wide strategy for a trait with contrasting extremes, because it reduces the genotyping unit from the individual to the pool ✅. Two pools of extreme-phenotype individuals from a segregating population are sequenced, and allele-frequency differences between them localise the contributing region ✅. It requires only two sequencing reactions, which is why it is described in the literature as standing out among QTL mapping methods as the most cost-effective ✅.

Two caveats matter for pepper specifically, and both are biological rather than logistical.

First, **BSA-seq accuracy depends on sequencing depth and coverage**, so cost rises with the resolution sought ✅. Second, and more limiting, **its application is constrained in species with large genomes** ✅. *Capsicum annuum* has an approximately 3.5 Gb genome — among the larger among cultivated Solanaceae — which raises the sequencing requirement substantially relative to rice or *Arabidopsis*. BSA-seq is therefore a reasonable option in pepper, but not the near-free one it is in small-genome crops.

**Genotyping-by-sequencing** provides genome-wide markers at approximately **US$10–50 per sample** ✅ and has been applied in pepper, including for QTL mapping of *Phytophthora capsici* resistance via combined QTL and association analysis ✅. A **PepperSNP 16K array** has also been used to genotype a GWAS panel ✅, which is the appropriate choice where an off-the-shelf array exists and the panel is large.

### 6.4 Deployment: converting a discovery into a routine assay

Discovery and deployment are different problems, and the affordable platform for each is different. **Kompetitive allele-specific PCR (KASP)** assays run on a standard real-time PCR instrument, require no gel electrophoresis, and cost approximately **US$0.05–0.10 per data point** ✅ — one to two orders of magnitude below genome-wide approaches on a per-sample basis. A published comparison of PCR-based SNP genotyping platforms positions KASP and PACE as the most cost-effective options for small laboratories, noting explicitly that "the ability to perform KASP assays on standard real-time PCR instruments makes it accessible to a broader range of laboratories, including those with limited resources" ✅.

The barrier to KASP adoption is therefore not equipment but **assay design**, which requires a known polymorphic site. This is the operational reason to sequence candidate genes first: it produces the variant that a KASP assay then deploys.

| Platform | Cost | Markers | Equipment | Bioinformatics | Best use |
| --- | --- | --- | --- | --- | --- |
| SSR | Low | 1–50 | Thermal cycler + gel/capillary | Minimal | Diversity, rough association |
| Amplicon sequencing | Low–moderate | Candidate gene panel | Cyclers + sequencing service | Moderate | **Best value for a lab with PCR** |
| BSA-seq | Moderate; depth-dependent | Genome-wide | Sequencing service | Substantial | Extreme phenotypes, moderate genomes |
| GBS / RAD-seq | ~US$10–50/sample | Genome-wide | Sequencing service | Substantial | GWAS, mapping populations |
| SNP array | Moderate | Fixed, ~16K | Array service | Moderate | Large panels, standard panels |
| **KASP** | **~US$0.05–0.10/data point** | Few, specific | **Standard real-time PCR** | Minimal | **Deployment and routine screening** |

### 6.5 A note on platform costs

Cost figures for genotyping platforms are frequently sourced from vendor material rather than peer-reviewed literature, and vendor pricing changes. The figures used above are drawn from a peer-reviewed review of PCR-based SNP genotyping ✅ and from the same source for sequencing-based approaches ✅. Laboratories budgeting a project should treat them as order-of-magnitude indicators and obtain current quotations.

**Table 6** — Genotyping platforms compared.

---

## 7. Synthesis: a proposed framework and minimum reporting standard

### 7.1 What the review has established

The preceding sections support four conclusions, and they are more encouraging than a critical reading of any one of them suggests.

**Early-stage osmotic screening works, in the sense that it discriminates.** It has produced tolerant germplasm in every Solanaceae crop examined, at low cost, without a field season, and independently in many laboratories (Section 3). The genetic variation it detects is real.

**It does not currently function as a general proxy for field drought tolerance, and the field does not agree on whether it can.** Of the studies that test transfer across developmental stages, four support it and four contradict it (Section 4). The disagreement is not random: it tracks identifiable design choices.

**Those design choices are cheap to fix.** Internal-consistency correlation being reported as cross-stage transfer, trait-level tests being used where genotype-level concordance is required, fixed PEG concentrations applied where genotype-specific levels are needed, and variation in developmental stage being ignored — each has a remedy that costs little (Sections 3 and 4).

**The molecular route is more open than it was.** Pepper's transformation recalcitrance has historically capped functional validation, but virus-induced gene silencing and, more recently, heritable virus-induced gene editing now provide tissue-culture-free routes (Section 5). The constraint has moved from capability to coordination.

### 7.2 Why the field's choices were reasonable

Each of the practices the review identifies as limiting was, and remains, a defensible response to real constraints. Stating this is not a courtesy — it explains why the recommendation in Section 7.3 is a standard rather than a correction.

**Fixed PEG concentrations** are the only practical choice when a screening panel is large and no prior information about individual genotypes exists. Genotype-specific determinations require a pre-experiment that many screening programmes are not resourced to run.

**Analysis of variance** on germination data has a long and accepted history in seed science, and for crops with uniform high germination the assumptions are met in practice. The conditions that osmotic screening creates — means driven toward 0% and 100% — are precisely those where the method's assumptions fail, and this follows from the experimental design rather than from analytical carelessness.

**Reporting the non-penetration of PEG as established** was reasonable when first advanced and has been reproduced in the introductions of hundreds of papers since. The original measurements predate the modern publication cycle by five decades and are effectively outside the citation reach of most authors writing today.

**Testing at a single developmental stage** is what makes screening cheap. A programme that tests all stages is no longer a screening programme; it is a breeding pipeline, and it costs proportionally more.

The recommendation that follows is therefore offered as a shared standard that would make the existing literature cumulative, not as a criticism of how it was produced.

### 7.3 The proposed framework

**Figure 1** presents the framework. It has four stages with explicit decision points.

```
STAGE 1 — SCREEN
  Panel          ≥20 genotypes, INCLUDING wild relatives and at least one
                 known tolerant and one known susceptible check
  Osmoticum      PEG molecular weight, supplier and batch recorded
  Concentration  Genotype-specific sub-lethal level where feasible;
                 otherwise ≥3 levels spanning the informative range
  Verification   Osmotic potential MEASURED, with the instrument named
  Environment    Temperature controlled and reported
  Unit           Petri dish = experimental unit; ≥4 replicates; ≥10 seeds each
  Traits         Germination %, rate, MGT, index; root and shoot length;
                 root:shoot; fresh and dry weight; vigour index
  Analysis       GLMM, binomial family, logit link, dish as random effect;
                 report the genotype × treatment interaction
  Indices        ≥1 productivity-oriented AND ≥1 susceptibility-oriented
  Selection      Retain a SPECTRUM — tolerant, intermediate, susceptible
  DECISION →     Which genotypes advance, and on what stated criterion?

STAGE 2 — VALIDATE
  Design         Managed drought at the agronomically relevant stage;
                 irrigated control; RCBD; ≥2 site-years
  Analysis       Mixed model with site-year as random effect
  Reporting      THE CONCORDANCE RATE — the proportion of screen-selected
                 genotypes that prove superior in the field
  DECISION →     Does the screen predict the field? If not, state that the
                 screen selects for a different trait, which is itself a result

STAGE 3 — CHARACTERISE
  Material       Contrasting genotype pairs from Stage 1
  Expression     Candidate-gene qRT-PCR (MIQE; reference genes validated
                 for the tissue and treatment, not assumed)
  Sequence       Amplicon sequencing of candidate genes across the panel
  Functional     VIGS, or virus-induced gene editing where available
  DECISION →     Is there an expression and/or sequence difference?

STAGE 4 — DEPLOY
  Assay          Convert polymorphism to KASP, CAPS or SSR
  Validation     Test marker–trait association in an independent panel
  Reporting      Marker effect size and the genotype concordance rate
```

**Table 7 — Proposed minimum reporting standard.** This is the review's principal deliverable and is offered as a checklist for authors, reviewers and editors. Every item is either free or inexpensive to satisfy, and every item is currently omitted by a substantial fraction of the literature.

| # | Parameter | Minimum | Rationale |
| --- | --- | --- | --- |
| 1 | Genotype panel | ≥20, including wild relatives and tolerant/susceptible checks | Checks anchor the ranking; wild relatives carry tolerance not represented in cultivars |
| 2 | Osmoticum identity | PEG molecular weight, supplier, batch | Osmotic pressure at equal mass varies with molecular weight; the cellular site of action differs |
| 3 | Concentration | Genotype-specific sub-lethal level where feasible; otherwise ≥3 levels | A single fixed level produces floor effects at the extremes |
| 4 | Osmotic potential | **Measured**, instrument named | Nominal values carry temperature- and method-dependent error |
| 5 | Temperature | Controlled and reported | Osmotic potential is temperature-dependent |
| 6 | Experimental unit | Petri dish (or plot), stated explicitly | Prevents pseudoreplication; the unit is not the seed |
| 7 | Replication | ≥4 units, ≥10 seeds per unit | Generalised linear model stability |
| 8 | Statistical model | GLMM, binomial, logit link for germination % | Binomial data violate normal-error assumptions, especially near boundaries |
| 9 | Interaction term | Genotype × treatment reported | Separates stress tolerance from general vigour |
| 10 | Indices | ≥1 productivity-oriented and ≥1 susceptibility-oriented, with justification | Index choice determines genotype ranking |
| 11 | Selection range | Spectrum retained | Selecting only extremes truncates the predictor and attenuates any later correlation |
| 12 | Correlation reporting | Separate internal (within-treatment) from cross-stage correlations | Internal concordance is not evidence of transfer |
| 13 | Field validation | Multi-season, managed drought | The only test of predictive value |
| 14 | Concordance rate | Reported where a screen feeds a breeding programme | The quantity that matters is genotype overlap, not trait correlation |
| 15 | Terminology | "Osmotic stress induced by PEG," not "drought" | The treatment does not simulate drought |

### 7.4 What adoption would change

The standard is deliberately undemanding. Items 6, 8, 9, 10, 12 and 15 are reporting or analysis choices that require no additional experiment, no additional material and no additional field season. Items 1, 2, 3, 7 and 11 are design choices within existing budgets; genotype-specific concentration determination (item 3) is the only one requiring a preliminary experiment, and it is optional where resources are constrained.

The substantive change would be item 14. **If screening studies routinely reported the proportion of their selected genotypes that proved superior in field evaluation, the question this review identifies as unresolved would be answered within a few publication cycles, using data that screening programmes are already generating.** The information exists; it is simply not reported in a form that permits synthesis.

**Table 7** — Minimum reporting standard.
**Figure 1** — The proposed framework, with decision points at each stage.
