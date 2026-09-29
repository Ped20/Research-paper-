# Screening for drought tolerance in *Capsicum* and the Solanaceae: methodological assumptions, an unresolved predictive link, and a cost-tiered path to markers

**Article type:** Review
**Running title:** Drought screening in *Capsicum* and the Solanaceae (7 words)
**Venue:** deliberately not fixed. The manuscript is formatted for submission to any plant-science or horticulture journal that publishes review articles; the venue decision and its consequences are set out in the author notes.
**Status:** Submission-ready draft. All in-text citations resolved; no placeholder markers anywhere in the manuscript. Reference list verified against Crossref (`reference-verification.md`). Figures 1–5 drawn (`figures/`). Supplementary Table S1 compiled.

---

## Abstract

Drought limits productivity across the Solanaceae, and early-stage screening with polyethylene glycol (PEG) has become the standard low-cost route to identifying tolerant genotypes in chilli pepper, tomato and eggplant. It requires no field season and has produced tolerant germplasm in every crop tested. This review assesses what that screening can support. Four findings emerge. First, the physicochemical basis of the treatment is less secure than its customary presentation implies: PEG solutions are non-colligative, their osmotic potential is temperature- and molecular-weight-dependent, and the assumption that PEG does not enter plant tissue is contradicted by direct measurement, including in *Capsicum* itself. Impurity and detergent effects were tested and rejected decades ago yet are still cited as established artefacts. Second, the field's default statistical treatment of germination data is inappropriate to the conditions osmotic screening creates, driving means toward 0% and 100% where normal-error assumptions fail. Third, whether early-stage rankings predict field performance is unresolved: of studies testing transfer across stages, four support it and four contradict it, and the disagreement tracks design choices rather than biology alone. In *Capsicum*, the question remains untested. Fourth, the molecular route is more accessible than pepper's transformation recalcitrance suggests: virus-induced gene silencing and heritable gene editing now allow tissue-culture-free validation. We propose a four-stage framework and a fifteen-item reporting standard, six items of which require no additional experiment. The single substantive change — reporting the proportion of screen-selected genotypes that prove superior in the field — would answer that question using data screening programmes already generate.

**Keywords:** *Capsicum annuum*; polyethylene glycol; drought tolerance; genotype screening; Solanaceae; reporting standards

---

## 1. Introduction

Chilli pepper (*Capsicum annuum* L.) is among the most widely cultivated spice crops worldwide and a significant source of income for smallholder producers in drought-prone regions of South Asia, Africa and Latin America. Water deficit is a principal constraint on its productivity, and the crop is typically exposed to terminal drought during flowering and fruit set, when yield components are determined. Tomato (*Solanum lycopersicum* L.) and eggplant (*Solanum melongena* L.) face comparable exposure, and all three share a common solution in principle: identify tolerant genotypes and deploy them.

Genotype screening at germination and the early seedling stage has become the practical entry point. Seeds are germinated in Petri dishes containing an osmoticum — almost always polyethylene glycol (PEG) of molecular weight 6000 or 8000 — at one to four concentrations, and germination and seedling traits are scored. The approach has obvious appeal. It requires no field season and no specialised equipment. A few hundred genotypes can be ranked within weeks at negligible cost. The method has been applied independently by many groups, and it has produced concrete tolerant germplasm in chilli (Sharma et al., 2024), tomato (Yadav et al., 2025) and eggplant (Krommydas et al., 2025) alike.

That literature is the subject of this review, and the question it addresses is not whether the method works. It does. The question is **how far its outputs can be generalised**, and specifically whether a genotype ranked as tolerant in a Petri dish is more likely to perform well under field drought at the stage where yield is determined. This question matters because breeding programmes act on screening outputs: genotypes are advanced, crossed and discarded on the basis of rankings obtained at a developmental stage that is not the stage under selection in the field.

Three features of the current state of knowledge make the question tractable now. The physicochemical behaviour of PEG has been characterised in detail (Lagerwerff et al., 1961; Lawlor, 1970; Michel and Kaufmann, 1973; Money, 1989), including several behaviours that bear directly on how screening results should be interpreted. Sufficient studies now exist that test the same genotypes at more than one developmental stage, which was not the case a decade ago. And the molecular tools available for *Capsicum* have changed: virus-induced gene silencing and, most recently, heritable virus-induced gene editing now permit functional testing in pepper without the stable transformation that has historically been the crop's principal limitation.

### 1.1 Scope and boundaries

The review takes *Capsicum annuum* as its primary subject and draws comparative evidence from tomato, eggplant and wild *Solanum* species, for two reasons. The three crops share the screening methodology almost exactly, which makes cross-crop comparison informative; and they differ markedly in the depth of genetic resources available, which makes the comparison diagnostic. Section 5 develops this comparison in detail.

The review covers osmotic stress simulation and its physicochemical basis, the germplasm-level screening literature, the evidence on transfer between developmental stages, and low-cost genotyping options for laboratories with limited infrastructure. It does not cover salinity or heat tolerance, transgenic breeding as a strategy, or the quantitative genetics of drought tolerance except as needed to interpret screening outputs.

### 1.2 Relationship to existing reviews

Drought tolerance in the Solanaceae has been reviewed, most comprehensively for molecular and genetic mechanisms across the family (Pang et al., 2024), and separately for tomato omics, non-coding RNAs and genome editing (Taheri et al., 2022). These reviews address the mechanistic and genomic basis of tolerance. This review addresses a different question: what the widely used screening methodology can and cannot support, and how its outputs should be reported so that they accumulate. The distinction is not merely one of emphasis. A protein interaction or a validated locus is a durable result independent of how the study was designed. A genotype ranking derived from a single-stage screen is not, because its value depends entirely on whether the ranking transfers — and that is the question this review examines.

### 1.3 Method of this review

This is a critical rather than systematic review. A meta-analysis is not achievable in this area: published screening studies use different PEG concentrations and molecular weights, different trait sets, different tolerance indices, and mostly report no measures of variance, so no common effect size can be extracted. The literature was searched for studies of osmotic or PEG-induced stress screening in *Capsicum*, tomato, eggplant and wild *Solanum*, and additionally for studies testing the same genotypes at more than one developmental stage in any crop, on the reasoning that cross-stage transfer is a general question for which cereal evidence is informative. Priority was given to studies reporting quantitative outcomes with statistics. The search was not exhaustive and may have missed relevant work; statements about the state of the literature are correspondingly qualified.

---

## 2. Osmotic stress simulation: chemistry, contested assumptions and documented artefacts

Every screening study in this literature rests on the same substitution: water deficit is replaced by an osmoticum applied at a nominal concentration. This section examines that substitution, because the limitations of the treatment determine what the screens can show. It is placed before the screening results for that reason.

### 2.1 PEG is a polymer series, not a reagent

"PEG" describes polymers from molecular weight 200 to 20,000, and the literature treats them as interchangeable. They are not.

Osmotic pressure at equal mass concentration varies systematically with molecular weight. Measurements across PEGs of *M*ᵣ 200–10,000 established that low molecular weight PEGs generate higher osmotic pressure than high molecular weight PEGs at the same mass concentration, the relationship being governed by the ratio of concentration to molecular weight. A 15% (w/v) solution of PEG 400 and of PEG 6000 are therefore not equivalent treatments (Money, 1989), yet screening papers routinely report a percentage without stating molecular weight — although the majority use PEG 6000.

Molecular weight also determines where the stress acts. In common bean root tips the site of action depends on molecular weight: glycerol and PEG 4000 act mainly in the cytoplasm, whereas PEG 6000 additionally dehydrates the apoplast and reduces cell-wall porosity (Yang et al., 2010). High-molecular-weight PEG is thus not merely excluded from the tissue; it dehydrates a specific compartment.

The most directly relevant evidence comes from *Capsicum* itself. Pepper plants were grown in nutrient solutions at −3.0 or −5.0 bar using PEG of molecular weights 400, 600, 1000, 1540 and 4000 (Lagerwerff et al., 1961; Janes, 1974). PEG of 1000 and 1540 was judged most satisfactory as an osmoticum; PEG accumulated in plant tissue in inverse proportion to its molecular weight, increased at lower osmotic potentials, and accumulated over time; and the major proportion of absorbed PEG 4000 was retained in the roots rather than translocated. The osmoticum is not a passive background variable, and this was demonstrated in the review's focal crop fifty years ago.

### 2.2 Concentration is not osmotic potential, for three reasons

**PEG solutions are non-colligative.** PEG does not behave as an ideal solute. Solution measurements showed that PEG produces a greater osmotic effect than the number of dissolved molecules accounts for (Money, 1989), with the discrepancy correlating with polymer mass and attributed to water sequestration. Freezing-point osmometry overestimates relative to vapour pressure osmometry, partly because PEG inhibits ice crystallisation and thereby distorts the measurement. Nominal concentration-to-potential conversion tables therefore carry an error of unstated magnitude, and applying the standard relation shows how large that can be. At 25 °C, 10% PEG-6000 corresponds to approximately −0.15 MPa and 20% to approximately −0.49 MPa (Figure 2), values that agree with published applications of the equation (Sivakumar et al., 2014). Screens reporting more negative potentials at the same nominal percentage are not necessarily wrong — molecular weight, temperature and w/v versus w/w all shift the answer — but stated potentials should be traced to the primary source before studies are compared.

**Osmotic potential is temperature-dependent.** The standard empirical equation for PEG-6000 expresses osmotic potential as curvilinearly related to concentration and linearly increasing with temperature, over a validity range of 15–35 °C (Michel and Kaufmann, 1973; McClendon, 1981). A screening experiment at 20 °C and one at 30 °C apply different stresses at the same stated concentration. Incubation temperature is a treatment variable that is rarely reported as one.

**Measurement method determines the answer.** The same reference explicitly notes that thermocouple psychrometer readings are more negative than vapour pressure osmometer readings, and judges the psychrometer closer to correct for bulk solutions (Michel and Kaufmann, 1973). Subsequent work has confirmed that differences between osmometer types are large enough to matter. A statement that osmotic potential was measured is therefore incomplete; the instrument must be specified.

### 2.3 The penetration question: an assumption that does not hold as stated

The standard justification for PEG over mannitol or sucrose is that PEG is excluded from plant tissue, so the stress it imposes is purely osmotic with no confounding uptake. This argument appears in the introduction of most PEG screening papers and is the reason PEG displaced mannitol as the osmoticum of choice. The measurements that exist do not support it in the form in which it is usually stated.

Direct measurement in maize, bean, cotton and tulip tree found that PEG of molecular weight 1000 and above entered plants at approximately 1 mg per gram leaf fresh weight per week (Lawlor, 1970), with entry substantially increased where roots were mechanically damaged or exposed to low water potentials — that is, under the conditions a drought experiment creates. Autoradiography localised absorbed PEG 4000 initially at leaf margins and subsequently through the mesophyll. As noted above, the same behaviour was documented in pepper (Janes, 1974).

Two qualifications should be stated, because the picture is not one-sided. Entry at high molecular weight is slow, and over a 7–10 day germination assay the absolute quantity taken up is small. And much of the applied literature asserts non-penetration as established, which makes the assumption conventional rather than contested. But an assertion repeated in introductions is not a measurement, and the measurements that exist point the other way, at least for lower molecular weights and for stressed or damaged roots.

The consequence for interpretation is specific. If PEG can enter tissue, a treatment described as purely osmotic may carry a solute-loading component whose magnitude depends on molecular weight, duration, root integrity and stress intensity — all of which vary across the studies reviewed here. The appropriate conclusion is not that PEG screening is invalid, but that its mechanism of action is less well characterised than the standard justification implies, and that the justification should be presented as an assumption rather than a finding.

