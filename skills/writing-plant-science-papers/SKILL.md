---
name: writing-plant-science-papers
description: Paragraph-level structural blueprint for molecular biology, plant science, and agricultural research papers. Covers mechanistic, applied-agronomy, and omics paper types. Provides a mandatory pre-flight questionnaire, a rolling evidence-ladder audit, reverse-engineering from figure plan to experiment list for pre-data projects, section blueprints, statistical and nomenclature rules, and venue-match checking across Nature Plants through Field Crops Research. Use when user says "写植物论文", "写分子生物论文", "plant science manuscript", "molecular biology paper structure", "agronomy paper", "crop science manuscript", or wants structural guidance for a plant/agriculture journal submission.
argument-hint: [venue-or-section]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Writing Plant Science & Agriculture Papers: Paragraph-Level Blueprint

Structural guidance for **$ARGUMENTS**

## Relationship to Other Skills

- **paper-write**: General generation workflow with citation verification. This skill supplies the biology-specific skeleton.
- **paper-plan**: Research outline creation. Use paper-plan for *what* to study; this skill for *how to structure the report of it* and, when no data exist yet, how to work backwards from the target venue.
- **paper-slides**: Conference talk generation. No overlap.

**Boundary**: this skill gives you the pre-flight gate, page budgets, paragraph roles, evidence-calibration rules, and figure logic for molecular-biology / plant-science / agronomy venues. It does not generate LaTeX, verify references, or produce data.

---

## §0. MANDATORY PRE-FLIGHT GATE

**Do not draft any section of any manuscript until every question below has been answered.**

This gate exists because in biology, drafting before the evidence and venue are settled produces text that later figures invalidate. A systems paper's early draft survives; a biology draft written before the last mutant is phenotyped does not. The cost of asking is one turn. The cost of not asking is a rewrite.

### The six questions (ask all of them, every time)

| # | Question | Why it changes the output |
| --- | --- | --- |
| 1 | **Paper type** — molecular/mechanistic · applied agronomy · omics/computational · method/resource? | Selects the figure architecture (§4) and the Results logic |
| 2 | **Target venue** — named journal, or "undecided"? | Sets word/abstract/figure limits (§8). If undecided, run the §8 procedure |
| 3 | **Strongest evidence** — where on the ladder (L0–L7), or if pre-data, the highest level *reachable*? | Sets the verb ceiling (§2) and the venue that is realistic |
| 4 | **Stage** — data in hand · partially collected · planning only? | Planning-only triggers §3 reverse-engineering mode |
| 5 | **Scope** — single claim · full mechanism · discovery + validation · field recommendation? | Calibrates how much of the blueprint to activate (§12) |
| 6 | **Constraints** — time, budget, field-site access, available genotypes, equipment? | Determines which panels are feasible; infeasible panels force a claim downgrade |

### Routing: what each answer activates

| Answer | Activates |
| --- | --- |
| molecular | §4 architecture A, §5 budget A |
| applied agronomy | §4 architecture B, §5 budget B, §10 agronomic significance ladder |
| omics | §4 architecture C, §5 budget C |
| planning only | §3 reverse-engineering mode — run *before* anything else |
| high-impact venue + evidence ≤ L2 | **Stop.** Report the mismatch. Change venue or add evidence |
| scoped to one claim | Use §7 Pattern 2 (Evidence Escalation) with 3–4 figures only |

### Re-check triggers — the gate is not one-time

Re-run the relevant part of the questionnaire whenever any of these occur:

- An experiment completes and changes the strongest evidence level
- A claim is downgraded because a control failed
- The target venue changes
- The topic moves (a competing paper publishes, a collaboration adds a system)
- Before final submission

**If the answer to Q3 changes, the permitted verbs in the abstract change. Re-audit them.**

---

## §1. The Core Translation (systems → biology)

Both fields write "problem → insight → evidence → conclusion." Everything else differs.

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
| "Discuss alternatives for every design choice" | "Rule out alternative interpretations for every claim" |
| Contribution list (numbered) | Advance statements — prose, not numbered |
| Separate Related Work section | **Discussion**, where prior work is integrated claim-by-claim |
| Reproducibility checklist | Reporting standards + data deposition + accession numbers |

**The decisive consequence:** a systems paper's currency is *architectural novelty*. A biology paper's currency is **evidence strength for a causal claim**. Reviewers will not accept an argument because it is elegant — only because the evidence supports it.

