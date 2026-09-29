# Review Paper Outline — Chilli Osmotic Stress Screening

**Topic:** In vitro screening of chilli (*Capsicum annuum* L.) genotypes for osmotic (drought) stress tolerance
**Genre:** Critical review (not systematic — see §1 justification)
**System applied:** `skills/writing-plant-science-papers/references/review-paper-blueprint.md`
**Target quality level:** **R4** — must deliver a reusable framework, not a summary

---

## 1. THE THESIS — write this first, everything follows

> **PEG-based germination screening is the cheapest and most widely used method for identifying drought-tolerant chilli genotypes, but its value is limited by three problems: PEG does not faithfully simulate drought; the screen's ability to predict field performance at the agronomically relevant stage is unvalidated, and in cereals the evidence is weak or negative; and *Capsicum* lags far behind cereals in drought marker development. The field therefore needs a standardised, stage-aware, cost-tiered pipeline rather than more one-off screens.**

Three component claims, each grounded (see §5, §6, §7). This thesis is what lifts the review from R2 to R4.

**Review type: critical / narrative, with a documented search.** Justification: a meta-analysis is not achievable here — published chilli screening studies use different PEG concentrations, different traits, different indices, and mostly report no variance measures, so no common effect size can be extracted. **State this openly in the Methods section** rather than pretending to a systematic review.

---

## 2. TITLE OPTIONS

1. *In vitro screening of chilli (Capsicum annuum L.) genotypes for osmotic stress tolerance: a critical review of methods, predictive value, and low-cost molecular prospects*
2. *From Petri dish to field: how well does osmotic stress screening in chilli predict drought tolerance?*
3. *Osmotic stress screening in chilli: a critical appraisal and a cost-tiered framework for genotype-to-marker pipelines*

Option 2 states the thesis in the title — strongest. Option 3 promises the R4 deliverable — safest for a review venue.

---

## 3. ABSTRACT SKELETON (5 sentences, per review blueprint §3)

| S | Role | Draft direction |
| --- | --- | --- |
| S1 | Why it matters | Chilli is a high-value crop in drought-prone regions; early-stage screening is attractive because it is cheap, fast, and space-efficient |
| S2 | The problem | But PEG screening is methodologically contested and its predictive validity for field performance is unestablished |
| S3 | What this review does | Synthesises N studies of osmotic screening in *Capsicum*, appraises study quality, and compiles the PEG–osmotic-potential relationship |
| S4 | The framework | Proposes a stage-aware, cost-tiered pipeline from screening to marker deployment |
| S5 | Who it is for | Breeders and labs with limited resources choosing a screening strategy |

---

## 4. SECTION-BY-SECTION OUTLINE

### 1. Introduction

- Chilli: economic importance, production constraints, drought as a major abiotic limitation
- Why early-stage screening is attractive: small space, short cycle, many genotypes, low cost, no field season required
- The problem: many screening studies, few validated outcomes; a screen that ranks genotypes in a Petri dish may not rank them in a field
- **Scope and boundaries:** this review covers osmotic stress simulation, in vitro screening in *Capsicum*, the predictive gap, and low-cost molecular options. It does **not** cover salinity, heat, or biotic stress except where the same methodologies overlap; nor transgenics as a breeding strategy
- **Methodology of this review:** databases, search strings, date range, inclusion/exclusion, records screened → included. 150–300 words. Includes the explicit statement that this is a critical review and the search may not be exhaustive

### 2. Osmotic stress simulation: agents, chemistry, and documented limitations ⭐

**This section carries the review's first critical claim. Place it BEFORE the achievements section — the limitations are what make the later synthesis necessary.**

- **PEG chemistry and the molecular-weight problem.** PEG-6000 is the most used in seed screening; PEG-3350, 4000, 8000 also appear. Molecular weight changes uptake behaviour
- **Concentration → osmotic potential.** Report the relationship and **note that published studies frequently report nominal % without verifying osmotic potential**. Michel & Kaufmann (1973) remains the standard conversion reference
- **Documented artefacts — the core of this section:**
  - PEG is absorbed by roots, translocated to shoots, and deposited on leaves in some species; associated with stomatal damage and **greater membrane injury than equivalent soil drying** (woody-species comparison, 1997)
  - Viscous PEG solutions limit oxygen diffusion → **hypoxia, a confounding stress** distinct from water deficit
  - PEG can penetrate seeds on direct contact, with toxic effects (Lawlor 1970; Sharma 1973)
  - Commercial PEG contains impurities; batch-to-batch variation
  - Osmotic potential is **temperature-dependent** — incubation temperature changes the stress actually applied
  - **PEG triggers dehydration but does not accurately simulate drought** (Plants, 2025) — the single most useful citation for this thesis
  - Documented case of PEG producing the **opposite** effect to real drought on a biological process (nodulation increased under PEG while real drought reduces it) — a clean example of why the proxy must be validated, not assumed