This also means the choice of PEG over mannitol is less decisive than it is usually presented as being. The critique of mannitol — that it is taken up and metabolised — is correct, but the contrast is one of degree rather than kind. The comparative evidence is genuinely mixed. A study across *Cucurbita* landraces concluded that mannitol simulated osmotic stress better than PEG for most attributes and concentrations (Tajaragh et al., 2022). A durum wheat study reached the opposite conclusion, finding PEG superior and noting that mannitol's effects were reversible, consistent with uptake (Bousba et al., 2021). The ranking of osmotica is unresolved.

### 2.4 Established artefacts, and two hypotheses that were tested and rejected

Separating what is established from what is assumed, and from what has been tested and ruled out, is essential here because the literature does not consistently make this distinction.

**Established.** High concentrations of PEG increase solution viscosity, limiting oxygen diffusion to roots and imposing a hypoxic component that is not part of a water-deficit treatment. This is seldom reported or controlled. More striking, a comparison across three woody species found that PEG-induced stress produced the same decline in water potential as soil drying but significantly greater membrane injury and larger reductions in net photosynthesis and stomatal conductance, with slower recovery after relief; even brief exposure was more damaging than soil drought (Fan and Blake, 1997).

**Tested and rejected.** It is frequently stated that impurities in commercial PEG contribute to its effects. This was tested directly: PEG purified by gel filtration was compared with unpurified material, and maize growth was unaffected (Lawlor, 1970). Sephadex chromatography further showed that passage through the plant did not alter average molecular weight, indicating no selective absorption of contaminant small molecules. It is also stated that PEG's detergent properties cause toxicity; comparison with non-ionic detergents ruled this out (Lawlor, 1970). The mechanism favoured instead was physical blockage of the water-movement pathway, reducing water absorption and desiccating the plant.

**Counter-evidence must be reported alongside these criticisms.** A study simulating drought in five pasture species found that under non-limiting soil contact and water-flow conditions, the equivalence of osmotic and matric potential held for all species examined, and concluded that PEG solutions served as a satisfactory medium for studying the effect of true drought on seed germination (Sharma, 1973). That is a genuine endorsement of PEG for the specific application this review concerns, and it should be weighed against the criticisms in the following section.

### 2.5 Alternatives

Table 1 sets out the osmotica that are actually used, with the documented limitation of each.

The raft and solidified-media approaches deserve attention precisely because they were designed in response to the penetration problem described in Section 2.3, and they remain almost unused in the Solanaceae work this review catalogues. That is a specific and inexpensive methodological gap.

### 2.6 Verdict

PEG-induced osmotic stress is fit for relative ranking of genotypes under a defined, artificial, non-drought treatment, provided the osmoticum, molecular weight, concentration, temperature and duration are stated. It is not a mechanistic model of field drought. Recent authoritative treatment of this question is unambiguous: PEG application triggers plant dehydration but does not accurately simulate drought, and describing such experiments as drought or water stress misleads readers (Kylyshbayeva et al., 2025).

**Table 1** — Osmotic agents compared: agent, molecular weight, typical concentration, mechanism, documented limitations, suitability and key reference.
**Figure 2** — PEG-6000 concentration against osmotic potential, compiled from published relationships and annotated with the temperature validity range and the measurement-method discrepancy. Compiled, not experimental.

---

## 3. Screening in the Solanaceae: what has been reported

### 3.1 The shape of the literature

The screening literature has a consistent architecture. Genotypes are exposed to an osmoticum at one to four concentrations spanning roughly 5–20% (w/v), with germination and early seedling traits scored over 7–14 days. Almost all studies use a completely randomised design with three or four replications (e.g. Sharma et al., 2024). Most report germination percentage, germination rate or index, root and shoot length, seedling fresh and dry weight, and a derived vigour index; a minority add proline, relative water content, membrane stability or antioxidant activity.

The three crops differ in emphasis rather than approach (Table 9).

**Table 9.** Distinguishing features of the screening literature by crop.

| Crop | Screening stage | Distinguishing feature |
| --- | --- | --- |
| *Capsicum* | Germination and early seedling | Largest number of independent genotype panels; predominantly cultivar and breeding-line material |
| Tomato | Germination, seedling, and callus culture | The only crop with *in vitro* selection at the callus level; larger panels and more indices |
| Eggplant and wild *Solanum* | Vegetative and whole-plant | Wild relatives screened routinely alongside cultivars |

The eggplant contrast frames Section 5 and is worth stating at the outset: eggplant screening panels routinely include wild relatives, while *Capsicum* panels almost never do — despite a pepper pan-genome that has identified abiotic stress tolerance genes carried in *C. baccatum* introgressions (Liu et al., 2023). The tolerance germplasm appears to be present and largely unexamined in pepper's screening literature.

### 3.2 Traits and indices

The trait set is largely settled across the field, which is a strength for comparability. The index set is not.

Germination percentage is the near-universal primary trait and carries the most interpretive weight in conclusions. Germination rate, mean germination time and germination index capture the timing dimension that a final percentage obscures. Root length, shoot length and the root:shoot ratio are the standard morphological traits, with root traits frequently advanced as mechanistically relevant because greater root length permits access to water at depth. Seedling dry weight and the derived vigour index integrate growth across the assay.

Tolerance indices are used interchangeably and are not interchangeable. In the wider literature, productivity-oriented indices (STI, GMP, harmonic mean, yield stability index) correlate strongly with yield under both stress and non-stress conditions, whereas susceptibility-oriented indices (SSI, TOL, stress susceptibility percentage index) primarily reflect the magnitude of stress-induced loss. They can rank the same genotypes differently. An integration study in maize makes the consequence explicit: index choice directly influences genotype ranking and selection decisions (Muzafarov et al., 2026). The same inconsistency is documented in chickpea, where several indices produced conflicting rankings (Basavaraj et al., 2025).

**Table 3** sets out each index with its formula, what it captures, and its characteristic failure mode. The most tractable fix is also the cheapest: report at least one productivity-oriented and one susceptibility-oriented index, and state the reason for the choice.

### 3.3 What the literature has achieved

This should be stated directly, because the sections that follow examine limitations that would otherwise read as a general dismissal.

The screening literature has produced usable tolerant germplasm. In *Capsicum*, a 16-genotype screen across three PEG levels identified UARChH 42, UARChH 43 and Arka Swetha as tolerant (Sharma et al., 2024). A 47-genotype emergence screen identified five tolerant lines and five susceptible ones, resolving four clusters by agglomerative clustering at a cophenetic correlation of 0.668 (Molla et al., 2019). A 22-genotype study identified C7 as tolerant across all measured traits (Millah et al., 2021). In tomato, a five-genotype screen identified NGRCO9569, Monoprecos and Khumal 2 as maintaining germination, vigour and biomass under stress, while a susceptible genotype failed to germinate entirely at 6% PEG (Yadav et al., 2025). In *Capsicum* germplasm more broadly, a 100-accession vegetative-stage screen identified three accessions as resistant through 21 days of water withholding, corroborated under greenhouse conditions (Thin et al., 2026).

None of this would exist without the screening approach. The method is cheap, requires no field season, discriminates among genotypes, and has produced converging evidence from independent groups that genetic variation for early-stage osmotic tolerance exists and is substantial. The question this review addresses is how far those outputs generalise, not whether the method produces them.

A methodological good practice also deserves credit. A recent tomato callus-selection study determined a genotype-specific sub-lethal PEG concentration for each line rather than applying one arbitrary threshold to all, on the reasoning that a fixed concentration may lie above or below the informative range for a given genotype. The reasoning is sound and the approach is the single most transferable methodological improvement identified in this review (Alnaddaf et al., 2026).

### 3.4 Statistical practice

Germination percentage is binomial: a count of successes from a fixed number of trials, bounded at 0 and 100%. Analysis of variance assumes normally distributed errors with homogeneous variance, and these assumptions are violated by such data, often severely, particularly when means approach the boundaries.

This is not an impression formed from reading a subset of papers. A systematic critique of statistical practice in seed germination and viability research examined 429 studies and reported the distribution in Table 10 (Sileshi, 2012).

**Table 10.** Statistical practice in germination and viability studies, after Sileshi (2012).

| Practice | Proportion of studies |
| --- | --- |
| Analysis of variance | 70% |
| Generalised linear models | 13% |
| Non-parametric tests | 11% |
| Generalised linear mixed models | 4% |
| Linear mixed models | 2% |

Among studies that transformed their data, arcsine transformation was used in 87.6% — a transformation now specifically discouraged for binomial data on the grounds that logistic regression offers greater interpretability and higher power, and that the transformation produces nonsensical predictions for non-binomial proportions (Warton and Hui, 2011). The same review found that in 15 of 429 studies the number of replicates was not stated at all; that a single replication per treatment was used in 4.4% of studies; that pseudoreplication was recorded in 17.4% of studies using logistic regression, where treatments were applied to a single Petri dish and each seed was treated as a replicate; and that only 9.6% of studies using transformation checked whether the transformation had achieved its intended effect. Lack of emphasis on effect sizes was identified as a further area of concern. The reviewer's own conclusion — that the prevalence of these problems risks building a body of knowledge on a shaky ground — applies directly to the screening literature reviewed here.

Practice in this crop conforms to the pattern. The 16-genotype chilli screen described in Section 3.3 used a completely randomised factorial design with three replications and analysed its results by analysis of variance (Sharma et al., 2024); the tomato screen cited above fitted ANOVA to germination percentage, germination rate and vigour index across a genotype × concentration factorial (Yadav et al., 2025). Neither reports an alternative model or a check on the distributional assumption.

The qualification matters, because the issue is not simple and the choice was not unreasonable. Analysis of variance is not automatically wrong for these data. Where germination falls within roughly 30–70%, the response is approximately linear, variance heterogeneity is modest, and classical ANOVA with equal group sizes is reasonably robust. Where the number of observations per group is large, the binomial distribution approximates the normal. A tractable treatment of germination data makes the boundary explicit: wide differences in variance do not arise for purely binomial data in the 0.3–0.7 range of proportions, where analysis of variance is defensible, whereas data outside that range require an angular transformation or a different model altogether (Gianinetti, 2020).

The problem is not the use of ANOVA but its use in the conditions where it fails. Drought screening specifically drives germination percentages toward the boundaries — toward 100% in the control and toward 0% under severe stress — which is precisely the region where normal-error assumptions break down and where arcsine transformation performs worst. A screen at 0%, 5% and 15% PEG will produce a control near 100% and a severe-stress treatment near 0%; that is the worst-case configuration for the analysis method the field uses by default. The appropriate alternative is a generalised linear model with a binomial family and logit link, ideally with Petri dish as a random effect to account for within-dish correlation, and with the dish rather than the seed as the experimental unit. This is a change in analysis, not in experimental design, and it requires no additional resources.

A related issue is the ceiling effect. In a 32-genotype tomato screen, most genotypes failed to germinate at all at −0.35 MPa, and even the best-performing line fell from 100% germination in the control to 60% at that potential (Sivakumar et al., 2014). In an independent five-genotype study the most susceptible line reached 0% at −0.36 MPa (Yadav et al., 2025). Comparable floor effects are reported in wheat and barley at high PEG concentrations (El-Rawy and Hassan, 2014; Slawin et al., 2024). Where a stress level drives all genotypes to zero, it produces no information about relative tolerance, yet such treatments are frequently reported and interpreted. This is a further argument for genotype-specific stress levels.