---

## §2. The Evidence Ladder and the Rolling Audit

### The ladder

| Level | Evidence type | Typical experiments | Permitted verbs |
| --- | --- | --- | --- |
| **L0** | Association | Expression correlation, co-expression network, GWAS signal, QTL interval, transcriptome comparison | "is associated with", "correlates with", "co-varies with" |
| **L1** | Necessity | T-DNA / CRISPR / RNAi knockdown, null mutant phenotype | "is required for", "loss of X reduced/impaired" |
| **L2** | Sufficiency | Overexpression, ectopic or inducible expression, heterologous expression | "is sufficient to", "ectopic expression restored" |
| **L3** | Specificity | Complementation with WT vs. mutant construct, ≥2 independent alleles, domain swap, catalytically dead variant | "acts through", "depends on the ... domain" |
| **L4** | Physical mechanism | Y2H, BiFC, split-luc, Co-IP, pull-down, in vitro reconstitution, enzymatic assay, structure | "physically interacts with", "directly promotes" |
| **L5** | Order of action | Epistasis / double mutant, tissue-specific rescue, temporal induction | "acts upstream/downstream of" |
| **L6** | Conservation | Ortholog functional test, natural variation, multi-species comparison | "is conserved in" |
| **L7** | Applied impact | Multi-year field trial, yield, stress tolerance under agronomic conditions | "improved ... in the field" |

### Rule 1: The verb ceiling

**Your strongest verb must not exceed your evidence level.** This is the single most common rejection cause in the field. With only expression data and a mutant phenotype you have L0–L1: write "is required for," never "regulates" as settled fact, never "controls."

### Rule 2: One claim, multiple independent lines

A claim with one line of evidence is an **observation**. A claim with independent lines (genetics + biochemistry + expression) is a **conclusion**. Aim for ≥2 independent lines per major claim. Where claims share one method, flag the shared dependency in the Discussion — reviewers will find it.

### Rule 3: Must-have controls

| Claim type | Controls reviewers demand |
| --- | --- |
| Gene expression (qPCR) | ≥2 (ideally 3) reference genes validated for your tissue/treatment, per MIQE |
| Mutant phenotype | ≥2 independent alleles; segregation analysis; background homozygosity |
| Complementation / rescue | WT construct rescues, mutant construct does not; matched promoter context |
| Protein interaction | Reciprocal test (bait/prey swap), negative control, expression verification |
| Overexpression | Empty-vector control line; expression level verified |
| Treatment effect | Untreated control, mock, time-matched sampling |
| Field trial | Randomised design, blocking, ≥2 site-years, weather + soil characterisation |

### The rolling audit — evidence is a variable, not an input

**Do not fix an evidence level at the start of a project and treat it as permanent.** Evidence accumulates and the level moves — usually upward, occasionally downward when a control fails. The blueprint must be re-scored as the topic progresses.

**Scoring table — maintain this, revise it after every experiment:**

| Claim you intend to make | Current level | Experiment that raised it | Next experiment that would raise it | Blocking constraint |
| --- | --- | --- | --- | --- |
| [ ] | L[ ] | [ ] | [ ] | [ ] |
| [ ] | L[ ] | [ ] | [ ] | [ ] |
| [ ] | L[ ] | [ ] | [ ] | [ ] |

**Audit outputs, recomputed each time:**

1. **The verb ceiling** — your strongest permitted verb per claim
2. **The realistic venue** — from the §8 match table
3. **The open gap** — which claim is the weakest link, and what would close it

> A paper should not be drafted around the evidence you *hope* to have. Draft around the level you *have*, and revise upward when the audit moves. Writing at the hoped-for level is how overclaiming happens, and overclaiming is what gets papers rejected after review rather than before it.

**Level movement is normal, in both directions.** A complementation experiment that fails to rescue drops a claim from L3 to L1. Record the drop, revise the verbs, and re-check the venue — do not quietly keep the stronger language.

---

## §3. Planning-Stage Mode: Reverse-Engineering from the Target

**Run this when Q4 (stage) = planning only, or when the evidence audit shows the venue and the ladder are mismatched.**

You cannot choose a claim and a venue independently. The loop below iterates until they agree. Most projects need two or three passes.

