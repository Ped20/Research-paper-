---
name: writing-plant-science-papers
description: Paragraph-level structural blueprint for molecular biology, plant science, and agricultural research papers. Provides section blueprints, evidence-ladder rules, figure-story planning, statistical reporting, and venue-specific formatting for journals from Nature Plants and The Plant Cell through to Field Crops Research and BMC Plant Biology. Use when user says "写植物论文", "写分子生物论文", "plant science manuscript", "molecular biology paper structure", "agronomy paper", "crop science manuscript", "OSDI-equivalent for biology", or wants fine-grained structural guidance for a plant/agriculture journal submission.
argument-hint: [venue-or-section]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Writing Plant Science & Agriculture Papers: Paragraph-Level Blueprint

Structural guidance for **$ARGUMENTS**

## Relationship to Other Skills

- **paper-write**: General generation workflow with citation verification. This skill supplies the biology-specific skeleton on top of it.
- **paper-plan**: Research outline creation. Use paper-plan first for *what* to study; use this skill for *how to structure the report of it*.
- **paper-slides**: Conference talk generation. No overlap.

**Boundary**: this skill gives you page budgets, paragraph roles, evidence-calibration rules, and figure logic for molecular-biology / plant-science / agronomy venues. It does not generate LaTeX, verify references, or produce data.

---

## 0. The Core Translation (read this first)

Systems papers and biology papers are both "problem → insight → evidence → conclusion." Everything else differs. This table is the whole adaptation:

| Systems paper concept | Biology / agriculture equivalent |
| --- | --- |
| Problem statement | Biological question or trait gap |
| Gap analysis (G1–Gn) | Knowledge gaps + limitations of the current model |
| Key insight / thesis | **Central advance**: gene/pathway/mechanism → trait |
| Design (architecture) | Mechanistic model + experimental strategy |
| Implementation | Materials & Methods (lines, constructs, assays, field design) |
| Evaluation | **Results** — the evidence for each claim |
| Baselines | Wild type, empty vector, null allele, current cultivar, standard practice, prior model |
| Ablation study | Genetic dissection: single mutants, domain deletions, epistasis |
| Scalability | **Generalizability**: other species, environments, years, genotypes |
| "Discuss alternatives for every choice" | "Rule out alternative interpretations for every claim" |
| Contribution list (numbered) | Advance statements (usually prose, not numbered) |
| Separate Related Work section | **Discussion**, where prior work is integrated claim-by-claim |
| Reproducibility checklist | Reporting standards + data deposition + accession numbers |

**The single most important consequence:** a systems paper's currency is *architectural novelty*. A biology paper's currency is **evidence strength for a causal claim**. Reviewers will not accept an argument because it is elegant; they will accept it only if the evidence ladder supports it.

---

## 1. The Evidence Ladder (the spine of the paper)

Before drafting, place every claim you intend to make on this ladder. This determines both the experiment list and the verb you are allowed to use.

| Level | Evidence type | Typical experiments | Permitted verbs |
| --- | --- | --- | --- |
| **L0** | Association | Expression correlation, co-expression network, GWAS signal, QTL interval, transcriptome comparison | "is associated with", "correlates with", "co-varies with" |
| **L1** | Necessity | T-DNA / CRISPR / RNAi knockdown, null mutant phenotype | "is required for", "loss of X reduced/impaired" |
| **L2** | Sufficiency | Overexpression, ectopic expression, inducible induction, heterologous expression | "is sufficient to", "ectopic expression restored" |
| **L3** | Specificity | Complementation with WT vs. mutant construct, ≥2 independent alleles, domain swap, catalytic-dead variant | "acts through", "depends on the ... domain" |
| **L4** | Physical mechanism | Y2H, BiFC, split-luc, Co-IP, pull-down, in vitro reconstitution, enzymatic assay, structural data | "physically interacts with", "directly promotes" |
| **L5** | Order of action | Epistasis / double mutant, tissue-specific rescue, temporal induction | "acts upstream/downstream of" |
| **L6** | Conservation | Ortholog functional test, natural variation, multi-species comparison | "is conserved in" |
| **L7** | Applied impact | Multi-year field trial, yield, stress tolerance under agronomic conditions | "improved ... in the field", "under field conditions" |

### Rule 1: The verb ceiling

**Your strongest verb must not exceed your evidence level.** This is the most common rejection cause in the field. If your only data are expression patterns and mutant phenotypes, you have L0–L1 and must write "is required for" — never "regulates" as a settled fact, and never "controls."