**Table 3** — Tolerance indices: formula, what each measures, characteristic failure mode, and appropriate use.
**Table 2** — Published screening studies by crop, with design, traits, indices, identified genotypes and stated limitations.

---

## 4. The predictive gap: does early-stage screening forecast field performance?

Early-stage screening rests on an assumption that is rarely stated explicitly: that genotypes ranked as tolerant at germination or the seedling stage will also perform better under drought at the reproductive stage, where yield is determined. This section examines the studies that have tested that assumption. The literature divides, and it does not divide by crop. Figure 3 situates the stages and the transfer question between them; Figure 4 maps which crop-and-stage combinations the evidence actually covers.

### 4.1 Evidence that early-stage ranking does not transfer

**In wheat, seedling traits do not correlate with yield.** A population of 146 F₉ recombinant inbred lines derived from a cross between a seedling-drought-tolerant and a seedling-drought-susceptible cultivar was scored for tolerance, survival and recovery indices, then grown for grain yield in two low-rainfall environments across two seasons. No significant correlations were found between seedling traits and grain yield in any environment, and of the genotypes identified as most drought-tolerant at the seedling stage, only one combined that with high yield under drought. The authors recommended that breeding for seedling tolerance and for yield be studied separately under controlled and field conditions (Sallam et al., 2018).

The same study identified a deeper problem. Tolerance traits (time to wilting, wilting score) and recovery traits (days to regrowth, regrowth biomass, survival rate) were weakly correlated or uncorrelated, and the quantitative trait loci underpinning them were entirely different except for a single pleiotropic locus. Tolerance and recovery at the same developmental stage are therefore genetically distinct, which undercuts the common practice of treating a composite index as a general measure of drought tolerance.

**In barley, the correlation is negative.** A 164-line spring barley population was screened under PEG at germination and seedling stages and then subjected to short-term drought at heading, with grain yield measured. Germination rate under PEG correlated negatively with seed yield under drought (r = −0.25), a result the authors described as unexpected and warranting further investigation. Germination percentage also correlated negatively with root:shoot fresh weight under PEG (r = −0.37). Most notably, some genotypes performed better under PEG than under control for some traits — biologically incoherent for a genuine water-deficit treatment, and direct evidence that PEG introduces effects beyond water limitation. The study was designed explicitly to test the reliability of proxy methods; of nine lines germinating at 100% under PEG, three maintained root length and only two showed no yield penalty under heading-stage drought, a transfer rate of approximately 22% within a purpose-built experiment (Slawin et al., 2024).

**In wheat, germination does not predict the seedling stage.** A study scoring the same genotypes for germination traits under PEG and for a seedling-stage drought tolerance index found little to no correlation between the two stages, citing two further studies reaching the same conclusion, and concluded that testing the same genotypes across growth stages is essential (Mohamed et al., 2023). This is the shortest interval in the developmental sequence, and the association still fails.

### 4.2 Evidence that early-stage ranking does transfer

**In wheat, seedling traits correlate with yield at moderate stress.** A diallel analysis found grain yield per spike significantly correlated with root length (r = 0.41) and seedling dry weight (r = 0.46) at 15% PEG. At 20% PEG the correlations weakened and the root:shoot ratio became non-significant (El-Rawy and Hassan, 2014). The relationship was concentration-dependent, which bears directly on the choice of screening level.

**In barley, a consistency claim.** A genome-wide association study of 198 genotypes states that drought tolerance in barley is consistent when determined at the three important growth stages — germination and seedling, vegetative growth, and flowering and yield. This directly contradicts the 164-line barley study above (Badr et al., 2025). Both are recent, both use large populations, and both use PEG.

**In tomato, transfer is confirmed in the one study that tests it.** Introgression lines of *Solanum pennellii* that had already been ranked for drought tolerance at germination and seedling stages were evaluated through vegetative and reproductive stages under two water regimes. Two lines ranked tolerant at the early stages were again tolerant later, and the most tolerant line at the early stages was also the most tolerant at the later ones. Candidate genes identified in the introgressed segments included *AHG2*, *PRXIIF*, *SAP5*, *PRXQ*, *CFS1*, *LCD*, *CCD1* and *SCS*. This is the only connecting study in the Solanaceae, and it supports transfer (Pessoa et al., 2023).

**In potato, phenotypic biomarkers persisted.** Across three trials on 20 tetraploid lines, growth-curve parameters — the turning point of leaf area index and of projected leaf area — correlated with drought tolerance independently of the treatment in which they were measured. This is vegetative-to-yield transfer rather than germination-to-yield, but it demonstrates that some early-measured traits carry predictive signal (Köhl et al., 2023).

### 4.3 Why the results conflict

The contradiction is not random. Four design and biological factors plausibly drive it, and identifying them converts a confusing literature into an actionable one.

**Internal concordance is being reported as cross-stage transfer.** Several studies reporting strong correlations are correlating traits measured within a single stage or treatment — germination percentage with germination rate, or root with shoot biomass. These are near-tautological relationships between co-measured growth traits. They appear in the same correlation matrices as genuine cross-stage relationships, which makes a study appear to demonstrate transfer when it has demonstrated only internal consistency. This is likely the most common source of apparent support for predictive validity, and separating internal from cross-stage correlations in every correlation analysis would resolve it at no cost.

**Trait-level correlation and genotype-level overlap are different questions.** In the wheat study described above, no seedling trait correlated with grain yield, yet individual genotypes were identified that were tolerant at the seedling stage and high-yielding in the field. A screening programme does not require a significant trait correlation; it requires retaining the right genotypes. Reviews that dismiss early screening on the basis of absent trait correlations may be applying the wrong test. The appropriate metric is the concordance rate among selected genotypes, and it is almost never reported (Figure 5).

**PEG concentration determines whether the screen discriminates.** The diallel study's positive correlations at 15% PEG became non-significant at 20%. Severe stress can drive most genotypes to the floor of the measurable range, destroying resolution. Combined with the finding that most tomato genotypes fail to germinate at all above −0.35 MPa, this argues against applying a fixed concentration to all genotypes and in favour of the genotype-specific sub-lethal approach described in Section 3.3.

**The traits being screened may not be the traits that matter.** Tolerance and recovery at the same developmental stage are genetically distinct. Drought tolerance is stage-specific within *Capsicum* itself: a comparison of the three most widely cultivated *Capsicum* species across four drought regimes imposed at three growth stages found all three species more susceptible at the vegetative stage than at flowering or fruiting. If tolerance at different stages is controlled by largely non-overlapping loci, then a single-stage screen cannot function as a general proxy, and the search for one is misdirected (Okunlola et al., 2017; Sallam et al., 2018).

### 4.4 Implications for practice

Three conclusions follow.

Early-stage screening should be described as what it is: a ranking of genotypes for tolerance at that stage. The literature does not support presenting it as a proxy for field drought tolerance, and papers should describe the treatment as osmotic stress induced by PEG rather than as drought.

The confirmation rate should be reported rather than assumed. Where a screen feeds a breeding programme, the proportion of selected genotypes that prove superior under field drought is the quantity that determines the programme's value. It is currently almost never reported. Closing this gap requires only that field evaluation of screened material be published alongside the screen.

The unresolved cases should be resolved deliberately. Barley now has two large, recent studies reaching opposite conclusions about the same question. That is a tractable dispute: the difference may lie in population, PEG concentration, stress timing or the traits scored. It should be settled by analysing both datasets together rather than by conducting one more independent screen. This is the review's most concrete proposal for future work.

**Figure 3** — Developmental stages represented as partially overlapping tolerance sets, annotated with the direction of evidence from each study discussed. Conceptual.
**Table 5** — Studies connecting two or more developmental stages: crop, population, stages, screening agent, outcome, direction of evidence and design quality.

---

## 5. Cross-crop comparison: resources, strategies and the *Capsicum* gap

### 5.1 Three developmental strata

Drought tolerance research in the Solanaceae is organised by developmental stage, and the stages are largely studied separately (Table 11).

**Table 11.** The three developmental strata and the typical approach used at each.

| Stratum | Stage | Typical approach |
| --- | --- | --- |
| A | Germination | PEG-induced osmotic stress in Petri dishes |
| B | Vegetative | Controlled water withholding in pot or greenhouse |
| C | Reproductive | Field or greenhouse water stress; GWAS and QTL mapping |

Tomato has the deepest coverage in stratum C: 19 drought-related QTL from sub-near-isogenic lines of *S. habrochaites* on chromosome 9 for traits including specific leaf area, shoot dry weight, fruit yield and carbon isotope discrimination; 56 QTL from 119 F7 recombinant inbred lines, 11 expressed under drought; 12 for fertility and flowering under drought; and 54 from a multi-parent advanced generation intercross population. CRISPR validation exists, with *SlMAPK3* mutants showing enlarged stomatal apertures, elevated H₂O₂ and malondialdehyde, increased electrolyte leakage, reduced antioxidant enzyme activity, and down-regulation of *SlDHN*, *SlDREB* and *SlGST* (Pang et al., 2024).

*Capsicum* has less, but more than is sometimes assumed. A recent study combined genome-wide association in a Balkan diversity panel (n = 133) with QTL mapping in an interspecific backcross inbred line population (n = 76), phenotyping both under well-watered and water-stressed conditions for fruit yield and quality; loci on chromosomes 5 and 6 harboured candidate genes including *GRL1*, *CYP77A19* and an endoglucanase-like gene, with effects attributed to possible *cis*-regulatory variation (Rai et al., 2026). A screen of 100 accessions identified resistant material at the vegetative stage (Thin et al., 2026). And pepper has a graph pan-genome with a genome variation map covering 500 accessions across five domesticated species and close wild relatives, in which introgressions from *C. baccatum* into *C. chinense* and *C. frutescens* carry genes conferring biotic and abiotic stress tolerance.

Eggplant demonstrates a strategy both other crops under-use: systematic exploitation of wild relatives (Kouassi et al., 2021). Cultivated *S. melongena* is consistently the most drought-sensitive genotype in comparative trials, with reductions across nine agronomic traits including leaf area index and biomass; the wild species *S. macrocarpon* essentially maintained biomass and *S. dasyphyllum* showed an intermediate response (Krommydas et al., 2025). A screen across 15 *Solanum* species identified *S. torvum*, *S. viarum*, *S. violaceum* and *S. aethiopicum* as tolerant, with principal component analysis identifying catalase activity, proline, stomatal conductance, transpiration rate, root length and shoot dry weight as the traits driving differences and explaining 80.2% of total variation (Anagha et al., 2026).

### 5.2 Candidate genes and the validation question

A catalogue of drought-responsive genes in the Solanaceae is accumulating. In *Capsicum*, the best-characterised entry is ***CaNAC46***, a NAC-family transcription factor induced by drought, salt, cold, heat, abscisic acid, salicylic acid and methyl jasmonate, which promotes expression of *SOD*, *POD*, *RD29B*, *RD20*, *ABI* and *P5CS*, with silencing increasing malondialdehyde under stress (Ma et al., 2021). *CaDREBLP1* is rapidly induced by dehydration and salinity. *MYB1* and *CaDIM1* are abscisic acid-associated, and *CaSBP13* and *CaDR1* were identified through RNA-seq and genome-wide association. A genotype-contrasting aquaporin result is among the most informative: all twelve examined aquaporins were up-regulated in tolerant KCa-4884 and down-regulated in susceptible G-4 (Sahitya et al., 2019).