```
Step 1  Write the claim you want to be able to make, using the Advance Formula:
        "We show that [X] [acts how] through [mechanism] to [trait], and that this [matters why]."

Step 2  Name the target venue family (§8).

Step 3  Look up the evidence level that venue's reviewers require (§8 match table).

Step 4  Work BACKWARDS from that level. List the figure panels such a paper needs
        (§4 architecture for your paper type).

Step 5  Convert each panel into an experiment, specified per the template below.

Step 6  Identify the critical path: which experiments are prerequisites for others,
        and which are on the longest chain to a submittable paper.

Step 7  FEASIBILITY CHECK. Any panel you cannot produce (no field site, no antibody,
        no ortholog line, no instrument time) downgrades the claim.

Step 8  If any panel is infeasible: revise the claim in Step 1 and return to Step 3.
        Repeat until claim, evidence plan, and venue agree.
```

### Experiment specification template

Complete one row per planned panel. The statistics column is not optional — if you cannot name the test before running the experiment, you cannot design the experiment.

| Panel | Question it answers | Design | n (biological) | Controls | Statistical test / model | Feasibility | Critical path? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | high/med/low | Y/N |
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

### The three planning outputs

1. **Planned figure sequence** — the architecture from §4, populated with your real system
2. **Experiment list** — the table above, sorted by critical path
3. **Rolling audit baseline** — the §2 scoring table with all levels currently at their honest starting values

> **Planning-stage discipline:** resist aiming a low-evidence project at a high-evidence venue and hoping. The gap between them is a list of experiments, and it is better discovered now than at review. Working backwards converts an ambition into a work plan.

---

## §4. The Figure Story

**Rule: draw the figures first.** A biology paper is a sequence of figures walking a reader from observation to mechanism. If you cannot sketch the sequence, you do not yet know what the paper argues.

**Reverse outline method** — write one sentence per planned panel:
> "Fig 3B shows that *x* mutant siliques are shorter than WT (n = 30, P < 0.001)."

These become the Results headings, the legend first sentences, and the Discussion topic sentences. Duplicates mean the panels should merge.

### Architecture A — Molecular / mechanistic (6–8 figures)

| # | Logical step | Content | Establishes | Level |
| --- | --- | --- | --- | --- |
| 1 | Context | Phenotype or phenomenon; system schematic | That the question matters | — |
| 2 | Discovery | Mutant screen, QTL, DEG list, GWAS hit, phylogeny | How the candidate was found | L0 |
| 3 | Pattern | Spatiotemporal expression, promoter–GUS, in situ, localisation | Where and when it acts | L0 |
| 4 | Necessity | Loss-of-function phenotype, ≥2 alleles | Required | L1 |
| 5 | Sufficiency | Overexpression, ectopic, inducible | Sufficient | L2 |
| 6 | Mechanism | Y2H/BiFC/Co-IP, activity, in vitro reconstitution | How it works | L4 |
| 7 | Order / specificity | Epistasis, double mutant, variant-construct rescue | Where in the pathway | L3–L5 |
| 8 | Model | Schematic: solid arrows demonstrated, dashed inferred | Integrated claim | — |
| 9* | Applied relevance | Field or agronomic performance; crop ortholog | That it matters | L6–L7 |

*Optional but increasingly expected in crop-species papers; substantially raises perceived impact.

### Architecture B — Applied / agronomy (tables are first-class)

| Item | Content | Notes |
| --- | --- | --- |
| Table 1 | Site and soil characterisation; weather per season | Reviewers check this first |
| Table 2 | ANOVA / mixed-model output: sources of variation, df, F or χ², P, variance components | Report the model, not just the result |
| Fig 1 | Treatment/genotype effect on the primary trait | Across seasons and sites; show individual points |
| Fig 2 | G×E: AMMI / GGE biplot or stability parameters | Essential for multi-environment trials |
| Fig 3 | Relationship, dose–response, regression with fitted model and CI band | Practical response curve |
| Table 3 | Economic analysis: gross margin, partial budget, water/fertiliser use efficiency | What makes it agronomy rather than agronomic botany |
| Fig 4* | Conceptual diagram of the recommendation | Raises citation rate for extension-facing work |

### Architecture C — Omics / computational (6–8 items)

