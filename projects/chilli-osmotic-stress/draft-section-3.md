# Draft — Section 3: Screening in the Solanaceae — What Has Been Reported

**Status:** First draft. Statistical critique grounded in a systematic review of the field rather than my own count (see §3.4).
**Word count:** ~2,400 (target 2,200–2,600)
**Register:** Descriptive then analytical. **This section deliberately includes an account of what the screening literature has achieved** — required for balance, and for the review to be accepted rather than rejected as an attack.

---

## 3. Screening in the Solanaceae: what has been reported

### 3.1 The shape of the literature

Across the three crops, the screening literature has a consistent architecture. Genotypes are exposed to an osmoticum, usually PEG-6000, at one to four concentrations spanning roughly 5–20% (w/v), with germination and early seedling traits scored over 7–14 days. Almost all studies use a completely randomised design with three or four replications, and most report germination percentage, germination rate or index, root and shoot length, seedling fresh and dry weight, and a derived vigour index. A substantial minority add physiological or biochemical traits — proline, relative water content, membrane stability, antioxidant enzyme activity.

The three crops differ in emphasis rather than in approach:

| Crop | Screening stage | Distinguishing feature |
| --- | --- | --- |
| ***Capsicum*** | Germination and early seedling | Largest number of independent genotype panels; usually cultivar and breeding-line material |
| **Tomato** | Germination, seedling, and callus/tissue culture | Only crop with *in vitro* selection at the callus level; larger panels and more indices |
| **Eggplant and wild *Solanum*** | Vegetative and whole-plant | Screens wild relatives alongside cultivars; the only crop where wild material is routine in panels |

The eggplant contrast is worth stating plainly at the outset, because it frames Section 5: **eggplant screening panels routinely include wild relatives, while *Capsicum* panels almost never do** — despite a pepper pan-genome demonstrating that abiotic-stress tolerance genes are carried in *C. baccatum* introgressions ✅. The tolerance germplasm appears to be present and largely unexamined in pepper's screening literature.

### 3.2 Traits, indices, and what each can support

The trait set is largely settled across the field, which is a strength — it makes studies comparable. The index set is not.

Germination percentage is the near-universal primary trait, and it is the one that carries the most interpretive weight in conclusions. Germination rate, mean germination time and germination index capture the timing dimension that a final percentage obscures. Root length, shoot length and the root:shoot ratio are the standard morphological traits, with root traits frequently advanced as mechanistically relevant because greater root length enables access to deeper soil water ✅. Seedling dry weight and the derived vigour index (typically seedling length × germination percentage) integrate growth over the assay.

**Tolerance indices deserve separate treatment, because they are used interchangeably and are not interchangeable.** Table 3 should carry the formulas and, critically, the failure mode of each:

| Index | Basis | What it captures | Failure mode |
| --- | --- | --- | --- |
| **SSI** — stress susceptibility index | Reduction relative to the population mean | Degree of yield loss under stress | Rewards inherently low-yielding genotypes; says nothing about productivity |
| **STI** — stress tolerance index | Yield under stress × yield under control ÷ mean² | Productivity under both conditions | Requires a meaningful control yield; less informative under severe stress |
| **TOL** — tolerance | Simple difference Yc − Ys | Absolute yield loss | Genotype with high potential yield can look sensitive |
| **MP / GMP** — mean / geometric mean productivity | Mean across environments | Productivity across both | GMP penalises extreme response; neither identifies stress-specific adaptation |
| **YSI** — yield stability index | Ys / Yc | Stability of performance | Rewards a genotype equally poor under both conditions |
| **DRI / MGIDI** — drought response / multi-trait genotype–ideotype distance | Multi-trait rank aggregation | Composite ranking | Weights are investigator-chosen; ranking sensitive to weighting |

The distinction between productivity-oriented and susceptibility-oriented indices is well documented in the wider literature: productivity indices (STI, GMP, HM, YSI) correlate strongly with yield under both conditions, while susceptibility indices (SSI, TOL, SSPI) primarily reflect the extent of stress-induced loss ✅. **They can rank the same genotypes differently**, and a recent integration study makes the consequence explicit: the choice of index "directly influences genotype ranking and selection decisions" ✅. Similar inconsistency has been documented in chickpea, where ATI, SSPI, YSI, PYR and TOL gave conflicting rankings ✅.

**This is the single most tractable methodological problem in the screening literature, and it has a cheap solution already in use:** report at least one productivity-oriented and one susceptibility-oriented index, and state the reason for the choice. The studies that already do this are the ones whose genotype rankings are most likely to transfer.

### 3.3 What the literature has achieved

It is necessary to state this directly, because the remainder of this section and Section 4 examine limitations that could otherwise be read as a general dismissal. They are not.

**The screening literature has produced concrete, usable tolerant germplasm.** In *Capsicum*, a 16-genotype screen across three PEG levels identified UARChH 42, UARChH 43 and Arka Swetha as tolerant ✅. A 47-genotype emergence screen identified five tolerant lines (BD-10906, BD-10912, BD-10911, BD-10916, BD-10913) and five susceptible ones, with a dendrogram resolving four clusters at a cophenetic correlation of 0.668 ✅. A 22-genotype study identified C7 as tolerant across all measured traits ✅. In tomato, a five-genotype screen identified NGRCO9569, Monoprecos and Khumal 2 as maintaining germination, vigour and biomass under stress, with Srijana failing completely at 6% PEG ✅. In the wider *Capsicum* germplasm, a 100-accession vegetative-stage screen identified IT308761, IT250221 and IT158637 as resistant through 21 days of water withholding, corroborated under greenhouse conditions ✅.