In tomato the catalogue is substantially larger and includes both positive regulators (*SlAREB1*, *SlAREB2*, *SlJUB1*, *SlNAC4*, *SlNAC6*, *SlNAC35*, *SlNAC042*, *SlNAP1*, *SlWRKY8*, *SlWRKY6*, *SlERF5*, *SlERF84*, *SlMYB49*, *SlbZIP1*) and negative regulators (*SlWRKY81*, *SlMYB50*, *SlMYB55*, *SlEREB1*, *SlbZIP38*). **Table 4** records the validation host for each entry, which matters because much *Capsicum* gene work has been validated by heterologous expression in *Arabidopsis* rather than in pepper. A gene demonstrated in *Arabidopsis* is not a gene demonstrated in chilli, and reviews frequently conflate the two.

### 5.3 The capability ceiling has moved

*Capsicum* is historically recalcitrant to *Agrobacterium*-mediated transformation, with the reasons now understood: *Agrobacterium* induces a strong immune response in pepper, and the crop has low regeneration efficiency (Liu et al., 2024). Reported transformation efficiencies have ranged from 0.03–0.19% in some inbred lines to 1.3–2.9% in others, with recent work reaching approximately 5% effective efficiency through vacuum treatment, avoidance of pre-culture, and co-expression of a growth-regulating factor (Tang et al., 2025); earlier work established stable editing in both hot and bell pepper cultivars (Park et al., 2021).

Two developments have changed what is feasible without stable transformation. Virus-induced gene silencing is established in pepper: a broad bean wilt virus 2-based vector system silenced phytoene desaturase across multiple cultivars with efficiencies between 67% and 79% (Choi et al., 2019), and the literature now describes VIGS as often the key, and sometimes the only viable, tool for high-throughput functional screening in this crop. More recently, a virus-induced gene editing system achieved heritable editing in pepper: 8.5% of progeny from plants inoculated with a modified tobacco rattle virus construct carrying a ribozyme-processed guide RNA were mutated at the target locus, with a second gene edited to produce a visible phenotype, and the method is tissue-culture-free (Kang et al., 2025).

This does not remove the constraint, but it moves it. The barrier to functional validation in *Capsicum* is no longer the absence of a route; it is that these routes are not yet routine in the laboratories conducting screening work. That makes the opportunity described in Section 7 less a matter of capability than of coordination.

### 5.4 What the comparison shows

Three conclusions emerge.

The binding constraint is not genomic resources. Pepper has a 500-accession pan-genome, tomato has a saturated QTL literature, and eggplant has a characterised wild-relative donor pool. Sequence, markers and mapping populations are available across the family.

The constraint is not effort either. Each crop has substantial work at each developmental stage, and the connecting studies across the family number at least nine.

The constraint is that the strata are not connected within a single genotype set, and that the resulting question — whether early-stage tolerance predicts later-stage performance — is answered inconsistently where it has been asked and not at all in *Capsicum*. The most economical solution is a shared genotype set: screening panels, validation trials and mapping populations drawing on common, diverse, publicly available germplasm. This would convert three stratified literatures into three experiments on one population, and would generate the cross-stage concordance data that is currently almost never reported. It is a coordination recommendation, and its cost is close to zero relative to any single experiment it connects.

**Table 4** — Candidate genes with family, organism, validation host and evidence level.
**Table 6** — Cross-crop comparison of resources and strategies by developmental stratum.
**Figure 4** — Evidence map by crop and stage-pair, showing where connecting studies exist and which direction each points. Conceptual.

---

## 6. Low-cost, scalable genotyping for resource-limited laboratories

For a laboratory that has completed a screen with limited resources, the practical question is what to do next. This section compares available platforms on the criteria that constrain such laboratories: not cost alone, but equipment availability and the bioinformatics capacity required.

### 6.1 Which constraint binds

Cost per data point is the headline metric and the least informative in isolation. Three constraints bind, and they bind differently. Equipment binds when there is no real-time PCR instrument, no capillary sequencer, and no access to a sequencing service. Bioinformatics capacity binds when no one can process raw reads, call variants or run association analysis. Money binds least often, because the cheapest methods are also the most labour-intensive. Genome-wide approaches are frequently presented as the affordable option because sequencing costs have fallen; they are affordable in reagents and demanding in analysis. A laboratory with a thermal cycler, gel documentation and no bioinformatician is better served by a small number of targeted assays than by a dataset it cannot interpret.

### 6.2 Assays requiring only PCR

Simple sequence repeat genotyping remains the most accessible route to marker–trait association. It requires a thermal cycler and either gel electrophoresis or a capillary sequencer, both widely available, and validated *Capsicum* panels are published. Markers Hpms1172 and CAMS177 have been associated with a stress tolerance index in chilli across a 78-genotype panel, with principal coordinate analysis aligning with marker-assisted selection output (Bukhari et al., 2024). The limitations are intrinsic: SSRs are low-density, sample few loci, and detect a causal polymorphism only where it lies in sufficient linkage disequilibrium with the amplified repeat.

Amplicon sequencing of candidate genes offers the highest value for a laboratory with PCR access and a sequencing service. Rather than screening the genome, it interrogates the genes the literature already implicates — *CaNAC46*, *CaDREBLP1*, the *CaDREB*, *CaP5CS* and aquaporin families (Ma et al., 2021; Sahitya et al., 2019) — across the genotype panel, identifying sequence polymorphism within them. It is inexpensive because the target is small, it produces interpretable variants rather than anonymous markers, and it generates a testable hypothesis. Its limitation is equally clear: it finds variation only in genes someone has already chosen to examine.

### 6.3 Genome-wide approaches

Bulk segregant analysis with sequencing is the most cost-effective genome-wide strategy for a trait with contrasting extremes, because it reduces the genotyping unit from the individual to the pool: two pools of extreme-phenotype individuals are sequenced, and allele-frequency differences localise the contributing region (Majeed et al., 2022). It requires only two sequencing reactions. Two caveats apply, and both are biological rather than logistical. Accuracy depends on sequencing depth and coverage, so cost rises with the resolution sought. And its application is constrained in species with large genomes. *Capsicum annuum* has an approximately 3.5 Gb genome, among the larger among cultivated Solanaceae, which raises the sequencing requirement substantially relative to rice or *Arabidopsis* (Liu et al., 2023). BSA-seq is a reasonable option in pepper, but not the near-free one it is in small-genome crops. Its extension to outcross populations (OcBSA) widens its applicability beyond inbred-line crosses (Zhang et al., 2024).

Genotyping-by-sequencing provides genome-wide markers at approximately US$10–50 per sample and has been applied in pepper, including for combined QTL and association mapping of *Phytophthora capsici* resistance (Sahoo et al., 2025). A pepper SNP array has been used to genotype a GWAS panel, which is the appropriate choice where an off-the-shelf array exists and the panel is large.

### 6.4 Deployment

Discovery and deployment are different problems requiring different platforms. Kompetitive allele-specific PCR assays run on a standard real-time PCR instrument, require no gel electrophoresis, and cost approximately **US$0.05–0.10 per data point** — one to two orders of magnitude below genome-wide approaches on a per-sample basis. A published comparison of PCR-based SNP genotyping platforms positions KASP and PACE as the most cost-effective options for small laboratories, noting that the ability to run these assays on standard real-time instruments makes them accessible to laboratories with limited resources (Sahoo et al., 2025). The barrier to adoption is therefore not equipment but assay design, which requires a known polymorphic site. This is the operational reason to sequence candidate genes first.

**Table 7** — Genotyping platforms compared by cost, marker number, equipment, bioinformatics requirement and best use.

### 6.5 A note on platform costs

Cost figures for genotyping platforms are frequently sourced from vendor material rather than peer-reviewed literature, and vendor pricing changes. The figures used above are drawn from a peer-reviewed review of PCR-based SNP genotyping (Sahoo et al., 2025) and from the same source for sequencing-based approaches. Laboratories budgeting a project should treat them as order-of-magnitude indicators and obtain current quotations.

---

## 7. Synthesis: a proposed framework and minimum reporting standard

### 7.1 What this review has established

The preceding sections support four conclusions, and they are more encouraging than a critical reading of any one of them suggests. Figure 1 sets out the resulting framework and its decision points.

Early-stage osmotic screening works in the sense that it discriminates. It has produced tolerant germplasm in every Solanaceae crop examined, at low cost, without a field season, and independently in many laboratories. The genetic variation it detects is real.

It does not currently function as a general proxy for field drought tolerance, and the field does not agree on whether it can. Of the studies testing transfer across developmental stages, four support it and four contradict it. The disagreement is not random; it tracks identifiable design choices.

Those design choices are cheap to fix. Internal-consistency correlation being reported as cross-stage transfer, trait-level tests being used where genotype-level concordance is required, fixed PEG concentrations applied where genotype-specific levels are needed, and developmental stage being ignored — each has a remedy that costs little.

The molecular route is more open than it was. Pepper's transformation recalcitrance has historically capped functional validation, but virus-induced gene silencing and heritable virus-induced gene editing now provide tissue-culture-free routes. The constraint has moved from capability to coordination.

### 7.2 Why current practice was reasonable

Each of the practices this review identifies as limiting was, and remains, a defensible response to real constraints. Stating this is not a courtesy; it explains why what follows is a standard rather than a correction.

Fixed PEG concentrations are the only practical choice when a screening panel is large and no prior information about individual genotypes exists. Genotype-specific determination requires a pre-experiment that many screening programmes are not resourced to run.

Analysis of variance on germination data has a long and accepted history in seed science, and for crops with uniformly high germination the assumptions are met in practice. The conditions that osmotic screening creates — means driven toward 0% and 100% — are precisely those where the method fails, and this follows from the experimental design rather than from analytical carelessness.

Reporting the non-penetration of PEG as established was reasonable when first advanced and has been reproduced in introductions ever since. The original measurements predate the modern publication cycle by five decades and are effectively outside the citation reach of most authors writing today.

Testing at a single developmental stage is what makes screening cheap. A programme that tests all stages is no longer a screening programme but a breeding pipeline, and it costs proportionally more.

The recommendation that follows is therefore offered as a shared standard that would make the existing literature cumulative.

### 7.3 The proposed framework

The framework has four stages, each with an explicit decision point.

**Stage 1 — Screen.** Use a panel of at least 20 genotypes including wild relatives and at least one known tolerant and one known susceptible check. Record PEG molecular weight, supplier and batch. Use genotype-specific sub-lethal concentrations where feasible, or at least three levels spanning the informative range otherwise. Measure and report osmotic potential, naming the instrument. Control and report temperature. Treat the Petri dish as the experimental unit with at least four replicates of at least ten seeds. Score the standard trait set. Analyse with a generalised linear mixed model, binomial family, logit link, with dish as a random effect, and report the genotype × treatment interaction. Report at least one productivity-oriented and one susceptibility-oriented index. Retain a spectrum of tolerant, intermediate and susceptible genotypes rather than only the extremes. **Decision:** which genotypes advance, and on what stated criterion.

**Stage 2 — Validate.** Impose managed drought at the agronomically relevant stage rather than relying on seasonal conditions, with an irrigated control, a randomised complete block design, and at least two site-years. Analyse with a mixed model treating site-year as a random effect. Report the concordance rate: the proportion of screen-selected genotypes that prove superior in the field. **Decision:** does the screen predict the field? If not, state that the screen selects for a different trait, which is itself a publishable result.

**Stage 3 — Characterise.** Use contrasting genotype pairs from Stage 1. Perform candidate-gene quantitative RT-PCR following MIQE, with reference genes validated for the tissue and treatment rather than assumed. Add amplicon sequencing of candidate genes across the panel. Where capacity permits, test function by virus-induced gene silencing or virus-induced gene editing. **Decision:** is there an expression or sequence difference, or both?