- **Alternatives and their own problems:**
  - Mannitol, sorbitol, sucrose — non-PEG options, but they are metabolisable/absorbable, so they alter carbon supply as well as water potential
  - Solidified PEG media and raft/membrane systems — designed to prevent PEG uptake; used in cereals
  - Soil-based or vermiculite-based drying — more realistic, less high-throughput
- **Verdict to state explicitly:** PEG is fit for **relative ranking** of genotypes under a defined, artificial osmotic stress; it is **not** a mechanistic model of field drought, and papers should stop calling the treatment "drought" without qualification

**Table 1 — Osmotic agents compared.** Columns: agent · typical concentration · osmotic potential · mechanism · documented artefacts · cost · suitability for seed screening · key reference

**Figure 2 — PEG-6000 concentration vs. osmotic potential**, compiled from published sources, each point cited. Note the temperature dependence. Label clearly as compiled, not experimental.

### 3. In vitro screening in chilli: what has been reported

- **Stages used:** germination-stage screening dominates; seedling-stage and callus/tissue-culture approaches also reported
- **Typical design:** genotype × PEG level factorial, completely randomised, 3–4 replications
- **Traits collected:** germination %, germination rate, mean germination time, germination index, root and shoot length, root:shoot ratio, seedling fresh and dry weight, seedling vigour index; some studies add proline, RWC, membrane stability
- **Tolerance indices:** GSI, SSI, STI, TOL, MP, GMP — define each, give the formula, and **state when each is appropriate and when it misleads** (Table 3)
- **Grouping methods:** PCA followed by cluster analysis, dendrograms

**Table 2 — Published osmotic screening studies in chilli.** Columns: study · genotypes (n) · screening stage · PEG level(s) & osmotic potential · traits · index used · genotypes identified as tolerant · checks included? · study limitations

Verified entries to seed the table:

| Study | n | Stage | PEG levels | Tolerant lines identified |
| --- | --- | --- | --- | --- |
| *J. Horticultural Sciences* (IIHR, 2024) | 16 | Seedling | 5% (−0.3 MPa), 10% (−0.6 MPa), 15% (−0.9 MPa) + control | UARChH 42, UARChH 43, Arka Swetha |
| RJOAS 10(118), 2021 | 22 | Germination | 15% | C7; other genotypes classified tolerant/sensitive per trait |
| Molla et al. (2019) *J. Plant Sciences* 7(4):76–85 | 47 | Germination | 12.5% | BD-10906, BD-10912, BD-10911, BD-10916, BD-10913 |
| Mollah et al. (2021) | — | Seedling | — | — |

> **Note the finding worth highlighting:** in the 22-genotype study, the commercial "drought-tolerant" check (Gada MK) was classified only *moderately* tolerant. The authors attributed this to tolerance being mechanism- and stage-specific. **That is direct published evidence for this review's thesis** — use it.

- **A recurring methodological weakness to name:** pseudo-replication. Germination percentage is frequently analysed by ANOVA with seeds as the unit. Germination is binomial and the experimental unit is the dish or plot, not the seed. Recommend GLMM with a binomial family. Report this as a **critical finding about the literature**, with a count of how many studies do it

### 4. The predictive gap: does the Petri dish predict the field? ⭐⭐

**This is the review's intellectual centre and, most likely, its original contribution. No one appears to have synthesised this for *Capsicum*.**

- **The assumption under test:** that ranking genotypes by germination under PEG predicts their field performance under drought
- **Evidence from cereals, where this has been tested directly:**
  - A 2024 barley study of 164 lines, explicitly designed to test "the reliability of proxy methods," found germination rate under PEG correlated **negatively (r = −0.25)** with seed yield under drought at heading — an outcome the authors called unexpected
  - The same study found germination percentage correlated **negatively** with root:shoot fresh weight under PEG (r = −0.37)
  - Some genotypes performed better under PEG than under control — which should be biologically impossible for a true water-deficit stress, and is itself evidence that PEG introduces non-drought effects
- **Why the gap exists:** germination-phase osmotic tolerance and reproductive-stage drought tolerance involve different mechanisms. Chilli is typically drought-stressed at **flowering and fruit set**, not at germination. A genotype can be tolerant at one stage and sensitive at another — the very phenomenon the 22-genotype chilli study observed
- **Consequences if the gap is real:** screening at germination selects for germination-stage tolerance. If that is not the target trait, the screen is efficiently identifying the wrong genotypes
- **What is missing from the chilli literature specifically:** no published multi-season study appears to correlate germination-stage PEG screening indices against field drought performance in *Capsicum*. **State this as an identified gap and a falsifiable prediction** — this is the R5 move