**None of this would exist without the screening approach.** The method is cheap, requires no field season, discriminates among genotypes, and has been applied independently by many groups to produce converging evidence that genetic variation for early-stage osmotic tolerance exists and is substantial. The question this review addresses is not whether the method works — it does — but **how much its outputs can be generalised**, and that question is answered in Section 4.

**A methodological good practice is also worth crediting.** A recent tomato callus-selection study determined a **genotype-specific sub-lethal PEG concentration (LC50)** for each line rather than applying one arbitrary threshold to all ✅. The authors' reasoning — that a fixed concentration is arbitrary and may be above or below the informative range for a given genotype — is correct, and the approach should be adopted more widely. It is the single most transferable methodological improvement identified in this review.

### 3.4 Statistical practice: a documented field-wide problem

Germination percentage is binomial: a count of successes from a fixed number of trials, bounded at 0 and 100%. Analysis of variance assumes normally distributed errors with homogeneous variance, and these assumptions are violated by such data, often severely, particularly when means approach the boundaries.

This is not an impression formed from reading a subset of papers. A systematic critique of statistical practice in seed germination and viability research examined **429 studies** and found ✅:

| Practice | Proportion |
| --- | --- |
| Analysis of variance | **70%** |
| Generalised linear models | 13% |
| Non-parametric tests | 11% |
| Generalised linear mixed models | 4% |
| Linear mixed models | 2% |

Among studies that transformed their data, **arcsine transformation was used in 87.6%** — a transformation now specifically discouraged for binomial data, on the grounds that logistic regression offers greater interpretability and higher power, and that the transformation produces nonsensical predictions for non-binomial proportions ✅. In the same systematic review:

- **In 15 of 429 studies the number of replicates was not even stated** ✅
- **A single replication per treatment was used in 4.4% of studies** ✅
- **Pseudoreplication was recorded in 17.4% of studies using logistic regression** — where "treatments were applied to a single experimental unit (e.g. Petri dishes) and each seed was treated as a replicate" ✅
- **Only 9.6% of studies that transformed their data checked whether the transformation had achieved the intended effect** ✅
- **Lack of emphasis on effect sizes** was identified as a further area of concern ✅

The reviewer's conclusion is worth quoting, because it applies directly to the screening literature this review catalogues: *"Given the prevalence of these problems, in my opinion we would be building a body of knowledge on a shaky ground."* ✅

**Chilli-specific practice conforms to this pattern.** A 2025 study optimising chilli germination used a completely randomised 8 × 3 factorial design with 30 seeds per replicate across 24 Petri dishes and analysed the results by analysis of variance ✅. A chilli seed-priming study used CRD with three replications and 50 seeds per replication, analysed as a factorial CRD ✅. A chilli GA₃ study used 240 seeds distributed across 12 Petri plates with three replications, analysed by ANOVA ✅. None of these reports a generalised linear model.

**The qualification must be stated fairly, because the issue is not simple.** Analysis of variance is not automatically wrong here. Where data fall within roughly 30–70% germination, the response is approximately linear, variance heterogeneity is modest, and classical ANOVA with equal group sizes is reasonably robust ✅. When the number of observations per group is large, the binomial distribution approximates the normal ✅. And a direct comparison of model fits found that where all ANOVA assumptions were met, ANOVA remained defensible ✅.

**The problem is not the use of ANOVA. It is the use of ANOVA in the conditions where it fails.** Drought screening specifically drives germination percentages toward the boundaries — toward 0% under severe stress or 100% under control — which is precisely the region where ANOVA's assumptions break down and where arcsine transformation performs worst. A study that screens at 0%, 5% and 15% PEG will produce a control near 100% and a severe-stress treatment near 0%; that is the worst-case configuration for the analysis method the field uses by default. The correct approach is a generalised linear model with a binomial family and a logit link, ideally with the Petri dish as a random effect to account for within-dish correlation — and the dish, not the seed, as the experimental unit.

**A second, related problem is the ceiling effect.** Most tomato genotypes failed to germinate entirely above −0.35 MPa ✅, and the same has been reported for wheat and barley at high PEG concentrations ✅. When a stress level drives all genotypes to zero, it produces no information about relative tolerance — yet such treatments are frequently reported and interpreted. This is an argument for genotype-specific stress levels (§3.3) rather than a fixed concentration for the whole panel.

**Table 3** — Tolerance indices: formula, what it measures, failure mode, and when to use it.

**Table 4** — Published screening studies, by crop, with design, traits, indices, identified genotypes, and stated limitations. Populated in the study inventory.

---

## Reviewer-facing notes

1. **§3.3 is not filler — it is the section's credibility.** A review that catalogues only methodological failures reads as hostile and will be reviewed accordingly. Naming the germplasm the screens produced, and crediting the LC50 innovation, costs ~350 words and buys the right to be critical in §3.4 and §4.
2. **Do not claim to have counted the chilli studies personally.** The 70% / 87.6% / 17.4% figures come from a systematic review of 429 studies ✅, and should be attributed as such. Presenting my own informal reading as a count would be misrepresentation. The chilli examples are illustrative of the pattern, not a survey.
3. **State the ANOVA qualification.** §3.4's middle paragraph — that ANOVA is defensible in the 30–70% range with equal n — is essential. Without it, the critique is overbroad and a statistically literate referee will say so.
4. **The strongest form of the argument is conditional, not absolute.** Not "the field uses the wrong test" but "the field's default test fails in exactly the conditions drought screening creates." That formulation is both more accurate and harder to attack.
5. **The 30–70% point is the review's best statistical insight.** Control near 100%, severe stress near 0%, analysed by a method that requires normality and homogeneous variance — this should be stated as a specific, checkable prediction about which studies are affected.
6. **Cite the source of every figure in Table 3.** Index formulas are frequently misattributed.