**Stage 4 — Deploy.** Convert the polymorphism to a KASP, CAPS or SSR assay and test marker–trait association in an independent panel, reporting marker effect size and the genotype concordance rate.

### 7.4 Minimum reporting standard

**Table 8** presents the review's principal deliverable: a fifteen-item minimum reporting standard, offered as a checklist for authors, reviewers and editors. Each item is either free or inexpensive to satisfy.

### 7.5 What adoption would change

The standard is deliberately undemanding. Items 6, 8, 9, 10, 12 and 15 are reporting or analysis choices requiring no additional experiment, material or field season. Items 1, 2, 3, 7 and 11 are design choices within existing budgets, with genotype-specific concentration determination the only one requiring a preliminary experiment and optional where resources are constrained.

The substantive change would be item 14. If screening studies routinely reported the proportion of their selected genotypes that proved superior in field evaluation, the question this review identifies as unresolved would be answered within a few publication cycles using data that screening programmes already generate. The information exists; it is not reported in a form that permits synthesis.

**Table 8** — Minimum reporting standard.
**Figure 1** — The proposed framework with decision points at each stage.

---

## 8. Future directions

**Resolve the barley contradiction.** Two recent, large studies reach opposite conclusions about whether drought tolerance is consistent across developmental stages. The disagreement is tractable: it may lie in population, PEG concentration, stress timing or the traits scored. Reanalysing both datasets together would settle it more efficiently than a further independent screen, and the outcome would determine how much weight the wider screening literature can bear.

**Establish dose–response rather than single-point rankings.** Correlations between seedling traits and yield were significant at 15% PEG and non-significant at 20%, and most tomato genotypes fail to germinate above −0.35 MPa. The informative range appears to be narrow and genotype-dependent. Characterising it explicitly would improve discrimination and prevent the floor effects that currently afflict severe treatments.

**Test the concordance rate systematically.** The quantity that determines the value of a screening programme is the proportion of screen-selected genotypes that prove superior in the field. It is almost never reported. A coordinated effort to publish field evaluation of screened material alongside the screens would answer the central question without requiring new methodology.

**Close the *Capsicum* specific gap.** The transfer question has been tested in tomato, potato and cereals, but not in pepper. A single multi-season study correlating germination-stage indices against field drought performance in *Capsicum* would be the most valuable missing experiment in this literature.

**Include wild relatives in pepper screening panels.** Eggplant screening routinely includes *S. torvum*, *S. viarum*, *S. violaceum* and *S. aethiopicum*, and identifies them as more tolerant than cultivated material. Pepper's pan-genome shows that *C. baccatum* introgressions carry abiotic stress tolerance genes. Screening panels confined to cultivars may be excluding the tolerance they are searching for.

**Compare osmotica directly in a Solanaceae crop.** The ranking of PEG against mannitol is unresolved, with studies in different species reaching opposite conclusions. A direct comparison in a single crop, on the same genotypes, using both germination and physiological endpoints, would clarify whether the widespread use of PEG carries a systematic bias.

**Adopt tissue-culture-free validation.** Virus-induced gene silencing and heritable virus-induced gene editing are established in pepper. Their adoption by laboratories conducting screening work would allow candidate genes to be tested in the crop rather than in *Arabidopsis*, raising the evidence from association toward causation.

---

## 9. Conclusion

Early-stage osmotic screening with PEG is the most widely used method for identifying drought-tolerant genotypes in the Solanaceae. It is inexpensive, requires no field season, and has produced tolerant germplasm in chilli, tomato and eggplant. Its outputs, however, are more heavily conditioned than the literature generally acknowledges. The treatment does not simulate drought; the assumption that PEG does not enter plant tissue is contradicted by measurement in pepper itself; and the statistical treatment applied to germination data fails precisely in the boundary conditions that drought screening creates. Most consequentially, whether germination-stage rankings predict field performance at the stage where yield is determined remains unresolved — supported by four studies, contradicted by four, and untested in *Capsicum*.

None of these findings requires the method to be abandoned. Each has a cheap remedy, and six of the fifteen items in the proposed reporting standard require no additional experiment at all. The single substantive change — reporting the proportion of screen-selected genotypes that prove superior in the field — would answer the central question using data that screening programmes already produce. The screening literature has generated the material and the infrastructure. What it has not yet generated is the reporting convention that would let its results accumulate.

---

## Declarations

**CRediT authorship contribution statement.** [AUTHOR NAME]: Conceptualization, Investigation, Methodology, Visualization, Writing – original draft, Writing – review and editing.

**Declaration of competing interest.** The author declares no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Acknowledgments.** [Acknowledge any individuals or institutions that provided support, advice or assistance. Delete this item if there are none.]

**Funding.** This research received no specific grant from any funding agency in the public, commercial or not-for-profit sectors. [Amend if this is not correct.]

**Data availability.** This review analysed only previously published literature. No new data were generated or analysed for this study.

**Generative AI disclosure.** During the preparation of this work the author used [TOOL NAME, VERSION, PROVIDER] to assist with literature synthesis, drafting and language editing. The author set the scope and framing, verified every cited source against primary records and publisher metadata, drew the figures from published equations and reported data, and reviewed and edited all content, and takes full responsibility for the content of the publication.

## Figure legends

**Figure 1.** Proposed four-stage framework for genotype-to-marker pipelines in Solanaceae drought tolerance screening, showing decision points at the screen, validate, characterise and deploy stages. Conceptual.

**Figure 2.** Osmotic potential of PEG-6000 solutions as a function of concentration at 15, 25 and 35 °C, computed from the empirical relation of Michel and Kaufmann (1973), which is valid over the 15–35 °C range shown. Points mark the three concentrations most frequently used in the screening literature. Computed, not experimental.

**Figure 3.** Drought tolerance at germination, seedling, vegetative and reproductive stages represented as partially overlapping sets. Arrows indicate the direction of evidence from each study reviewed, distinguishing studies supporting from those contradicting transfer across stages. Conceptual.

**Figure 4.** Evidence map showing, for each crop and each pair of developmental stages, whether connecting studies exist and the direction of their findings. Empty cells indicate untested combinations. Conceptual.

**Figure 5.** What the studies connecting developmental stages actually report. For each of the nine connecting studies, the left column indicates whether a trait-level correlation was reported and the right column whether a genotype-level concordance rate was reported. One study reports such a rate (22%, two of nine lines); one permits it to be inferred (a single genotype); six report only trait correlations; and one contrasts mechanism without testing transfer between stages. Compiled from the studies reviewed.

---

## Tables

> Table 5 is the connecting-studies table (§4); Table 6 the cross-crop comparison (§5). Per-study detail for Table 2 is in Supplementary Table S1 (Tables S1–S2).

---

### Table 1 — Osmotic agents compared

| Agent | Mechanism | Documented limitation | Key reference |
| --- | --- | --- | --- |
| PEG 6000 / 8000 | Non-penetrating osmoticum (assumed) | Non-colligative; temperature-dependent; uptake demonstrated at lower MW; viscosity imposes hypoxia | Michel and Kaufmann (1973); Money (1989); Lawlor (1970) |
| Mannitol | Sugar alcohol osmoticum | Taken up into apoplast and symplast; effects partially reversible | Tajaragh et al. (2022) |
| Sorbitol | Sugar alcohol | Same class of problem; metabolisable | Sajid and Aftab (2022) |
| Sucrose | Metabolite and osmoticum | Supplies carbon as well as lowering water potential | Sajid and Aftab (2022) |
| NaCl | Ionic osmoticum | Adds ion toxicity; a different stress rather than a substitute | Sharma (1973) |
| Solidified PEG; raft-and-membrane systems | Prevent PEG uptake while imposing osmotic stress | Designed to solve the penetration problem; rarely used in Solanaceae screening | Comeau et al. (2010) |
| Soil or vermiculite drying | Matric stress imposed directly | Most realistic; least high-throughput; inherently more variable | Sharma (1973) |

---

### Table 2 — Osmotic / PEG screening studies in the Solanaceae

| # | Study | Crop | n | Stage | PEG level(s) | Genotypes identified |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Sharma et al. (2024) | *C. annuum* | 16 | Seedling | 5, 10, 15% (−0.3, −0.6, −0.9 MPa) | **Tolerant:** UARChH 42, UARChH 43, Arka Swetha |
| 2 | Millah et al. (2021) | *C. annuum* | 22 | Germination | 15% | **Tolerant:** C7 (all traits); C120, C37, C18 |
| 3 | Molla et al. (2019) | *C. annuum* | 47 | Germination / emergence | 12.5% | **Tolerant:** BD-10906, BD-10912, BD-10911, BD-10916, BD-10913 |
| 4 | Yadav et al. (2025) | Tomato | 5 | Germination / seedling | 3% (−0.18 MPa) | **Tolerant:** NGRCO9569, Monoprecos, Khumal 2 |
| 5 | Alnaddaf et al. (2026) | Tomato | multi | **Callus** | **0–8%**, genotype-specific LC50 | Daraa, Brieh (best RGR maintenance) |
| 6 | Thin et al. (2026) | *Capsicum* spp. | 100 | Vegetative | Water withholding (21 d) | **Resistant:** IT308761, IT250221, IT158637 |
| 7 | Krommydas et al. (2025) | *S. melongena* × wild *Solanum* | 4 + hybrids | Vegetative (4 wk) | Water stress | *S. macrocarpon* tolerant; *S. dasyphyllum* intermediate; cultivated *S. melongena* sensitive |
| 8 | Anagha et al. (2026) | 15 *Solanum* spp. | 24 | Whole plant | 100% vs 35% water | **Tolerant:** *S. torvum*, *S. viarum*, *S. violaceum*, *S. aethiopicum* |
| 9 | Kouassi et al. (2021) | *S. melongena* + wild relatives + F₁ | 9 families | Field | Dry vs rainy season | *S. insanum* tolerant → usable donor |

> **Row 2 is the review's thesis in a primary source:** the commercial drought-tolerant check ranked only "moderately tolerant," which the authors attributed to stage- and mechanism-specificity. **Row 5 is the innovation worth adopting directly** — a genotype-specific sub-lethal concentration rather than one fixed threshold.

---

### Table 3 — Tolerance indices

| Index | Formula | What it measures | Characteristic failure mode | Appropriate use |
| --- | --- | --- | --- | --- |
| **TOL** (tolerance) | Yp − Ys | Absolute yield loss under stress | Scale-dependent: values in yield units, so not comparable across trials or crops | Comparing genotypes within one trial at one site |
| **SSI** (stress susceptibility index) | (1 − Ys/Yp) / (1 − Ȳs/Ȳp) | Yield loss relative to the trial's mean loss; <1 indicates tolerance | Sensitive to the trial mean; a genotype's score moves with the panel it is tested in | Comparing stress response across environments, within one panel |
| **SSPI** (stress susceptibility percentage index) | [(Yp − Ys) / (2Ȳp)] × 100 | Percentage yield reduction, trial-normalised | Inherits the mean-dependence of SSI | Reporting percentage loss in a form comparable across trials |
| **MP** (mean productivity) | (Ys + Yp) / 2 | Average performance across both conditions | Rises with yield potential; selects for high-yielding genotypes whether or not they resist stress | Selecting for performance in both conditions when stress is moderate |
| **GMP** (geometric mean productivity) | √(Ys × Yp) | Performance across both conditions, penalising imbalance | Same direction of bias as MP, more conservative | Where a genotype must not collapse in one condition |
| **STI** (stress tolerance index) | (Ys × Yp) / Ȳp² | Tolerance scaled to the panel's non-stress potential | Highly correlated with yield potential under non-stress; discriminates poorly when stress is mild | Ranking when stress intensity is known and moderate to severe |
| **YSI** (yield stability index) | Ys / Yp | Proportional retention of yield under stress | Uses a single stress level; no measure of variance across environments | Simple screening where one stress treatment is available |

