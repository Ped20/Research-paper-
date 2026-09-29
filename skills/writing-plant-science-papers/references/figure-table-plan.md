# Figure & Table Plan — The Part That Decides Acceptance

Display items are not illustration. They **are** the argument; the prose is commentary on them. Several editors and experienced reviewers will read your figures before reading a word of your text, and some will decide on the figures alone.

Companion files: `SKILL.md`, `manuscript-scaffold.md`, `reporting-checklists.md`.

---

## 0. Reverse-Engineering from the Target (planning-stage mode)

**Use this when no data exist yet, or when the venue and the evidence are mismatched.** Normal practice is to do science and then find a journal; this inverts it, and it is the faster path when the target is known.

```
Step 1  Write the claim you want to make:
        "We show that [X] [acts how] through [mechanism] to [trait],
         and that this [matters why]."

Step 2  Name the venue family (SKILL.md §8).

Step 3  Look up the evidence level that venue's reviewers require.

Step 4  Work BACKWARDS. List the panels such a paper needs —
        use the architecture below matching your paper type.

Step 5  Convert each panel into an experiment: design, n, controls, test.

Step 6  Identify the critical path — which experiments gate others.

Step 7  FEASIBILITY CHECK. Any panel you cannot produce (no field site, no
        antibody, no ortholog line, no instrument time) downgrades the claim.

Step 8  Revise the claim in Step 1 and return to Step 3.
        Repeat until claim, evidence plan, and venue agree.
```

**Worked example.** Target: a specialised molecular journal (requires L3–L4). Claim: "*ABC1* promotes seed set through interaction with *XYZ*."

| Backward step | Output |
| --- | --- |
| Required level | L3–L4 |
| Required panels | necessity · sufficiency · specificity · interaction (4–5 figures) |
| Experiments implied | 2 CRISPR alleles + phenotyping; overexpression line; variant-construct rescue; Y2H + Co-IP with expression verification |
| Critical path | Alleles → phenotyping → rescue; interaction assays can run in parallel |
| Feasibility | No Co-IP antibody available → interaction weakens to split-luc + Y2H only → claim drops toward L2–L3 |
| Claim revision | "*ABC1* is required for seed set" — and venue moves down one tier, or an antibody is sourced |

> The exercise is worth doing even when it changes nothing. It converts "we should probably also do X" into a dated, costed work plan — or into an early decision to change venue.

### Feasibility → claim revision table

Fill this in and keep it. It is the artefact that prevents a project from drifting toward a venue it cannot reach.

| Required panel | Feasible? | If not, claim downgrades to | Resulting venue tier |
| --- | --- | --- | --- |
| [ ] | Y / N | L[ ] | [ ] |
| [ ] | Y / N | L[ ] | [ ] |
| [ ] | Y / N | L[ ] | [ ] |

---

## 1. The Figure-First Rule

**Never write prose before the figure sequence exists.** Work in this order:

1. Write one sentence per planned panel, present tense, quantitative.
2. Sort the sentences into a logical chain.
3. Merge or cut until the chain is 6–8 items for a molecular paper.
4. Turn each item into a Results subsection heading (a claim, not a topic).
5. Only then write prose.

Worked example of the transformation:

| Panel sentence | Becomes heading |
| --- | --- |
| "*abc1* mutants have 40% fewer seeds per silique than WT (n = 30 plants, P < 0.001)." | "Loss of *ABC1* reduces seed set" |
| "ABC1-GFP signal is nuclear in the embryo sac (n = 12 ovules)." | "ABC1 localises to the nucleus in the embryo sac" |
| "abc1-1 was not rescued by a catalytically dead ABC1 variant, while WT ABC1 fully restored seed set." | "Rescue requires ABC1 catalytic activity" |

If two panel sentences say the same thing, merge the panels. If a panel sentence supports nothing else, cut the panel — every panel must earn its place in the chain.

---

## 2. Molecular / Mechanistic Paper — Standard Architecture

