# Study Inventory — The Review's Backbone

Populated Table 2 (screening studies) and Table 4 (candidate genes) for the Solanaceae-scoped review.
**Every row must be verified against the primary source before submission.** Rows marked ⚠️ are partially verified.

---

## Table 2 — Osmotic / PEG screening studies

### 2a. *Capsicum annuum* (chilli)

| # | Study | n | Stage | PEG level(s) | Traits / indices | Genotypes identified | Checks | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | *J. Horticultural Sciences* (IIHR), 2024 | 16 | Seedling | 5% (−0.3 MPa), 10% (−0.6 MPa), 15% (−0.9 MPa) + control | CRD factorial, 3 reps | **UARChH 42, UARChH 43, Arka Swetha** | ⚠️ not stated | Single season; osmotic potential assumed not measured |
| 2 | RJOAS 10(118), 2021 | 22 | Germination | 15% | Shoot length, root length, root:shoot, seedling length, shoot DW, germination % → drought sensitivity index | **C7** (tolerant across all traits); C120, C37, C18 tolerant | ✅ Gada MK F1 (commercial tolerant) + Tit Super | ⚠️ **Commercial tolerant check scored only "moderate"** — direct evidence of stage/mechanism specificity |
| 3 | Molla et al. (2019) *J. Plant Sciences* 7(4):76–85 | 47 | Germination / emergence | 12.5% | RGE, RGR, RGI, RVI, relative PEG injury rate; dendrogram (4 clusters, cophenetic 0.668) | **BD-10906, BD-10912, BD-10911, BD-10916, BD-10913** (top 5); BD-10902, RT-20, AM-29, BD-10893, BD-10930 (bottom 5) | ⚠️ not stated | Single season; ranking from aggregated score, no independent validation |
| 4 | Mollah et al. (2021) — seedling-stage chilli screening | ⚠️ | Seedling | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **Retrieve full record** |
| 5 | Arka Lohit study (8 cultivars) ⚠️ | 8 | Seedling | 20% | Proline accumulation, root:shoot dry weight | **Arka Lohit** (highest proline + root:shoot DW) | ⚠️ | ⚠️ 20% described as "moderate stress" — check vs. other studies calling 15% severe |

> **Finding to highlight in §3:** row 2 is published evidence for the review's thesis. The commercial *drought-tolerant* check did not rank top — the authors attributed this to tolerance being mechanism- and stage-specific. That is the opening the review needs.

### 2b. *Solanum lycopersicum* (tomato) — comparative evidence

| # | Study | n | Stage | PEG level(s) | Traits / indices | Genotypes identified | Limitations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | Yadav et al. (2025) *BMC Plant Biol* 25:1476 | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | **Priority retrieval — recent, directly comparable** |
| 7 | *BMC Plant Biol* (2026) in vitro callus selection | ⚠️ multi | **Callus** (root explants) | **0–8%**, MS + 2 mg/L BAP + 0.2 mg/L NAA | RGR, viability, **LC50 per genotype** | **Daraa, Brieh** (best RGR maintenance); Baskanta worst at 8% | Authors state molecular validation + field evaluation still required |
| 8 | F2/F3 population screening, 2026 | 26 populations | Germination | 12% | Germination capacity, abnormal seedlings, growth rate, vigour index, shoot/root length, FW, DW | Population-level | Germination capacity 90% → 60.6%; vigour index 26.3 → 2.84 |
| 9 | MASU *J.* 2(1) — in vitro screening | 32 | Germination / seedling | −0.2 and −0.35 MPa | Germination %, root length, shoot length, seedling DW, vigour index | **LE 18** (germination 100 → 96.7 → 60.0); LE 27 next | **Germination arrested completely at −0.35 MPa in most genotypes** — ceiling of the screen |
| 10 | Genotypic differences vs. PEG-simulated drought | 20 of larger set | Seedling | 4% | Proline, membrane stability index, biomass | Genotypes 6232–6234 series, 10584, 10587 | Proline used as a secondary discriminator |