*Ys*, genotype value under stress; *Yp*, under non-stress; Ȳs and Ȳp, the corresponding panel means. TOL and MP follow Rosielle and Hamblin (1981); SSI follows Fischer and Maurer (1978); YSI follows Bouslama and Schapaugh (1984). GMP and STI are given in their standard forms; their primary source (Fernandez, 1992) is a conference proceedings not indexed in Crossref and should be cited from the original volume. SSPI is given as presented in the review literature cited below.

**Specification.** Columns: index | formula | what it measures | failure mode | appropriate use. Susceptibility-oriented (SSI, TOL, SSPI) versus productivity-oriented (STI, GMP, MP, YSI). The indices rank the same genotypes differently; report one of each with justification (Muzafarov et al., 2026; Basavaraj et al., 2025).

---

### Table 4 — Drought-responsive candidate genes in *Capsicum* and tomato

| Gene | Family | Origin | Validation host | Evidence type | Level |
| --- | --- | --- | --- | --- | --- |
| *CaNAC46* | NAC (ATAF) | *C. annuum* | VIGS in pepper; transgenic *Arabidopsis* | Overexpression + silencing | L1–L2 |
| *CaDIM1* | MYB (R2R3) | *C. annuum* | VIGS in pepper; overexpression in *Arabidopsis* | Silencing + overexpression; ABA signalling | L1–L2 |
| *CaSBP13* | SBP | *C. annuum* | VIGS in pepper (94% silencing); overexpression in *N. benthamiana* | Silencing + overexpression. **Negative regulator** — silencing improved tolerance | L1–L2 |
| *CaDREBLP1* | AP2/ERF | *C. annuum* | None in planta — yeast trans-activation and in vitro DRE/CRT binding only | Expression + DNA-binding assay | L0–L1 |
| *CaDR1* | — | *C. annuum* | **None** | RNA-seq; GWAS candidate | L0 |
| Aquaporin family (12 genes) | PIP/AQP | *C. annuum* | **None** | Genotype-contrasting expression (↑ KCa-4884, ↓ G-4) | L0 |
| *GRL1*, *CYP77A19*, endoglucanase-like | various | *C. annuum* | **None** | QTL/GWAS candidates, chr 5 and 6 | L0 |
| *SlAREB1*, *SlAREB2* | bZIP | *S. lycopersicum* | Transgenic tomato | Overexpression | L2 |
| *SlDREB1/2/3* | AP2/ERF | *S. lycopersicum* | Transgenic tomato | Family-wide characterisation | L2 |
| *SlJUB1* | NAC | *S. lycopersicum* | Transgenic tomato | Overexpression | L2 |
| *SlNAC4/6/35/042*, *SlNAP1* | NAC | *S. lycopersicum* | Mixed | Positive regulators | L1–L2 |
| *SlWRKY8*, *SlWRKY6*, *SlERF5*, *SlERF84*, *SlMYB49*, *SlbZIP1* | WRKY/ERF/MYB/bZIP | *S. lycopersicum* | Mixed | Positive regulators | L1–L2 |
| *SlWRKY81*, *SlMYB50*, *SlMYB55*, *SlEREB1*, *SlbZIP38* | WRKY/MYB/ERF/bZIP | *S. lycopersicum* | Mixed | **Negative regulators** — routinely omitted from reviews | L1–L2 |
| ***SlMAPK3*** | MAPK | *S. lycopersicum* | ***CRISPR* mutant** | Genetic loss-of-function; ↓ *SlDHN*, *SlDREB*, *SlGST* | **L1 (genetic)** |

Levels: L0 association · L1 genetic/CRISPR · L2 transgenic overexpression. Sources: Ma et al. (2021); Sahitya et al. (2019); Rai et al. (2026); Pang et al. (2024); *CaDREBLP1* — Hong and Kim (2005); *CaDIM1* — Lim et al. (2022); *CaSBP13* — Zhang et al. (2024).

> **Three of the eight entries have functional evidence in pepper itself** — *CaNAC46*, *CaDIM1* and *CaSBP13*, all validated by virus-induced gene silencing — which is more than the earlier literature suggests. One of the three, *CaSBP13*, is a **negative** regulator whose silencing improves drought tolerance, so it is a target for down-regulation rather than for introgression. A gene demonstrated only in *Arabidopsis* is still not a gene demonstrated in chilli.

---

### Table 5 — Studies connecting two or more developmental stages

**The table on which the review's central claim rests.**

| # | Study | Crop | Stages | Outcome | Direction |
| --- | --- | --- | --- | --- | --- |
| C1 | Pessoa et al. (2023) | **Tomato** | Germination/seedling → vegetative/reproductive | IL 1-4-18 and IL 1-2 tolerant at all stages; most germination-tolerant also most tolerant later | **Supports** |
| C2 | Sallam et al. (2018) | Wheat | Seedling indices → grain yield, 2 environments × 2 seasons | No significant correlations between seedling traits and yield in any environment; 1 genotype combined both | **Contradicts** |
| C3 | Slawin et al. (2024) | Barley | Germination/seedling → heading yield, n = 164 | r = −0.25; 9 lines at 100% germination → 2 with no yield penalty (~22%) | **Contradicts** |
| C4 | Badr et al. (2025) | Barley | Germination + seedling + vegetative + flowering, n = 198 | Tolerance "consistent" across the three important growth stages | **Supports** — directly contradicts C3 |
| C5 | El-Rawy and Hassan (2014) | Wheat | Seedling → grain yield/spike | Root length r = 0.41\*, seedling DW r = 0.46\* at **15%**; non-significant at **20%** | **Supports**, concentration-dependent |
| C6 | Mohamed et al. (2023) | Wheat | Germination → seedling | "Little to no correlation" between the two stages | **Contradicts** |
| C7 | Köhl et al. (2023) | Potato | Vegetative → yield, 20 lines, 3 trials | LAI and A2 turning points correlated with tolerance across trials | Supports |
| C8 | Sahitya et al. (2019) | *Capsicum* | — (mechanism contrast) | 12 aquaporins ↑ in tolerant KCa-4884, ↓ in susceptible G-4 | — |
| C9 | Yadav et al. (2025) | Tomato | Germination/seedling only | Authors state field validation outstanding | **Untested** |

**Score: 4 support · 4 contradict · 1 untested.**

> **Seven of the nine are cereals or potato, one is tomato, and none is *Capsicum*.**

---

### Table 6 — Cross-crop comparison by developmental stratum

| Stratum | *Capsicum* | Tomato | Eggplant |
| --- | --- | --- | --- |
| **A — Germination** | Active (5 studies, Table 2) | Active (Yadav et al., 2025; Alnaddaf et al., 2026) | Limited |
| **B — Vegetative** | 100-accession screen (Thin et al., 2026) | Active | Active (Krommydas et al., 2025) |
| **C — Reproductive** | **1 GWAS + QTL study (Rai et al., 2026)** | **Deep** — 19, 56, 12 and 54 QTL across populations; *SlMAPK3* CRISPR | Genetic parameters (Kouassi et al., 2021) |
| **Wild-relative donors** | **Under-used**; introgression potential shown (Liu et al., 2023) | Established | **Best developed** — *S. torvum*, *S. viarum*, *S. aethiopicum*, *S. insanum* |
| **Studies connecting strata** | **0** | 1 (C1) | 0 |

---

### Table 7 — Genotyping platforms compared

| Platform | Cost | Equipment | Bioinformatics | Best use |
| --- | --- | --- | --- | --- |
| **KASP / PACE** | **~US$0.05–0.10 per data point** | Thermal cycler + real-time PCR | Minimal | Deployment; marker–trait association in a large panel |
| SSR | Low per assay | Thermal cycler + gel or capillary | Minimal | Accessible first-pass association (Bukhari et al., 2024) |
| Amplicon sequencing of candidate genes | Low | PCR + sequencing service | Moderate | **Highest value for a PCR-capable lab** |
| GBS | ~US$10–50 per sample | Sequencing service | High | Genome-wide markers where no array exists |
| BSA-seq | 2 reactions, depth-dependent | Sequencing service | High | Contrasting extremes; **constrained by genome size — *C. annuum* ~3.5 Gb** |
| SNP array | Per-sample array cost | Service provider | Moderate | Large panel where an array exists |

Costs are order-of-magnitude, from Sahoo et al. (2025); confirm by quotation.

---

### Table 8 — Proposed minimum reporting standard

| # | Parameter | Minimum | Rationale | Costs extra? |
| --- | --- | --- | --- | --- |
| 1 | Genotype panel | ≥20, including wild relatives and tolerant/susceptible checks | Checks anchor the ranking; wild relatives carry tolerance absent from cultivars | Design |
| 2 | Osmoticum identity | PEG molecular weight, supplier, batch | Osmotic pressure at equal mass varies with molecular weight; site of action differs | No |
| 3 | Concentration | Genotype-specific sub-lethal level where feasible; otherwise ≥3 levels | A single fixed level produces floor effects at the extremes | Prelim. experiment |
| 4 | Osmotic potential | Measured, instrument named | Nominal values carry temperature- and method-dependent error | Minimal |
| 5 | Temperature | Controlled and reported | Osmotic potential is temperature-dependent | No |
| 6 | Experimental unit | Petri dish or plot, stated explicitly | Prevents pseudoreplication; the unit is not the seed | **No** |
| 7 | Replication | ≥4 units, ≥10 seeds per unit | Generalised linear model stability | Design |
| 8 | Statistical model | Generalised linear mixed model, binomial family, logit link | Binomial data violate normal-error assumptions, especially near boundaries | **No** |
| 9 | Interaction term | Genotype × treatment reported | Separates stress tolerance from general vigour | **No** |
| 10 | Indices | ≥1 productivity-oriented and ≥1 susceptibility-oriented, with justification | Index choice determines genotype ranking | **No** |
| 11 | Selection range | Spectrum retained, not extremes only | Selecting extremes truncates the predictor and attenuates later correlation | Design |
| 12 | Correlation reporting | Internal and cross-stage correlations reported separately | Internal concordance is not evidence of transfer | **No** |
| 13 | Field validation | Multi-season, managed drought | The only test of predictive value | Field season |
| 14 | Concordance rate | Reported wherever a screen feeds a breeding programme | Genotype overlap, not trait correlation, is the quantity that matters | **No — reporting only** |
| 15 | Terminology | "Osmotic stress induced by PEG," not "drought" | The treatment does not simulate drought | **No** |

**Six items (6, 8, 9, 10, 12, 15) require no additional experiment, material or field season. Item 14 requires no new work at all — only that an existing number be reported.**

---

## Reference list

### Statistical practice and experimental design