**Figure 3 — The stage-specificity problem.** Conceptual schematic: germination-stage tolerance, seedling-stage tolerance, and reproductive-stage tolerance as partially overlapping sets, with the PEG screen targeting the first and field yield determined by the third. Label as schematic.

### 5. Molecular basis of drought response in *Capsicum*

- **Genome resources:** *C. annuum* CM334 and Zunla-1 assemblies; *C. chinense*, *C. baccatum* available. Genome availability is not the bottleneck
- **Candidate gene families:** DREB/CBF, NAC, AREB/ABF, ERF, WRKY, MYB transcription factors; *P5CS* and *NCED* (osmolyte and ABA biosynthesis); *LEA*, *RD29B*, *RD22*; *SOD*, *CAT*, *POD* (ROS scavenging)
- **Best-characterised *Capsicum* entries:** ***CaNAC46*** — a NAC (ATAF subfamily) transcription factor induced by drought, salt, cold, heat, ABA, salicylic acid and methyl jasmonate; promotes expression of *SOD*, *POD*, *RD29B*, *RD20*, *ABI* and *P5CS*; silencing increases malondialdehyde under stress. *DREB1* in pepper has also been associated with drought tolerance via activation of drought-inducible genes
- **Correction to note:** much *Capsicum* gene work is validated by **heterologous expression in *Arabidopsis***, not in chilli. That is a lower evidence level than it is often reported as — say so

**Table 4 — Candidate genes with evidence level.** Columns: gene · family · evidence type (transgenic in *Arabidopsis* / expression only / mutant / VIGS) · level · organism of validation · reference

- **The gap that makes this section matter:** *Capsicum* GWAS and QTL work has concentrated on fruit quality, yield components, and disease resistance (e.g. *Phyto5.2* for *Phytophthora capsici*; GWAS for fruit traits). **Validated drought-tolerance QTL or markers for chilli are conspicuously scarce.** Contrast with cereals, where drought QTL and KASP markers exist

### 6. Low-cost, scalable genotyping: options for resource-limited laboratories ⭐

**This section answers the practical question directly and is a major part of the R4 deliverable.**

| Approach | Cost | Scale | Equipment | Evidence bought |
| --- | --- | --- | --- | --- |
| **SSR genotyping** | Low | High | Thermal cycler + gel or capillary | Marker–trait association; validated *Capsicum* SSRs exist, including markers associated with stress tolerance index |
| **Amplicon sequencing of candidate genes** | Low–moderate | Medium–high | Cyclers + sequencing service | SNP discovery in genes you already have reason to suspect |
| **Extreme-phenotype pool sequencing** | Moderate **per library**, not per genotype | High | Sequencing service | Genome-wide allele-frequency differences from only 2–4 libraries |
| **GBS / RAD-seq** | ~$10–50 per sample | High | Sequencing service | Genome-wide markers for GWAS or diversity |
| **KASP assays** | ~$0.05–0.10 per data point | Very high | Standard real-time PCR instrument | Deployment: routine screening of many lines with few markers |
| **RAPD / ISSR alone** | Very low | — | Gel documentation | ⚠️ Reproducibility problems; increasingly rejected. Not recommended as primary evidence |

- Note that **KASP runs on standard real-time PCR instruments**, which is what makes it accessible — the barrier is assay design, not equipment
- Present the **tiered decision framework** (Figure 4): what a lab with only PCR should do; what a lab with qPCR should do; what to outsource
- **Report negative cost/benefit honestly:** SSR and amplicon approaches are cheap but discovery-limited; pool-seq and GBS buy breadth but require bioinformatics capacity that may be the real constraint, not money

**Table 5 — Genotyping platforms compared.** Columns: platform · cost per sample/data point · markers per sample · equipment · bioinformatics required · off-the-shelf vs. custom · best use case

### 7. Synthesis: a proposed integrated framework ⭐ THE R4 DELIVERABLE

Present as **Figure 1** (pipeline with decision points) plus **Table 6** (proposed minimum reporting standard).

```
STAGE 1 — Screen
  · ≥20 genotypes including a known tolerant and susceptible check
  · ≥3 PEG levels; osmotic potential VERIFIED with an osmometer
  · Petri dish = experimental unit; ≥4 replicates
  · GLMM (binomial) for germination; report G×T interaction, not just
    performance at the highest stress
  · Compute multiple tolerance indices; group by PCA + clustering
  · Retain a SPECTRUM (tolerant / intermediate / susceptible)
      ↳ Not only extremes: selection truncation attenuates the very
        correlation you will later test
  DECISION: which genotypes advance?

STAGE 2 — Validate (the step most often omitted, and the reason the
          literature has not answered the central question)
  · Field, managed drought at the agronomically relevant stage
  · Irrigated control; RCBD; ≥2 seasons; site-year as random effect
  · Report correlation between screening index and field drought response
  DECISION: does the screen predict the field? If not, the screen is
            a selection tool for a different trait — say so

STAGE 3 — Characterise
  · Contrasting genotypes (tolerant vs susceptible pairs)
  · Candidate-gene qRT-PCR (MIQE-compliant; validated reference genes)
  · AND/OR amplicon sequencing of candidate genes across the panel
  DECISION: is there an expression and/or sequence difference?

STAGE 4 — Deploy (only if Stage 3 succeeds)
  · Convert polymorphism to CAPS / KASP / SSR assay
  · Validate marker–trait association in the wider panel
  · Independently derived material required
```