Drafting check: highlight every causal verb in your abstract. For each one, write the supporting figure panel in the margin. Any verb without a panel behind it gets downgraded.

### Rule 2: One claim, multiple independent lines

A claim supported by one line of evidence is an **observation**. A claim supported by independent lines (genetics + biochemistry + expression) is a **conclusion**. Aim for at least two independent lines per major claim.

Where claims share a single method (e.g., three claims all resting on qRT-PCR), flag the shared dependency explicitly in the Discussion — reviewers will find it.

### Rule 3: Must-do controls checklist

| Claim type | Controls reviewers demand |
| --- | --- |
| Gene expression (qPCR) | ≥2 (ideally 3) stable reference genes, validated by MIQE; no reference gene validation = desk-reject at strict venues |
| Mutant phenotype | ≥2 independent alleles; segregation analysis; background homozygosity |
| Complementation / rescue | WT construct rescues, mutant construct does not; same promoter/context |
| Protein interaction | Reciprocal test (bait/prey swap), negative control, expression verification |
| Overexpression | Empty-vector control line, expression level verified |
| Treatment effect | Untreated control, mock treatment, time-matched sampling |
| Field trial | Randomized design, blocking, ≥2 site-years, weather + soil characterization |

---

## 2. The Figure Story (plan this before writing prose)

**Rule: draw the figures first.** A biology paper is a sequence of figures that walks a reader from observation to mechanism. If you cannot sketch the figure sequence, you do not yet know what the paper argues.

**Reverse outline method** — write one sentence per planned figure panel:
> "Fig 3B shows that *x* mutant siliques are shorter than WT (n = 30, P < 0.001)."

Collect these sentences. They become: the Results subsection headings, the figure legends' first sentences, and the Discussion's topic sentences. If two sentences say the same thing, the corresponding figures should merge.

### Standard figure architectures

**Molecular / mechanistic paper (6–8 figures):**

| Figure | Logical step | Content |
| --- | --- | --- |
| 1 | Context | The phenotype / biological phenomenon. Establishes that the question matters |
| 2 | Discovery | Gene identification: mutant screen, QTL, DEG list, GWAS hit |
| 3 | Pattern | Spatiotemporal expression, tissue localization, promoter activity |
| 4 | Necessity | Loss-of-function phenotype (L1) |
| 5 | Sufficiency | Overexpression / ectopic / inducible (L2) |
| 6 | Mechanism | Interaction, activity, localization, biochemistry (L4) |
| 7 | Order / specificity | Epistasis, rescue with variant constructs (L3, L5) |
| 8 | Model | Schematic working model — **solid arrows = established here, dashed = inferred** |

**Agronomy / applied paper (tables are first-class, unlike systems papers):**

| Item | Content |
| --- | --- |
| Table 1 | Site description: coordinates, soil classification, weather, management |
| Table 2 | ANOVA / mixed-model output: sources of variation, df, F or χ², P |
| Fig 1 | Treatment or genotype effect on the primary trait, across site-years |
| Fig 2 | G×E: AMMI / GGE biplot or stability parameters |
| Fig 3 | Relationship / dose–response / regression with fitted model |
| Table 3 | Economic or practical analysis (gross margin, partial budget) |

### The four-statement rule

Every conclusion must appear **four times**, in four registers:

1. **Hypothesis** — closing sentence of the Introduction, or the rationale sentence opening the Results subsection
2. **Result** — the concluding sentence of that Results subsection
3. **Caption** — the first sentence of the figure legend, standalone and quantitative
4. **Interpretation** — the topic sentence of the corresponding Discussion paragraph

A finding stated once, in the middle of a paragraph, will be missed by the reviewer skimming your PDF.

### Figure QA

- Define every error bar in the legend: SD, SE, or 95% CI. "Error bars represent SD" is mandatory.
- State n in every legend, and state whether n is biological or technical replicates. **Technical replicates are not replicates for inference.**
- Prefer showing individual data points over bar-and-whisker for small n (see Weissgerber et al. 2015 in Sources).
- Micrographs: scale bar in every panel, identical exposure/processing within a comparison.
- **Image integrity**: no splicing without explicit demarcation, no selective adjustment of a region, no duplicated or reused panels. Journals now run automated forensics. This ends careers.

---

## 3. Word / Page Allocation

### Molecular-scale paper (e.g. 7,000-word limit, 6–8 display items)