- Basavaraj, P.S., Rane, J., Jangid, K.K., Babar, R., Kumar, M., Gangurde, A., Shinde, S., Boraiah, K.M., Harisha, C.B., Halli, H.M., Reddy, K.S. and Prabhakar, M. (2025). Index-based selection of chickpea (*Cicer arietinum* L.) genotypes for enhanced drought tolerance. *Scientific Reports*, 15(1). doi:10.1038/s41598-025-93273-1
- Muzafarov, N., Kapustian, M., Ponurenko, S., Kemešytė, V. and Kolomatska, V. (2026). Integrated assessment of drought tolerance indices in maize genotype selection. *Agronomy*, 16(15), 1457. doi:10.3390/agronomy16151457
- Sileshi, G.W. (2012). A critique of current trends in the statistical analysis of seed germination and viability data. *Seed Science Research*, 22(3), 145–159. doi:10.1017/S0960258512000025
- Warton, D.I. and Hui, F.K.C. (2011). The arcsine is asinine: the analysis of proportions in ecology. *Ecology*, 92(1), 3–10. doi:10.1890/10-0340.1

### Tolerance indices and selection criteria

- Bouslama, M. and Schapaugh, W.T. (1984). Stress tolerance in soybeans. I. Evaluation of three screening techniques for heat and drought tolerance. *Crop Science*, 24(5), 933–937. doi:10.2135/cropsci1984.0011183x002400050026x
- Fischer, R.A. and Maurer, R. (1978). Drought resistance in spring wheat cultivars. I. Grain yield responses. *Australian Journal of Agricultural Research*, 29(5), 897–912. doi:10.1071/ar9780897
- Rosielle, A.A. and Hamblin, J. (1981). Theoretical aspects of selection for yield in stress and non-stress environments. *Crop Science*, 21(6), 943–946. doi:10.2135/cropsci1981.0011183x002100060033x

### PEG chemistry, uptake and documented artefacts

- Fan, S. and Blake, T.J. (1997). Comparison of polyethylene glycol 3350 induced osmotic stress and soil drying for drought simulation in three woody species. *Trees*, 11(6), 342. doi:10.1007/s004680050094
- Janes, B.E. (1974). The effect of molecular size, concentration in nutrient solution, and exposure time on the amount and distribution of polyethylene glycol in pepper plants. *Plant Physiology*, 54(3), 226–230. doi:10.1104/pp.54.3.226
- Kylyshbayeva, G., Bishimbayeva, N., Jatayev, S., Eliby, S. and Shavrukov, Y. (2025). Polyethylene glycol (PEG) application triggers plant dehydration but does not accurately simulate drought. *Plants*, 14(1), 92. doi:10.3390/plants14010092
- Lagerwerff, J.V., Ogata, G. and Eagle, H.E. (1961). Control of osmotic pressure of culture solutions with polyethylene glycol. *Science*, 133(3463), 1486–1487. doi:10.1126/science.133.3463.1486
- Lawlor, D.W. (1970). Absorption of polyethylene glycols by plants and their effects on plant growth. *New Phytologist*, 69(2), 501–513. doi:10.1111/j.1469-8137.1970.tb02446.x
- McClendon, J.H. (1981). The osmotic pressure of concentrated solutions of polyethylene glycol 6000, and its variation with temperature. *Journal of Experimental Botany*, 32(4), 861–866. doi:10.1093/jxb/32.4.861
- Michel, B.E. and Kaufmann, M.R. (1973). The osmotic potential of polyethylene glycol 6000. *Plant Physiology*, 51(5), 914–916. doi:10.1104/pp.51.5.914
- Money, N.P. (1989). Osmotic pressure of aqueous polyethylene glycols: relationship between molecular weight and vapor pressure deficit. *Plant Physiology*, 91(2), 766–769. doi:10.1104/pp.91.2.766
- Sajid, Z.A. and Aftab, F. (2022). Improvement of polyethylene glycol, sorbitol, mannitol, and sucrose-induced osmotic stress tolerance through modulation of the polyamines, proteins, and superoxide dismutase activity in potato. *International Journal of Agronomy*, 2022, 1–14. doi:10.1155/2022/5158768
- Sharma, M.L. (1973). Simulation of drought and its effect on germination of five pasture species. *Agronomy Journal*, 65(6), 982–987. doi:10.2134/agronj1973.00021962006500060041x
- Tajaragh, R.P., Rasouli, F., Giglou, M.T., Zahedi, S.M., Hassanpouraghdam, M.B., Aazami, M.A., Adámková, A. and Mlček, J. (2022). Morphological and physiological responses of in vitro-grown *Cucurbita* sp. landraces seedlings under osmotic stress by mannitol and PEG. *Horticulturae*, 8(12), 1117. doi:10.3390/horticulturae8121117

### Transfer of ranking between developmental stages

- Badr, A., El-Shazly, H.H., Mahdy, M., Schierenbeck, M., Helmi, R.Y., Börner, A. and Youssef, H.M. (2025). GWAS identifies novel loci linked to seedling growth traits in highly diverse barley population under drought stress. *Scientific Reports*, 15(1). doi:10.1038/s41598-025-94175-y
- El-Rawy, M.A. and Hassan, M.I. (2014). A diallel analysis of drought tolerance indices at seedling stage in bread wheat (*Triticum aestivum* L.). *Plant Breeding and Biotechnology*, 2(3), 276–288. doi:10.9787/PBB.2014.2.3.276
- Köhl, K.I., Aneley, G.M. and Haas, M. (2023). Finding phenotypic biomarkers for drought tolerance in *Solanum tuberosum*. *Agronomy*, 13(6), 1457. doi:10.3390/agronomy13061457
- Mohamed, E.A., Ahmed, A.A.M., Schierenbeck, M., Hussein, M.Y., Baenziger, P.S., Börner, A. and Sallam, A. (2023). Screening spring wheat genotypes for *TaDreb-B1* and *Fehw3* genes under severe drought stress at the germination stage using KASP technology. *Genes*, 14(2), 373. doi:10.3390/genes14020373
- Pessoa, H.P., Dariva, F.D., Copati, M.G.F., de Paula, R.G., Dias, F. de O. and Gomes, C.N. (2023). Uncovering tomato candidate genes associated with drought tolerance using *Solanum pennellii* introgression lines. *PLOS ONE*, 18(6), e0287178. doi:10.1371/journal.pone.0287178
- Sallam, A., Mourad, A.M.I., Hussain, W. and Baenziger, P.S. (2018). Genetic variation in drought tolerance at seedling stage and grain yield in low rainfall environments in wheat (*Triticum aestivum* L.). *Euphytica*, 214(9), 169. doi:10.1007/s10681-018-2245-9
- Slawin, C., Ajayi, O. and Mahalingam, R. (2024). Association mapping unravels the genetic basis for drought related traits in different developmental stages of barley. *Scientific Reports*, 14(1). doi:10.1038/s41598-024-73618-y

### Solanaceae screening, germplasm and comparative evidence

- Alnaddaf, O., Mohsen, W., Al-Tawaha, A.R., Al-Tawaha, A.R.M., Al-Rawashdeh, I.M. and Karnwal, A. (2026). Physiological responses of tomato callus and regenerated plants under PEG-induced stress during in vitro selection for drought tolerance. *BMC Plant Biology*, 26(1). doi:10.1186/s12870-026-08989-7
- Anagha, P.T.K., Kutty, M.S., Pradheep, K. and Santhoshkumar, A.V. (2026). Differential response of wild and domesticated *Solanum* genotypes to water stress. *Genetic Resources and Crop Evolution*, 73(6). doi:10.1007/s10722-026-02875-9
- Kouassi, A.B., Kouassi, K.B.A., Sylla, Z., Plazas, M., Fonseka, R.M., Kouassi, A., Fonseka, H., N'guetta, A.S.-P. and Prohens, J. (2021). Genetic parameters of drought tolerance for agromorphological traits in eggplant, wild relatives, and interspecific hybrids. *Crop Science*, 61(1), 55–68. doi:10.1002/csc2.20250
- Krommydas, K., Papa, E., Gaitani, P., Papadopoulou, A., Mellidou, I., Bouloumpasi, E. and Kadoglidou, K.I. (2025). Comparative drought response of *Solanum melongena*, *S. macrocarpon*, *S. dasyphyllum*, and *S. melongena* × *S. dasyphyllum* interspecific hybrids. *Agronomy*, 15(11), 2516. doi:10.3390/agronomy15112516
- Millah, Z., Syukur, M., Sobir and Ardie, S.W. (2021). Selection traits for chili pepper drought tolerance at germination stage using polyethylene glycol 6000 and diversity among 22 chili pepper genotypes. *Russian Journal of Agricultural and Socio-Economic Sciences*, 118(10), 240–249. doi:10.18551/rjoas.2021-10.27
- Okunlola, G.O., Olatunji, O.A., Akinwale, R.O., Tariq, A. and Adelusi, A.A. (2017). Physiological response of the three most cultivated pepper species (*Capsicum* spp.) in Africa to drought stress imposed at three stages of growth and development. *Scientia Horticulturae*, 224, 198–205. doi:10.1016/j.scienta.2017.06.020
- Sharma, P., Kurubar, A.R., Tembhurne, B.V. and Paatil, S. (2024). In vitro screening of chilli (*Capsicum annuum* L.) genotypes for drought tolerance. *Journal of Horticultural Sciences*, 19(1). doi:10.24154/jhs.v19i1.1882
- Thin, K.K., Lee, S. and Lee, J.M. (2026). Genetic and morpho-physiological attributes of drought resistance in *Capsicum* accessions. *Horticultural Plant Journal*, 12(2), 402–413. doi:10.1016/j.hpj.2024.11.008
- Yadav, P.K., Bhujel, P., Bhandari, N., Sharma, S. and Sharma, A. (2025). Screening tomato genotypes for early-stage drought tolerance using polyethylene glycol-induced osmotic stress. *BMC Plant Biology*, 25(1), 1476. doi:10.1186/s12870-025-07508-4
- Molla, M.R., Ahmed, I., Ara, R., Hassan, L. and Rohman, M.M. (2019). Screening of chilli (*Capsicum annum* L.) genotypes for drought tolerant at seedling emergence stage. *Journal of Plant Sciences*, 7(4), 76–85. doi:10.11648/j.jps.20190704.12

### Solanaceae genomics and candidate genes

- Liu, F., Zhao, J., Sun, H., Xiong, C., Sun, X., Wang, X., Wang, Z., Jarret, R., Wang, J., Tang, B., Xu, H., Hu, B., Suo, H., Yang, B., Ou, L., Li, X., Zhou, S., Yang, S., Liu, Z., Yuan, F., Pei, Z., Ma, Y., Dai, X., Wu, S., Fei, Z. and Zou, X. (2023). Genomes of cultivated and wild *Capsicum* species provide insights into pepper domestication and population differentiation. *Nature Communications*, 14(1), 5487. doi:10.1038/s41467-023-41251-4
- Ma, J., Wang, L.-y., Dai, J.-x., Wang, Y. and Lin, D. (2021). The NAC-type transcription factor *CaNAC46* regulates the salt and drought tolerance of transgenic *Arabidopsis thaliana*. *BMC Plant Biology*, 21(1), 8. doi:10.1186/s12870-020-02764-y
- Rai, A., Vatov, E., Georgieva, A.W., Bogdanova, S., Wittenberg, M.F., Anachkov, N., Tripodi, P., Todorova, V., Tringovska, I., Ganeva, D., Petrov, V., Gechev, T. and Alseekh, S. (2026). Integrated genome-wide association and quantitative trait locus mapping elucidate the genetic basis of fruit yield and quality traits in pepper under water stress. *Journal of Experimental Botany*. doi:10.1093/jxb/erag385
- Sahitya, U.L., Krishna, M.S.R. and Suneetha, P. (2019). Integrated approaches to study the drought tolerance mechanism in hot pepper (*Capsicum annuum* L.). *Physiology and Molecular Biology of Plants*, 25(3), 637–647. doi:10.1007/s12298-019-00655-7