> **Design finding worth promoting to Table 6:** study 7 determined a **genotype-specific sub-lethal PEG concentration (LC50)** rather than applying a fixed arbitrary threshold to all genotypes. This is methodologically superior — a fixed concentration either fails to discriminate tolerant lines or kills everything. **Recommend it as a minimum standard.**

> **Ceiling finding:** study 9 shows most tomato genotypes fail to germinate at all at −0.35 MPa. Screening above a genotype-independent threshold therefore produces floor effects, not rankings.

### 2c. Other Solanaceae

| # | Study | Species | Design | Finding |
| --- | --- | --- | --- | --- |
| 11 | *Agronomy* 15(11):2516, 2025 | *S. melongena* vs *S. macrocarpon*, *S. dasyphyllum*, interspecific hybrids | Water stress, early stage (4 wk) | **Cultivated eggplant highly sensitive** (LAI ↓47.7–55.4%, biomass ↓31.4–38.6%); wild species tolerant; hybrids intermediate with heterosis retained → **wild relatives as rootstocks** |
| 12 | *Genet. Resour. Crop Evol.* (2026) | 24 genotypes / 15 *Solanum* species | 100% vs 35% water | Tolerant: ***S. torvum*, *S. viarum*, *S. violaceum*, *S. aethiopicum***. Susceptible: *S. pseudocapsicum*, *S. melongena*. PCA: catalase, proline, stomatal conductance, transpiration, root length, shoot DW → **80.2% of variation** |
| 13 | Kouassi et al. (2021) *Crop Science* | *S. melongena* + wild relatives + F₁ hybrids | Field, dry vs rainy season | Genetic parameters for drought tolerance; *S. insanum* (primary gene pool) tolerant → usable donor |
| 14 | Eggplant progressive-drought transcriptomics (2026) | *S. melongena* GPE020510 (tolerant) vs GPE008940 (sensitive), G2P-SOL core | RNA-seq, moderate + severe stress | Tolerance = **early ABA-centred regulation** (*ABI5*, *TAS14*, LEA/dehydrin) + transport/redox; sensitive genotype showed RNA/protein-turnover signatures instead |

> **Comparative insight for §5:** the wild-relative strategy is *established* in eggplant and *emerging* in tomato, but barely applied in *Capsicum* — where the cultivated gene pool dominates screening panels. That asymmetry is a publishable observation.

---

## Table 4 — Candidate genes and their true evidence level

**Critical: report the validation host.** Much *Capsicum* gene work is validated in *Arabidopsis*, not in pepper. That is a lower evidence level than it is usually reported as.

| Gene | Family | Species | Validation | True level | Note |
| --- | --- | --- | --- | --- | --- |
| ***CaNAC46*** | NAC (ATAF) | *C. annuum* | Transgenic *Arabidopsis*; VIGS in pepper | **L1–L2** | Induced by drought, salt, cold, heat, ABA, SA, MeJA. Promotes *SOD*, *POD*, *RD29B*, *RD20*, *ABI*, *P5CS*. Silencing ↑ MDA under stress. **Best-characterised *Capsicum* entry point** |
| *CaDREB1* | AP2/ERF | *C. annuum* | ⚠️ | **L2** | Increased levels enhance drought tolerance via drought-inducible genes |
| *CaAIMK1* | MAPK | *C. annuum* | ⚠️ | L0–L1 | ABA-induced MAP kinase; implicated in drought avoidance / WUE |
| *SlAREB1 / SlAREB2* | bZIP | *S. lycopersicum* | Transgenic tomato | L2 | ABA-dependent pathway; upregulate oxidative-stress and ABA-responsive genes |
| *SlDREB1/2/3* | AP2/ERF | *S. lycopersicum* | Transgenic; genome-wide family characterised | L2 | *SlDREB2* is a transcriptional activator of DRE elements. Family-wide analysis published (Frontiers, 2022) |
| *SlJUB1* | NAC | *S. lycopersicum* | Transgenic | L2 | Binds *SlDREB* and *DELLA* promoters; ROS homeostasis |
| *SlNAC4, SlNAC6, SlNAC35, SlNAC042, SlNAP1, SlNAC2* | NAC | *S. lycopersicum* | Mixed | L1–L2 | Multiple positive regulators catalogued |
| *SlWRKY8, SlWRKY6, SlERF5, SlERF84, SlMYB49* | WRKY/ERF/MYB | *S. lycopersicum* | Mixed | L1–L2 | Positive regulators |
| *SlWRKY81, SlMYB50, SlMYB55, SlEREB1, SlbZIP38* | — | *S. lycopersicum* | Mixed | L1–L2 | **Negative regulators** — often omitted from reviews; include them |
| *SlMAPK3* | MAPK | *S. lycopersicum* | **CRISPR mutant** | **L1 (genetic)** | Mutants: larger stomatal aperture, ↑ H₂O₂, ↑ MDA, ↑ electrolyte leakage, ↓ antioxidant activity, ↓ *SlDHN*, *SlDREB*, *SlGST* |