| Section | Words | Notes |
| --- | --- | --- |
| Title | 10–20 | No abbreviations; state the finding, not just the topic |
| Abstract | 200–250 | Unstructured at most plant journals; see §4 |
| Introduction | 700–1,000 | 5–7 paragraphs |
| Results | 2,000–3,000 | 6–8 subsections, one per logical figure step |
| Discussion | 1,200–1,800 | 5–8 paragraphs; usually ≤30% of total |
| Materials & Methods | 1,500–2,500 | Often supplementary at Nature-family venues |
| Conclusions | 0–400 | Optional; some venues forbid a separate section |
| References | — | 40–70 typical |
| Display items | — | 6–8 figures/tables |

### Applied / agronomy paper (e.g. Field Crops Research)

| Section | Words | Notes |
| --- | --- | --- |
| Abstract | 250–400 | Usually **structured**: Context & Objective / Methods / Results & Conclusions / Significance |
| Highlights | 3–5 bullets | ≤85 characters each, including spaces |
| Introduction | 500–800 | Ends with an explicit objective statement |
| Materials & Methods | 1,000–1,500 | Field design, statistics, site characterization |
| Results | 1,200–1,800 | Often combined as "Results and Discussion" |
| Discussion | 1,200–2,000 | Must address agronomic + economic significance, not just statistical |
| Conclusions | 300–500 | Practical recommendation + generalizability limits |
| References | — | 50–80 typical |

**The agronomic significance ladder** — a distinct obligation with no systems-paper analogue. Every effect must be reported at three levels:

1. **Statistical** — is the effect real? (P, CI, model diagnostics)
2. **Agronomic** — is the effect large enough to matter in the field? (a significant 2% yield gain may be noise to a grower)
3. **Economic / practical** — does it pay, and under what conditions? (gross margin, break-even)

Papers that stop at level 1 are routinely rejected as "incremental."

---

## 4. Section Blueprints

### Title

Two formulas that work:

- **Mechanistic**: `[Gene/Protein] [verb] [process] to [outcome] in [species]` — e.g. "X controls flowering time through Y in *Arabidopsis*"
- **Applied**: `[Practice/genotype] [effect] on [trait] under [conditions]` — e.g. "Delayed sowing increases water-use efficiency in wheat under Mediterranean conditions"

Avoid: puns, "Novel...", "Study of...", question form, and titles that name only the topic without the finding.

### Abstract (4–6 sentences)

```
S1: Background — what is known and why this trait/process matters
S2: Gap — what remains unresolved ("However, whether... remains unknown")
S3: Approach — what you did, in one sentence, with species and system
S4: Key result(s) — quantitative, with direction and magnitude
S5: Mechanism/interpretation — what this means biologically
S6: Implication — applied relevance or broader significance
```

**Hard rules:**
- No citations, no abbreviations (or define them), no figure references.
- The abstract is the paper's only advertisement — every claim in it must be traceable to a figure.
- Do **not** let the abstract outrun the figures. Editors now specifically check for abstract-to-evidence mismatch, and it is a leading cause of rejection *after* peer review.

Structured variants (BMC: Background / Results / Conclusions; Field Crops Research: four headed sections) — same logic, labelled.

### Introduction (5–7 paragraphs)

```
P1  Territory      — the biological process/trait, why it matters. Agricultural,
                     ecological, or fundamental stakes. Concrete, not rhetorical.
P2-3 Knowledge     — what is currently established. Cite primary literature,
                     not reviews, for foundational claims. This is a funnel.
P4  Gap            — the specific unresolved question. Must be falsifiable and
                     specific: not "little is known about X" but
                     "whether X acts in the same pathway as Y is unknown."
P5  Rationale      — why this species, this system, this approach. Justify the
                     choice, don't just assert it.
P6  Advance        — what you show and what it means. Preview the finding.
```

Systems-paper habit to **unlearn**: numbered contribution lists. Plant journals do not expect them and reviewers treat them as grant-style. State the advance in prose.

Note: the "gap paragraph" is where weak papers die. "Little is known about the role of X in Y" is not a gap — it is an admission you did not read the literature. A real gap names the competing possibilities and why they can't be distinguished yet.

### Results (the heart — 60% of your effort)

Structure: **6–8 subsections, one per logical figure step**, ordered by the evidence ladder.

Each subsection follows a fixed four-move shape:

