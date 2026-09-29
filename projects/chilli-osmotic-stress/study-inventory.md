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

### The asymmetry — the core of §5

| Resource | Tomato | *Capsicum* | Eggplant |
| --- | --- | --- | --- |
| Drought QTL mapped | **Many** — 19 from *S. habrochaites* sub-NILs (chr 9); 56 from 119 F7 RILs (11 under drought); 12 under drought; 54 from MAGIC | **Scarce** | Few |
| GWAS for drought | ⚠️ limited (mostly fruit traits) | **Limited** — GWAS has targeted agronomic/fruit traits | Limited |
| Characterised TF families | **Extensive** | **Narrow** — *CaNAC46*, *DREB1*, *AIMK1* | Emerging |
| CRISPR validation | ✅ (*SlMAPK3*) | ⚠️ limited by transformation recalcitrance | Limited |
| Wild relatives used as donors | ✅ (*S. habrochaites*, *S. pimpinellifolium*) | ⚠️ underused in screening panels | ✅ **Established** (*S. torvum*, *S. viarum*, *S. insanum*) |

> **This table is the review's argument in one view.** Tomato and eggplant have built the genetic architecture for drought breeding; *Capsicum* has the screening literature and the genomic sequence, but not the validated loci. The review's contribution is to specify what transfers and how.

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