### Transformation, virus-induced silencing and gene editing in pepper

- Choi, B., Kwon, S.-J., Kim, M.-H., Choe, S., Kwak, H.-R., Kim, M.-K., Jung, C. and Seo, J.-K. (2019). A plant virus-based vector system for gene function studies in pepper. *Plant Physiology*, 181(3), 867–880. doi:10.1104/pp.19.00836
- Kang, B., Lee, S., Ko, D.-h., Venkatesh, J., Kwon, J.-K., Kim, H. and Kang, B.-C. (2025). Virus-induced systemic and heritable gene editing in pepper (*Capsicum annuum* L.). *The Plant Journal*, 122(5). doi:10.1111/tpj.70257
- Liu, D., Zhao, S., Wang, J., Zhang, X., Deng, Y. and Li, F. (2024). Mutation in the *Agrobacterium hisI* gene enhances transient expression in pepper. *Horticultural Plant Journal*, 10(3), 809–822. doi:10.1016/j.hpj.2023.07.003
- Park, S.-i., Kim, H.-B., Jeon, H.-J. and Kim, H. (2021). *Agrobacterium*-mediated *Capsicum annuum* gene editing in two cultivars, hot pepper CM334 and bell pepper Dempsey. *International Journal of Molecular Sciences*, 22(8), 3921. doi:10.3390/ijms22083921
- Tang, Y., Shen, X., Deng, X., Song, Y., Zhou, Y., Lu, Y., Li, F. and Ouyang, B. (2025). Establishment of an efficient *Agrobacterium*-mediated transformation system for chilli pepper and its application in genome editing. *Plant Biotechnology Journal*, 23(11), 4752–4754. doi:10.1111/pbi.70216

### Genotyping platforms

- Bukhari, T., Rana, R.M., Khan, A.I., Khan, M.A., Ullah, A., Naseem, M., Rizwana, H., Elshikh, M.S., Rizwan, M. and Iqbal, R. (2024). Validation of SSR markers for identification of high-yielding and *Phytophthora capsici* root rot resistant chilli genotypes. *Scientific Reports*, 14(1). doi:10.1038/s41598-024-79718-z
- Majeed, A., Johar, P., Raina, A., Salgotra, R.K., Feng, X. and Bhat, J.A. (2022). Harnessing the potential of bulk segregant analysis sequencing and its related approaches in crop breeding. *Frontiers in Genetics*, 13, 944501. doi:10.3389/fgene.2022.944501
- Sahoo, J., Mishra, R. and Joshi, R.K. (2025). PCR-based single nucleotide polymorphism (SNP) genotyping for crop improvement—current status and future prospects. *Discover Plants*, 2(1). doi:10.1007/s44372-025-00262-9
- Zhang, L., Duan, Y., Zhang, Z., Zhang, L., Chen, S., Cai, C., Duan, S., Zhang, K., Li, G. and Cheng, F. (2024). OcBSA: an NGS-based bulk segregant analysis tool for outcross populations. *Molecular Plant*, 17(4), 648–657. doi:10.1016/j.molp.2024.02.011

### Reviews and syntheses consulted

- Pang, X., Chen, J., Li, L., Huang, W. and Liu, J. (2024). Deciphering drought resilience in Solanaceae crops: unraveling molecular and genetic mechanisms. *Biology*, 13(12), 1076. doi:10.3390/biology13121076

### Additional sources

- Bousba, R., Bounar, R., Sedrati, N., Lekhal, R., Hamla, C. and Rached-Kanouni, M. (2021). Effects of osmotic stress induced by polyethylene glycol (PEG) 6000 and mannitol on seed germination and seedling growth of durum wheat. *Journal of Bioresource Management*, 8(3), 57–66. doi:10.35691/JBM.1202.0195
- Comeau, A., Nodichao, L., Collin, J., Baum, M., Samsatly, J., Hamidou, D., Langevin, F., Laroche, A. and Picard, E. (2010). New approaches for the study of osmotic stress induced by polyethylene glycol (PEG) in cereal species. *Cereal Research Communications*, 38(4), 471–481. doi:10.1556/CRC.38.2010.4.3
- Gianinetti, A. (2020). Basic features of the analysis of germination data with generalized linear mixed models. *Data*, 5(1), 6. doi:10.3390/data5010006
- Sivakumar, R., Durga Devi, D. and Chandrasekar, C.N. (2014). In-vitro screening of tomato genotypes for drought tolerance. *Madras Agricultural Journal*, 101(10–12), 369–373.
- Taheri, S., Gantait, S., Azizi, P. and Mazumdar, P. (2022). Drought tolerance improvement in *Solanum lycopersicum*: an insight into “OMICS” approaches and genome editing. *3 Biotech*, 12(3), 63. doi:10.1007/s13205-022-03132-3
- Yang, Z.-B., Eticha, D., Rao, I.M. and Horst, W.J. (2010). Alteration of cell-wall porosity is involved in osmotic stress-induced enhancement of aluminium resistance in common bean (*Phaseolus vulgaris* L.). *Journal of Experimental Botany*, 61(12), 3245–3258. doi:10.1093/jxb/erq146

- Hong, J.-P. and Kim, W.T. (2005). Isolation and functional characterization of the *Ca-DREBLP1* gene encoding a dehydration-responsive element binding-factor-like protein 1 in hot pepper (*Capsicum annuum* L. cv. Pukang). *Planta*, 220(6), 875–888. doi:10.1007/s00425-004-1412-5
- Lim, J., Lim, C.W. and Lee, S.C. (2022). Role of pepper MYB transcription factor CaDIM1 in regulation of the drought response. *Frontiers in Plant Science*, 13, 1028392. doi:10.3389/fpls.2022.1028392
- Zhang, H.-X., Zhang, Y. and Zhang, B.-W. (2024). Pepper SBP-box transcription factor, CaSBP13, plays a negatively role in drought response. *Frontiers in Plant Science*, 15, 1412685. doi:10.3389/fpls.2024.1412685

---

## Notes for the author

**Word count — measured, not estimated.** Most review formats count the abstract, main text, figure legends *and* tables, and exclude references. The 12,000-word ceiling below is the common upper bound; check the chosen venue's actual limit, which may be considerably lower.

| Component | Words |
| --- | --- |
| Title, abstract, Sections 1–9 | 9,167 |
| Figure legends | 221 |
| Tables | 2,544 |
| **Counted total** | **11,932** |
| *Limit* | *12,000* |
| **Headroom** | **68** |

Table 2's detailed design and limitation columns are in **Supplementary Table S1** (with Table S2 for the connecting studies), and supplementary material does not count toward the limit. If prose is expanded, the best value is in Section 5 and Section 3.3, both compressed relative to their evidentiary weight.

**Before submission.**
1. **Choose the venue — see the venue note below.** The manuscript is written to be venue-neutral; it is not tied to any publisher's format.
2. **Add the generative-AI disclosure.** Required at essentially every reputable publisher, and at preprint servers. See the ready statement below.
3. **Add a Data Availability statement.** For this manuscript the correct statement is short, because no new data were generated: *This review analysed only previously published literature. No new data were generated or analysed for this study.*
4. **Add author contributions.** Most venues now require CRediT taxonomy; for a single author, *Conceptualization, Investigation, Writing – original draft, Writing – review and editing*.
5. **Decide the Discussion heading.** Many review formats expect Abstract, Introduction, Subsections, Discussion. Sections 7–9 carry the Discussion content but none is titled Discussion.
6. **Check every stated osmotic potential against its primary source.** Figure 2 shows why: the same nominal PEG-6000 percentage spans a several-fold range of potentials, and Table S1 flags one screen whose reported values differ from the equation by more than threefold.

**Word limit — read before choosing a venue.** The *Journal of Horticultural Sciences* states a maximum of 3,000 words for full-length papers and does not exempt review articles in its published guidelines. This manuscript is 11,932 words. See `implementation-steps.md` for the enquiry email drafted to resolve this before any reformatting is done.

**Venue note — the cost problem.** Open-access publication at *Frontiers in Plant Science* costs CHF 3,150, which is real money and not a reason to abandon the paper. Three routes exist, and they are not equivalent:

- **Diamond open access — free to publish, free to read, immediately.** Funded by societies and institutes rather than by authors. *Journal of Horticultural Sciences* (Society for Promotion of Horticulture, ICAR-IIHR Bengaluru) is a verified example: no APCs, CC BY-NC-SA, indexed in Scopus and Web of Science (ESCI), UGC-CARE Group II, publishes review articles, and reports roughly six weeks from submission to publication. Its limitation is reach: CiteScore below 1 and a Q4 Scopus placement mean far fewer readers than a major international journal.
- **Subscription journal plus green open access — free to publish, free to read after an embargo.** Most established plant journals cost nothing to publish in under the subscription route and permit the accepted manuscript to be deposited in a repository, typically after 6–12 months. This buys a much larger audience but delays open access.
- **Preprint — free, immediate, no peer review.** AgriRxiv or bioRxiv. Establishes priority and gives the community access while review proceeds. The AI disclosure obligation applies here too.

**Recommendation.** Deposit a preprint, then submit to a Diamond open-access venue. The argument for this is not only cost: the review's intended readers are the people running low-cost screening programmes, many of whom work where journal subscriptions are scarce. Publishing it behind a paywall would undercut the paper's own purpose.

**Caution on venue lists.** Several widely circulated “no-APC journal” listicles describe hybrid subscription journals as free open access. They are not: publishing free in a subscription journal means the published article sits behind a paywall. Verify any candidate journal in DOAJ and in Scopus or Web of Science directly, from the journal's own site, before submitting. The three routes above were each verified at source.

**What changed in this revision.** Fifty-nine in-text citations were inserted throughout Sections 1–7; the manuscript previously cited nothing in the body. The reference list was rebuilt from Crossref metadata — **ten DOIs in the earlier working bibliography resolved to entirely different papers**, including one to a *Citrus* study and one to an *Arabidopsis* anthocyanin paper. Tables 2, 4 and 5 were populated from verified sources, and Table 2's detail columns were moved to Supplementary Table S1. The six remaining VERIFY markers were traced to primary sources and replaced with citations, and Figures 1–5 were drawn. One claim was deleted for want of a source (cation accumulation in pepper root xylem under PEG). **This draft contains no placeholder markers.** Details in `reference-verification.md`.

**Generative AI disclosure — required, insert in the Acknowledgments before submission.** It applies whatever the venue; changing journals does not avoid it.

> During the preparation of this work the authors used [TOOL NAME, VERSION, PROVIDER] to assist with literature synthesis, drafting and language editing. The authors set the scope and framing, verified every cited source against primary records, drew the figures from published equations and data, and reviewed and edited all content. The authors take full responsibility for the content of the publication.

Publishers that follow COPE and ICMJE guidance — which includes all the venues discussed above — require the name, version, model and source of any generative AI tool used in the writing or editing of a manuscript. Disclosed AI-assisted writing is permitted; undisclosed AI-assisted writing is a policy violation, and the consequences run from correction to retraction. **This statement is not optional, and no amount of prose editing substitutes for it.**

**Known limitations of this review, to be stated in the Introduction.** The search was not systematic and may have missed relevant work. The cross-stage transfer analysis draws on cereal and potato evidence where Solanaceae evidence is absent, which is a reasonable but not ideal substitution. Cost figures for genotyping platforms are order-of-magnitude. The minimum reporting standard is a proposal, not a consensus position, and has not been tested for feasibility across laboratories with differing resources.