```
Move 1  Rationale   — "To determine whether X is required for Y, we ..."
Move 2  Experiment  — brief methods-in-passage (details go to M&M)
Move 3  Result      — what happened, quantitative, with statistics inline
Move 4  Local       — "Thus, X is required for ..., suggesting ..."
        inference
```

**Rules:**
- Subsection headings must be **claims, not topics**. "The *abc1* mutant has reduced seed set" beats "Phenotypic analysis of *abc1* mutants."
- Past tense for results; present tense for established facts and interpretations.
- Report exact P values where possible (P = 0.003), not just "P < 0.05". Reserve "P < 0.001" for genuinely smaller values.
- State n and the test inline at first use.
- Do not discuss. That is the Discussion's job. A local "thus" inference is fine; comparing to other papers is not.
- Never write "data not shown." Include it or drop the claim.

### Discussion (5–8 paragraphs)

```
P1  The finding    — restate the central advance, then say what it means
P2  Fit            — how this agrees with / extends existing literature
P3  Conflict       — where it disagrees with prior work, and why. Engage
                     honestly; do not omit disconfirming studies.
P4  Mechanism      — the working model, and the evidence for each arrow
P5  Alternatives   — interpretations you ruled out, and how (this is the
                     direct analogue of "discuss alternatives for every choice")
P6  Limitations    — what your system cannot establish. Be specific and
                     unflinching; reviewers penalise hiding more than admitting.
P7  Implications   — applied/agricultural significance and future work
```

Where papers are short, P2–P4 merge. Never drop P5 and P6.

### Materials and Methods

Placement varies: before Results (traditional plant journals), after Discussion (many applied journals), or in supplementary (Nature-family). Match the venue.

**Reproducibility minimum — a reviewer will check each of these:**

- Species, cultivar, ecotype, and seed stock ID (NASC / ABRC / MaizeGDB / stock centre)
- Growth conditions: photoperiod, temperature (day/night), light intensity (µmol m⁻² s⁻¹), humidity, substrate, pot size
- Field: site coordinates, soil classification, sowing/harvest dates, plot size, design (RCBD, split-plot), replicate number, fertilization and irrigation regime, weather data source
- Constructs: vector backbone, promoter, tag position, primers (list in supplement)
- Lines: allele names, background, generation, zygosity, how many independent lines
- Antibodies: supplier, catalogue number, RRID, dilution
- Statistics: software **and version**, test used, model specification, correction method, n definition
- Accession numbers: GEO/SRA/ENA for sequencing, PRIDE for proteomics, MetaboLights for metabolomics, Zenodo/Dryad for code and data

---

## 5. Writing Patterns

### Pattern 1: Gap → Answer Mapping

State gaps G1–Gn in the Introduction; answer each with a figure in Results; verify in Discussion using the same labels.

> *Example pattern:* three open questions in the Introduction ↔ three Results subsections ↔ three Discussion paragraphs.

### Pattern 2: Evidence Escalation

Order Results so each subsection raises the evidence level: association → necessity → sufficiency → mechanism → order. The reader experiences the argument tightening.

### Pattern 3: The Advance Formula

> "We show that **[gene/pathway]** **[acts how]** through **[mechanism]** to **[affect trait]**, and that this **[matters why]**."

This is the biology analogue of the systems "X is better for Y in Z." It should be reconstructible from your abstract alone.

### Pattern 4: Convergence Model

Build the final model figure explicitly from the evidence ladder: solid arrows for steps you demonstrated, dashed arrows for steps inferred from literature or plausible but untested. Reviewers reward this honesty — and an undifferentiated model figure invites "the authors overstate their model" criticism.

### Pattern 5: The Honest Counterexample

If one of your independent lines disagrees (e.g., transcript rises but protein does not), report it and interpret it. Suppressing it is the single most common way a paper becomes unreproducible.

---

## 6. Venue Reference Table

> **Always verify against the current Guide for Authors — limits change yearly.** Figures below were checked in 2026 and are indicative only.