### ⚠️ CORRECTED — the asymmetry claim was overstated

**An earlier version of this file claimed *Capsicum* has "not the validated loci." Verification found that is wrong.** Withdrawn and replaced.

What the check found:

| Finding | Source | Consequence |
| --- | --- | --- |
| **Pepper reproductive-stage drought GWAS + QTL** — Balkan *C. annuum* panel (n=133) + interspecific BILs (n=76), WW vs WS; loci on chr 5 & 6; candidate genes *GRL1*, *CYP77A19*, endoglucanase-like | *J Exp Bot* (2026), doi:10.1093/jxb/erag385 | **Directly contradicts the absence claim** |
| **100 *Capsicum* accessions screened at vegetative stage** — resistant IT308761, IT250221, IT158637 (21 d water withholding); susceptible IT158411, IT163497, IT225019, IT237567, IT236754; *An2* MYB noted | ScienceDirect (2025) | Pepper does have germplasm-level drought screening beyond germination |
| **Pepper graph pan-genome** — 500 accessions, 5 domesticated species + wild relatives; *C. baccatum* introgressions carry abiotic stress tolerance genes | *Nature Communications* (2023) | Genomic resources are **not** the constraint |
| **Aquaporin contrast** — all 12 AQPs up in tolerant KCa-4884, down in susceptible G-4 | PMC6522565 | Pepper has genotype-contrasting mechanism data |

### The revised asymmetry — stage stratification, not absence

| Stratum | *Capsicum* | Tomato | Eggplant |
| --- | --- | --- | --- |
| **A — Germination** | Active (Table 2a: 5 studies) | Active (Yadav 2025; 32-genotype; F2/F3) | Limited |
| **B — Vegetative** | 100-accession screen (2025); root-architecture screen (30 accessions) | Active | Active |
| **C — Reproductive** | **1 recent GWAS+QTL study (2026)** | **Many** — 19 QTL (*S. habrochaites* chr 9); 56 QTL (F7 RILs); 12 QTL; 54 QTL (MAGIC); CRISPR *SlMAPK3* | Genetic parameters (Kouassi 2021); transcriptomics |
| **Wild-relative donors** | Under-used in screening panels; pan-genome shows introgression potential | ✅ *S. habrochaites*, *S. pimpinellifolium* | ✅ **Best developed** — *S. torvum*, *S. viarum*, *S. violaceum*, *S. aethiopicum*, *S. insanum* |
| **Studies connecting strata** | **0 identified** | **0 identified** | **0 identified** |

> **The corrected argument is stronger and harder to refute.** It is not "pepper lacks the genetics" — it is "all three crops stratify drought work by developmental stage, and nothing connects the strata." Pepper simply has thinner coverage in Stratum C than tomato.

### Stage-specificity evidence *within Capsicum* — highly citable