| # | Logical step | Content | What it must establish | Evidence level |
| --- | --- | --- | --- | --- |
| 1 | Context | The phenotype or phenomenon; a schematic of the system | That the question matters | — |
| 2 | Discovery | Mutant screen, QTL interval, DEG list, GWAS hit, phylogeny | How the candidate was identified | L0 |
| 3 | Pattern | Spatiotemporal expression, promoter–GUS, in situ, tissue localisation | Where and when the gene acts | L0 |
| 4 | Necessity | Loss-of-function phenotype, ≥2 independent alleles | The gene is required (L1) | L1 |
| 5 | Sufficiency | Overexpression, ectopic, inducible expression | The gene is sufficient (L2) | L2 |
| 6 | Mechanism | Y2H/BiFC/Co-IP, enzymatic activity, in vitro reconstitution | How it works (L4) | L4 |
| 7 | Order / specificity | Epistasis, double mutant, complementation with variant constructs, domain deletion | Where it sits in the pathway (L3, L5) | L3–L5 |
| 8 | Model | Schematic: solid arrows = demonstrated, dashed = inferred | The integrated claim | — |

**Optional Fig 9 — applied relevance.** Field or agronomic performance of the genotype. Increasingly expected in crop-species papers, and it substantially raises perceived impact. If your system is a model species, this is where a heterologous expression or a crop ortholog test goes.

**Do not** put the model figure first, and do not bury it in the Discussion. It belongs at the end of the Results or the start of the Discussion, where the reader has just accumulated every arrow it contains.

---

## 3. Applied / Agronomy Paper — Standard Architecture

Tables are first-class citizens here. Unlike systems papers, a well-built table reporting the ANOVA is often more persuasive than any figure.

| Item | Content | Notes |
| --- | --- | --- |
| **Table 1** | Site and soil characterisation; weather during each season | Per site-year. Reviewers check this before anything else |
| **Table 2** | ANOVA / mixed-model output: sources of variation, df, F or χ², P, variance components | Report the model, not just the result |
| **Fig 1** | Treatment or genotype effect on the primary trait | Across seasons and sites; show individual points |
| **Fig 2** | G×E interaction: AMMI or GGE biplot, or stability parameters | Essential for multi-environment trials |
| **Fig 3** | Relationship, dose–response, or regression with a fitted model and CI band | Establish the mechanism *or* the practical response curve |
| **Table 3** | Economic or practical analysis: gross margin, partial budget, water/fertiliser use efficiency | This is what makes it agronomy rather than agronomic botany |
| **Fig 4** *(optional)* | Conceptual or systems diagram of the recommendation | Strongly raises citation rate for extension-facing papers |

**Every table must have:** units in every column heading, the number of observations, the statistical test used, and footnote definitions for every abbreviation.

---

## 4. Panel-Level Craft

### Graphs
- Show individual data points for n ≤ ~15 (dot plot, box + points, or violin). A bar chart of 3 replicates hides everything that matters.
- Error bars: define as SD, SE, or 95% CI **in the legend**. Prefer CI — it is directly interpretable.
- Sample size in every legend. State whether n is biological or technical.
- Lowercase bold panel letters `(a) (b) (c)` in the top-left of each panel.
- Use the same symbol/colour for the same entity across all figures in the paper.
- Do not use colour alone to convey meaning; distinguish by shape or linetype as well (colour-blind safety).
- Axes: units in parentheses after the axis title. Scale marks inside the axes. Font 8–10 pt at final printed size.

### Micrographs
- Scale bar in **every** panel, with the length indicated.
- Identical exposure, gain, and processing within any comparison.
- State the imaging modality, objective, and any deconvolution or adjustment software in Methods.
- If panels come from different sessions, say so.

### Blots and gels (Western, Northern, semi-quant)
- Show the relevant band region **with surrounding context**, not a tight crop.
- Clearly demarcate any splicing with vertical lines.
- Report the loading control in the same figure.
- Uncropped scans **must** be deposited as supplementary material at most venues.
- Quantify across ≥3 biological replicates; a single representative blot is not evidence.

### Schematics and model figures
- Draw with vector tools, not raster screenshots of slides.
- Solid arrows = demonstrated in this work; dashed = inferred or from literature. Say which in the legend.
- Label every component. Include a minimal key.
- Keep the model honest: if an arrow rests on one allele and one assay, dashed is the correct choice.