| # | Logical step | Content | Establishes |
| --- | --- | --- | --- |
| 1 | System | Study design, sample collection, analysis workflow schematic | Scope and rigour |
| 2 | Landscape | PCA / clustering / sample relationships | Data quality, batch structure |
| 3 | Discovery | DEGs, QTL interval, Manhattan plot, module–trait correlation | What was found | 
| 4 | Structure | Co-expression network, enrichment, pathway topology | How findings relate |
| 5 | Signature | Prioritised candidate gene, module, or hub — with the prioritisation logic shown | Why *this* candidate |
| 6 | **Validation** | Independent cohort, tissue, species, or season | **The critical panel** |
| 7 | Functional link | Transient assay, mutant, heterologous test (if available) | Causation, not correlation |
| 8 | Model | Integrated schematic | Synthesis |

> Omics papers fail for one reason above all others: discovery without independent validation. Panel 6 is not optional — a candidate list from one dataset is a hypothesis, not a result.

### The four-statement rule

Every conclusion appears **four times**, in four registers:

1. **Hypothesis** — closing sentence of the Introduction, or the rationale opening a Results subsection
2. **Result** — the concluding sentence of that Results subsection
3. **Caption** — first sentence of the figure legend, standalone and quantitative
4. **Interpretation** — topic sentence of the corresponding Discussion paragraph

A finding stated once, mid-paragraph, is missed by the reviewer skimming your PDF.

### Figure QA

- Define every error bar in the legend: SD, SE, or 95% CI. Mandatory.
- State n in every legend and whether it is biological or technical. **Technical replicates are not replicates for inference.**
- Show individual points for small n rather than bar-and-whisker.
- Micrographs: scale bar per panel; identical exposure and processing within a comparison.
- **Image integrity**: no undemarcated splicing, no selective regional adjustment, no duplicated or reused panels. Automated forensics are now standard and this ends careers.

*(Panel-level craft, legend templates, and the section↔figure mapping table are in `references/figure-table-plan.md`.)*

---

## §5. Word / Page Allocation

### Budget A — Molecular paper (7,000–9,000 word venues)

| Section | Words | Notes |
| --- | --- | --- |
| Title | 10–20 | No abbreviations; state the finding |
| Abstract | 200–250 | Unstructured at most plant journals |
| Introduction | 700–1,000 | 5–7 paragraphs |
| Results | 2,000–3,000 | 6–8 subsections, one per figure step |
| Discussion | 1,200–1,800 | 5–8 paragraphs; ≤30% of total at some venues |
| Materials & Methods | 1,500–2,500 | Often supplementary |
| Conclusions | 0–400 | Optional; forbidden at some venues |
| References | — | 40–70 typical |

### Budget B — Applied / agronomy paper

| Section | Words | Notes |
| --- | --- | --- |
| Abstract | 250–400 | Usually **structured** |
| Highlights | 3–5 bullets | ≤85 characters each, including spaces |
| Introduction | 500–800 | Ends with an explicit objective statement |
| Materials & Methods | 1,000–1,500 | Field design, statistics, site characterisation |
| Results | 1,200–1,800 | Often combined as "Results and Discussion" |
| Discussion | 1,200–2,000 | Must address agronomic + economic significance |
| Conclusions | 300–500 | Practical recommendation + limits |
| References | — | 50–80 typical |

**The three-level significance obligation** — no systems-paper analogue. Every effect reported at three levels:

1. **Statistical** — is it real? (P, CI, model diagnostics)
2. **Agronomic** — is it large enough to matter? (a significant 2% yield gain may be noise to a grower)
3. **Economic / practical** — does it pay, and under what conditions? (gross margin, break-even)

Papers stopping at level 1 are routinely rejected as incremental.

### Budget C — Omics / computational paper

| Section | Words | Notes |
| --- | --- | --- |
| Abstract | 200–350 | Structured at BMC-style venues |
| Introduction | 600–900 | Ends with the analysis question, not just the biological one |
| Results | 2,500–4,000 | Discovery → structure → validation → functional link |
| Discussion | 1,000–1,500 | Must separate what is validated from what is hypothesised |
| Methods | 1,500–3,000 | Reproducibility-critical: versions, thresholds, parameters |
| Data availability | — | Accession numbers mandatory pre-submission |

**Omics-specific rule:** state *a priori* thresholds (padj, log₂FC, allele frequency) and report sensitivity to them. Thresholds tuned to produce a pleasing gene list are detectable and disqualifying.

---

## §6. Section Blueprints

### Title