| Finding | Detail |
| --- | --- |
| ***C. chinense* more drought-tolerant** than *C. annuum* and *C. frutescens* | African 3-species comparison, 4 drought regimes × 3 stages |
| **All three species more susceptible at vegetative than at flowering/fruiting** | Direct within-genus evidence of stage-specificity — the review's core phenomenon |
| Capsaicin content altered by drought in *C. chinense* but not *C. annuum* | Quality consequence with applied relevance |

---

## Competing reviews — MUST be differentiated from

**A reviewer will ask why your review is needed. Answer it in the Introduction.**

| Review | Scope | How yours differs |
| --- | --- | --- |
| *Deciphering Drought Resilience in Solanaceae Crops: Molecular and Genetic Mechanisms* (2024) | Molecular/genetic mechanisms across Solanaceae | Mechanisms. **Yours is methodology and predictive validity** — different question entirely |
| *Drought tolerance improvement in* Solanum lycopersicum: *OMICS approaches and genome editing* (2022) | Tomato omics + editing | Tomato-only, technology-focused |
| *Molecular mechanisms and genomic strategies for stress resilience in pepper* (2025) | Pepper genomics, all stresses | Pepper-only, discovery-focused, not screening-focused |
| *Heat stress resilience in* Capsicum annuum (2025) | Heat, not drought | Different stress |

**Required statement in your Introduction:** name the existing reviews, state what they cover, and state explicitly what yours covers that they do not — *screening methodology, its documented artefacts, its untested predictive validity, and the transfer of validated approaches from tomato and eggplant*. Without this paragraph, the first reviewer comment will be "how does this differ from X?"

---

## Retrieval priorities

1. **Yadav et al. (2025)** *BMC Plant Biol* 25:1476 — most recent directly comparable tomato screening study
2. **Mollah et al. (2021)** — chilli seedling-stage screening
3. **Michel & Kaufmann (1973)** — the PEG concentration ↔ osmotic potential conversion standard, needed for Figure 2
4. **Any *Capsicum* drought GWAS or QTL** — if one exists, the asymmetry claim in §5 needs softening

---

## CONNECTING STUDIES — the systematic count (falsifies the "zero" claim)

Searched for studies testing the **same genotypes at more than one developmental stage**. Nine found across four crops. **The literature contradicts itself.**

| # | Study | Crop | Stages connected | Outcome | Direction |
| --- | --- | --- | --- | --- | --- |
| C1 | *S. pennellii* introgression lines, **PLoS ONE 2023** | **Tomato** | Germination/seedling → vegetative/reproductive | IL 1-4-18 and IL 1-2 tolerant at all stages; most germination-tolerant also most tolerant later. Genes: *AHG2*, *PRXIIF*, *SAP5*, *PRXQ*, *CFS1*, *LCD*, *CCD1*, *SCS* | ✅ **supports** |
| C2 | Sallam et al. 2018, *Euphytica* 214:169 | Wheat | Seedling indices → grain yield, 2 environments × 2 seasons | **"No significant correlations found between seedling traits and grain yield in any environment"**; only 1 genotype had both | ❌ **contradicts** |
| C3 | Sci Rep 2024 (164 barley lines) | Barley | Germination/seedling → heading-stage yield | r = **−0.25** germination rate vs yield. 9 lines 100% germination → only 2 with no yield penalty (~22% transfer) | ❌ **contradicts** |
| C4 | Sci Rep 2025 (barley GWAS, 198 genotypes) | Barley | Germination + seedling + vegetative + flowering | "Drought tolerance in barley is **consistent** when determined at the three important growth stages" | ✅ **supports** — directly contradicts C3 |
| C5 | Wheat diallel, *Plant Breed. Biotech.* 2014 | Wheat | Seedling PEG → grain yield/spike | Root length r = 0.41\*, seedling DW r = 0.46\* at **15%** PEG; non-significant at **20%** | ✅ supports, concentration-dependent |
| C6 | *Genes* 2023 (KASP wheat) | Wheat | Germination → seedling | "**Little to no correlation** in drought tolerance between germination and seedling stage" (citing Hasseb; Moursi) | ❌ contradicts |
| C7 | *Agronomy* 2023 (potato, 20 lines, 3 trials) | Potato | Vegetative growth curves → yield | LAI and A2 turning points correlated with drought tolerance across trials | ✅ supports |
| C8 | PMC6522565 | *Capsicum* | — (mechanism contrast) | 12 aquaporins up in tolerant KCa-4884, down in susceptible G-4 | — |
| C9 | Yadav et al. 2025, BMC | Tomato | Germination/seedling | Tolerant lines "promising candidates for **field validation**" — authors state validation is outstanding | ⚠️ untested |