### Graphical abstract (where required)
- Any of: `[practice/ˈɡenotype] [effect] on [trait] under [conditions]`
- Must depict the **biological or agronomic consequence**, not merely the molecular signal. Panels showing only expression changes or protein interactions are a common rejection trigger for the graphical abstract specifically.
- Readable at social-media thumbnail size: minimal text, large fonts, landscape orientation.

---

## 5. Section ↔ Figure Mapping Table

Complete this before writing. It is the single most useful planning artefact for a biology paper.

| Fig/Table | Logical step | Evidence level | Supports which Results subsection | Appears in which Discussion paragraph | Claim in abstract? |
| --- | --- | --- | --- | --- | --- |
| Fig 1 | Context | — | [ ] | [ ] | [ ] |
| Fig 2 | Discovery | L0 | [ ] | [ ] | [ ] |
| Fig 3 | Pattern | L0 | [ ] | [ ] | [ ] |
| Fig 4 | Necessity | L1 | [ ] | [ ] | [ ] |
| Fig 5 | Sufficiency | L2 | [ ] | [ ] | [ ] |
| Fig 6 | Mechanism | L4 | [ ] | [ ] | [ ] |
| Fig 7 | Order/specificity | L3–L5 | [ ] | [ ] | [ ] |
| Fig 8 | Model | — | [ ] | [ ] | [ ] |
| Table 1 | Site/soil/weather | — | [ ] | [ ] | — |
| Table 2 | ANOVA | — | [ ] | [ ] | — |
| Table 3 | Economics | — | [ ] | [ ] | [ ] |

**Checks this table reveals instantly:**
- A figure supporting no Discussion paragraph → either the figure is unnecessary or the Discussion is incomplete.
- A Discussion paragraph citing no figure → it is speculation and should be marked as such.
- An abstract claim appearing in no figure row → overclaim. Fix it.

---

## 6. Figure Legend Template

```
Fig. N. [First sentence — the conclusion this figure demonstrates, standalone
and quantitative.] [Second and third sentences — what each panel shows.]
[Experimental conditions, species, tissue, timepoint.] [Statistical test,
definition of error bars, n, biological vs technical replicates.] [Scale bar
length for micrographs.] [Abbreviation definitions.]
```

**Worked example:**

> **Fig. 4.** Loss of *ABC1* reduces seed set in *Arabidopsis*. **(a)** Silique length and **(b)** seeds per silique in wild type (Col-0), *abc1-1* and *abc1-2* (n = 30 plants per genotype, three independent experiments). **(c)** Developing seeds at 8 days after pollination; scale bars, 500 µm. Boxes show median and interquartile range; whiskers extend to 1.5× IQR; individual points are shown. Asterisks indicate significant differences from Col-0 (two-way ANOVA with Tukey's HSD correction; \*\*\*P < 0.001; exact P values in Supplementary Table 3). DAP, days after pollination; WT, wild type.

Note what the first sentence does: a reader who reads only that sentence still learns the finding.

---

## 7. Pre-Submission Figure Audit

- [ ] Each figure is cited in the text in numerical order
- [ ] Each panel is cited at least once in the text
- [ ] Legends stand alone — readable without the main text
- [ ] n stated in every legend, with biological/technical distinction
- [ ] Error bar definition in every legend
- [ ] Statistical test named in every legend that shows a comparison
- [ ] Scale bars in every micrograph
- [ ] Panel letters consistent (lowercase bold, top-left)
- [ ] Same symbol/colour for the same entity across all figures
- [ ] Font size legible at final printed size
- [ ] Resolution meets the venue minimum (typically 300 dpi raster, vector preferred for graphs and schematics)
- [ ] Uncropped blots/gels deposited as supplementary
- [ ] No duplicated, mirrored, or recombined panels anywhere in the paper or its supplements
- [ ] No selective brightness/contrast adjustment within a comparison
- [ ] Colour-blind safe
- [ ] Ethics: no identifying information in field photos or human-subject imagery