- **Mechanistic**: `[Gene/Protein] [verb] [process] to [outcome] in [species]`
- **Applied**: `[Practice/genotype] [effect] on [trait] under [conditions]`
- **Omics**: `[Approach] reveals [signature/candidate] for [trait] in [system]`

Avoid puns, "Novel...", "Study of...", question form, and topic-only titles.

### Abstract (4–6 sentences)

```
S1  Background — what is known and why this trait matters
S2  Gap — what remains unresolved
S3  Approach — species, system, method
S4  Key result — quantitative, with direction and magnitude
S5  Mechanism / interpretation
S6  Implication — applied or broader significance
```

No citations. No abbreviations undefined. No figure references. **Every claim traceable to a panel.** Editors specifically check for abstract-to-evidence mismatch, and it is a leading cause of post-review rejection.

### Introduction (5–7 paragraphs)

```
P1      Territory     — the process/trait and its stakes. Concrete, not rhetorical.
P2–P3   Knowledge     — what is established. Primary literature, not reviews.
P4      Gap           — the unresolved question, falsifiable and specific.
P5      Rationale     — why this species, system, approach.
P6      Advance       — what you show and what it means.
```

**Unlearn the numbered contribution list** — plant journals read these as grant-style; the advance goes in prose.

The gap paragraph is where weak papers die. "Little is known about the role of X in Y" is not a gap, it is an admission you did not read the literature. A real gap names the competing possibilities and why they cannot yet be distinguished.

### Results (60% of your effort)

6–8 subsections, one per figure step, ordered by the ladder so the argument tightens.

Each subsection: **Rationale → Experiment → Result → Local inference**

```
"To determine whether X is required for Y, we ... (rationale)
 ... assays were performed as described ... (experiment)
 ... mutant siliques contained 40% fewer seeds than WT (n = 30, P < 0.001) ... (result)
 Thus, X is required for seed set, suggesting ... (inference)"
```

Rules:
- Headings must be **claims, not topics**: "The *abc1* mutant has reduced seed set," not "Phenotypic analysis."
- Past tense for results; present for established facts and interpretations.
- Exact P values where possible (P = 0.003), not just "P < 0.05."
- n and test stated inline at first use, per audit.
- No discussion of other papers here. A local "thus" is fine; comparison is not.
- No "data not shown."
- **Verbs here must obey the audit ceiling — re-check after every experiment.**

### Discussion (5–8 paragraphs)

```
P1  Finding       — restate the advance, then interpret it
P2  Fit           — how this agrees with and extends prior work
P3  Conflict      — where it disagrees, and why. Engage disconfirming studies
P4  Mechanism     — the working model, arrow by arrow
P5  Alternatives  — interpretations ruled out and how (the direct analogue of
                    "discuss alternatives for every choice")
P6  Limitations   — what this system cannot establish. Specific and unflinching
P7  Implications  — applied/agricultural significance and future work
```

Short papers merge P2–P4. **Never drop P5 or P6.**

### Materials and Methods

Reproducibility minimum — a reviewer will check each:

- Species, cultivar/ecotype, seed stock ID (NASC / ABRC / MaizeGDB)
- Growth conditions: photoperiod, day/night temperature, light intensity (µmol m⁻² s⁻¹), humidity, substrate, pot size
- Field: coordinates, soil classification, sowing/harvest dates, plot size, design, replicates, fertilisation and irrigation, weather data source
- Constructs: backbone, promoter, tag position; primers in supplement
- Lines: allele names, background, generation, zygosity, number of independent lines
- Antibodies: supplier, catalogue number, RRID, dilution
- Statistics: **software and version**, model, test, correction, definition of n
- Accessions: GEO/SRA/ENA, PRIDE, MetaboLights, Zenodo/Dryad

---

## §7. Writing Patterns

**Pattern 1 — Gap → Answer Mapping.** Gaps G1–Gn in the Introduction, answered by figure in Results, verified in Discussion with the same labels.

**Pattern 2 — Evidence Escalation.** Order Results so each subsection raises the level: association → necessity → sufficiency → mechanism → order. The reader feels the argument tighten. Use this when scope is a single claim and you have 3–4 figures.

**Pattern 3 — The Advance Formula.**
> "We show that **[gene/pathway]** **[acts how]** through **[mechanism]** to **[affect trait]**, and that this **[matters why]**."

The biology analogue of the systems "X is better for Y in Z." Reconstructible from the abstract alone.