### Score: 4 support, 4 contradict, 1 untested

> **The "zero connecting studies" claim was wrong and is withdrawn.** The real finding — a genuinely contradictory literature — is stronger.

### ⭐ THE BEST ORIGINAL METHODOLOGICAL POINT

**Internal concordance is being reported as cross-stage transfer.** Several studies reporting "strong correlations" correlate traits *within* one stage or treatment (germination % with germination rate; root with shoot biomass) — near-tautological relationships between co-measured growth traits. These appear in the same correlation matrices as cross-stage relationships, making a study *appear* to demonstrate transfer when it has only demonstrated internal consistency.

**Nobody appears to have made this criticism explicitly for this literature.** It explains the contradiction better than any biological account, and it is the review's strongest single contribution.

### ⭐ SECOND POINT — the wrong test may be applied

In C2, **no** seedling trait correlated with yield, yet **individual genotypes** were identified that were tolerant at seedling stage and high-yielding in the field. A breeding programme needs the right *genotypes*, not a significant *trait* correlation. Reviews dismissing early screening on absent trait correlations may be applying the wrong test. **The correct metric is the concordance rate among selected genotypes — and almost nobody reports it.**

### Third point — tolerance and recovery are genetically distinct

C2 found tolerance traits (wilting) and recovery traits (regrowth) to be weakly correlated or uncorrelated, with **QTLs entirely different except one pleiotropic locus**. Undercuts the practice of treating a composite index as a general "drought tolerance" measure.

### Capsicum remains the gap

Of nine connecting studies, **seven are cereals or potato**, one is tomato, and **none is *Capsicum***. The chilli-specific question — does a germination screen predict field drought performance in pepper? — has not been answered.

---

## SECTION 2 SOURCE FILE — PEG chemistry and artefacts

### ⚠️ THREE MORE CLAIMS CORRECTED DURING §2 DRAFTING

| Planned claim | Verdict | Evidence |
| --- | --- | --- |
| Commercial PEG impurities cause artefacts | ❌ **TESTED AND REJECTED** | Lawlor 1970: purified by gel filtration vs unpurified, maize growth unaffected. Sephadex chromatography showed passage through plants did not alter average MW → no selective absorption of contaminant small molecules |
| PEG detergent properties cause toxicity | ❌ **TESTED AND REJECTED** | Lawlor 1970: comparison with non-ionic detergents ruled it out |
| PEG does not enter plant tissues (standard justification) | ❌ **CONTRADICTED** | See below — reversed into a finding |

### ⭐ Claim reversed into the section's strongest point: the penetration question

**Established uptake, measured directly:**
- Lawlor 1970: **PEG ≥ 1000 MW entered plants at ~1 mg/g leaf FW/week**; entry increased substantially with **mechanically damaged roots or low water potentials** — i.e. exactly the conditions of a drought experiment. Autoradiography localised PEG 4000 at leaf margins then mesophyll ✅
- **Lagerwerff et al., pepper (*Capsicum annuum* L. var. California Wonder)** — directly the review's focal crop. Plants at −3.0 / −5.0 bar with PEG 400, 600, 1000, 1540, 4000:
  - PEG **1000 and 1540 most satisfactory** as osmotica
  - Accumulation **inversely related to molecular weight**, greater at lower (more negative) osmotic potential, increased with time
  - **Except PEG 4000, more PEG in leaves than roots**; PEG 4000 retained mainly in roots
  - Once leaf concentration reached 1–2 mg/mL, further absorbed PEG transferred to leaves ✅