| Venue | Abstract | Main text | Display items | Notes |
| --- | --- | --- | --- | --- |
| **Nature Plants** (Article) | 150 words, unreferenced | 3,000 words | ≤6 | Intro unheaded; separate Methods |
| **The Plant Cell** | 200 words | ~7,000 words incl. abstract | 6–10 | Heavy mechanistic demand |
| **Plant Physiology** (Research Article) | 250 words | ~7,000 words incl. abstract | 6–10 | 30–50 citations; structured abstract |
| **The Plant Journal** | Summary section | 7,000–9,000 words | 3–7 | Word count includes legends & M&M |
| **J Exp Bot** | 200 words | — | — | Highlights section required |
| **New Phytologist** (Full paper) | 200 words, 4 bullet points | 6,500–7,500 words | 6–8 | Discussion ≤30% of text |
| **Field Crops Research** | 400 words, **structured** | — | — | Highlights (3–5 × ≤85 chars) required |
| **Agronomy Journal** | ~250 words | — | — | ASA/CSSA style manual applies |
| **BMC Plant Biology** | 350 words, structured | — | — | Background/Results/Conclusions |
| **Frontiers in Plant Science** | 350 words | 12,000 words *incl. legends* | No cap | Word cap bites harder than it looks |
| **PLoS ONE** | 300 words | No limit | No limit | Rigour over novelty |

**Selection heuristic:** pick the venue *after* you know your highest evidence level. L1–L2 evidence will not survive at Nature Plants or The Plant Cell regardless of writing quality; it may be strong at BMC Plant Biology or PLoS ONE. Mismatch between evidence level and venue is the most avoidable rejection in the field.

---

## 7. Nomenclature, Style, and Units

Reviewers in this field police nomenclature hard. Getting it wrong signals inexperience.

| Organism | Gene (italic) | Protein (roman) | Mutant |
| --- | --- | --- | --- |
| *Arabidopsis thaliana* | `ABC1` (uppercase italic) | ABC1 | `abc1` (lowercase italic) |
| Maize (*Zea mays*) | `abc1` (lowercase italic) | ABC1 | `abc1` |
| Rice (*Oryza sativa*) | `OsABC1` | OsABC1 | `osabc1` |
| Tomato (*Solanum lycopersicum*) | `SlABC1` | SlABC1 | `slabc1` |

- Species names italic; genus abbreviated after first mention (*Arabidopsis thaliana* → *A. thaliana*).
- Statistical symbols italic: *P*, *n*, *r*², *F*, *t*, *χ*².
- Units: µmol m⁻² s⁻¹ (not "µE"), °C, mM, µM, g L⁻¹, kg ha⁻¹, DAS (days after sowing), DAP (days after planting).
- Spell out numbers under 10 unless attached to a unit.
- "Significant" only when a statistical test supports it; otherwise "substantial" or "marked".
- Define each abbreviation at first use; do not abbreviate terms used fewer than four times.

---

## 8. Statistical Reporting Rules

- State the **model**, not just the test: "a linear mixed model with genotype as fixed effect and site-year as random effect."
- Report **effect sizes with confidence intervals**, not P values alone. A P value tells the reader nothing about magnitude.
- **Biological vs technical replicates**: n = 3 biological replicates means three independent plants/preparations. Three wells from one extract is n = 1. Misreporting this is research misconduct territory, not a style issue.
- Correct for multiple comparisons (Benjamini–Hochberg FDR for omics; Tukey/Holm for pairwise). State the method.
- Omics thresholds: justify the cut-off (e.g. padj < 0.05 and |log₂FC| > 1) *a priori*. Do not tune thresholds to get a pleasing gene list; report sensitivity to the threshold.
- Report failed/contrasting experiments. Do not report only the marker that worked.
- Where relevant, do not treat P > 0.05 as proof of no effect — report the CI and discuss power.

---

## 9. Reporting Standards and Data Deposition

| Data type | Standard / repository |
| --- | --- |
| qPCR | MIQE (Bustin et al. 2009; MIQE 2.0, 2025) — reference gene validation mandatory |
| Plant phenotyping / field | MIAPPE 1.1 (Papoutsoglou et al. 2020) |
| RNA-seq / microarray | MINSEQE; GEO or ArrayExpress; SRA/ENA for raw reads |
| Proteomics | MIAPE; PRIDE |
| Metabolomics | MetaboLights / Metabolomics Workbench |
| Sequences | GenBank / ENA; accession in the manuscript |
| Code and processed data | Zenodo or Dryad, with DOI, cited in Data Availability |
| Antibodies, cell lines | RRID |
| Plant material | Stock centre ID (NASC, ABRC, MaizeGDB, etc.) |

Many journals will not send a paper to review without accession numbers. Deposit before submission, not during revision.

---

## 10. Workflow