**Pattern 4 — Convergence Model.** Build the final model figure from the audit: solid arrows for demonstrated steps, dashed for inferred. Reviewers reward the honesty, and an undifferentiated model invites "the authors overstate their model."

**Pattern 5 — The Honest Counterexample.** If an independent line disagrees (transcript rises, protein does not), report and interpret it. Suppression is the most common route to an irreproducible paper.

---

## §8. Venue Selection: Procedure and Match Checker

### Procedure

```
1. Score the evidence audit (§2). You need the level, not the ambition.
2. If stage = planning, run §3 first — the venue may be an output, not an input.
3. Look up the required level in the match table below.
4. If your level >= required: proceed with that venue family.
   If your level < required: choose — add evidence (§3), or move down a tier.
   NEVER submit at a level below the requirement and hope the writing carries it.
5. Confirm the current limits in the venue's Guide for Authors — they change yearly
   and the Guide outranks this table.
6. Re-check at submission. The audit moves; the venue may need to.
```

### Venue ↔ evidence match table

| Venue family | Minimum level | Required panels | Realistic for |
| --- | --- | --- | --- |
| Nature Plants · The Plant Cell · Molecular Plant | L4+ with L1–L5 convergence | 7–8: mechanism + order + specificity (+ field or conservation) | Multi-line, multi-system mechanism |
| New Phytologist · Plant Physiology · TPJ · JXB · Plant Cell & Environment | L3–L4 | 6–7: necessity + sufficiency + specificity | Solid single-gene mechanism |
| BMC Plant Biology · PLoS ONE · Frontiers in Plant Science · Scientific Reports | L1–L2 | 5–6: phenotype + necessity + expression | Complete but narrower studies |
| Field Crops Research · Agronomy Journal · Crop Science · European Journal of Agronomy | L7, multi-site-year | Tables 1–3 + field figures | Field data with economic analysis |
| Bioinformatics / computational journals | L0 + independent validation | 6–8 incl. validation panel | Omics with a validation cohort |

> **Mismatch is the most avoidable rejection in the field.** A well-executed L1 study submitted to The Plant Cell is rejected for evidence, not for writing. The same study at BMC Plant Biology is competitive. Choose the tier your evidence supports, then write the best possible paper at that tier.

### Venue reference table

> Indicative values checked in 2026. **Always verify against the current Guide for Authors.**

| Venue | Abstract | Main text | Display items | Notes |
| --- | --- | --- | --- | --- |
| Nature Plants (Article) | 150 words, unreferenced | 3,000 words | ≤6 | Intro unheaded; separate Methods |
| The Plant Cell | 200 words | ~7,000 incl. abstract | 6–10 | Heavy mechanistic demand |
| Plant Physiology | 250 words | ~7,000 incl. abstract | 6–10 | 30–50 citations |
| The Plant Journal | Summary section | 7,000–9,000 | 3–7 | Count includes legends & M&M |
| J Exp Bot | 200 words | — | — | Highlights required |
| New Phytologist (Full paper) | 200 words, 4 bullets | 6,500–7,500 | 6–8 | Discussion ≤30% of text |
| Field Crops Research | 400 words, structured | — | — | Highlights 3–5 × ≤85 chars |
| Agronomy Journal | ~250 words | — | — | ASA/CSSA style manual |
| BMC Plant Biology | 350 words, structured | — | — | Background/Results/Conclusions |
| Frontiers in Plant Science | 350 words | 12,000 incl. legends | No cap | Cap bites harder than it looks |
| PLoS ONE | 300 words | No limit | No limit | Rigour over novelty |

---

## §9. Nomenclature, Style, Units

Reviewers police nomenclature hard. Errors signal inexperience.

| Organism | Gene (italic) | Protein (roman) | Mutant |
| --- | --- | --- | --- |
| *Arabidopsis thaliana* | `ABC1` uppercase italic | ABC1 | `abc1` lowercase italic |
| Maize (*Zea mays*) | `abc1` lowercase italic | ABC1 | `abc1` |
| Rice (*Oryza sativa*) | `OsABC1` | OsABC1 | `osabc1` |
| Tomato (*Solanum lycopersicum*) | `SlABC1` | SlABC1 | `slabc1` |