**Fair qualifications to state:**
- Entry is **slow** for high MW (~1 mg/g FW/week); over a 7–10 d germination assay this is small in absolute terms
- Modern papers routinely assert non-penetration — but an assertion in an introduction is not a measurement

**Consequence:** the PEG-vs-mannitol contrast is **one of degree, not kind**. Mannitol uptake is real; PEG uptake is also real, and molecular-weight dependent.

### The osmoticum comparison is unresolved

| Study | Conclusion |
| --- | --- |
| *Cucurbita* landraces, *Horticulturae* 2022 | **Mannitol simulated osmotic stress better than PEG** for most attributes and concentrations; PEG better for some biochemical discriminators ✅ |
| Durum wheat, *J. Bioresource Management* | **PEG superior** to mannitol; mannitol effects **reversible**, consistent with uptake ✅ |
| Pasture species, *Agronomy Journal* 1973 | PEG **> NaCl > mannitol** in severity at iso-potential; both NaCl and mannitol suspected to enter seeds ✅ |

> **Opposite conclusions. Report as unresolved.**

### Michel & Kaufmann 1973 — actual content (more useful than the usual citation)

- ψs **curvilinearly related to concentration**; **linearly increasing with temperature**
- Empirical equation valid **only 15–35 °C**
- **Thermocouple psychrometer readings are MORE NEGATIVE than vapour pressure osmometer readings**; psychrometer judged closer to correct for bulk solutions
- Effects "related to structural changes in the PEG polymer" — not behaving like salts/sugars ✅

> **So "osmotic potential measured" is not a complete methods statement — the instrument must be named.**

### PEG solutions are non-colligative

- PEG produces **greater osmotic effect than the molecule count predicts**; the discrepancy correlates with polymer mass; attributed to water sequestration ✅
- Freezing-point osmometry **overestimates** vs vapour pressure osmometry; PEG can inhibit ice crystallisation, distorting freezing-point readings ✅
- Practical upshot: nominal % → MPa conversion tables carry error of unstated magnitude

### Established artefacts (keep these)

| Artefact | Evidence |
| --- | --- |
| **Hypoxia** — high PEG concentrations raise viscosity, limiting O₂ diffusion to roots | ✅ |
| **Greater tissue damage than equivalent soil drying** — same water-potential decline, but **significantly greater membrane injury**, larger reductions in photosynthesis and stomatal conductance, **slower recovery**; even brief exposure worse than soil drought | 3 woody species ✅ |
| **Ion accumulation** — PEG 400 associated with increased K⁺, Na⁺, Ca²⁺, Mg²⁺ in pepper root xylem | ⚠️ verify primary source |
| **Mechanism** — Lawlor proposed **physical blockage of the water-movement pathway**, not chemical toxicity | ✅ |

### The counter-case — MUST be reported

**Agronomy Journal 1973, 5 pasture species:** under non-limiting soil/seed contact and water flow, **the equivalence of osmotic (PEG) and matric potential held for all species**, and PEG "did serve as a convenient and satisfactory media for studying the effect of true drought on seed germination" ✅

> Omitting this would make §2 advocacy rather than review.

### The concrete methodological gap

**Solidified PEG media and raft-and-membrane systems** were developed specifically to prevent PEG uptake while imposing osmotic stress (Cereal Research Communications 2010) ✅. They remain **almost unused in Solanaceae screening**. Specific, cheap, and links §2 to §7's framework.

### The terminology finding

**Kylyshbayeva et al. 2025, *Plants* 14(1):92** — "Polyethylene Glycol (PEG) Application Triggers Plant Dehydration but Does Not Accurately Simulate Drought." States that authors describing PEG application as "drought, dehydration, osmotic, or water stresses" **mislead readers** ✅. Reviews the agar/Petri-dish use for germinated seeds and young seedlings ✅.

> Cite this as the authoritative basis for the "stop calling it drought" recommendation.