```
1.  Determine venue → look up current word/abstract/figure limits
2.  Place every intended claim on the Evidence Ladder (§1); drop or re-scope claims you cannot support
3.  Draw the figure sequence (§2); write one sentence per panel
4.  Merge panel sentences into Results subsection headings (claims, not topics)
5.  Reverse-outline: heading list = the paper's argument. Fix logic here, not in prose
6.  Draft Results first (it is the least rhetorical section and anchors everything)
7.  Draft Discussion: finding → fit → conflict → mechanism → alternatives → limits → implications
8.  Draft Introduction backwards from the gap your Results actually fill
9.  Draft Abstract last, sentence by sentence, checking each claim against a figure
10. Draft Materials & Methods against the reproducibility checklist (§4)
11. Assemble figures to spec; write legends using the four-statement rule
12. Deposit data; collect accession numbers and stock IDs
13. Run the self-check (§11) and the verb-ceiling audit
14. Hand off to /paper-write for citation verification and formatting
```

---

## 11. Quick Self-Check

- [ ] Every causal verb is at or below the evidence level supporting it (§1 Rule 1)
- [ ] Every major claim rests on ≥2 independent lines of evidence
- [ ] ≥2 independent alleles for every mutant phenotype claim
- [ ] Figures are ordered as an escalating argument, not as a lab notebook
- [ ] Every conclusion appears four times: hypothesis, result, caption, interpretation
- [ ] Abstract contains no claim unsupported by a figure
- [ ] Discussion explicitly rules out alternative interpretations
- [ ] Limitations stated plainly, in their own paragraph
- [ ] Statistics: model named, effect sizes and CIs reported, n defined (biological vs technical), corrections stated
- [ ] Error bars defined in every legend; n in every legend
- [ ] All accession numbers, stock IDs, and RRIDs present
- [ ] Nomenclature follows species conventions (gene italic / protein roman)
- [ ] No "data not shown"; no fabricated or reused panels
- [ ] Word, abstract, and figure limits within the current Guide for Authors
- [ ] Reporting standard declared where applicable (MIQE, MIAPPE, MINSEQE)

---

## 12. Academic Integrity (non-negotiable)

- **Never fabricate** observations, images, gels, blots, or results. Image manipulation is detectable and career-ending.
- **Never generate citations from memory.** Verify every reference against a database. Hallucinated citations in a biology manuscript are now a recognised signature of LLM drafting and trigger desk rejection at several publishers.
- **Do not overclaim.** The verb ceiling (§1) is an integrity rule, not a style preference.
- **Disclose LLM use** per venue policy.
- **Do not repurpose text** from your own prior publications without clear citation and permission (self-plagiarism is enforced).
- This blueprint provides structural guidance only — it does not generate findings, figures, or text you should submit unread.

---

## 13. Authoritative Sources

1. Mensh & Kording (2017) "Ten simple rules for structuring papers." *PLoS Comput Biol* 13(9):e1005619. doi:10.1371/journal.pcbi.1005619 — context–content–conclusion logic; the basis of §4.
2. Gopen & Swan (1990) "The Science of Scientific Writing." *American Scientist* 78:550–558 — topic position and stress position; essential for Results paragraphs.
3. Schimel, J. (2012) *Writing Science: How to Write Papers That Get Cited and Proposals That Get Funded.* Oxford University Press — story structure for biology specifically.
4. Bustin et al. (2009) "The MIQE guidelines." *Clinical Chemistry* 55(4):611–622. doi:10.1373/clinchem.2008.112797 — and MIQE 2.0 (2025) *Clinical Chemistry* hvaf043.
5. Papoutsoglou et al. (2020) "Enabling reusability of plant phenomic datasets with MIAPPE 1.1." *New Phytologist* 227(1):260–273. doi:10.1111/nph.16544.
6. Weissgerber et al. (2015) "Beyond bar and line graphs: time for a new data presentation paradigm." *PLoS Biol* 13(4):e1002128. doi:10.1371/journal.pbio.1002128.
7. Rougier, Droettboom & Bourne (2014) "Ten simple rules for better figures." *PLoS Comput Biol* 10(9):e1003833. doi:10.1371/journal.pcbi.1003833.
8. Sand-Jensen (2007) "How to write consistently boring scientific literature." *Oikos* 116:723–727 — a useful corrective against padding.
9. ASA / CSSA / SSSA *Publications Handbook and Style Manual* — authoritative for agronomy journals.
10. Current Guide for Authors for your target venue — **outranks every source above on matters of format.**