- Species names italic; genus abbreviated after first mention.
- Statistical symbols italic: *P*, *n*, *r*², *F*, *t*, *χ*².
- Units: µmol m⁻² s⁻¹ (not µE), °C, mM, µM, g L⁻¹, kg ha⁻¹, DAS, DAP.
- "Significant" only with a statistical test; otherwise "substantial" or "marked."
- Define abbreviations at first use; never abbreviate terms used fewer than four times.

---

## §10. Statistical Reporting

- State the **model**, not just the test: "a linear mixed model with genotype as fixed effect and site-year as random effect."
- Report **effect sizes with confidence intervals**, not P values alone.
- **Biological vs technical replicates** — three wells from one extract is n = 1. Misreporting is misconduct, not style.
- Correct for multiple comparisons (Benjamini–Hochberg for omics; Tukey/Holm for pairwise). State the method.
- Omics thresholds justified *a priori*; sensitivity to threshold reported.
- Report failed and contrasting experiments.
- P > 0.05 is not proof of no effect — report the CI and discuss power.

---

## §11. Reporting Standards and Data Deposition

| Data type | Standard / repository |
| --- | --- |
| qPCR | MIQE (Bustin 2009; MIQE 2.0, 2025) — reference gene validation mandatory |
| Plant phenotyping / field | MIAPPE 1.1 (Papoutsoglou 2020) |
| RNA-seq / microarray | MINSEQE; GEO or ArrayExpress; SRA/ENA for raw reads |
| Proteomics | MIAPE; PRIDE |
| Metabolomics | MetaboLights / Metabolomics Workbench |
| Sequences | GenBank / ENA; accession in manuscript |
| Code and processed data | Zenodo / Dryad with DOI |
| Antibodies, cell lines | RRID |
| Plant material | Stock centre ID |

Many journals will not send a paper to review without accession numbers. **Deposit before submission, not during revision.** Detail: `references/reporting-checklists.md`.

---

## §12. Scope Calibration

Use this to size the paper to the topic and avoid activating the whole blueprint when the work does not need it.

| Scope | Figures | Sections to activate | Sections to skip |
| --- | --- | --- | --- |
| **Single claim** (one gene, one phenotype, one mechanism) | 3–4 | §4 arch A panels 1, 4, 6, 8; Patterns 2 & 3 | Pattern 1; omics budget; economic analysis |
| **Full mechanism** (gene → pathway → trait) | 6–8 | Everything in arch A; Patterns 1, 3, 4 | Agronomic significance ladder |
| **Discovery + validation** (omics-led) | 6–8 | Arch C; omics budget; omics thresholds rule | Molecular mechanism panels unless data exist |
| **Field recommendation** (practice or genotype × environment) | 3–5 items | Arch B; Budget B; three-level significance | Molecular figure panels entirely |
| **Method / resource** | 4–6 | Arch A panels 1–2 + validation; Methods expanded | Pattern 1; mechanism panels |

**Calibration principles:**

- The *evidence ladder* applies to every scope. The *figure architecture* does not — pick the one matching Q1.
- Never activate a reporting checklist you cannot satisfy. If no field work was done, MIAPPE does not apply; if no qPCR, MIQE does not.
- A single-claim paper is not a lesser paper. It is a shorter one; it must still obey the verb ceiling and the alternatives paragraph.
- If the scope is unclear, it is usually unclear because the claim is unclear. Return to §3 Step 1.

---

## §13. Workflow

```
0.  RUN THE PRE-FLIGHT GATE (§0). Six questions. Do not skip. Do not draft first.
1.  If planning-stage: run §3 reverse-engineering before anything else.
2.  Build or revise the evidence audit (§2). Score every intended claim.
3.  Select the venue family (§8) and confirm current limits in its Guide for Authors.
4.  Calibrate scope (§12) — decide which sections apply.
5.  Draw the figure sequence (§4); write one sentence per panel.
6.  Merge panel sentences into Results headings (claims, not topics).
7.  Reverse-outline: heading list = the argument. Fix logic here, not in prose.
8.  Draft Results first — least rhetorical, anchors everything.
9.  Draft Discussion: finding → fit → conflict → mechanism → alternatives → limits → implications.
10. Draft Introduction backwards from the gap the Results actually fill.
11. Draft Abstract last, checking each claim against a figure and against the verb ceiling.
12. Draft Methods against the reproducibility checklist (§6).
13. Assemble figures; write legends with the four-statement rule.
14. Deposit data; collect accessions and stock IDs.
15. Re-run the audit. If levels moved, revise the verbs and re-confirm the venue.
16. Run the self-check (§14) and the verb-ceiling audit.
17. Hand off to /paper-write for citation verification and formatting.
```