**Table 6 — Proposed minimum reporting standard**, which is what future papers should be held to:

| Parameter | Minimum | Rationale |
| --- | --- | --- |
| Genotypes | ≥20, including tolerant and susceptible checks | Enables ranking and anchors the scale |
| Osmoticum | PEG molecular weight and supplier stated | Behaviour is MW-dependent |
| Osmotic potential | Measured, not nominal | Batch and temperature variation |
| Temperature | Stated and controlled | Osmotic potential is temperature-dependent |
| Experimental unit | Petri dish (or plot), stated explicitly | Prevents pseudo-replication |
| Replication | ≥4 units, ≥10 seeds per unit | GLMM stability |
| Statistical model | GLMM binomial for germination % | Percentages are not normal |
| Interaction | G × treatment reported | Separates tolerance from general vigour |
| Indices | ≥2 reported, with justification | Single indices mislead |
| Selection range | Spectrum retained, not extremes | Prevents correlation attenuation |
| Field validation | Multi-season, managed drought | The only test of predictive value |

### 8. Future directions

Specific and testable, tied to the gaps identified:

- A multi-season study correlating germination-stage PEG indices against field drought response in *Capsicum* — the single most valuable missing experiment
- A comparison of PEG against a soil-drying control in chilli, testing whether the two rank genotypes identically. **If they do not, the PEG literature's rankings are not transferable**
- Whether tolerance rankings are stable across germination, seedling, and reproductive stages in chilli
- Drought-focused GWAS in chilli using diverse panels, which is where the crop lags cereals most
- VIGS-based functional testing of *CaNAC46* and *CaDREB* orthologs in chilli itself, rather than in *Arabidopsis*

### 9. Conclusion

- Restate the thesis: PEG screening is cheap, useful, and **oversold** — and the field's central question (does it predict the field?) remains untested in chilli
- State explicitly what would change the conclusion: a multi-season chilli study showing strong correlation between the screen and field performance would vindicate the approach and make the existing literature far more valuable than it currently is

---

## 5. FIGURE PLAN

| Figure | Type | Content |
| --- | --- | --- |
| Fig 1 | Conceptual | Integrated screening → validation → characterisation → deployment pipeline with decision points |
| Fig 2 | Compiled | PEG-6000 concentration vs. osmotic potential, points cited |
| Fig 3 | Conceptual | Stage-specificity of drought tolerance — the predictive gap |
| Fig 4 | Conceptual | Cost-tiered decision framework for resource-limited labs |
| Tables 1–6 | — | Per §4 above |

**All conceptual figures must be labelled as conceptual.** Do not present a schematic as data. This is the integrity rule most often broken in reviews.

---

## 6. INTEGRITY — the specific constraints on this review

You said you would use "hypothetical genotypes and no real varieties." Here is the precise line:

| ✅ Legitimate in a review | ❌ Not legitimate |
| --- | --- |
| Tabulating how many genotypes each **real, cited** study used | Reporting results from genotypes that were never tested |
| Proposing a **recommended** panel size for future work | Presenting those recommendations as findings |
| Generic placeholders (`Genotype A`, `Genotype B`) in a **conceptual schematic**, labelled as schematic | A table of "representative genotypes" that are not real and cited |
| A worked example labelled `illustrative example` | Presenting modelled values as experimental results |
| Citing real tolerant lines identified in real studies (UARChH 42, BD-10906, etc.) | Attributing findings to the wrong paper |

**The test:** could a reader verify this against the source? If not, it must be labelled conceptual.

Also note: **you now need no field access and no laboratory at all** for this review. The absence of your own data is not a weakness here — the review's contribution is synthesising what others have done. Your earlier four-stage plan is not wasted; it becomes **Figure 1 and Table 6**, presented as a proposed framework rather than as your experiment.

---

## 7. NEXT STEPS

1. Run the literature search and complete **Table 2** — it is the review's backbone
2. Extract PEG concentration → osmotic potential values from each study for **Figure 2**
3. Verify every citation against the source
4. Draft the synthesis section (§7) first — it is the deliverable
5. Score the draft against the Review Quality Ladder. **Below R4, revise before submitting**
6. Confirm the target venue accepts unsolicited reviews and check its length limit