---

## §14. Quick Self-Check

**Before writing**
- [ ] Pre-flight gate answered — all six questions (§0)
- [ ] Evidence audit scored for every intended claim (§2)
- [ ] Venue confirmed against the match table, not against ambition (§8)
- [ ] Scope calibrated (§12)

**During writing**
- [ ] Every causal verb at or below its supported level
- [ ] Every major claim on ≥2 independent lines of evidence
- [ ] ≥2 independent alleles for every mutant phenotype claim
- [ ] Figures ordered as an escalating argument, not a lab notebook
- [ ] Every conclusion in four registers: hypothesis, result, caption, interpretation
- [ ] Abstract contains no claim unsupported by a figure
- [ ] Discussion rules out alternative interpretations (P5) and states limitations (P6)
- [ ] Omics: validation panel present (§4 arch C panel 6)
- [ ] Applied: statistical, agronomic, and economic significance all addressed

**Before submission**
- [ ] Statistics: model named, effect sizes and CIs reported, n defined (biological vs technical), corrections stated
- [ ] Error bars defined and n stated in every legend
- [ ] Accessions, stock IDs, RRIDs present
- [ ] Nomenclature follows species conventions
- [ ] No "data not shown"; no fabricated, reused, or manipulated panels
- [ ] Word, abstract, and figure limits within the current Guide for Authors
- [ ] Reporting standard declared where applicable (MIQE, MIAPPE, MINSEQE)
- [ ] Audit re-run after the final experiment; verbs match the final levels

---

## §15. Academic Integrity (non-negotiable)

- **Never fabricate** observations, images, gels, blots, or results. Image manipulation is detectable and career-ending.
- **Never generate citations from memory.** Verify every reference against a database. Hallucinated citations are a recognised signature of LLM drafting and trigger desk rejection at several publishers.
- **Do not overclaim.** The verb ceiling is an integrity rule, not a style preference.
- **Record evidence-level drops.** If a control fails, revise the verbs — do not quietly retain stronger language.
- **Disclose LLM use** per venue policy.
- **Do not recycle** text from your own prior publications without citation (self-plagiarism is enforced).
- This blueprint provides structural guidance only — it does not generate findings, figures, or submittable text.

---

## §16. Authoritative Sources

1. Mensh & Kording (2017) "Ten simple rules for structuring papers." *PLoS Comput Biol* 13(9):e1005619. doi:10.1371/journal.pcbi.1005619 — context–content–conclusion logic; basis of §6.
2. Gopen & Swan (1990) "The Science of Scientific Writing." *American Scientist* 78:550–558 — topic and stress positions; essential for Results paragraphs.
3. Schimel (2012) *Writing Science.* Oxford University Press — story structure for biology.
4. Bustin et al. (2009) "The MIQE guidelines." *Clinical Chemistry* 55(4):611–622. doi:10.1373/clinchem.2008.112797; MIQE 2.0 (2025) *Clinical Chemistry* hvaf043.
5. Papoutsoglou et al. (2020) "Enabling reusability of plant phenomic datasets with MIAPPE 1.1." *New Phytologist* 227(1):260–273. doi:10.1111/nph.16544.
6. Weissgerber et al. (2015) "Beyond bar and line graphs." *PLoS Biol* 13(4):e1002128. doi:10.1371/journal.pbio.1002128.
7. Rougier, Droettboom & Bourne (2014) "Ten simple rules for better figures." *PLoS Comput Biol* 10(9):e1003833. doi:10.1371/journal.pcbi.1003833.
8. Sand-Jensen (2007) "How to write consistently boring scientific literature." *Oikos* 116:723–727.
9. ASA / CSSA / SSSA *Publications Handbook and Style Manual* — authoritative for agronomy journals.
10. The current Guide for Authors for your target venue — **outranks every source above on matters of format.**

---

## Companion Files

| File | Use |
| --- | --- |
| `references/quick-reference.md` | One-page condensed card for daily use |
| `references/manuscript-scaffold.md` | Fillable section-by-section scaffold |
| `references/figure-table-plan.md` | Figure architecture, panel craft, section↔figure mapping |
| `references/reporting-checklists.md` | MIQE, MIAPPE, MINSEQE, statistics, venue-match gate |
